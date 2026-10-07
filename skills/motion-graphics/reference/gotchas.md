# Gotchas de HyperFrames en producción

Cosas que no están en `hyperframes/reference/hyperframes.md` y que costaron un render o
una ronda. **Pendiente:** cuando se limpie la skill `hyperframes` como base, esto se muda
allá.

## Composición

- **Animá solo `transform`, `opacity`, `filter` y `clip-path`.** El linter rechaza
  animar `left`, `top` o márgenes.
- **Las superposiciones a propósito se declaran.** Si dos elementos se pisan por diseño
  (un pop-out sobre el teléfono), poné `data-layout-allow-overlap` en el contenedor. Si
  no, `check` lo marca como oclusión.
- **Los estados iniciales de un `fromTo` se filtran antes del cue.** Con
  `immediateRender` (el default), el estado "from" se aplica en el frame 0 aunque el tween
  arranque en el 7. Usá `immediateRender: false` y fijá el estado inicial con un `tl.set`
  en 0.
- **El seek no dispara `onUpdate`.** Todo lo que se dibuja por código (canvas, WebGL,
  contadores) va por un setter tweenado (`reference/threejs.md`).
- **Desde una sub-composición, las rutas son relativas a la raíz del proyecto**
  (`assets/...`), no a la carpeta de la composición (`../assets/...`).
- **Una regla genérica le puede ganar a la específica.** `.pop img { width: 100% }` le
  gana a `img.chk` si la segunda tiene menos especificidad. Usá `.pop img.chk`.

## Studio

- **Studio agrega `data-hf-id="…"`** a los elementos del HTML cuando lo abrís. Un script
  que busca y reemplaza en el HTML tiene que matchear con regex y tolerar ese atributo.
- **Studio lista como composición cualquier `.html` del proyecto.** Si una composición se
  genera desde una plantilla, la plantilla va como `src/*.tpl`, y un `tools/build.py`
  escribe el `.html` final.
- **La reproducción no avanza en una ventana de Chrome automatizada** (Chrome la toma
  como oculta). Verificá posicionándote en cada momento y con renders. A la persona le
  anda normal.
- **Studio puede dar WebGL1.** Ver `reference/threejs.md`.
- **Un puerto por proyecto.** `preview --background` en cada carpeta hermana, y el link
  de cada una con su puerto.
- **`init` instala las skills oficiales de HyperFrames en el proyecto.** Para que no lo
  haga, `HYPERFRAMES_SKIP_SKILLS=1`.

## Audio

- **El render suma los stems linealmente**: `data-volume` es ganancia lineal.
- **Si el AAC pasa de −1 dBTP, el render baja toda la mezcla hasta entrar.** Sin margen
  en los stems, el render suena más bajo de lo que mediste. Con 3 pasadas sin entrar,
  el render falla (`audioPadTrim: AAC true peak remained above -1 dBFS`).
- **Un tema de stock que arranca a nivel pleno en el frame 0 hace fallar el render**
  por ese mismo chequeo. Lo evita un fade-in de 30 ms (`music_conform.py` ya lo pone).
- **Un WAV mono se duplica a los dos canales y suena +3 dB.** Los stems se escriben en
  estéreo (los scripts de la skill ya lo hacen).

## Análisis de música

- **Los tiempos de `librosa.beat.beat_track` salen 0.1–0.2 s antes del golpe real.**
  Sirven para el tempo, no para la fase: la fase se mide en transitorios por banda
  (`beat_phase.py`).
- **El BPM crudo de librosa viene cuantizado.** El real sale de una regresión sobre los
  beats.
