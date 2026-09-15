# Reference — HyperFrames (verificado en fuentes primarias)

> **Fecha de verificación: 2026-08-25.** Todo lo de la sección "Confirmado" sale
> de las fuentes primarias listadas abajo (README del repo oficial y archivos
> `.mdx` de la documentación, leídos desde `raw.githubusercontent.com` en la rama
> `main`). Lo de "Inferido" es lectura nuestra, no cita. Lo de "Verificar" **no
> está en las fuentes**: no lo afirmes al user, decile que hay que chequearlo.
>
> HyperFrames se mueve rápido (la CLI iba en `0.8.x` a esta fecha; el 2026-09-09
> se re-verificaron `render --help` y `check --help` contra `0.8.33`). Si algo de
> acá no matchea con lo que devuelve la máquina, **gana la máquina**:
> `npx hyperframes <comando> --help` y `npx hyperframes doctor` son la fuente
> de verdad del entorno.
>
> **En el Studio el render lo corre la app** (`mcp__indash__render_video`, un
> cascarón sobre `npx hyperframes render`): lo de `render` está acá para que
> entiendas qué hace la tool, no para que lo corras vos. Lo que sí corrés vos,
> dentro de `composition/`: `lint`, `check`, `transcribe`, `beats`, `add`,
> `media-treatment`, `doctor`. Curado para el Studio: sin editor, sin cloud,
> sin TTS.

## Fuentes primarias

| Qué | Link |
|---|---|
| Repo oficial (código + README) | https://github.com/heygen-com/hyperframes |
| Documentación | https://hyperframes.heygen.com/introduction |
| Quickstart | https://hyperframes.heygen.com/quickstart |
| Contrato HTML (schema de composición) | https://hyperframes.heygen.com/reference/html-schema |
| Atributos de timing | https://hyperframes.heygen.com/concepts/data-attributes |
| Referencia de la CLI | https://hyperframes.heygen.com/packages/cli |
| Render y output | https://hyperframes.heygen.com/prompting/rendering-and-output |
| Editar videos existentes | https://hyperframes.heygen.com/prompting/editing-existing-videos |
| Transiciones (catálogo) | https://hyperframes.heygen.com/prompting/transitions |
| Captions / talking head | https://hyperframes.heygen.com/prompting/captions-and-talking-heads |
| Efectos de audio | https://hyperframes.heygen.com/reference/audio-effects |
| Paquete npm | https://www.npmjs.com/package/hyperframes |
| Playground de la comunidad | https://www.hyperframes.dev/ |

**Desambiguación.** Hay varios proyectos que se llaman parecido. El que usa esta
skill es **`heygen-com/hyperframes`**: el framework open source de HeyGen para
convertir HTML/CSS + media + animaciones seekables en video determinístico, con
CLI y skills para agentes. No es un producto de hardware, ni un plugin de NLE,
ni el sitio `hyperframes.dev` (ese es el playground de la comunidad del **mismo**
proyecto, no otro).

---

## 1. Confirmado en la documentación

### 1.1 Qué es

> "HyperFrames is an open-source framework for turning HTML, CSS, media, and
> seekable animations into deterministic MP4 videos. Use it locally with the
> CLI, from AI coding agents with skills, or as the rendering core behind hosted
> authoring workflows." — README, `main`.

Tagline: *"Write HTML. Render video. Built for agents."*

- **Licencia**: Apache 2.0.
- **Requisitos**: Node.js **22+** y **FFmpeg**. El render corre Chrome headless
  (Puppeteer) y encodea con FFmpeg.
- **Determinismo**: el renderer *busca* (seek) cada frame en Chrome headless y
  encodea con FFmpeg → mismo input, mismos frames, mismo output.
- **Sin build step**: un `index.html` de composición se abre y se reproduce como
  está.
- **Comparación explícita con Remotion** (está en el README): mismo motor
  conceptual (Chrome headless + FFmpeg), distinto modelo de autoría — Remotion
  apuesta a componentes React, HyperFrames a HTML plano.

### 1.2 Instalación y CLI

```bash
npx hyperframes init my-video      # scaffold del proyecto
npx hyperframes preview            # preview en browser con live reload
npx hyperframes render             # render a MP4
```

Comandos documentados (referencia de la CLI) que usa esta skill: `add`,
`catalog`, `transcribe`, `media-treatment`, `beats`, `preview`, `lint`,
`check`, `render` (vía la tool), `doctor`. Existen además `init`, `capture`,
`tts`, `remove-background`, `snapshot`, `publish`, `cloud render` y `lambda`
— fuera del proceso del Studio: no scaffoldeamos proyectos aparte (la
composición vive en el creativo), no sintetizamos voz, no renderizamos en la
nube.

Convenciones transversales de la CLI: casi todo acepta `--json` (pensado para
agentes), `--dir` elige el directorio del proyecto, y `--non-interactive` /
`--yes` evitan cualquier prompt.

**`render` — lo que hace la tool** (`hyperframes render [OPTIONS] [DIR]`,
verificado en `0.8.33`; `DIR` = la carpeta del proyecto, o sea
`composition/`):

| Flag | Default | Qué hace |
|---|---|---|
| `--output, -o` | `renders/<name>.mp4` **relativo a DIR** | Path del archivo de salida. La tool pasa uno explícito (temporal) y después lo mueve a `renders/vN.mp4` del creativo, así `composition/renders/` nunca aparece |
| `--composition, -c` | `index.html` | Renderizar otra composición del proyecto |
| `--format` | `mp4` | `mp4`, `webm`, `mov`, `gif`, `png-sequence`. La tool siempre pide MP4 |
| `--fps, -f` | `data-fps` del root, si no 30 | 1–240, o racional de ffmpeg (`30000/1001`) — **`data-fps` en el root SÍ existe** (lo dice `render --help` de 0.8.33) |
| `--quality, -q` | `standard` | `draft`, `standard`, `high`. Maneja CRF y bitrate. Es el `quality` de la tool |
| `--resolution` | tamaño de la composición | Supersample vía `deviceScaleFactor`. No reencuadra. La tool no lo usa |
| `--browser-timeout` | 60 s | Timeout de navegación de la página de entrada; para composiciones pesadísimas |
| `--strict` / `--strict-all` | off | Fallar ante errores de lint (o errores + warnings) |

**`preview`**: `--port` (default 3002), `--background`, `--foreground`, `--json`,
`--status`, `--list`, `--stop`, `--kill-all`. En una shell no interactiva o de
agente, `preview` a secas arranca un preview **manejado en background** y el
resultado incluye la URL exacta del proyecto en Studio.

**`lint` vs `check`:**
- `lint` lee el HTML y reporta errores estáticos (atributos inválidos, librería
  de animación faltante, `<video>` sin `muted`…). No abre browser: es rápido.
  Errores (`✗`) hay que arreglarlos antes de renderizar.
- `check` es el **gate de browser**: corre el linter primero, después carga la
  composición una vez y barre una grilla de seeks auditando errores de runtime,
  defectos de layout (overflow, clipping, oclusión), aserciones de motion y
  contraste WCAG AA. Flags útiles: `--json`, `--snapshots`, `--at 1.5,4,7.25`,
  `--at-transitions`, `--strict`.

Otros comandos que esta skill usa seguido (siempre con cwd = `composition/`):
- `npx hyperframes add <block>` — instala un bloque/componente del catálogo
  (por ejemplo `flash-through-white`, `instagram-follow`, `data-chart`).
- `npx hyperframes transcribe video.mp4 [--model medium.en] [--language es] [--to srt|vtt]`
  — transcripción local (motor `auto` → Parakeet si está, si no Whisper). Es
  lo único de audio que generás: **no hay TTS en el Studio**.
- `npx hyperframes media-treatment --capabilities --json` — superficie vigente
  de color grading y efectos, legible por máquina. **Usalo en vez de hardcodear
  una lista de efectos.**
- `npx hyperframes doctor` — diagnóstico del entorno.

### 1.3 Contrato de composición (los `data-*` que importan)

Una composición es **HTML normal**. El timing vive en atributos, no en JS.

**Root de la composición:**

| Atributo | Requerido | Significa |
|---|---|---|
| `data-composition-id` | Sí | ID único; tiene que coincidir con la key del registro de timelines |
| `data-start="0"` | Sí en el root top-level | Inicio de la composición |
| `data-width` / `data-height` | Sí | Dimensiones del frame autorado, en píxeles |
| `data-duration` | Casi siempre | Duración total del render, en segundos |
| `data-no-timeline` | Solo si no hay timeline | Le dice al runtime que no espere una |

**La duración del render sale del `data-duration` del root**, no del largo del
timeline de GSAP. El compilador lo lee antes de que corran los scripts: un
script no puede cambiarlo para ese render.

**Clips con timing:**

| Atributo | Requerido | Significa |
|---|---|---|
| `id` | Sí | Identificador estable para timing, edición y animación |
| `data-start` | Sí | Inicio en segundos, o expresión relativa |
| `data-duration` | Sí para clips DOM, imagen y composición anidada | Largo del slot visible |
| `data-track-index` | No | **Solo display**: es la fila que dibuja Studio. El render no lo lee y no impide overlap. |
| `class="clip"` | Recomendado | Convención de layout: la regla `.clip` compartida da la caja full-frame. La visibilidad se calcula por `data-start`, no por la clase. |

> **Track ≠ capa.** El orden de pintado se controla con `z-index` de CSS, nunca
> con `data-track-index`.

**Timing relativo:** un `data-start` no numérico refiere al *fin* de otro clip de
la misma composición. Formas soportadas: `clip-id`, `clip-id + 0.5`,
`clip-id - 0.5`. No cruza composiciones, el clip referido tiene que tener
duración conocida, y no puede haber ciclos.

**Media (`<video>` / `<audio>`):**

| Atributo | Significa |
|---|---|
| `data-media-start` | Offset dentro del archivo fuente (lo que un NLE llama trim de entrada). **Es el nombre canónico para `<video>` y `<audio>`** — el mixer de audio lee *solo* este. |
| `data-playback-start` | Mismo concepto, pero es el nombre canónico para el **host de una composición anidada**. |
| `data-playback-rate` | Multiplicador de velocidad, de `0.1` a `5` |
| `data-volume` | Ganancia estática. `1` = 0 dB, `0` = silencio, arriba de `1` amplifica hasta `3.98` (+12 dB) |
| `data-has-audio="true"` | En un `<video>`: declara que ese video aporta audio |

> **Trampa documentada:** un `<video>` autorado solo con `data-playback-start`
> renderiza **imagen recortada sobre audio sin recortar**, porque el mixer lee
> únicamente `data-media-start`. Para `<video>`/`<audio>` usá siempre
> `data-media-start`.

Reglas duras de media: un `<video>` va `muted` salvo que sea intencionalmente
audible y declare `data-has-audio="true"`; **nunca** llames `play()`, `pause()`
ni seteés `currentTime` — HyperFrames es dueño de la reproducción y el seek.
`<video>` y `<audio>` pueden omitir `data-duration` si su duración intrínseca se
conoce y querés que suene el resto entero.

**Color grading:** `data-color-grading` con JSON (`preset`, `intensity`,
`adjust`, `details`, `effects`, `colorSpace`) sobre un `<img>` o `<video>` real.
**No** gradúa una escena HTML completa.

**Composiciones anidadas:** el host declara `data-composition-src` + su propia
ventana de timeline (`data-start`, `data-duration`, `data-width`,
`data-height`), y el `data-composition-id` del host tiene que coincidir con el ID
de adentro del archivo fuente. El archivo anidado transporta su markup dentro de
un `<template>` (con sus estilos y scripts adentro). HyperFrames seekea los
timelines anidados por separado: no los agregues a mano al timeline padre.

**Variables:** `data-composition-variables` declara el schema en el `<html>`;
`data-variable-values` pasa valores desde un host anidado; `--variables` /
`--variables-file` / `--batch` los pasan en el render. Binding directo con
`data-var-text`, `data-var-src` o `var(--variableId)` en CSS; `getVariables()`
cuando el valor afecta lógica.

**Contrato de animación (GSAP):**
- un solo timeline finito, creado con `{ paused: true }`;
- registrado **sincrónicamente** en `window.__timelines`;
- con la misma key que `data-composition-id`;
- sin estado de reloj de pared, sin random sin semilla, sin repeticiones
  infinitas.

Adaptadores soportados según el README: GSAP, CSS keyframes, Lottie, Three.js,
Anime.js, WAAPI, o un adapter propio.

**Audio — cuatro atributos** (referencia de audio effects):

| Atributo | Guarda | Va en |
|---|---|---|
| `data-fx-chain` | La cadena de efectos, en orden de señal (JSON) | `<audio>`, `<video>`, `<hf-audio-group>` |
| `data-automation` | Envolventes sobre volumen o un parámetro de efecto (JSON) | `<audio>`, `<video>`, `<hf-audio-group>` |
| `data-fx-carve` | Ajustes del *voiceover carve* (JSON) | `<audio>`, `<video>` |
| `data-audio-group` | ID del bus al que pertenece el clip (string pelado) | **solo `<audio>`** |

El JSON de esos atributos va **entre comillas dobles con las comillas internas
escapadas como `&quot;`**. Nada valida la cadena estáticamente: el preview toca
seco una cadena ilegible, y el render **falla toda la mezcla** en vez de
entregar una pista seca que suena plausible y está mal.

### 1.4 Transiciones

Dos familias, las dos de primera clase:

- **Shader** (`@hyperframes/shader-transitions`, WebGL): compositan las dos
  escenas píxel por píxel. Bloques documentados: `cross-warp-morph`,
  `thermal-distortion`, `whip-pan`, `cinematic-zoom`, `ridged-burn`, `glitch`,
  `chromatic-radial-split`, `light-leak`, `gravitational-lens`,
  `domain-warp-dissolve`, `ripple-waves`, `swirl-vortex`, `sdf-iris`,
  `flash-through-white`.
- **CSS**: animan los contenedores de escena (opacity, transforms, clip-path,
  filters). Bloques documentados: `transitions-blur`, `transitions-dissolve`,
  `transitions-push`, `transitions-cover`, `transitions-scale`,
  `transitions-destruction`, `transitions-light`, `transitions-mechanical`,
  `transitions-grid`, `transitions-3d`, `transitions-radial`,
  `transitions-distortion`.

Se instalan con `npx hyperframes add <bloque>`.

Regla de la doc, textual en espíritu: **elegí UNA transición primaria** para la
mayoría de los cortes, más uno o dos acentos para cambios de tema y el clímax.
*"Never use a different transition on every seam — that reads as chaos, not
design."*

Mapa energía → transición (resumido de la doc):

| Energía | Shader primaria | CSS primaria |
|---|---|---|
| Calma (wellness, brand story, lujo) | `cross-warp-morph`, `thermal-distortion` | `transitions-blur`, `transitions-dissolve` |
| Media (corporate, SaaS, explainer) | `whip-pan`, `cinematic-zoom` | `transitions-push`, `transitions-cover` |
| Alta (promos, deportes, música, launch) | `ridged-burn`, `glitch`, `chromatic-radial-split` | `transitions-scale`, `transitions-destruction`, `transitions-light` |

### 1.5 Captions y talking heads

- `/embedded-captions` (skill oficial de HyperFrames) agrega captions a un clip
  de talking head **sin tocar el footage**. Corre local de punta a punta:
  transcribe y mattea al sujeto sin API key. Necesita un clip de **un solo
  sujeto**; clips multi-speaker o con cortes duros se parten por toma o se
  rechazan.
- El modelo es **rail + embed**: el *rail* (rótulo legible, tipo lower-third)
  carga la mayoría del texto; el *embed* es la excepción ganada — **una** palabra
  grande matteada detrás del sujeto en el clímax. Meter todo el transcript como
  embed es el error más común que la skill previene.
- Las "identidades" de caption documentadas: `anchor` (default conservador,
  rail verbatim), `editorial`, `cream`, `loud`, `neon` (column-flow por
  registro), y las temáticas `ordnance`, `terminal`, `stomp`.
- `/talking-head-recut` es el hermano: overlays gráficos diseñados
  (lower-thirds, data callouts, pull-quotes, PiP) sobre el clip intacto.

### 1.6 Editar: el mapa verbo → atributo

La doc de edición mapea cada verbo de NLE a un cambio concreto e inspeccionable:

| Decís | Verbo de editor | Qué toca el agente |
|---|---|---|
| "que la escena 2 arranque más tarde" | Move | `data-start` |
| "poné los captions arriba del video" | Restack | `data-track-index` + `z-index` inline |
| "que el logo termine antes" | Trim (derecha) | `data-duration` |
| "saltate el primer segundo del clip" | Trim (frente, solo media) | `data-media-start` |
| "que la escena 2 dure dos segundos" | Retime | `data-duration` (y el largo del timeline de GSAP) |
| "la música está muy fuerte" | Level | `data-volume` |

Dos hábitos que la doc marca como no negociables al editar: **un cambio por
render** y **objetivos absolutos** ("escena 2 = 2 segundos", no "un toque más
corta"). *Split* se hace pidiéndolo (un clip pasa a ser dos con `data-start` /
`data-duration` ajustados); Studio todavía no expone split, slip, slide, ripple
ni roll como gesto.

### 1.7 Render y output — defaults y costos

- **Defaults**: MP4, 1920×1080, 30 fps, calidad `standard`. La doc dice que
  `standard` ya es visualmente lossless en 1080p.
- **Tiers**: `draft` para iterar, `standard` default, `high` para el master de
  entrega. La receta recomendada: *draft mientras iterás, un solo `high` final*.
- **Transparencia**: `mov` → ProRes 4444 con alpha (la opción de editor:
  Premiere, Final Cut, Resolve, After Effects; archivos grandes). `webm` → VP9
  con alpha, chico pero **solo los browsers decodean el alpha** — cualquier
  editor de video renderiza las zonas transparentes en negro. `png-sequence` →
  frames RGBA lossless. La transparencia solo tiene sentido en una pieza que va
  *arriba* de otro material (lower third, sting de logo); en una escena
  full-frame produce un archivo idéntico pero más pesado y menos compatible.
- **4K**: es un flag de render, no de autoría — la composición queda en su
  tamaño y Chrome supersamplea. Cuesta ~4× por frame y da un archivo 3–5× más
  grande, y **no aporta nada** a contenido ya atado a una grilla de píxeles (un
  `<video>` 1080p, un `<canvas>` de tamaño fijo, una imagen sub-4K). Constraints:
  la orientación tiene que coincidir con el aspect de la composición, la escala
  tiene que ser múltiplo entero (1080p → 4K es exactamente 2×), y **4K no se
  combina con HDR** en la misma pasada.
- **Framerate**: 60 fps duplica los frames a capturar y encodear. Vale para
  motion graphics rápidos en pantalla de alto refresco; se desperdicia en un
  talking head o una secuencia de títulos lenta.
- **HDR**: HDR10 MP4 (H.265 10-bit, BT.2020), *source-driven* — solo sale HDR si
  la composición referencia media HDR real. Fuera del proceso del Studio.
- **Dónde corre**: local, en la máquina del humano, vía la tool. La nube
  (`cloud render`, `lambda`) queda fuera del Studio por ahora.
- La doc marca explícitamente que **el render es user-gated por diseño**: el
  agente frena en el draft y renderiza el `high` cuando la persona aprueba.

### 1.8 Skills oficiales para agentes

`npx skills add heygen-com/hyperframes` (interactivo) o
`npx hyperframes skills update` (lo que un agente o un run no interactivo
debería usar: instala exactamente el core set desde `main`).

Router: `/hyperframes` — se lee primero, es el mapa de capacidades. Workflows de
creación: `/product-launch-video`, `/faceless-explainer`, `/pr-to-video`,
`/embedded-captions`, `/talking-head-recut`, `/motion-graphics`,
`/music-to-video`, `/slideshow`, `/general-video`, `/remotion-to-hyperframes`.
Skills de dominio: `/hyperframes-core`, `/hyperframes-animation`,
`/hyperframes-keyframes`, `/hyperframes-creative`, `/media-use`,
`/hyperframes-cli`, `/hyperframes-audio`, `/hyperframes-registry`, `/figma`.

> Esas skills son **de HyperFrames**, no del stack de Indash. Si están
> instaladas en la máquina del user, aprovechalas: saben más de la sintaxis
> vigente que este archivo. Si no están, esta skill se sostiene sola con el
> contrato de arriba.

---

## 2. Inferido (lectura nuestra, no cita)

1. **4:5 (1080×1350) no es un preset de `init --resolution`.** Los presets
   documentados son landscape / portrait / square (y sus variantes 4K). Para una
   pieza 4:5 hay que setear `data-width="1080"` `data-height="1350"` en el root,
   el `<meta name="viewport">` y la caja `#root` del CSS a mano. Inferencia por
   ausencia en la tabla de presets, no por una nota explícita.
2. **El aspect ratio de la composición se decide al autorar, no al renderizar.**
   `render --resolution` solo supersamplea manteniendo el aspect: no reencuadra.
   Por eso, si el mismo corte tiene que salir en 9:16 y en 1:1, son **dos
   composiciones** (o una con variables y dos renders), no un flag.
3. **HyperFrames no reencuadra un clip por vos.** Un clip 16:9 metido en una
   composición 9:16 se acomoda con CSS (`object-fit`, `transform`), que es el
   equivalente de un pan & scan. No hay un "auto-reframe" documentado.
4. **La duración total la manda el root.** Si una escena que abarca toda la
   composición se alarga, hay que subir también el `data-duration` del root
   (la doc lo dice para el caso de retiming; lo generalizamos).
5. **El flujo natural para el stack es CLI local**, no un servicio: la pieza
   final sale de la máquina del humano. En el Studio esa CLI la envuelve
   `mcp__indash__render_video` para que el render caiga versionado en el
   creativo; el día que la app empaquete FFmpeg y Chromium, la tool no cambia.

---

## 3. Verificar (NO está en las fuentes que leímos)

No afirmes nada de esto. Si el user lo pregunta, decile que hay que verificarlo
contra la doc vigente o contra la máquina.

1. **¿Existe un MCP server oficial de HyperFrames?** No encontramos uno en el
   README ni en el índice de la doc. La integración documentada con agentes es
   vía **skills + CLI**, no vía MCP. *Verificar.*
2. **`data-fps` en el root.** `render --help` de 0.8.33 lo confirma como
   default de `--fps` ("Defaults to the composition's root data-fps, else 30"),
   así que escribirlo en el root es válido; lo que no leímos es su entrada en
   la tabla del schema HTML. Si lo usás, ponelo igual a `video.fps` del
   manifiesto (30 salvo motivo).
3. **Límites duros**: duración máxima de una composición, cantidad máxima de
   clips o de composiciones anidadas, tamaño máximo de archivo fuente. No
   documentados en lo que leímos. *Verificar.*
4. **Formatos de video/imagen de entrada soportados exactamente.** `init`
   documenta MP4/WebM/MOV para `--video` y MP3/WAV/M4A para `--audio`; qué
   acepta un `<video src>` arbitrario dentro de la composición depende de lo que
   decodee Chrome. `preview --proxy` transcodea códecs hostiles para el browser
   (HEVC, ProRes, AV1) a un proxy de autoría. *Verificar* caso por caso con
   `lint` / `check`.
5. **Versión exacta de la CLI en la máquina del user.** Al 2026-08-25 el
   registro de npm devolvía `0.8.14` para `hyperframes`, pero es un proyecto que
   publica seguido. *Chequealo con `npx hyperframes --version`* en vez de
   asumirlo.
6. **Comportamiento de `publish` y `snapshot`.** Aparecen en el índice de
   comandos pero no leímos su referencia completa. *Verificar.*
7. **Compatibilidad exacta con los assets del MCP de Indash.** Los videos y
   frames que devuelve Indash son URLs públicas. La doc dice que las
   composiciones tienen que resolver la media local o por URL pública, pero
   **no verificamos** el comportamiento de HyperFrames con URLs firmadas o que
   expiran. Por las dudas, la skill baja los assets a disco antes de componer.
