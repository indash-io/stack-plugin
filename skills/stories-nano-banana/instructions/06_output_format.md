# 06 — Output Format

Acá entregás. Después de Concept + Prompt Generation + Self-check, formateás el output final con el formato exacto que el user espera.

---

## Estructura exacta del output final

> Si el user pidió **A/B** (dos modos visuales paralelos), saltá a la sección "Output A/B" más abajo. Para una sola secuencia, seguí esta estructura.

```markdown
# Stories: [Nombre del Producto]

## Brief creativo

**Producto**: [nombre exacto del producto]
**Tipo de secuencia**: [arquetipo]
**Stories**: [N]
**Idioma copy**: [es]
**Modo visual**: [Minimalista / Lifestyle cinematográfico]
**Mood**: [una a dos palabras]
**Estilo visual**: [editorial / lifestyle / minimal / etc.]
**Lente de la secuencia**: [mm + apertura]
**Tratamiento de luz**: [una frase]
**Aspect ratio**: 9:16 (1080x1920, Instagram Stories)

**Paleta heredada del producto**:
- [color 1] — [#hex]
- [color 2] — [#hex]
- [color 3] — [#hex]
- [color 4] — [#hex]

**Tipografía heredada**: [familia + características]

**Lógica narrativa**:
[Una frase que explique el arco de la secuencia.]

---

## Story-by-story

| # | Función | Copy on-image | Concepto visual | Sticker sugerido |
|---|---|---|---|---|
| 1 | Hook | "..." | ... | [tipo] ([contenido]) |
| 2 | ... | "..." | ... | ... |
| ... | ... | ... | ... | ... |
| N | CTA | "..." | ... | Link ("...") |

---

## Prompts para Nano Banana

> **Cómo usarlos**: pegá cada prompt en nano banana junto con la imagen de referencia del producto (la misma para las N stories). Los prompts están numerados — generá uno por uno en el orden indicado. Después de generar, agregá los stickers sugeridos directamente en Instagram al subir cada story.

### Story 1 — Hook

```
[prompt completo de la story 1, párrafo narrativo en español, todas las dimensiones del template, 9:16 + zona segura]
```

### Story 2 — [Función]

```
[prompt completo de la story 2]
```

### Story N — CTA

```
[prompt completo de la story N]
```

---

## Notas finales

[Solo si hay algo crítico que el user debe saber. Si no, omití esta sección.]
- [Nota 1, ej: "Si nano banana no respeta la tipografía exacta de la etiqueta, regenerá esa story especificando 'preserve label typography from reference image' al inicio."]
- [Nota 2, ej: "La story 4 incluye persona — si los resultados de mano salen deformes, regenerá especificando 'hands clearly visible, fingers relaxed and natural' al final del prompt."]
- [Nota 3, ej: "Para el sticker de countdown en story 1, configurá la fecha objetivo en Instagram al subir."]
```

---

## Output A/B (cuando el user pidió ambos modos visuales)

Si el user pidió A/B testing o "ambos modos", el output entrega **dos secuencias paralelas** en bloques separados. Ambas comparten copy on-image, stickers por story y lógica narrativa; varían en modo visual (lente, mood, luz, persona, paleta, color del texto, escena).

Estructura:

```markdown
# Stories: [Nombre del Producto] — A/B

## Contexto compartido

**Producto**: [nombre exacto]
**Tipo de secuencia**: [arquetipo]
**Stories**: [N por secuencia]
**Idioma copy**: es
**Aspect ratio**: 9:16 (1080x1920, Instagram Stories)
**Lógica narrativa**: [una frase, igual para A y B]
**Tipografía heredada**: [familia + características — la misma en A y B]

**Copy on-image por story** (mismo en A y B):
- Story 1: "..."
- Story 2: "..."
- Story N: "..."

**Stickers sugeridos por story** (mismos en A y B):
- Story 1: [tipo + contenido]
- Story 2: [tipo + contenido]
- Story N: Link ("...")

---

## Secuencia A · Minimalista

**Mood**: [una palabra]
**Lente**: [mm + apertura, típico 50mm a f/2.0–2.2]
**Luz**: [softbox, neutra 5000K]
**Persona**: no
**Paleta**: 3-4 hex heredados del producto
**Color del texto on-image**: [hex de la paleta]

### Tabla story-by-story (Secuencia A)
[tabla con concepto visual de cada story en clave minimalista]

### Prompts (Secuencia A)
[3 a 6 prompts numerados, cada uno en bloque de código]

---

## Secuencia B · Lifestyle cinematográfico

**Mood**: [dos palabras: acción + temperatura emocional]
**Lente**: [típico 35mm a f/2.8]
**Luz**: [cálida lateral 3200K, contraste alto]
**Persona**: sí (en qué stories)
**Paleta extendida**: 5-6 hex (producto + entorno)
**Color del texto on-image**: blanco hueso #ECE7DC con jerarquía bold/regular

### Tabla story-by-story (Secuencia B)
[tabla con concepto visual de cada story en clave lifestyle]

### Prompts (Secuencia B)
[3 a 6 prompts numerados, cada uno en bloque de código]

---

## Notas finales

- **Cómo testear**: [sugerencia concreta — ej: subí A en historia destacada permanente y B en stories del día. Medí completion rate y respuestas al sticker de engagement.]
- [Notas técnicas si aplican: tipografía, persona, sticker config, etc.]
```

### Reglas A/B
- Las dos secuencias **comparten** copy on-image, sticker por story, lógica narrativa, hook, CTA. **No varíes el copy entre A y B** — eso rompe la comparación.
- Cada secuencia trae sus propios prompts completos (no medio prompt + delta).
- El bloque "Cómo usarlos" puede aparecer una sola vez al inicio del output, indicando que aplica a las dos secuencias.

---

## Reglas duras del output

1. **Siempre** este orden: brief → tabla story-by-story (con columna sticker) → prompts → notas (opcional). Para A/B: contexto compartido → secuencia A completa → secuencia B completa → notas.
2. **Siempre** los prompts numerados, en bloques de código separados.
3. **Siempre** el bloque de "Cómo usarlos" antes del primer prompt, mencionando que los stickers se agregan en Instagram al subir.
4. **Nunca** mezcles los prompts en un solo bloque — uno por story, separados.
5. **Nunca** agregues preámbulos tipo *"¡Acá tenés tu secuencia!"* — empezá directo con el `# Stories: ...`.
6. **Nunca** agregues cierre tipo *"Espero que te sirva, avisame si querés ajustes"* — terminá con las notas finales o sin nada.
7. **Sí** ofrecé al final, en una sola línea, ajustes posibles:
   > *"Si querés cambiar el hook, ajustar una story o regenerar un prompt específico, decime cuál."*

---

## Cuándo agregar notas finales

Solo si:
- Hay una story que puede ser complicada de generar (persona, texto largo, tipografía específica).
- La tipografía del producto no es clara y el user puede tener que ajustar.
- Hay variaciones recomendadas (ej: si el primer pase no convence, qué probar).
- Hay stickers que requieren configuración específica en Instagram (countdown con fecha, quiz con respuesta correcta, link con URL).

Si los prompts están sólidos y nada complicado a la vista → **no agregues notas**. Output más limpio.

---

## Validación final antes de entregar

Antes de mostrar el output al user, corré el `eval/quality_checklist.md` completo. Si algo falla:
- Story específica falla → regenerá ese prompt.
- Algo del brief falla (ej: paleta mal extraída) → corregí y volvé a correr el check.
- **No entregues** hasta pasar el checklist al 100%.

---

## Ejemplo de output final completo (resumido)

```markdown
# Stories: Eau de Parfum "Solar 04"

## Brief creativo

**Producto**: Eau de Parfum "Solar 04" — 50ml
**Tipo de secuencia**: Listicle (3 razones)
**Stories**: 5
**Idioma copy**: es
**Mood**: lujo sensorial silencioso
**Estilo visual**: editorial mediterráneo
**Lente de la secuencia**: 85mm a f/2.0
**Tratamiento de luz**: luz cálida de ventana lateral, temperatura 3200K, soft directional
**Aspect ratio**: 9:16 (1080x1920, Instagram Stories)

**Paleta heredada del producto**:
- blanco hueso — #F2EBDD
- dorado antiguo — #B89968
- ámbar profundo — #6B3410
- sombra carbón — #2A241D

**Tipografía heredada**: serif moderna de alto contraste, similar a Didot, mayúsculas con tracking abierto

**Lógica narrativa**:
Hook con la promesa numerada → tres razones técnicas concretas → CTA con prueba garantizada.

---

## Story-by-story

| # | Función | Copy on-image | Concepto visual | Sticker sugerido |
|---|---|---|---|---|
| 1 | Hook | "Por qué dura 12+ horas" | Frasco sobre pedestal de mármol, alcoba mediterránea, texto en zona segura central | Pregunta ("¿cuánto te dura el tuyo?") |
| 2 | Razón 1 | "01 · Liberación gradual" | Macro con sombra de hoja seca atravesando la etiqueta | Ninguno |
| 3 | Razón 2 | "02 · Base de candelilla" | Frasco junto a terrón de cera natural sobre lino crudo | Ninguno |
| 4 | Razón 3 | "03 · Aplicar en piel húmeda" | Persona aplicándose perfume en la muñeca, momento candid | Slider de emoji (🔥) |
| 5 | CTA | "Probalo · 30 días" | Frasco frontal sobre superficie limpia, máxima legibilidad | Link ("comprá") |

---

## Prompts para Nano Banana

> **Cómo usarlos**: pegá cada prompt en nano banana junto con la imagen de referencia del producto. Los prompts están numerados — generá uno por uno en el orden indicado. Después de generar, agregá los stickers sugeridos directamente en Instagram al subir cada story.

### Story 1 — Hook

\`\`\`
Usá la imagen de producto provista como sujeto exacto — conservá el frasco de vidrio ámbar, la tipografía de la etiqueta y la tapa dorada idénticos — y ubicá el frasco sobre un pedestal de mármol gastado... [prompt completo en 9:16 con zona segura]
\`\`\`

### Story 2 — Razón 1

\`\`\`
[prompt completo]
\`\`\`

[... resto de stories ...]

### Story 5 — CTA

\`\`\`
[prompt completo]
\`\`\`

---

Si querés cambiar el hook, ajustar una story o regenerar un prompt específico, decime cuál.
```

Ese es el formato exacto. Limpio, escaneable, listo para copiar y pegar en nano banana, con stickers definidos para configurar en Instagram al subir.
