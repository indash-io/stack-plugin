# MALO — Captions que nadie puede leer

Marca anonimizada. Categoría: bebidas. Pieza 9:16 para Reels, con voiceover.

El corte estaba bien. Los captions la arruinaron.

---

## Lo que se entregó

```html
<div id="caps" class="clip" data-start="0" data-duration="14" data-track-index="5">
  <p class="cap">Probamos la fórmula durante seis meses en tres ciudades distintas
     hasta encontrar el punto exacto de carbonatación que buscábamos</p>
</div>
```
```css
.cap {
  position: absolute; bottom: 90px; left: 20px; right: 20px;
  font-family: "Bebas Neue", sans-serif;
  font-size: 96px; color: #FFFFFF;
}
```

---

## MALO #1 — Texto pegado al borde inferior en 9:16

`bottom: 90px` en una composición de 1920px de alto: el caption vive en el 5%
inferior, **exactamente** donde Instagram dibuja el caption del post, el CTA y
la barra de navegación.

El caption existe en el MP4 y no existe en el teléfono.

**Fix**: en 9:16, nada de texto por debajo de `y = 1500px` (78% del alto). Con
las variables de `style/safe_zones.md`: `bottom: var(--safe-bottom)` con
`--safe-bottom: 420px`.

---

## MALO #2 — El rail se mete en el rail de acciones

`right: 20px`. El 15% derecho del cuadro (los últimos 162px) está ocupado por
like, comentar, compartir y el disco del sonido. Las últimas palabras de cada
línea quedan debajo de los iconos.

**Fix**: `right: var(--safe-right)` con `--safe-right: 162px`.

---

## MALO #3 — Un párrafo entero como un solo bloque

24 palabras en un caption. A `font-size: 96px` eso son cinco o seis líneas que
tapan medio cuadro y se muestran 14 segundos seguidos, sin sincronía con lo que
se dice.

**Fix**: modelo **rail + embed**. El rail se parte en bloques de ≤8 palabras,
cada uno con su `data-start` y `data-duration` sincronizados con la voz. Máximo
dos líneas por bloque.

Y la partición va **por unidad de sentido**: `"Probamos la fórmula" / "durante
seis meses"`, no `"Probamos la fórmula durante seis" / "meses"`.

---

## MALO #4 — Blanco puro sobre video, sin scrim

`color: #FFFFFF` y nada más. El clip pasa por un plano de la lata contra un
cielo blanco: durante un segundo y medio el caption desaparece por completo y
después vuelve.

**Fix**: scrim con degradado detrás del texto (la solución default), o placa
sólida si la pieza es más gráfica. La sombra sola es refuerzo, no defensa.

Y verificalo: `npx hyperframes check --snapshots` audita contraste WCAG AA en
cada muestra. Acá lo habría cazado.

Ver `style/captions_typography.md` §4.

---

## MALO #5 — Tipografía display a 1.8s de exposición

`Bebas Neue` — condensada, alta, todo en mayúsculas por diseño. A 96px y con
cinco líneas, es una masa de trazos verticales. Se adivina, no se lee.

**Fix**: sans geométrica de peso alto para captions de video. Y si la marca
tiene fuente propia, **esa**, desde `library/fonts/`, no un parecido de Google
Fonts.

---

## MALO #6 — La fuente ni siquiera está en el proyecto

`font-family: "Bebas Neue"` sin `@font-face` y sin el archivo en `assets/`.
En la máquina del editor estaba instalada; en el render de otra máquina cae al
fallback del sistema. Dos renders, dos tipografías.

**Fix**:

```css
@font-face {
  font-family: "MarcaSans";
  src: url("./assets/Marca-Bold.woff2") format("woff2");
  font-weight: 700;
  font-display: block;
}
```

`font-display: block` es obligatorio: sin eso, el render puede capturar frames
con la fuente de fallback aunque el archivo esté.

---

## MALO #7 — `data-track-index` usado como capa

`data-track-index="5"` para "poner los captions arriba del video". No hace eso.
Es la fila que dibuja Studio: **el render lo ignora** y no impide overlap. El
orden de pintado real quedó librado al orden del DOM.

**Fix**: `z-index` en CSS. Siempre.

Ver `reference/hyperframes.md` §1.3 — la doc lo dice explícito: "Tracks are not
layers".

---

## MALO #8 — Un solo clip de caption para toda la pieza

`data-start="0" data-duration="14"`: el mismo bloque de texto encendido de punta
a punta. No hay sincronía con la voz, no hay aire, no hay ritmo de lectura.

**Fix**: un clip DOM por bloque de rail, con su `data-start` / `data-duration`,
0.2-0.3s de aire entre que uno sale y entra el siguiente.

---

## MALO #9 — Cero embeds… y en la versión siguiente, todos

La corrección apresurada fue promover **cada** bloque a embed gigante detrás del
sujeto. Pasó de ilegible a agotador: la doc de HyperFrames marca eso como el
error más común que el flujo de captions previene.

**Fix**: el rail carga el texto; el embed es **una** palabra, en el clímax.
Aproximadamente uno por beat, nunca dos co-visibles, un ápice por pieza.

---

## MALO #10 — Copy que no es lo que se dice

El caption está reescrito "para que quede mejor" y no coincide con el audio.
Alguien que mira con sonido escucha una cosa y lee otra.

**Fix**: si el caption es verbatim, **es verbatim** — transcribilo con
`npx hyperframes transcribe --language es` en vez de reescribirlo de memoria. Si
querés texto editorial distinto del audio, entonces no son captions: son textos
on-screen, y no van sincronizados palabra por palabra.

---

## La versión arreglada

```html
<div id="rail-01" class="clip layer-text" data-start="0.2" data-duration="2.6">
  <p class="caption-rail">Seis meses de pruebas</p>
</div>
<div id="rail-02" class="clip layer-text" data-start="3.0" data-duration="2.4">
  <p class="caption-rail">en <em>tres ciudades</em></p>
</div>
<div id="embed-01" class="clip layer-text" data-start="5.8" data-duration="1.6">
  <p class="caption-embed">EL PUNTO EXACTO</p>
</div>
```
```css
.caption-rail {
  position: absolute;
  left: var(--safe-x); right: var(--safe-right);
  bottom: var(--safe-bottom);
  font-family: "MarcaSans", system-ui, sans-serif;
  font-size: 64px; font-weight: 700; line-height: 1.25;
  color: var(--papel);
}
.caption-rail em { font-style: normal; color: var(--acento); }
.layer-text { z-index: 3; }
.layer-scrim { z-index: 2; }
```

Tres bloques en vez de un párrafo, dentro de zona segura, con scrim detrás,
tipografía de marca embebida, `z-index` para el orden y **un** embed que se lo
gana.
