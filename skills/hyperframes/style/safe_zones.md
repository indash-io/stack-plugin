# Style — Zonas seguras por plataforma

La UI de cada plataforma se dibuja **encima** de tu video. Lo que cae debajo de
esa UI no existe.

> **Estado de estos números.** Son los canónicos 2026 del stack: Meta unificó
> la zona segura 9:16 de Stories y Reels en marzo 2026 (top 14%, sides 6%;
> bottom 20% en Stories y 35% en Reels — el bottom es la única diferencia), y
> la grilla de perfil de Instagram es 3:4 desde fines de 2025. **No** salen de
> la documentación de HyperFrames. Las plataformas cambian su UI sin avisar:
> tratalos como **margen conservador** y verificá contra el spec vigente cuando
> la pieza sea un entregable pago crítico.

---

## 1. La regla general

**Todo texto, logo y elemento accionable vive dentro de la zona segura del
formato.** Lo que salga de ahí, que sea **imagen**, no información.

Y la regla de oro del 9:16: una pieza que va a Stories **y** Reels se compone
contra la zona de **Reels** (la estricta). Si es solo Story, ganás 290px de
alto útil abajo.

---

## 2. Por formato

### 9:16 — 1080×1920 (Reels, TikTok, Stories, Shorts)

El más agresivo, y por eso el que se autora primero cuando hay varios formatos.

**Reels (el default para video):**

| Franja | Píxeles | Qué la ocupa |
|---|---|---|
| Superior | 0 – 270px (14%) | Avatar, nombre de cuenta, "Sponsored" |
| **Zona segura** | **270 – 1250px** | Tu contenido |
| Inferior | últimos 670px (35%) | Caption del post, audio, CTA de la plataforma, navegación |
| Lateral derecho | últimos 120px del ancho | Rail de acciones (like, comentar, compartir, sonido) |
| Lateral izquierdo | primeros 65px | Margen de respiración |

**Stories (solo si la pieza NO va a Reels):**

| Franja | Píxeles |
|---|---|
| Superior | 0 – 270px |
| **Zona segura** | **270 – 1540px** |
| Inferior | últimos 380px (20%) — input de respuesta, CTA, stickers |
| Laterales | 65px por lado |

**Consecuencias prácticas:**
- En Reels el texto no baja de **y = 1250px**. Un caption "en el tercio
  inferior" es un caption tapado.
- El **lateral derecho** también está ocupado: no metas texto ni el logo ahí.
  El área realmente libre en Reels es aproximadamente `x: 65–960px`,
  `y: 270–1250px`.
- El sujeto puede ocupar todo el cuadro. Es el **texto** el que se corre.
- En Stories, la franja inferior además recibe stickers (link, encuesta):
  dejala limpia.

### 4:5 — 1080×1350 (feed de Instagram, video en feed)

| Franja | Píxeles | Por qué |
|---|---|---|
| Superior / inferior | 64px | Respiración — la UI vive fuera del cuadro |
| **Laterales** | **100px por lado** | La grilla de perfil recorta a 3:4 (~34px por lado) + respiración |

El 4:5 es el formato más generoso, pero desde que la grilla de perfil es 3:4,
un texto pegado al borde lateral desaparece en el thumbnail del perfil.

### 1:1 — 1080×1080 (Meta ads, placement mixto)

| Franja | Píxeles | Por qué |
|---|---|---|
| Superior / inferior | 64px | Respiración |
| **Laterales** | **140px por lado** | La grilla 3:4 recorta ~135px por lado de un cuadrado |

Ojo con el **placement mixto**: un ad 1:1 puede aparecer recortado a 4:5 en
feed y con overlay en Stories/Reels. Si el ad va a varios placements, componé
el texto dentro del **centro del 70%** y no lo pegues a ningún borde.

### 16:9 — 1920×1080 (YouTube, landing, desktop)

| Franja | Píxeles | Qué la ocupa |
|---|---|---|
| Inferior | últimos 120px | Controles del player, barra de progreso, subtítulos del player |
| Esquina inf. der. | ~250×80px | Botón de "ver más tarde" / marca de agua del canal |
| **Zona segura** | 5% de margen en los cuatro lados | Tu contenido |

Convención clásica de broadcast, que sigue funcionando: **title safe = 90%
central**, **action safe = 93% central**.

---

## 3. Cómo se implementa en la composición

Definí la zona segura como variables CSS del root y colgá todo el texto de ahí.
Para 9:16 con destino Reels (el default):

```css
:root {
  --safe-top: 270px;      /* 14% de 1920 */
  --safe-bottom: 670px;   /* 35% — Reels; para Story-only: 380px */
  --safe-x: 65px;
  --safe-right: 120px;    /* rail de acciones de Reels */
}

.caption-rail {
  position: absolute;
  left: var(--safe-x);
  right: var(--safe-right);
  bottom: var(--safe-bottom);
}

.hook-text {
  position: absolute;
  left: var(--safe-x);
  right: var(--safe-right);
  top: calc(var(--safe-top) + 80px);
}
```

Cambiar de formato pasa a ser **cambiar cuatro variables** más el
`data-width`/`data-height` del root, en vez de reposicionar cada elemento.

---

## 4. Verificalo, no lo supongas

```bash
npx hyperframes check --snapshots
```

`check` audita layout (overflow, clipping, oclusión) y guarda los frames en
`snapshots/`. **Mirá esos PNG con la zona segura en la cabeza.** Es el único
control real de que el texto quedó donde tenía que quedar.

Truco durante la autoría: una capa de guía visible solo en preview.

```html
<div id="safe-guide" class="clip" data-start="0" data-duration="12"></div>
```
```css
#safe-guide {
  z-index: 999; pointer-events: none;
  border-top: var(--safe-top) solid rgba(255,0,0,.18);
  border-bottom: var(--safe-bottom) solid rgba(255,0,0,.18);
  border-right: var(--safe-right) solid rgba(255,0,0,.18);
}
```

**Sacala (o borrá el elemento) antes del render final.** Un render con la guía
adentro es un render tirado.

---

## 5. Recorte entre formatos

Cuando el mismo corte sale en 9:16 y en 4:5, el material se reencuadra y el
texto se recoloca. Dos reglas:

1. **Componé primero el formato más restrictivo** (9:16 Reels) y derivá los
   otros. Al revés, el texto siempre queda fuera de zona.
2. **El sujeto vive en el centro.** Si el sujeto está a un tercio del cuadro en
   16:9, al pasar a 9:16 con `object-fit: cover` se pierde. Corregilo con
   `object-position`, no reencuadrando a ojo en el render.

---

## 6. Checklist de zona segura

- [ ] Ningún texto por encima del límite superior de la franja.
- [ ] Ningún texto por debajo del límite inferior (**Reels: y = 1250px**).
- [ ] En 9:16: nada de texto ni logo en los últimos **120px** del ancho (rail).
- [ ] En 4:5 y 1:1: nada de texto en la franja lateral que se come la grilla 3:4.
- [ ] El CTA está **entero** dentro de la zona segura, no a medias.
- [ ] El logo del cierre está dentro de la zona segura.
- [ ] Los `snapshots/` de `check` se miraron de verdad.
- [ ] La capa de guía **no** está en el render final.
