# BAD — Multi-ref pasado como "frame final" para revelar la otra cara del producto

## Brief received
> "Generes un video de 15 segundos medio hyper motion zoom in a todos los productos y a sus partes del otro lado, para que arranque a mostrar cada uno con tomas más de cerca de ambos productos."

Producto (marca de depilación, anonimizada): **3 silicone pebbles de color** (pink, purple, mint), cada uno con su foto del frente y su foto del underside subidas a indash. El frente tiene el wordmark de la marca embossed; el underside es liso con un punto de inyección visible.

## What was generated
3 renders Seedance × 5s (uno por color). Cada render se disparó así:
- `@Image1` = frente del producto (frame-0)
- `@Image2` = underside del producto
- Motion prompt: "extreme macro close-up of the front → 180-degree natural spin revealing its underside, which must match @Image2 exactly — same shape, same color, same surface detail."

Los 3 renders fallaron de la misma manera: Seedance hizo el flip pero **inventó la underside** — el color quedó parecido pero la forma del molde, el punto de inyección y la superficie no matchean la `@Image2` real. El producto deja de ser "el pebble rosa real" y pasa a ser "un objeto rosa parecido que Seedance imaginó".

## Why this failed (root causes)

### 1. Seedance no acepta "frame final"
La multi-ref de Seedance 2.0 NO está temporalmente tagueada. Cuando pasás 9 refs, todas son **soft conditioning del contenido** — no son frames específicos del timeline. El modelo entiende `@Image2` como "otro angulo/concepto del mismo objeto", no como "el frame al que tenés que llegar a los 3 segundos".

El prompt "rotates revealing its underside which must match @Image2 exactly" suena claro al humano pero el modelo no tiene mecanismo para forzarlo. Termina interpolando libremente desde `@Image1` (el frame-0 real).

### 2. La cara opuesta de un producto NO está en el frame-0
Cuando el frame-0 muestra la cara A, la cara B no está en ninguna parte del input visual que el modelo procesa frame-a-frame. Cuando llega el momento de rotar, Seedance tiene que **inventar** la cara B basándose en su prior. Para productos genéricos (una manzana, una pelota) funciona. Para productos con label/wordmark/textura específica, alucina.

### 3. Hypermotion + flip + label fidelity = 3 fidelidades en un mismo shot
Es un caso clásico de la **regla de las 3 fidelidades** (`reference/seedance_2_params.md`):
- Fidelidad de movimiento (hypermotion zoom-in)
- Fidelidad de transformación (rotación 180°)
- Fidelidad de label/marca (wordmark embossed, forma del molde)

Juntar las 3 en un solo render rompe siempre. Algo cede. En este caso cedió la fidelidad de label en la cara que Seedance tuvo que inventar.

## What should have been done

### Fix A — 2 shots por producto, no 1
Partir el flip en 2 renders Seedance separados, cada uno con SU propio frame-0:
- **Shot A (2.5s)**: frente del producto, hypermotion zoom-in, hold en macro de la cara frontal. Frame-0 = la foto del frente real.
- **Shot B (2.5s)**: underside del producto, hold inicial + hypermotion zoom-out o leve rotación de cierre. Frame-0 = la foto del underside real.

Stitch invisible en CapCut con un whip-pan o un whoosh-cut. El viewer percibe "un flip", el modelo nunca tuvo que inventar nada.

### Fix B — Si se necesita el flip continuo, no usar Seedance
Para una rotación 180° con label fidelity perfecta en ambas caras, opciones:
1. **Render real en Blender/Cinema 4D** del modelo 3D del producto, con la textura del label aplicada — fuera de scope de Seedance.
2. **Veo 3.1 con multi-ref (3 imgs)** — Veo en algunos casos respeta mejor refs múltiples como targets temporales, pero no es determinístico tampoco. Probarlo con muestra antes de comprometer el job.
3. **Frame-blending en CapCut** con 2 stills generados por Nano Banana (frente + underside) y un morph entre ellos — peor que un flip 3D pero predecible.

### Fix C — Confirmar fidelity ANTES del flip
Si igual se intenta single-shot, hacer **un render piloto de 3s** primero con un solo color como prueba. Si la underside no matchea, no quemar los otros 2 colores. Ahorra 2/3 del costo.

## Output bug a documentar
- `pebble_tour_pink.mp4` → underside hallucinada (forma simétrica perfecta, sin el punto de inyección real)
- `pebble_tour_purple.mp4` → underside con color correcto pero textura inventada
- `pebble_tour_mint.mp4` → underside con un wordmark fantasma que NO está en la foto real del underside

## Lección clave
**Multi-ref en Seedance es soft conditioning, no timeline anchoring.** Si necesitás que el frame N matchee una imagen específica, generá ese frame N como frame-0 de su propio shot. No hay shortcut.
