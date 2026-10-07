"""Calza una toma de locución (una sola lectura continua) a los cortes del video, línea por línea.

Paso 1 — dónde está cada línea en la toma:
  vo_fit.py segments TOMA.wav
    → imprime los tramos de habla entre silencios. Agrupalos en las líneas del guion
      (transcribí la toma con `npx hyperframes transcribe TOMA.wav -l es` para saber qué
      palabra cae en qué tramo).

Paso 2 — calzar:
  vo_fit.py fit --take TOMA.wav --lines lines.json --duration 30 --out vo.wav [--tempo 1.0]
    lines.json = [{"start": 0.256, "end": 2.642, "target": 0.3}, ...]   (start/end en la toma,
    target = segundo del video donde debe arrancar)
    → cada línea arranca en max(target, fin de la anterior + 0.12 s); las pausas internas
      se acortan a 0.30 s; --tempo (≤1.08) acelera sin cambiar el tono si algo llega tarde.
    → cadena de voz: HP 85 Hz, compresión 3:1 sobre -26 dBFS, normalizada a -14 LUFS medida en
      estéreo (el nivel de la voz en la mezcla aprobada de referencia), techo suave en -1.5 dBFS.
      Sale ESTÉREO: un WAV mono el render lo duplica a ambos canales y suena +3 dB más fuerte
      de lo que mediste.
    → imprime el horario real de cada línea ("tarde +0.35" si no llegó a su corte).
"""

import argparse
import json
import re
import subprocess
import wave

import numpy as np
from scipy import signal

SR = 48000
GAP, CAP, TAIL = 0.12, 0.30, 0.09


def load(path):
    cmd = ["ffmpeg", "-v", "error", "-i", path, "-ac", "1", "-ar", str(SR), "-f", "f32le", "-"]
    return np.frombuffer(subprocess.run(cmd, capture_output=True, check=True).stdout, dtype="<f4").astype(float)


def segments(path, noise=-42, d=0.09):
    err = subprocess.run(["ffmpeg", "-nostats", "-i", path, "-af", f"silencedetect=noise={noise}dB:d={d}", "-f", "null", "-"],
                         capture_output=True, text=True).stderr
    starts = [float(v) for v in re.findall(r"silence_start: ([\d.]+)", err)]
    ends = [float(v) for v in re.findall(r"silence_end: ([\d.]+)", err)]
    dur = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", path],
                               capture_output=True, text=True).stdout)
    edges = sorted([(0.0, "s")] + [(s, "e") for s in starts] + [(e, "s") for e in ends] + [(dur, "e")])
    speech, cur = [], None
    for t, kind in edges:
        if kind == "s":
            cur = t
        elif cur is not None and t - cur > 0.05:
            speech.append((round(cur, 3), round(t, 3)))
            cur = None
    return speech


def squeeze(x, thresh_db=-42):
    win = int(SR * 0.01)
    quiet = np.sqrt(np.convolve(x**2, np.ones(win) / win, "same")) < 10 ** (thresh_db / 20)
    keep, i, k, n = [], 0, 0, len(x)
    while k < n:
        if quiet[k]:
            j = k
            while j < n and quiet[j]:
                j += 1
            if (j - k) / SR > CAP and 0 < k and j < n:
                h = int(SR * CAP / 2)
                keep.append(x[i : k + h])
                i = j - h
            k = j
        else:
            k += 1
    keep.append(x[i:])
    y, xf = keep[0], int(SR * 0.02)
    for seg in keep[1:]:
        r = np.linspace(0, 1, xf)
        y = np.concatenate([y[:-xf], y[-xf:] * (1 - r) + seg[:xf] * r, seg[xf:]]) if len(y) > xf and len(seg) > xf else np.concatenate([y, seg])
    return y


def stretch(x, tempo):
    if abs(tempo - 1) < 1e-3:
        return x
    raw = subprocess.run(["ffmpeg", "-v", "error", "-f", "f32le", "-ar", str(SR), "-ac", "1", "-i", "-", "-af", f"atempo={tempo}",
                          "-f", "f32le", "-"], input=x.astype("<f4").tobytes(), capture_output=True, check=True).stdout
    return np.frombuffer(raw, dtype="<f4").astype(float)


def lufs(x):
    st = np.stack([x, x], 1)
    r = subprocess.run(["ffmpeg", "-nostats", "-f", "s16le", "-ar", str(SR), "-ac", "2", "-i", "-", "-af", "ebur128", "-f", "null", "-"],
                       input=(np.clip(st, -1, 1) * 32767).astype("<i2").tobytes(), capture_output=True)
    return float([l for l in r.stderr.decode().splitlines() if l.strip().startswith("I:")][-1].split()[1])


def chain(vo, target=-14.0):
    vo = signal.sosfilt(signal.butter(2, 85, "hp", fs=SR, output="sos"), vo)
    win = int(SR * 0.03)
    lvl = 20 * np.log10(np.sqrt(np.convolve(vo**2, np.ones(win) / win, "same")) + 1e-9)
    gdb = np.where(lvl > -26, (-26 + (lvl + 26) / 3) - lvl, 0.0)
    vo = vo * 10 ** (signal.savgol_filter(gdb, int(SR * 0.04) | 1, 2) / 20)
    vo = vo * 10 ** ((target - lufs(vo)) / 20)
    ceil = 10 ** (-1.5 / 20)
    return np.tanh(vo / ceil) * ceil


def fit(a):
    x = load(a.take)
    lines = json.load(open(a.lines))
    out = np.zeros(int(SR * a.duration))
    t = 0.0
    for n, ln in enumerate(lines, 1):
        s0, s1 = int(SR * max(0, ln["start"] - 0.03)), int(SR * (ln["end"] + TAIL))
        seg = stretch(squeeze(x[s0:s1]), a.tempo)
        f, g = int(SR * 0.012), int(SR * 0.06)
        seg[:f] *= np.linspace(0, 1, f)
        seg[-g:] *= np.linspace(1, 0, g)
        start = max(ln["target"], t + GAP)
        i = int(SR * start)
        j = min(len(out), i + len(seg))
        out[i:j] += seg[: j - i]
        t = start + len(seg) / SR
        late = start - ln["target"]
        print(f"L{n:<2} objetivo {ln['target']:6.2f}  arranca {start:6.2f}  termina {t:6.2f}" + (f"   tarde {late:+.2f}" if late > 0.05 else ""))
    if t > a.duration - 0.15:
        print("!! la última línea se pasa del final: subí --tempo (máx 1.08) o mové objetivos")
    out = chain(out)
    st = np.stack([out, out], 1)
    with wave.open(a.out, "wb") as w:
        w.setnchannels(2)
        w.setsampwidth(2)
        w.setframerate(SR)
        w.writeframes((np.clip(st, -1, 1) * 32767).astype("<i2").tobytes())
    print(f"{a.out} escrito · voz a {lufs(out):.1f} LUFS")


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("segments")
    s.add_argument("take")
    f = sub.add_parser("fit")
    f.add_argument("--take", required=True)
    f.add_argument("--lines", required=True)
    f.add_argument("--duration", type=float, required=True)
    f.add_argument("--out", required=True)
    f.add_argument("--tempo", type=float, default=1.0)
    a = ap.parse_args()
    if a.cmd == "segments":
        for k, (s0, s1) in enumerate(segments(a.take), 1):
            print(f"{k:3d}  {s0:7.3f} → {s1:7.3f}   ({s1 - s0:4.2f} s)")
    else:
        fit(a)


if __name__ == "__main__":
    main()
