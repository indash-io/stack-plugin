# 05 — Prompt Engineering para Nano Banana

> **Canon**: este archivo es la *aplicación* de las leyes de
> `core/skills/prompt-craft/SKILL.md` (la fuente única del stack) a este
> workflow. Ante un conflicto de fondo, core gana — actualizá acá la
> aplicación, nunca redefinas la ley.

Este archivo no repite el template. El template (`templates/prompt_template.md`) define **qué** poner en el prompt. Este archivo define **por qué** y **cómo** funcionan los prompts en nano banana, para que escribas con criterio en lugar de rellenar campos.

---

## Qué es nano banana

**Nano banana** es el nombre informal de **Gemini 2.5 Flash Image** (Google). Es un modelo de generación de imágenes optimizado para:

1. **Consistencia con imágenes de referencia** — su superpoder. Le pasás una imagen y la respeta con altísima fidelidad (packaging, rostro, objeto). Por eso es el modelo correcto para secuencias de stories de e-commerce: el producto se mantiene idéntico en las N stories.
2. **Multi-image fusion** — puede combinar varias imágenes input en una sola escena coherente.
3. **Renderizado de texto** — renderiza texto dentro de la imagen mucho mejor que la generación anterior. Con dirección clara (fuente, peso, color, posición), funciona casi siempre.
4. **Fotorrealismo de productos y personas** — fuerte en luz, materiales y piel cuando lo dirigís bien.

**No** confundir con Midjourney ni con DALL-E. Las técnicas que funcionan en esos no transfieren limpio a nano banana.

---

## Las 7 leyes de nano banana

### Ley 1 — Lenguaje natural narrativo, no keywords
Nano banana fue entrenado con captions tipo descripción humana. **Rinde mejor con prosa fluida, no con listas de keywords pegoteadas.**

- ❌ *"perfume bottle, marble, golden hour, 85mm, f/2.0, editorial, luxury, warm tones, cinematic, photorealistic, 8k, masterpiece"*
- ✅ *"Un frasco de perfume sobre un pedestal de mármol gastado, iluminado por la luz cálida del atardecer entrando por una ventana lateral. Tomado con lente de 85mm a f/2.0, mood de lujo silencioso."*

El segundo es **más corto y más efectivo**. Confiá en oraciones completas.

### Ley 2 — Anclá siempre a la imagen de referencia
El producto **debe** salir idéntico entre los N slides del carrusel. La única forma de garantizarlo es mencionar explícitamente la imagen input.

Patrones que funcionan:
- *"Usá la imagen de producto provista como sujeto exacto — conservá envase, etiquetas, colores y proporciones idénticos"*
- *"El producto de la imagen de referencia, sin alteraciones, ubicado en…"*

Patrones que **fallan**:
- No mencionar la imagen input → el modelo "imagina" un producto similar, que deriva entre slides.
- Describir el producto con palabras además de referenciar la imagen → genera conflicto, el modelo prioriza tu descripción y altera el producto.

**Regla**: si tenés imagen input, **no describas el producto con palabras**. Solo ubicalo y dirigí su contexto.

### Ley 3 — Dirección cinematográfica > adjetivos vagos
Nano banana entiende vocabulario fotográfico técnico (lente, apertura, ángulo, calidad de luz). Es lo que más diferencia un prompt amateur de uno pro.

| Vago | Específico |
|---|---|
| *"foto bonita"* | *"tomado con 85mm a f/2.0, ángulo a la altura del producto"* |
| *"buena luz"* | *"luz de ventana lateral suave, temperatura cálida 3200K, con sutil rim light"* |
| *"fondo limpio"* | *"sobre travertino color hueso, espacio negativo generoso en el tercio superior"* |
| *"que se vea profesional"* | *"claridad de formato medio, foco nítido, mood de lujo silencioso"* |

### Ley 4 — Nada de prompts negativos
A diferencia de Stable Diffusion, **nano banana no tiene un campo de negative prompts y no los procesa bien si los embebés**. Frases como *"sin gente, sin desenfoque, sin texto"* tienden a confundir al modelo o a generar exactamente lo que pediste evitar.

**Regla**: describí siempre lo que SÍ querés ver, nunca lo que no.

### Ley 5 — Texto on-image: ser quirúrgico + creativo
Nano banana renderiza texto bien si le das **fuente + peso + color + posición + tamaño relativo + entrecomillado exacto**. Pero "quirúrgico" no es lo mismo que "siempre tercio superior central". El texto on-image es **composición creativa**: cambia de lugar entre stories, juega con jerarquía bold/regular, y a veces necesita que dirijas la imagen detrás (blur, scrim, grade) para que respire.

Las 6 estrategias de placement (cabezal / pie / centro sobre producto / desplazado / wrap / doble peso) y los 6 tratamientos de imagen (blur, scrim, grade, vignette, letterbox, sin tratamiento) están detallados en **`style/text_composition.md`**. Leelo antes de escribir la dimensión 8 de cualquier prompt — sin esto, las N stories de una secuencia salen clonadas.

Best practice (placement clásico):
> Renderizá el titular **"Se absorbe en 30 segundos"** en sans-serif geométrica limpia, peso regular, en verde salvia #8FA086, ubicado en el tercio inferior central del cuadro, ocupando aproximadamente 1/4 del espacio vertical.

Best practice (con tratamiento dirigido para resaltar):
> Renderizá el titular **"Estuvimos en cocinas de grandes restaurantes"** en sans-serif geométrica, peso bold para "grandes restaurantes" y peso regular para el resto (jerarquía a doble peso), en blanco hueso #ECE7DC, ubicado al centro vertical del cuadro ocupando 1/3 del espacio. Para asegurar contraste contra la cocina detrás, aplicá una zona de sombra natural ligeramente oscurecida (grade local del 15%) en la franja del texto, sin que se note como overlay artificial.

Errores comunes:
- No entrecomillar el copy exacto → el modelo "interpreta" el texto y lo modifica.
- Pedir múltiples bloques de texto en un solo slide → suele renderizar uno bien y el otro mal. **Un slide = un bloque de texto principal.**
- Pedir tipografías muy raras o display extremas → fallback a algo similar pero no exacto. Si querés tipografía específica, usá una familia común (serif, sans-serif geométrica, slab, monospace) y describila por características.
- Olvidar el contraste → si el fondo y el texto tienen luminancia similar **en esa zona específica**, el texto se pierde. Si la zona compite, dirigí blur/scrim/grade. **Siempre** asegurá contraste.
- **Clonar placement entre stories** → secuencia plana, parece template de Canva. Variá entre las N stories.

### Ley 6 — Personas: dirigí o salen "AI"
Nano banana puede generar el clásico "rostro de IA" (piel plástica, simetría perfecta, expresión vacía, ojos vidriosos) si no la dirigís. Las claves para mitigar:

1. **Edad concreta**, no "joven" — *"mujer de 38 años"* ≫ *"mujer joven"*.
2. **Textura de piel natural obligatoria** — *"poros visibles, líneas finas, sin sobre-suavizado"*. Esta frase sola elimina el 60% del look IA.
3. **Expresión específica** — *"concentración serena mirándose al espejo"* ≫ *"sonriendo"*.
4. **Pose candid, no posada** — *"momento candid, captura espontánea"*.
5. **Manos visibles → manos descriptas** — siempre describí qué hace la mano, posición de los dedos, qué sostiene. Esto evita los dedos extra clásicos.
6. **Casting realista** — *"belleza realista, no de pasarela"*, *"rostro con carácter"*.
7. **Iluminación que muestre piel** — luz lateral suave > luz frontal plana. La luz plana borra la textura y vuelve plástica la cara.

### Ley 7 — Consistencia entre slides del carrusel
Los N prompts del mismo carrusel deben sentirse como tomados en la misma sesión. Para eso comparten:

- **Misma referencia de imagen del producto** (no negociable)
- **Mismo lente** (ej: 50mm en todos, o 85mm en todos)
- **Misma paleta** (heredada del producto)
- **Mismo mood** (una palabra que define el carrusel entero)
- **Mismo tratamiento general de luz** (ej: todos con luz natural cálida; todos con luz de estudio fría)

Lo que **debe variar** entre slides:
- Ángulo de cámara
- Escena/contexto
- Composición (espacio para texto en distinto lugar)
- Presencia/ausencia de persona
- Distancia (un slide cerrado, otro abierto)

Sin variación → el carrusel se siente repetitivo.
Sin consistencia → el carrusel se siente desarmado.

---

## Errores comunes que la skill debe evitar

### 1. Keyword soup
> ❌ *"perfume, luxury, marble, golden hour, cinematic, 8k, photorealistic, masterpiece, hyperdetailed, professional"*

Pegote de keywords aprendido de Midjourney. En nano banana **degrada** el resultado.

### 2. Doble descripción del producto
> ❌ *"Usá la imagen del producto provisto. Es un frasco alto de vidrio ámbar con tapa dorada y etiqueta serif…"*

Si referenciás la imagen, **no describas el producto**. La descripción compite con la referencia y el modelo termina alterando algo.

### 3. Stacking de adjetivos
> ❌ *"un fondo limpio, minimalista, moderno, profesional, elegante, sofisticado y atemporal"*

Una palabra precisa siempre gana. *"Travertino color hueso"* > los 7 adjetivos juntos.

### 4. Pedir efectos imposibles de cámara
> ❌ *"motion blur cinematográfico mientras el producto rota a 30fps con bokeh anamórfico"*

Stories son imágenes estáticas (aunque el feed sea de 5-15s). Pedir movimiento o efectos de video confunde al modelo.

### 5. Ambigüedad en el texto on-image
> ❌ *"con un titular llamativo arriba"*

¿Qué dice el titular? ¿Qué fuente? ¿Qué color? Sin especificar, sale random o ilegible.

### 6. Asumir que el modelo "sabe" la marca
> ❌ *"con la estética de Aesop"*

A veces funciona, a veces no. **Siempre** describí la estética con sus elementos visuales (paleta, materiales, mood, luz), no con el nombre de la marca.

### 7. Pedir múltiples productos cuando solo hay uno de referencia
Si tenés una sola imagen de referencia, **un solo producto en escena**. Pedirle al modelo "tres frascos en línea" cuando solo le pasaste uno → genera tres frascos diferentes, ninguno consistente.

---

## Trucos específicos por tipo de producto

### Producto con etiqueta tipográfica importante (perfume, vino, skincare)
- Anclá fuerte: *"conservá la tipografía de la etiqueta idéntica, sin alterar"*.
- Evitá ángulos muy oblicuos en el slide hook → la etiqueta se distorsiona.
- Reservá los ángulos creativos para slides de desarrollo.

### Producto reflectivo / metálico / vidrio
- Especificá la fuente de luz porque **se va a reflejar**: *"luz suave de softbox grande para evitar reflejos duros"* o *"reflejos suaves del entorno cálido en el vidrio"*.
- Pedí explícitamente **rim light** para separar del fondo.

### Producto textil / ropa
- Especificá **cómo está dispuesta la prenda**: *"plegada con dobleces precisos"* / *"colgada con caída natural"* / *"vestida sobre un cuerpo con movimiento natural de tela"*.
- Material: *"textura de lino visible"*, *"algodón con leve arrugado natural"*.

### Producto de comida o bebida
- **Frescura**: *"con condensación visible en el vidrio"*, *"con vapor sutil saliendo"*, *"granos de sal recién molida sobre la superficie"*.
- Ángulo: 3/4 alto vende, cenital cuenta.

### Producto pequeño (joyería, accesorios)
- **Macro**: lente 100mm macro, f/2.8, profundidad de campo super superficial.
- Fondo simple para que no compita con el detalle.

### Producto que requiere demostración (cosmético, electrónico)
- Persona en cuadro mostrando uso → ver Ley 6.
- Posición de manos descripta con precisión.

---

## Checklist mental al escribir cada prompt

Antes de cerrar un prompt, preguntate:

- [ ] ¿Anclé a la imagen de referencia en la primera oración?
- [ ] ¿Describí escena específica, no genérica?
- [ ] ¿Especifiqué lente, ángulo, composición, profundidad?
- [ ] ¿Especifiqué fuente, dirección, calidad y temperatura de luz?
- [ ] ¿Definí estilo + textura + mood en una frase precisa?
- [ ] ¿Mencioné la paleta heredada con hex?
- [ ] Si hay persona: ¿edad concreta, textura de piel real, expresión específica, manos descriptas, candid?
- [ ] Si hay texto: ¿copy entrecomillado, fuente, peso, color, posición, tamaño relativo?
- [ ] ¿Cerré con 9:16 + calidad técnica + zona segura?
- [ ] ¿El texto on-image queda dentro del 14%-85% vertical (zona segura de UI de Instagram)?
- [ ] ¿Está en prosa fluida, sin keyword soup?
- [ ] ¿Comparte lente/mood/paleta/luz con los otros prompts de la secuencia?
- [ ] ¿El copy on-image tiene ≤6-8 palabras (más corto que carrusel)?

Si todas las respuestas son sí, el prompt está listo. Si alguna falla, reescribí esa parte antes de pasar a la siguiente story.

---

## Específico de Stories: zona segura de UI de Instagram

Instagram tapa los extremos verticales de cada story con su UI nativa:

| Zona | % del alto vertical | Qué tapa Instagram |
|---|---|---|
| **Superior** | 0% – 14% | Avatar, nombre del usuario, tiempo, ícono de cierre |
| **Centro (zona segura)** | 14% – 85% | Tu contenido visible |
| **Inferior** | 85% – 100% | Input "enviar mensaje", ícono de envío, indicadores |

**Regla**: el texto on-image **siempre** vive entre el 14% y 85% del alto vertical. Si vive en los extremos, queda ilegible o tapado.

**Trucos prácticos**:
- Si querés texto "arriba", ubicalo en el **tercio superior central** (~20-35% del alto), no en el borde superior.
- Si querés texto "abajo", ubicalo en el **tercio inferior central** (~65-80% del alto), no en el borde inferior.
- Para CTAs con sticker de Link, dejá el último 15% del cuadro **vacío de texto importante** — ahí va el sticker o el indicador de tap-up.
- Stickers de engagement (poll, quiz, pregunta) suelen ubicarse en el tercio inferior (zona ~70-85%) — si tu copy on-image vive ahí, el sticker lo va a tapar. Movelo arriba.
