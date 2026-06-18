# 06 — Output Format

Acá entregás. Después de Concept + Prompt Generation + Self-check, formateás el output final con el formato exacto que el user espera.

---

## Estructura exacta del output final

> Si el user pidió **A/B** (dos modos visuales paralelos), saltá a la sección "Output A/B" más abajo. Para un solo carrusel, seguí esta estructura.

```markdown
# Carrusel: [Nombre del Producto]

## Brief creativo

**Producto**: [nombre exacto del producto]
**Tipo de carrusel**: [arquetipo]
**Slides**: [N]
**Idioma copy**: [es]
**Modo visual**: [Minimalista / Lifestyle cinematográfico]
**Mood**: [una a dos palabras]
**Estilo visual**: [editorial / lifestyle / minimal / etc.]
**Lente del carrusel**: [mm + apertura]
**Tratamiento de luz**: [una frase]

**Paleta heredada del producto**:
- [color 1] — [#hex]
- [color 2] — [#hex]
- [color 3] — [#hex]
- [color 4] — [#hex]

**Tipografía heredada**: [familia + características]

**Lógica narrativa**:
[Una frase que explique el arco del carrusel.]

---

## Slide-by-slide

| # | Función | Copy on-image | Concepto visual |
|---|---|---|---|
| 1 | Hook | "..." | ... |
| 2 | ... | "..." | ... |
| ... | ... | ... | ... |
| N | CTA | "..." | ... |

---

## Imágenes generadas

> Estas son las imágenes ya generadas con Indash (paso 7). Para cada slide: la URL pública + el modelo usado.

| # | Función | Modelo | Imagen |
|---|---|---|---|
| 1 | Hook | nano-banana / gpt-image | [URL] |
| 2 | ... | ... | [URL] |
| N | CTA | ... | [URL] |

---

## Prompts (registro)

> Los prompts con los que se generó cada slide, por si querés regenerar o ajustar. Para regenerar un slide, se reusa el prompt con el modelo indicado, `aspect_ratio: "4:5"` y las mismas referencias.

### Slide 1 — Hook _(modelo: [nano-banana / gpt-image])_

```
[prompt completo del slide 1, párrafo narrativo en español, todas las dimensiones del template]
```

### Slide 2 — [Función]

```
[prompt completo del slide 2]
```

### Slide N — CTA

```
[prompt completo del slide N]
```

---

## Notas finales

[Solo si hay algo crítico que el user debe saber. Si no, omití esta sección.]
- [Nota 1, ej: "Si nano banana no respeta la tipografía exacta de la etiqueta, regenerá ese slide especificando 'preserve label typography from reference image' al inicio."]
- [Nota 2, ej: "El slide 4 incluye persona — si los resultados de mano salen deformes, regenerá especificando 'hands clearly visible, fingers relaxed and natural' al final del prompt."]
```

---

## Output A/B (cuando el user pidió ambos modos visuales)

Si el user pidió A/B testing o "ambos modos", el output entrega **dos carruseles paralelos** en bloques separados. Ambos comparten copy on-image, narrativa, hook y CTA; varían en modo visual (lente, mood, luz, persona, paleta, color del texto, escena, elementos gráficos).

Estructura:

```markdown
# Carrusel: [Nombre del Producto] — A/B

## Contexto compartido

**Producto**: [nombre exacto]
**Tipo de carrusel**: [arquetipo]
**Slides**: [N por carrusel]
**Idioma copy**: es
**Aspect ratio**: 4:5 (1080x1350)
**Lógica narrativa**: [una frase, igual para A y B]
**Tipografía heredada**: [familia + características — la misma en A y B]

**Copy on-image por slide** (mismo en A y B):
- Slide 1: "..."
- Slide 2: "..."
- Slide N: "..."

---

## Carrusel A · Minimalista

**Mood**: [una palabra]
**Lente**: [mm + apertura, típico 50mm a f/2.0–2.2 o 85mm a f/2.0]
**Luz**: [softbox, neutra 5000-5500K]
**Persona**: no (o muy controlada en un slide específico)
**Paleta**: 3-4 hex heredados estrictos del producto
**Color del texto on-image**: [hex de la paleta]
**Elementos gráficos**: ninguno (sin pills, sin íconos)

### Tabla slide-by-slide (Carrusel A)
[tabla con concepto visual de cada slide en clave minimalista]

### Prompts (Carrusel A)
[3 a 7 prompts numerados, cada uno en bloque de código]

---

## Carrusel B · Lifestyle cinematográfico

**Mood**: [una a dos palabras]
**Lente**: [típico 35mm a f/2.8]
**Luz**: [cálida lateral 3200-3400K, contraste medio-alto]
**Persona**: sí (en qué slides)
**Paleta extendida**: 5-6 hex (producto + entorno)
**Color del texto on-image**: blanco hueso #ECE7DC con jerarquía bold/regular
**Elementos gráficos**: pills + brand mark + (si aplica) íconos lineales

### Tabla slide-by-slide (Carrusel B)
[tabla con concepto visual de cada slide en clave lifestyle]

### Prompts (Carrusel B)
[3 a 7 prompts numerados, cada uno en bloque de código]

---

## Notas finales

- **Cómo testear**: [sugerencia concreta — ej: subí A en post permanente y B como segundo post de la misma campaña. Medí saves, shares, profile visits y CTR del último slide.]
- [Notas técnicas si aplican: tipografía, persona, render de pills/íconos, etc.]
```

### Reglas A/B
- Los dos carruseles **comparten** copy on-image, narrativa, hook, CTA. **No varíes el copy entre A y B** — eso rompe la comparación.
- Cada carrusel trae sus propios prompts completos (no medio prompt + delta).
- El bloque "Cómo usarlos" puede aparecer una sola vez al inicio del output, indicando que aplica a los dos carruseles.

---

## Reglas duras del output

1. **Siempre** este orden: brief → tabla slide-by-slide → prompts → notas (opcional). Para A/B: contexto compartido → carrusel A completo → carrusel B completo → notas.
2. **Siempre** los prompts numerados, en bloques de código separados.
3. **Siempre** el bloque de "Cómo usarlos" antes del primer prompt.
4. **Nunca** mezcles los prompts en un solo bloque — uno por slide, separados.
5. **Nunca** agregues preámbulos tipo *"¡Acá tenés tu carrusel!"* — empezá directo con el `# Carrusel: ...`.
6. **Nunca** agregues cierre tipo *"Espero que te sirva, avisame si querés ajustes"* — terminá con las notas finales o sin nada.
7. **Sí** ofrecé al final, en una sola línea, ajustes posibles si los hay:
   > *"Si querés cambiar el hook, ajustar un slide o regenerar un prompt específico, decime cuál."*

---

## Cuándo agregar notas finales

Solo si:
- Hay un slide que puede ser complicado de generar (persona, texto largo, tipografía específica).
- La tipografía del producto no es clara y el user puede tener que ajustar.
- Hay variaciones recomendadas (ej: si el primer pase no convence, qué probar).

Si los prompts están sólidos y nada complicado a la vista → **no agregues notas**. Output más limpio.

---

## Guardado del entregable (paso 9 — no negociable)

El entregable **no solo se muestra en el chat: también se guarda en disco**. Esta convención es **global** (vive en `hooks/context/stack-policy.md`, no se redefine por cliente).

**Qué se guarda**: el output completo de esta sección — brief creativo + tabla slide-by-slide + tabla de imágenes generadas (URLs) + los N prompts. Es el mismo markdown que mostrás en el chat.

**Dónde**:
- Si estás **dentro de una carpeta de cliente** (tiene `entregables/`): guardá en `entregables/carruseles/`. Si la subcarpeta `carruseles/` no existe, creala.
- Si **no** hay estructura de cliente en el directorio actual: guardá en `./entregables/carruseles/` del directorio de trabajo (creándolo) y avisale al user que conviene dar de alta el cliente con `new-client` para tener todo ordenado.

**Nombre del archivo (canónico)**: `<AAAA-MM-DD>_<producto-slug>_v<N>.md`
- `<AAAA-MM-DD>` = fecha del día.
- `<producto-slug>` = nombre del producto en kebab-case, sin acentos (ej: "Solar 04" → `solar-04`).
- `v<N>` = versión: `v1` la primera; subí el número en cada regeneración del mismo producto/día.
- A/B → sufijo `-A` / `-B` (ej: `2026-06-17_solar-04_v1-A.md` y `..._v1-B.md`).

**Imágenes generadas (si las guardás en disco)**: van en una subcarpeta con el **mismo nombre sin `.md`**: `entregables/carruseles/2026-06-17_solar-04_v1/`.

**Reglas de guardado**:
1. **Siempre** mostrás el resultado en el chat **y además** lo guardás con el nombre canónico.
2. **Nunca pises** un archivo existente: si el nombre ya existe, subí la versión (`v2`, `v3`…).
3. Al entregar, decí en **una línea** la ruta exacta donde lo guardaste.

---

## Validación final antes de entregar

Antes de mostrar el output al user, corré el `eval/quality_checklist.md` completo. Si algo falla:
- Slide específico falla → regenerá ese prompt.
- Algo del brief falla (ej: paleta mal extraída) → corregí y volvé a correr el check.
- **No entregues** hasta pasar el checklist al 100%.

---

## Ejemplo de output final completo (resumido)

```markdown
# Carrusel: Eau de Parfum "Solar 04"

## Brief creativo

**Producto**: Eau de Parfum "Solar 04" — 50ml
**Tipo de carrusel**: Listicle (3 razones)
**Slides**: 5
**Idioma copy**: es
**Modo visual**: Minimalista
**Mood**: lujo sensorial silencioso
**Estilo visual**: editorial mediterráneo
**Lente del carrusel**: 85mm a f/2.0
**Tratamiento de luz**: luz cálida de ventana lateral, temperatura 3200K, soft directional

**Paleta heredada del producto**:
- blanco hueso — #F2EBDD
- dorado antiguo — #B89968
- ámbar profundo — #6B3410
- sombra carbón — #2A241D

**Tipografía heredada**: serif moderna de alto contraste, similar a Didot, mayúsculas con tracking abierto

**Lógica narrativa**:
Hook con la promesa numerada → tres razones técnicas concretas → CTA con prueba garantizada.

---

## Slide-by-slide

| # | Función | Copy on-image | Concepto visual |
|---|---|---|---|
| 1 | Hook | "Por qué dura 12+ horas" | Frasco sobre pedestal de mármol, alcoba mediterránea, espacio arriba para titular |
| 2 | Razón 1 | "01 · Liberación gradual de moléculas" | Macro con sombra de hoja seca atravesando la etiqueta |
| 3 | Razón 2 | "02 · Base oclusiva de cera de candelilla" | Frasco junto a terrón de cera natural sobre lino crudo |
| 4 | Razón 3 | "03 · Aplicación en piel húmeda" | Persona aplicándose perfume en la muñeca, momento candid |
| 5 | CTA | "Probalo 30 días · si no convence, devolvemos" | Frasco frontal sobre superficie limpia, máxima legibilidad |

---

## Prompts para Nano Banana

> **Cómo usarlos**: pegá cada prompt en nano banana junto con la imagen de referencia del producto. Los prompts están numerados — generá uno por uno en el orden indicado.

### Slide 1 — Hook

\`\`\`
Usá la imagen de producto provista como sujeto exacto — conservá el frasco de vidrio ámbar, la tipografía de la etiqueta y la tapa dorada idénticos — y ubicá el frasco sobre un pedestal de mármol gastado dentro de una alcoba mediterránea iluminada por el sol... [prompt completo]
\`\`\`

### Slide 2 — Razón 1

\`\`\`
[prompt completo]
\`\`\`

[... resto de slides ...]

### Slide 5 — CTA

\`\`\`
[prompt completo]
\`\`\`

---

Si querés cambiar el hook, ajustar un slide o regenerar un prompt específico, decime cuál.
```

Ese es el formato exacto. Limpio, escaneabe, listo para copiar y pegar en nano banana.
