# Template — Output

Formato exacto del entregable, tal como se muestra en el chat. Lo que queda
en disco es el creativo: `composition/` (con `PLAN.md`) + `renders/vN.mp4` +
el manifiesto cerrado.

Reglas de cierre: `instructions/07_output_format.md`.

---

```markdown
# [Nombre de la pieza] — [Formato] · [Duración]s

[Una sola frase de contexto de editor: qué es la pieza, para qué plataforma y
cuál es el ángulo del corte. Sin adjetivos de relleno.]

---

## Plan de edición

[La tabla completa de `templates/edit_plan.md`: cortes, seams, curva de audio,
movimiento interno, zona segura, material que queda afuera.]

---

## Composición

`creatives/<brief>/<grupo>/<id>/composition/`

```
composition/
  PLAN.md
  index.html
  assets/    clip-01-v2.mp4 · clip-02-v1.mp4 · packshot.webp · musica.mp3 · Marca-Bold.ttf · logo.svg
```

<details>
<summary><code>index.html</code></summary>

​```html
[la composición completa]
​```

</details>

---

## Render

[**Modo `full_render`**]
`renders/v2.mp4` (activo) — [duración]s · [ancho×alto] · [tamaño] · `high`
(v1 fue el draft aprobado; queda en `renders/`, el puntero puede volver)

[**Modo `plan_only`**]
Falta [Node 22+ / FFmpeg] para renderizar acá. La composición está completa;
cuando esté instalado:

​```bash
cd creatives/<brief>/<grupo>/<id>/composition
npx hyperframes lint
npx hyperframes check --snapshots --at [timecodes clave del plan]
# desde el chat: render_video draft → view_creative → render_video high
​```

---

## Manifiesto

`status: review` · `video.active: v2` · `video.seconds: [N]`
[o, en `plan_only`: queda en `draft`, sin render]

---

## Notas

- [Cualquier cosa que el humano tenga que saber: material que quedó afuera y
  por qué, un claim que no se pudo verificar, un asset que conviene regenerar,
  qué versión de cada clip entró.]
- [Si algo de HyperFrames quedó como "verificar", decilo acá explícitamente.]

Si querés ajustar un corte, cambiar el hook, mover un caption o sacarlo en otro
formato, decime cuál y lo cambio.
```

---

## Variante: el mismo corte en dos formatos

Son dos creativos. En la sección **Composición** una entrada por creativo:

```markdown
## Composición

- `creatives/<brief>/stories/<id>/composition/` → `renders/v2.mp4` (9:16, activo)
- `creatives/<brief>/feed/<id>-1x1/composition/` → `renders/v1.mp4` (1:1, activo)

### Deltas entre formatos

| Elemento | 9:16 | 1:1 |
|---|---|---|
| ... | ... | ... |
```

Y en **Render**, una línea por creativo. Cada uno pasó su propio `lint` /
`check` / `render_video`.

---

## Variante: iteración sobre una versión anterior

En una segunda vuelta **no** pegues el HTML entero de nuevo. Mostrá el diff:

```markdown
# [Nombre] — v3

Cambio pedido: el corte 2 pasa de 3.0s a 2.4s (queda más ágil el desarrollo).

## Diff

| Elemento | v2 | v3 |
|---|---|---|
| `#shot-02` `data-duration` | 3 | 2.4 |
| `#shot-03` `data-start` | 5 | 4.4 |
| `#shot-04` `data-start` | 7.5 | 6.9 |
| `#cta-frame` `data-start` | 9.8 | 9.2 |
| `#root` `data-duration` | 12 | 11.4 |
| `#music-*` tramos | — | recortados en 0.6s |

Todo lo demás queda igual: encuadres, captions, transiciones y audio no se
tocaron.

[Plan de edición actualizado]

## Render

`renders/v3.mp4` (activo, draft) — 11.4s · 1080×1920. `video.seconds` → 11.4.
```

Un cambio por vuelta, objetivos absolutos, y la cláusula de freeze explícita.

---

## Prohibiciones de formato

- ❌ Preámbulo ("¡Acá tenés!", "¡Genial!").
- ❌ Cierre de despedida ("Espero que te sirva", "Cualquier cosa avisame").
- ❌ Emojis.
- ❌ Composición sin plan de edición, o plan sin composición.
- ❌ HTML con placeholders para que el humano complete.
- ❌ Afirmar un flag, un códec o un atributo que no esté en
  `reference/hyperframes.md`.
- ❌ Olvidarse de decir qué render quedó activo y en qué estado el manifiesto.
