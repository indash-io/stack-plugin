# 01 — Intake

Acá validás que haya con qué editar. **Esta skill no genera material: lo
ensambla.** Si no hay material, no hay pieza.

---

## Lo que necesitás sí o sí

| Input | Por qué | Si falta |
|---|---|---|
| **Material** — clips, imágenes, frames, audio (rutas locales o URLs) | Es lo que vas a editar | **Frená y pedilo.** No inventes planos. |
| **Plataforma de destino** — IG Reels, TikTok, feed 4:5, Meta ads, YouTube | Define aspect ratio, zona segura y duración | Proponé el default y confirmalo en Decisions |
| **Duración objetivo** | Define cuántos cortes entran | Proponé según plataforma (`style/pacing.md`) |

## Lo que proponés vos (no lo preguntes suelto)

Todo esto va junto en la **única pregunta consolidada** del paso 3, con un
default ya elegido y su razón en una línea:

- estructura del corte (cuántos segmentos y qué hace cada uno)
- transición primaria
- estilo de captions (o si no lleva)
- audio: música, voiceover, audio nativo de los clips, o silencio
- qué material entra y qué queda afuera

---

## Cómo llega el material (tres casos)

### Caso A — el user trabaja dentro de una carpeta de cliente

El caso normal del stack. El material ya está en `exports/`:

```
<cliente>/exports/videos/2026-08-20_solar-04-demo_v1/
<cliente>/exports/carruseles/2026-08-18_solar-04_v1/
<cliente>/assets/logos/  <cliente>/assets/fonts/
```

No preguntes qué hay: **andá a mirar** (paso 2, Discovery) y después mostrale el
inventario en Decisions.

### Caso B — el user pasa rutas o URLs sueltas

Aceptalas. Si son URLs (típico: lo que devuelve `generate_video` del MCP de
Indash), **bajalas a disco antes de componer** — una URL que expira rompe el
render, y el proyecto tiene que ser reproducible.

```bash
mkdir -p <proyecto>/assets
curl -L -o <proyecto>/assets/shot-01.mp4 "<url>"
```

### Caso C — el material todavía no existe

El user pide "editame un reel de X" y no hay clips. **No es esta skill.**
Decilo en una línea y derivá:

> Todavía no hay material para editar. Para generar los clips es `all-videos`
> (o `ugc-generator` si es UGC de producto). Cuando estén en `exports/videos/`,
> vuelvo y armo el corte.

**No** empieces a escribir una composición con placeholders que el user va a
tener que rellenar. Eso no es un entregable.

---

## Preguntas que SÍ hacés en Intake (máximo 2, y solo si falta lo crítico)

- *"¿Dónde está el material? ¿En `exports/` del cliente o me pasás las rutas?"*
- *"¿Para qué plataforma? (Reels 9:16, feed 4:5, Meta ads, YouTube 16:9)"*

Nada más. El resto se consolida en el paso 3.

## Preguntas que NO hacés acá

- ❌ "¿Qué transición querés?" → va en Decisions, con default.
- ❌ "¿Querés captions?" → va en Decisions, con default.
- ❌ "¿Qué música?" → va en Decisions, con default.
- ❌ "¿Cuántos cortes?" → lo decidís vos en el plan de edición.

---

## Señales de que el brief está incompleto de verdad

Frená y pedí si pasa alguna:

1. No hay ni una ruta ni una URL de material.
2. El user pide "el mismo video pero en otro formato" y no está claro **cuál**
   video (más de un candidato en `exports/`).
3. El user pide captions de un voiceover que no existe como archivo ni como
   texto.
4. El user pide una duración imposible para el material que hay (por ejemplo 30s
   de pieza con 6s de material total y sin imágenes fijas para estirar).

En los cuatro casos: **una sola intervención**, concreta, con la opción más
razonable propuesta.

---

## Salida de este paso

Tenés identificado:
- de dónde sale el material,
- la plataforma de destino (aunque sea la propuesta por default),
- si hay carpeta de cliente y `CLAUDE.md` de marca.

→ Pasá a `instructions/02_discovery.md`. **En silencio.**
