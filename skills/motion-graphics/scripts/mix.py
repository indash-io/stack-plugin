"""Ducking de la música bajo la voz y medición de la mezcla antes y después del render.

  mix.py duck --music music.wav --vo vo.wav --db 8 --out music.wav
      → baja la música N dB mientras hay voz (gate -40 dBFS, hold 0.25 s, ataque 80 ms,
        release 400 ms). Corré esto DESPUÉS de vo_fit: el duck sigue la voz calzada.
  mix.py measure --stem vo.wav:0.9 --stem music.wav:0.75 --stem sfx.wav:0.55
      → suma los stems con sus data-volume (lineales, como los aplica HyperFrames) y mide.
        Sirve para ajustar volúmenes sin renderizar.
  mix.py measure --file renders/draft.mp4
      → mide el render real. Es la medición que vale para entregar.

Objetivo: -14 LUFS integrados (±1). True peak ≤ -1.5 dBTP en los stems, ≤ -1.0 en el render:
HyperFrames suma los stems lineal (data-volume = ganancia lineal) y, si el AAC pasa de -1 dBTP,
baja la mezcla ENTERA hasta entrar. Sin margen en los stems, el render sale más bajo de lo medido.
"""

import argparse
import os
import re
import subprocess
import tempfile
import wave

import numpy as np

SR = 48000


def load(path):
    cmd = ["ffmpeg", "-v", "error", "-i", path, "-ac", "2", "-ar", str(SR), "-f", "f32le", "-"]
    return np.frombuffer(subprocess.run(cmd, capture_output=True, check=True).stdout, dtype="<f4").reshape(-1, 2).astype(float)


def write(path, x):
    with wave.open(path, "wb") as w:
        w.setnchannels(2)
        w.setsampwidth(2)
        w.setframerate(SR)
        w.writeframes((np.clip(x, -1, 1) * 32767).astype("<i2").tobytes())


def duck(a):
    music, vo = load(a.music), load(a.vo).mean(1)
    n = len(music)
    vo = np.pad(vo, (0, max(0, n - len(vo))))[:n]
    win = int(SR * 0.02)
    rms = np.sqrt(np.convolve(vo**2, np.ones(win) / win, "same"))
    gate = np.convolve((rms > 10 ** (-40 / 20)).astype(float), np.ones(int(SR * 0.25)), "same") > 0
    g, y = np.zeros(n), 0.0
    att, rel = np.exp(-1 / (SR * 0.08)), np.exp(-1 / (SR * 0.4))
    for i in range(0, n, 64):
        tgt = float(gate[i])
        y = tgt + (y - tgt) * (att if tgt > y else rel) ** 64
        g[i : i + 64] = y
    write(a.out, music * 10 ** (-a.db * g / 20)[:, None])
    print(f"{a.out}: música -{a.db:g} dB bajo la voz ({gate.mean():.0%} del tiempo con voz)")


def measure(a):
    if a.file:
        src = ["-i", a.file]
    else:
        stems = [(p, float(v)) for p, v in (s.rsplit(":", 1) for s in a.stem)]
        xs = [load(p) * v for p, v in stems]
        n = max(len(x) for x in xs)
        mix = sum(np.pad(x, ((0, n - len(x)), (0, 0))) for x in xs)
        tmp = a.out or os.path.join(tempfile.mkdtemp(), "mix.wav")
        write(tmp, mix)
        src = ["-i", tmp]
    err = subprocess.run(["ffmpeg", "-nostats", *src, "-af", "ebur128=peak=true", "-f", "null", "-"], capture_output=True, text=True).stderr
    summary = err[err.rfind("Summary:") :]
    lufs = float(re.search(r"I:\s+(-?[\d.]+) LUFS", summary).group(1))
    tp = float(re.search(r"Peak:\s+(-?[\d.]+) dBFS", summary).group(1))
    tp_max = -1.0 if a.file else -1.5
    ok = abs(lufs + 14) <= 1 and tp <= tp_max
    print(f"integrado {lufs:.1f} LUFS · true peak {tp:.1f} dBTP → " + ("OK" if ok else f"FUERA (objetivo -14 ±1 LUFS, TP ≤ {tp_max})"))
    if not ok and not a.file:
        print(f"  escalá todos los data-volume ×{10 ** ((-14 - lufs) / 20):.2f}" + ("  (y bajá picos: el TP no entra)" if tp + (-14 - lufs) > tp_max else ""))


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    d = sub.add_parser("duck")
    d.add_argument("--music", required=True)
    d.add_argument("--vo", required=True)
    d.add_argument("--db", type=float, default=8.0)
    d.add_argument("--out", required=True)
    m = sub.add_parser("measure")
    m.add_argument("--stem", action="append", default=[], help="ruta.wav:data-volume")
    m.add_argument("--file", default=None)
    m.add_argument("--out", default=None, help="guardar la suma de stems")
    a = ap.parse_args()
    duck(a) if a.cmd == "duck" else measure(a)


if __name__ == "__main__":
    main()
