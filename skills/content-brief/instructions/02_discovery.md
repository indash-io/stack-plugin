# 02 — Discovery

Trabajo silencioso. Armás el contexto del período con las tools del MCP de
indash: marca, reglas, productos, referencias. No hablás con el user hasta el
Mix.

## Sub-paso 2A: La marca (fuente de verdad: el workspace)

- `get_brand_kit` → voz/tono, paleta (hex), tipografías, logos y las reglas de
  la marca. Es lo que gobierna todo el copy y toda dirección visual del brief.
- `get_style_references` → las referencias visuales del kit (piezas a emular).
  Úsalas para calibrar la dirección de los conceptos visuales, no las copies.

Si el brand kit está vacío o incompleto, **avisá qué falta** y trabajá con lo
que el user provea — nunca lo inventes.

## Sub-paso 2B: Productos en juego

- `list_products` → el catálogo real (nombre, `product_id`, descripción,
  precio, URL, cantidad de fotos).
- Identificá cuáles entran en el período según el objetivo.
- Para los productos foco, `get_product_images` te muestra qué fotos existen:
  si un producto foco **no tiene fotos utilizables**, marcalo — es un bloqueo
  de ejecución que el brief tiene que declarar (o pedir resolver antes).
- **No inventes productos, precios ni features.** El `product_id` real va en
  cada bloque que lleve producto.

## Sub-paso 2C: Reglas del período

Anotá las reglas duras que el brief tiene que respetar (ej: "cuotas sin
precio", "sin preventa", "humor suave", "cero invención de claims", voseo).
Salen del brand kit, del pedido del user y del historial del workspace. Estas
reglas gobiernan todos los bloques.

## Síntesis interna

```
CLIENTE/WORKSPACE: [nombre]
PERIODO: [mes / campaña]
OBJETIVO: [vender / lanzar / promo / fecha / awareness]
VOZ: [una línea]
REGLAS DURAS: [lista]
PALETA: [hex del brand kit]
PRODUCTOS FOCO:
  - [nombre] — [product_id] — [precio] — [fotos: N utilizables / sin fotos ⚠️]
```

Con esto avanzás al Mix (`03_mix.md`).
