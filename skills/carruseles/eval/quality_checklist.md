# Quality Checklist — Self-check antes de entregar

Corré este checklist **antes** de mostrar el output al user. Si algo falla, regenerá esa parte. **No entregues nada que no pase el 100% de los checks aplicables.**

---

## Sección 1 — Brief creativo

- [ ] Nombre del producto es **exacto** según la URL (no abreviado, no traducido).
- [ ] Tipo de carrusel está confirmado y matchea uno de los 6 arquetipos.
- [ ] **Modo visual** está declarado (Minimalista / Lifestyle cinematográfico). Para A/B, los dos modos están declarados en bloques separados.
- [ ] Los parámetros del brief (lente, mood, luz, persona, paleta, color del texto) están **alineados al modo elegido** según `style/visual_modes.md`.
- [ ] Cantidad de slides está entre **3 y 7**.
- [ ] Mood está expresado en **una a dos palabras precisas**, no en lista de adjetivos.
- [ ] Paleta tiene **3-4 colores** (Minimalista) o **5-6 colores** (Lifestyle, sumando entorno), todos con descripción + hex.
- [ ] Tipografía heredada está descripta con **categoría + características** (no solo nombre genérico).
- [ ] Lógica narrativa está en **una frase**, no en párrafo.
- [ ] Estilo visual + lente + tratamiento de luz están definidos y son **coherentes con el modo**.

---

## Sección 2 — Slide-by-slide (tabla)

Para cada slide:

- [ ] Función está clara (Hook / [arquetipo-específica] / CTA).
- [ ] Copy on-image tiene ≤10 palabras.
- [ ] Copy on-image es **específico** (números crudos cuando los hay, no marketing-speak).
- [ ] Copy on-image **no tiene emojis** (salvo que el user los pidió).
- [ ] Copy on-image **no tiene exclamaciones** (salvo arquetipo Promo, máx 1-2).
- [ ] Concepto visual está en **una sola frase**.
- [ ] Listicles: estructura paralela en los ítems (todos con la misma forma gramatical).

Para el conjunto:

- [ ] Slide 1 es **Hook** que frena el scroll (pregunta, afirmación contraintuitiva o promesa numerada).
- [ ] Slide N (último) es **CTA accionable** con verbo + acción concreta.
- [ ] No hay slides de relleno.
- [ ] No hay repetición de copy entre slides.
- [ ] Si hay persona, está solo en los slides donde **aporta** (no en todos).

---

## Sección 3 — Cada prompt individual

Corré este sub-check **slide por slide**:

### 3A. Estructura
- [ ] Es un **párrafo narrativo** en español, sin bullets internos.
- [ ] Longitud entre **80 y 200 palabras** (sweet spot 120-160).
- [ ] Empieza con **anclaje a la imagen de referencia** (dimensión 1).
- [ ] Termina con el **cierre técnico 4:5** (dimensión 9).

### 3B. Las 8 dimensiones obligatorias presentes (más la 7 si hay persona)
- [ ] 1. Anclaje a la imagen
- [ ] 2. Escena y contexto específicos (no genéricos)
- [ ] 3. Cámara: lente + ángulo + composición + profundidad
- [ ] 4. Iluminación: fuente + dirección + calidad + temperatura
- [ ] 5. Estilo + textura + mood en frase precisa
- [ ] 6. Paleta heredada con hex
- [ ] 7. *(si aplica)* Persona con las 7 disciplinas
- [ ] 8. Texto on-image entre comillas con dirección quirúrgica *(si aplica)*
- [ ] 9. Aspect ratio + calidad técnica

### 3C. Prohibiciones
- [ ] **No** describe el producto desde cero (solo lo ubica en la escena).
- [ ] **No** tiene listas de adjetivos pegoteadas (keyword soup).
- [ ] **No** tiene prompts negativos ("sin X, sin Y").
- [ ] **No** menciona la marca por nombre como atajo de estética ("estilo Aesop").
- [ ] **No** pide múltiples bloques de texto en el mismo slide.
- [ ] **No** pide efectos de movimiento (carrusel es estático).
- [ ] **No** muestra un ángulo del producto sin tener referencia disponible de ese ángulo (espalda, lateral, interior, macro de detalle no visible en la frontal). Si el slide propone un ángulo nuevo → frená, pedí la imagen al user, no avances.

### 3D. Texto on-image (si el slide lo lleva)
- [ ] Copy va **entre comillas dobles**.
- [ ] Especifica **familia tipográfica** (heredada o descriptiva).
- [ ] Especifica **peso** (regular / bold / light).
- [ ] Especifica **color con hex**.
- [ ] Especifica **posición** (arriba / centro / abajo).
- [ ] Especifica **tamaño relativo** (1/3, 1/4, 1/5 del cuadro).
- [ ] Especifica **contraste** o espacio negativo para legibilidad.

### 3E. Persona (si el slide la incluye)
- [ ] **Edad concreta**, no rango (ej: "38 años", no "joven").
- [ ] **Textura de piel natural** especificada ("poros visibles, sin sobre-suavizado").
- [ ] **Expresión específica** (no "sonriendo" a secas).
- [ ] **Pose candid / espontánea** explicitada.
- [ ] Si hay manos en cuadro: **manos descriptas en detalle**.
- [ ] Casting realista, no de catálogo.

---

## Sección 4 — Consistencia + Variación entre slides

**Lo que debe ser igual** (consistencia):
- [ ] Todos los prompts referencian la **misma imagen de producto** con la misma frase de anclaje.
- [ ] Todos comparten el **mismo lente y apertura**.
- [ ] Todos comparten el **mismo mood en una palabra**.
- [ ] Todos comparten la **misma paleta con los mismos hex**.
- [ ] Todos comparten el **mismo tratamiento general de luz** (cálida vs fría, suave vs dura).
- [ ] El producto se ve **reconocible y consistente** en los N slides.

**Lo que debe variar** (ritmo visual):
- [ ] Los **ángulos de cámara** varían entre slides (no se repiten).
- [ ] Las **escenas / contextos** varían entre slides.
- [ ] **La posición del texto on-image varía entre al menos 2 slides** del carrusel. Ningún caso de "todos los textos en la misma zona del cuadro" (anti-patrón crítico — ver `examples/bad/ai_generico.md` MALO #9).
- [ ] **Slide 1 (Hook) y último slide (CTA) tienen composiciones claramente distintas** entre sí (apertura vs cierre).
- [ ] Si el carrusel tiene 4+ slides con texto, **al menos uno usa un tratamiento visual distinto** (texto al medio sobre imagen con blur cinematográfico, texto lateral, tipografía gigante, asimetría intencional, etc.).
- [ ] La **distancia / encuadre** varía entre slides (cerrado / abierto / macro).

---

## Sección 5 — Output formateado

- [ ] Empieza con `# Carrusel: [Nombre del Producto]`.
- [ ] Sigue el orden exacto: Brief → Tabla slide-by-slide → Prompts → Notas (opcional).
- [ ] Cada prompt está en **bloque de código separado** y numerado.
- [ ] Hay un bloque "Cómo usarlos" antes del primer prompt.
- [ ] **No hay preámbulo** ("¡Acá tenés!", "¡Genial!", etc.).
- [ ] **No hay cierre de despedida** ("Espero que te sirva", "Avisame cualquier cosa").
- [ ] Termina con la línea: *"Si querés cambiar el hook, ajustar un slide o regenerar un prompt específico, decime cuál."*

---

## Sección 6 — Reglas no-negociables (de skill.md)

- [ ] Se preguntó al user **antes** de generar (paso 3 Decisions).
- [ ] Output incluye **shot list + prompts** (no solo prompts pelados).
- [ ] **Modo visual** está propuesto y declarado (Minimalista / Lifestyle / A+B).
- [ ] Cada prompt referencia explícitamente la imagen del producto.
- [ ] **Cada slide muestra una vista del producto que tiene su correspondiente imagen de referencia provista por el user.** Ningún slide muestra un ángulo (espalda, lateral, interior, macro de detalle no visible en la frontal) sin que el user haya mandado la imagen específica. Sin esto → MALO #10, el producto se inventa.
- [ ] Paleta y tipografía son **heredadas de la imagen** (no inventadas; el modo Lifestyle puede sumar entorno pero la base es del producto).
- [ ] Aspect ratio **4:5** está en cada prompt.
- [ ] Último slide es **CTA accionable**, no cierre poético.
- [ ] Cantidad de slides **entre 3 y 7**.
- [ ] **No** hay mezcla de modos visuales dentro del mismo carrusel (un carrusel = un modo).
- [ ] Para A/B: los dos carruseles **comparten copy on-image y narrativa**, solo varían visualmente.
- [ ] **No** hay keyword soup.
- [ ] **No** hay features inventados del producto (todo sale de la URL).
- [ ] **No** hay copy on-image vago o genérico.
- [ ] **No** hay emojis en el copy (salvo pedido del user).
- [ ] La skill se mantuvo **agnóstica** por marca/categoría.

---

## Si algo falla

| Tipo de falla | Acción |
|---|---|
| Falla en un prompt individual | Regenerá ese prompt aplicando la regla violada. |
| Falla en consistencia (Sección 4) | Reescribí los prompts para alinear lente/mood/paleta/luz. |
| Falla en brief o tabla | Corregí el brief y reescribí los prompts afectados. |
| Falla en formato del output | Reordená sin tocar contenido. |
| Falla en regla no-negociable | **Frená** y volvé al paso del workflow donde se rompió. No entregues. |

---

## Criterio final de "está listo"

El output está listo solo si:

1. **Pasa todas las secciones aplicables** del checklist.
2. Si lo tomás vos como user y lo pegás en nano banana, **no necesitás editarlo**.
3. Si lo lee otra persona, entiende el carrusel **sin pedir explicación**.

Si dudás → re-leé el output completo una vez más antes de entregar. Si seguís dudando → falta algo.
