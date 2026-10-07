"""Tempo, fase y mapa de compases de un tema: lo necesario para calzarlo a la grilla del video.

Uso:
  beat_phase.py TEMA.wav [--seconds 90]

Imprime:
  - BPM refinado (regresión sobre los beats; el tempo crudo de librosa viene cuantizado).
  - Fase del beat medida en TRANSITORIOS por banda (kick / medios / hats). No uses los
    tiempos de beat_track para la fase: salen ~0.1-0.2 s antes del golpe real.
  - Mapa por compás (energía en 4 bandas + novedad): las secciones (break, drop,
    estribillo, outro) son los saltos de novedad.
  - El golpe final: el último pico fuerte seguido de caída sostenida.
"""

import argparse
import subprocess
import warnings

import numpy as np
from scipy import signal

warnings.filterwarnings("ignore")
SR = 44100


def load(path, seconds=None):
    cmd = ["ffmpeg", "-v", "error", "-i", path, "-ac", "1", "-ar", str(SR), "-f", "f32le", "-"]
    x = np.frombuffer(subprocess.run(cmd, capture_output=True, check=True).stdout, dtype="<f4").astype(float)
    return x[: int(SR * seconds)] if seconds else x


def transients(x, lo, hi):
    sos = signal.butter(4, [lo, hi], "band", fs=SR, output="sos")
    env = np.abs(signal.hilbert(signal.sosfiltfilt(sos, x)))
    env = signal.savgol_filter(env, int(SR * 0.004) | 1, 2)
    d = np.clip(np.diff(env, prepend=env[0]), 0, None)
    pk, _ = signal.find_peaks(d, distance=int(SR * 0.2), height=np.percentile(d, 99.7))
    return pk / SR


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("audio")
    ap.add_argument("--seconds", type=float, default=90, help="cuánto analizar para tempo/fase")
    a = ap.parse_args()

    import librosa

    full = load(a.audio)
    x = full[: int(SR * a.seconds)]
    _, beats = librosa.beat.beat_track(y=librosa.resample(x, orig_sr=SR, target_sr=22050), sr=22050, units="time")
    k = np.arange(len(beats))
    period, _ = np.linalg.lstsq(np.vstack([k, np.ones_like(k)]).T, beats, rcond=None)[0]
    bpm = 60 / period
    print(f"BPM ≈ {bpm:.2f}  (beat = {period:.4f} s)  · duración {len(full) / SR:.2f} s")

    best = None
    for name, (lo, hi) in {"kick 30-120 Hz": (30, 120), "medios 1-4 kHz": (1000, 4000), "hats 6-12 kHz": (6000, 12000)}.items():
        t = transients(x, lo, hi)
        if len(t) < 6:
            print(f"  {name:16s} pocos golpes ({len(t)})")
            continue
        ph = t % period
        hist, edges = np.histogram(ph, bins=40, range=(0, period))
        mode = (edges[np.argmax(hist)] + edges[np.argmax(hist) + 1]) / 2
        share = hist.max() / len(t)
        print(f"  {name:16s} {len(t):4d} golpes · fase {mode:.3f} s · {share:.0%} en la moda · ej: "
              + " ".join(f"{v:.3f}" for v in t[(t > 4)][:6]))
        if name.startswith("kick") and len(t) >= 8:
            best = mode
        if best is None and share > 0.4:
            best = mode
    if best is None:
        best = beats[0] % period
    print(f"→ fase recomendada: beats en {best:.3f} + {period:.4f}·k  (verificá a ojo en el mapa)")

    bar = 4 * period
    print("\ncompás  t0      sub   low   mid  high  novedad")
    sos = {b: signal.butter(4, r, "band", fs=SR, output="sos") for b, r in
           {"sub": (20, 120), "low": (120, 500), "mid": (500, 2500), "high": (2500, 11000)}.items()}
    bands = {b: signal.sosfilt(s, full) ** 2 for b, s in sos.items()}
    prev = None
    t0 = best % bar
    n = 0
    while t0 + bar <= len(full) / SR:
        i, j = int(t0 * SR), int((t0 + bar) * SR)
        v = np.array([10 * np.log10(bands[b][i:j].mean() + 1e-12) for b in bands])
        nov = "" if prev is None else f"{np.sqrt(np.mean((v - prev) ** 2)):6.1f}" + ("  ◀" if np.sqrt(np.mean((v - prev) ** 2)) > 3 else "")
        print(f"{n:5d} {t0:7.2f} " + " ".join(f"{q:5.1f}" for q in v) + nov)
        prev, t0, n = v, t0 + bar, n + 1

    # golpe final = la caída sostenida más grande de los últimos 25 s (2 s de groove antes vs 2 s
    # después), refinada al pico local: ahí cae el último downbeat antes del ring-out
    win = int(SR * 0.05)
    rms = 20 * np.log10(np.sqrt(np.convolve(full**2, np.ones(win) / win, "same")[::win]) + 1e-9)
    tt = np.arange(len(rms)) * 0.05
    groove = np.median(rms[rms > rms.max() - 40])
    best_drop, final = 0.0, None
    for i in np.where(tt > tt[-1] - 25)[0]:
        if i < 40 or i + 42 > len(rms):
            continue
        before = rms[i - 40 : i].mean()
        if before < groove - 3:  # lo de antes tiene que ser groove, no la cola del ring-out
            continue
        drop = before - rms[i + 2 : i + 42].mean()
        if drop > best_drop:
            best_drop, final = drop, i
    if final is not None and best_drop >= 5:
        # la curva de caída es una meseta: el golpe es el borde del acantilado más empinado cerca de ella
        lo, hi = max(0, final - 30), min(len(rms) - 4, final + 30)
        cliff = [rms[j] - rms[j + 1 : j + 4].mean() for j in range(lo, hi)]
        j = lo + int(np.argmax(cliff))
        snap = best + round((tt[j] - best) / period) * period
        print(f"\ngolpe final ≈ {tt[j]:.2f} s → en la grilla {snap:.3f} s  (caída de {best_drop:.1f} dB después)")
    else:
        print("\ngolpe final: no detectado (¿termina en fade?)")

if __name__ == "__main__":
    main()
