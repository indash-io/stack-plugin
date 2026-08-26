# Style — Zonas seguras por plataforma

La UI de cada plataforma se dibuja **encima** de tu video. Lo que cae debajo de
esa UI no existe.

> **Estado de estos números.** Son la convención operativa del stack — la misma
> base que usa `stories-nano-banana` (zona segura vertical 14%–85%), extendida a
> Reels, TikTok y ads. **No** salen de la documentación de HyperFrames: son del
> oficio. Las plataformas cambian su UI sin avisar, así que tratalos como
> **margen conservador**, no como spec, y **verificá** contra el spec vigente de
> la plataforma cuando la pieza sea un entregable pago crítico.

---

## 1. La regla general

**Todo texto, logo y elemento accionable vive en el 70% central del cuadro.**
El 15% de arriba y el 15% de abajo son territorio de la plataforma.

Si algo tiene que salir del 70% central, que sea **imagen**, no información.

---

## 2. Por formato

### 9:16 — 1080×1920 (Reels, TikTok, Stories, Shorts)

El más agresivo, y por eso el que se autora primero cuando hay varios formatos.

| Franja | % del alto | Píxeles | Qué la ocupa |
|---|---|---|---|
| Superior | 0 – 14% | 0 – 270px | Avatar, nombre de cuenta, "Sponsored", barra de progreso de Stories |
| **Zona segura** | **14 – 78%** | **270 – 1500px** | Tu contenido |
| Inferior | 78 – 100% | 1500 – 1920px | Caption del post, CTA de la plataforma, barra de navegación, input de respuesta |
| Lateral derecho | últimos 15% del ancho | 918 – 1080px | Rail de acciones (like, comentar, compartir, sonido) |

**Consecuencias prácticas:**
- El texto no baja de **y = 1500px**. Un caption "en el tercio inferior" en
  video vertical es un caption tapado.
- El **lateral derecho** también está ocupado: no metas texto ni el logo ahí.
  El área realmente libre es aproximadamente `x: 60–918px`, `y: 270–1500px`.
- El sujeto puede ocupar todo el cuadro. Es el **texto** el que se corre.
- En Stories, la franja inferior además recibe stickers (link, encuesta):
  dejala limpia.

### 4:5 — 1080×1350 (feed de Instagram, video en feed)

| Franja | % del alto | Píxeles | Qué la ocupa |
|---|---|---|---|
| Superior | 0 – 8% | 0 – 108px | Poco: header del post, arriba del cuadro |
| **Zona segura** | **8 – 88%** | **108 – 1190px** | Tu contenido |
| Inferior | 88 – 100% | 1190 – 1350px | Barra de acciones y caption, justo debajo |

El 4:5 es el formato **más generoso**: la UI vive mayormente fuera del cuadro.
Aun así dejá margen: el crop del preview en grilla es cuadrado y recorta arriba
y abajo.

### 1:1 — 1080×1080 (Meta ads, placement mixto)

| Franja | % del alto | Píxeles |
|---|---|---|
| Superior | 0 – 10% | 0 – 108px |
| **Zona segura** | **10 – 90%** | **108 – 972px** |
| Inferior | 90 – 100% | 972 – 1080px |

Ojo con el **placement mixto**: un ad 1:1 puede aparecer recortado a 4:5 en feed
y con overlay en Stories. Si el ad va a varios placements, componé el texto
dentro del **centro cuadrado del 80%** y no lo pegues a ningún borde.

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

Definí la zona segura como variables CSS del root y colgá todo el texto de ahí:

```css
:root {
  --safe-top: 270px;      /* 14% de 1920 */
  --safe-bottom: 420px;   /* 22% de 1920 → el texto no pasa de y=1500 */
  --safe-x: 60px;
  --safe-right: 162px;    /* 15% de 1080: el rail de acciones */
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

1. **Componé primero el formato más restrictivo** (9:16) y derivá los otros. Al
   revés, el texto siempre queda fuera de zona.
2. **El sujeto vive en el centro.** Si el sujeto está a un tercio del cuadro en
   16:9, al pasar a 9:16 con `object-fit: cover` se pierde. Corregilo con
   `object-position`, no reencuadrando a ojo en el render.

---

## 6. Checklist de zona segura

- [ ] Ningún texto por encima del límite superior de la franja.
- [ ] Ningún texto por debajo del límite inferior.
- [ ] En 9:16: nada de texto ni logo en el 15% derecho (rail de acciones).
- [ ] El CTA está **entero** dentro de la zona segura, no a medias.
- [ ] El logo del cierre está dentro de la zona segura.
- [ ] Los `snapshots/` de `check` se miraron de verdad.
- [ ] La capa de guía **no** está en el render final.
