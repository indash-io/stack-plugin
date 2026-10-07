"""Recortes de UI real a partir de capturas o frames de grabaciones de pantalla.

  ui_crops.py boxes CAPTURA.png [--min-w 300 --min-h 80]
      → cajas blancas (cards) y oscuras (botones, tarjetas) con sus coordenadas en px de la captura.
  ui_crops.py crop CAPTURA.png X0 Y0 X1 Y1 SALIDA.png [--radius 30] [--scale 2]
      → recorte con esquinas redondeadas en alfa, x2 con Lanczos + unsharp suave (para pop-outs).
  ui_crops.py key CAPTURA.png X0 Y0 X1 Y1 SALIDA.png --bg R,G,B
      → recorte con el fondo sólido quitado (ilustraciones sobre fondo plano de la app).
  ui_crops.py rows CAPTURA.png Y0 Y1 [--x0 40 --x1 700]
      → filas de texto oscuro (para ubicar un highlight sobre una línea exacta).

Las coordenadas que imprime `boxes` son las que después usás para el patch del hueco
(cuando la pieza "sale" de la pantalla, su lugar queda vacío del color de fondo).
"""

import argparse

import numpy as np
from PIL import Image, ImageDraw, ImageFilter
from scipy import ndimage


def boxes(a):
    im = np.asarray(Image.open(a.image).convert("RGB")).astype(int)
    print(f"tamaño {im.shape[1]}×{im.shape[0]} · fondo en el borde = {tuple(int(v) for v in im[im.shape[0] // 2, 5])}")
    for name, mask in (("blanca", im.min(2) >= 250), ("oscura", im.max(2) < 60)):
        lab, _ = ndimage.label(mask)
        for sl in ndimage.find_objects(lab):
            w, h = sl[1].stop - sl[1].start, sl[0].stop - sl[0].start
            if w >= a.min_w and h >= a.min_h:
                print(f"  {name:6s} x {sl[1].start:4d}–{sl[1].stop:4d}  y {sl[0].start:4d}–{sl[0].stop:4d}  ({w}×{h})")


def crop(a):
    im = Image.open(a.image).convert("RGB").crop((a.x0, a.y0, a.x1, a.y1))
    w, h = im.size
    s = a.scale
    im = im.resize((w * s, h * s), Image.LANCZOS).filter(ImageFilter.UnsharpMask(radius=1.2, percent=60, threshold=2))
    m = Image.new("L", (w * s * 4, h * s * 4), 0)
    ImageDraw.Draw(m).rounded_rectangle([0, 0, w * s * 4 - 1, h * s * 4 - 1], radius=a.radius * s * 4, fill=255)
    im.putalpha(m.resize((w * s, h * s), Image.LANCZOS))
    im.save(a.out)
    print(f"{a.out}: {im.size[0]}×{im.size[1]}")


def key(a):
    c = np.asarray(Image.open(a.image).convert("RGB").crop((a.x0, a.y0, a.x1, a.y1))).astype(float)
    bg = np.array([float(v) for v in a.bg.split(",")])
    alpha = np.clip((np.sqrt(((c - bg) ** 2).sum(2)) - 10) / 22, 0, 1)
    lab, n = ndimage.label(alpha > 0.5)
    sizes = ndimage.sum(np.ones_like(alpha), lab, range(1, n + 1))
    alpha *= ndimage.binary_dilation(np.isin(lab, 1 + np.where(sizes > 800)[0]), iterations=2)
    im = Image.fromarray(np.dstack([c, alpha * 255]).astype(np.uint8))
    im = im.resize((im.width * 2, im.height * 2), Image.LANCZOS)
    im.save(a.out)
    print(f"{a.out}: {im.size[0]}×{im.size[1]} (fondo {a.bg} fuera)")


def rows(a):
    im = np.asarray(Image.open(a.image).convert("RGB")).astype(int)
    dark = im.max(2) < 110
    r = np.where(dark[a.y0 : a.y1, a.x0 : a.x1].sum(1) > 2)[0] + a.y0
    if not len(r):
        return print("sin texto en ese rango")
    groups, s, p = [], r[0], r[0]
    for v in r[1:]:
        if v > p + 3:
            groups.append((s, p))
            s = v
        p = v
    groups.append((s, p))
    for y0, y1 in groups:
        cols = np.where(dark[y0 : y1 + 1, a.x0 : a.x1].sum(0) > 0)[0] + a.x0
        print(f"  y {y0:4d}–{y1:4d}   x {cols.min():4d}–{cols.max():4d}")


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    b = sub.add_parser("boxes")
    b.add_argument("image")
    b.add_argument("--min-w", type=int, default=300)
    b.add_argument("--min-h", type=int, default=80)
    for name in ("crop", "key"):
        p = sub.add_parser(name)
        p.add_argument("image")
        for k in ("x0", "y0", "x1", "y1"):
            p.add_argument(k, type=int)
        p.add_argument("out")
        if name == "crop":
            p.add_argument("--radius", type=int, default=30)
            p.add_argument("--scale", type=int, default=2)
        else:
            p.add_argument("--bg", required=True)
    r = sub.add_parser("rows")
    r.add_argument("image")
    r.add_argument("y0", type=int)
    r.add_argument("y1", type=int)
    r.add_argument("--x0", type=int, default=40)
    r.add_argument("--x1", type=int, default=700)
    a = ap.parse_args()
    {"boxes": boxes, "crop": crop, "key": key, "rows": rows}[a.cmd](a)


if __name__ == "__main__":
    main()
