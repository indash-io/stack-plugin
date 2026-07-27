---
name: ig-post
description: "Reglas de formato para post único de Instagram feed (una sola imagen, 1:1 o 4:5). Se carga cuando la pieza es UN post (no carrusel, no story). También cubre el caso 'imagen suelta libre' (web, blog, banner) cuando no es para Instagram."
language: es
---

# Format — Instagram Post (single image)

Skill de **formato puro** para una sola imagen de feed. También sirve como fallback para "imagen suelta" sin formato específico.

## Specs técnicas

- **1:1 cuadrado**: 1080x1080. Buena para producto centrado, claim corto.
- **4:5 vertical**: 1080x1350. Más espacio vertical, mejor para escenas con persona o texto multi-línea.
- **Aspect ratio**: pasalo siempre como **`aspect_ratio: "1:1"` o `"4:5"`** en `generate_image`. NO lo escribas en el texto del prompt — es parámetro de la tool.
- **Cantidad default**: 1 imagen. Si el user pide "varias versiones / drafts", son N llamadas a `generate_image` con mismo `campaign` y `filename_hint` distinto — siguen siendo posts independientes, no es un carrusel.

## Cuándo usar 1:1 vs 4:5

| Caso | Aspect |
|---|---|
| Producto centrado, hero shot, packaging premium | 1:1 |
| Persona usando el producto, escena lifestyle | 4:5 |
| Claim de texto fuerte con espacio negativo | 4:5 |
| Promo / lanzamiento clean | 1:1 |

Si el user no especifica, **default 4:5**. Más universal en grilla de perfil.

## Una imagen, una idea

A diferencia de carrusel o secuencia, acá **toda la comunicación entra en una sola toma**. Eso significa:

- Un sujeto principal claro. No metas tres elementos compitiendo.
- Si hay copy on-image, una sola línea o jerarquía bold+regular bien resuelta.
- Espacio negativo respetado: el ojo necesita un lugar de descanso.

## Estilo visual (spectrum)

Cuando definís la idea (etapa 1 del proceso), ubicá la pieza en este spectrum:

- **Minimalista** → imagen limpia, sin (o casi sin) texto on-image, producto + escena.
- **Editorial** → copy on-image cuidado, jerarquía clara, mood narrativo.
- **Flyer / promo** → ultra editado: múltiples bloques de texto, badges, descuentos, elementos gráficos.

## Variaciones rápidas (mismo brief, output diferente)

Cuando el user pide *"hacéme otra versión"* o *"una variación más X"*:

- **Reusá el mismo `campaign`** para agrupar las variaciones.
- Cambiá `filename_hint` (ej: `hero-v2`, `hero-darker`).
- Si el cambio es pequeño y debería preservar la composición, tratalo como **edit** (ver "EDIT vs GENERATE" en prompt-craft) — pasale la versión anterior como primera ref.
- Si el cambio es grande (otra escena, otro mood), tratalo como **generate** nuevo con las mismas refs de producto.

## Imagen "suelta libre" (sin formato Instagram específico)

A veces el user pide una imagen que NO es para Instagram (web, blog, mockup, banner, ad). En ese caso:

- Preguntá el aspect si no lo dice. No asumas.
- Pasá el `aspect_ratio` correspondiente a `generate_image` (valores soportados: `1:1`, `4:5`, `9:16`, `16:9`, `3:4`, `4:3`, `2:3`, `3:2`, `5:4`, `21:9`).
- Casos comunes:
  - **16:9** horizontal → web hero, banner, ad horizontal.
  - **3:2** horizontal → foto editorial clásica.
  - **2:3** vertical → Pinterest, mobile vertical.
  - **3:4** vertical → print clásico.
- Cierre del prompt (sin aspect): "alta resolución" + "fotorrealista" + foco.
