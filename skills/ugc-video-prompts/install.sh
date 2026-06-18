#!/bin/bash
set -e

SKILL_NAME="ugc-video-prompts"
SKILL_SRC="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SKILL_DEST="$HOME/.claude/skills/$SKILL_NAME"

mkdir -p "$HOME/.claude/skills"

if [ -e "$SKILL_DEST" ] || [ -L "$SKILL_DEST" ]; then
  echo "Ya existe $SKILL_DEST"
  echo "Para reinstalar: rm \"$SKILL_DEST\" && ./install.sh"
  exit 1
fi

ln -s "$SKILL_SRC" "$SKILL_DEST"

echo "Skill instalada via symlink:"
echo "  $SKILL_DEST -> $SKILL_SRC"
echo ""
echo "Probá abriendo Claude Code en cualquier carpeta y pidiendo un video UGC."
echo "Para actualizar: cd \"$SKILL_SRC\" && git pull"
