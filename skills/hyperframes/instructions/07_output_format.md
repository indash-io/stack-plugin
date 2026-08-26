# 07 — Output format y guardado

El entregable se **muestra en el chat Y se guarda en disco**. No es opcional
(regla 21 del `SKILL.md`; convención global en `hooks/context/stack-policy.md`).

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

## Dónde se guarda

| Qué | Dónde |
|---|---|
| El `.md` del entregable | `exports/videos/<AAAA-MM-DD>_<concepto-slug>_v<N>.md` |
| El proyecto HyperFrames + los renders | `exports/videos/<AAAA-MM-DD>_<concepto-slug>_v<N>/` |

- `<AAAA-MM-DD>` = fecha del día.
- `<concepto-slug>` = el concepto o producto en kebab-case, **sin acentos**
  ("Solar 04 demo" → `solar-04-demo`).
- `v<N>` = versión. `v1` la primera; **versioná, nunca pises**: si el nombre ya
  existe, subí a `v2`, `v3`… A/B → sufijo `-A` / `-B`
  (`2026-08-25_solar-04-demo_v1-A.md`).
- La subcarpeta lleva **el mismo nombre sin `.md`**.

Si **no** hay estructura de cliente en el directorio actual, guardá en
`./exports/videos/` del directorio de trabajo (creándolo) y avisale al user en
una línea que conviene dar de alta el cliente con `new-client` para tener todo
ordenado.

### Cuando el mismo corte sale en varios formatos

Cada formato es su propia composición, y viven como subcarpetas del mismo set:

```
exports/videos/2026-08-25_solar-04-demo_v1/
  9x16/index.html   renders/solar-04-demo_9x16_v1.mp4
  4x5/index.html    renders/solar-04-demo_4x5_v1.mp4
  assets/           ← compartida por las dos
```

En el `.md` del entregable va **un plan de edición** (el corte es el mismo) y
una nota por formato con lo que cambia: reencuadres y posición del texto.

---

## Cómo se muestra en el chat

- El **plan de edición** va completo: es lo que el user lee y aprueba.
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
  user lo complete. Si falta material, se frenó en Intake.
- ❌ No pises un archivo existente. **Versioná.**
- ❌ No te olvides de decir la ruta.
- ❌ No prometas un formato, un códec o un flag que no esté verificado en
  `reference/hyperframes.md`.
