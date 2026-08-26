# Quality Checklist — Self-check antes de entregar

Corré esto **antes** de decirle al user que está listo. Si algo falla, arreglalo
o **decilo explícito**. Esta skill la usa gente que puede no saber editar: un
problema que no señalás es un problema que se publica.

---

## Sección 1 — Entorno y proceso

- [ ] Verifiqué el entorno (o corrí `setup.sh`) **antes** de tocar un archivo.
- [ ] Usé el python del venv (`~/.indash/edicion-ugc/venv/bin/python`), no el
      `python3` del sistema.
- [ ] Apliqué el **gate condicional** del conector: avancé sin `indash` porque el
      material ya estaba en disco y lo dije en una línea; o, si hacía falta
      generar un B-roll, frené y lo pedí.
- [ ] Corrí **`revisar` antes de `montar`**. Siempre, sin excepción.
- [ ] Leí el reporte de `revisar` y actué según la tabla del `SKILL.md` — no lo
      pasé por arriba.

---

## Sección 2 — Morphs

- [ ] Si había **morph sobre voz**, conseguí un clip de producto y lo pasé como
      `broll`. Si no lo conseguí, **lo dije**: la pieza sale con un defecto
      visible.
- [ ] Si el log dijo *"taparlo se comería Xs de voz. NO se ajusta"*, **avisé al
      humano**. Eso no se resuelve solo.
- [ ] **No** interpreté `morph 0.000` como "clip limpio". Significa "sin saltos
      secos"; las derivas graduales pasan derecho y hay que mirarlas a ojo.
- [ ] Miré el video en los timestamps que reportó `revisar`.

---

## Sección 3 — La placa

- [ ] Hay placa. Si el log dijo `!! sin placa definida`, **frené** en vez de
      entregar una pieza sin cierre.
- [ ] Si el script avisó de **ambigüedad** (varios archivos candidatos), elegí
      yo el correcto y lo declaré en `placa` — no lo dejé adivinar.
- [ ] Si avisó que la placa **no es 9:16**, se lo dije al user: se recorta y
      puede perder parte del diseño.
- [ ] Si es imagen fija dura 1.50s; si es video, va entera. Lo confirmé en el log.

---

## Sección 4 — El corte

- [ ] La duración final tiene sentido contra la suma de los clips (el corpus va
      de 8.4s a 20.3s; muy fuera de ahí, mirá qué pasó).
- [ ] El empalme entre clips no repite la pose de apertura.
- [ ] No quedaron silencios muertos en cabeza ni en cola.
- [ ] Si hubo B-roll: el bloque es **uno solo**, y sus bordes no dejan 2-3
      frames de diálogo sueltos contra otro corte.
- [ ] Si toqué `broll_dur`, es porque la evidencia del largo es finita (n=4), no
      porque sí.

---

## Sección 5 — Subtítulos

- [ ] Los nombres propios de la marca están bien escritos. Si no, agregué la
      variante a `marcas_whisper` y **volví a montar**.
- [ ] Ninguna frase queda tapada, cortada ni fuera de pantalla.
- [ ] Las frases siguen a la voz: no desaparecen antes de que termine de hablar
      ni quedan colgadas después.
- [ ] Si la corrección de nombre es permanente para esa marca, la subí al
      `brand/edicion-ugc.json` del cliente en vez de dejarla en el config del
      trabajo.

---

## Sección 6 — Salida y persistencia

- [ ] El archivo quedó en `exports/videos/` de la carpeta del cliente con el
      nombre `<AAAA-MM-DD>_<slug>_v<N>.mp4`.
- [ ] **No pisé** ningún archivo existente: si el nombre estaba, subió la versión.
- [ ] El `slug` describe la pieza (producto, concepto), no es `crudo` ni
      `untitled`.
- [ ] Dije **la ruta** en una línea al entregar.
- [ ] El `_build/` de intermedios no se coló como entregable.

---

## Sección 7 — El reporte al user

El handoff dice, sí o sí:

- [ ] **Duración final.**
- [ ] **Qué se recortó** (silencios, cuánto).
- [ ] **Si hubo morph y si se tapó o no.**
- [ ] **La ruta del archivo.**
- [ ] **Lo que quedó sin resolver**, explícito y arriba, no escondido al final.
- [ ] Nada que el script no haya dicho: si no lo midió, no lo afirmes.

---

## Sección 8 — Lo que esta skill NO mira (decilo si aplica)

- [ ] **El audio**: música, tono, si la voz suena robótica. Nadie lo mide.
- [ ] **Las derivas graduales** de la cara. Solo se ven a ojo.
- [ ] **Si la pieza retiene.** El pipeline aplica constantes; no evalúa el hook
      ni el copy. Eso es criterio humano (o `hyperframes`, si hay que
      recomponerla).

---

## Criterio final de "está listo"

1. Pasa todas las secciones aplicables.
2. **Miraste el video entero**, no solo el log.
3. Si algo quedó a medias, el user lo sabe **antes** de publicarlo.

Si dudás, corré `revisar` sobre el resultado y mirá los timestamps otra vez.
