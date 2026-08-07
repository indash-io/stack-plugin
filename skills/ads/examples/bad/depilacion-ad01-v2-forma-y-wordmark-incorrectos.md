---
brand: depilacion (marca anonimizada)
category: belleza / depilación
fecha: 2026-06-30
modelo_usado: gpt-image
modelo_correcto: gpt-image (correcto) — error fue en uso de refs, no en modelo
---

# Depilación AD 01 v2 — Producto sigue mal: forma simétrica y wordmark genérico

## Qué salió mal (segunda iteración, todavía mal)

Después de corregir la forma rectangular tipo jabón (V1 → bad example anterior), V2 cayó en otro error: pebbles **ovales simétricos tipo huevo / almendra** cuando el producto real es **asimétrico tipo gota / pétalo**.

Errores concretos en V2:

1. **Forma del pebble incorrecta (otra vez)**: el producto real tiene una asimetría clara — una curva amplia en la parte de arriba y un perfil más afilado/aplanado abajo. Es una silueta de **gota o pétalo en perspectiva**, NO un huevo simétrico ni una almendra balanceada. V2 tiene pebbles redondeados uniformes.

2. **Wordmark de la marca con tipografía genérica**: el wordmark real es lowercase con un estilo rounded soft custom (curvas suaves específicas en cada letra). V2 lo renderizó como un sans bold genérico, perdiendo la personalidad de marca.

3. **Falta el patrón hexagonal del lado de uso**: el lado de uso del producto tiene un patrón hexagonal de nano-cristales (visible en p4, p5, p6 del workspace de Indash). Aunque para AD 01 se ve el lado del wordmark (no el de uso), entender este detalle informa la perspectiva 3D del pebble.

4. **Pink y Teal renderizados sin packshot real**: Pink y Teal NO existen como SKUs separados en el workspace de Indash; solo están Purple y Black. Yo asumí que el usuario los tenía y los recoloreé desde la silueta inventada — error doble.

## Causa raíz

- **No leí TODAS las imágenes del producto en Indash antes de armar el prompt**. El SKU del borrador de vello tiene 8 imágenes; solo miré 2-3. Las otras (p0 viral con el wordmark grande, p4 modo de uso, p6 con caja) muestran la forma asimétrica REAL y la tipografía del wordmark con claridad.
- **Confié en una sola pasada de descripción verbal** ("oval/almond pebble") en vez de pasar 4-5 ángulos del producto como refs y dejar que gpt-image absorba la silueta.
- **No verifiqué la existencia de Pink y Teal en el workspace** antes de generar.

## Cómo evitarlo

1. **Antes de generar cualquier ad con un producto real**: leer **TODAS** las imágenes de ese producto en Indash (`get_product_images`). No solo el hero. Las imágenes 4, 5, 6, 7 suelen tener vistas, detalles y contexto que el hero esconde.

2. **Si la forma del producto es asimétrica o tiene un wordmark custom**: pasar **mínimo 3-4 vistas distintas** (hero, modo de uso, vista lateral, packaging) como `reference_image_urls`. Esto le da al modelo de imagen una representación 3D del producto.

3. **Si faltan color variants**: NO inventarlos. Confirmar con el usuario antes de generar. Si el usuario insiste en proceder sin packshot, avisar explícitamente en la entrega que ese color es "concepto sin packshot de referencia, fidelidad no garantizada".

4. **Verificar después de cada generación**: la forma del producto matches el packshot? El wordmark está renderizado en la tipografía custom o en una genérica? Si genérica → regenerar con el packshot pasado como ref + instrucción de "preserve exact wordmark typography from reference, do not substitute with generic sans".

## Brief original (mismo que V1)

> AD 01 · 1080×1350 vertical · Purple/Black/Pink/Teal · Conversión Oferta · "La imagen tiene que ser similar a la referencia, pero adaptada a la oferta actual" · Texto: "<Producto> x $29.990" / "Nunca estuvieron tan baratas" / CTA "ÚLTIMAS UNIDADES"

## Línea roja

> **El producto real manda.** Si lo que generaste no es indistinguible del packshot real al primer vistazo, mal. La fidelidad no se aproxima. Si no podés verificar shape + wordmark + detalles del producto desde las imágenes del workspace antes de generar, parar y traerlas. Cada imagen del catálogo es información, no decoración.
