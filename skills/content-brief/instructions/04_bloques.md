# 04 — Bloques por pieza

Con el mix confirmado, escribís el bloque de cada pieza. El formato es EL
contrato: `templates/bloque_por_pieza.md`. Cada bloque tiene que llegar
**completo** — si el bloque está completo, la ejecución corre sin preguntas; si
le falta un campo, alguien va a tener que preguntarlo (o decidirlo solo)
después.

## Cómo trabajás cada tipo

Derivá la ideación de cada tipo a su skill — ahí vive el oficio (arquetipos,
registros, reglas de copy). Vos aportás el contexto del período (objetivo,
funnel, producto, reglas duras) y garantizás la coherencia del conjunto:

| Tipo | Skill | Qué te devuelve |
|---|---|---|
| Ads de Meta | `ideacion-ads` | Bloques con ángulo + copy de Meta completo + concepto visual |
| Carruseles | `ideacion-carruseles` | Bloques de grupo: narrativa + sub-bloque por slide |
| Stories | `ideacion-stories` | Bloques de secuencia: copy + sticker por story |
| Videos | `ideacion-video` | Bloques de video (un creativo `kind: video` + `seconds` cada uno): guion por clip + registro + gesto |
| Emails | `ideacion-emails` | Bloques de campaña: 3 ángulos + subjects + hipótesis |

Si el pedido es de un solo tipo ("armá 3 ads para el lanzamiento"), la skill de
ideación puede correr sola — pero cuando el período pide varios tipos, **vos
sos quien reparte los ángulos** para que no se pisen.

## Principios (valen para todos los bloques)

1. **Cada pieza tiene una función** dentro del período. No repitas el mismo
   ángulo N veces; variá el hook. Para A/B real, ángulos distintos — no
   variaciones cosméticas del mismo.
2. **Funnel + formato explícitos** en cada bloque.
3. **La decisión ¿componer o generar? va escrita.** Pieza tipográfica /
   brand-flat / precio+packshot → se COMPONE. Escena orgánica → se GENERA.
   Nunca implícita.
4. **Producto declarado**: `product_id` real + vista pedida (frente / perfil /
   detalle / en-uso / packshot) — o `lifestyle sin producto`, declarado. Un
   bloque que no dice qué producto y qué vista es un bloque incompleto.
5. **Copy on-image textual y exacto.** El texto va a ser capas en el manifiesto
   — escribilo palabra por palabra, no "un claim sobre X". Voseo si la marca lo
   usa; sin claims inventados; reglas duras respetadas en cada línea.
6. **Concepto visual accionable, no prompt.** 2-4 líneas: escena o composición,
   producto en cuadro, mood, y **dónde queda el espacio negativo para el
   texto**. El prompt final lo arma la ejecución.
7. **Numerá las piezas** dentro de cada tipo e ids en kebab-case
   (`ad-oferta-01`, `story-hook-01`) — el id va a ser la carpeta del creativo.

## Revisión de coherencia (antes de ensamblar)

Releé el conjunto completo y chequeá:

- ¿Hay dos piezas con el mismo hook o el mismo ángulo? → cambiá una.
- ¿El funnel quedó balanceado según el objetivo? (un lanzamiento sin piezas de
  frío no llena el funnel)
- ¿Todos los bloques respetan las mismas reglas duras?
- ¿Algún bloque usa un producto sin fotos utilizables? → marcarlo ⚠️ en el brief.

Con todos los bloques completos → pasá a `05_entrega.md`.
