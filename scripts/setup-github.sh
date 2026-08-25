#!/usr/bin/env bash
#
# Setup de GitHub del repo del plugin — labels + branch protection.
#
# QUÉ HACE
#   1. Crea (o actualiza, si ya existen) los labels que usa el skills hub:
#      - suggestion    → sugerencia de cambio a una skill que ya existe
#      - new-skill     → propuesta de skill nueva
#      - skill:<name>  → uno por cada carpeta de skills/, leída del filesystem
#   2. Protege la branch main:
#      - status check `validate` requerido (el job de .github/workflows/validate.yml)
#      - 1 aprobación requerida
#      - review de CODEOWNERS requerida
#      - force push y borrado de la branch deshabilitados
#
# CUÁNDO CORRERLO
#   Lo corre **un humano con permisos de admin en indash-io/stack-plugin**, a
#   mano. Cambiar los settings del repo no es una decisión de un agente ni de
#   CI: nadie lo dispara automáticamente. Volver a correrlo es seguro — es
#   idempotente: los labels que ya están se actualizan en vez de fallar, y la
#   branch protection se pisa con la misma config.
#
#   Después de agregar una skill nueva a skills/, corrélo de nuevo para que
#   aparezca su label skill:<name>.
#
# REQUISITOS
#   - gh CLI autenticado (`gh auth status`) con permisos de admin en el repo.
#
# USO
#   bash scripts/setup-github.sh              # sobre indash-io/stack-plugin
#   REPO=otra-org/otro-repo bash scripts/setup-github.sh
#
set -euo pipefail

REPO="${REPO:-indash-io/stack-plugin}"
BRANCH="${BRANCH:-main}"
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

command -v gh >/dev/null || { echo "✗ Falta el gh CLI: https://cli.github.com"; exit 1; }
gh auth status >/dev/null 2>&1 || { echo "✗ gh no está autenticado — corré 'gh auth login'"; exit 1; }

echo "→ Repo: $REPO"

# --- Labels ---------------------------------------------------------------
# `gh label create --force` crea el label o actualiza color/descripción si ya
# existe: eso es lo que hace idempotente esta parte.
ensure_label() {
  local name="$1" color="$2" description="$3"
  gh label create "$name" --repo "$REPO" --color "$color" --description "$description" --force >/dev/null
  echo "  ✓ label $name"
}

echo "→ Labels de triage"
ensure_label "suggestion" "0E8A16" "Sugerencia de cambio a una skill que ya existe"
ensure_label "new-skill"  "1D76DB" "Propuesta de skill nueva"

echo "→ Labels por skill (leídos de skills/)"
for dir in "$ROOT"/skills/*/; do
  [ -f "${dir}SKILL.md" ] || continue
  skill="$(basename "$dir")"
  ensure_label "skill:${skill}" "C5DEF5" "Toca la skill ${skill}"
done

# --- Branch protection ----------------------------------------------------
# PUT es idempotente: reemplaza la protección entera por esta config.
echo "→ Branch protection en $BRANCH"
gh api -X PUT "repos/${REPO}/branches/${BRANCH}/protection" \
  --input - >/dev/null <<'JSON'
{
  "required_status_checks": {
    "strict": true,
    "contexts": ["validate"]
  },
  "enforce_admins": false,
  "required_pull_request_reviews": {
    "required_approving_review_count": 1,
    "require_code_owner_reviews": true,
    "dismiss_stale_reviews": true
  },
  "restrictions": null,
  "allow_force_pushes": false,
  "allow_deletions": false,
  "required_linear_history": false,
  "required_conversation_resolution": true
}
JSON
echo "  ✓ status check 'validate' requerido, 1 aprobación, review de CODEOWNERS, sin force push"

echo "✓ Listo."
