# 07 — Output format y cierre

El entregable se **muestra en el chat Y queda en el creativo**: la
composición en `composition/` (con su `PLAN.md`), el render en `renders/`, y
el manifiesto cerrado. No es opcional.

Formato exacto en `templates/output_template.md`.

---

## Qué contiene el entregable

En este orden, sin excepción:

1. **Línea de contexto del editor** — una sola frase: qué pieza es, para qué
   plataforma, de cuánto.
2. **El plan de edición por segundos** — la tabla de `templates/edit_plan.md`
   (la misma que guardaste en `composition/PLAN.md`).
3. **La composición** — el `index.html` completo la primera vez; en
   iteraciones, solo el diff.
4. **El render** — en `full_render`, qué `vN` quedó activo (`renders/vN.mp4`,
   duración, tamaño, calidad); en `plan_only`, los comandos y qué falta.
5. **El cierre del manifiesto** — una línea: estado en que quedó.

**No** hay preámbulo ("¡Acá tenés!") ni cierre de despedida ("Espero que te
sirva"). Cerrás con la línea de ajustes (ver abajo).

---

## Dónde queda todo — el creativo

```
creatives/<brief>/<grupo>/<id>/
  <id>.indash              video.active = "vN" (lo movió render_video), status review
  composition/
    PLAN.md                el plan de edición completo (la pieza es reproducible sin el chat)
    index.html             la composición
    assets/                clips, stills, packshot, música, fuentes, logo — COPIADOS, rutas relativas
    snapshots/             scratch de `check --snapshots` (no se referencia)
  renders/
    v1.mp4  v2.mp4 …       append-only; los escribió render_video, nunca vos
```

- **Todos** los assets copiados a `assets/`, rutas relativas. El creativo tiene
  que renderizar igual dentro de un año, aunque el Workbench se haya
  reordenado.
- **Nunca** escribas `renders/` a mano ni un mp4 en `composition/`. Si
  necesitás un render, es `render_video`.
- El Workbench queda como estaba: es del humano. Si generaste algo nuevo
  durante el montaje (un still de tapa, un recorte), dejalo también ahí para
  que lo encuentre.

### El cierre del manifiesto (último paso, siempre)

`render_video` ya dejó `video.active` apuntando al render vigente. Vos cerrás
el estado, **después** del último render:

- `meta.status: "review"` (el humano aprueba desde la app),
- `meta.generating: false`, `meta.updatedAt`,
- `video.seconds` = el `data-duration` real, si cambió respecto del plan,
- una línea en `history.jsonl`:
  `{"at":"…","event":"status-changed","from":"draft","to":"review","by":"agent"}`.

Escribilo con 2 espacios de indent y newline final, y sin tocar nada más del
manifiesto. En `plan_only` no cerrás nada: queda en `draft`.

### Cuando el mismo corte sale en varios formatos

Cada formato es **su propio creativo** del plan (el grupo del otro formato).
Copiá `composition/` a esa carpeta, cambiá root / viewport / caja `#root` /
variables de zona segura (y las `object-position` que hagan falta), y corré
ahí su pase de gates + `render_video`. Un solo plan de edición (el corte es el
mismo) + deltas por formato en cada `PLAN.md`.

---

## Cómo se muestra en el chat

- El **plan de edición** va completo: es lo que el humano lee y aprueba.
- La **composición** va completa en bloque de código la primera vez. En las
  iteraciones posteriores, mostrá **solo el diff** (qué atributo cambió en qué
  clip) — pegar 200 líneas de HTML por cada ajuste de 0.3s no ayuda a nadie.
- En `full_render`, el render activo va en su propia línea, destacado. La
  tarjeta del board ya lo reproduce; `mcp__indash__show_media` si querés
  ponerlo en el chat.

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
- ❌ No escribas `renders/` ni `video.active` a mano.
- ❌ No dejes el manifiesto en `generating: true`.
- ❌ No prometas un formato, un códec o un flag que no esté verificado en
  `reference/hyperframes.md`.
