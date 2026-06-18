# 01 — Input Processing

## Qué parsear del brief

El brief puede venir en cualquier formato. Tu trabajo es extraer estos campos.

### Campos obligatorios

| Campo | Ejemplo | Si falta |
|---|---|---|
| `brand` | la del cliente de la carpeta de trabajo | Tomar del contexto del cliente (`CLAUDE.md` + `brand/`). Si no hay cliente ni la marca en Indash, caer al fallback `brands/{slug}/` y, si tampoco, preguntar |
| `promo_type` | `20% off`, `3x2`, `restock`, `lanzamiento`, `BFCM`, `2x1`, `bundle` | Preguntar |
| `featured_product` | "Borrador de Vello Smud", "Ice Roller", "Smud Black" | Preguntar |
| `deadline` | "hasta domingo 23:59", "48hs", "fin de mes" | Asumir 48-72hs y avisar |

### Campos opcionales (inferir o usar default)

| Campo | Default |
|---|---|
| `segment` | "all subscribers" |
| `secondary_products` | vacío (solo hero) |
| `discount_code` | vacío (link directo) |
| `free_shipping_threshold` | tomar del contexto del cliente (`CLAUDE.md` / `brand/brand.md`) si existe; fallback `brands/{marca}/brand.md` |
| `social_proof` | usar solo si el `brand.md` del cliente lo valida (fallback `brands/{marca}/brand.md`) |
| `language` | `es-AR` (voseo) — override consciente si la marca pide otro |

## Resolver producto con MCP de Indash

Una vez identificado el `featured_product` del brief:

1. **`mcp__indash__list_products`** → buscar producto por nombre. Guardar `product_id`.
2. **`mcp__indash__get_product_images`** → traer URLs reales del producto. Guardar las primeras 2-3 URLs (las mejores).
3. Las URLs se usan como `reference_image_urls` en `mcp__indash__generate_image` cuando se generen las imágenes de hero / lifestyle.

**Atajo:** si el contexto del cliente tiene `productos/index.md` (lo arma `new-client` desde el MCP de Indash) y el producto del brief matchea, usá ese `product_id` directo y saltá `list_products`. En modo fallback legacy, los `product_id` semilla viven cacheados en `brands/{marca}/brand.md` bajo `indash_product_ids`.

## Regla: NUNCA inventar datos duros

Prohibido inventar:
- Precios específicos
- Stock real ("quedan 12")
- Testimonios con nombre completo
- Stats que no estén validados en el contexto de marca del cliente (`CLAUDE.md` / `brand/brand.md`; fallback `brands/{marca}/brand.md`)
- Códigos de descuento que no estén en el brief

Si el brief no los tiene → lenguaje cualitativo ("stock limitado", "+100.000 clientas" solo si la marca lo valida).

## Regla: 1 sola ronda de preguntas

Si faltan campos obligatorios, hacer **una sola pregunta compacta** listando todo. Ejemplo:

> Me faltan 3 cosas: (1) qué producto va en el hero, (2) hasta cuándo dura la promo, (3) si hay código de descuento o es link directo. Respondeme y genero las variantes.

Si el usuario dice "dale, decidí vos", asumir defaults y avisar en `brief.md`.

## Slug del folder de output

Formato canónico: `<AAAA-MM-DD>_<campaña-slug>_v<N>` (kebab-case, sin acentos). Se guarda dentro de `entregables/emails/` de la carpeta del cliente (ver SKILL.md → "Output final"). Versiona, no pisa.

Ejemplos:
- `2026-05-05_20off-smud_v1`
- `2026-04-30_3x2-ice-roller_v1`
- `2026-04-30_restock-favoritos_v2`
- `2026-11-28_bfcm-smud_v1`

## Señales del brief que cambian decisiones

| Señal | Cambia esto |
|---|---|
| "BFCM / Cyber" | Layouts H4 (countdown), B11 (ribbon), C3. Urgencia visible. |
| "Restock" | Hero H5 (collage productos), copy "volvieron tus favoritos" |
| "Lanzamiento" | Hero H7 (editorial split), badge "NEW", visual del producto protagonista |
| "Fecha especial" (Madre/Amigo) | Hero H6 (lifestyle), C4 (icon grid temático) |
| "VIP / suscriptoras antiguas" | V1 emocional gana — tono más ritual, menos descuento |
| "Nuevos / cold" | V2 racional gana — claim claro, oferta visible |
| "Bundle / kit" | H5 collage + B10 comparativa + B8 shopping guide |
