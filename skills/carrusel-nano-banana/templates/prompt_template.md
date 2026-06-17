# Prompt Template — Nano Banana

Este es el **molde fijo** que cada prompt debe seguir. Si este template está bien, el output escala. Si está mal, todo el carrusel se rompe.

---

## Reglas estructurales

Cada prompt es **un párrafo narrativo en español**, escrito como un brief de cinematógrafo. **No** listas de keywords. **No** bullets dentro del prompt final. Oraciones completas, prosa fluida.

El prompt **debe** cubrir las dimensiones de abajo, en este orden. Las marcadas con *(condicional)* solo se incluyen si el slide las requiere.

---

## Las dimensiones del prompt (en orden)

### 1. Anclaje al producto (referencia explícita a la imagen input) — OBLIGATORIO
Siempre arrancá con una frase que ate el prompt a la imagen de referencia. Patrones válidos:
- *"Usá la imagen de producto provista como sujeto exacto — conservá envase, etiquetas, colores y proporciones idénticos — y…"*
- *"Tomá el producto de la imagen de referencia y ubicalo en… (no alteres el producto en sí)."*

**Por qué**: nano banana usa la referencia para garantizar consistencia entre los N slides. Sin este anclaje, el producto deriva entre slides.

### 2. Escena y contexto — OBLIGATORIO
Dónde está el producto. Superficie, entorno, elementos secundarios. Específico, no genérico.
- ❌ *"sobre un fondo limpio"*
- ✅ *"apoyado sobre una mesada de travertino calentado por el sol, junto a una servilleta de lino a medio doblar y una rama de romero"*

### 3. Cámara y composición — OBLIGATORIO
- **Tipo de toma**: macro / primer plano / plano medio / plano abierto
- **Lente**: 35mm, 50mm, 85mm, 100mm macro
- **Ángulo**: a la altura del producto / cenital (top-down) / contrapicado / 3/4
- **Composición**: centrada / regla de los tercios / espacio negativo arriba (para dejar lugar al texto)
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

### 7. Persona / modelo humano *(condicional — solo si el slide la requiere)*
Si el slide incluye una persona, esta dimensión es **crítica** porque nano banana puede caer en el "AI face" si no la dirigís bien. Tratá a la persona como casting real, no como modelo idealizado.

Estructura obligatoria cuando hay persona:

> Una persona real **[edad específica, no rango]**, **[origen / fenotipo si es relevante a la marca]**, con **textura de piel natural visible (poros, líneas finas, asimetrías humanas — sin retoque excesivo)**, **[descripción de pelo concreta: largo, textura, peinado]**, vistiendo **[ropa específica que coincida con el mood y la paleta]**. **[Pose/acción concreta — qué está haciendo con el producto]**, expresión **[específica, no "smiling": ej. media sonrisa contenida, mirada al frasco con curiosidad, ojos cerrados disfrutando el aroma]**. Captura **espontánea, no posada (candid moment)**. **[Si las manos están en cuadro: posición clara y descripta para evitar deformidades — ej. "sosteniendo el frasco con la mano derecha desde la base, dedos relajados y visibles"]**.

Reglas duras para personas:
- **Edad concreta** (ej: "mujer de 34 años") — nunca "una mujer joven y bonita".
- **Textura de piel real**: siempre incluí *"poros visibles, textura natural, sin sobre-suavizado"*.
- **Expresión específica**: nunca *"sonriendo"* a secas. Decí qué tipo de sonrisa o microexpresión.
- **Manos visibles = manos descriptas**: si están en cuadro, decí exactamente cómo están. Esto evita los dedos de más típicos de IA.
- **Pose espontánea**: usá *"momento candid"*, *"capturada sin posar"*, *"acción natural en curso"*.
- **Casting real, no de catálogo**: usá descriptores tipo *"belleza realista, no de pasarela"*, *"rostro con carácter, no genérico"*.
- **Iluminación que respete piel**: la luz tiene que mostrar textura, no aplanarla.

### 8. Texto on-image *(condicional — solo si el slide lo requiere)*
Si el slide lleva texto, integralo con esta estructura exacta:

> Renderizá el titular **"[copy exacto en español]"** en **[familia tipográfica heredada del producto]**, **[peso: regular / bold / light]**, en **[color hex de la paleta]**, ubicado en la **[zona: arriba / centro / abajo]** del cuadro, ocupando aproximadamente **[1/3 / 1/4]** del espacio vertical, con **[espacio negativo generoso debajo / contraste claro contra el fondo]**.

Si el slide no lleva texto: omití esta dimensión enteramente (no escribas "sin texto").

### 9. Aspect ratio + calidad técnica (cierre) — OBLIGATORIO
Cerrá siempre con:
> *"Relación de aspecto vertical 4:5 (1080x1350, retrato), fotografía editorial de alto detalle, fotorrealista, foco nítido en el producto."*

Si hay persona en cuadro, agregá: *"...con foco nítido en el producto y en el rostro/manos de la persona."*

---

## Estructura narrativa del prompt (patrón fijo)

```
[Anclaje a imagen de referencia]. [Escena y contexto].
[Cámara, lente, ángulo, composición, profundidad de campo].
[Iluminación: fuente + dirección + calidad + temperatura].
[Estilo + textura + mood].
[Paleta heredada].
[Persona — si aplica].
[Texto on-image — si aplica].
[Aspect ratio + calidad técnica].
```

Todo en un solo párrafo, oraciones completas, sin bullets, sin listas, sin keyword-stuffing.

---

## Ejemplo A — Sin persona (slide 1, hook, producto = perfume)

**Slide:** Hook de un carrusel listicle "5 razones por las que este perfume dura 12+ horas".
**Copy on-image:** "Por qué dura 12+ horas"

**Prompt:**

> Usá la imagen de producto provista como sujeto exacto — conservá el frasco de vidrio ámbar, la tipografía de la etiqueta y la tapa dorada idénticos — y ubicá el frasco sobre un pedestal de mármol gastado dentro de una alcoba mediterránea iluminada por el sol, con una hoja de higuera seca proyectando una sombra larga sobre la superficie. Tomado con un lente de 85mm a f/2.0, ángulo levemente contrapicado (10° por debajo del centro del producto) para transmitir autoridad silenciosa, composición centrada con espacio negativo generoso en el tercio superior del cuadro. Iluminado por luz cálida de ventana de la tarde tardía desde la izquierda de cámara, suave y direccional, temperatura cercana a 3200K, con una sutil luz de borde recortando el costado derecho del frasco. Fotografía editorial de perfume, claridad de formato medio, mood de *lujo sensorial silencioso*. Paleta neutra cálida heredada del producto: blanco hueso #F2EBDD, dorado antiguo #B89968, ámbar profundo #6B3410, sombra carbón #2A241D. Renderizá el titular "Por qué dura 12+ horas" en una serif moderna de alto contraste (coincidente con la tipografía de la etiqueta del frasco), peso regular, en color ámbar profundo #6B3410, ubicado en la zona superior del cuadro, ocupando aproximadamente 1/4 del espacio vertical, con espacio negativo generoso debajo separando el titular del producto. Relación de aspecto vertical 4:5 (1080x1350, retrato), fotografía editorial de alto detalle, fotorrealista, foco nítido en el producto.

---

## Ejemplo B — Con persona (slide 2, demostración de uso, producto = crema facial)

**Slide:** Slide de desarrollo mostrando aplicación. Producto = pote de crema facial con etiqueta minimalista crema y verde salvia.
**Copy on-image:** "Se absorbe en 30 segundos"

**Prompt:**

> Usá la imagen de producto provista como sujeto exacto — conservá el pote de vidrio crema, la etiqueta verde salvia y la tapa de bambú idénticos — y mostralo apoyado en un estante de cerámica artesanal junto al lavabo de un baño con luz de mañana, mientras una persona aplica una pequeña cantidad de crema en su pómulo. Tomado con un lente de 50mm a f/2.2, ángulo a la altura del rostro de la persona en perfil 3/4, composición con regla de tercios (rostro a la izquierda, producto en foco secundario a la derecha), profundidad de campo superficial. Iluminado por luz natural difusa de una ventana grande detrás de cámara, suave y envolvente, temperatura neutra 5000K, con un suave relleno desde abajo que evita sombras duras bajo los ojos. Fotografía lifestyle editorial, claridad digital limpia con grano sutil, mood de *ritual matinal calmo*. Paleta heredada del producto: crema cálido #EDE6D6, verde salvia #8FA086, terracota apagado #B57F66, marrón bambú #6B5340. Una persona real, mujer de 38 años de fenotipo latino, con textura de piel natural visible (poros, leves líneas de expresión bajo los ojos, asimetrías humanas, sin sobre-suavizado), pelo castaño oscuro a la altura de los hombros recogido suelto en un rodete bajo, vistiendo una camisa de lino blanco sin estructurar. Aplicando una pequeña cantidad de crema con el dedo medio de la mano derecha sobre su pómulo derecho, dedos relajados y visibles claramente, con el pote sostenido en la mano izquierda al borde del cuadro. Expresión: concentración serena, mirándose en un espejo fuera de cuadro, ojos entrecerrados naturalmente. Captura espontánea, momento candid, no posada. Renderizá el titular "Se absorbe en 30 segundos" en una sans-serif geométrica limpia (coincidente con la tipografía de la etiqueta), peso regular, en color verde salvia #8FA086, ubicado en la zona inferior del cuadro, ocupando aproximadamente 1/4 del espacio vertical, con contraste claro contra el fondo. Relación de aspecto vertical 4:5 (1080x1350, retrato), fotografía editorial de alto detalle, fotorrealista, con foco nítido en el producto y en el rostro/manos de la persona.

---

## Variantes según función del slide (con posición sugerida del texto)

| Slide | Énfasis del prompt | Posición del texto |
|---|---|---|
| **Hook (slide 1)** | Composición con espacio para titular grande arriba o centro. Mood que detenga el scroll (intriga, contraste, escala). El producto en presencia, no en uso. | Texto grande arriba o centro vertical |
| **Argumento / Diferencial (slide 2)** | Detalle del producto con elementos secundarios. Bullets/pills si aplica. | Texto arriba alineado a izquierda o centro, bullets abajo |
| **Concepto / Prueba (intermedios)** | Variar ángulo, escena y tratamiento de imagen. Considerá leve blur cinematográfico para dar peso al texto. Si hay humanos, suelen ir acá. | Texto al medio sobre imagen con leve blur, o texto pequeño abajo |
| **Penúltimo (bullets / desglose)** | Listicle desplegado o detalle final antes del cierre. | Titular arriba + bullets distribuidos en el medio o abajo |
| **CTA (último slide)** | Composición frontal o levemente elevada, máxima legibilidad. | CTA abajo, producto al medio o arriba (composición invertida respecto al hook) |

**Regla crítica de variación**: la posición del texto **debe variar entre al menos 2 slides** del carrusel. Ver matriz completa en `style/visual_modes.md` sección "Matriz de composición y posición del texto entre slides".

---

## Reglas no-negociables del prompt

1. **Siempre** arrancá anclando a la imagen de referencia (dimensión 1).
2. **Siempre** terminá con la dimensión 9 (4:5 + calidad).
3. **Nunca** uses listas de adjetivos pegoteadas (*"moderno, limpio, vibrante, brillante, profesional"*). Una palabra precisa > cinco palabras vagas.
4. **Nunca** menciones cámaras de marca específicas a menos que aporte (*"Hasselblad H6D-100c"*). Mejor decir *"claridad de formato medio"*.
5. **Nunca** uses prompts negativos (*"sin desenfoque, sin texto, sin gente"*). Nano banana no los procesa bien — describí lo que SÍ querés.
6. **Siempre** los N prompts del carrusel comparten: lente, mood, paleta, tratamiento de luz general. Lo que cambia: ángulo, escena, composición, **posición del texto**, presencia/ausencia de persona, tratamiento de imagen (nítido vs blur cinematográfico).
7. **Nunca** describas el producto desde cero ("un frasco alto de vidrio ámbar con…"). El producto sale de la referencia, vos solo lo ubicás y lo iluminás.
8. **Si hay persona**: edad específica, textura de piel natural obligatoria, expresión específica, manos visibles = manos descriptas, captura candid. **Sin excepción.**
9. **Variá la posición del texto entre slides**. Nunca dejes los N slides con texto en la misma zona del cuadro — eso genera carruseles predecibles y planos. Ver `style/visual_modes.md` y `examples/bad/ai_generico.md` MALO #9.
