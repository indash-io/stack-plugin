---
brand: smud
category: belleza / depilación
fecha: 2026-06-30
modelo_usado: nano-banana
modelo_correcto: nano-banana con refs reales + workflow híbrido para texto
---

# Smud AD 01 — Producto con forma INCORRECTA + referencia ignorada

## Qué salió mal

1. **Forma del producto inventada**: rendericé el "Borrador de Vello Smud" como un **rectángulo redondeado tipo barra de jabón**. La forma real es un **pebble oval/almendrado/asimétrico** (más ancho de un lado, curvo, ergonómico para sostener en mano).

2. **Referencia visual ignorada**: el brief mandaba "La imagen tiene que ser similar a la referencia" (lime green ad con "Regalar Mal Debería Ser Delito → 40% OFF → + Packaging De Regalo → SOLO POR HOY" como pill button). Yo armé un layout totalmente distinto.

3. **Tipografía del wordmark inventada**: pasé "smud" como texto a renderizar dentro del prompt. nano-banana lo dibujó como una letra estándar bold. La tipografía real de "smud" es una marca custom con curvas suaves específicas.

4. **Color Pink y Teal inventados sin packshot**: nano-banana adivinó cómo se verían las 4 versiones. Riesgo bajo solo si la forma estuviera bien.

## Causa raíz

- No verifiqué la forma real del producto en Indash antes de armar el prompt. Asumí "pebble = jabón".
- No le pasé al MCP el packshot real como `reference_image_urls` con instrucción de **preservar la silueta exacta**.
- Aplicación pasiva de la skill: ejecuté el brief literal en vez de cruzar contra los assets reales del workspace.

## Cómo evitarlo

1. **SIEMPRE leer las imágenes de producto de Indash ANTES de armar el prompt**. No describir la forma con palabras — pasar el packshot como ref + decir "preserve the exact silhouette of the reference, do not modify shape, proportions, or wordmark".
2. **Si la marca tiene un wordmark custom**, NO incluirlo como texto en el prompt. Confiar 100% en la ref y prohibir explícitamente que invente texto sobre el producto.
3. **Si el brief dice "similar a la referencia"**, replicar la composición del ref pixel-a-pixel mental (layout, jerarquía tipográfica, colores), NO armar uno nuevo "inspirado".
4. **Si faltan colores como SKU en Indash** (Pink, Teal aquí), **pedirlos al usuario antes de generar**. No recolorear desde uno y rezar.

## Brief original

> AD 01 · 1080×1350 vertical · Smud Purple/Black/Pink/Teal · Conversión Oferta · Bottom of Funnel
> "La imagen tiene que ser similar a la referencia, pero adaptada a la oferta actual"
> Texto: "Smuds x $29.990" / "Nunca estuvieron tan baratas" / CTA "ÚLTIMAS UNIDADES"

## Línea roja

> Si no podés verificar la **forma real**, la **tipografía del wordmark** y los **colores reales del producto** antes de generar, parar y pedir refs. La fidelidad no se inventa.
