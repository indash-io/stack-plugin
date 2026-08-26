# Quality Checklist — Self-check antes de entregar

Corré este checklist **antes** de renderizar y **antes** de mostrar el output.
Si algo falla, arreglalo. **No entregues nada que no pase el 100% de los checks
aplicables.**

---

## Sección 1 — Proceso

- [ ] Anuncié el **modo** (`full_render` / `plan_only`) en la primera línea.
- [ ] Apliqué el **gate del conector `indash`**: si la tarea necesitaba marca,
      productos o generación y no estaba conectado, frené y lo pedí. Si avancé
      sin él, lo dije explícito.
- [ ] Leí `reference/hyperframes.md` completo antes de escribir composición.
- [ ] Heredé el contexto del cliente (`CLAUDE.md` + `assets/brand-kit/`).
- [ ] Hice **una sola pregunta consolidada** en Decisions y el user confirmó.
- [ ] **No** rendericé nada antes de esa confirmación.
- [ ] Medí la duración real de cada archivo con `ffprobe` (no la adiviné).

---

## Sección 2 — El plan de edición

- [ ] La suma de las duraciones de los cortes = `data-duration` del root, exacto.
- [ ] Ningún `data-duration` de clip supera la duración **real** del archivo.
- [ ] El corte 1 es el **hook** y ocupa 10-20% de la duración total.
- [ ] El texto del hook está visible desde el **frame 1** (animación de entrada
      ≤0.4s arrancando en `0`).
- [ ] El hook **no** es un logo, un fundido desde negro ni un plano de
      establecimiento.
- [ ] Cada corte tiene una **función declarada** y aporta una idea nueva.
- [ ] **Ninguna duración de corte es igual a la de su vecina** (mín. 0.2s de
      diferencia).
- [ ] Ningún corte de contenido baja de 0.6s ni pasa de 4s (pieza ≤15s).
- [ ] El corte del CTA dura **≥1.5s** (ideal 2.0-2.5s).
- [ ] El CTA tiene **verbo + acción concreta**, no un cierre poético ni un logo
      solo.
- [ ] Hay **una** transición primaria y **como máximo un** acento.
- [ ] La curva de audio está declarada tramo por tramo (aunque sea "sin audio").
- [ ] Si hay voz, todo lo demás está por debajo de `0.3`.
- [ ] Los planos estáticos tienen movimiento interno (push-in / pan), uno por
      corte.
- [ ] Hay una sección de **material que queda afuera**, con la razón.

---

## Sección 3 — Texto on-screen y captions

- [ ] Máximo **un** bloque de texto principal visible a la vez.
- [ ] Cada bloque tiene **≤8 palabras** y **≤2 líneas**.
- [ ] Las líneas parten por **unidad de sentido**, no por ancho de caja.
- [ ] El texto entra **con el corte** y sale con 0.2-0.3s de aire antes del
      siguiente.
- [ ] Modelo **rail + embed**: el rail carga el texto, el embed es **una**
      palabra en el clímax. Nunca dos embeds co-visibles.
- [ ] Todo el copy es **específico** (números crudos cuando los hay), sin
      marketing-speak.
- [ ] **Sin emojis** (salvo pedido explícito) y **sin exclamaciones** (salvo
      promo, máx. 1).
- [ ] **Ningún claim inventado**: todo sale del brief, la URL o el `CLAUDE.md`.
- [ ] Registro consistente (voseo si la marca es rioplatense) — sin mezclar
      voseo y tuteo.
- [ ] Si los captions son verbatim, salen del **transcript real**, no
      reescritos de memoria.
- [ ] **Una sola** animación de entrada de texto en toda la pieza.

---

## Sección 4 — Zona segura

- [ ] Ningún texto por encima del límite superior de la franja del formato.
- [ ] Ningún texto por debajo del límite inferior.
- [ ] En 9:16: nada de texto ni logo en el **15% derecho** (rail de acciones).
- [ ] El CTA está **entero** dentro de la zona segura, no a medias.
- [ ] El logo del cierre está dentro de la zona segura.
- [ ] La capa de guía visual (si la usé) **no** está en el render final.

---

## Sección 5 — Contrato de la composición

Cada uno de estos está verificado en `reference/hyperframes.md`. Un check que
falla acá es un render roto o, peor, un render que sale mal en silencio.

### 5A. Root
- [ ] `data-composition-id` presente y **==** la key de `window.__timelines`.
- [ ] `data-start="0"` en el root top-level.
- [ ] `data-width` / `data-height` en píxeles, **==** `<meta viewport>` **==**
      caja `#root` del CSS.
- [ ] `data-duration` presente y **==** el último timecode del plan.

### 5B. Clips
- [ ] Cada clip tiene **`id` estable**, `data-start` y `data-duration`.
- [ ] `class="clip"` en los clips DOM y de imagen.
- [ ] El orden de pintado se resuelve con **`z-index`**, nunca con
      `data-track-index`.
- [ ] Los timings relativos (`clip-id + N`) no forman ciclos y refieren a clips
      de la misma composición con duración conocida.

### 5C. Media
- [ ] Trim de entrada de `<video>` / `<audio>` con **`data-media-start`**
      (nunca `data-playback-start`).
- [ ] Todo `<video>` lleva `muted` + `playsinline`, salvo audio nativo
      intencional — y en ese caso declara `data-has-audio="true"`.
- [ ] **Ningún** `play()`, `pause()` ni `currentTime` en el script.
- [ ] `data-volume` dentro de rango (`0` a `3.98`).
- [ ] Todos los `src` son **rutas relativas** dentro del proyecto (ninguna URL
      remota).
- [ ] Los assets que venían por URL están **bajados a disco**.

### 5D. Animación
- [ ] **Un solo** timeline finito, creado con `{ paused: true }`.
- [ ] Registrado **sincrónicamente** en `window.__timelines[<composition-id>]`.
- [ ] El script de GSAP está cargado (si la composición usa GSAP).
- [ ] **Sin** reloj de pared (`setInterval`, `Date.now()`, `animation: infinite`).
- [ ] **Sin** random sin semilla.
- [ ] **Sin** repeticiones infinitas.

### 5E. Tipografía y audio
- [ ] La fuente de marca está **copiada al proyecto** y declarada con
      `@font-face` + **`font-display: block`**.
- [ ] Si hay JSON en atributos de audio (`data-fx-chain`, `data-automation`), va
      entre comillas dobles con las internas escapadas como `&quot;`.

### 5F. Nada inventado
- [ ] **Todo** atributo, flag y comando que escribí está en
      `reference/hyperframes.md`.
- [ ] Lo que no pude verificar lo dije como *"hay que verificar"*, no como un
      hecho.
- [ ] No prometí un MCP, un límite, un códec ni un reencuadre automático que no
      esté documentado.

---

## Sección 6 — Gates y render

- [ ] `npx hyperframes lint` corrió y **no tiene errores (`✗`)**.
- [ ] `npx hyperframes check --snapshots` corrió y **miré los PNG**.
- [ ] Los hallazgos de **contraste** se resolvieron con scrim/placa, no
      ignorándolos ni pasando `--no-contrast`.
- [ ] Los hallazgos de **layout** (overflow, clipping, oclusión) se resolvieron.
- [ ] El primer render fue `--quality draft`.
- [ ] El `high` salió **solo después** de la aprobación explícita del user.
- [ ] No pedí `--resolution` (4K) ni `--fps 60` sin que el destino los resuelva.
- [ ] Si pedí transparencia, la pieza **tiene** algo que transparentar y el
      contenedor es el correcto (MOV para editores, WebM solo para browser).

---

## Sección 7 — Sobre el render (lo que los gates NO miran)

Mirá el draft con esto en la mano. `lint` y `check` no evalúan si la pieza
retiene.

- [ ] **El primer segundo aguanta solo**, sin contexto. Si lo mirás muteado y sin
      saber de qué marca es, ¿frena?
- [ ] El ritmo **respira**: no suena a metrónomo ni a slideshow.
- [ ] No hay dos cortes seguidos que digan lo mismo.
- [ ] Las transiciones se sienten **intencionales**, no decorativas.
- [ ] Los captions se leen **mientras están en pantalla**, no un frame después.
- [ ] El audio no tapa la voz en ningún tramo.
- [ ] El CTA da tiempo de leer y reaccionar.
- [ ] La pieza **termina**, no se corta.
- [ ] Nada se ve estirado, recortado mal ni con barras no intencionales.
- [ ] Ningún frame muestra la fuente de fallback.

---

## Sección 8 — Output y persistencia

- [ ] Entregué **plan de edición + composición + comando de render**. Los tres.
- [ ] Guardé el `.md` en
      `exports/videos/<AAAA-MM-DD>_<concepto-slug>_v<N>.md`.
- [ ] El proyecto y los renders están en la subcarpeta **homónima sin `.md`**.
- [ ] **Versioné, no pisé** ningún archivo existente.
- [ ] Dije la ruta de guardado en una línea.
- [ ] Sin preámbulo, sin cierre de despedida, sin emojis.
- [ ] Cerré con la línea de ajustes.
- [ ] Si es una iteración, entregué el **diff**, no el HTML entero de nuevo.

---

## Si algo falla

| Tipo de falla | Acción |
|---|---|
| Falla en el plan (ritmo, hook, estructura) | Volvé a `instructions/04_edit_concept.md`. Es lo más barato de arreglar. |
| Falla en el contrato de composición | Volvé a `instructions/05_composition.md` y corregí el atributo. |
| Falla de zona segura o contraste | Corregí el CSS y volvé a correr `check --snapshots`. |
| Falla en un gate (`lint` / `check`) | Arreglá y volvé a correr. **No** renderices con errores de lint. |
| Falla en el render (ritmo, legibilidad) | Un cambio, objetivo absoluto, freeze del resto, nuevo draft. |
| Falla en una regla no-negociable del `SKILL.md` | **Frená** y volvé al paso del workflow donde se rompió. No entregues. |
| Escribí algo de HyperFrames que no está verificado | Sacalo o marcalo como *"verificar"*. Nunca lo dejes como afirmación. |

---

## Criterio final de "está listo"

1. Pasa **todas** las secciones aplicables.
2. Si el user corre los comandos tal cual, **sale el MP4 sin editar nada**.
3. Si mirás la pieza muteada, en un teléfono, sin saber de qué marca es:
   **frena el scroll y se entiende**.

Si dudás, mirá el draft una vez más. Si seguís dudando, falta algo.
