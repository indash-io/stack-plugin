# Modelos de video — cuándo salir de omni, y qué cambia si salís

`generate_video` en Studio es **siempre image-to-video**: el still elegido es el
`start_image`, no hay text-to-video puro. El proceso de esta skill (guion →
still → render) está **calibrado sobre `omni`** — todo lo del SKILL.md aplica
tal cual con omni. Este archivo existe para cuando el humano pide otro modelo:
qué gana, qué pierde y qué reglas cambian.

## La tabla

| Modelo | Duración | Audio nativo | `last_image` | `negative_prompt` | Para qué sirve de verdad |
|---|---|---|---|---|---|
| `omni` | **hasta 10s** | sí | no | no | **El default UGC.** Rápido, barato, audio nativo decente. Todo el proceso está medido sobre él |
| `seedance-2.0` | 4-15s | sí (con asteriscos, ver Audio) | sí | no | El más capaz en general: physics, estabilidad de movimiento, multi-momento adentro de un clip (timeline `0-3s / 3-6s`). Clips de más de 10s |
| `seedance-1.5` | 4-15s | sí | sí | no | La variante barata de seedance. **Puede no tener precio cargado en billing** — si el server lo rechaza con un error de validación, no es un bug: avisale al humano y volvé a omni o seedance-2.0 |
| `veo-3.1` | **hasta 8s** | sí — el mejor lip-sync | no | sí | Realismo humano extremo y lip-sync preciso. Ojo: 8s es techo duro — **no llega a los 10s del formato**, el guion se recorta a ~24-26 palabras |
| `kling-3.0` | 3-15s | sí (no en español, ver Audio) | sí | sí | Physics y consistencia de producto entre planos. Clips largos sin diálogo |

## Audio por idioma (la decisión que más clips arruina)

| Diálogo en | omni | veo-3.1 | seedance-2.0 | kling-3.0 |
|---|---|---|---|---|
| Español rioplatense | ✅ nativo (escribir literal "Argentine Rioplatense Spanish") | ✅ nativo — respeta acentos regionales | ✅ nativo con receta: `"sh" on "ll"/"y" + "vos" + sing-song` | ❌ **aluciña siempre** → `audio: false` |
| Mexicano / neutro LATAM / España | ✅ | ✅ | ✅ con receta del acento explícita en el prompt | ❌ |
| Otros acentos (cubano, chileno…) | probar 1 clip y que lo escuche un humano | ✅ | ❌ sin caso validado → `audio: false` | ❌ |
| Inglés | ✅ | ✅ | ✅ | ✅ |

Cuando el audio va **off** (`audio: false`), el prompt tiene que pedir
articulación igual: *"lips move in natural full conversational articulation as
if speaking (no native audio generation), voice added in post"* — eso le da
material a un lipsync posterior. NO pidas "minimal articulation": queda muerto.
Y no prendas el audio "para que quede más dinámico" en un modelo que aluciña el
español: es un trade-off falso, el clip sale inutilizable.

## Reglas que cambian con seedance (las dos que más cuestan)

1. **Look UGC hay que sobre-dirigirlo.** Seedance default-ea a comercial
   pulido. Si el clip tiene que leerse UGC, escribí explícito: `subtle handheld
   micro-shake`, `natural window light`, `no studio lighting`, `iPhone POV
   framing`. Omitirlo = sale un ad cinematográfico donde iba un selfie.
2. **Texto en pantalla flojo.** Seedance degrada el text rendering: si el
   packaging tiene tipografía protagonista, el dictado letra por letra del
   still importa el doble, y el prompt de video repite "sus letras no cambian
   ni se deforman".

## `last_image` (seedance y kling): interpolación, no referencia

Pasar `last_image` hace que el clip **interpole del primer frame al último**:
sirve para before/after, reveals y transiciones controladas. **No** es "otra
foto del producto" ni una referencia de sujeto — es el estado final concreto de
la MISMA escena. La forma vieja de usarlo mal (segunda imagen = otro ángulo del
producto) produce morphs indeseados.

## La regla de las 3 fidelidades (vale para todos los modelos)

En un solo clip no podés exigir las tres a la vez:

1. Fidelidad de **producto específico** (forma, color exacto, etiquetas).
2. Fidelidad de **persona específica** (la cara y ropa del still, sin deriva).
3. **Movimiento de cámara extremo continuo** (FPV, hyperlapse, whip-pan).

**Máximo 2 por clip.** Si el pedido junta las 3, sale roto casi siempre: partí
en dos clips (uno con cámara + producto sin persona; otro con persona +
producto y cámara quieta) y que el corte entre ambos haga el trabajo. Esto se
decide en el guion/still, no en el render — si llegaste acá con las 3 en un
clip, volvé al Paso 1.

## Costos

El render se cobra **por segundo pedido**, upfront, del saldo del workspace
(~100 créditos/segundo como referencia). Un modelo más largo no es "gratis
porque es un solo clip": 15s de seedance cuestan más que 10s de omni. Si un
modelo rebota por saldo o por precio no cargado, reportá exactamente qué clip
quedó sin renderizar y con qué prompt, y esperá la recarga — sin re-preguntar.
