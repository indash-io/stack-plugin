# 03 — Dirección: voz, `style`, acotaciones, tags

Con el guion cerrado, decidís cómo suena. Tres capas, de la general a la
puntual. Formato exacto de cada una en `reference/tags.md`.

## Capa 1 — La voz (lo permanente)

Edad, género, timbre y acento **son de la voz**. Tres fuentes, detalle en
`reference/voces.md`:

- Si la persona (o el `CLAUDE.md`, sección "Voz de marca") ya tiene una voz
  fija — un nombre de estudio o un `voice_…` — esa.
- **Sin acento específico** → estudio: shortlist de 2-3 por los tres adjetivos
  del tono, audición en el paso 5.
- **Idioma/acento concreto** ("mexicano", "neutro latino", "inglés US") →
  biblioteca: `list_voices` con `language_codes` (+ `genders`, `accents`),
  shortlist de 2-3, audición.
- **Persona específica** ("una argentina de veinte años, voz clara, porteña")
  o **voz de marca a reusar** → `design_voice` con la descripción de rasgos
  permanentes (edad, género, timbre, acento, forma base de hablar; en 1-2
  frases; `language_code` siempre). Escuchan el sample; si no cierra, se
  itera **un rasgo por vez**, y las descartadas se borran (`delete_voice`).
  El `voice_id` ganador se anota en el `CLAUDE.md` del cliente.
- Nunca elijas vos la voz definitiva por el nombre ni por la descripción: la
  persona escucha.
- Dos voces → contraste de carácter (Firm + Upbeat, Warm + Excitable), nombres
  de persona.

## Capa 2 — El `style` de la pieza

Una o dos frases en lenguaje natural, en este orden: **tono, ritmo, energía,
registro, a quién le habla, contexto de escucha**.

```
Voz en off de un UGC de Instagram: natural, como contándole a una amiga,
ritmo ágil sin apurarse, sonriendo, registro cercano con voseo. Se escucha
en el celular, muchas veces sin auriculares.
```

Lo que **no** va en el `style`: edad, género ni acento permanente (eso es la
voz, capa 1 — Google lo dice explícito), instrucciones línea por línea (para
eso están las acotaciones), ni cosas que el modelo no puede hacer (ver
`reference/capacidades.md`). El idioma se detecta solo del texto del guion.

## Capa 3 — Acotaciones y tags (solo donde cambia algo)

- **Acotación** `(así)` al inicio de una línea cuando **esa línea** se dice
  distinto al resto: bajar la voz, acelerar, dudar, remarcar.
- **Tag** `<…>` donde una persona real haría eso: un `<breath>` antes del CTA,
  un `<short pause>` antes del precio, un `<chuckle>` si el guion es gracioso
  **en esa frase**.
- Presupuesto orientativo: en un guion de 10-15s, **0-2 acotaciones y 0-2
  tags**. En uno de 60s, no más de una por bloque. Si cada línea tiene
  acotación, el `style` estaba mal escrito.
- Sin exclamaciones dobles, sin MAYÚSCULAS para gritar: pedilo en la
  acotación ("gritando", "susurrando").

## Dos voces

- `speakers`: `[{ name: "Ana", voice: "Kore", style: "cálida, segura" },
  { name: "Tomi", voice: "Puck", style: "curioso, un poco escéptico" }]`.
- El guion con `Ana:` / `Tomi:` al inicio de cada línea. Escribilo como
  charla: interrupciones cortas, `|mhm|` de la que escucha, una risa donde
  cabe. El modelo hace los turnos solo; no lo dirijas de más.
- Máximo 2 voces por item. Tres personajes = dos items y montaje.

## Modelo

- `gemini-tts` (default) para todo lo que lleva dirección.
- `gemini-tts-lite` (dos tercios) para N variantes del mismo copy, narración
  plana o placeholders de edición que después se regraban.

## Salida de este paso

El **guion dirigido**: `style` + guion con sus acotaciones y tags + voz o
shortlist + (si aplica) `speakers`. Lo pegás en `templates/guion.md` y va a la
pregunta consolidada del paso 4.
