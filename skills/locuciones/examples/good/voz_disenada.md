# Ejemplo good — diseñar la voz de una marca y reusarla

**Pedido:** *"Quiero que todos los reels de la marca tengan la misma voz: una
piba argentina de veinte y pico, que suene real, no locutora."* El `CLAUDE.md`
del cliente no tiene "Voz de marca". Marca de skincare joven, voseo.

## Por qué no alcanza con el `style`

"Una argentina de veinte años" es **edad + acento + género**: rasgos
permanentes. Google dice explícito que eso no va en `speech_metadata.style`
(el modelo lo ignora o lo hace a medias). Es **voice design**.

## Primera pasada: biblioteca (gratis)

`list_voices` con `language_codes: ["es-AR"]`, `genders: ["female"]`. Trajo
cuatro prebuilt argentinas. Se auditó el hook en dos de ellas (2 items
`short`, 20 créditos). Veredicto de la persona: *"suenan a locutora de radio"*.
Eso es el timbre y la forma base de hablar → diseñar.

## Diseño (10 créditos)

```json
{
  "name": "Juli — porteña 25",
  "description": "Una mujer argentina de veintipocos, voz clara con un poco de aire, acento porteño marcado, habla rápido y con seguridad, como recomendándole algo a una amiga. Nada de dicción de locutora.",
  "gender": "female",
  "language_code": "es-AR",
  "persona": "Friend recommending"
}
```

Sample de 4s. La persona: *"esa, pero un toque más grave"*. Segundo diseño
cambiando **un solo rasgo** ("voz clara, un poco grave, con aire…"). Ese
quedó. `delete_voice` al primero.

Costo total de la voz: 20 (audición biblioteca) + 20 (dos diseños) = 40
créditos. Una sola vez para toda la marca.

## Reuso

En el `CLAUDE.md` del cliente:

```
## Voz de marca
- `voice_9f2c…` — "Juli — porteña 25": mujer argentina de veintipocos, voz
  clara, un poco grave, con aire, acento porteño, habla rápido y con
  seguridad. Diseñada 2026-09-24, vence 2027-09-24. Sample: <url>
```

Desde ahí, cada locución de la marca va con `voice: "voice_9f2c…"` y el
`style` solo dice **cómo se lee esta pieza**: *"UGC natural, sonriendo, ritmo
ágil, como a una amiga"* / *"más íntimo, bajando la voz, de noche"*. La voz no
cambia; la lectura sí.

## Lo que se dijo en la entrega

- Que el agente no escuchó nada: la persona eligió por los samples.
- Que la voz vence en un año y que quedó anotada para reusarla.
- Que se borró la descartada para no ocupar cuota.
