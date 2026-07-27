---
name: prompt-craft
description: "Conocimiento universal de prompt engineering para generación y edición de imágenes con cualquier modelo (Gemini multimodal, gpt-image, Imagen). Se carga siempre que la tarea involucre escribir o ajustar un prompt para generate_image. Cubre: leyes del prompting cinematográfico, cómo anclar referencias por modelo, edit vs generate, personas, errores comunes."
language: es
---

# Prompt Craft

Esta skill es **conocimiento, no workflow**. No te dice qué pasos seguir — te dice cómo escribir prompts que funcionen, sea para una imagen suelta, una story, un carrusel, un edit, o lo que sea. El flow lo decidís vos según el pedido.

Aplica a TODO formato (story, carrusel, post, edit, single image) y a TODOS los modelos vía `generate_image`.

## Las 7 leyes del prompting cinematográfico

### Ley 1 — Lenguaje natural narrativo, no keywords

Los modelos modernos (Gemini, gpt-image, Imagen) fueron entrenados con captions tipo descripción humana. **Rinden mejor con prosa fluida, no con listas de keywords pegoteadas.**

- ❌ *"perfume bottle, marble, golden hour, 85mm, f/2.0, editorial, luxury, warm tones, cinematic, photorealistic, 8k, masterpiece"*
- ✅ *"Un frasco de perfume sobre un pedestal de mármol gastado, iluminado por la luz cálida del atardecer entrando por una ventana lateral. Tomado con lente de 85mm a f/2.0, mood de lujo silencioso."*

El segundo es **más corto y más efectivo**. Confiá en oraciones completas.

### Ley 2 — Anclá siempre a la imagen de referencia

Si tenés una imagen como input (producto, persona, estilo), **el producto/sujeto debe salir idéntico** a esa referencia. La única forma de garantizarlo: mencionar explícitamente la imagen.

Patrones que funcionan:
- *"Usá la imagen de producto provista como sujeto exacto — conservá envase, etiquetas, colores y proporciones idénticos."*
- *"El producto de la imagen de referencia, sin alteraciones, ubicado en…"*

Patrones que **fallan**:
- No mencionar la imagen input → el modelo "imagina" un producto similar y deriva entre piezas.
- Describir el producto con palabras además de referenciarlo → genera conflicto, el modelo prioriza tu descripción y altera el producto.

**Regla**: si tenés imagen input, **no describas el producto con palabras**. Solo ubicalo y dirigí su contexto.

### Ley 3 — Dirección cinematográfica, no adjetivos vagos

Los modelos entienden vocabulario fotográfico técnico (lente, apertura, ángulo, calidad de luz). Es lo que más diferencia un prompt amateur de uno pro.

| Vago | Específico |
|---|---|
| *"foto bonita"* | *"tomado con 85mm a f/2.0, ángulo a la altura del producto"* |
| *"buena luz"* | *"luz de ventana lateral suave, temperatura cálida 3200K, con sutil rim light"* |
| *"fondo limpio"* | *"sobre travertino color hueso, espacio negativo generoso en el tercio superior"* |
| *"que se vea profesional"* | *"claridad de formato medio, foco nítido, mood de lujo silencioso"* |

### Ley 4 — Nada de prompts negativos

Los modelos modernos no procesan bien frases tipo *"sin gente, sin desenfoque, sin texto"*. Tienden a confundirse o a generar exactamente lo que pediste evitar.

**Regla**: describí siempre lo que SÍ querés ver, nunca lo que no.

### Ley 5 — Texto on-image: quirúrgico + creativo

Cuando el prompt incluye copy renderizado en la imagen, especificá: **fuente + peso + color + posición + tamaño relativo + entrecomillado exacto**.

Best practice:
> Renderizá el titular **"Se absorbe en 30 segundos"** en sans-serif geométrica limpia, peso regular, en verde salvia #8FA086, ubicado en el tercio inferior central del cuadro, ocupando aproximadamente 1/4 del espacio vertical.

Errores comunes:
- No entrecomillar el copy exacto → el modelo "interpreta" y modifica el texto.
- Pedir múltiples bloques de texto en un solo cuadro → suele renderizar uno bien y el otro mal. **Una imagen = un bloque de texto principal.**
- Pedir tipografías display extremas → fallback a algo similar pero no exacto. Usá familias comunes (serif, sans-serif geométrica, slab, monospace) descriptas por características.
- Olvidar el contraste local → si el fondo y el texto tienen luminancia parecida **en esa zona**, el texto se pierde. Si la zona compite, dirigí blur/scrim/grade explícito.

Las reglas específicas de **dónde** poner el texto (zona segura de UI, jerarquía cross-pieza) viven en cada skill de formato.

### Ley 6 — Personas: dirigí o salen "AI"

Sin dirección, los modelos generan el clásico "rostro IA" (piel plástica, simetría perfecta, expresión vacía, ojos vidriosos). Mitigaciones:

1. **Edad concreta**, no "joven" — *"mujer de 38 años"* ≫ *"mujer joven"*.
2. **Textura de piel natural obligatoria** — *"poros visibles, líneas finas, sin sobre-suavizado"*. Esta frase elimina ~60% del look IA.
3. **Expresión específica** — *"concentración serena mirándose al espejo"* ≫ *"sonriendo"*.
4. **Pose candid, no posada** — *"momento candid, captura espontánea"*.
5. **Manos visibles → manos descriptas** — siempre describí qué hace la mano, posición de los dedos, qué sostiene. Evita los dedos extra clásicos.
6. **Casting realista** — *"belleza realista, no de pasarela"*, *"rostro con carácter"*.
7. **Iluminación que muestre piel** — luz lateral suave > luz frontal plana. La luz plana borra textura y aplasta.

### Ley 7 — Consistencia entre piezas de una secuencia

Si vas a generar N imágenes que viven juntas (carrusel, secuencia de stories, set de variaciones), tienen que sentirse tomadas en la misma sesión. Comparten:

- **Misma referencia del producto** (no negociable).
- **Mismo lente** (50mm en todas, o 85mm en todas — no mezcles).
- **Misma paleta** (heredada del producto).
- **Mismo mood** (una palabra que define la secuencia entera).
- **Mismo tratamiento general de luz**.

Lo que **debe variar**:
- Ángulo de cámara.
- Escena/contexto.
- Composición (espacio para texto en distinto lugar).
- Distancia (una pieza cerrada, otra abierta).

Sin variación → la secuencia se siente repetitiva. Sin consistencia → se siente desarmada.

---

## EDIT vs GENERATE — la distinción clave

Editar una imagen NO es lo mismo que regenerar una. Confundirlos es el error más caro porque deshace cambios pedidos.

### Generate (from scratch o con refs como inspiración)
El usuario quiere una imagen nueva. Las refs (si hay) son **inspiración / consistencia de producto**.

- Prompt = descripción completa de la escena.
- Refs = producto + opcionalmente estilos o moods.
- Resultado: imagen nueva alineada con las refs.

### Edit (modificar una imagen existente)
El usuario tiene una imagen base y quiere cambiarle algo: el fondo, un elemento, el copy, el color.

**Reglas duras:**
1. **La imagen original es la PRIMERA `reference_path`.** No una más en la lista — la primera. Es la base sobre la que se edita.
2. **El prompt describe SOLO el delta**, no la imagen entera. Ejemplo:
   - ❌ *"Un frasco de perfume sobre mármol con luz cálida y un titular 'XYZ'… ahora con fondo más oscuro."*
   - ✅ *"Tomá la imagen base y oscurecé el fondo: cambialo de mármol claro a piedra carbón, manteniendo el resto idéntico (producto, luz, composición, texto)."*
3. **Mencioná explícitamente lo que NO debe cambiar.** "Manteniendo el producto, la composición y el texto idénticos" reduce drift.
4. Si hay otras refs (ej: una imagen-estilo a copiar), van **después** de la imagen base.
5. **Pasá el `aspect_ratio` de la pieza original SIEMPRE.** Sin ese param el modelo cambia las dimensiones del output (de 9:16 termina sacando 16:9). Es param de la tool, no se mete en el prompt.

### Cuándo elegir qué modelo

| Caso | Modelo |
|---|---|
| Generate con refs (consistencia de producto, multi-image) | `google/gemini-3-pro-image` (alta calidad) o `google/gemini-2.5-flash-image-preview` (rápido) |
| Edit puntual de una imagen existente | `openai/gpt-image-1` (la tool ya rutea por `/v1/images/edits` cuando hay refs) o Gemini multimodal |
| Generate sin refs (texto puro a imagen) | Gemini, gpt-image, o `google/imagen-4.0-generate-001` |
| Iteración rápida (variaciones, drafts) | `google/gemini-2.5-flash-image-preview` |
| Output final de campaña | `google/gemini-3-pro-image` |

**Default razonable**: Gemini Pro para final, Gemini Flash para iterar.

---

## Cómo se pasan las refs por modelo (importante)

La tool `generate_image` abstrae esto, pero conviene saber qué hace por debajo para escribir bien el prompt:

- **Gemini multimodal** (`gemini-3-pro-image`, `gemini-2.5-flash-image-preview`): las refs viajan como bloques `image_url` en `chat/completions`. Funciona perfecto con texto + N imágenes. **Pasale las refs, mencionalas en el prompt.**
- **gpt-image** (`openai/gpt-image-1`, `gpt-image-2`): si pasás `reference_paths`, la tool va por `/v1/images/edits` (multipart). La primera imagen es la "base", las demás son adicionales. Si NO pasás refs, va por `/v1/images/generations` (texto puro).
- **Imagen / Flux / Grok-Imagine**: solo `/generations`, NO soportan refs. Si pedís refs con esos modelos, la tool tira error explícito — usá Gemini o gpt-image.

**Regla simple**: si querés refs y dudás, usá Gemini.

---

## Errores comunes (anti-patrones)

### 1. Keyword soup
> ❌ *"perfume, luxury, marble, golden hour, cinematic, 8k, photorealistic, masterpiece, hyperdetailed, professional"*

Pegote estilo Midjourney. **Degrada** el resultado en modelos modernos.

### 2. Doble descripción del producto
> ❌ *"Usá la imagen del producto provisto. Es un frasco alto de vidrio ámbar con tapa dorada y etiqueta serif…"*

Si referenciás la imagen, **no describas el producto**. Compite con la referencia.

### 3. Stacking de adjetivos
> ❌ *"un fondo limpio, minimalista, moderno, profesional, elegante, sofisticado y atemporal"*

Una palabra precisa siempre gana. *"Travertino color hueso"* > los 7 adjetivos juntos.

### 4. Pedir efectos imposibles de cámara
> ❌ *"motion blur cinematográfico mientras el producto rota a 30fps con bokeh anamórfico"*

Las piezas son imágenes estáticas. Pedir movimiento confunde al modelo.

### 5. Ambigüedad en el texto on-image
> ❌ *"con un titular llamativo arriba"*

¿Qué dice? ¿Qué fuente? ¿Qué color? Sin especificar, sale random o ilegible.

### 6. Asumir que el modelo "sabe" la marca
> ❌ *"con la estética de Aesop"*

A veces funciona, a veces no. **Siempre** describí la estética con sus elementos visuales (paleta, materiales, mood, luz), no con el nombre de la marca.

### 7. Pedir múltiples productos cuando solo hay uno de referencia
Una sola ref de producto, **un solo producto en escena**. Pedirle "tres frascos en línea" → genera tres frascos diferentes, ninguno consistente.

### 8. Edit que se vuelve generate
Pedir un edit y describir la imagen entera en el prompt. Ver sección "EDIT vs GENERATE" arriba.

---

## Trucos por tipo de producto

### Producto con etiqueta tipográfica importante (perfume, vino, skincare)
- Anclá fuerte: *"conservá la tipografía de la etiqueta idéntica, sin alterar"*.
- Evitá ángulos muy oblicuos en piezas hero → la etiqueta se distorsiona.
- Reservá ángulos creativos para piezas de desarrollo.

### Producto reflectivo / metálico / vidrio
- Especificá la fuente de luz porque **se va a reflejar**: *"luz suave de softbox grande para evitar reflejos duros"* o *"reflejos suaves del entorno cálido en el vidrio"*.
- Pedí explícitamente **rim light** para separar del fondo.

### Producto textil / ropa
- Cómo está dispuesta la prenda: *"plegada con dobleces precisos"* / *"colgada con caída natural"* / *"vestida sobre un cuerpo con movimiento natural de tela"*.
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

## Estructura mental de un prompt cinematográfico

Un prompt sólido cubre estas dimensiones (en este orden, en prosa fluida):

```
[Anclaje a referencia si hay]. [Escena y contexto].
[Cámara: lente, ángulo, composición, profundidad de campo].
[Iluminación: fuente + dirección + calidad + temperatura].
[Estilo + textura + mood en una frase].
[Paleta heredada con hex].
[Persona — si aplica, con Ley 6].
[Texto on-image — si aplica, con detalle de Ley 5].
[Calidad técnica de cierre — fotorrealismo, foco, resolución].
```

**El aspect ratio NO va en el texto del prompt.** Va como parámetro `aspect_ratio` en `generate_image` (valores: `1:1`, `4:5`, `9:16`, `16:9`, etc.). Sin ese param el modelo elige uno por su cuenta y rompe la pieza, especialmente en edits. Las dimensiones de **formato** (aspect, zona segura, número de piezas) viven en las skills de formato (`ig-post`, `ig-story`, `ig-stories-secuencia`, `ig-carousel`).

---

## Checklist mental al cerrar un prompt

- [ ] ¿Anclé a la referencia (si hay) en la primera oración?
- [ ] ¿Describí escena específica, no genérica?
- [ ] ¿Especifiqué lente, ángulo, composición, profundidad?
- [ ] ¿Especifiqué fuente, dirección, calidad y temperatura de luz?
- [ ] ¿Definí estilo + textura + mood en una frase precisa?
- [ ] ¿Mencioné la paleta con hex?
- [ ] Si hay persona: ¿edad concreta, textura natural, expresión específica, manos descriptas, candid?
- [ ] Si hay texto: ¿copy entrecomillado, fuente, peso, color, posición, tamaño?
- [ ] ¿Está en prosa fluida, sin keyword soup?
- [ ] Si es parte de secuencia: ¿comparte lente/mood/paleta/luz con las otras?
- [ ] Si es edit: ¿el prompt describe SOLO el delta y la imagen base es la primera ref?
- [ ] ¿Pasaste `aspect_ratio` como parámetro (no en el texto del prompt)? Para edits, ¿es el mismo aspect que la imagen base?

Si todas son sí, el prompt está listo.
