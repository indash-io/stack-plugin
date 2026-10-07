"""Calza un tema a la grilla del video: segmentos cortados en compás, empalmes, y (opcional)
el gag de "música de espera" telefónica con tape-stop.

Uso:
  music_conform.py --track TEMA.wav --out music.wav --duration 30 \
      --seg 0:30:6.0                      # video 0-30 = tema desde 6.0 (un solo tramo)
      [--seg 20:39:114.366 ...]           # más tramos: video_desde:video_hasta:tema_en_video_desde
      [--atempo 1.021]                    # estira el tema ANTES de cortar (tiempos del tema ya estirados)
      [--hold 0:7.42]                     # ese tramo suena por teléfono, se acelera y frena en seco
      [--xfade 0.025] [--fade-out 0.6]

Reglas que hace cumplir:
  - Empalmes con crossfade corto justo ANTES del downbeat (el golpe queda intacto).
  - Fade-in de 30 ms en el frame 0: un arranque a nivel pleno hace que el AAC del render
    pase de -1 dBTP y el render de HyperFrames falla (audioPadTrim).
"""

import argparse
import subprocess
import wave

import numpy as np
from scipy import signal

SR = 48000


def load(path, atempo=None):
    af = ["-af", f"atempo={atempo}"] if atempo else []
    cmd = ["ffmpeg", "-v", "error", "-i", path, *af, "-ac", "2", "-ar", str(SR), "-f", "f32le", "-"]
    return np.frombuffer(subprocess.run(cmd, capture_output=True, check=True).stdout, dtype="<f4").reshape(-1, 2).astype(float)


def bp(x, lo, hi, order=4):
    return signal.sosfilt(signal.butter(order, [lo, hi], "band", fs=SR, output="sos"), x)


def phone_hold(track, t_from_track, dur, stop=0.42):
    """Música de espera: banda telefónica, crujido, se acelera con la tensión y frena (tape-stop)."""
    n = int(SR * (dur + stop))
    tt = np.arange(n) / SR
    rate = 1 + 0.13 * (np.minimum(tt, dur) / dur) ** 2
    k = tt > dur
    rate[k] = 1.13 * (1 - (tt[k] - dur) / stop).clip(0, 1) ** 1.6
    mono = track.mean(1)
    x = np.interp(t_from_track * SR + np.cumsum(rate), np.arange(len(mono)), mono)
    x = np.tanh(bp(x, 340, 3300) * 1.8)
    x = np.round(x * 40) / 40
    x = bp(x[(np.arange(n) // 6) * 6], 300, 3400, 2)
    x[-int(SR * 0.05):] *= np.linspace(1, 0, int(SR * 0.05))
    return np.stack([x, x], 1) * 0.55


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--track", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--duration", type=float, required=True)
    ap.add_argument("--seg", action="append", required=True, help="video_desde:video_hasta:tema_en_video_desde")
    ap.add_argument("--atempo", type=float, default=None)
    ap.add_argument("--hold", default=None, help="desde:hasta (segundos de video) con tratamiento telefónico")
    ap.add_argument("--xfade", type=float, default=0.025)
    ap.add_argument("--fade-out", type=float, default=0.6)
    a = ap.parse_args()

    track = load(a.track, a.atempo)
    out = np.zeros((int(SR * a.duration), 2))
    segs = sorted(tuple(map(float, s.split(":"))) for s in a.seg)
    xf = int(SR * a.xfade)
    hold = tuple(map(float, a.hold.split(":"))) if a.hold else None
    for i, (v0, v1, t0) in enumerate(segs):
        if hold and v0 < hold[1]:
            # el tramo arranca con la versión telefónica; el tema "real" entra recién al terminar el hold + tape-stop
            h = phone_hold(track, t0 + (hold[0] - v0), hold[1] - hold[0])
            a0 = int(SR * hold[0])
            out[a0 : a0 + len(h)] += h[: len(out) - a0]
            gap_end = hold[1] + 0.58  # 0.42 de tape-stop + un respiro antes del downbeat siguiente
            t0, v0 = t0 + (gap_end - v0), gap_end
        a_ = int(SR * v0) - (xf if i else 0)
        b_ = int(SR * v1)
        s0 = int(SR * t0) - (xf if i else 0)
        seg = track[s0 : s0 + (b_ - a_)].copy()
        if i:
            seg[:xf] *= np.linspace(0, 1, xf)[:, None]
        if i + 1 < len(segs):
            nxt = int(SR * segs[i + 1][0]) - a_
            seg[nxt - xf : nxt] *= np.linspace(1, 0, xf)[:, None]
            seg[nxt:] = 0
        out[a_ : a_ + len(seg)] += seg
    fi = int(SR * 0.03)
    out[:fi] *= np.linspace(0, 1, fi)[:, None]
    fo = int(SR * a.fade_out)
    if fo:
        out[-fo:] *= np.linspace(1, 0, fo)[:, None] ** 2
    ceil = 10 ** (-1 / 20)  # los temas de stock vienen masterizados a 0 dBFS: techo suave para no clipear
    out = np.tanh(out / ceil) * ceil
    with wave.open(a.out, "wb") as w:
        w.setnchannels(2)
        w.setsampwidth(2)
        w.setframerate(SR)
        w.writeframes((np.clip(out, -1, 1) * 32767).astype("<i2").tobytes())
    print(f"{a.out}: {a.duration:.2f} s, {len(segs)} tramo(s)" + (f", hold telefónico {a.hold}" if hold else ""))


if __name__ == "__main__":
    main()
