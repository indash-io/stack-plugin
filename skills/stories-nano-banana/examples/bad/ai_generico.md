# Ejemplos MALOS — Qué NO hacer

Este archivo entrena el **criterio negativo**: cómo se ve un output mal hecho y por qué falla. Si la skill se encuentra produciendo algo similar, frená y reescribí.

---

## MALO #1 — Keyword soup (estilo Midjourney)

**Prompt malo**:

```
perfume bottle, amber glass, marble pedestal, golden hour, mediterranean, 85mm, f/2.0, editorial, luxury, warm tones, cinematic, photorealistic, 8k, masterpiece, hyperdetailed, professional photography, beautiful lighting, vibrant
```

**Por qué falla**:
1. Lista de keywords pegoteada — nano banana fue entrenado con captions narrativos, no con strings de keywords. Degrada el resultado.
2. Adjetivos vagos apilados ("luxury, warm, cinematic, beautiful") — ninguno aporta dirección concreta.
3. Sin anclaje a la imagen de referencia — el modelo va a generar un perfume genérico, no el del usuario.
4. Sin texto on-image especificado — ¿qué dice el story?
5. "8k, masterpiece" — vocabulario aprendido de Midjourney que en nano banana no aporta.
6. Sin paleta heredada con hex.
7. Sin aspect ratio.

**Cómo se hace bien**: ver `examples/good/listicle_cocina.md` — story 1.

---

## MALO #2 — Doble descripción del producto

**Prompt malo**:

```
Usá la imagen del producto provisto. El producto es un frasco alto de vidrio ámbar con tapa dorada metalizada y etiqueta blanca con tipografía serif. Mide aproximadamente 12cm de alto. Ubicalo sobre un pedestal de mármol blanco italiano...
```

**Por qué falla**:
1. Después de referenciar la imagen, **describe el producto con palabras**. La descripción compite con la referencia y el modelo termina alterando el frasco (cambia altura, cambia matiz del ámbar, cambia tipografía).
2. Detalles del producto ("12cm de alto", "tapa metalizada") son innecesarios — la imagen los aporta.
3. Resultado: el producto sale **distinto** entre storys porque cada prompt lo redescribe levemente diferente.

**Regla rota**: B5 — Nunca describas el producto desde cero. Solo ubicalo y dirigí su contexto.

**Cómo se hace bien**:
> *"Usá la imagen de producto provista como sujeto exacto — conservá envase, etiquetas, colores y proporciones idénticos — y ubicá el frasco sobre un pedestal de mármol blanco italiano…"*

---

## MALO #3 — Copy on-image vago / marketing-speak

**Slides malos**:

| # | Copy malo |
|---|---|
| 1 | "Descubrí la diferencia" |
| 2 | "Calidad superior, ingredientes premium" |
| 3 | "Resultados que se notan" |
| 4 | "Sumate a la familia" |

**Por qué falla**:
1. Slide 1: "Descubrí la diferencia" — ¿qué diferencia? No detiene el scroll, no genera curiosidad. Genérico.
2. Slide 2: "Calidad superior, ingredientes premium" — palabras prohibidas (premium, superior). Ninguna se puede sostener con un hecho.
3. Slide 3: "Resultados que se notan" — ¿qué resultados? ¿en cuánto tiempo? ¿en qué? Cero especificidad.
4. Slide 4: "Sumate a la familia" — CTA poético, no accionable. ¿Qué hago? ¿Comprar? ¿Seguir? ¿Suscribirme? Sin verbo concreto.

**Cómo se hace bien**:

| # | Copy bueno |
|---|---|
| 1 | "Por qué dura 12+ horas" |
| 2 | "01 · Liberación gradual de moléculas" |
| 3 | "Probado en 200 personas · 89% notó cambio en 6 semanas" |
| 4 | "Probalo 30 días · garantía total" |

**Regla rota**: A2 (especificidad), A8 (sin marketing-speak), A10 (CTA accionable).

---

## MALO #4 — Persona genérica "AI face"

**Prompt malo (fragmento)**:

```
Una mujer joven y hermosa con piel perfecta sosteniendo el producto, sonriendo a la cámara, fondo borroso, look profesional.
```

**Por qué falla**:
1. **"Joven y hermosa"** → modelo genera la cara IA estándar (simétrica, sobre-suavizada, vacía).
2. **"Piel perfecta"** → activa el sobre-suavizado plástico que delata el AI face.
3. **"Sonriendo"** → expresión genérica e inespecífica → sonrisa de catálogo.
4. **"Sosteniendo el producto"** → sin describir las manos → manos deformadas, dedos extra.
5. **"Fondo borroso"** → vago. ¿Qué tipo de fondo? ¿Qué luz?
6. **"Look profesional"** → palabra vacía.

**Cómo se hace bien**:
> *"Una persona real, mujer de 38 años de fenotipo latino, con textura de piel natural visible (poros, leves líneas finas bajo los ojos, asimetrías humanas, sin sobre-suavizado), pelo castaño oscuro a la altura de los hombros recogido suelto en un rodete bajo, vistiendo una camisa de lino blanco sin estructurar. Aplicando una pequeña cantidad de crema con el dedo medio de la mano derecha sobre su pómulo derecho, dedos relajados y visibles claramente. Expresión: concentración serena, mirándose en un espejo fuera de cuadro, ojos entrecerrados naturalmente. Captura espontánea, momento candid, no posada."*

**Regla rota**: B11 (las 7 disciplinas para personas).

---

## MALO #5 — Prompt negativo embebido

**Prompt malo (fragmento)**:

```
... iluminado por luz natural, sin gente en la escena, sin desenfoque excesivo, sin texto adicional, sin marcas de agua, sin distorsión, sin manos visibles, fondo limpio sin elementos distractores...
```

**Por qué falla**:
1. Nano banana **no procesa bien prompts negativos**. Tiende a generar exactamente lo que pediste evitar (la palabra activa el concepto).
2. Resultado típico: aparece gente, aparece texto extra, aparecen elementos en el fondo.
3. Lista larga de "sin X, sin Y, sin Z" parece ordenada pero está saboteando el output.

**Cómo se hace bien**:
> *"... iluminado por luz natural difusa, escena de producto en foco único, fondo de mármol travertino limpio sin otros objetos en cuadro."*

(Describí lo que SÍ querés ver, no lo que NO.)

**Regla rota**: B6 (cero prompts negativos).

---

## MALO #6 — Workflow saltado: generar sin confirmar

**Conversación mala**:

```
User: Carrusel para [URL] con esta imagen [imagen].
Skill: ¡Genial! Acá tenés tu secuencia de stories de 5 storys...
[entrega los prompts directo]
```

**Por qué falla**:
1. Salta el paso 3 (Decisions). El user no confirmó tipo, storys, hook, mood.
2. La skill decidió todo sola sin propuesta visible. Si algo está mal, el user tiene que pedir cambios sobre algo ya hecho — pérdida de tiempo y tokens.
3. **Regla no-negociable rota**: siempre se confirma antes de generar.

**Cómo se hace bien**:
- Recibe URL + imagen → silencio (Discovery) → pregunta consolidada con propuestas → user confirma/edita → genera.

---

## MALO #7 — Inconsistencia entre storys

**Síntoma**: el mismo secuencia de stories tiene:
- Slide 1: lente 85mm, luz cálida, mood lujo silencioso, paleta neutros cálidos.
- Slide 2: lente 35mm, luz fría, mood enérgico, paleta saturada.
- Slide 3: vuelta a 85mm, otra paleta más.

**Por qué falla**: parece tres secuencia de storieses distintos pegados, no uno solo. El user lo posta y se ve incoherente en el feed.

**Regla rota**: B10 (consistencia entre prompts) + ley 7 de prompt_engineering.

**Cómo se hace bien**: lente, mood, paleta y luz general son **iguales** en todos los storys. Lo que cambia es ángulo + escena + composición.

---

## MALO #8 — Texto on-image sin dirección

**Prompt malo (fragmento)**:

```
... con un titular llamativo en la parte superior que diga algo sobre la duración del producto, en una tipografía moderna...
```

**Por qué falla**:
1. **"Algo sobre la duración"** → el modelo inventa el copy, sale "Long Lasting Effect" o cualquier cosa.
2. **"Tipografía moderna"** → vago, fallback random.
3. **"Llamativo"** → no es una dirección, es un adjetivo vacío.
4. Sin color, sin posición exacta, sin tamaño relativo.

**Cómo se hace bien**:
> *"Renderizá el titular "Por qué dura 12+ horas" en serif moderna de alto contraste (coincidente con la tipografía de la etiqueta), peso regular, en color ámbar profundo #6B3410, ubicado en la zona superior del cuadro, ocupando aproximadamente 1/4 del espacio vertical, con espacio negativo generoso debajo separando el titular del producto."*

**Regla rota**: B8 (texto entre comillas + dirección completa).

---

## MALO #9 — Texto fuera de la zona segura de Instagram (exclusivo Stories)

**Prompt malo (fragmento)**:

```
... Renderizá el titular "Por qué dura 12+ horas" en serif moderna, en la zona superior del cuadro, ocupando el 5% superior, justo en el borde de arriba para que se vea grande y dramático ...
```

**Por qué falla**:
1. El **5% superior del cuadro** está **tapado por la UI nativa de Instagram** (avatar del usuario, nombre, indicador de tiempo). El titular queda ilegible o cortado.
2. La regla es: el texto vive entre el **14% y 85%** del alto vertical. Cualquier cosa fuera de ese rango se pierde.
3. Lo mismo aplica al **15% inferior** — ahí va el input de "enviar mensaje" y el texto se tapa.

**Cómo se hace bien**:
> *"... Renderizá el titular "Por qué dura 12+ horas" en serif moderna, ubicado en el tercio superior central del cuadro dentro de la zona segura de UI (entre el 14% y 85% del alto vertical, evitando los bordes superior e inferior tapados por Instagram), ocupando aproximadamente 1/3 del espacio vertical ..."*

**Regla rota**: B13 (zona segura) + Ley específica de Stories.

---

## MALO #10 — Copy on-image largo en Stories (12+ palabras)

**Stories malas**:

| # | Copy malo |
|---|---|
| 1 | "Descubrí por qué tu protector solar no te está protegiendo realmente" |
| 2 | "El 89% de las personas no aplican la cantidad correcta y eso es un problema" |

**Por qué falla**:
1. Stories tienen **5-15 segundos de auto-advance**. Con 12+ palabras, el usuario no llega a leerlo antes de que pase la siguiente story.
2. El máximo en Stories es **6-8 palabras** (más corto que carrusel). Idealmente 3-6.
3. Con copy largo, además, el texto ocupa demasiado espacio vertical y deja al producto sin protagonismo.

**Cómo se hace bien**:

| # | Copy bueno |
|---|---|
| 1 | "¿Por qué no te protege?" |
| 2 | "El 89% aplica muy poco" |

**Regla rota**: A1 (brevedad — max 6-8 palabras en Stories).

---

## MALO #11 — Olvidar el sticker en el shot list

**Output malo**: el shot list de la secuencia de stories no incluye la columna "Sticker sugerido" o la última story no tiene Link.

**Por qué falla**:
1. Los stickers son **parte del lenguaje nativo de Stories**. Sin sticker en la última story, no hay link al producto.
2. La skill prometió entregar sugerencias de stickers en el brief — si no aparecen, falla la promesa.
3. El user tiene que armar los stickers después en Instagram, así que necesita saber qué poner dónde.

**Cómo se hace bien**: cada story en el shot list tiene su sticker (puede ser "ninguno" si la composición lo pide). **La última story siempre tiene Link**.

---

## Resumen de errores recurrentes

1. ❌ Keyword soup en lugar de prosa.
2. ❌ Doble descripción del producto (referencia + texto).
3. ❌ Copy genérico, marketing-speak, CTAs poéticos.
4. ❌ Personas sin las 7 disciplinas.
5. ❌ Prompts negativos.
6. ❌ Saltarse el paso de confirmación.
7. ❌ Inconsistencia entre stories.
8. ❌ Texto on-image sin dirección quirúrgica.
9. ❌ Texto fuera de la zona segura (14%-85% vertical) — **exclusivo Stories**.
10. ❌ Copy on-image de más de 8 palabras — **exclusivo Stories**.
11. ❌ Shot list sin columna de stickers o sin Link en la última story — **exclusivo Stories**.

Si tu output cae en cualquiera de estos → frená y reescribí esa parte. No entregues.
