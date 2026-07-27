---
name: ig-story
description: "Reglas de formato para UNA story de Instagram (vertical 9:16). Se carga cuando la pieza es una sola story. Para múltiples stories con narrativa, ver ig-stories-secuencia."
language: es
---

# Format — Instagram Story (single)

Skill de **formato puro** para UNA story. Si la pieza son varias stories que cuentan algo en conjunto, ver `ig-stories-secuencia`.

## Specs técnicas

- **Aspect ratio**: 9:16 vertical.
- **Resolución**: 1080x1920.
- **Cantidad default**: 1 story. Si son varias en secuencia con narrativa, usá `ig-stories-secuencia`.
- **Aspect ratio**: pasalo siempre como **`aspect_ratio: "9:16"`** en `generate_image`. NO lo escribas en el texto del prompt — es parámetro de la tool, no descripción.
- **Cierre del prompt** (sí va en el texto, sin aspect): *"fotografía editorial de alto detalle, fotorrealista, foco nítido en el producto, composición que respeta la zona segura de UI con el texto fuera del 14% superior y del 15% inferior del cuadro."*

## Zona segura de UI

Instagram tapa los extremos verticales:

| Zona | % vertical | Qué tapa |
|---|---|---|
| Superior | 0–14% | Avatar, nombre, tiempo, cierre |
| **Centro (segura)** | **14–85%** | Tu contenido visible |
| Inferior | 85–100% | Input "enviar mensaje", ícono envío, indicadores |

**Regla**: el texto on-image **siempre** vive entre el 14% y 85% del alto. Si vive en los extremos, queda ilegible o tapado.

Trucos:
- "Texto arriba" = tercio superior central (~20–35% del alto), no borde superior.
- "Texto abajo" = tercio inferior central (~65–80%), no borde inferior.
- Para CTAs con sticker de Link, dejá el último 15% del cuadro **vacío de texto importante** — ahí va el sticker.
- Stickers de engagement (poll, quiz, pregunta) suelen ubicarse en zona ~70–85% — si tu copy on-image vive ahí, el sticker lo va a tapar. Movelo arriba.

## Copy on-image

- **Máximo 6–8 palabras**. El user tiene 5–15 segundos antes del auto-advance.
- Una story = un bloque de texto principal. No metas dos titulares.

## Sticker (opcional)

Una story sola puede llevar un sticker de engagement (poll, pregunta, quiz, link). El sticker NO va dentro de la imagen generada — es un overlay nativo de Instagram. Solo lo sugerís como nota al user.

Si la story es CTA con link, dejá el último 15% del cuadro vacío de texto importante (ahí va el sticker de Link).
