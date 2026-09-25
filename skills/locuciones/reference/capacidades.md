# Capacidades de `generate_speech` — qué sí, qué no, cuánto cuesta

Fuente: las tools de voz del conector `indash` — `generate_speech`,
`list_voices`, `design_voice`, `delete_voice` — sobre Gemini 3.8 TTS y la
Voices API de Google (docs leídas 2026-09-24). Si algo no está acá, **no lo
prometas**: decí que hoy no está expuesto.

## Qué SÍ

| Capacidad | Cómo se usa |
|---|---|
| **Dos modelos** | `gemini-tts` (Gemini 3.8 Flash TTS, **default**, el que se dirige) y `gemini-tts-lite` (Flash-Lite, **dos tercios de los créditos**, para volumen o narración plana) |
| **30 voces de estudio** | `voice` = nombre del roster (`reference/voces.md`). Default `Kore`. Hablan cualquier idioma |
| **Biblioteca extendida** | `list_voices` con `language_codes` (`es-AR`, `es-MX`, `es-419`, `en-US`…), `genders`, `accents`, `personas`, `search`. Cientos de voces prebuilt afinadas por idioma/acento. Se pasa el `voice_id` tal cual en `voice` |
| **Voz diseñada** | `design_voice` con una descripción de 1-2 frases de rasgos **permanentes**: edad, género, timbre, acento, forma base de hablar. Devuelve un `voice_…` guardado para el workspace + un **sample** para escuchar (creative `audio`). Después `voice: "voice_…"` en `generate_speech`. **Es la única forma de fijar edad/género/acento** — en el `style` no van |
| **Borrar una voz diseñada** | `delete_voice` con su `voice_id`. Libera cuota |
| **Dirección de la pieza** | `style`: tono, ritmo, energía, acento, a quién le habla, en lenguaje natural |
| **Dirección por línea** | Acotación entre paréntesis **al inicio** de una línea del guion: `(bajando la voz, cómplice) Esto no se lo cuentes.` |
| **Vocalizaciones en el punto exacto** | Tags inline: `<laugh>`, `<chuckle>`, `<sigh>`, `<breath>`, `<gasp>`, `<cough>`, `<throat-clearing>`, `<groan>`, `<short pause>`, `<long pause>`. Interjecciones de escucha: `\|mhm\|`, `\|yeah\|` |
| **Dos voces en escena** | `speakers` (exactamente 2: nombre + voz + `style` opcional cada una) y el guion con `Nombre: línea`. El modelo hace los turnos, interrupciones y backchannel solo |
| **130 idiomas** (Flash) / 101 (Lite) | Se detecta solo del texto. El **acento** se pide en `style` |
| **Largo** | Hasta **4.500 caracteres hablados por item** (~5 min). Los tags, acotaciones y etiquetas de speaker no cuentan |
| **Batch** | 1-12 items por llamada, cada uno con su guion, voz, dirección y modelo |
| **Salida** | WAV 24 kHz mono 16-bit, guardado como creative **`audio`** en la galería del workspace (draft privado; `promote_creative` lo comparte). Devuelve `url`, `creative_id`, `duration_seconds`, `tier`, `size_kb` |

## Qué NO (hoy)

- **Clonar una voz real** (la de la dueña de la marca, la de un influencer). La
  API lo soporta con verificación de consentimiento, pero la tool **no lo
  expone** (queda para después). Lo más cercano y honesto: `design_voice` con
  una descripción de esa voz — y decir que es una voz parecida, no la suya.
- **Cambiar edad, género o acento con el `style`.** Google lo dice explícito:
  esos rasgos son de la voz. Se eligen (`list_voices`) o se diseñan
  (`design_voice`).
- **MP3 / AAC / OGG desde el MCP.** Sale WAV. Convertir es local:
  `ffmpeg -i in.wav -b:a 192k out.mp3`.
- **Duración exacta.** El largo del audio es consecuencia del guion y la
  dirección; la estimación (~15 chars/s) tiene un margen de ±15%. Si hace falta
  clavar 10.0s, se ajusta el guion o se estira/recorta en edición.
- **SSML, pitch numérico, velocidad numérica.** Todo es lenguaje natural
  ("más lento", "grave") — y funciona.
- **Más de dos voces en un item.** Tres personajes = dos items (o dos escenas)
  y montaje.
- **Streaming / tiempo real.** Es una generación, no una llamada.
- **Escuchar el resultado.** El agente no puede. La persona escucha.

## Costo — por item, según el largo del guion

El cobro es **por llamada, por item**, con el tier calculado **antes** de
generar sobre los caracteres **hablados** (sin tags ni acotaciones):

| Tier | Caracteres hablados | ≈ Duración | `gemini-tts` | `gemini-tts-lite` |
|---|---|---|---|---|
| `short` | ≤ 450 | ≤ 30s | 10 créditos | 7 |
| `standard` | ≤ 1.500 | ≤ 100s | 30 | 20 |
| `long` | ≤ 4.500 | ≤ 5 min | 90 | 60 |
| **diseño de voz** (`design_voice`) | — | sample corto | 10 | — |

`list_voices` y `delete_voice` son gratis.

Lecturas prácticas:

- **Una audición** (una línea del guion en 3 voces) = 3 items `short` = 30
  créditos. Es lo más barato que se puede hacer para no equivocar la voz.
- Una VO de 10-15s para un UGC es `short`. Un ad de 30-45s con respiración,
  también. Un explainer de 2 min es `standard`.
- Un guion de 460 caracteres paga `standard`: **10 caracteres de más duplican
  el precio triple**. Cuando estás al borde, recortá.
- `gemini-tts-lite` para las 8 variantes de un mismo copy o para narración sin
  dirección. Para lo que se dirige, Flash.
- **Diseñar una voz cuesta lo mismo que una audición de una voz** (10). Pero
  cada diseño es una voz nueva guardada en Google: **200 por proyecto para
  todo Indash, un año de vida**. Iterá la descripción con criterio, borrá las
  descartadas con `delete_voice`, y anotá el `voice_id` ganador en el
  `CLAUDE.md` del cliente para no volver a diseñarla.
- Si un item falla, se refunda solo. Un guion inválido (vacío, pasado del tope,
  dos voces sin `Nombre:` en la primera línea) se rechaza **antes** de cobrar.

## Lo que el modelo hace bien y lo que se le escapa

**Bien:** tono sostenido, cambios de intensidad por línea, risas y suspiros
naturales, pausas dramáticas, diálogos con ritmo real, voseo si el guion lo
trae, y — con una voz de la biblioteca o diseñada — un acento sostenido de
punta a punta.

**Se le escapa (y cómo se maneja):**

- **Nombres de marca y palabras inventadas** → los puede leer "en inglés" o
  raro. Escribilos como suenan si hace falta (`Indash` → `Indash` suele salir
  bien; `Xüpp` → `shup`), y probalos en la audición.
- **Números, siglas, símbolos** → se leen literal. `20%` → escribí `veinte por
  ciento`. `IG` → `Instagram`. `$4.999` → `cuatro mil novecientos noventa y
  nueve pesos`.
- **Frases larguísimas** → se quedan sin aire y pierden intención. Cortá.
- **Idiomas mezclados en la misma línea** → un término en inglés dentro de una
  frase en español puede salir con acento raro. Si es una palabra clave del
  producto, aceptalo o buscá alternativa; si no, evitalo.
- **Exceso de tags** → tres `<laugh>` en una línea suenan a personaje, no a
  persona.
