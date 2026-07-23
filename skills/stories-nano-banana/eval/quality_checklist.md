# Quality Checklist — Self-check antes de entregar

Corré este checklist **antes** de mostrar el output al user. Si algo falla, regenerá esa parte. **No entregues nada que no pase el 100% de los checks aplicables.**

---

## Sección 1 — Brief creativo

- [ ] Nombre del producto es **exacto** según la URL (no abreviado, no traducido).
- [ ] Tipo de secuencia está confirmado y matchea uno de los 6 arquetipos.
- [ ] Cantidad de stories está entre **3 y 6**.
- [ ] Aspect ratio **9:16 (1080x1920, Instagram Stories)** está mencionado.
- [ ] Mood está expresado en **una a dos palabras precisas**, no en lista de adjetivos.
- [ ] Paleta tiene entre **3 y 5 colores**, todos con descripción + hex.
- [ ] Tipografía heredada está descripta con **categoría + características** (no solo nombre genérico).
- [ ] Lógica narrativa está en **una frase**, no en párrafo.
- [ ] Estilo visual + lente + tratamiento de luz están definidos.

---

## Sección 2 — Story-by-story (tabla)

Para cada story:

- [ ] Función está clara (Hook / [arquetipo-específica] / CTA).
- [ ] Copy on-image tiene **≤6-8 palabras** (más corto que carrusel).
- [ ] Copy on-image es **específico** (números crudos cuando los hay, no marketing-speak).
- [ ] Copy on-image **no tiene emojis** (salvo que el user los pidió).
- [ ] Copy on-image **no tiene exclamaciones** (salvo arquetipo Promo, máx 1-2).
- [ ] Concepto visual está en **una sola frase** y especifica zona segura del texto.
- [ ] **Sticker sugerido está presente** (puede ser "ninguno").
- [ ] Listicles: estructura paralela en los ítems (todos con la misma forma gramatical).

Para el conjunto:

- [ ] Story 1 es **Hook** que frena el scroll en el primer segundo (pregunta, afirmación contraintuitiva o promesa numerada).
- [ ] Story N (última) es **CTA accionable** con verbo + acción concreta.
- [ ] Story N tiene **sticker Link**, sin excepción.
- [ ] No hay stories de relleno.
- [ ] No hay repetición de copy entre stories.
- [ ] Si hay persona, está solo en las stories donde **aporta** (no en todas).
- [ ] Variedad de stickers a lo largo de la secuencia (no todas iguales, no todas "ninguno").

---

## Sección 3 — Cada prompt individual

Corré este sub-check **story por story**:

### 3A. Estructura
- [ ] Es un **párrafo narrativo** en español, sin bullets internos.
- [ ] Longitud entre **80 y 200 palabras** (sweet spot 120-160).
- [ ] Empieza con **anclaje a la imagen de referencia** (dimensión 1).
- [ ] Termina con el **cierre técnico 9:16 + zona segura** (dimensión 9).

### 3B. Las 9 dimensiones obligatorias presentes (más la 7 si hay persona)
- [ ] 1. Anclaje a la imagen
- [ ] 2. Escena y contexto específicos (no genéricos)
- [ ] 3. Cámara: lente + ángulo + composición vertical + profundidad
- [ ] 4. Iluminación: fuente + dirección + calidad + temperatura
- [ ] 5. Estilo + textura + mood en frase precisa
- [ ] 6. Paleta heredada con hex
- [ ] 7. *(si aplica)* Persona con las 7 disciplinas
- [ ] 8. Texto on-image entre comillas con dirección quirúrgica + **zona segura especificada** *(si aplica)*
- [ ] 9. Aspect ratio **9:16** + calidad técnica + zona segura de UI

### 3C. Prohibiciones
- [ ] **No** describe el producto desde cero (solo lo ubica en la escena).
- [ ] **No** tiene listas de adjetivos pegoteadas (keyword soup).
- [ ] **No** tiene prompts negativos ("sin X, sin Y").
- [ ] **No** menciona la marca por nombre como atajo de estética ("estilo Aesop").
- [ ] **No** pide múltiples bloques de texto en la misma story.
- [ ] **No** pide efectos de movimiento (stories son imágenes estáticas).

### 3D. Texto on-image (si la story lo lleva)
- [ ] Copy va **entre comillas dobles**.
- [ ] Copy tiene **≤6-8 palabras**.
- [ ] Especifica **familia tipográfica** (heredada o descriptiva).
- [ ] Especifica **peso** (regular / bold / light, o jerarquía bold+regular si es doble peso).
- [ ] Especifica **color con hex** y ese color tiene **contraste real con la zona específica del fondo donde vive** (no en promedio del cuadro).
- [ ] Especifica **placement** eligiendo una de las 6 estrategias de `style/text_composition.md` (cabezal / pie / centro sobre producto / desplazado / wrap / doble peso), siempre dentro de la zona segura 14%-85% vertical.
- [ ] Especifica **tamaño relativo** (1/6 a 1/3 del cuadro, alineado con la jerarquía de la story).
- [ ] **Si el fondo de la zona del texto compite con la legibilidad**, especifica un tratamiento dirigido (blur / scrim 25-30% / grade local 15% / vignette / letterbox / sin tratamiento si fondo ya es monocromático).
- [ ] **Menciona explícitamente** que el texto vive dentro de la zona segura, evitando los bordes superior e inferior tapados por Instagram.

### 3E. Persona (si la story la incluye)
- [ ] **Edad concreta**, no rango (ej: "38 años", no "joven").
- [ ] **Textura de piel natural** especificada ("poros visibles, sin sobre-suavizado").
- [ ] **Expresión específica** (no "sonriendo" a secas).
- [ ] **Pose candid / espontánea** explicitada.
- [ ] Si hay manos en cuadro: **manos descriptas en detalle**.
- [ ] Casting realista, no de catálogo.

---

## Sección 4 — Consistencia entre stories

- [ ] Todos los prompts referencian la **misma imagen de producto** con la misma frase de anclaje.
- [ ] Todos comparten el **mismo lente y apertura**.
- [ ] Todos comparten el **mismo mood en una palabra**.
- [ ] Todos comparten la **misma paleta con los mismos hex**.
- [ ] Todos comparten el **mismo tratamiento general de luz** (cálida vs fría, suave vs dura).
- [ ] Todos cierran con **9:16 + zona segura**.
- [ ] Los ángulos / escenas / composiciones **varían** entre stories (no se repiten).
- [ ] **Placement del texto varía entre stories** (cabezal / pie / centro / doble peso, etc. — no clonar el mismo tercio en stories consecutivas; en secuencias de 3 usar 3 placements distintos; en 4-6 nunca más de 2 stories iguales y nunca consecutivas).
- [ ] **El CTA (última story) deja el tercio inferior libre** para el sticker de Link (texto típicamente en cabezal o centro).
- [ ] **Tratamientos de imagen varían** cuando se usan (no las N stories con el mismo blur o el mismo scrim — mezclar o usar "sin tratamiento" en al menos una).
- [ ] El producto se ve **reconocible y consistente** en las N stories (gracias al anclaje a la imagen).

---

## Sección 5 — Output formateado

- [ ] Empieza con `# Stories: [Nombre del Producto]`.
- [ ] Sigue el orden exacto: Brief → Tabla story-by-story (con columna sticker) → Prompts → Notas (opcional).
- [ ] Cada prompt está en **bloque de código separado** y numerado como "Story N".
- [ ] Hay un bloque "Cómo usarlos" antes del primer prompt, mencionando que los stickers se agregan en Instagram al subir.
- [ ] **No hay preámbulo** ("¡Acá tenés!", "¡Genial!", etc.).
- [ ] **No hay cierre de despedida** ("Espero que te sirva", "Avisame cualquier cosa").
- [ ] Termina con la línea: *"Si querés cambiar el hook, ajustar una story o regenerar un prompt específico, decime cuál."*

---

## Sección 6 — Reglas no-negociables (de SKILL.md)

- [ ] Se preguntó al user **antes** de generar (paso 3 Decisions).
- [ ] Output incluye **shot list (con stickers) + prompts** (no solo prompts pelados).
- [ ] Cada prompt referencia explícitamente la imagen del producto.
- [ ] Paleta y tipografía son **heredadas de la imagen** (no inventadas).
- [ ] Aspect ratio **9:16 (1080x1920)** está en cada prompt.
- [ ] **Zona segura de UI** está mencionada explícitamente en cada prompt con texto on-image.
- [ ] Última story es **CTA accionable** con sticker Link, no cierre poético.
- [ ] Cantidad de stories **entre 3 y 6**.
- [ ] Cada story tiene **sticker sugerido** (puede ser "ninguno").
- [ ] **No** hay keyword soup.
- [ ] **No** hay features inventados del producto (todo sale de la URL).
- [ ] **No** hay copy on-image vago, genérico o de más de 8 palabras.
- [ ] **No** hay emojis en el copy (salvo pedido del user).
- [ ] La skill se mantuvo **agnóstica** por marca/categoría.

---

## Si algo falla

| Tipo de falla | Acción |
|---|---|
| Falla en un prompt individual | Regenerá ese prompt aplicando la regla violada. |
| Falla en consistencia (Sección 4) | Reescribí los prompts para alinear lente/mood/paleta/luz. |
| Falla en brief o tabla | Corregí el brief y reescribí los prompts afectados. |
| Falla en zona segura | Reescribí la dimensión 8 + 9 de ese prompt. **Crítico** — sin esto el texto se tapa en Instagram. |
| Falla en sticker | Agregá la columna sticker a la tabla del shot list. La última story debe tener Link. |
| Falla en formato del output | Reordená sin tocar contenido. |
| Falla en regla no-negociable | **Frená** y volvé al paso del workflow donde se rompió. No entregues. |

---

## Criterio final de "está listo"

El output está listo solo si:

1. **Pasa todas las secciones aplicables** del checklist.
2. Si lo tomás vos como user y lo pegás en nano banana, **no necesitás editarlo**.
3. Si lo subís a Instagram Stories, **el texto on-image se ve completo** (no tapado por la UI).
4. Si lo lee otra persona, entiende la secuencia **sin pedir explicación** y sabe qué stickers configurar.

Si dudás → re-leé el output completo una vez más antes de entregar. Si seguís dudando → falta algo.
