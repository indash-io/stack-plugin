# BAD — UGC stitched routine with character + product-scale drift

## Brief received
> "Video UGC skincare routine de una mexicana en el baño, usando varios productos más el del cliente (skincare), 15 segundos, onda creadora de contenido."

## What was generated
Stitched 3 shots × 5s. Shot 1 (hook with bottle raised) and Shot 2 (cheek application) held up. **Shot 3 (mirror payoff) broke**:
- La cara de la chica cambió notablemente respecto a shots 1 y 2 — peinado, facciones y proporciones distintas.
- El envase del cliente en primer plano sobre la encimera apareció con un tamaño desproporcionado (mucho más grande de lo que correspondía por escala respecto al rostro/encimera).

## Why this failed (root causes)

### 1. Character drift entre shots stitched
Pasar el frame 0 del shot 1 como ref del shot 3 **no es suficiente** cuando:
- El framing cambia (de medium shot a medium con espejo lateral)
- La pose cambia (de frente a cámara a perfil hacia espejo)
- Hay un segundo plano nuevo (espejo + reflexión) que confunde la atención del modelo

Nano Banana, al recibir el frame 1 como ref pero un prompt que describe una composición muy distinta, **reinterpreta la identidad** en vez de copiarla. La cara queda "similar pero diferente" — fatal para UGC donde la creadora ES la marca.

### 2. Product-scale drift
El envase en shot 1 estaba en la mano (escala chica relativa al cuadro). En shot 3 se movió a primer plano sobre la encimera **sin anclar su tamaño** en el prompt. El modelo lo escala "para que se vea" y termina enorme, irreal, rompiendo la creencia del viewer.

### 3. Reflejo de espejo como trampa
Pedir "ella + su reflexión en el espejo" en un solo frame de Nano Banana = el modelo tiene que inventar dos caras coherentes a la vez. Casi nunca matchean entre sí, ni con la ref previa.

## What should have been done

### Fix A — Identity lock sentence (copiar verbatim entre shots)
Crear UNA frase de identidad y repetirla EXACTA en los 3 prompts de frame 0:

> "Mexican woman, 26, warm undertone skin with faint visible acne scars on cheeks, dark wavy hair half-up in claw clip with pink headband, no makeup, oversized white cotton t-shirt — keep the EXACT same face as @Image1 reference, do not reinterpret features."

No improvisar variaciones por shot. Identidad = constante, no variable creativa.

### Fix B — Multi-ref identity stack (mínimo 2 refs de la persona)
A partir del shot 2 en adelante:
- Generar un **portrait-only crop** del shot 1 (recorte solo de la cara, sin contexto) y subirlo como ref adicional
- Pasar a Nano Banana: `[portrait_crop, full_shot1, product_image]` con el portrait listado primero y referenciado en el prompt como `@Image1 (identity lock)`
- El portrait sin contexto fuerza al modelo a tratarlo como identity reference, no como "escena para reinterpretar"

### Fix C — Product scale anchor
En cada frame 0 que tenga el producto, declarar su tamaño explícito:
- Mano: `"bottle ~12cm tall, occupying roughly 15% of frame height"`
- Encimera primer plano: `"bottle ~12cm tall, occupying roughly 25% of frame height, label height equal to half the woman's chin-to-forehead distance for scale realism"`

Sin anchor numérico/proporcional, Nano Banana escala "para que se lea el label" y rompe la escala física.

### Fix D — Evitar reflejos de espejo con identidad
Si necesitás el espejo:
- **Opción A**: solo el reflejo (la chica de espaldas, vemos solo su cara en el espejo). 1 cara que generar, no 2.
- **Opción B**: solo la chica de frente, el espejo apenas insinuado fuera de foco. 1 cara, espejo como atmósfera.
- **Nunca pedir** chica + reflejo nítidos en el mismo frame.

### Fix E — Pose continuity entre shots
El shot 3 cambió de "frente a cámara con bottle en mano" a "perfil hacia espejo con bottle en encimera". Salto demasiado grande. Mejor:
- Shot 3 alternativo: misma chica frente a cámara, toca su mejilla con ambas manos, sonrisa wider, hace un pequeño "yes" con la cabeza. El bottle queda en la mesa lateral fuera de foco. **Continuidad de pose = continuidad de identidad percibida.**

## The lesson

UGC stitched vive o muere por **continuidad percibida**. Tres reglas no negociables:

1. **Identity lock sentence** repetida verbatim en los N frame 0.
2. **Producto anclado por escala numérica** en cada frame 0 donde aparezca.
3. **Pose y framing similares entre shots consecutivos** — los cambios bruscos son donde Nano Banana reinterpreta.

Si el brief pide cambios bruscos (hook frontal → mirror payoff lateral) y querés mantener identidad: forzar un **shot puente** o aceptar que cada salto grande es un riesgo de drift. Mejor 3 shots con micro-variaciones que 3 shots con composiciones radicalmente distintas.

Ver `reference/ugc_stitched_consistency.md` para la checklist operativa.
