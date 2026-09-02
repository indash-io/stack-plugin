# 07 — Output format y guardado

El entregable se **muestra en el chat Y queda guardado como proyecto
reproducible**. No es opcional (regla 22 del `SKILL.md`).

Formato exacto en `templates/output_template.md`.

---

## Qué contiene el entregable

En este orden, sin excepción:

1. **Línea de contexto del editor** — una sola frase: qué pieza es, para qué
   plataforma, de cuánto.
2. **El plan de edición por segundos** — la tabla de `templates/edit_plan.md`.
3. **La composición** — el `index.html` completo, en bloque de código.
4. **Los comandos** — la escalera de gates de `instructions/06_render_qa.md`.
5. **El resultado** — en `full_render`, la ruta del MP4 renderizado; en
   `plan_only`, la nota de qué falta para renderizar.
6. **La ruta de guardado** — una línea.

**No** hay preámbulo ("¡Acá tenés!") ni cierre de despedida ("Espero que te
sirva"). Cerrás con la línea de ajustes (ver abajo).

---

## Dónde se guarda — ⚠️ convención PROVISORIA

El Studio todavía no define un lugar para el video ensamblado. Mientras tanto,
la entrega aterriza donde aterriza **todo** export del Studio: la carpeta
**Descargas** del humano.

```
~/Downloads/<brief>-<grupo>-final-v<N>/
  PLAN.md            el plan de edición completo (la pieza es reproducible sin el chat)
  index.html         la composición
  assets/            clip-01.mp4 · clip-02.mp4 · packshot.png · music.mp3 · Marca-Bold.ttf
  renders/           <grupo>_draft.mp4 · <grupo>_final_v<N>.mp4
```

- `<brief>-<grupo>` = los ids reales del plan (`2026-09-tummy-video-1`), en
  kebab-case como ya vienen.
- `v<N>` = versión de la **entrega**: `-final-v1` la primera; **versioná,
  nunca pises** — si la carpeta existe, la siguiente es `-final-v2`.
- **Todos** los assets copiados adentro, rutas relativas. El proyecto tiene que
  renderizar igual dentro de un año, sin el proyecto del Studio a mano.
- **Prohibido** guardar el proyecto o el MP4 dentro de `creatives/`, `.indash/`
  o cualquier carpeta del proyecto del Studio.
- Cuando el contrato de disco defina el destino del video final, esta
  convención cambia y la skill se actualiza. Decilo si el humano pregunta.

### Cuando el mismo corte sale en varios formatos

Cada formato es su propia composición, y viven como subcarpetas de la misma
entrega:

```
~/Downloads/<brief>-<grupo>-final-v1/
  9x16/index.html    renders/<grupo>_9x16_final_v1.mp4
  4x5/index.html     renders/<grupo>_4x5_final_v1.mp4
  assets/            ← compartida por las dos
  PLAN.md            ← un solo plan (el corte es el mismo) + deltas por formato
```

---

## Cómo se muestra en el chat

- El **plan de edición** va completo: es lo que el humano lee y aprueba.
- La **composición** va completa en bloque de código la primera vez. En las
  iteraciones posteriores, mostrá **solo el diff** (qué atributo cambió en qué
  clip) — pegar 200 líneas de HTML por cada ajuste de 0.3s no ayuda a nadie.
- En `full_render`, la ruta del MP4 va en su propia línea, destacada.

---

## Línea de cierre (siempre la misma)

> Si querés ajustar un corte, cambiar el hook, mover un caption o sacarlo en
> otro formato, decime cuál y lo cambio.

---

## Qué NO hacés en el output

- ❌ No entregues la composición sin el plan de edición.
- ❌ No entregues el plan sin la composición.
- ❌ No entregues un HTML con placeholders (`<!-- tu clip acá -->`) para que el
  humano lo complete. Si falta material, se frenó en Intake.
- ❌ No pises una entrega existente. **Versioná.**
- ❌ No te olvides de decir la ruta.
- ❌ No prometas un formato, un códec o un flag que no esté verificado en
  `reference/hyperframes.md`.
