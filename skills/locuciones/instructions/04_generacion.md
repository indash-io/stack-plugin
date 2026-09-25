# 04 — Generación: `list_voices`, `design_voice`, `generate_speech`

Recién después de la confirmación del paso 4. **Una llamada de
`generate_speech`, todos los items.** Antes, si hace falta, la voz.

## Elegir de la biblioteca (gratis)

```json
{ "workspace_id": "<ws>", "language_codes": ["es-AR"], "genders": ["female"], "limit": 20 }
```

Devuelve `designed` (las del workspace, con `sample_url`), `studio` (30) y
`library` (paginado con `next_page_token`). Las de biblioteca no traen sample:
la audición es una línea con `generate_speech`.

## Diseñar una voz (10 créditos, una por llamada)

```json
{
  "workspace_id": "<ws>",
  "name": "Juli — porteña 25",
  "description": "Una mujer argentina de veintipocos, voz clara con un poco de aire, acento porteño marcado, habla rápido y con seguridad, como recomendándole algo a una amiga.",
  "gender": "female",
  "language_code": "es-AR",
  "persona": "Friend recommending"
}
```

Devuelve `voice_id` (`voice_…`), `expires_at` y `sample.url` para escuchar.
Rasgos permanentes en la descripción; la emoción de la lectura va después en
`style`. Si no cierra, un rasgo por vez y `delete_voice` a la descartada. El
ganador se anota en el `CLAUDE.md` del cliente ("Voz de marca: `voice_…`").

## La locución

```json
{
  "workspace_id": "<del list_workspaces / CLAUDE.md del cliente>",
  "items": [
    {
      "script": "(entusiasta, rápido) ¿Te pasa que llegás a casa y no tenés ganas de cocinar? <short pause>\nAcá va la solución, en diez minutos. <breath>\nProbalo hoy. Link en la bio.",
      "style": "Voz en off de UGC de Instagram, natural, como a una amiga, ritmo ágil, sonriendo, español rioplatense con voseo.",
      "voice": "Zubenelgenubi",
      "model": "gemini-tts",
      "output_name": "2026-09-24_pasta-lista_v1-A.wav"
    }
  ]
}
```

- `items`: 1-12. Audición = un item por voz candidata con la **misma** línea y
  el **mismo** `style`. Versiones finales = un item por variante.
- `output_name`: el nombre canónico del set (`<fecha>_<slug>_v<N>[-A|-B].wav`).
  Si no lo pasás, la tool inventa uno único; pasalo, así la galería y el disco
  coinciden.
- `voice` acepta las tres fuentes con el mismo string: `"Kore"`, un `voice_id`
  de biblioteca, o un `voice_…` diseñado **de este workspace** (uno ajeno se
  rechaza antes de cobrar; uno vencido, también).
- Dos voces: sacás `voice`, ponés `speakers` (2) y el guion con `Nombre:`.
  Cada `speakers[].voice` acepta las mismas tres fuentes.
- Modelo por item: podés mezclar `gemini-tts` y `gemini-tts-lite` en la misma
  llamada.

## Antes de disparar, chequeá

- Cada `script` está **debajo del tier que dijiste** que iba a costar (contá
  caracteres hablados: sin tags ni acotaciones). Al borde de 450 / 1.500,
  recortá: 10 caracteres de más cambian el tier.
- Ningún item pasa 4.500 caracteres hablados. Si pasa, partí en items (por
  bloque o por shot) — se concatenan local con `ffmpeg`.
- En dos voces, la **primera línea** nombra a un speaker.
- El `workspace_id` es el del cliente correcto.

## Leer el resultado

Por item, en orden:

- `status: "completed"` → `url` (pública, para escuchar), `creative_id`,
  `duration_seconds`, `tier` (lo que se cobró), `size_kb`, `output_name`.
- `status: "error"` → `error` con el motivo. El crédito de ese item **ya se
  refundó**; no vuelvas a llamar sin cambiar algo.

Chequeos que hacés vos (no podés escuchar):

| Chequeo | Qué hacer si falla |
|---|---|
| `duration_seconds` vs. objetivo (±15%) | Más largo: recortá guion o pedí "más rápido" en `style`. Más corto: sumá una frase o "más pausado" |
| `tier` = el que anunciaste | Si subió, avisá el costo real y por qué (te pasaste de caracteres) |
| Error "too long" | Partí el guion en items |
| Error "every line must belong" | La primera línea del diálogo no tenía `Nombre:` |
| Error de la API (429, contenido) | Decilo tal cual; un reintento manual es razonable, tres no |
| Error "not a designed voice of this workspace" | El `voice_…` es de otro cliente o está mal copiado: `list_voices` |
| Error "expired on …" | La voz diseñada venció (un año): diseñala de nuevo con la misma descripción |
| `design_voice` con "quota" / RESOURCE_EXHAUSTED | El proyecto llegó a las 200 voces guardadas: borrá descartadas con `delete_voice` (las tuyas) y avisá al equipo de Indash |
| "no Gemini API key" | Es del servidor, no tuyo: avisale a la persona y frená |

## Costo — decilo antes y después

Antes: "3 audiciones `short` (30 créditos) y después 1 final `short` (10)".
Después: lo que efectivamente cobró cada item (`tier`). Si algo falló, aclará
que se refundó.

## Regenerar

Cuando la persona escucha y pide cambios, cambiás **dirección** (`style`,
acotación, tag, voz), no "probá otra vez": el modelo no tiene semilla que
mover. Una regeneración = una llamada nueva con los items que cambian, no con
todos.
