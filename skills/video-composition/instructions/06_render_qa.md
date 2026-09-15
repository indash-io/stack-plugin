# 06 — Render y QA

**El render final es user-gated por diseño.** La doc de HyperFrames lo dice
explícito: el agente frena en el draft y renderiza el final cuando la persona
aprueba. No te saltees ese freno para "ahorrar una vuelta".

El render **no lo corrés vos con `npx hyperframes render`**: lo corre la app
con `mcp__indash__render_video`, que es la única que escribe
`renders/vN.mp4` (append-only) y mueve `video.active` del manifiesto. Lo que
sí corrés vos, dentro de `composition/`: `lint` y `check`.

---

## La escalera de gates (en este orden, siempre)

```
lint  →  check  →  render_video draft  →  view_creative  →  [APROBACIÓN DEL HUMANO]  →  render_video high
barato   browser    la tool               tu ojo              el freno                     caro
```

Cada gate atrapa una clase distinta de error. Saltearse uno significa
descubrirlo en el gate siguiente, que es más caro.

---

## 1. `lint` — el gate estático (segundos)

```bash
cd creatives/<brief>/<grupo>/<id>/composition
npx hyperframes lint
npx hyperframes lint --json     # si querés parsearlo
```

Lee el HTML y reporta errores comunes sin abrir browser. Los errores (`✗`) hay
que arreglarlos antes de renderizar; los warnings (`⚠`) son problemas probables.
`--verbose` agrega los info.

Errores típicos que atrapa:
- `missing_gsap_script` — la composición usa GSAP y el script no está cargado.
- `unmuted-video` — un `<video>` sin `muted` (autoplay poco confiable).
- atributos de timing inválidos o faltantes.

**Si `lint` da error, no sigas.** `check` ni siquiera abre el browser cuando hay
un error de lint.

---

## 2. `check` — el gate de browser (decenas de segundos)

```bash
npx hyperframes check --snapshots
npx hyperframes check --at 0.5,2,5,9,11.5 --snapshots
npx hyperframes check --at-transitions
```

Carga la composición una vez y barre una grilla de seeks auditando en cada
muestra: errores de runtime y requests fallidos, defectos de layout (overflow,
clipping, oclusión, overlaps sostenidos), aserciones de motion y **contraste
WCAG AA**.

Cómo usarlo bien en esta skill:

- **`--snapshots`** guarda los frames auditados en `composition/snapshots/`.
  **Miralos** (Read). Son la forma más barata de ver si un caption quedó tapado
  o si un clip entró recortado mal. Esa carpeta es scratch tuyo: no hace falta
  borrarla, pero no la referencies desde el HTML.
- **`--at`** con los timecodes clave del plan de edición: el frame del hook, el
  medio de cada corte, el CTA. Vale más que la grilla automática. Es también
  la forma de mirar **un instante puntual** después de un render.
- **`--at-transitions`** para cazar solapamientos transitorios en los seams — el
  error clásico de dos escenas visibles a la vez donde no corresponde.
- El chequeo de contraste es tu aliado para los captions: si tira contraste
  bajo, el texto no se lee sobre ese fondo. Metele un scrim (ver
  `style/captions_typography.md`), no subas el tamaño.

**No** pases `--no-contrast` para "que pase". El contraste es exactamente lo que
hace que un caption exista.

---

## 3. Draft — el gate del ojo (el tuyo primero)

```
mcp__indash__render_video { creative: "creatives/<brief>/<grupo>/<id>", quality: "draft" }
```

La tool corre `npx hyperframes render` sobre `composition/`, escribe el
próximo `renders/vN.mp4` y (default `set_active: true`) mueve `video.active`
del manifiesto. Te devuelve `{ render: "vN", path, bytes, seconds, quality }`.
Si falta FFmpeg o Node 22, te lo dice: pasás a `plan_only` (abajo).

Después, **miralo vos**:

```
mcp__indash__view_creative { creative: "creatives/<brief>/<grupo>/<id>" }
```

Devuelve la **hoja de contactos**: 8 frames equiespaciados del render activo
en grilla 4×2 (cada uno con su timecode; si tu FFmpeg no tiene `drawtext`, los
tiempos vienen en el bloque de texto, en orden izquierda→derecha,
arriba→abajo) + `seconds`, `fps`, tamaño, `hasAudio` y la lista de `renders`.
Contra qué lo mirás: `eval/quality_checklist.md`, sección "Sobre el render".

- **La duración medida tiene que ser la del plan.** Si `seconds` no coincide
  con `data-duration`, algo cortó antes (el root manda).
- `hasAudio: false` con clips de voz o música declarada = un `muted` de más o
  un `data-has-audio` de menos.
- Para un instante exacto que la hoja no muestra: `check --at <s> --snapshots`.

Un render `draft` es un `vN` como cualquier otro: si el humano lo prefiere
sobre un `high` posterior, el puntero vuelve. Nunca se pierde nada.

---

## 4. El freno: aprobación del humano

**Mostrale el draft y pedí el OK explícito.** Una línea, sin ceremonia: el
board ya reproduce el render activo en la tarjeta del creativo, y con
`mcp__indash__show_media` podés ponerlo en el chat.

> Ahí está el draft (`renders/v1.mp4`, ya se ve en la tarjeta). Miralo y decime
> si va — si está bien lo saco en `high`, que es el que tarda.

Si el humano pide cambios → volvés a `instructions/04_edit_concept.md` o a
`instructions/05_composition.md` según qué falle, y aplicás **un cambio por
render** con **objetivos absolutos**. Cada vuelta es otro `render_video draft`
→ otro `vN`.

---

## 5. Final

```
mcp__indash__render_video { creative: "creatives/<brief>/<grupo>/<id>", quality: "high" }
```

`high` se paga **una sola vez**, sobre el corte ya aprobado. La doc es explícita
en que `standard` ya es visualmente lossless en 1080p: reservá `high` para el
master que se entrega. Miralo una vez más con `view_creative` (la duración, el
audio) y cerrá el manifiesto (paso 07).

Si el humano pidió un segundo formato, ese es **otro creativo** del plan: copiás
`composition/` a su carpeta, ajustás root/viewport/zona segura, y corrés su
propio pase de gates y su propio `render_video`.

---

## 6. Iteración: las dos reglas

Salen de la doc de edición de HyperFrames y no son negociables:

1. **Un cambio por render.** Si cambiás tres cosas y mejora, no sabés cuál fue.
2. **Objetivos absolutos.** *"La escena 2 dura 2.0s"* ✅ · *"acortá un toque la
   escena 2"* ❌ — lo segundo invita a oscilar y no cerrar nunca.

Y una tercera del oficio: **congelá lo que ya está bien.** Cuando el humano
pida un cambio de estilo, repetile la cláusula de freeze: *"el encuadre y el
timing están bien, no los toco"*. Sin eso, un restyle puede disparar una
reconstrucción que deriva en ejes que ya estaban aprobados.

### Mapa verbo → atributo (para editar rápido)

| Lo que pide el humano | Qué tocás |
|---|---|
| "que la escena 2 arranque más tarde" | `data-start` |
| "que el logo termine antes" | `data-duration` |
| "saltate el primer segundo del clip" | `data-media-start` |
| "que la escena 2 dure 2 segundos" | `data-duration` (+ el largo de la tween si el motion tiene que estirarse) |
| "la música está muy fuerte" | `data-volume` |
| "los captions están detrás del video" | `z-index` (no `data-track-index`) |
| "partí la escena 2 en dos" | un clip pasa a ser dos, con `data-start` / `data-duration` ajustados |
| "cambiame el precio del segundo 3" | el texto del bloque — ES la razón de que el fuente sea la composición |

Si retimás una escena que abarca toda la composición, **subí también el
`data-duration` del root** (y `video.seconds` en el manifiesto): el root manda
la duración total y un hijo más largo no renderiza más allá.

---

## 7. Cuando el render falla

`render_video` te devuelve la cola del log de hyperframes en el error.

| Síntoma | Causa probable | Qué mirar |
|---|---|---|
| El render corta antes de lo esperado | `data-duration` del root corto | El root manda, no el timeline de GSAP |
| Una escena se congela en su último frame | `data-duration` del clip > duración real del archivo | La tabla de Discovery (`ffprobe`) |
| Imagen recortada pero audio entero | `data-playback-start` en un `<video>` | Cambialo a `data-media-start` |
| La mezcla de audio falla entera | Cadena `data-fx-chain` ilegible | El JSON escapado con `&quot;`; el preview la toca seca y el render falla |
| Un caption no se ve | `z-index` o zona segura | `check --snapshots` |
| El texto sale con otra fuente | `@font-face` no resolvió a tiempo | `font-display: block` + fuente copiada a `assets/` |
| "Falta composition/index.html" | Composición en otra carpeta | Tiene que ser `creatives/<brief>/<grupo>/<id>/composition/index.html` |
| "está approved (congelado)" | El creativo ya se aprobó | El humano lo des-aprueba desde la app, o es otro creativo |
| Falta FFmpeg / Node 22 | Entorno | `plan_only` (abajo) — y decile al humano qué instalar |
| Timeout (10 min) | Composición pesadísima o Chrome colgado | `npx hyperframes doctor`; menos workers; revisá assets gigantes |

Ante cualquier duda de entorno: `npx hyperframes doctor`.

---

## En modo `plan_only`

No renderizás. La composición queda completa en `composition/` (eso sí lo
escribís) y entregás la escalera como bloque de comandos, en orden, con **qué
mirar en cada gate**, para cuando el entorno esté:

```bash
cd creatives/<brief>/<grupo>/<id>/composition
npx hyperframes lint                # errores (✗) → arreglar antes de seguir
npx hyperframes check --snapshots   # mirá snapshots/: captions legibles, nada cortado
# después, desde el chat del Studio:
#   mcp__indash__render_video { creative: "creatives/<brief>/<grupo>/<id>", quality: "draft" }
#   mcp__indash__view_creative { creative: "creatives/<brief>/<grupo>/<id>" }
#   mcp__indash__render_video { creative: "...", quality: "high" }   ← cuando el draft esté aprobado
```

Y agregá el recordatorio de requisitos: **Node 22+ y FFmpeg** (macOS:
`brew install ffmpeg`). El manifiesto queda en `draft` con `video.active`
como estaba: sin render no hay commit.

→ Pasá a `instructions/07_output_format.md`.
