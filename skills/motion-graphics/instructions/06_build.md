# 06 — Build

Objetivo: el proyecto corre en Studio sin errores y pasa `lint` y `check`. Antes de
escribir composición leé `${CLAUDE_PLUGIN_ROOT}/skills/hyperframes/reference/hyperframes.md`
(API) y `reference/gotchas.md` (lo que rompe en producción).

## 1. Scaffold

```bash
HYPERFRAMES_SKIP_SKILLS=1 npx hyperframes init <carpeta> --non-interactive --example=blank --resolution <landscape|portrait>
```

```
index.html             root: monta las capas y los <audio>
compositions/
  00-world.html        Three.js persistente debajo de todo (si hay mundo 3D)
  01-<escena>.html …   una composición por escena del storyboard
  90-fx.html           flash frames, glitch, barridos en los cortes
  99-finish.html       grano, viñeta
assets/  app/ brand/ fonts/ audio/ vendor/
audio-src/             los .py que generan los stems
src/*.tpl + tools/build.py   solo si una composición se genera (gotchas: .tpl)
STORYBOARD.md
```

## 2. Tiempo

- Un timeline GSAP pausado por composición, registrado en `window.__timelines`.
- Todo tiempo sale de la grilla: `const B = n => n * 0.5` (beats a 120 BPM). Si escribís
  un número suelto, que sea un beat o una corchea.
- Las escenas se pisan medio beat en los cortes cuando la transición lo pide (zoom-through,
  iris). Si no, el corte es seco en el downbeat.

## 3. Patrones que ya funcionaron

- **Teléfono en CSS 3D con pantallas reales**: cada pantalla va en su propio wrapper
  con su cover del punto de grabación. Las pantallas cambian con push lateral.
  - Pop-out: el recorte de la UI sale con `translateZ` + escala, y un parche tapa el hueco.
  - Tap: círculo que se expande en el botón real, y la pantalla siguiente entra en ese beat.
- **Highlight sobre una línea real**: las filas que da `ui_crops.py rows` + un trazo en
  el acento de la marca que se dibuja de izquierda a derecha (`clip-path`).
- **Logo 3D que aterriza en el logo real de una pantalla**: el handoff 3D → DOM de
  `reference/threejs.md`.
- **End card**: un iris (círculo con `clip-path`) que abre desde el último tap y muestra
  la imagen oficial sin tocar.
- **Captions**: dos capas apiladas (trazo + relleno) si el guion pide contorno.

## 4. El loop técnico

```bash
npx hyperframes lint
npx hyperframes check --json                 # layout, contraste, runtime
npx hyperframes snapshot --at 3.0,7.6,11.2   # los momentos que tocaste
npx hyperframes preview --background         # deja Studio corriendo; usá un puerto por proyecto
```

Con Studio abierto en Chrome, posicionate en cada escena 3D y leé la consola. La
reproducción no avanza en una ventana de Chrome automatizada (Chrome la toma como oculta):
verificá posicionándote en cada momento y con renders.

Listo cuando `lint` no da errores, `check` pasa y la consola de Studio está limpia.
Siguiente: `07_review.md`.
