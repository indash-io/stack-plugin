"""Contact sheets de un render: la forma de *mirar* un video entero de una vez.

Uso:
  contact_sheet.py VIDEO --fps 6 [--from 0] [--to 999] [--out PREFIJO]

Detecta la orientación (9:16 o 16:9) y arma hojas con el tiempo de cada frame
impreso arriba. Imprime las rutas de las hojas: abrilas con Read, una por una.
6 fps para una pasada completa; 10-15 fps alrededor de un momento sospechoso.
"""

import argparse
import glob
import json
import os
import shutil
import subprocess
import tempfile

from PIL import Image, ImageDraw


def probe(video):
    out = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries", "stream=width,height",
                          "-of", "json", video], capture_output=True, check=True, text=True).stdout
    s = json.loads(out)["streams"][0]
    return s["width"], s["height"]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("video")
    ap.add_argument("--fps", type=float, default=6)
    ap.add_argument("--from", dest="t0", type=float, default=0)
    ap.add_argument("--to", dest="t1", type=float, default=999)
    ap.add_argument("--out", default=None, help="prefijo de salida (default: junto al video)")
    a = ap.parse_args()

    w, h = probe(a.video)
    portrait = h > w
    cols, rows, tw, th = (12, 3, 150, 267) if portrait else (6, 5, 384, 216)
    prefix = a.out or os.path.splitext(a.video)[0] + "_sheet"
    tmp = tempfile.mkdtemp()
    subprocess.run(["ffmpeg", "-v", "error", "-ss", str(a.t0), "-to", str(a.t1), "-i", a.video,
                    "-vf", f"fps={a.fps},scale={tw}:{th}", f"{tmp}/f%05d.png"], check=True)
    frames = sorted(glob.glob(f"{tmp}/f*.png"))
    per = cols * rows
    paths = []
    for si in range(0, len(frames), per):
        chunk = frames[si : si + per]
        r = (len(chunk) + cols - 1) // cols
        sheet = Image.new("RGB", (cols * (tw + 4), r * (th + 18)), (30, 30, 30))
        dr = ImageDraw.Draw(sheet)
        for k, f in enumerate(chunk):
            t = a.t0 + (si + k) / a.fps
            x, y = (k % cols) * (tw + 4), (k // cols) * (th + 18)
            sheet.paste(Image.open(f), (x + 2, y + 16))
            dr.text((x + 4, y + 2), f"{t:.2f}", fill=(255, 230, 0))
        p = f"{prefix}-{si // per:02d}.jpg"
        sheet.save(p, quality=85)
        paths.append(p)
    shutil.rmtree(tmp)
    print(f"{len(frames)} frames, {len(paths)} hojas:")
    print("\n".join(paths))


if __name__ == "__main__":
    main()
