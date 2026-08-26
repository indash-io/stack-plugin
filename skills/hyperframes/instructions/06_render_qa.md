# 06 — Render y QA

**El render final es user-gated por diseño.** La doc de HyperFrames lo dice
explícito: el agente frena en preview y renderiza cuando la persona aprueba. No
te saltees ese freno para "ahorrar una vuelta".

---

## La escalera de gates (en este orden, siempre)

```
lint  →  check  →  preview / draft  →  [APROBACIÓN DEL USER]  →  high
barato   browser    ojo humano           el freno               caro
```

Cada gate atrapa una clase distinta de error. Saltearse uno significa
descubrirlo en el gate siguiente, que es más caro.

---

## 1. `lint` — el gate estático (segundos)

```bash
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

- **`--snapshots`** guarda los frames auditados + un recorte PNG por hallazgo.
  **Miralos.** Son la forma más barata de ver si un caption quedó tapado o si un
  clip entró recortado mal.
- **`--at`** con los timecodes clave del plan de edición: el frame del hook, el
  medio de cada corte, el CTA. Vale más que la grilla automática.
- **`--at-transitions`** para cazar solapamientos transitorios en los seams — el
  error clásico de dos escenas visibles a la vez donde no corresponde.
- El chequeo de contraste es tu aliado para los captions: si tira contraste
  bajo, el texto no se lee sobre ese fondo. Metele un scrim (ver
  `style/captions_typography.md`), no subas el tamaño.

**No** pases `--no-contrast` para "que pase". El contraste es exactamente lo que
hace que un caption exista.

---

## 3. Draft — el gate del ojo humano

```bash
npx hyperframes render --quality draft --output renders/<slug>_draft.mp4
```

En `full_render` esto lo corrés vos. Después:

- **Mirá el archivo.** Los frames de `check` no muestran ritmo; el draft sí.
- Contra qué lo mirás: `eval/quality_checklist.md`, sección "Sobre el render".

Alternativa para iterar rápido sin renderizar:

```bash
npx hyperframes preview           # live reload; en shell de agente arranca en background
npx hyperframes preview --status --json
```

En una shell no interactiva `preview` arranca un servidor manejado en background
y el resultado trae la URL del proyecto en Studio. Pasásela al user: mirar el
preview y scrubear la timeline es más rápido que cualquier render.

---

## 4. El freno: aprobación del user

**Mostrale el draft y pedí el OK explícito.** Una línea, sin ceremonia:

> Ahí está el draft (`renders/<slug>_draft.mp4`). Miralo y decime si va — si
> está bien lo saco en `high`, que es el que tarda.

Si el user pide cambios → volvés a `instructions/04_edit_concept.md` o a
`instructions/05_composition.md` según qué falle, y aplicás **un cambio por
render** con **objetivos absolutos**.

---

## 5. Final

```bash
npx hyperframes render --quality high --output renders/<slug>_v1.mp4
```

`high` se paga **una sola vez**, sobre el corte ya aprobado. La doc es explícita
en que `standard` (el default) ya es visualmente lossless en 1080p: reservá
`high` para el master que se entrega.

Si el user pidió un segundo formato, ahí sale la **segunda composición** (no un
flag), con su propio pase de gates.

---

## 6. Iteración: las dos reglas

Salen de la doc de edición de HyperFrames y no son negociables:

1. **Un cambio por render.** Si cambiás tres cosas y mejora, no sabés cuál fue.
2. **Objetivos absolutos.** *"La escena 2 dura 2.0s"* ✅ · *"acortá un toque la
   escena 2"* ❌ — lo segundo invita a que el agente oscile y no cierre nunca.

Y una tercera del oficio: **congelá lo que ya está bien.** Cuando pidas un
cambio de estilo, agregá la cláusula de freeze: *"el encuadre y el timing están
bien, no los toques"*. Sin eso, un restyle puede disparar una reconstrucción que
deriva en ejes que ya estaban aprobados.

### Mapa verbo → atributo (para editar rápido)

| Lo que pide el user | Qué tocás |
|---|---|
| "que la escena 2 arranque más tarde" | `data-start` |
| "que el logo termine antes" | `data-duration` |
| "saltate el primer segundo del clip" | `data-media-start` |
| "que la escena 2 dure 2 segundos" | `data-duration` (+ el largo de la tween si el motion tiene que estirarse) |
| "la música está muy fuerte" | `data-volume` |
| "los captions están detrás del video" | `z-index` (no `data-track-index`) |
| "partí la escena 2 en dos" | un clip pasa a ser dos, con `data-start` / `data-duration` ajustados |

Si retimás una escena que abarca toda la composición, **subí también el
`data-duration` del root**: el root manda la duración total y un hijo más largo
no renderiza más allá.

---

## 7. Cuando el render falla

| Síntoma | Causa probable | Qué mirar |
|---|---|---|
| El render corta antes de lo esperado | `data-duration` del root corto | El root manda, no el timeline de GSAP |
| Una escena se congela en su último frame | `data-duration` del clip > duración real del archivo | La tabla de Discovery (`ffprobe`) |
| Imagen recortada pero audio entero | `data-playback-start` en un `<video>` | Cambialo a `data-media-start` |
| La mezcla de audio falla entera | Cadena `data-fx-chain` ilegible | El JSON escapado con `&quot;`; el preview la toca seca y el render falla |
| Un caption no se ve | `z-index` o zona segura | `check --snapshots` |
| El texto sale con otra fuente | `@font-face` no resolvió a tiempo | `font-display: block` + fuente copiada al proyecto |
| Timeout de página | Muchos videos/fuentes/assets | `--browser-timeout` (en segundos) |
| El render tarda muchísimo | 4K / 60fps pedidos de más | Sacalos si el destino no los resuelve |

Ante cualquier duda de entorno: `npx hyperframes doctor`.

---

## En modo `plan_only`

No corrés nada. Entregás la escalera completa como bloque de comandos, en orden,
con **qué mirar en cada gate**:

```bash
cd exports/videos/2026-08-25_<slug>_v1

npx hyperframes lint            # errores (✗) → arreglar antes de seguir
npx hyperframes check --snapshots   # mirá snapshots/: captions legibles, nada cortado
npx hyperframes render --quality draft --output renders/<slug>_draft.mp4
# ↑ mirá el draft: ¿el primer segundo frena el scroll? ¿el ritmo respira?
npx hyperframes render --quality high --output renders/<slug>_v1.mp4
```

Y agregá el recordatorio de requisitos: **Node 22+ y FFmpeg**.

→ Pasá a `instructions/07_output_format.md`.
