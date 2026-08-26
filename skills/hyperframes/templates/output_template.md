# Template — Output

Formato exacto del entregable, tal como se muestra en el chat **y** como se
guarda en `exports/videos/<AAAA-MM-DD>_<concepto-slug>_v<N>.md`.

Reglas de guardado: `instructions/07_output_format.md`.

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

Proyecto: `exports/videos/<AAAA-MM-DD>_<slug>_v<N>/`

```
<slug>_v<N>/
  index.html
  assets/    shot-01.mp4 · shot-02.mp4 · packshot.png · music.mp3 · vo.wav · Marca-Bold.woff2
  renders/   <slug>_draft.mp4 · <slug>_v<N>.mp4
```

<details>
<summary><code>index.html</code></summary>

​```html
[la composición completa]
​```

</details>

---

## Render

​```bash
cd exports/videos/<AAAA-MM-DD>_<slug>_v<N>

npx hyperframes lint
npx hyperframes check --snapshots --at [timecodes clave del plan]
npx hyperframes render --quality draft --output renders/<slug>_draft.mp4
# ↑ mirá el draft; cuando esté aprobado:
npx hyperframes render --quality high --output renders/<slug>_v<N>.mp4
​```

Requisitos: **Node.js 22+** y **FFmpeg**. Defaults del render: MP4, 30 fps,
tamaño de la composición.

---

## Resultado

[**Modo `full_render`**]
`exports/videos/<AAAA-MM-DD>_<slug>_v<N>/renders/<slug>_v<N>.mp4` — [duración]s ·
[ancho×alto] · [tamaño del archivo]

[**Modo `plan_only`**]
Falta [Node 22+ / FFmpeg] para renderizar acá. El proyecto está completo: corré
los comandos de arriba y sale el MP4.

---

## Notas

- [Cualquier cosa que el user tenga que saber: material que quedó afuera y por
  qué, un claim que no se pudo verificar, un asset que conviene regenerar.]
- [Si algo de HyperFrames quedó como "verificar", decilo acá explícitamente.]

Guardado en `exports/videos/<AAAA-MM-DD>_<slug>_v<N>.md`.

Si querés ajustar un corte, cambiar el hook, mover un caption o sacarlo en otro
formato, decime cuál y lo cambio.
```

---

## Variante: entrega en dos formatos

Un solo plan de edición, y en la sección **Composición** una entrada por
formato:

```markdown
## Composición

Proyecto: `exports/videos/<AAAA-MM-DD>_<slug>_v<N>/`

```
<slug>_v<N>/
  9x16/index.html    renders/<slug>_9x16_v<N>.mp4
  4x5/index.html     renders/<slug>_4x5_v<N>.mp4
  assets/            (compartida)
```

### Deltas entre formatos

| Elemento | 9:16 | 4:5 |
|---|---|---|
| ... | ... | ... |
```

Y en **Render**, la escalera de gates corre **por composición** (con `-c` o
entrando a cada subcarpeta).

---

## Variante: iteración sobre una versión anterior

En una segunda vuelta **no** pegues el HTML entero de nuevo. Mostrá el diff:

```markdown
# [Nombre] — v2

Cambio pedido: el corte 2 pasa de 3.0s a 2.4s (queda más ágil el desarrollo).

## Diff

| Elemento | v1 | v2 |
|---|---|---|
| `#shot-02` `data-duration` | 3 | 2.4 |
| `#shot-03` `data-start` | 5 | 4.4 |
| `#shot-04` `data-start` | 7.5 | 6.9 |
| `#cta-frame` `data-start` | 9.8 | 9.2 |
| `#root` `data-duration` | 12 | 11.4 |
| `#music-*` tramos | — | recortados en 0.6s |

Todo lo demás queda igual: encuadres, captions, transiciones y audio no se
tocaron.

[Plan de edición actualizado + comando de render]

Guardado en `exports/videos/<AAAA-MM-DD>_<slug>_v2.md`.
```

Un cambio por vuelta, objetivos absolutos, y la cláusula de freeze explícita.

---

## Prohibiciones de formato

- ❌ Preámbulo ("¡Acá tenés!", "¡Genial!").
- ❌ Cierre de despedida ("Espero que te sirva", "Cualquier cosa avisame").
- ❌ Emojis.
- ❌ Composición sin plan de edición, o plan sin composición.
- ❌ HTML con placeholders para que el user complete.
- ❌ Afirmar un flag, un códec o un atributo que no esté en
  `reference/hyperframes.md`.
- ❌ Olvidarse de decir la ruta de guardado.
