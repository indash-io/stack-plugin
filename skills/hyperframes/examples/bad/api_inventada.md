# MALO — API inventada de HyperFrames

El error más caro de esta skill: entregar una composición que **no existe**.
Atributos que suenan razonables, flags que parecen lógicos, comandos que "debería
haber". El user corre el render, falla, y perdió media hora confiando en algo que
nadie verificó.

Todos los casos de acá son cosas que un agente escribe sin querer cuando
completa por analogía con otras herramientas (Remotion, FFmpeg, After Effects,
un NLE) en vez de leer `reference/hyperframes.md`.

---

## MALO #1 — `data-transition` en el clip

```html
<!-- ❌ NO EXISTE -->
<video id="shot-02" class="clip" src="./assets/shot-02.mp4"
       data-start="2" data-duration="3"
       data-transition="crossfade" data-transition-duration="0.4"></video>
```

Suena perfectamente razonable. **No está en el contrato.** Las transiciones son
bloques del catálogo (`npx hyperframes add transitions-push`) o un crossfade
hecho a mano con overlap + una tween de opacidad.

**Fix**:

```html
<video id="shot-02" class="clip layer-video" src="./assets/shot-02.mp4"
       data-start="shot-01 - 0.3" data-duration="3.3" muted playsinline></video>
```
```js
tl.fromTo("#shot-02", { opacity: 0 }, { opacity: 1, duration: 0.3, ease: "none" }, 1.7);
```

---

## MALO #2 — `data-aspect-ratio` / `data-format` en el root

```html
<!-- ❌ NO EXISTE -->
<div id="root" data-composition-id="main" data-aspect-ratio="9:16" data-duration="12">
```

El formato se declara con **`data-width` y `data-height` en píxeles**. No hay un
atributo de aspect ratio.

**Fix**: `data-width="1080" data-height="1920"`, y los mismos números en el
`<meta name="viewport">` y en la caja `#root` del CSS.

---

## MALO #3 — `render --aspect 9:16` para reencuadrar

```bash
# ❌ NO HACE ESO
npx hyperframes render --aspect 9:16 --output vertical.mp4
```

`--resolution` en `render` **supersamplea manteniendo el aspect**: el ratio de
destino tiene que coincidir con el de la composición y la escala tiene que ser
un múltiplo entero. No reencuadra nada.

**Fix**: dos formatos = **dos composiciones**. Se decide en Decisions y se
entrega como dos subcarpetas del mismo set (ver
`templates/output_template.md`).

---

## MALO #4 — `data-playback-start` en un `<video>`

```html
<!-- ❌ MEDIO ROTO: imagen recortada, audio entero -->
<video id="ugc" src="./assets/ugc.mp4" data-start="0" data-duration="6"
       data-playback-start="3.5" data-has-audio="true"></video>
```

Es el caso más traicionero porque **funciona a medias**: el runtime lee
`data-playback-start`, pero el mixer de audio lee **solo** `data-media-start` y
alimenta con eso el `-ss` de ffmpeg. Resultado: la imagen entra a los 3.5s del
archivo y el audio desde el 0. Desincronizado, y sin un error que lo delate.

**Fix**: para `<video>` y `<audio>`, **siempre `data-media-start`**.
`data-playback-start` es el nombre canónico solo para el host de una composición
anidada.

---

## MALO #5 — `data-track-index` como orden de capas

```html
<!-- ❌ NO CONTROLA EL ORDEN DE PINTADO -->
<div id="caps" class="clip" data-start="0" data-duration="12" data-track-index="10"></div>
```

Ya está desarrollado en `examples/bad/captions_ilegibles.md` (#7), pero se repite
tanto que va de nuevo: `data-track-index` es la **fila que dibuja Studio**. El
render lo ignora. El orden de pintado es **`z-index`**.

---

## MALO #6 — Padear el timeline de GSAP para alargar el render

```js
// ❌ NO ALARGA NADA
tl.set({}, {}, 15);   // "para que dure 15 segundos"
```

La duración del render sale del **`data-duration` del root**. El compilador lo
lee antes de que corra ningún script. Un timeline más largo que el root
simplemente no se ve; un centinela vacío no hace nada.

**Fix**: `data-duration="15"` en el root.

---

## MALO #7 — Controlar la reproducción a mano

```js
// ❌ ROMPE EL SEEK
document.querySelector("#shot-01").currentTime = 2.2;
document.querySelector("#shot-01").play();
```

HyperFrames es dueño de la reproducción y del seek: es lo que hace que el render
sea determinístico. Tocarlo desde el script pelea con el motor.

**Fix**: `data-media-start="2.2"` en el elemento. Nunca `play()`, `pause()` ni
`currentTime`.

---

## MALO #8 — Animación con reloj de pared

```css
/* ❌ NO ES SEEKABLE */
.pulso { animation: latido 1.2s infinite ease-in-out; }
```

```js
// ❌ TAMPOCO
setInterval(() => contador.textContent = ++n, 100);
```

El renderer **busca cada frame**: no reproduce en tiempo real. Una animación
infinita con reloj de pared, un `setInterval` o un `Math.random()` sin semilla
dan un resultado distinto en cada render — lo contrario del punto de la
herramienta.

**Fix**: todo dentro del timeline registrado, finito, con `paused: true`. Si
necesitás aleatoriedad (confeti, partículas), PRNG con semilla fija.

---

## MALO #9 — Prometer un MCP de HyperFrames

> "Conectá el MCP de HyperFrames y lo renderizo desde acá."

**No verificamos que exista.** La integración documentada con agentes es vía
**skills + CLI** (`npx skills add heygen-com/hyperframes`), no vía MCP.

**Fix**: si el user pregunta, decí que **hay que verificarlo** y ofrecé lo que sí
está: la CLI local. Ver `reference/hyperframes.md` §3, punto 1.

---

## MALO #10 — Inventar un límite (o negar uno)

> "HyperFrames aguanta hasta 5 minutos por composición."
> "No hay límite de clips."

Ninguna de las dos está en las fuentes. Duración máxima, cantidad máxima de
clips y tamaño máximo de fuente **no están documentados** en lo que leímos.

**Fix**: *"eso no está en la doc — habría que verificarlo"*. Y si el brief
depende de ese límite, hacé un `draft` corto de prueba antes de comprometer el
entregable.

---

## La regla que resume las diez

**Si no está en `reference/hyperframes.md`, no lo escribas como si fuera cierto.**

La sección 3 de ese archivo se llama "Verificar" justamente para esto: hay una
lista de cosas que no pudimos confirmar. Decir *"hay que verificar"* toma dos
segundos. Un render fallido en la máquina del cliente cuesta bastante más — y
cuesta credibilidad, que es lo caro.
