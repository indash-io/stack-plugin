#!/bin/bash
# Instala lo que necesitan los scripts de motion-graphics. Idempotente.
#
# El venv NO vive dentro de la skill: la carpeta del plugin es una cache que se
# pisa entera en cada auto-update del marketplace. Va a ~/.indash/motion-graphics/.
set -e

V=~/.indash/motion-graphics/venv
SKILL="$(cd "$(dirname "$0")" && pwd)"

command -v ffmpeg >/dev/null || { echo "Falta ffmpeg (brew install ffmpeg)"; exit 1; }
command -v node >/dev/null || { echo "Falta Node 22+ (HyperFrames lo necesita)"; exit 1; }
[ "$(node -p 'process.versions.node.split(".")[0]')" -ge 22 ] || { echo "Node < 22: HyperFrames necesita 22+"; exit 1; }
command -v pdftocairo >/dev/null || echo "Aviso: falta poppler (brew install poppler) — solo lo usa pdf_paths.py para manuales de marca en PDF"

mkdir -p "$(dirname "$V")"
[ -x "$V/bin/python" ] || python3 -m venv "$V"
"$V/bin/pip" install --quiet --upgrade numpy scipy pillow librosa

echo
echo "Listo. Los scripts se corren con:"
echo "  $V/bin/python $SKILL/<script>.py --help"
