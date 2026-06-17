# 04 — Concept

Después del OK del user en Decisions, armás la **narrativa story por story**: qué dice cada una, qué muestra cada una, qué sticker lleva, cómo se conectan. Este paso es **trabajo silencioso** — todavía no le mostrás nada al user. El output del concept es la base sobre la que escribís los prompts en el paso 5.

---

## Qué producís en este paso

Una **tabla interna** con N filas, una por story:

| # | Función | Copy on-image | Concepto visual (1 frase) | Persona | Sticker sugerido |
|---|---|---|---|---|---|
| 1 | Hook | "..." | ... | no | ... |
| 2 | ... | "..." | ... | ... | ... |
| ... | ... | ... | ... | ... | ... |
| N | CTA | "..." | ... | no | Link |

Esta tabla **no se le muestra al user** (eso pasa en el output final, formateado). Pero es lo que vos usás para generar los prompts en el paso 5.

---

## Cómo escribir el copy on-image

### Reglas duras

1. **Máximo 6-8 palabras por story.** Idealmente 3-6. Más corto que carrusel — el ojo escanea más rápido en stories.
2. **Específico siempre.** Genérico nunca.
   - ❌ "Calidad superior" / "Lo mejor del mercado" / "Descubrí la diferencia"
   - ✅ "12 horas de fragancia" / "10 años de garantía" / "Hecho en 4 horas"
3. **Cero emojis** salvo que el user los pidió explícitamente.
4. **Verbos en infinitivo o presente** para CTAs. Nunca pasivos.
   - ✅ "Probalo · 30 días" / "Reservá el tuyo" / "Empezá tu rutina"
   - ❌ "Sea probado" / "Será reservado"
5. **Sin signos de exclamación** salvo en arquetipo Promo y con moderación.
6. **Sin marketing-speak**. Cada palabra tiene que poder defenderse.
   - ❌ "premium", "exclusivo", "único", "incomparable", "revolucionario"
   - ✅ palabras concretas que describan algo verificable.
7. **Estructura paralela en listicles**. Si el ítem 1 empieza con sustantivo, los ítems 2 y 3 también.
8. **Datos crudos cuando los tenés**. Números > adjetivos.
   - ❌ "Larga duración" → ✅ "12+ horas"

### Cómo definir el hook (story 1)

El hook tiene que **frenar el scroll en el primer segundo** (las stories tienen 5-15s de auto-advance, así que cada milisegundo cuenta). Tres tácticas que funcionan:

1. **Pregunta provocadora**: *"¿Por qué no te protege?"*
2. **Afirmación contraintuitiva**: *"Las baratas son las más caras"*
3. **Promesa numerada concreta**: *"3 razones que dura 12+ horas"*

Evitá hooks tipo "Te presentamos X" o "Conocé Y" — son genéricos y no detienen.

### Cómo definir el CTA (última story)

El CTA tiene que ser **accionable** y atado a un sticker de Link. No "gracias por leer".

Patrones que funcionan:
- *"Probalo · 30 días"* + sticker link
- *"Reservá el tuyo · 200 unidades"* + sticker link
- *"Empezá tu rutina · 25% off"* + sticker link
- *"Conseguilo antes del [fecha]"* + sticker countdown + link
- *"Comprá"* (cuando el copy es minimalista) + sticker link grande

El CTA puede tener **dos partes**: acción + razón/urgencia, separadas por punto medio.

---

## Cómo definir el sticker de cada story

Esto es exclusivo de stories (no existe en carrusel). Cada story tiene un **sticker sugerido** en el shot list.

### Reglas para asignar stickers

1. **Última story = Link siempre**. Sin excepción.
2. **Hook = sticker de engagement** (pregunta, poll, slider, quiz). El que mejor matchea el arquetipo.
3. **Stories intermedias**: la mayoría puede ir sin sticker ("ninguno") cuando la composición visual es dominante. Forzar sticker en cada story diluye el engagement.
4. **Promo = countdown obligatorio** en al menos una story (idealmente la del hook o la 3).
5. **Si la story es 100% texto-driven** (copy enorme dominante) → "ninguno" para no chocar.
6. **Si la story tiene mucho espacio negativo arriba o abajo** → ahí va el sticker.

### Mapa rápido por arquetipo

| Arquetipo | Hook | Medio | CTA |
|---|---|---|---|
| Educativo | Quiz | Pregunta o ninguno | Link |
| Hot take | Poll | Pregunta o ninguno | Link |
| Listicle | Pregunta | Ninguno | Link |
| Caso de estudio | Slider de emoji | Pregunta | Link |
| Storytelling | Pregunta + música | Slider | Link |
| Promo | Countdown | Quiz o countdown | Link |

### Cómo escribir el contenido del sticker en el shot list

- **Pregunta**: incluí la pregunta entre paréntesis. Ej: *"Pregunta (¿cuánto te dura el tuyo?)"*
- **Poll**: incluí las dos opciones. Ej: *"Poll (sí / no)"* o *"Poll (más caro / más barato)"*
- **Quiz**: incluí pregunta + respuesta correcta. Ej: *"Quiz (¿cuánto SPF aplicás? — respuesta: 2 dedos)"*
- **Countdown**: incluí fecha objetivo. Ej: *"Countdown (15 de mayo, 23:59)"*
- **Slider**: incluí emoji y label. Ej: *"Slider de emoji (🔥, '¿qué tanto te suena?')"*
- **Link**: incluí texto del CTA del sticker. Ej: *"Link ('comprá')"* o *"Link ('reservá ahora')"*

---

## Cómo escribir el concepto visual de cada story

Cada concepto visual es **una sola frase** que define:

- **Sujeto en cuadro**: producto + qué más (otro objeto, persona, contexto)
- **Escena**: dónde está (tipo de superficie, entorno)
- **Ángulo**: a la altura / cenital / contrapicado / 3/4
- **Placement del texto + tratamiento si aplica**: cuál de las 6 estrategias de placement usás (cabezal / pie / centro sobre producto / desplazado / wrap / doble peso) y, si el fondo de esa zona compite con el texto, qué tratamiento aplicás (blur, scrim, grade, vignette, letterbox, o ninguno). Detalle completo en `style/text_composition.md`. **Variá placement entre stories de la misma secuencia** — no cloneés.

Ejemplos:

> "Frasco sobre pedestal de mármol, alcoba mediterránea, 3/4 ligero contrapicado, texto cabezal grande en tercio superior central, sin tratamiento (fondo monocromático claro)."

> "Macro del frasco con sombra de hoja seca atravesando la etiqueta, cenital ligero, texto a pie en tercio inferior central, sin tratamiento."

> "Persona aplicándose perfume en la muñeca, plano medio 3/4, mood candid, texto centro vertical sobre producto a doble peso (palabra clave bold + descriptor regular), grade local del 15% en la franja del texto para asegurar contraste contra la cocina detrás."

---

## Cómo garantizar consistencia entre stories

Lo que **debe ser igual** en las N stories:

| Elemento | Por qué |
|---|---|
| Producto (de la referencia) | Sin esto, no es el mismo producto |
| Lente | Sin esto, las stories parecen de sesiones distintas |
| Mood | Sin esto, la secuencia se siente desarmada |
| Paleta | Sin esto, hay choque cromático |
| Tratamiento general de luz (cálida/fría, suave/dura) | Sin esto, parecen de horas distintas del día |
| Aspect ratio 9:16 + zona segura respetada | Sin esto, el texto se tapa con UI de Instagram |

Lo que **debe variar** entre stories:

| Elemento | Por qué |
|---|---|
| Ángulo de cámara | Para que cada story se vea distinta |
| Escena / contexto | Para que la narrativa avance |
| Composición / dónde va el texto dentro de la zona segura | Para que el texto siempre tenga lugar y no se sienta repetido |
| Distancia (cerrado / abierto / macro) | Para variar ritmo visual |
| Persona presente o no | Para variar entre presencia y "objeto en sí" |
| Sticker | Para variar el tipo de engagement |

**Regla de oro**: si tomaras las N stories y las vieras en secuencia en Instagram, deberían sentirse como **una misma sesión narrativa** (consistencia) **pero con ritmo y variación** (no repetidas, no aburridas).

---

## Cómo aplicar el arquetipo elegido

Andá a `templates/story_archetypes.md` y seguí la estructura del arquetipo confirmado en Decisions:

- **Educativo**: hook (problema) → causa → solución → CTA
- **Hot take**: hook (afirmación polémica) → argumento → evidencia → CTA
- **Listicle**: hook (promesa numerada) → ítem 1 → ítem 2 → ítem N → CTA
- **Caso de estudio**: hook (resultado) → antes → después → CTA
- **Storytelling**: hook (pregunta) → origen → proceso → resultado → CTA
- **Promo**: hook (qué) → detalle → urgencia → CTA

Adaptá el copy, el concepto visual y el sticker de cada story a su función dentro del arquetipo.

---

## Anti-patrones a evitar

1. **Story de relleno**: si una story no aporta nada, sacala. Mejor 4 buenas que 6 mediocres.
2. **Doble hook**: solo la story 1 es hook. Las siguientes son desarrollo.
3. **Repetición visual**: si dos stories son casi idénticas, fusionalas o cambiá una.
4. **Copy genérico en stories intermedias**: cada story tiene que decir algo único.
5. **CTA poético**: la última story es para acción + link sticker, no para reflexión.
6. **Cambio brusco de mood**: si la secuencia arranca calma y termina enérgica, hay un problema de coherencia.
7. **Texto fuera de la zona segura**: si el texto vive en los primeros 14% o últimos 15% del cuadro, queda tapado por la UI nativa de Instagram.
8. **Sticker forzado en cada story**: a veces "ninguno" es la decisión correcta. No saturar.
9. **Placement de texto clonado entre stories**: las N stories con texto en el mismo tercio superior central, mismo tamaño, mismo color → template plano. Cabezal en una, pie en otra, centro a doble peso en la tercera. Variá. Más detalle y bad examples en `style/text_composition.md`.
10. **Texto sin contraste real**: blanco hueso sobre fondo blanco hueso, negro sobre olla negra. La regla del color del texto del modo se aplica **mirando la zona específica del cuadro donde vive el texto**, no en promedio. Si compite, dirigí blur/scrim/grade.

---

## Checklist antes de pasar al paso 5

- [ ] Cada story tiene función clara (hook / desarrollo / CTA).
- [ ] Cada copy on-image tiene ≤6-8 palabras y dice algo específico.
- [ ] Cada concepto visual está en una sola frase y especifica zona segura del texto.
- [ ] Cada story tiene sticker sugerido (puede ser "ninguno").
- [ ] Última story tiene Link sticker, sin excepción.
- [ ] Las N stories comparten lente + mood + paleta + luz general.
- [ ] Las N stories varían ángulo + escena + composición + sticker.
- [ ] Story 1 frena el scroll. Story N tiene CTA accionable con verbo + link.
- [ ] Si hay persona, está solo en stories donde aporta (no en todas).
- [ ] No hay repetición visual entre stories.
- [ ] Cada story podría defenderse sola (no necesita el contexto de otra para entenderse).

Si pasa todo → andá a `instructions/05_prompt_engineering.md` + `templates/prompt_template.md` y escribí los N prompts.
