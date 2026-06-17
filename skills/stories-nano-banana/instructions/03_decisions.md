# 03 — Decisions

Acá rompés el silencio del Discovery y hacés **una sola pregunta consolidada** al user con propuestas por default ya armadas. El user confirma o edita. **Siempre se confirma antes de generar. No-negociable.**

---

## La regla del "una sola pregunta"

No hagas preguntas en serie tipo chat. **Una sola pregunta consolidada**, con propuestas completas y razones cortas. El user contesta de una y avanzás.

---

## Estructura de la pregunta consolidada

Usá este formato exacto:

```markdown
Listo, ya analicé el producto y la imagen. Te tiro mi propuesta para la secuencia de stories:

**Producto**: [nombre exacto del scrapeo]

**Mi propuesta**:
- **Tipo**: [arquetipo elegido] — [razón en una línea]
- **Stories**: [N] — [razón corta: por qué N y no otro]
- **Modo visual**: [Minimalista / Lifestyle cinematográfico] — [razón en una línea. Si es buen candidato para A/B, agregá: *"avisame si querés ambas versiones para A/B testing"*]
- **Hook**: "[hook propuesto en español, max 6-8 palabras]"
- **Estilo visual**: [editorial / lifestyle / minimal / etc., alineado al modo]
- **Mood**: [una a dos palabras precisas, alineadas al modo]
- **Lente de la secuencia**: [mm + apertura, según el modo]
- **Persona en cuadro**: [sí/no — y si sí, en qué stories. En Minimalista casi siempre no; en Lifestyle al menos una.]
- **Paleta**: [3-5 colores con hex en Minimalista; 5-6 en Lifestyle sumando entorno] (extraída de la imagen + entorno si aplica)
- **Tipografía**: [familia + características] (heredada del producto)
- **Stickers sugeridos**: [resumen de qué sticker va en cada story, ej. "story 1 pregunta · story 4 link"]

¿Avanzo así o cambiás algo?

Si querés ajustar algo concreto (stories, tipo, modo, hook, estilo, persona, stickers, etc.), decímelo en una sola respuesta y lo ajusto antes de generar los prompts.
```

---

## Cómo elegir cada propuesta por default

### Tipo de secuencia
- Si el user pidió uno específico → usá ese.
- Si no → usá el mapa de `templates/story_archetypes.md`:
  - "Cómo se usa" no obvio → Educativo
  - Marca con personalidad fuerte → Hot take
  - 2-3 beneficios diferenciados → Listicle
  - Resultados visibles documentados → Caso de estudio
  - Origen / oficio / historia genuina → Storytelling
  - Drop / oferta / fecha → Promo
- Default seguro si dudás: **Listicle**.

### Cantidad de stories
- Si el user pidió uno específico → usá ese (clamp entre 3 y 6).
- Si no:
  - Promo simple → 3-4
  - Educativo / Hot take → 4
  - Listicle de 2 ítems → 4
  - Listicle de 3 ítems → 5
  - Caso de estudio → 4
  - Storytelling → 5
- **Default si no hay otra señal: 4.**

### Hook
- Aprovechá los beneficios clave o el ángulo más fuerte del producto.
- **Máximo 6-8 palabras** (más corto que carrusel).
- Específico, no genérico.
- Si la marca tiene tono polémico, podés usar hook contraintuitivo.

### Modo visual
- Detalle completo de los modos en `style/visual_modes.md`. Resumen rápido para Decisions:
  - **Minimalista** (default): producto como escultura, fondo neutro, sin persona, paleta acotada, texto en color de paleta. Mejor para joyería, frasco, packaging, premium, marca editorial.
  - **Lifestyle cinematográfico**: producto en uso real, con persona/contexto, luz cálida, paleta extendida, texto blanco sobre fondo oscuro. Mejor para electrodomésticos, ollas/utensilios, herramientas, ropa, cosmética en aplicación, marca con storytelling.
  - **A/B paralelo**: dos secuencias completas (mismo copy + sticker, distinto modo). Solo si el user lo pide explícito o si tu propuesta default deja claro que vale testear.
- Si dudás → default = Minimalista, y dejá una línea ofreciendo *"si querés también la versión lifestyle para A/B, avisame"*.

### Estilo visual
- Heredado del producto (lo extrajiste en Discovery) **+ alineado al modo elegido**.
- En Minimalista: editorial / minimal / heritage moderno / escultórico.
- En Lifestyle: documental / cinematográfico / oficio / lifestyle editorial.

### Mood
- Una a dos palabras precisas. **No una lista.**
- Heredado del tono de marca + categoría.

### Lente
- Producto pequeño con detalle (joyería, packaging fino) → 100mm macro a f/2.8.
- Producto editorial / lookbook → 85mm a f/2.0.
- Producto en escena con contexto → 50mm a f/2.2.
- Producto en lifestyle amplio → 35mm a f/2.8.
- Default seguro: **50mm a f/2.0**.

### Persona en cuadro
- Por arquetipo:
  - Educativo → sí en story de demostración
  - Hot take → opcional, en story de evidencia
  - Listicle → opcional, en uno de los ítems si aplica
  - Caso de estudio → casi siempre sí
  - Storytelling → opcional, manos del fundador o artesano
  - Promo → opcional, depende del producto
- Si no estás seguro → no la pongas.

### Stickers sugeridos
- Mapa rápido por arquetipo (ver `templates/story_archetypes.md` para detalle):
  - Educativo: quiz en hook, link en CTA.
  - Hot take: poll en hook, link en CTA.
  - Listicle: pregunta en hook, link en CTA, neutros en el medio.
  - Caso de estudio: slider de emoji en hook, link en CTA.
  - Storytelling: música ambient + pregunta o slider, link en CTA.
  - **Promo**: countdown obligatorio (en hook o story 3), link en CTA.
- **Última story siempre tiene Link sticker**, sin excepción.
- Si una story es 100% visual y el sticker arruinaría la composición → "ninguno" es válido.

### Paleta y tipografía
- Heredadas de la imagen. **No proponés otras.**

---

## Cómo manejar la respuesta del user

### Caso A: el user dice "dale, avanzá" / "perfecto" / equivalente
→ Pasá directo a `04_concept.md`.

### Caso B: el user pide cambios concretos
→ Aplicá los cambios. **No hagas otra ronda de propuesta.** Confirmá brevemente y avanzá:

> Listo, ajusto: [cambio 1], [cambio 2]. Avanzo a generar.

→ Pasá a `04_concept.md`.

### Caso C: el user duda o pide opinión
→ Recomendá **una** dirección con razón breve. No abras otra ronda de opciones.

> Yo iría por [opción] porque [razón en una línea]. ¿Avanzo así?

### Caso D: el user pide algo que viola las reglas (ej: "8 stories", "secuencia mezcla de listicle + storytelling")
→ Explicá brevemente por qué no, ofrecé la alternativa:

> 8 stories es demasiado para retención (el ojo escanea más rápido en Stories que en carrusel; después del 5 cae mucho la lectura). ¿Te sirve 6? O si querés contar más, lo separamos en dos secuencias.

### Caso E: el user pide A/B (ambos modos visuales)
→ Confirmá en una línea y avanzá. El output va a tener dos secuencias paralelas (ver `instructions/06_output_format.md` sección A/B). Las dos comparten copy on-image, sticker por story y lógica narrativa; varían modo visual (lente, mood, luz, persona, paleta, color del texto, escena).

> Listo, te armo Secuencia A · Minimalista y Secuencia B · Lifestyle cinematográfico, con el mismo copy y stickers para que las puedas A/B testear. Avanzo.

### Caso F: el user pide cambiar el modo después de la propuesta default (ej: "mejor lifestyle", "más onda", "con personas")
→ Cambiá el modo y reajustá los parámetros derivados (lente, mood, luz, persona, paleta, color del texto). Confirmá brevemente:

> Cambio a Lifestyle cinematográfico: lente 35mm, luz cálida lateral 3200K, persona del chef en stories 1 y 2, texto blanco sobre fondo oscuro, paleta extendida con acero y ámbar. Avanzo.

---

## Lo que NO hacés en Decisions

- ❌ No hagas múltiples preguntas en serie.
- ❌ No propongas "3 opciones para que elijas". Una propuesta sólida con razón.
- ❌ No empieces a escribir prompts antes de la confirmación.
- ❌ No saltees Decisions porque "el user ya pasó toda la info". Aún si pasó todo, hacés un resumen breve del plan y pedís OK.
- ❌ No cambies el formato de la pregunta consolidada. Es siempre el mismo bloque.
- ❌ No omitas la línea de stickers — es parte del valor de la skill.

---

## Ejemplo de pregunta consolidada lleno

**Contexto**: producto = Eau de Parfum "Solar 04" (perfume artesanal premium, marca con storytelling fuerte). User pasó URL + imagen, sin más detalles.

```markdown
Listo, ya analicé el producto y la imagen. Te tiro mi propuesta para la secuencia de stories:

**Producto**: Eau de Parfum "Solar 04" — 50ml

**Mi propuesta**:
- **Tipo**: Listicle (3 razones) — el producto tiene 3 features técnicos diferenciados que merecen desarrollo individual.
- **Stories**: 5 — 1 hook + 3 razones + 1 CTA.
- **Hook**: "Por qué dura 12+ horas"
- **Estilo visual**: editorial mediterráneo
- **Mood**: lujo sensorial silencioso
- **Lente de la secuencia**: 85mm a f/2.0 (uniforme en las 5 stories)
- **Persona en cuadro**: sí, solo en la story 4 (aplicación en muñeca, momento candid)
- **Paleta**: blanco hueso #F2EBDD, dorado antiguo #B89968, ámbar profundo #6B3410, sombra carbón #2A241D
- **Tipografía**: serif moderna de alto contraste, similar a Didot, mayúsculas con tracking abierto
- **Stickers sugeridos**: story 1 pregunta ("¿cuánto te dura?") · story 4 slider de emoji · story 5 link ("comprá"). Stories 2 y 3: ninguno (visuales dominantes).

¿Avanzo así o cambiás algo?
```

Esto se lee en 15 segundos y el user puede confirmar o editar de una.
