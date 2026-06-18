# 05 — Prompt Engineering (nano-banana + gpt-image)

Este archivo no repite el template. El template (`templates/prompt_template.md`) define **qué** poner en el prompt — las 9 dimensiones obligatorias en orden fijo aplican para **ambos modelos**. Este archivo define **cómo** escribir el prompt según el modelo elegido en Decisions para `instructions/07_generation.md`, porque **nano-banana y gpt-image responden a estímulos distintos**.

**Regla**: el modelo se eligió en el paso 3 (Decisions). En el paso 5 escribís el prompt **aplicando las leyes del modelo elegido para ese slide**. No mezcles: un prompt nano-banana corrido en gpt-image, o al revés, degrada el resultado.

- Slide marcado `nano-banana` → aplicá **"Las 7 leyes de nano-banana"** (abajo).
- Slide marcado `gpt-image` → aplicá **"Las 7 leyes de gpt-image"** (al final de este archivo).
- Las dimensiones del template son las mismas; lo que cambia es **el tono y la precisión** con que las escribís.

---

## Qué es nano banana

**Nano banana** es el nombre informal de **Gemini 2.5 Flash Image** (Google). Es un modelo de generación de imágenes optimizado para:

1. **Consistencia con imágenes de referencia** — su superpoder. Le pasás una imagen y la respeta con altísima fidelidad (packaging, rostro, objeto). Por eso es el modelo correcto para carruseles de e-commerce: el producto se mantiene idéntico en los N slides.
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

### Ley 5 — Texto on-image: ser quirúrgico
Nano banana renderiza texto bien si le das **fuente + peso + color + posición + tamaño relativo + entrecomillado exacto**. Si dejás algo al azar, sale mal.

Best practice:
> Renderizá el titular **"Se absorbe en 30 segundos"** en sans-serif geométrica limpia, peso regular, en verde salvia #8FA086, ubicado en la zona inferior del cuadro, ocupando aproximadamente 1/4 del espacio vertical.

Errores comunes:
- No entrecomillar el copy exacto → el modelo "interpreta" el texto y lo modifica.
- Pedir múltiples bloques de texto en un solo slide → suele renderizar uno bien y el otro mal. **Un slide = un bloque de texto principal.**
- Pedir tipografías muy raras o display extremas → fallback a algo similar pero no exacto. Si querés tipografía específica, usá una familia común (serif, sans-serif geométrica, slab, monospace) y describila por características.
- Olvidar el contraste → si el fondo y el texto tienen luminancia similar, el texto se pierde. **Siempre** asegurá contraste.

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

Carruseles son imágenes estáticas. Pedir movimiento o efectos de video confunde al modelo.

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

---

## Qué es gpt-image

**gpt-image** es **GPT Image 1** (OpenAI). Es un modelo de generación de imágenes optimizado para:

1. **Render de texto legible y ortografía correcta** — su superpoder. Renderiza títulos, párrafos cortos, bullets, datos y badges con tipografía limpia y sin caracteres deformados, incluso en español con tildes y ñ. Es muy superior a nano-banana acá.
2. **Seguimiento estricto de layout** — respeta jerarquía, posición, proporciones y composiciones tipo poster/infografía con alta precisión.
3. **Diseño gráfico y data viz** — diagramas, comparativas, tablas, charts, líneas conectoras, hub-and-spoke con etiquetas.
4. **Colores hex precisos y fondos planos** — respeta colores hex y permite fondos transparentes o sólidos limpios cuando lo pedís.

**No** es tan fuerte como nano-banana en **fidelidad exacta a una imagen de referencia** (puede reinterpretar el producto/logo entre generaciones) ni en **fotorrealismo de productos físicos** específicos.

---

## Las 7 leyes de gpt-image

### Ley 1 — Layout estructurado funciona, sé explícito
gpt-image **entiende y respeta** indicaciones explícitas de layout. Mientras que en nano-banana decís *"ubicado en la zona inferior del cuadro"*, en gpt-image podés (y debés) ser más cuantitativo:

- ✅ *"El titular ocupa el 25% superior del cuadro, alineado al centro horizontal, con margen del 8% al borde superior. Debajo del titular, el producto centrado ocupa el 50% del cuadro vertical."*
- También sirve: *"composición de tres bandas horizontales — banda superior con headline, banda central con producto, banda inferior con CTA pill"*.

Cuanto más estructurado el slide (infografía, comparativa, tabla), más rinde una indicación cuantitativa.

### Ley 2 — Referencia se pasa, pero la fidelidad es secundaria
Si pasás `reference_image_urls`, gpt-image las usa como **inspiración**, no como sujeto exacto. El producto puede **reinterpretarse** entre slides. Por eso:

- Si la consistencia del producto entre slides es **crítica** → ese slide debería estar marcado `nano-banana`, no gpt-image (volvé a Decisions y corregí).
- Si igual va por gpt-image (porque manda el texto/gráfica) → reforzá la referencia con descripción detallada del producto en palabras (forma, color, label visible). gpt-image necesita más palabras de lo que nano-banana necesita.

Patrón válido:
- *"Render the product shown in the reference image as the central subject — a small matte black bottle with a thin white label, cream sand text, photographed in studio."*

### Ley 3 — Texto on-image: especificá ortografía exacta
gpt-image es muy bueno en texto, pero **se le tiene que decir exactamente qué renderizar**. Patrones que funcionan:

- *"Render the headline EXACTLY as written, no character changes: «Grasas esenciales en su forma más pura»"* (las comillas francesas o las dobles le señalan los límites del literal).
- *"Render the text in Spanish, preserving accents (á é í ó ú) and the letter «ñ» without alteration."*
- Combinalo siempre con: **fuente** (familia o descripción) + **peso** (regular / medium / bold) + **color hex** + **alineación** + **tamaño relativo** (1/4 del cuadro, etc.).

**Anti-patrón**: dejar el copy "al estilo de" sin escribirlo literal. Falla.

### Ley 4 — Nada de prompts negativos (igual que nano-banana)
gpt-image también prefiere instrucciones positivas. No le digas *"sin sombras, sin texturas, sin gente"*. Decile lo que SÍ querés: *"fondo plano color cream sand #E8DDC8 sin texturas, sin elementos adicionales"*.

### Ley 5 — Colores hex y fondos: respetá la precisión
gpt-image **respeta colores hex** mucho mejor que la mayoría. Aprovechá:

- *"El fondo es un magenta saturado plano #E91E63, sin gradientes, sin texturas, sin sombras."*
- *"Render the text in #FFD500 (bright yellow), the secondary text in #FFFFFF."*

Si el slide es **flat design / brand-driven** (como Panda Kids con sus bloques pink + sky blue + amarillo), gpt-image es la elección correcta porque lo respeta hex por hex.

### Ley 6 — Personas: sigue las 7 disciplinas, especificá fotorrealismo
gpt-image tiende a **estilizar más** que nano-banana. Si querés persona fotorrealista, especificalo explícito:

- *"Photorealistic real photography, not illustration, not 3D render."*
- Aplicá igual las 7 disciplinas anti-AI-face (edad concreta, textura de piel natural, expresión específica, manos descriptas, pose candid, casting realista, luz que respete piel).

Si en cambio querés ilustración o flat brand graphic, gpt-image rinde **muy bien** — pedilo: *"flat vector illustration, kids brand aesthetic"*.

### Ley 7 — Consistencia entre slides: trabajalo desde el sistema visual
Como gpt-image puede reinterpretar el producto/logo, la consistencia entre slides se mantiene desde el **sistema visual compartido**:

- **Misma paleta hex** declarada en cada prompt.
- **Misma familia tipográfica** descripta de la misma forma.
- **Mismo fondo** (color o sistema gráfico).
- **Mismas reglas de layout** (grilla, márgenes, esquinas).
- **Mismo dispositivo gráfico recurrente** (brand mark, sello, doodles, pills).

Si el producto necesita ser idéntico → ese slide va con nano-banana, no acá.

---

## Diferencias rápidas en cómo lo prompteás

| Aspecto | nano-banana | gpt-image |
|---|---|---|
| Estilo de redacción | Prosa cinematográfica narrativa | Prosa estructurada con datos cuantitativos |
| Referencia de producto | Anclá fuerte ("usá la imagen como sujeto exacto") | Pasala + describí el producto en palabras |
| Texto on-image | Corto, entrecomillado | Largo OK, marcá ortografía exacta y caracteres especiales |
| Layout | Descripción visual ("zona superior") | Cuantitativa ("25% superior, margen 8%") |
| Colores hex | Lista en paleta heredada | Asignados explícitamente a cada elemento |
| Fondo | Escena fotográfica realista | Plano hex limpio O escena (ambos sirven) |
| Persona | "Belleza realista, textura de piel natural" | Agregar "photorealistic real photography" |
| Estilo gráfico (flat/vector) | Falla / mediocre | Excelente |

---

## Checklist mental al escribir cada prompt

Antes de cerrar un prompt, preguntate:

**Comunes a ambos modelos:**
- [ ] ¿Anclé/referencié la imagen de producto en la primera oración?
- [ ] ¿Describí escena específica, no genérica?
- [ ] ¿Especifiqué lente, ángulo, composición, profundidad?
- [ ] ¿Especifiqué fuente, dirección, calidad y temperatura de luz?
- [ ] ¿Definí estilo + textura + mood en una frase precisa?
- [ ] ¿Mencioné la paleta heredada con hex?
- [ ] Si hay persona: ¿edad concreta, textura de piel real, expresión específica, manos descriptas, candid?
- [ ] Si hay texto: ¿copy entrecomillado, fuente, peso, color hex, posición, tamaño relativo?
- [ ] ¿Cerré con 4:5 + calidad técnica?
- [ ] ¿Está en prosa fluida, sin keyword soup?
- [ ] ¿Comparte lente/mood/paleta/luz/sistema visual con los otros prompts del carrusel?

**Si es nano-banana, además:**
- [ ] ¿El anclaje a la imagen es la primera oración del prompt, contundente ("usá la imagen como sujeto exacto, sin alterar")?
- [ ] ¿Evité describir el producto con palabras (compite con la referencia)?
- [ ] ¿La descripción es cinematográfica narrativa, no cuantitativa?
- [ ] Si hay texto, ¿es corto (≤10 palabras) y está entrecomillado?
- [ ] ¿Cero prompts negativos? ¿Cero keyword soup?

**Si es gpt-image, además:**
- [ ] ¿Especifiqué el layout con datos cuantitativos (porcentajes, márgenes)?
- [ ] ¿Marqué la ortografía exacta del texto on-image y los caracteres especiales (tildes, ñ)?
- [ ] ¿Asigné un hex explícito a cada elemento de texto y al fondo?
- [ ] Si hay persona fotorrealista, ¿agregué "photorealistic real photography, not illustration"?
- [ ] ¿La consistencia entre slides está asegurada vía paleta + tipografía + layout (no vía referencia exacta del producto)?
- [ ] ¿Cero prompts negativos?

Si todas las respuestas son sí, el prompt está listo. Si alguna falla, reescribí esa parte antes de pasar al siguiente slide.
