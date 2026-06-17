# 03 — Decisions

Acá rompés el silencio del Discovery y hacés **una sola pregunta consolidada** al user con propuestas por default ya armadas. El user confirma o edita. **Siempre se confirma antes de generar. No-negociable.**

---

## La regla del "una sola pregunta"

No hagas preguntas en serie tipo chat ("¿qué tipo de carrusel querés?" → user responde → "¿cuántos slides?" → user responde → "¿qué estilo?"…). Eso cansa.

**Una sola pregunta consolidada**, con propuestas completas y razones cortas. El user contesta de una y avanzás.

---

## Estructura de la pregunta consolidada

Usá este formato exacto:

```markdown
Listo, ya analicé el producto y la imagen. Te tiro mi propuesta para el carrusel:

**Producto**: [nombre exacto del scrapeo]

**Mi propuesta**:
- **Tipo**: [arquetipo elegido] — [razón en una línea: por qué este arquetipo matchea el producto]
- **Slides**: [N] — [razón corta: por qué N y no otro]
- **Modo visual**: [Minimalista / Lifestyle cinematográfico] — [razón en una línea. Si es buen candidato para A/B, agregá: *"avisame si querés ambas versiones para A/B testing"*]
- **Hook**: "[hook propuesto en español, max 10 palabras]"
- **Estilo visual**: [editorial / lifestyle / minimal / etc., alineado al modo]
- **Mood**: [una a dos palabras precisas, alineadas al modo]
- **Lente del carrusel**: [mm + apertura, según el modo]
- **Persona en cuadro**: [sí/no — y si sí, en qué slides. En Minimalista casi siempre no; en Lifestyle al menos en algunos.]
- **Paleta**: [3-5 colores con hex en Minimalista; 5-6 en Lifestyle sumando entorno] (extraída de la imagen + entorno si aplica)
- **Tipografía**: [familia + características] (heredada del producto)
- **Elementos gráficos** (solo Lifestyle): [pills sí/no, brand mark, íconos lineales si aplica]

¿Avanzo así o cambiás algo?

Si querés ajustar algo concreto (slides, tipo, modo, hook, estilo, persona, etc.), decímelo en una sola respuesta y lo ajusto antes de generar los prompts.
```

---

## Cómo elegir cada propuesta por default

### Tipo de carrusel
- Si el user pidió uno específico → usá ese.
- Si no → usá el mapa de `templates/carousel_archetypes.md`:
  - "Cómo se usa" no obvio → Educativo
  - Marca con personalidad fuerte → Hot take
  - 3+ beneficios diferenciados → Listicle
  - Resultados visibles documentados → Caso de estudio
  - Origen / oficio / historia genuina → Storytelling
  - Drop / oferta / fecha → Promo
- Default seguro si dudás: **Listicle**.

### Cantidad de slides
- Si el user pidió uno específico → usá ese (clamp entre 3 y 7).
- Si no:
  - Promo simple → 3-4
  - Educativo / Hot take → 4
  - Listicle de 3 ítems → 5 (1 hook + 3 ítems + 1 CTA)
  - Listicle de 4 ítems → 6
  - Caso de estudio → 4
  - Storytelling → 5
- **Default si no hay otra señal: 4.**

### Hook
- Aprovechá los beneficios clave o el ángulo más fuerte del producto.
- Máximo ~10 palabras.
- Específico, no genérico ("Descubrí la diferencia" ❌, "Por qué dura 12 horas" ✅).
- Si la marca tiene tono polémico, podés usar hook contraintuitivo.

### Modo visual
- Detalle completo de los modos en `style/visual_modes.md`. Resumen rápido para Decisions:
  - **Minimalista** (default): producto como protagonista, fondo neutro, sin persona, paleta acotada, texto en color de paleta. Mejor para joyería, frasco, packaging premium, suplemento técnico, marca editorial.
  - **Lifestyle cinematográfico**: persona protagonista en escena real, luz cálida, paleta extendida con entorno, texto blanco grande dominante, pills y brand mark como elementos gráficos. Mejor para electrodomésticos, cocina, fitness, cosmética en aplicación, suplemento aspiracional, marca con storytelling.
  - **A/B paralelo**: dos carruseles completos (mismo copy + narrativa, distinto modo). Solo si el user lo pide explícito o si tu propuesta default deja claro que vale testear.
- Si dudás → default = Minimalista (más controlable). En la propuesta dejá una línea ofreciendo *"si querés también la versión Lifestyle para A/B, avisame"*.
- **Si el user no responde el modo en su confirmación, usás el modo que propusiste por default.** No volvés a preguntar.

### Estilo visual
- Heredado del producto (lo extrajiste en Discovery) **+ alineado al modo elegido**.
- En Minimalista: editorial / minimal / heritage moderno / clínico / industrial honesto.
- En Lifestyle: documental cinematográfico / lifestyle editorial / oficio en acción / brand digital moderno.

### Mood
- Una a dos palabras precisas. **No una lista.**
- Heredado del tono de marca + categoría.
- Ejemplos: *lujo silencioso*, *enérgico y eléctrico*, *calmo y considerado*, *crudo y honesto*, *playful*, *clínico*, *heritage*.

### Lente
- Producto pequeño con detalle (joyería, packaging fino) → 100mm macro a f/2.8.
- Producto editorial / lookbook → 85mm a f/2.0.
- Producto en escena con contexto → 50mm a f/2.2.
- Producto en lifestyle amplio → 35mm a f/2.8.
- Default seguro: **50mm a f/2.0**.

### Persona en cuadro
- Por arquetipo:
  - Educativo → sí en slide de demostración
  - Hot take → opcional, en slide de evidencia
  - Listicle → opcional, en uno de los ítems si aplica
  - Caso de estudio → casi siempre sí
  - Storytelling → opcional, manos del fundador o artesano
  - Promo → opcional, depende del producto
- Si no estás seguro → no la pongas. La consistencia con persona es más difícil que sin.

### Paleta y tipografía
- Heredadas de la imagen. **No proponés otras.**
- Si la imagen no aporta tipografía clara, decilo: *"tipografía no extraíble de la imagen, voy a usar [familia genérica que matchee mood]"*.

---

## Cómo manejar la respuesta del user

### Caso A: el user dice "dale, avanzá" / "perfecto" / equivalente
→ Pasá directo a `04_concept.md`.

### Caso B: el user pide cambios concretos
→ Aplicá los cambios. **No hagas otra ronda de propuesta.** Confirmá brevemente y avanzá:

> Listo, ajusto: [cambio 1], [cambio 2]. Avanzo a generar.

→ Pasá a `04_concept.md`.

### Caso C: el user duda o pide opinión
→ Recomendá **una** dirección con razón breve. No abras otra ronda de opciones. Tomá decisión y pedí confirmación final:

> Yo iría por [opción] porque [razón en una línea]. ¿Avanzo así?

### Caso D: el user pide algo que viola las reglas (ej: "8 slides", "carrusel mezcla de listicle + storytelling")
→ Explicá brevemente por qué no, ofrecé la alternativa:

> 8 slides es demasiado para retención (después del 5 cae mucho la lectura). ¿Te sirve 7? O si querés contar más, lo separamos en dos carruseles.

### Caso E: el user pide A/B (ambos modos visuales)
→ Confirmá en una línea y avanzá. El output va a tener dos carruseles paralelos (ver `instructions/06_output_format.md` sección A/B). Los dos comparten copy on-image, narrativa, hook y CTA; varían modo visual (lente, mood, luz, persona, paleta, color del texto, escena, elementos gráficos).

> Listo, te armo Carrusel A · Minimalista y Carrusel B · Lifestyle cinematográfico, con el mismo copy y narrativa para que los puedas A/B testear. Avanzo.

### Caso F: el user pide cambiar el modo después de la propuesta default (ej: "mejor lifestyle", "más onda", "con personas")
→ Cambiá el modo y reajustá los parámetros derivados (lente, mood, luz, persona, paleta, color del texto, elementos gráficos). Confirmá brevemente:

> Cambio a Lifestyle cinematográfico: lente 35mm, luz cálida lateral 3200K, persona en stories 1 y 3, texto blanco dominante, pills + brand mark, paleta extendida sumando entorno. Avanzo.

### Caso G: el user no responde el modo visual en su confirmación
→ Avanzá con el modo que propusiste por default. **No vuelvas a preguntar.** El user ya pudo cambiarlo y no lo hizo, eso es confirmación implícita.

---

## Lo que NO hacés en Decisions

- ❌ No hagas múltiples preguntas en serie.
- ❌ No propongas "3 opciones para que elijas". Una propuesta sólida con razón.
- ❌ No empieces a escribir prompts antes de la confirmación.
- ❌ No saltees Decisions porque "el user ya pasó toda la info". Aún si pasó todo, hacés un resumen breve del plan y pedís OK.
- ❌ No cambies el formato de la pregunta consolidada. Es siempre el mismo bloque.

---

## Ejemplo de pregunta consolidada lleno

**Contexto**: producto = Eau de Parfum "Solar 04" (perfume artesanal premium, marca con storytelling fuerte). User pasó URL + imagen, sin más detalles.

```markdown
Listo, ya analicé el producto y la imagen. Te tiro mi propuesta para el carrusel:

**Producto**: Eau de Parfum "Solar 04" — 50ml

**Mi propuesta**:
- **Tipo**: Listicle (3 razones) — el producto tiene 3 features técnicos diferenciados (concentración, base, fórmula) que merecen desarrollo individual.
- **Slides**: 5 — 1 hook + 3 razones + 1 CTA.
- **Modo visual**: Minimalista — la marca tiene packaging editorial premium y el feed actual es minimal/heritage. Si querés la versión Lifestyle para A/B, avisame.
- **Hook**: "Por qué dura 12+ horas"
- **Estilo visual**: editorial mediterráneo
- **Mood**: lujo sensorial silencioso
- **Lente del carrusel**: 85mm a f/2.0 (uniforme en los 5 slides)
- **Persona en cuadro**: sí, solo en el slide 4 (aplicación en muñeca, momento candid)
- **Paleta**: blanco hueso #F2EBDD, dorado antiguo #B89968, ámbar profundo #6B3410, sombra carbón #2A241D
- **Tipografía**: serif moderna de alto contraste, similar a Didot, mayúsculas con tracking abierto

¿Avanzo así o cambiás algo?
```

Esto se lee en 15 segundos y el user puede confirmar o editar de una.
