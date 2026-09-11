# Bloque por pieza — el contrato entre ideación y ejecución

> **Espejo** — la fuente única vive en `skills/content-brief/templates/bloque_por_pieza.md` del set de ideación. Si editás uno, editá el otro.



El brief que arma el set de ideación se compone de **bloques**: uno por pieza (o por
grupo, en carruseles). Este formato ES el contrato: si el bloque llega
completo, `new-brief` lo vuelca a `plan.json` + manifiestos **sin re-decidir nada**,
y la ejecución corre sin preguntas. Todo campo que falte acá es una pregunta que
alguien va a tener que hacer después — o peor, una decisión que la ejecución va a
tomar sola.

## Campos comunes (toda pieza)

| Campo | Qué va | Regla |
|---|---|---|
| `id` | kebab-case, sin acentos (`story-01`, `ad-oferta-01`) | Va a ser el nombre de la carpeta del creativo |
| `grupo` + `formato` | `stories` 1080×1920 · `feed` 4:5 1080×1350 · `square` 1080×1080 · `reels` 1080×1920 | Un grupo = un formato |
| `funnel` | frío \| tibio \| caliente | Siempre declarado |
| `arquetipo` | Del catálogo de la skill de ideación que produjo el bloque | Nombralo, no lo describas |
| **`¿componer o generar?`** | **componer** = pieza tipográfica / brand-flat / precio+packshot → capas, sin generación. **generar** = lleva escena orgánica → capa ai-gen | La decisión más importante del bloque. Nunca implícita |
| **`producto`** | `product_id` + **vista pedida** (frente / perfil / detalle / en-uso / packshot) — o `lifestyle sin producto` **declarado** | Lifestyle sin producto es legítimo, pero se decide acá y queda escrito |
| `copy on-image` | El texto EXACTO: título / sub (opcional) / CTA | Va como **capas de texto**, jamás al modelo de imagen |
| `concepto visual` | 2-4 líneas: la escena orgánica (si se genera) o la composición (si se compone), incluyendo dónde queda el espacio negativo para el texto | Sin adjetivos vacíos |
| `notes` | Restricciones: claims prohibidos, no-negociables de la marca, reglas del cliente | Lo que la ejecución no puede adivinar |

## Campos por tipo de pieza

- **Carrusel** → el bloque es el **grupo**: N slides (3-7, default 4), narrativa
  hook → desarrollo → CTA declarada, y un sub-bloque por slide (mismos campos
  comunes). El último slide es SIEMPRE un CTA accionable.
- **Story / secuencia** → además: **sticker de engagement por story** (poll /
  pregunta / countdown / link / ninguno). Es instrucción de **publicación** (se
  agrega en Instagram al subir), no de render — pero se decide en ideación.
- **Ad de Meta** → además: **copy de Meta completo** — Primary Text, Headline,
  Description, CTA — con conteo de caracteres. Viaja en el brief para quien
  publica; la pieza visual es un creativo más.
- **Video UGC** → el bloque es **un creativo** del grupo de su formato:
  `kind: video` + `seconds` (un video = un formato; los clips se derivan:
  `ceil(seconds/10)`). Por clip: **guion** (28-32 palabras por 10s,
  techo ~34) + **registro** (orgánico/genuino vs descriptivo/beneficios) + el
  **gesto** que el still tiene que actuar (el hook se actúa, no solo se dice).
  Nombre de marca dudoso → marcarlo `pronunciación a validar`.
- **Email** → 3 ángulos (emocional / racional / aspiracional) + subject +
  preheader + hipótesis de A/B por variante. La ejecución HTML **no pasa por el
  Studio** — este bloque se entrega a quien ejecute el mail.

## Mapeo a `plan.json` (lo hace `new-brief`, mecánicamente)

| Del bloque | Al disco |
|---|---|
| grupo + formato | `groups[]` de `plan.json` (solo `format`) |
| pieza (`id`, título; + `kind: video` y `seconds` si es video) | `creatives[]` del grupo |
| ¿componer o generar? + producto + vista + restricciones | `notes` del creativo (escritas, textuales) |
| copy on-image | capas `text` del manifiesto scaffoldeado |
| guion del clip | `notes` del creativo de video + el documento del brief; `video-clips` los vuelca a `workbench/<brief>/<video>/scripts/` al producir |
| sticker / copy de Meta / bloques de email | quedan en el documento del brief (`briefs/<brief>/source/`) — no se renderizan |
