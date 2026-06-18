# Bad example — Street vox-pop bloss en Seedance 2.0 (3 iteraciones fallidas)

**Caso real ocurrido 2026-05-18.** Pedido: ad UGC 15s 9:16 estilo "street vox-pop mexicano", 2 mujeres (entrevistadora + entrevistada con cicatrices de acné), entrevistadora ofrece bloss. Modelo: Seedance 2.0. Audio nativo en juego.

Resultado: **3 iteraciones de video que fallaron por razones distintas pero relacionadas**. Cada iteración resolvió un problema y abrió otro. Documenta el cluster de errores a evitar y la lección general: **el experto soy yo, no el usuario**.

---

## Iteración 1 — audio nativo OFF, articulación minimal

**Decisión:** seguir la regla del framework "español + Seedance = audio OFF + voz aparte + lipsync en post" → pedí `lips move in minimal conversational articulation synced to off-camera voice (no native audio generation)`.

**Resultado:** video estático. Las dos mujeres apenas mueven los labios. El video lee como "foto en movimiento", no como entrevista viva.

**Causa raíz:** la articulación "minimal" deja material insuficiente para una entrevista — el espectador percibe la escena como muerta antes de que el lipsync en post pueda compensar.

**Decisión que pareció buena pero fue mala:** invertir a audio nativo ON para forzar dinamismo (iteración 2).

---

## Iteración 2 — audio nativo ON, articulación expresiva

**Decisión:** activar `generate_audio: true` y pedir `full natural conversational articulation, animated, expressive, lips move continuously`. Razonamiento: el modelo va a generar movimiento de labios más rico si está pensando "está sonando voz" internamente.

**Resultado real:**
- ✅ Mucho más dinámica visualmente (gestos, micro-risas, eyebrow raises).
- ❌ **Audio en español alucinó completamente** — palabras inventadas, fonemas que no son español, pronunciación rota. La regla del framework existe por una razón y la rompí.
- ❌ El iPhone + clip-on mic rosa derivó visualmente entre cuts (color exacto, posición, integridad del prop).
- ❌ "No se ve TAN realista" — el render tuvo look AI/3D suave característico de Seedance cuando se le piden demasiados elementos simultáneos.

**Causas raíz:**

1. **Confundí "audio nativo ON" con "necesario para dinamismo".** Seedance genera articulación viva sin necesitar audio ON — solo hay que pedir performance expresiva explícita en el prompt + dejar audio OFF.

2. **El clip-on mic rosa es un prop excesivamente específico.** Multi-subject consistency es debilidad documentada de Seedance 2.0. Sumar un prop pequeño con color específico que tiene que mantenerse idéntico entre cuts es agregar punto de falla.

3. **Demasiados elementos compitiendo:** 2 personas + props específicos (iPhone + mic) + setting urbano + transformación visual + cast consistency en 15s. Seedance degrada cuando se le pide mucho.

---

## Iteración 3 — sin clip-on mic + photorealism reforzado

**Decisión:** sacar el mic, dejar solo iPhone, reforzar `RAW DOCUMENTARY PHOTOREALISM, shot on iPhone 15 Pro front camera, NOT animated, NOT 3D, NOT illustrated` en el prompt. Bajar duración a 12s.

**Problema descubierto en los frames Nano Banana antes de lanzar Seedance:**

**El iPhone solo (sin mic) no comunica "te estoy entrevistando".** Lee como "tomá mi celular" o "mirá esto en mi pantalla". La narrativa visual del formato vox-pop se quiebra: sin el mic clip-on que es el "tell" del género, el iPhone extendido es ambiguo. Y en Shot 3 la entrevistadora con un iPhone pelado en la mano izquierda mientras ofrece el producto con la derecha lee directamente raro.

**Causa raíz adicional descubierta:** **el usuario me marcó algo que yo debí haber visto.** No apliqué quality checklist a los frames antes de mostrárselos. Le delegué la validación crítica a él en lugar de hacerla yo como Senior Creative Director.

**Segundo problema descubierto:** regeneré Shot 1 v3 pero NO regeneré Shot 2 (que usaba el Shot 1 original como `reference_image_url`). Resultado: el cast de la entrevistada en Shot 2 NO matchea con Shot 1 v3 y Shot 3 v3. Lo marcó el usuario, otra vez en lugar de yo.

---

## Lecciones consolidadas

### 1. Audio nativo: regla dura sin excepciones para español regional

- **Español regional + Kling 3.0 o Seedance 2.0 = audio nativo OFF, siempre.**
- Para dinamismo de articulación, audio OFF + `natural expressive conversational articulation as if speaking, full mouth movement, not minimal` en el prompt es **suficiente**. No hace falta activar audio nativo.
- El "trade-off" de "audio ON para que el video se vea vivo" es **falso** — la articulación expresiva se pide explícitamente y se obtiene sin generar audio. Audio nativo en español solo agrega alucinación que después hay que tirar entera.

→ Codificado en `style/writing_rules.md` regla 33.

### 2. Minimalismo de props en Seedance multi-subject

- Cada prop específico (color exacto, marca visible, micro-detalle) que tiene que mantenerse consistente entre cuts es **un punto de falla**. Multi-subject consistency es debilidad oficial de Seedance 2.0.
- **Regla:** en escenas multi-subject (2+ personas), minimizar props a lo esencial. Para "street interview", el mic clip-on rosa es un nice-to-have, no un essential — y costó más de lo que aportó.
- Si el concept "necesita" un prop específico para leer bien, considerar: ¿se puede leer la narrativa sin él? Si sí, sacarlo. Si no, simplificar el prop a la versión más genérica posible (mic de mano corto sin color específico, en lugar de clip-on con marca/color específico).

→ Codificado en `style/writing_rules.md` regla 34 y `instructions/strategy.md` sección "Minimalismo de elementos en multi-subject Seedance".

### 3. Si cambio un elemento del concept visual, re-validar narrativa

- Saqué el mic para resolver derivación → introduje ambigüedad narrativa nueva (iPhone solo no comunica entrevista).
- **Regla:** cuando sacas o cambias un elemento clave del concept visual, **re-validar que toda la escena se sigue leyendo correctamente como lo que es**. No asumir que la narrativa sobrevive el cambio.
- Caminos posibles cuando un elemento clave deriva:
  - (a) simplificar la versión del elemento (mic genérico en lugar de mic específico)
  - (b) reemplazarlo por otro que cumpla la misma función narrativa
  - (c) sacarlo + adaptar el resto del concept para que la narrativa funcione sin él
- (c) es lo que terminé proponiendo (sin iPhone/mic, "amiga que se acerca a otra en la calle") — pero llegué tarde, después de 3 iteraciones.

→ Codificado en `style/writing_rules.md` regla 35.

### 4. Anchor frame propagation — si regenero un anchor, regenero los dependientes

- Regeneré Shot 1 v3 (anchor del cast).
- Shot 2 v3 dependía del Shot 1 original como `reference_image_url`. NO lo regeneré → cast desincronizado entre Shot 1 v3 y Shot 2.
- **Regla:** si regenero un frame que es anchor de otros (vía `reference_image_url`), TODOS los frames dependientes deben regenerarse con el nuevo anchor.
- Aplica a cast anchors, product anchors, setting anchors.

→ Codificado en `style/writing_rules.md` regla 36 y `eval/quality_checklist.md` sección M.

### 5. Self-validation antes del usuario — soy el experto, no él

- **El usuario me marcó cosas dos veces que yo debí haber visto** (cast desincronizado entre Shot 1 v3 y Shot 2, ambigüedad narrativa al sacar el mic).
- El rol del skill es "Senior UGC Creative Director" — eso implica aplicar el quality checklist a los outputs YO antes de mostrárselos al usuario. No le toca a él validar criterios técnicos que están escritos en el framework.
- **Regla:** antes de mostrar frames o videos al usuario, correr el quality checklist completo internamente. Marcar inconsistencias YO. Si encuentro algo que falla, decirlo (no esconderlo) + proponer el fix.
- El usuario decide la dirección creativa. **Yo decido si el output cumple el estándar técnico.**

→ Codificado en `skill.md` workflow paso 8.5 y `eval/quality_checklist.md` sección N.

---

## Resumen de cambios incorporados al framework

| Archivo | Cambio |
|---|---|
| `style/writing_rules.md` | Reglas 33-36 (audio strategy refinada, minimalismo props, narrative re-validation, anchor propagation) |
| `instructions/strategy.md` | Nueva sección "Minimalismo de elementos en multi-subject Seedance" |
| `instructions/execution.md` | Refinada regla de articulación: NO requiere audio ON para dinamismo |
| `skill.md` | Workflow paso 8.5 (self-validation antes del usuario) |
| `eval/quality_checklist.md` | Secciones M (anchor propagation) y N (self-validation pre-entrega) |

---

## Si tuviera que rehacerlo desde cero

1. **Concept revisado primero:** sin iPhone, sin mic — "amiga que se acerca a otra en la calle a preguntarle algo casual". Menos props, más realismo, narrativa que se lee por gesto + guión (que va en voiceover post). Reduce multi-subject complexity drastically.
2. **Audio nativo OFF desde el primer render.** Sin excepciones para español regional.
3. **Articulación expresiva pedida explícitamente** en el prompt, sin necesidad de audio ON. `natural full conversational articulation as if speaking, lips move continuously and expressively, not minimal, not stiff`.
4. **Frames Nano Banana validados POR MÍ contra el checklist** antes de mostrarlos al usuario. Cast consistency, props minimalistas, narrativa visual que se lee sin necesidad de explicación.
5. **Si regenero un anchor → regenero todos los dependientes.**
6. **Solo después de los 4 frames validados internamente, lanzar Seedance** con 12s (no 15s), audio OFF, énfasis photorealism.
