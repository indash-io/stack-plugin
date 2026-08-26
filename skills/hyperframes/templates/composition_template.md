# Template — Composición HyperFrames

Esqueleto de `index.html` para una pieza de performance del stack. Todo lo que
hay acá está respaldado por `reference/hyperframes.md`; las decisiones detrás
están en `instructions/05_composition.md`.

Adaptá los números al plan de edición. **No copies los valores de ejemplo sin
reemplazarlos.**

---

## `index.html` — 9:16, 12 segundos, 5 cortes

```html
<!doctype html>
<html lang="es">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=1080, height=1920" />
    <script src="https://cdn.jsdelivr.net/npm/gsap@3/dist/gsap.min.js"></script>
    <style>
      @font-face {
        font-family: "MarcaSans";
        src: url("./assets/Marca-Bold.woff2") format("woff2");
        font-weight: 700;
        font-display: block;
      }

      :root {
        /* Marca — heredada del CLAUDE.md del cliente */
        --tinta: #1B1A17;
        --papel: #F2EBDD;
        --acento: #B89968;

        /* Zona segura 9:16 — ver style/safe_zones.md */
        --safe-top: 270px;
        --safe-bottom: 420px;
        --safe-x: 60px;
        --safe-right: 162px;
      }

      body { margin: 0; background: #000; }

      #root {
        position: relative;
        width: 1080px;
        height: 1920px;
        overflow: hidden;
        font-family: "MarcaSans", system-ui, sans-serif;
      }

      .clip { position: absolute; inset: 0; }

      .clip video, .clip img {
        width: 100%; height: 100%;
        object-fit: cover;
        display: block;
      }

      /* Orden de pintado: SIEMPRE z-index, nunca data-track-index */
      .layer-video   { z-index: 1; }
      .layer-scrim   { z-index: 2; }
      .layer-text    { z-index: 3; }

      .scrim {
        background: linear-gradient(to top, rgba(0,0,0,.72) 0%, rgba(0,0,0,0) 42%);
      }

      .hook-text {
        position: absolute;
        left: var(--safe-x); right: var(--safe-right);
        top: calc(var(--safe-top) + 60px);
        margin: 0;
        font-size: 110px; font-weight: 700; line-height: 1.05;
        color: var(--papel);
        text-wrap: balance;
      }

      .caption-rail {
        position: absolute;
        left: var(--safe-x); right: var(--safe-right);
        bottom: var(--safe-bottom);
        margin: 0;
        font-size: 64px; font-weight: 700; line-height: 1.25;
        color: var(--papel);
      }
      .caption-rail em { font-style: normal; color: var(--acento); }

      .cta-text {
        position: absolute;
        left: var(--safe-x); right: var(--safe-right);
        bottom: calc(var(--safe-bottom) + 120px);
        margin: 0;
        font-size: 84px; font-weight: 700; line-height: 1.1;
        color: var(--tinta);
      }

      .brand-mark {
        position: absolute;
        left: var(--safe-x);
        bottom: var(--safe-bottom);
        width: 220px;
      }
    </style>
  </head>

  <body>
    <div
      id="root"
      data-composition-id="main"
      data-start="0"
      data-duration="12"
      data-width="1080"
      data-height="1920"
    >
      <!-- ── CORTE 1 · HOOK · 0.0 – 2.0 ─────────────────────────────── -->
      <video
        id="shot-01"
        class="clip layer-video"
        src="./assets/shot-01.mp4"
        data-start="0"
        data-duration="2"
        data-media-start="2.2"
        muted
        playsinline
      ></video>

      <div id="scrim-01" class="clip layer-scrim scrim"
           data-start="0" data-duration="2"></div>

      <h1 id="hook-text" class="clip layer-text"
          data-start="0" data-duration="2">
        <span class="hook-text">Se absorbe en 30 segundos</span>
      </h1>

      <!-- ── CORTE 2 · DESARROLLO · 2.0 – 5.0 ───────────────────────── -->
      <video
        id="shot-02"
        class="clip layer-video"
        src="./assets/shot-02.mp4"
        data-start="2"
        data-duration="3"
        muted
        playsinline
      ></video>

      <div id="scrim-02" class="clip layer-scrim scrim"
           data-start="2" data-duration="3"></div>

      <div id="cap-02" class="clip layer-text"
           data-start="2" data-duration="2.7">
        <p class="caption-rail">Una capa fina alcanza <em>todo el día</em></p>
      </div>

      <!-- ── CORTE 3 · DESARROLLO · 5.0 – 7.5 ───────────────────────── -->
      <video
        id="shot-03"
        class="clip layer-video"
        src="./assets/shot-03.mp4"
        data-start="5"
        data-duration="2.5"
        data-media-start="1.4"
        muted
        playsinline
      ></video>

      <!-- ── CORTE 4 · PAYOFF · 7.5 – 9.8 ───────────────────────────── -->
      <video
        id="shot-04"
        class="clip layer-video"
        src="./assets/shot-04.mp4"
        data-start="7.5"
        data-duration="2.3"
        muted
        playsinline
      ></video>

      <div id="scrim-04" class="clip layer-scrim scrim"
           data-start="7.5" data-duration="2.3"></div>

      <div id="cap-04" class="clip layer-text"
           data-start="7.7" data-duration="2.0">
        <p class="caption-rail">Sin residuo graso</p>
      </div>

      <!-- ── CORTE 5 · CTA · 9.8 – 12.0 ─────────────────────────────── -->
      <img
        id="cta-frame"
        class="clip layer-video"
        src="./assets/packshot.png"
        data-start="9.8"
        data-duration="2.2"
        alt=""
      />

      <div id="cta-block" class="clip layer-text"
           data-start="9.9" data-duration="2.1">
        <p class="cta-text">Pedilo en el link</p>
        <img class="brand-mark" src="./assets/logo.svg" alt="" />
      </div>

      <!-- ── AUDIO ──────────────────────────────────────────────────── -->
      <!-- La música se parte en tramos para la curva de volumen del plan. -->
      <audio id="music-a" src="./assets/music.mp3"
             data-start="0"   data-duration="2"    data-media-start="8.5"  data-volume="0.80"></audio>
      <audio id="music-b" src="./assets/music.mp3"
             data-start="2"   data-duration="7.8"  data-media-start="10.5" data-volume="0.20"></audio>
      <audio id="music-c" src="./assets/music.mp3"
             data-start="9.8" data-duration="2.2"  data-media-start="18.3" data-volume="0.60"></audio>

      <audio id="vo" src="./assets/vo.wav"
             data-start="2" data-duration="7.8" data-volume="1"></audio>
    </div>

    <script>
      // Contrato de animación: UN timeline finito, paused, registrado
      // sincrónicamente, con la MISMA key que data-composition-id.
      window.__timelines = window.__timelines || {};
      const tl = gsap.timeline({ paused: true });

      // Hook — visible desde el frame 1, entrada de 0.35s
      tl.fromTo("#hook-text .hook-text",
        { y: 40, opacity: 0 },
        { y: 0, opacity: 1, duration: 0.35, ease: "power3.out" }, 0);
      tl.to("#hook-text .hook-text", { opacity: 0, duration: 0.2, ease: "power2.in" }, 1.75);

      // Caption corte 2
      tl.fromTo("#cap-02 .caption-rail",
        { y: 32, opacity: 0 },
        { y: 0, opacity: 1, duration: 0.3, ease: "power3.out" }, 2.05);
      tl.to("#cap-02 .caption-rail", { opacity: 0, duration: 0.2 }, 4.5);

      // Caption payoff
      tl.fromTo("#cap-04 .caption-rail",
        { y: 32, opacity: 0 },
        { y: 0, opacity: 1, duration: 0.3, ease: "power3.out" }, 7.75);
      tl.to("#cap-04 .caption-rail", { opacity: 0, duration: 0.2 }, 9.5);

      // CTA — push-in lento sobre el packshot (movimiento interno)
      tl.fromTo("#cta-frame",
        { scale: 1.0 }, { scale: 1.06, duration: 2.2, ease: "none" }, 9.8);
      tl.fromTo("#cta-block",
        { opacity: 0 }, { opacity: 1, duration: 0.3, ease: "power3.out" }, 9.95);

      window.__timelines.main = tl;
    </script>
  </body>
</html>
```

---

## Deltas por formato

Cambiar de formato = cambiar el root, el viewport, la caja `#root` y las cuatro
variables de zona segura. Nada más.

| | 9:16 | 4:5 | 1:1 | 16:9 |
|---|---|---|---|---|
| `data-width` / `data-height` | 1080 / 1920 | 1080 / 1350 | 1080 / 1080 | 1920 / 1080 |
| `--safe-top` | 270px | 108px | 108px | 54px |
| `--safe-bottom` | 420px | 200px | 130px | 130px |
| `--safe-x` | 60px | 60px | 60px | 96px |
| `--safe-right` | 162px | 60px | 60px | 96px |
| Escala tipográfica | ×1.00 | ×0.70 | ×0.56 | ×0.56 |

---

## Patrón: transición con overlap

Cuando el seam lleva crossfade, el clip entrante arranca **antes** de que
termine el saliente, con `data-start` relativo negativo:

```html
<video id="shot-02" class="clip layer-video" src="./assets/shot-02.mp4"
       data-start="shot-01 - 0.3" data-duration="3.3" muted playsinline></video>
```
```js
tl.fromTo("#shot-02", { opacity: 0 }, { opacity: 1, duration: 0.3, ease: "none" }, 1.7);
```

El overlap se resuelve con **`z-index`** (el entrante arriba), no con
`data-track-index`.

---

## Patrón: clip con aspect distinto (fondo desenfocado)

```html
<video id="s3-bg" class="clip layer-video" src="./assets/shot-03.mp4"
       data-start="5" data-duration="2.5" muted playsinline></video>
<video id="s3" class="clip layer-video" src="./assets/shot-03.mp4"
       data-start="5" data-duration="2.5" muted playsinline></video>
```
```css
#s3-bg { object-fit: cover; filter: blur(28px) brightness(.7); transform: scale(1.15); z-index: 1; }
#s3    { object-fit: contain; z-index: 2; }
```

---

## Patrón: clip con audio nativo (UGC)

```html
<video id="ugc-01" class="clip layer-video" src="./assets/ugc-01.mp4"
       data-start="0" data-duration="4"
       data-has-audio="true" data-volume="1"
       playsinline></video>
```

Sin `muted`, y con `data-has-audio="true"` declarado. Bajá la música a
`0.10–0.15` mientras suena.

---

## Recordatorios (los errores que más se repiten)

- `data-composition-id` del root **==** key de `window.__timelines`.
- `data-width`/`data-height` **==** viewport **==** caja `#root`.
- `data-duration` del root manda la duración del render, **no** el largo del
  timeline de GSAP.
- Trim de entrada de `<video>`/`<audio>`: **`data-media-start`**, nunca
  `data-playback-start`.
- Todo `<video>` va `muted` + `playsinline`, salvo audio nativo intencional.
- Nunca `play()`, `pause()` ni `currentTime` desde JS.
- Orden de pintado: **`z-index`**. `data-track-index` es display de Studio.
- `font-display: block` en todo `@font-face`.
- Todos los `src` son rutas relativas dentro del proyecto.
