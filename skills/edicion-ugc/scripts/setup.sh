#!/bin/bash
# Instala lo que necesita la skill edicion-ugc. Idempotente: correlo las veces
# que quieras, si ya esta todo no hace nada.
#
# El venv NO vive dentro de la skill: la carpeta del plugin es una cache que se
# pisa entera en cada auto-update del marketplace. Va a ~/.indash/edicion-ugc/.
set -e

V=~/.indash/edicion-ugc/venv
M=~/.cache/whisper-cpp/ggml-large-v3-turbo.bin
SKILL="$(cd "$(dirname "$0")" && pwd)"

[ "$(uname -s)" = "Darwin" ] || {
  echo "Esta skill esta probada en macOS (usa Homebrew y las fuentes de ~/Library/Fonts)."
  echo "En otro sistema hay que instalar ffmpeg, whisper-cpp, el modelo y Montserrat a mano."
  exit 1
}
command -v brew >/dev/null || { echo "Falta Homebrew: https://brew.sh"; exit 1; }

brew list ffmpeg      >/dev/null 2>&1 || brew install ffmpeg
brew list whisper-cpp >/dev/null 2>&1 || brew install whisper-cpp
brew list --cask font-montserrat >/dev/null 2>&1 || brew install --cask font-montserrat

# El modelo pesa 1.5 GB. Se baja a .part y recien ahi se renombra, para que una
# descarga cortada no quede como modelo "instalado" y roto.
[ -f "$M" ] || { mkdir -p "$(dirname "$M")"
  echo "Bajando el modelo de whisper (1.5 GB, tarda)..."
  curl -L -f --retry 3 -o "$M.part" \
    "https://huggingface.co/ggerganov/whisper.cpp/resolve/main/ggml-large-v3-turbo.bin"
  mv "$M.part" "$M"; }

mkdir -p "$(dirname "$V")"
[ -x "$V/bin/python" ] || python3 -m venv "$V"
"$V/bin/pip" install --quiet --upgrade pillow

echo
echo "Listo. Para usarla a mano:"
echo "  $V/bin/python $SKILL/editar.py revisar <carpeta-de-crudos>"
echo "  $V/bin/python $SKILL/editar.py montar  <config.json>"
