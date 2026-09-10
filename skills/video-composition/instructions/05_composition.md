# 05 — Composición HyperFrames

Traducís el plan de edición a un proyecto HyperFrames real. **Todo lo que
escribas acá tiene que estar respaldado por `reference/hyperframes.md`.** Si un
atributo o un flag no está ahí, no lo uses: decí *"hay que verificar"*.

Usá `templates/composition_template.md` como esqueleto. Este archivo explica las
decisiones.

---

## 1. Estructura: la composición vive EN el creativo

```
creatives/<brief>/<grupo>/<id>/
  <id>.indash                 el manifiesto (no lo tocás acá — ver 07)
  composition/                ← tu carpeta
    PLAN.md                   el plan de edición
    index.html                la composición
    assets/
      clip-01-v2.mp4          los clips vigentes, COPIADOS de workbench/<brief>/<carpeta>/clips/
      clip-02-v1.mp4
      packshot.<ext>          copiado de library/products/ o de un candidato (su formato original)
      musica.mp3              copiada de la carpeta del Workbench (la trajo el humano)
      Marca-Bold.ttf          copiada de library/fonts/ del proyecto
      logo.svg                copiado de library/logos/
  renders/                    ← NO lo escribís vos: lo llena render_video (v1.mp4, v2.mp4 …)
```

**Todo lo que la composición referencia vive en `composition/assets/`**, con
rutas relativas (`./assets/clip-01-v2.mp4`). Copiá los archivos — nunca
referencies `workbench/`, `library/` ni `creatives/` directo: si el humano
mueve o renombra en el Workbench, la composición no se puede romper, y el
creativo tiene que renderizar solo dentro de un año. Conservá el nombre con
versión del clip (`clip-01-v2.mp4`): dice qué toma entró.

`composition/` es tuya hasta que el creativo está `approved`: la escribís de
cero o la editás libremente en cada iteración. No hace falta scaffoldear con
`npx hyperframes init` (crearía un proyecto aparte): partí de
`templates/composition_template.md` y escribí `index.html` directo.

---

## 2. El root: formato y duración

```html
<div
  id="root"
  data-composition-id="main"
  data-start="0"
  data-duration="12"
  data-width="1080"
  data-height="1920"
>
```

| Formato | `data-width` | `data-height` |
|---|---|---|
| 9:16 | 1080 | 1920 |
| 4:5 | 1080 | 1350 |
| 1:1 | 1080 | 1080 |
| 16:9 | 1920 | 1080 |

Los mismos números van en `<meta name="viewport" content="width=1080, height=1920">`
y en el `width`/`height` de `#root` en el CSS. Los tres tienen que coincidir.

**`data-duration` del root = duración final del render.** El compilador lo lee
antes de que corra ningún script: un script no lo puede cambiar. Y **no** sale
del largo del timeline de GSAP. Si una escena se estira más allá del root, no se
ve.

---

## 3. Un clip por corte

```html
<video
  id="shot-01"
  class="clip"
  src="./assets/shot-01.mp4"
  data-start="0"
  data-duration="2"
  data-media-start="2.2"
  muted
  playsinline
></video>
```

Reglas duras (todas verificadas en la doc, ver `reference/hyperframes.md` §1.3):

- **`id` estable** en cada clip: es lo que después usás para editar, animar y
  referenciar en timing relativo.
- **`data-media-start`** para el trim de entrada de `<video>` y `<audio>` —
  **nunca** `data-playback-start` en esos elementos: el mixer de audio lee solo
  `data-media-start`, y mezclarlos deja imagen recortada sobre audio entero.
  `data-playback-start` es el nombre canónico **solo** para el host de una
  composición anidada.
- **`muted` + `playsinline`** en todo `<video>` salvo que sea intencionalmente
  audible; en ese caso, además, `data-has-audio="true"`.
- **Nunca** `play()`, `pause()` ni `currentTime` desde JS.
- `data-track-index` es **display de Studio**: el render lo ignora y no impide
  overlap. El orden de pintado se controla con **`z-index` de CSS**.
- `data-duration` **≤ duración real del archivo** (medida en Discovery). Si lo
  pasás, HyperFrames congela el último frame.

### Timing: absoluto vs relativo

Un `data-start` numérico es tiempo absoluto en segundos. Un `data-start` con el
**id de otro clip** arranca cuando ese clip termina, y admite `+` / `-`
segundos:

```html
data-start="shot-01"          <!-- justo cuando termina shot-01 -->
data-start="shot-01 - 0.3"    <!-- 0.3s de overlap, para un crossfade -->
data-start="shot-01 + 0.2"    <!-- 0.2s de aire -->
```

Referencias solo dentro de la misma composición, el clip referido tiene que
tener duración conocida, y **no puede haber ciclos**.

**Recomendación práctica**: usá **absolutos** para los cortes principales (así
el HTML se lee contra el plan de edición de un vistazo) y **relativos** solo
donde el overlap importa (los seams con transición).

---

## 4. Encuadre y `object-fit`

HyperFrames **no reencuadra por vos**. Un clip con aspect distinto al de la
composición se resuelve con CSS:

```css
.clip video, .clip img { width: 100%; height: 100%; object-fit: cover; }
```

Las tres estrategias que se propusieron en Decisions:

**Cover** — recorta los laterales. El default cuando el sujeto está centrado:

```css
#shot-03 { object-fit: cover; object-position: center 40%; }
```

**Fondo desenfocado** — el mismo archivo dos veces: uno de fondo escalado y
borroso, el real centrado encima. Dos `<video>` con el mismo `src`, mismo
`data-start` y `data-duration`, distinto `z-index`:

```html
<video id="s3-bg" class="clip" src="./assets/shot-03.mp4" data-start="5" data-duration="2.5" muted playsinline></video>
<video id="s3" class="clip" src="./assets/shot-03.mp4" data-start="5" data-duration="2.5" muted playsinline></video>
```
```css
#s3-bg { object-fit: cover; filter: blur(28px) brightness(0.7); transform: scale(1.15); z-index: 1; }
#s3    { object-fit: contain; z-index: 2; }
```

**Afuera** — si ninguna lo salva sin romper el ritmo. Ya se decidió en Decisions.

---

## 5. Animación: el contrato de GSAP

```html
<script src="https://cdn.jsdelivr.net/npm/gsap@3/dist/gsap.min.js"></script>
<script>
  window.__timelines = window.__timelines || {};
  const tl = gsap.timeline({ paused: true });

  tl.fromTo("#hook-text", { y: 40, opacity: 0 },
            { y: 0, opacity: 1, duration: 0.35, ease: "power3.out" }, 0);
  tl.to("#hook-text", { opacity: 0, duration: 0.2 }, 1.8);

  window.__timelines.main = tl;   // misma key que data-composition-id
</script>
```

Las cuatro reglas del contrato (`reference/hyperframes.md` §1.3):

1. **un solo** timeline finito, creado con `{ paused: true }`;
2. registrado **sincrónicamente** en `window.__timelines`;
3. con la **misma key** que `data-composition-id`;
4. **sin** reloj de pared, **sin** random sin semilla, **sin** repeticiones
   infinitas.

Romper cualquiera de las cuatro rompe el determinismo, que es la razón de ser de
HyperFrames. Si necesitás algo aleatorio (confeti, partículas), usá un PRNG con
semilla fija.

**El linter falla si la composición usa GSAP y el script no está cargado** — es
uno de los errores que `lint` reporta por nombre (`missing_gsap_script`).

Adaptadores alternativos documentados: CSS keyframes, Lottie, Three.js,
Anime.js, WAAPI, o un adapter propio. Para una pieza de performance, **GSAP
alcanza y sobra**; no metas Three.js porque sí.

---

## 6. Transiciones

Se instalan del catálogo, no se escriben a mano:

```bash
npx hyperframes add transitions-push
npx hyperframes add flash-through-white
```

- Los bloques **shader** (`@hyperframes/shader-transitions`) compositan las dos
  escenas píxel por píxel: `cross-warp-morph`, `whip-pan`, `cinematic-zoom`,
  `ridged-burn`, `glitch`, `light-leak`, `flash-through-white`, `sdf-iris`…
- Los bloques **CSS** animan los contenedores: `transitions-blur`,
  `transitions-dissolve`, `transitions-push`, `transitions-cover`,
  `transitions-scale`, `transitions-light`…

Lista completa en `reference/hyperframes.md` §1.4.

Si no querés instalar nada, un **crossfade CSS** hecho a mano es perfectamente
válido: dos clips con overlap (`data-start="shot-01 - 0.3"`) y una tween de
opacidad en el timeline. Es más barato y para el 60-70% de los seams alcanza.

**Una primaria + un acento como máximo.** El overlap de la transición se
resuelve con `data-start` relativo negativo y `z-index`, no con
`data-track-index`.

---

## 7. Captions y texto on-screen

Todo el detalle tipográfico está en `style/captions_typography.md` y el
posicionamiento en `style/safe_zones.md`. Lo estructural:

```html
<div id="cap-1" class="clip caption-rail" data-start="2.0" data-duration="3.0">
  <p>Se absorbe en 30 segundos</p>
</div>
```

- El bloque de caption es un clip DOM más: `id`, `class="clip"`, `data-start`,
  `data-duration`. Su visibilidad la maneja `data-start`, no la clase.
- El orden de pintado sobre el video es **`z-index`**, no `data-track-index`.
- La animación de entrada/salida vive en el timeline de GSAP, no en `@keyframes`
  con reloj de pared.

**Si hay voz y querés captions verbatim**, primero los guiones de
`workbench/<brief>/<carpeta>/scripts/*.md` (son lo que se dijo); para
sincronizarlos palabra por palabra, o cuando la voz es un archivo que trajo el
humano sin guion, transcribí con la CLI:

```bash
npx hyperframes transcribe ./assets/clip-01-v2.mp4 --language es --to srt --output ./assets/clip-01.srt
```

Motor `auto` (Parakeet si está, si no Whisper); corre local, sin API key.

Modelo **rail + embed**: el rail carga el texto, el embed es **una** palabra
grande en el clímax. Nunca el transcript entero como embed (regla 16 del `SKILL.md`).

### Fuentes de marca

```css
@font-face {
  font-family: "MarcaSans";
  src: url("./assets/Marca-Bold.ttf") format("truetype");
  font-weight: 700;
  font-display: block;
}
```

Copiá el archivo real de `library/fonts/` del proyecto al proyecto. `font-display:
block` evita que el render capture un frame con la fuente de fallback.

---

## 8. Audio

```html
<audio id="music" src="./assets/music.mp3"
       data-start="0" data-duration="12"
       data-media-start="8.5" data-volume="0.22"></audio>

<audio id="vo" src="./assets/vo.wav"
       data-start="2" data-duration="7.8" data-volume="1"></audio>
```

- `data-volume`: `1` = 0 dB, `0` = silencio, arriba de `1` amplifica hasta
  `3.98` (+12 dB).
- `data-media-start` para entrar en la parte buena de la música (casi nunca es
  el segundo 0 del archivo).
- Para una **curva** de volumen (bajar bajo la voz y subir en el CTA) hay dos
  caminos: partir la música en varios `<audio>` consecutivos con distinto
  `data-volume` (simple y verificable), o usar `data-automation` con envolventes
  (más fino). Si vas por `data-automation`, escribí el JSON **entre comillas
  dobles con las comillas internas escapadas como `&quot;`** — la doc lo marca
  explícito, y una comilla simple deja el atributo invisible para las
  herramientas de la CLI.
- **Nada valida la cadena de audio estáticamente.** El preview toca *seco* una
  cadena ilegible; el render **falla toda la mezcla**. Si vas a meter
  `data-fx-chain`, verificá con un render `draft` antes de dar nada por bueno.

Si el clip de video aporta su propio audio: `data-has-audio="true"` en el
`<video>` y sacale el `muted`.

---

## 9. Los gates y el render

Los gates los corrés vos, dentro de `composition/`; el render lo corre la app:

```bash
# 1. gates (cwd = composition/)
npx hyperframes lint
npx hyperframes check --snapshots
```

```
# 2. draft para revisar el corte → renders/vN.mp4 + video.active
mcp__indash__render_video { creative: "creatives/<brief>/<grupo>/<id>", quality: "draft" }
mcp__indash__view_creative { creative: "creatives/<brief>/<grupo>/<id>" }   # hoja de contactos

# 3. final, solo cuando el humano aprobó el draft
mcp__indash__render_video { creative: "creatives/<brief>/<grupo>/<id>", quality: "high" }
```

La tool renderiza `composition/index.html` a MP4 al tamaño de la composición,
a los fps del root (`data-fps`, si no 30), con la calidad que le pasás. No hay
más flags que esos por diseño: 4K, 60 fps, transparencia o HDR no aportan nada
a una pieza para feed hecha de `<video>` 1080p, y un video del board es
siempre un MP4 full-frame. Si el humano necesita un master distinto (ProRes
con alpha para un editor), eso es un pedido aparte: `npx hyperframes render
--format mov` a mano, fuera de `renders/`, y se lo entregás como archivo.

---

## 10. Checklist rápido antes de pasar al render

- [ ] `data-composition-id` del root == key de `window.__timelines`.
- [ ] `data-width` / `data-height` == viewport == caja `#root` del CSS.
- [ ] `data-duration` del root == último timecode del plan de edición.
- [ ] Ningún `data-duration` de clip supera la duración real del archivo.
- [ ] Todos los `src` son rutas relativas dentro del proyecto.
- [ ] Todo `<video>` tiene `muted` + `playsinline` (o `data-has-audio="true"`).
- [ ] Trim de entrada con `data-media-start`, no `data-playback-start`.
- [ ] Un solo timeline GSAP, `paused: true`, registrado sincrónicamente.
- [ ] Orden de pintado por `z-index`, no por `data-track-index`.
- [ ] Todo el texto dentro de la zona segura del formato.
- [ ] La fuente de marca está copiada al proyecto y declarada con `@font-face`.

→ Corré `eval/quality_checklist.md` completo y pasá a
`instructions/06_render_qa.md`.
