# 04 — Concept

Después del OK del user en Decisions, armás la **narrativa slide por slide**: qué dice cada uno, qué muestra cada uno, cómo se conectan. Este paso es **trabajo silencioso** — todavía no le mostrás nada al user. El output del concept es la base sobre la que escribís los prompts en el paso 5.

---

## Qué producís en este paso

Una **tabla interna** con N filas, una por slide:

| # | Función | Copy on-image | Concepto visual (1 frase) | Persona | **Vista del producto** | **¿Tengo referencia?** | Variación de ángulo/escena |
|---|---|---|---|---|---|---|---|
| 1 | Hook | "..." | ... | no | frontal | ✅ | ... |
| 2 | ... | "..." | ... | ... | macro tachas frontal | ✅ | ... |
| ... | ... | ... | ... | ... | ... | ... | ... |
| N | CTA | "..." | ... | no | espalda | ❌ → pedir | ... |

Esta tabla **no se le muestra al user** (eso pasa en el output final, formateado). Pero es lo que vos usás para validar referencias y generar los prompts en el paso 5.

---

## Validación de referencias antes de generar (PASO BLOQUEANTE)

**Antes de pasar al paso 5 (Prompt Generation), revisá la columna "¿Tengo referencia?" de la tabla.**

- ✅ Todas las vistas tienen referencia → **avanzá**.
- ❌ Falta al menos una referencia → **frená**. Volvé a Decisions (Caso H) y resolvé:
  - Pedí las imágenes faltantes al user.
  - O reformulá el concept para que todos los slides usen vistas que sí tengas.
  - O reducí la cantidad de slides.

**Nunca generes prompts de un slide cuya vista del producto no tenés en una imagen de referencia.** Nano banana va a inventar y va a salir mal (ver `examples/bad/ai_generico.md` MALO #10).

### Vistas que típicamente requieren referencia explícita

- Espalda / dorso del producto (apparel, electrónicos, packaging con info atrás)
- Lateral / perfil
- Interior / forrería / abierto
- Macro de un detalle específico (costuras, tipografía pequeña, sello, certificación)
- Vista superior / cenital
- Producto en uso / con persona

### Vistas derivables de la frontal (no requieren referencia adicional)

- 3/4 frontal con leve giro
- Macro de un detalle que sí está en la frontal (ej: tachas del pecho de un chaleco, etiqueta del frasco)
- Hero shot frontal en distintas escenas / fondos
- Frontal con persona usándolo (la persona se referencia aparte; el producto es la frontal de siempre)

---

## Cómo escribir el copy on-image

### Reglas duras

1. **Máximo ~10 palabras por slide.** Idealmente 4-7.
2. **Específico siempre.** Genérico nunca.
   - ❌ "Calidad superior" / "Lo mejor del mercado" / "Descubrí la diferencia"
   - ✅ "12 horas de fragancia" / "10 años de garantía" / "Hecho en 4 horas"
3. **Cero emojis** salvo que el user los pidió explícitamente.
4. **Verbos en infinitivo o presente** para CTAs. Nunca pasivos.
   - ✅ "Probalo 30 días" / "Reservá el tuyo" / "Empezá tu rutina"
   - ❌ "Sea probado" / "Será reservado"
5. **Sin signos de exclamación** salvo en arquetipo Promo y con moderación.
6. **Sin marketing-speak**. Cada palabra tiene que poder defenderse.
   - ❌ "premium", "exclusivo", "único", "incomparable", "revolucionario"
   - ✅ palabras concretas que describan algo verificable.
7. **Estructura paralela en listicles**. Si el ítem 1 empieza con sustantivo, los ítems 2 y 3 también.
8. **Datos crudos cuando los tenés**. Números > adjetivos.
   - ❌ "Larga duración"
   - ✅ "12+ horas"

### Cómo definir el hook (slide 1)

El hook tiene que **frenar el scroll en 1 segundo**. Tres tácticas que funcionan:

1. **Pregunta provocadora**: *"Por qué tu protector solar no te protege"*
2. **Afirmación contraintuitiva**: *"Las prendas baratas son las más caras"*
3. **Promesa numerada concreta**: *"3 razones por las que dura 12+ horas"*

Evitá hooks tipo "Te presentamos X" o "Conocé Y" — son genéricos y no detienen.

### Cómo definir el CTA (último slide)

El CTA tiene que ser **accionable**. No "gracias por leer".

Patrones que funcionan:
- *"Probalo 30 días · garantía total"*
- *"Reservá el tuyo · 200 unidades"*
- *"Empezá tu rutina · primer mes 25% off"*
- *"Conseguilo antes del [fecha]"*
- *"Pedido en [link bio]"*

El CTA puede tener **dos partes**: acción + razón/urgencia, separadas por punto medio o salto de línea visual.

---

## Densidad de diseño (obligatorio)

Antes de escribir el concepto visual de cada slide, leé `style/design_richness.md`. Cada slide debe llevar **al menos un dispositivo de diseño** (mockup de dispositivo, diagrama con conectores, hub-and-spoke, line-icons con label, render 3D o data viz) que *explique* el mensaje — no un objeto flotante con un título encima. Definí el **template** (claro/editorial u oscuro/tech), el **sistema gráfico recurrente** (headline bicolor, indicador de progreso, brand mark, textura) y **variá el dispositivo** entre slides.

## Cómo escribir el concepto visual de cada slide

Cada concepto visual es **una sola frase** que define:

- **Sujeto en cuadro**: producto + qué más (otro objeto, persona, contexto)
- **Escena**: dónde está (tipo de superficie, entorno)
- **Ángulo**: a la altura / cenital / contrapicado / 3/4
- **Composición**: dónde queda el texto (espacio negativo arriba / abajo / lateral)

Ejemplos:

> "Frasco sobre pedestal de mármol, alcoba mediterránea, 3/4 ligero contrapicado, espacio negativo arriba para titular."

> "Macro del frasco con sombra de hoja seca atravesando la etiqueta, cenital ligero, sin espacio negativo (texto reducido)."

> "Persona aplicándose perfume en la muñeca recién salida de la ducha, plano medio 3/4, mood candid, espacio negativo a la izquierda."

---

## Cómo garantizar consistencia entre slides

Lo que **debe ser igual** en los N slides:

| Elemento | Por qué |
|---|---|
| Producto (de la referencia) | Sin esto, no es el mismo producto |
| Lente | Sin esto, los slides parecen de sesiones distintas |
| Mood | Sin esto, el carrusel se siente desarmado |
| Paleta | Sin esto, hay choque cromático |
| Tratamiento general de luz (cálida/fría, suave/dura) | Sin esto, parecen de horas distintas del día |

Lo que **debe variar** entre slides:

| Elemento | Por qué |
|---|---|
| Ángulo de cámara | Para que cada slide se vea distinto |
| Escena / contexto | Para que la narrativa avance |
| **Posición del texto on-image** | **Crítico**. Nunca todos los textos en la misma zona. Ver matriz en `style/visual_modes.md`. |
| **Tratamiento de imagen** (nítido vs blur cinematográfico) | Algunos slides nítidos, otros con leve blur que da peso al texto. |
| Distancia (cerrado / abierto / macro) | Para variar ritmo visual |
| Persona presente o no | Para variar entre presencia y "objeto en sí" |
| Jerarquía tipográfica | Un slide con titular gigante, otro con texto medio, otro con bullets distribuidos |

**Regla de oro**: si tomaras los N slides y los pusieras uno al lado del otro, deberían sentirse como **fotos de la misma sesión** (consistencia) **pero no repetidas** (variación).

### Anti-patrón crítico: texto siempre en la misma zona

Si tu Concept termina con los N slides teniendo el texto en la misma posición del cuadro (ej: "todos en el tercio superior central"), **frená**. Eso genera carruseles predecibles y planos. Volvé a la matriz de `style/visual_modes.md` y reasigná posiciones distintas según la función de cada slide:

- **Hook** → texto grande arriba o centro vertical
- **Argumento / Desarrollo** → texto arriba con bullets/pills abajo, o texto lateral
- **Concepto / Prueba intermedio** → texto al medio sobre imagen con blur cinematográfico
- **Penúltimo / Bullets** → titular arriba + bullets distribuidos
- **CTA** → CTA abajo, producto al medio o arriba (composición invertida respecto al hook)

Ver el caso real comentado en `examples/bad/ai_generico.md` MALO #9.

---

## Cómo aplicar el arquetipo elegido

Andá a `templates/carousel_archetypes.md` y seguí la estructura del arquetipo confirmado en Decisions:

- **Educativo**: hook (problema) → causa → solución → CTA
- **Hot take**: hook (afirmación polémica) → argumento → evidencia → CTA
- **Listicle**: hook (promesa numerada) → ítem 1 → ítem 2 → ítem N → CTA
- **Caso de estudio**: hook (resultado) → antes → después → CTA
- **Storytelling**: hook (pregunta) → origen → proceso → resultado → CTA
- **Promo**: hook (qué) → detalle → urgencia → CTA

Adaptá el copy y el concepto visual de cada slide a su función dentro del arquetipo.

---

## Anti-patrones a evitar

1. **Slide de relleno**: si un slide no aporta nada, sacalo. Mejor 4 buenos que 6 mediocres.
2. **Doble hook**: solo el slide 1 es hook. Los siguientes son desarrollo.
3. **Repetición visual**: si dos slides son casi idénticos, fusionalos o cambiá uno.
4. **Copy genérico en slides intermedios**: cada slide tiene que decir algo único.
5. **CTA poético**: el último slide es para acción, no para reflexión.
6. **Cambio brusco de mood**: si el carrusel arranca calmo y termina enérgico, hay un problema de coherencia.

---

## Checklist antes de pasar al paso 5

- [ ] Cada slide tiene función clara (hook / desarrollo / CTA).
- [ ] Cada copy on-image tiene ≤10 palabras y dice algo específico.
- [ ] Cada concepto visual está en una sola frase.
- [ ] **Cada slide tiene una vista del producto identificada** y **una imagen de referencia disponible para esa vista**. Si falta referencia para algún slide → frená y volvé a Decisions (Caso H).
- [ ] Los N slides comparten lente + mood + paleta + luz general.
- [ ] Los N slides varían ángulo + escena + composición + **posición del texto** + **tratamiento de imagen**.
- [ ] **Al menos 2 de los N slides usan posiciones de texto distintas entre sí** (no todos arriba, no todos abajo, no todos en el mismo lugar).
- [ ] **Slide 1 (Hook) y último slide (CTA) tienen composiciones distintas** entre sí (apertura vs cierre).
- [ ] Slide 1 frena el scroll. Slide N tiene CTA accionable con verbo.
- [ ] Si hay persona, está solo en slides donde aporta (no en todos).
- [ ] No hay repetición visual entre slides.
- [ ] Cada slide podría defenderse solo (no necesita el contexto de otro para entenderse).

Si pasa todo → andá a `instructions/05_prompt_engineering.md` + `templates/prompt_template.md` y escribí los N prompts.
