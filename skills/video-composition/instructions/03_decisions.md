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
| 1 | clips/clip-01-v2.mp4 | 10.0s | 1080×1920 | sí (voz) | [qué dice] | ✅ hook |
| 2 | clips/clip-02-v3.mp4 | 10.0s | 1080×1920 | sí (voz) | [qué dice] | ✅ desarrollo + CTA |
| 3 | broll-cocina.mov | 5.0s | 1920×1080 | no | [qué muestra] | ⚠️ formato distinto |
| 4 | packshot.webp | — | 1600×2000 | — | [qué muestra] | ✅ cierre |
| 5 | musica.mp3 | 42.0s | — | sí | cama | ✅ bajo la voz |

**Mi propuesta**
- **Formato**: [el del creativo: 9:16 1080×1920 / …] para [plataforma] — [razón: zona segura]
- **Duración**: [N]s ([= video.seconds / propongo cambiarla porque …])
- **Estructura**: [N] cortes — hook [0–Xs] → [desarrollo] → [payoff] → [CTA]
- **Hook**: [qué se ve en el primer segundo, en una línea]
- **Transición primaria**: `[bloque]` a [X]s — [razón: energía de la pieza]
- **Acento** (1 solo): `[bloque]` en [dónde] — [razón]
- **Captions**: [rail `anchor` / sin captions / kinetic] — [razón]
- **Tipografía**: [familia real de `library/fonts/`] · **Paleta**: [hex de `library/brand/brand.md`]
- **Audio**: [música + VO / música sola / audio nativo del clip N / sin audio] — [razón]
- **Encuadre del clip 3** (formato distinto): [cover recortando los laterales / fondo desenfocado + clip centrado / queda afuera] — [razón]
- **Versiones**: clip 2 entra la `-v3` (la última) — [decímelo si preferís otra]
- **Render**: `draft` primero para que lo veas (en la tarjeta del board), `high` solo cuando lo apruebes

**Queda afuera**: [archivo] — [razón en media línea]

¿Avanzo así o cambiás algo?
```

Si algo del material no se pudo identificar, agregá una línea:

> El b-roll no lo pude identificar (no hay guion ni nombre que lo explique). ¿Qué muestra?
> Según eso lo ubico o lo dejo afuera.

---

## Cómo elegís cada default

### Formato

**Ya está decidido**: es el `canvas` del manifiesto (= el `format` del grupo
del plan). Lo que elegís es la **plataforma** dentro de ese formato, porque
cambia la zona segura:

| Destino | Formato | Píxeles |
|---|---|---|
| Reels / TikTok / Stories / Shorts | **9:16** | 1080×1920 |
| Feed de Instagram (video) | **4:5** | 1080×1350 |
| Meta ads placement mixto | **1:1** | 1080×1080 |
| YouTube / landing / desktop | **16:9** | 1920×1080 |

**Si el user pide dos formatos**: son **dos creativos** del plan (cada uno en
el grupo de su formato), con dos composiciones — no un flag de render. Decilo
explícito y proponé cuál se autora primero (el más restrictivo en zona
segura: 9:16). Si el segundo creativo no existe en el plan, hay que agregarlo
(`new-brief` scaffold) antes de montar. Cada formato es otro creativo del plan (regla 9 del `SKILL.md`).

### Duración

**El default es `video.seconds`** del manifiesto (lo que dice el plan). Si el
material no lo aguanta o la plataforma pide otra cosa, proponé el cambio y,
si el humano acepta, actualizá `video.seconds` al cerrar (paso 07).

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
| No hay música en la carpeta del Workbench | **Decilo**: la pieza sale sin música y se puede sumar después (el humano la suelta en la carpeta). No inventes un archivo que no existe. |

**Sin TTS ni música generada** (regla 21 del `SKILL.md`): el audio es lo que
trajo el humano más el nativo de los clips. Si hace falta una voz que no
existe, es un clip nuevo (`video-clips`), no una síntesis.

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

**E — pide dos formatos** → confirmá que son dos creativos (dos composiciones)
y cuál va primero. El segundo se deriva del primero reencuadrando, no
re-planificando.

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
