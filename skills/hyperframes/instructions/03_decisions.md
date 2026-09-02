# 03 — Decisions

Acá rompés el silencio del Discovery con **una sola pregunta consolidada**. El
user confirma o edita. **Siempre se confirma antes de renderizar. No
negociable.**

---

## La regla del "una sola pregunta"

Nada de preguntas en serie ("¿qué formato?" → responde → "¿cuántos segundos?" →
responde → "¿qué transición?"). Una propuesta completa, con razones cortas, que
se lee en 20 segundos y se contesta de una.

---

## Estructura exacta de la pregunta consolidada

```markdown
Modo: [full_render / plan_only]

Ya revisé el material y la marca. Te tiro el plan de edición:

**Material disponible**

| # | Archivo | Dur. | Res. | Audio | Qué es | Entra |
|---|---|---|---|---|---|---|
| 1 | shot-01.mp4 | 6.0s | 1080×1920 | no | [qué muestra] | ✅ hook |
| 2 | shot-02.mp4 | 8.0s | 1080×1920 | sí | [qué muestra] | ✅ desarrollo |
| 3 | shot-03.mp4 | 5.0s | 1920×1080 | no | [qué muestra] | ⚠️ formato distinto |
| 4 | packshot.png | — | 1080×1350 | — | [qué muestra] | ✅ cierre |

**Mi propuesta**
- **Formato**: [9:16 1080×1920 / 4:5 1080×1350 / 1:1 1080×1080 / 16:9 1920×1080] — [razón: plataforma de destino]
- **Duración**: [N]s — [razón: qué pide la plataforma + cuánto material hay]
- **Estructura**: [N] cortes — hook [0–Xs] → [desarrollo] → [payoff] → [CTA]
- **Hook**: [qué se ve en el primer segundo, en una línea]
- **Transición primaria**: `[bloque]` a [X]s — [razón: energía de la pieza]
- **Acento** (1 solo): `[bloque]` en [dónde] — [razón]
- **Captions**: [rail `anchor` / sin captions / kinetic] — [razón]
- **Tipografía**: [familia real de `library/fonts/`] · **Paleta**: [hex de `library/brand/brand.md`]
- **Audio**: [música + VO / música sola / audio nativo del clip N / sin audio] — [razón]
- **Encuadre del clip 3** (formato distinto): [cover recortando los laterales / fondo desenfocado + clip centrado / queda afuera] — [razón]
- **Render**: `draft` primero para que lo veas, `high` solo cuando lo apruebes

**Queda afuera**: [archivo] — [razón en media línea]

¿Avanzo así o cambiás algo?
```

Si algo del material no se pudo identificar, agregá una línea:

> El clip 3 no lo pude identificar (el guion del manifiesto no alcanza). ¿Qué muestra? Según
> eso lo ubico o lo dejo afuera.

---

## Cómo elegís cada default

### Formato

| Destino | Formato | Píxeles |
|---|---|---|
| Reels / TikTok / Stories / Shorts | **9:16** | 1080×1920 |
| Feed de Instagram (video) | **4:5** | 1080×1350 |
| Meta ads placement mixto | **1:1** | 1080×1080 |
| YouTube / landing / desktop | **16:9** | 1920×1080 |

Default si el user no dijo nada y el material es vertical: **9:16**. Si el
material es horizontal y no hay señal de plataforma: **16:9**.

**Si el user pide dos formatos**: son **dos composiciones**, no un flag de
render. Decilo explícito y proponé cuál se autora primero (el más restrictivo en
zona segura: 9:16). Ver regla 7 del `SKILL.md`.

### Duración

| Pieza | Rango | Default |
|---|---|---|
| Reel / TikTok orgánico | 7–20s | **12s** |
| Meta ad (performance) | 6–15s | **10s** |
| Story individual | 5–15s | **8s** |
| Brand film corto | 20–45s | **30s** |

Clampealo a lo que el material aguanta: `duración total del material útil ×
0.8` es un techo realista si no hay imágenes fijas para estirar.

### Estructura

Default de 4 bloques, ajustando el reparto según la duración
(`style/pacing.md` tiene la tabla completa):

1. **Hook** (0 → 1.5-3s) — el plano más fuerte, sin logo, sin fundido.
2. **Desarrollo** (2-3 cortes) — el producto en uso, el beneficio, la prueba.
3. **Payoff** — el resultado o el momento de mayor contraste.
4. **CTA** (últimos 1.5-2.5s) — packshot + texto accionable + logo.

### Transición primaria

Elegí **una** según la energía de la pieza, con el mapa de
`reference/hyperframes.md` §1.4:

| Energía de la pieza | Default |
|---|---|
| Calma (wellness, lujo, brand story) | `transitions-blur` (CSS) o `cross-warp-morph` (shader) |
| Media (SaaS, explainer, demo) | `transitions-push` (CSS) o `whip-pan` (shader) |
| Alta (promo, drop, performance ad) | `transitions-scale` (CSS) o `flash-through-white` (shader) |

**Default seguro si dudás: corte seco con un `transitions-dissolve` de 0.25s.**
Las CSS son más baratas y cubren el 60-70% de los cambios de escena ordinarios;
guardá una shader para el momento que de verdad importa.

Regla dura: **una primaria + máximo un acento**. Nunca una por corte.

### Captions

| Situación | Default |
|---|---|
| Hay voiceover o alguien habla en cámara | Rail `anchor` (verbatim, legible) + **un** embed en la palabra más fuerte |
| No hay voz, la pieza es visual | Sin captions; 2-4 textos on-screen cortos, uno por bloque |
| Pieza para feed (se mira sin sonido) | Texto on-screen **obligatorio**, aunque no haya voz |

Detalle tipográfico en `style/captions_typography.md`. Posición en
`style/safe_zones.md`.

### Audio

| Situación | Default |
|---|---|
| Hay VO grabado o guion | VO al frente (`data-volume: 1`) + cama de música a `0.15-0.25` |
| No hay VO | Música sola a `0.6-0.8` |
| El clip tiene audio nativo bueno (UGC, ambiente) | Audio nativo (`data-has-audio="true"`) + música muy baja o nada |
| El user no tiene música | **Decilo**: la pieza sale sin música y se puede sumar después. No inventes un archivo que no existe. |

`npx hyperframes tts` genera un VO local (soporta locale `es`) — **proponelo,
no lo ejecutes sin confirmar**: es una decisión creativa, no técnica.

### Encuadre de clips con formato distinto

Tres opciones válidas, y proponés una:

1. **Cover** (`object-fit: cover`) — recorta los laterales. Default cuando el
   sujeto está centrado.
2. **Fondo desenfocado** — el mismo clip escalado y con `filter: blur()` de
   fondo, el clip real centrado arriba. Default cuando el sujeto se pierde al
   recortar.
3. **Afuera** — si ninguna de las dos lo salva sin romper el ritmo.

---

## Cómo manejás la respuesta del user

**A — "dale, avanzá"** → directo a `instructions/04_edit_concept.md`.

**B — pide cambios concretos** → aplicalos, confirmá en una línea, avanzá. **No
hagas otra ronda de propuesta.**

> Listo: 15s en vez de 12, transición `whip-pan`, sin captions. Avanzo al plan.

**C — duda o pide opinión** → recomendá **una** dirección con razón breve y pedí
confirmación final. No abras un menú de opciones.

**D — pide algo que rompe una regla** (por ejemplo una transición distinta por
corte, o texto pegado al borde inferior en 9:16) → explicá por qué no en una
línea y ofrecé la alternativa:

> Una transición distinta por corte se lee como caos. Te propongo `whip-pan`
> como primaria y `flash-through-white` solo en el payoff — así el acento
> significa algo.

**E — pide dos formatos** → confirmá que son dos composiciones y cuál va
primero. El segundo se deriva del primero reencuadrando, no re-planificando.

**F — no responde algún punto** → avanzás con tu default. **No vuelvas a
preguntar.** Que no lo haya cambiado es confirmación.

---

## Lo que NO hacés en Decisions

- ❌ No hagas preguntas en serie.
- ❌ No ofrezcas "3 opciones para que elijas". Una propuesta sólida con razón.
- ❌ No empieces a escribir composición antes de la confirmación.
- ❌ No saltees Decisions porque "el user ya pasó todo". Aunque lo haya pasado,
  hacés el resumen del plan y pedís OK.
- ❌ No cambies el formato de la pregunta. Es siempre el mismo bloque.
- ❌ No renderices nada — ni un draft — antes del OK.

---

## Salida de este paso

El user confirmó (o editó) formato, duración, estructura, hook, transiciones,
captions, audio y encuadres.

→ Pasá a `instructions/04_edit_concept.md`.
