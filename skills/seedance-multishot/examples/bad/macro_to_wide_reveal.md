# BAD — Macro-to-wide reveal con producto ausente del frame-0

## Brief received
> "Apple-style launch hypermotion 15s del Omega 3. Arrancar en macro de cápsulas y hacer un snap zoom-out que revele la botella en hero composition."

Producto: **Omega 3 VITS** — botella plástica blanca con label específico, cápsulas blandas doradas.

## What was generated
Render `omega_apple_b_macro_to_wide_15s.mp4`. Los primeros 3 segundos del macro de cápsulas se ven bien — golden glossy, motion blur, premium feel. **El snap zoom-out se rompió:** cuando la cámara pulls back para revelar la botella, Seedance inventa un envase genérico que NO matchea el Omega 3 VITS real. El label, la forma, los colores — todo alucinado. El shot completo termina siendo "una botella cualquiera con cápsulas alrededor", no el producto del cliente.

## Why this failed (root causes)

### 1. El producto no estaba en el frame-0
El frame-0 (`omega_apple_b_macro_caps.png`) era un macro puro de 3-4 cápsulas doradas sobre fondo blanco. **La botella no aparecía en ningún píxel del input visual.** El prompt pasaba la foto real de la botella como `reference_image_url` único, pero el ref único de Seedance se interpreta como **frame-0**, no como "imagen de la cosa que tiene que aparecer cuando hagas zoom-out".

Cuando Seedance llega al beat de revelar la botella, no tiene anclaje visual de cómo es. Cae en su prior genérico de "botella de suplemento" y la inventa.

### 2. Mismo bug que el multi-ref como "frame final"
Esto es la otra cara de [[multi-ref-rotation-target]]. Allá el problema era pasar el underside como `@Image2` esperando que aterrice ahí. Acá el problema es **pasar el producto como ÚNICO ref pero usarlo como frame-0 de algo que NO contiene el producto**. Mismo principio: **Seedance solo respeta lo que está EN el frame-0 visual**. No tiene mecanismo para "aparecer este producto en el segundo N".

### 3. La fantasía de "macro → wide" como single shot
Macro extremo y wide composition con producto branded son dos shots conceptualmente distintos:
- Macro: pocos elementos, foco hyper-shallow, contexto cero
- Wide: producto entero, composición completa, label legible

Pedirle a Seedance que interpole de uno al otro en 3 segundos = el modelo tiene que generar contenido que NO ESTÁ en el frame-0 (el resto del producto + el contexto). Es invención obligatoria, no transformación.

## What should have been done

### Fix A — 2 shots stitched
Partir el shot en dos renders separados:
- **Shot 1 (3-4s)**: macro de cápsulas, frame-0 = imagen de cápsulas. Termina con un push-out / motion blur tail.
- **Shot 2 (11-12s)**: wide hero composition con el producto, frame-0 = imagen del producto en su composición wide (la que generaste con Nano Banana). Arranca con un snap-in / motion blur head.

Stitch invisible en CapCut con whoosh + whip-pan o cross-dissolve corto. El viewer percibe "macro → wide", el modelo nunca tuvo que inventar la botella.

### Fix B — Frame-0 con TODO en cuadro desde el inicio
Si igual querés single-shot, el frame-0 tiene que contener **la botella Y las cápsulas en macro juntas**. Por ejemplo: macro de una cápsula en primer plano con la botella **borrosa pero visible** detrás. Después el motion prompt describe el push-out + rack focus shift que la trae sharp. El producto estuvo en frame todo el tiempo, solo cambió el foco. Esto SÍ funciona.

### Fix C — La regla compacta
**Si querés que el producto aparezca en el shot, tiene que estar en el frame-0. Punto.** Pasar la foto del producto como ref sin que esté en la composición del frame-0 no lo "agrega" después.

## Lección clave
**Seedance interpola DESDE el frame-0, no hacia un target.** Todo lo que tiene que aparecer en el shot tiene que existir visualmente en el primer frame — borroso, parcial, pequeño, pero presente. Lo que no está, se inventa.

Si el guion exige un reveal de algo que no está en el frame-0, es siempre un caso de stitching de 2 shots, no de single-shot motion prompt.
