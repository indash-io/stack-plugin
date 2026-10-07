"""Saca vectores reales (íconos, símbolos, logos) de una página de un manual de marca en PDF.

  pdf_paths.py MANUAL.pdf PAGINA SALIDA_DIR [--region X0,Y0,X1,Y1] [--min 20] [--fill 0f2913]

Convierte la página a SVG con pdftocairo, lista cada <path> con relleno y su caja (en
coordenadas del SVG de la página), y escribe cada uno como SVG suelto (path_<n>.svg,
viewBox ajustado). Con --region te quedás con los que caen adentro (p. ej. la grilla de
íconos); con --fill, solo los de ese color. Después renombrás los que vas a usar.

Si los íconos de la página no salen como paths (texto en una fuente de íconos), no hay
vector que extraer: rasterizá la página en alta (pdftoppm -r 288) y recortá.
"""

import argparse
import os
import re
import subprocess
import tempfile


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("pdf")
    ap.add_argument("page", type=int)
    ap.add_argument("outdir")
    ap.add_argument("--region", default=None)
    ap.add_argument("--min", type=float, default=20, help="tamaño mínimo (lado mayor) para no listar glifos sueltos")
    ap.add_argument("--fill", default=None, help="hex sin #, p. ej. 0f2913")
    a = ap.parse_args()

    os.makedirs(a.outdir, exist_ok=True)
    svg = os.path.join(tempfile.mkdtemp(), "page.svg")
    subprocess.run(["pdftocairo", "-svg", "-f", str(a.page), "-l", str(a.page), a.pdf, svg], check=True)
    body = open(svg).read().split("</defs>", 1)[-1]
    region = [float(v) for v in a.region.split(",")] if a.region else None
    n = 0
    for m in re.finditer(r"<path[^>]*>", body):
        tag = m.group(0)
        d = re.search(r' d="([^"]*)"', tag)
        fill = re.search(r'fill="([^"]*)"', tag)
        if not d or not fill or fill.group(1) == "none":
            continue
        nums = [float(v) for v in re.findall(r"-?\d+\.?\d*", d.group(1))]
        xs, ys = nums[0::2], nums[1::2]
        if not xs:
            continue
        x0, y0, x1, y1 = min(xs), min(ys), max(xs), max(ys)
        if max(x1 - x0, y1 - y0) < a.min:
            continue
        if region and not (x0 >= region[0] and y0 >= region[1] and x1 <= region[2] and y1 <= region[3]):
            continue
        col = fill.group(1)
        rgb = re.findall(r"([\d.]+)%", col)
        hexcol = "".join(f"{round(float(v) * 2.55):02x}" for v in rgb) if len(rgb) == 3 else col.lstrip("#")
        if a.fill and hexcol.lower() != a.fill.lower():
            continue
        n += 1
        w, h = x1 - x0, y1 - y0
        out = os.path.join(a.outdir, f"path_{n:03d}.svg")
        open(out, "w").write(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{x0:.3f} {y0:.3f} {w:.3f} {h:.3f}" '
                             f'width="{w * 8:.0f}" height="{h * 8:.0f}"><path fill="#{hexcol}" d="{d.group(1)}"/></svg>')
        print(f"path_{n:03d}.svg  x {x0:7.1f}  y {y0:7.1f}  {w:6.1f}×{h:6.1f}  #{hexcol}")
    print(f"{n} paths escritos en {a.outdir}")


if __name__ == "__main__":
    main()
