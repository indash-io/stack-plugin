# Ads skill — instalación para el equipo

Skill de Claude Code para generar ads de Meta (FB/IG) para marcas de e-commerce DTC.

## Requisitos

1. **Claude Code instalado** en la máquina (CLI, desktop app o IDE).
2. **MCP de Indash conectado** en la sesión de Claude Code. Si no lo tenés:
   ```bash
   claude mcp add --transport http indash https://www.indash.ai/api/mcp \
     --header "Authorization: Bearer <TU_API_KEY_DE_INDASH>"
   ```
   Verificá con `claude mcp list` que diga `✓ Connected`.
3. (Opcional) Que la marca con la que vas a trabajar tenga el workspace + productos cargados en Indash.

## Instalación

### Opción A — desde zip

1. Descomprimí `ads.zip` en `~/.claude/skills/`. Tiene que quedar `~/.claude/skills/ads/SKILL.md`.
2. Reiniciá Claude Code. La skill aparece automáticamente como `ads` en la lista de skills.

### Opción B — desde Git

```bash
cd ~/.claude/skills
git clone <repo-url> ads
```

## Cómo usarla

Disparala explícita o implícitamente:

- **Implícito**: pedile a Claude algo como "generá 4 ads de Meta para mi producto X" o "necesito 3 creatividades para campaña de retargeting" — la skill se activa sola.
- **Explícito**: decile "usá la skill `ads`" o invocala con `/ads`.

La skill va a:
1. Pedirte inputs faltantes (producto, imágenes de referencia, URL).
2. Buscar el producto en Indash automáticamente si lo nombrás.
3. Proponerte 2-4 ángulos creativos distintos y **esperar tu confirmación**.
4. Generar las imágenes (vía Indash MCP) + copy completo de Meta.
5. Guardar todo en `~/Desktop/AI Agents/ADS/output/<fecha>/<marca>/<grupo>/`.

## Output

Por cada variación recibís:
- Imagen final 4:5 o 9:16 o 1:1 (según placement)
- Primary Text con conteo de caracteres
- Headline (27-40 chars) con conteo
- Description (27-30 chars) con conteo
- CTA de la lista oficial de Meta
- Justificación del ángulo creativo

## Limitaciones conocidas

- No genera video / Reels animados (solo estática y carrusel).
- No publica directo en Meta Ads Manager — entrega los activos.
- Si el producto NO está en Indash, la fidelidad visual baja (avisa).
- Output siempre en español (rioplatense por default).

## Soporte

Si la skill se comporta raro o querés mejorarla, editá los archivos dentro de `~/.claude/skills/ads/`:
- `SKILL.md` — workflow principal
- `instructions/` — los 6 pasos con sus reglas
- `style/` — voz y reglas de copy
- `templates/` — formatos de output
- `examples/bad/` — errores conocidos con análisis (alimentar este folder mejora la skill)
- `eval/quality_checklist.md` — self-check pre-entrega

Para que un cambio se aplique, no hace falta reiniciar — la próxima invocación de la skill ya lee la versión nueva.
