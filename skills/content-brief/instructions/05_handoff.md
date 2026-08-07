# 05 — Output + Handoff

Armás el brief final, lo guardás, y cerrás explicando cómo ejecutar cada bloque.

## Armado del brief

Usá `templates/brief_template.md`. El brief lleva, en orden:
1. Encabezado: cliente, período, objetivo, fecha, voz y reglas.
2. Resumen del mix (tabla con cantidades por tipo).
3. Detalle por pieza, agrupado por tipo (los bloques del paso 4).

## Guardado (no negociable)

Guardá el brief en la carpeta del cliente:

- **Ruta**: `briefs/<AAAA-MM-DD>_<periodo-slug>_v<N>.md`
  - `<periodo-slug>` = el período en kebab-case (ej: "Junio 2026" → `junio-2026`, "Lanzamiento Smartwatch Kids" → `lanzamiento-smartwatch-kids`).
  - `v<N>` = versión; subí el número si regenerás el mismo período. **Nunca pises** un brief existente.
- Si no hay carpeta de cliente, guardá en `./briefs/` y sugerí dar de alta el cliente con `new-client`.
- Mostrás el brief en el chat **y** decís en una línea dónde lo guardaste.

## Handoff de ejecución

Cerrá mapeando cada bloque a su skill, en el orden sugerido de producción:

> Brief guardado en `briefs/...`. Para producirlo:
> - **Ads** → skill `ads` (te genera imagen + copy de Meta por variación).
> - **Carruseles** → skill `carruseles` (genera las imágenes 4:5).
> - **Stories** → skill `stories-nano-banana`.
> - **Videos** → skill `ugc-video-prompts` (UGC) o `seedance-multishot` (film B2B).
> - **Emails** → skill `email-marketing-ecomm`.
>
> Decime por cuál arrancamos y ejecuto pieza por pieza.

## Reglas

1. Brief **guardado** con nombre canónico, además de mostrado.
2. Handoff **concreto**: cada bloque nombra su skill.
3. Tono rioplatense, sin relleno.
