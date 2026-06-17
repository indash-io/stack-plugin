# Prompt Template — Nano Banana (Stories)

Este es el **molde fijo** que cada prompt debe seguir. Si este template está bien, el output escala. Si está mal, toda la secuencia se rompe.

---

## Reglas estructurales

Cada prompt es **un párrafo narrativo en español**, escrito como un brief de cinematógrafo. **No** listas de keywords. **No** bullets dentro del prompt final. Oraciones completas, prosa fluida.

El prompt **debe** cubrir las dimensiones de abajo, en este orden. Las marcadas con *(condicional)* solo se incluyen si la story las requiere.

---

## Las dimensiones del prompt (en orden)

### 1. Anclaje al producto (referencia explícita a la imagen input) — OBLIGATORIO
Siempre arrancá con una frase que ate el prompt a la imagen de referencia. Patrones válidos:
- *"Usá la imagen de producto provista como sujeto exacto — conservá envase, etiquetas, colores y proporciones idénticos — y…"*
- *"Tomá el producto de la imagen de referencia y ubicalo en… (no alteres el producto en sí)."*

**Por qué**: nano banana usa la referencia para garantizar consistencia entre las N stories. Sin este anclaje, el producto deriva entre slides.

### 2. Escena y contexto — OBLIGATORIO
Dónde está el producto. Superficie, entorno, elementos secundarios. Específico, no genérico.
- ❌ *"sobre un fondo limpio"*
- ✅ *"apoyado sobre una mesada de travertino calentado por el sol, junto a una servilleta de lino a medio doblar y una rama de romero"*

### 3. Cámara y composición vertical — OBLIGATORIO
Como el formato es **9:16 vertical extremo**, la composición debe pensarse "de arriba a abajo", no "de izquierda a derecha".

- **Tipo de toma**: macro / primer plano / plano medio / plano abierto vertical
- **Lente**: 35mm, 50mm, 85mm, 100mm macro
- **Ángulo**: a la altura del producto / cenital (top-down) / contrapicado / 3/4
- **Composición vertical**: producto en el **tercio central o inferior del cuadro**, dejando espacio negativo arriba y/o abajo dentro de la zona segura para el texto
- **Profundidad de campo**: superficial (f/1.8–f/2.8) o profunda

### 4. Iluminación — OBLIGATORIO
- **Fuente**: luz de ventana / softbox de estudio / sol de hora dorada / luz nublada difusa / luz neón práctica
- **Dirección**: lateral / frontal / contraluz / cenital / luz de borde (rim light)
- **Calidad**: suave y difusa / dura y direccional
- **Temperatura**: cálida 3200K / neutra 5000K / fría 6500K

### 5. Estilo visual y mood — OBLIGATORIO
Estilo (editorial, lifestyle, minimal, maximalist, retro, documental), textura (digital limpio, grano de 35mm, claridad de formato medio), y mood en una o dos palabras precisas (*calmo y considerado*, *enérgico y eléctrico*, *lujo silencioso*, etc.).

### 6. Paleta heredada del brand — OBLIGATORIO
Mencionar la paleta extraída de la imagen de referencia con descripción precisa + hex.
- *"paleta neutra cálida: blanco hueso #F2EBDD, terracota suave #C8755A, oliva profundo #4A4F2C"*

### 7. Persona / modelo humano *(condicional — solo si la story la requiere)*
Si la story incluye una persona, esta dimensión es **crítica** porque nano banana puede caer en el "AI face" si no la dirigís bien. Tratá a la persona como casting real, no como modelo idealizado.

Estructura obligatoria cuando hay persona:

> Una persona real **[edad específica, no rango]**, **[origen / fenotipo si es relevante a la marca]**, con **textura de piel natural visible (poros, líneas finas, asimetrías humanas — sin retoque excesivo)**, **[descripción de pelo concreta: largo, textura, peinado]**, vistiendo **[ropa específica que coincida con el mood y la paleta]**. **[Pose/acción concreta — qué está haciendo con el producto]**, expresión **[específica, no "smiling": ej. media sonrisa contenida, mirada al frasco con curiosidad, ojos cerrados disfrutando el aroma]**. Captura **espontánea, no posada (candid moment)**. **[Si las manos están en cuadro: posición clara y descripta para evitar deformidades]**.

Reglas duras para personas:
- **Edad concreta** (ej: "mujer de 34 años") — nunca "una mujer joven y bonita".
- **Textura de piel real**: siempre incluí *"poros visibles, textura natural, sin sobre-suavizado"*.
- **Expresión específica**: nunca *"sonriendo"* a secas. Decí qué tipo de sonrisa o microexpresión.
- **Manos visibles = manos descriptas**: si están en cuadro, decí exactamente cómo están.
- **Pose espontánea**: usá *"momento candid"*, *"capturada sin posar"*, *"acción natural en curso"*.
- **Casting real, no de catálogo**: usá descriptores tipo *"belleza realista, no de pasarela"*, *"rostro con carácter, no genérico"*.
- **Iluminación que respete piel**: la luz tiene que mostrar textura, no aplanarla.

### 8. Texto on-image + zona segura de UI *(condicional — solo si la story lo requiere)*
**Stories tienen una zona segura específica**: el texto debe vivir entre el **14% y 85% del alto vertical** del cuadro. Los píxeles superiores (avatar, nombre, tiempo) y los inferiores (input de respuesta, ícono de envío) los tapa Instagram.

Esta dimensión no es solo "poner el texto en el tercio central". Es **composición creativa**:
- Elegí una de las **6 estrategias de placement** (cabezal / pie / centro sobre producto / desplazado / wrap / doble peso) según el rol de la story y lo que ya elegiste para las otras stories de la secuencia.
- Si el fondo compite con el texto en esa zona específica, dirigí uno de los **6 tratamientos de imagen** (blur, scrim, grade, vignette, letterbox, sin tratamiento) para empujar el texto adelante.
- **Variá placement entre stories** de la misma secuencia. No clones.

Detalle completo de las 6 estrategias + 6 tratamientos + reglas de variación + 8 anti-patrones en **`style/text_composition.md`**. Leerlo es obligatorio antes de escribir esta dimensión.

Si la story lleva texto, integralo con esta estructura exacta:

> Renderizá el titular **"[copy exacto en español, máximo 6-8 palabras]"** en **[familia tipográfica heredada del producto]**, **[peso: regular / bold / light, o jerarquía bold+regular si es doble peso]**, en **[color hex de la paleta — en Modo A típicamente un hex de la paleta con contraste; en Modo B típicamente blanco hueso #ECE7DC]**, ubicado **[placement elegido: tercio superior central / tercio inferior central / centro vertical sobre producto / desplazado / wrap detrás del producto]** del cuadro (siempre dentro del rango 14%-85% del alto, evitando los bordes superior e inferior tapados por la UI de Instagram), ocupando aproximadamente **[1/6 a 1/3 del espacio vertical, según jerarquía]**, con **[contraste real contra el fondo de esa zona específica + tratamiento dirigido si aplica: blur de fondo / scrim sutil 25-30% / grade local del 15% / vignette / letterbox sólido / sin tratamiento]**.

Si la story no lleva texto: omití esta dimensión enteramente (no escribas "sin texto").

### 9. Aspect ratio + calidad técnica (cierre) — OBLIGATORIO
Cerrá siempre con:
> *"Relación de aspecto vertical 9:16 (1080x1920, formato Instagram Stories), fotografía editorial de alto detalle, fotorrealista, foco nítido en el producto, composición que respeta la zona segura de UI con el texto fuera del 14% superior y del 15% inferior del cuadro."*

Si hay persona en cuadro, agregá: *"...con foco nítido en el producto y en el rostro/manos de la persona."*

---

## Estructura narrativa del prompt (patrón fijo)

```
[Anclaje a imagen de referencia]. [Escena y contexto].
[Cámara, lente, ángulo, composición vertical, profundidad de campo].
[Iluminación: fuente + dirección + calidad + temperatura].
[Estilo + textura + mood].
[Paleta heredada].
[Persona — si aplica].
[Texto on-image + zona segura — si aplica].
[Aspect ratio 9:16 + calidad técnica + zona segura].
```

Todo en un solo párrafo, oraciones completas, sin bullets, sin listas, sin keyword-stuffing.

---

## Ejemplo A — Sin persona (story 1, hook, producto = perfume)

**Story:** Hook de una secuencia listicle "3 razones por las que este perfume dura 12+ horas".
**Copy on-image:** "Por qué dura 12+ horas"
**Sticker sugerido**: pregunta ("¿cuánto te dura el tuyo?")

**Prompt:**

> Usá la imagen de producto provista como sujeto exacto — conservá el frasco de vidrio ámbar, la tipografía de la etiqueta y la tapa dorada idénticos — y ubicá el frasco sobre un pedestal de mármol gastado dentro de una alcoba mediterránea iluminada por el sol, con una hoja de higuera seca proyectando una sombra larga sobre la superficie. Tomado con un lente de 85mm a f/2.0, ángulo levemente contrapicado (10° por debajo del centro del producto) para transmitir autoridad silenciosa, composición vertical con el frasco ubicado en el tercio inferior del cuadro y espacio negativo amplio en el tercio central y superior dentro de la zona segura para alojar el titular. Iluminado por luz cálida de ventana de la tarde tardía desde la izquierda de cámara, suave y direccional, temperatura cercana a 3200K, con una sutil luz de borde recortando el costado derecho del frasco. Fotografía editorial de perfume, claridad de formato medio, mood de *lujo sensorial silencioso*. Paleta neutra cálida heredada del producto: blanco hueso #F2EBDD, dorado antiguo #B89968, ámbar profundo #6B3410, sombra carbón #2A241D. Renderizá el titular "Por qué dura 12+ horas" en una serif moderna de alto contraste (coincidente con la tipografía de la etiqueta del frasco), peso regular, en color ámbar profundo #6B3410, ubicado en el tercio central del cuadro dentro de la zona segura de UI (entre el 14% y 85% del alto vertical, evitando los bordes superior e inferior tapados por Instagram), ocupando aproximadamente 1/3 del espacio vertical, con espacio negativo generoso debajo separando el titular del producto. Relación de aspecto vertical 9:16 (1080x1920, formato Instagram Stories), fotografía editorial de alto detalle, fotorrealista, foco nítido en el producto, composición que respeta la zona segura de UI con el texto fuera del 14% superior y del 15% inferior del cuadro.

---

## Ejemplo B — Con persona (story 2, demostración de uso, producto = crema facial)

**Story:** Story de desarrollo mostrando aplicación. Producto = pote de crema facial con etiqueta minimalista crema y verde salvia.
**Copy on-image:** "Se absorbe en 30 segundos"
**Sticker sugerido**: countdown ("probala mañana 9am")

**Prompt:**

> Usá la imagen de producto provista como sujeto exacto — conservá el pote de vidrio crema, la etiqueta verde salvia y la tapa de bambú idénticos — y mostralo apoyado en un estante de cerámica artesanal junto al lavabo de un baño con luz de mañana, mientras una persona aplica una pequeña cantidad de crema en su pómulo. Tomado con un lente de 50mm a f/2.2, ángulo a la altura del rostro de la persona en perfil 3/4, composición vertical con el rostro de la persona ocupando el tercio central del cuadro y el pote como sujeto secundario en el tercio inferior derecho, profundidad de campo superficial, espacio negativo en el tercio superior dentro de la zona segura para el titular. Iluminado por luz natural difusa de una ventana grande detrás de cámara, suave y envolvente, temperatura neutra 5000K, con un suave relleno desde abajo que evita sombras duras bajo los ojos. Fotografía lifestyle editorial, claridad digital limpia con grano sutil, mood de *ritual matinal calmo*. Paleta heredada del producto: crema cálido #EDE6D6, verde salvia #8FA086, terracota apagado #B57F66, marrón bambú #6B5340. Una persona real, mujer de 38 años de fenotipo latino, con textura de piel natural visible (poros, leves líneas de expresión bajo los ojos, asimetrías humanas, sin sobre-suavizado), pelo castaño oscuro a la altura de los hombros recogido suelto en un rodete bajo, vistiendo una camisa de lino blanco sin estructurar. Aplicando una pequeña cantidad de crema con el dedo medio de la mano derecha sobre su pómulo derecho, dedos relajados y visibles claramente, con el pote sostenido en la mano izquierda al borde del cuadro. Expresión: concentración serena, mirándose en un espejo fuera de cuadro, ojos entrecerrados naturalmente. Captura espontánea, momento candid, no posada. Renderizá el titular "Se absorbe en 30 segundos" en una sans-serif geométrica limpia (coincidente con la tipografía de la etiqueta), peso regular, en color verde salvia #8FA086, ubicado en el tercio superior central del cuadro dentro de la zona segura de UI (entre el 14% y 85% del alto vertical), ocupando aproximadamente 1/4 del espacio vertical, con contraste claro contra el fondo. Relación de aspecto vertical 9:16 (1080x1920, formato Instagram Stories), fotografía editorial de alto detalle, fotorrealista, con foco nítido en el producto y en el rostro/manos de la persona, composición que respeta la zona segura de UI con el texto fuera del 14% superior y del 15% inferior del cuadro.

---

## Variantes según función de la story

| Story | Énfasis del prompt |
|---|---|
| **Hook (story 1)** | Composición con texto grande y centrado dentro de la zona segura. Mood que detenga el scroll en el primer segundo (intriga, contraste, escala). El producto en presencia, no en uso. |
| **Desarrollo (stories 2..N-1)** | Variar ángulo y escena entre stories para no repetirse, pero mantener paleta + lente + mood consistentes. Si hay humanos, se usan acá (demostración, contexto de uso). |
| **CTA (última story)** | Composición frontal o levemente elevada, máxima legibilidad del texto, escena limpia, foco total en el producto + el CTA accionable, idealmente con espacio claro para que el sticker de link/swipe no choque con elementos visuales. |

---

## Reglas no-negociables del prompt

1. **Siempre** arrancá anclando a la imagen de referencia (dimensión 1).
2. **Siempre** terminá con la dimensión 9 (9:16 + calidad + zona segura).
3. **Nunca** uses listas de adjetivos pegoteadas (*"moderno, limpio, vibrante, brillante, profesional"*). Una palabra precisa > cinco palabras vagas.
4. **Nunca** menciones cámaras de marca específicas a menos que aporte. Mejor decir *"claridad de formato medio"*.
5. **Nunca** uses prompts negativos (*"sin desenfoque, sin texto, sin gente"*). Nano banana no los procesa bien — describí lo que SÍ querés.
6. **Siempre** las N stories del carrusel comparten: lente, mood, paleta, tratamiento de luz general. Lo que cambia: ángulo, escena, composición, presencia/ausencia de persona.
7. **Nunca** describas el producto desde cero ("un frasco alto de vidrio ámbar con…"). El producto sale de la referencia, vos solo lo ubicás y lo iluminás.
8. **Si hay persona**: edad específica, textura de piel natural obligatoria, expresión específica, manos visibles = manos descriptas, captura candid. **Sin excepción.**
9. **Siempre** el texto on-image va dentro de la zona segura (14%-85% vertical). Stories que renderizan texto en los extremos quedan ilegibles en Instagram.
10. **Máximo 6-8 palabras** en el copy on-image. El usuario tiene 5-15 segundos para leerlo antes del auto-advance.
11. **Variá placement de texto entre stories** de la misma secuencia. Tres stories con texto en el mismo tercio superior central = template plano. Mezclá cabezal, pie, centro y doble peso. Si el fondo compite, dirigí blur, scrim o grade explícitamente. Detalles en `style/text_composition.md`.
