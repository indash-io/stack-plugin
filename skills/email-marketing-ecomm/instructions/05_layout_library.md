# 05 — Layout Library (Ecom B2C)

Biblioteca de bloques modulares para construir mails con variedad visual real. Cada mail = **1 Hero + 2–4 Body + 1 Closing**.

## Regla de oro

Las 3 variantes del mismo brief **deben usar combinaciones distintas**. Test de variedad obligatorio antes de generar HTML.

---

## HEROS (elegir 1)

### H1 — Texto-led + producto chico abajo
Hero de TEXTO grande (hasta 3 líneas), imagen producto debajo, CTA después.
**Cuándo:** emocional / brand-led poético.

### H2 — Imagen-led full bleed
Imagen full-bleed (1200x1500) ocupando casi todo el viewport inicial. Texto sobre la imagen o debajo, breve. CTA grande.
**Cuándo:** producto con apelo visual fuerte (lifestyle, mood).

### H3 — Big number / badge gigante
Solo el número/oferta como protagonista (`3 × 2`, `20% OFF`, `2 X 1`). Imagen producto pequeña debajo opcional.
**Cuándo:** promo dura, audiencia cold, urgencia.

### H4 — Countdown timer
Reloj `48:00:00` estático arriba (no JS). Tape ribbon con la oferta debajo. Hero secundario producto/collage.
**Cuándo:** urgencia real, últimas horas, sale por terminar.

### H5 — Collage / canasta de productos
Imagen con MÚLTIPLES productos en escena (canasta, mesa, lay-flat). Texto debajo. CTA.
**Cuándo:** restock, lanzamiento de varios, bundle.

### H6 — Lifestyle hand/model
Imagen de mano sosteniendo producto, o modelo aplicándolo. Crops asimétricos OK. Texto al costado o debajo.
**Cuándo:** producto que se siente / aplica / sostiene (skincare, beauty tools, lip products).

### H7 — Editorial split
Hero partido en 2 columnas: texto grande izq, imagen producto der (o viceversa). En mobile texto arriba, imagen abajo.
**Cuándo:** producto premium, narrativa sofisticada, lanzamiento.

---

## BODY BLOCKS (combinar 2–4)

### B1 — Grid 2x2 simple
4 productos en grid: imagen + nombre + sub-label.
**Cuándo:** mostrar línea, mail emocional/brand.

### B2 — Productos con precio antes/después
Card: badge "Descuento", imagen, nombre, precio actual + tachado.
**Cuándo:** racional, sale, BFCM. **Requiere precios reales en brief.**

### B3 — Testimonio-led product cards
Card con imagen producto + review + ★★★★★ + nombre + ✓ verificado.
**Cuándo:** prueba social, retargeting. **Solo si la marca tiene reviews validadas.**

### B4 — Lifestyle con badges
Imagen lifestyle grande + 3-4 píldoras/badges con beneficios.
**Cuándo:** explicar features sin texto largo.

### B5 — Side-by-side text + image
2 columnas: texto izq, imagen producto der (o alternar).
**Cuándo:** explicar propuesta de valor, multi-feature, narrativa pausada.

### B6 — Pasos numerados (1, 2, 3)
3 filas: círculo con número + título + descripción.
**Cuándo:** cómo funciona, cómo usar el producto, cómo se aplica la promo.

### B7 — Timeline de resultados
Filas con label de tiempo (Día 1 / Semana 2 / Semana 4) + descripción.
**Cuándo:** producto con curva de resultados (skincare, suplementos, beauty tools).

### B8 — Shopping guide por persona / uso
Sección encabezada con pregunta ("¿Qué buscás?", "Según tu uso"). 4-6 sub-bloques: imagen + frase de beneficio + CTA específico.
**Cuándo:** catálogo amplio, gift guide, "elegí según vos".

### B9 — Featured single product + code reveal
1 producto destacado + box con código de descuento.
**Cuándo:** mail con código (`PRIMAVERA20`), exclusivo, post-onboarding.

### B10 — Comparativa (Light vs Best vs Extreme)
Tabla horizontal con 2-3 productos, badge "Recomendado" en uno.
**Cuándo:** marca con tiers, ayudar a elegir.

### B11 — Diagonal ribbon decorativo
Tape de color cruzando diagonal con texto repetido (`CYBER MONTH 🔥`).
**Cuándo:** entre secciones como separador visual de urgencia.
**HTML:** PNG pre-rotado (CSS rotate no anda en Outlook).

### B12 — Stats row
3 celdas con número grande + label uppercase. Ejemplo Smud: `+100k clientas / 0 cuchillas / 7 zonas aptas`.
**Cuándo:** social proof cuantitativo validado.

---

## CLOSING / URGENCY BLOCKS (elegir 1)

### C1 — Última chance texto puro
Headline ("Última chance", "Tu momento"), 1-2 líneas con fecha, CTA grande.
**Cuándo:** cierre cálido emocional.

### C2 — Countdown final + CTA
Reloj chico recordando + CTA grande.
**Cuándo:** mail con urgencia dura, refuerzo.

### C3 — Diagonal ribbon + close
Ribbon decorativo cruzando + headline + CTA. En Smud: ribbon lime `#D4F564`.
**Cuándo:** Cyber Month / BFCM / promos high-energy.

### C4 — Heart / icon grid
Grilla decorativa de íconos (corazones, gotas, círculos lila). Headline + CTA debajo.
**Cuándo:** fecha especial (Valentine, Madre, primavera, navidad) o cierre aspiracional.

---

## Combinaciones recomendadas por tipo de promo

| Tipo de promo | V1 Hero | V2 Hero | V3 Hero |
|---|---|---|---|
| **% off** (este caso Smud) | H6 (lifestyle) | H3 (big number) | H7 (editorial split) |
| BFCM / Cyber Sale | H1 (texto) | H4 (countdown) | H6 (lifestyle) |
| Restock | H5 (collage) | H3 | H2 |
| Lanzamiento producto | H7 | H3 | H2 |
| 2x1 / 3x2 | H1 / H6 | H3 | H7 |
| Fecha especial | H6 | H4 | H2 |
| Bundle / kit | H5 | H3 + B10 | H8 |

---

## Test de variedad obligatorio

✅ **Test 1:** Los 3 heros son distintos (no los 3 H2, no los 3 H3)
✅ **Test 2:** Al menos 4 body-blocks distintos sumando entre las 3 variantes
✅ **Test 3:** Los 3 closings son distintos

Si alguno falla → cambiar UNA variante.

---

## Imágenes via MCP de Indash

Para cada hero / lifestyle / producto editado:

1. `mcp__indash__list_products` → identificar `product_id`
2. `mcp__indash__get_product_images` → traer URLs reales
3. `mcp__indash__generate_image` con esas URLs en `reference_image_urls` + prompt editorial
4. La URL devuelta se embebe directo en el HTML

**Modelos:**
- `nano-banana` (Gemini, default) — lifestyle, modelos, escenas
- `gpt-image` (OpenAI) — text rendering en imagen, badges con texto

**Aspect ratios:**
- `4:5` — hero vertical (mobile-first)
- `1:1` — producto clean
- `16:9` — banner horizontal
- `9:16` — stories / mobile full
