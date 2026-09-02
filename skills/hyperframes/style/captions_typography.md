# Style — Captions y tipografía on-screen

Un caption que no se lee no existe. Todo lo de acá está al servicio de eso.

**Dónde** va el texto es otro archivo: `style/safe_zones.md`.

---

## 1. Rail + embed: el modelo

Es el modelo que documenta HyperFrames para captions
(`reference/hyperframes.md` §1.5) y sirve igual para texto on-screen sin voz:

- **Rail** — el rótulo legible que carga el texto. Es el default y lleva la
  mayoría de las palabras.
- **Embed** — la excepción ganada: **una** palabra grande, en el clímax, tratada
  como gráfica (matteada detrás del sujeto, o a pantalla completa).

Regla dura: **el embed es escaso.** Aproximadamente uno por beat, nunca dos
visibles a la vez, como máximo un ápice en toda la pieza. Embeber el transcript
entero es el error más común y el que más rápido arruina una pieza.

---

## 2. Jerarquía tipográfica

| Rol | Tamaño (sobre 1920px de alto) | Peso | Cuándo |
|---|---|---|---|
| **Hook** | 90–120px | Bold / Black | El texto del primer corte |
| **Rail** (caption verbatim) | 54–72px | Medium / Semibold | Mientras alguien habla |
| **Texto de bloque** | 64–84px | Semibold / Bold | Un concepto por corte, sin voz |
| **Embed** (clímax) | 160–260px | Black | Una palabra, una vez |
| **Legal / disclaimer** | 28–34px | Regular | Solo si la marca lo exige |
| **CTA** | 72–96px | Bold | El cierre |

Escalá proporcionalmente para otros formatos: en 1080×1350 (4:5) multiplicá por
~0.70; en 1080×1080 (1:1) por ~0.56; en 1920×1080 (16:9) por ~0.56.

**Todo en `px` absolutos**, calculados sobre las dimensiones del root. La
composición tiene tamaño fijo: no hay responsive que resolver, y un `vw` se
comporta distinto en preview y en render según la ventana.

---

## 3. La fuente es la de la marca

```css
@font-face {
  font-family: "MarcaSans";
  src: url("./assets/Marca-Bold.ttf") format("truetype");
  font-weight: 700;
  font-display: block;
}
```

- Copiá el archivo real desde `library/fonts/` del proyecto al proyecto.
- **`font-display: block`** es obligatorio: sin eso, el render puede capturar
  frames con la fuente de fallback y la pieza sale con dos tipografías.
- Declará un stack de fallback razonable igual (`system-ui, sans-serif`), pero
  **no** uses "un parecido de Google Fonts" como reemplazo de la fuente de
  marca. Eso es un error de marca, no un atajo.
- Si el cliente no tiene fuente propia: una sans geométrica de peso alto para
  captions de video. No experimentes con display extremas — a 1.8 segundos de
  exposición no se leen.

---

## 4. Legibilidad: el fondo siempre compite

El video de atrás cambia frame a frame. Un caption blanco sobre un cielo blanco
desaparece medio segundo. Tres soluciones, en orden de preferencia:

**A — Scrim (gradiente):** el default. Una franja con degradado detrás del texto.

```css
.caption-rail::before {
  content: "";
  position: absolute; inset: -40px -60px;
  background: linear-gradient(to top, rgba(0,0,0,.72), rgba(0,0,0,0));
  z-index: -1;
}
```

**B — Placa sólida:** una caja de color de marca detrás del texto. Más gráfica,
menos cinematográfica. Buena para datos y precios.

**C — Sombra / stroke:** `text-shadow: 0 2px 12px rgba(0,0,0,.6)` o un borde
fino. Es la más discreta y la más frágil: sirve como refuerzo, no como única
defensa.

**Nunca** confíes en que "el fondo de ese clip es oscuro". Cambia en 2 segundos.

**Verificalo**, no lo supongas: `npx hyperframes check --snapshots` audita
contraste WCAG AA en cada muestra. Si tira contraste bajo, **metele scrim** — no
subas el tamaño, que solo hace más grande el problema.

---

## 5. Reglas de escritura del texto on-screen

1. **Máximo 6-8 palabras** por bloque.
2. **Un solo bloque de texto principal visible a la vez.** Dos compitiendo =
   ninguno se lee.
3. **Específico o nada.** *"Se absorbe en 30 segundos"* ✅ · *"Descubrí la
   diferencia"* ❌ · *"Level up tu rutina"* ❌.
4. **Números crudos** cuando los haya. Los números frenan el scroll.
5. **Sin emojis**, salvo pedido explícito del user.
6. **Sin signos de exclamación**, salvo pieza de promo y como máximo uno.
7. **CTA con verbo + acción concreta**: *"Pedilo en el link"*, no *"Gracias por
   mirar"*.
8. **Nunca inventes un claim.** Si no está en las `notes` del plan, en los
   guiones (`meta.video.script`), en `library/brand/brand.md` o en
   `library/products/products.md`, no va on-screen.
9. **Voseo** si la marca es rioplatense y `brand.md` no dice otra cosa.
   Nunca mezclar voseo y tuteo en la misma pieza.

---

## 6. Cortar el rail: dónde parte una línea

Cuando el rail lleva una frase larga, partila **por unidad de sentido**, no por
ancho de caja:

- ✅ `"Se absorbe" / "en 30 segundos"`
- ❌ `"Se absorbe en 30" / "segundos"`

Máximo **dos líneas** por bloque de rail. Tres líneas ya son un párrafo y nadie
lee párrafos en un reel.

`interlineado 1.1–1.2` para títulos grandes, `1.25–1.35` para el rail.

---

## 7. Animación del texto

Toda la animación vive en el timeline de GSAP registrado (nunca en `@keyframes`
con reloj de pared). Ver `instructions/05_composition.md` §5.

| Momento | Duración | Ease | Movimiento |
|---|---|---|---|
| Entrada | 0.25–0.4s | `power3.out` | `y: 40 → 0`, `opacity: 0 → 1` |
| Salida | 0.15–0.25s | `power2.in` | `opacity: 1 → 0` (sin movimiento) |
| Palabra activa (rail) | 0.1s | `none` | cambio de color, sin desplazamiento |
| Embed (clímax) | 0.35s | `power4.out` | `scale: 0.92 → 1`, `opacity: 0 → 1` |

- La entrada del texto **arranca con el corte**, no 0.5s después.
- La salida termina **antes** del corte siguiente, con 0.2-0.3s de aire.
- **Un solo tipo de animación de texto en toda la pieza.** Un fade acá, un slide
  allá y un typewriter en el CTA se lee como plantilla, no como diseño.

---

## 8. Highlight de palabra clave

En el rail, una palabra puede llevar énfasis inline (color de acento) sin salir
del rail. Es la forma barata de dirigir la atención sin promover a embed.

```html
<p>Se absorbe en <em>30 segundos</em></p>
```
```css
.caption-rail em { font-style: normal; color: var(--acento); }
```

**Una palabra por línea como máximo.** Si todo está destacado, nada lo está.

---

## 9. Anti-patrones

| Anti-patrón | Por qué falla |
|---|---|
| Caption verbatim de todo, en embed gigante | Ilegible y agotador; es el error #1 |
| Texto pegado al borde inferior en 9:16 | Lo tapa la UI de la plataforma |
| Dos bloques de texto simultáneos | Compiten, no se lee ninguno |
| Fuente de fallback en algunos frames | Falta `font-display: block` |
| Blanco puro sobre video claro sin scrim | Desaparece medio segundo y vuelve |
| Tres animaciones de entrada distintas | Plantilla, no diseño |
| Texto que entra a mitad del corte | Se pierde la mitad del tiempo de lectura |
| Display extrema a 1.8s de exposición | No se lee, se adivina |

Casos desarrollados en `examples/bad/captions_ilegibles.md`.
