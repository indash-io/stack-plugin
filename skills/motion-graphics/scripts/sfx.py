"""SFX sintetizados y deterministas, renderizados desde una lista de cues.

  sfx.py list                                       → los efectos disponibles y sus parámetros
  sfx.py render cues.json --duration 30 --out sfx.wav

cues.json = [{"t": 10.35, "fx": "whoosh", "level": 0.35, "pan": 0, "args": {"dur": 0.4, "up": true}}, ...]
  t      segundo del video (poné el cue en el frame del movimiento, no "cerca")
  level  0-1 (default 1) · pan -1..1 (default 0, solo efectos mono)
  args   parámetros propios del efecto (ver `list`)

Sale estéreo, con HP en 30 Hz y pico en -4 dBFS: el nivel final lo da data-volume en el HTML.
"""

import argparse
import inspect
import json
import wave

import numpy as np
from scipy import signal

SR = 48000
rng = np.random.default_rng(20261002)


def T(dur):
    return np.arange(int(SR * dur)) / SR


def noise(dur):
    return rng.standard_normal(int(SR * dur))


def _f(kind, fc, order=2):
    return signal.butter(order, fc, kind, fs=SR, output="sos")


def lp(x, fc, order=2):
    return signal.sosfilt(_f("lp", min(fc, SR * 0.45), order), x, axis=0)


def hp(x, fc, order=2):
    return signal.sosfilt(_f("hp", fc, order), x, axis=0)


def bp(x, lo, hi, order=2):
    return signal.sosfilt(_f("band", [lo, hi], order), x, axis=0)


def sweep_bp(x, f0, f1, q=1.2, block=256, curve=2.0):
    """Pasabanda cuyo centro se desliza f0 → f1."""
    out, zi, nb = np.zeros_like(x), None, int(np.ceil(len(x) / block))
    for b in range(nb):
        fc = f0 * (f1 / f0) ** ((b / max(1, nb - 1)) ** curve)
        sos = _f("band", [max(20, fc / (1 + 1 / (2 * q))), min(SR * 0.45, fc * (1 + 1 / (2 * q)))], 1)
        zi = np.zeros((sos.shape[0], 2)) if zi is None else zi
        out[b * block : (b + 1) * block], zi = signal.sosfilt(sos, x[b * block : (b + 1) * block], zi=zi)
    return out


def _ir(rt=2.4, dur=3.2, tone=5200):
    ir = lp(np.stack([noise(dur), noise(dur)], 1) * np.exp(-6.9 * T(dur) / rt)[:, None], tone)
    ir[: int(SR * 0.012)] *= np.linspace(0, 1, int(SR * 0.012))[:, None]
    return ir / np.sqrt(np.sum(ir**2) / 2)


IR = _ir()


def verb(st, wet=0.25):
    return np.stack([signal.fftconvolve(st[:, c], IR[:, c])[: len(st)] for c in range(2)], 1) * wet


def st(x):
    return np.stack([x, x], 1)


def place(dst, x, t, gain=1.0, pan=0.0):
    if x.ndim == 1:
        a = (pan + 1) * np.pi / 4
        x = np.stack([x * np.cos(a), x * np.sin(a)], 1) * np.sqrt(2)
    i = int(round(t * SR))
    s, j = max(0, -i), min(len(dst), i + len(x))
    if j > i + s:
        dst[i + s : j] += gain * x[s : j - i]


# ------------------------------------------------------------------ movimiento
def whoosh(dur=0.45, up=True):
    """Paso rápido de un objeto o de cámara. up=False para lo que cae o se va."""
    f0, f1 = (500, 4200) if up else (4200, 400)
    x = sweep_bp(noise(dur), f0, f1, q=1.1, curve=1.0) * 2.2 * np.sin(np.pi * T(dur) / dur) ** 1.6
    return np.stack([x * 0.9, np.roll(x, 60)], 1)


def swish(dur=0.28, up=True):
    """Whoosh corto y fino: push entre pantallas, card que entra."""
    f0, f1 = (1200, 5200) if up else (5200, 1200)
    return sweep_bp(noise(dur), f0, f1, q=1.0, curve=1.0) * 1.6 * np.sin(np.pi * T(dur) / dur) ** 1.5


def riser(dur=1.0, f0=300, f1=5200):
    """Tensión que sube hasta un corte o un drop. Terminalo EN el downbeat."""
    t = T(dur)
    tone = np.sin(2 * np.pi * np.cumsum(110 * 8 ** ((t / dur) ** 1.5)) / SR) * 0.18
    x = (sweep_bp(noise(dur), f0, f1, q=1.4, curve=1.4) * 1.6 + tone) * (t / dur) ** 2.2
    return np.stack([x, np.roll(x, 90)], 1)


def air_swell(dur=0.55):
    """Respiro suave hacia un corte (el reemplazo amable del whoosh en piezas relajadas)."""
    t = T(dur)
    x = sweep_bp(noise(dur), 900, 3600, q=0.9, curve=1.0) * (t / dur) ** 2.4 * np.minimum(1, (dur - t) / 0.03).clip(0, 1)
    return np.stack([x, np.roll(x, 120)], 1) * 0.5


def rustle(dur=0.8):
    """Papel, sobres, tarjetas que se mueven."""
    t = T(dur)
    x = bp(noise(dur), 1800, 7000) * (0.4 + 0.6 * np.abs(np.sin(2 * np.pi * 9 * t + 3 * np.sin(2 * np.pi * 2.3 * t))))
    return x * np.sin(np.pi * t / dur) * 0.22


# ------------------------------------------------------------------ golpes
def sub_boom(dur=2.2, f0=62, f1=30):
    t = T(dur)
    return np.tanh(np.sin(2 * np.pi * np.cumsum(f1 + (f0 - f1) * np.exp(-t * 3.5)) / SR) * np.exp(-t * 2.2) * 1.4)


def impact():
    """El golpe grande (logo que aterriza, reveal final). Uno o dos por pieza."""
    t = T(2.6)
    x = sub_boom(2.6, 70, 30) * 0.55 + lp(noise(2.6), 5200) * np.exp(-t * 9) * 0.6 + hp(noise(2.6), 3000) * np.exp(-t * 3.2) * 0.16
    return st(x) + verb(st(x), 0.35)


def hit():
    """Golpe de corte en downbeat."""
    t = T(0.9)
    x = sub_boom(0.9, 95, 42) * 0.45 + lp(noise(0.9), 3200) * np.exp(-t * 22) * 0.4
    return st(x) + verb(st(x), 0.2)


def thud():
    """Algo que apoya o cae: una card que asienta, un objeto contra el piso."""
    t = T(0.5)
    return sub_boom(0.5, 120, 55) * 0.8 + lp(noise(0.5), 900) * np.exp(-t * 30) * 0.4


# ------------------------------------------------------------------ UI
def click(tone=2600):
    """Tap de dedo en un botón."""
    t = T(0.05)
    return (bp(noise(0.05), tone * 0.6, tone * 1.6) * np.exp(-t * 260) + np.sin(2 * np.pi * 180 * t) * np.exp(-t * 120) * 0.4) * 0.6


def pop(f=900):
    """Algo que aparece (check, badge, pop-out)."""
    t = T(0.09)
    return np.sin(2 * np.pi * np.cumsum(f * (1 + 0.8 * np.exp(-t * 60))) / SR) * np.exp(-t * 55) * 0.35


def tick(f=5200):
    """Reloj, contador, ráfaga de items (de a muchos, separados ≥ 12 ms)."""
    t = T(0.018)
    return np.sin(2 * np.pi * f * t) * np.exp(-t * 420) * 0.35


def blip(f=1760, dur=0.28):
    """Notificación corta."""
    t = T(dur)
    return (np.sin(2 * np.pi * f * t) + 0.3 * np.sin(4 * np.pi * f * t)) * np.exp(-t * 18) * np.minimum(1, t / 0.002) * 0.4


def chime(f=1318.5, dur=1.2):
    """Confirmación / éxito. Afinalo a la tonalidad del tema si se puede."""
    t = T(dur)
    x = sum(a * np.sin(2 * np.pi * f * h * t) * np.exp(-t * d) for h, a, d in ((1, 1.0, 5), (2.0, 0.35, 8), (3.01, 0.15, 12)))
    return st(x) * 0.3 + verb(st(x) * 0.3, 0.3)


def sparkle(n=9):
    """Brillo: algo premium que aparece (tarjeta, logo)."""
    out = np.zeros((int(SR * 0.9), 2))
    for k in range(n):
        place(out, blip(2093 * 2 ** ((k * 5 % 12) / 12), 0.25) * 0.5, k * 0.045 + 0.01 * (k % 3), pan=-0.7 + 1.4 * (k % 5) / 4)
    return out + verb(out, 0.4)


def glass(dur=0.6):
    """Reflejo que barre una superficie (glint)."""
    x = sweep_bp(noise(dur), 3000, 10000, q=3.0, curve=1.0) * np.sin(np.pi * T(dur) / dur) ** 2
    return np.stack([x, np.roll(x, 200)], 1) * 0.5


def vibrate(dur=0.35):
    """Celular vibrando sobre una mesa."""
    t = T(dur)
    x = lp(np.sign(np.sin(2 * np.pi * 150 * t)), 700) * (0.65 + 0.35 * np.sin(2 * np.pi * 26 * t))
    return x * np.minimum(1, t / 0.02) * (1 - t / dur) * 0.22


# ------------------------------------------------------------------ cartoon (con medida)
def boing(f0=170, f1=560):
    """Rebote, algo que se estira o salta. Humor: no más de dos por pieza."""
    t = T(0.45)
    fr = f0 + (f1 - f0) * (1 - np.exp(-t * 18)) + 40 * np.sin(2 * np.pi * 18 * t) * np.exp(-t * 6)
    return np.sin(2 * np.pi * np.cumsum(fr) / SR) * np.exp(-t * 7) * 0.35


def zap(dur=0.9):
    """Barrido ascendente electrónico (algo que se carga o se activa)."""
    t = T(dur)
    x = np.sin(2 * np.pi * np.cumsum(220 * 12 ** (t / dur)) / SR) * np.sin(np.pi * t / dur) ** 1.2
    return x * 0.22 + hp(noise(dur), 5000) * (t / dur) * 0.05


FX = {f.__name__: f for f in (whoosh, swish, riser, air_swell, rustle, impact, hit, thud, sub_boom,
                              click, pop, tick, blip, chime, sparkle, glass, vibrate, boing, zap)}


def render(cues, duration):
    out = np.zeros((int(SR * duration), 2))
    for c in cues:
        place(out, FX[c["fx"]](**c.get("args", {})), c["t"], c.get("level", 1.0), c.get("pan", 0.0))
    out = hp(out, 30)
    return out / (np.max(np.abs(out)) + 1e-9) * 10 ** (-4 / 20)


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("list")
    r = sub.add_parser("render")
    r.add_argument("cues")
    r.add_argument("--duration", type=float, required=True)
    r.add_argument("--out", required=True)
    a = ap.parse_args()
    if a.cmd == "list":
        for name, f in FX.items():
            print(f"{name + str(inspect.signature(f)):34s} {(f.__doc__ or '').strip()}")
        return
    cues = json.load(open(a.cues))
    out = render(cues, a.duration)
    with wave.open(a.out, "wb") as w:
        w.setnchannels(2)
        w.setsampwidth(2)
        w.setframerate(SR)
        w.writeframes((np.clip(out, -1, 1) * 32767).astype("<i2").tobytes())
    print(f"{a.out}: {len(cues)} cues, {a.duration:.2f} s")


if __name__ == "__main__":
    main()
