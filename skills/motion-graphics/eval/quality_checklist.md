# Quality checklist — antes de entregar

Si un ítem falla, va a la lista de fixes de `instructions/07_review.md`. No se convierte
en salvedad de la entrega.

## Historia
- [ ] La UVP se entiende sin la voz: mirado en mute, se sabe qué es y para quién.
- [ ] Cada claim en pantalla y en la voz está en el ledger con su fuente.
- [ ] Ningún no-claim aparece contradicho.
- [ ] El pedido original, releído palabra por palabra, se cumple en cada término.

## Material real
- [ ] Cada elemento que representa al producto tiene un archivo real como fuente en el storyboard.
- [ ] No hay ícono de app, pantalla, dorso, badge ni feature inventado.
- [ ] Los assets oficiales están sin tocar y solo en la pieza para la que llegaron.
- [ ] El punto de grabación de iOS no asoma en ningún frame.

## Ritmo
- [ ] Ningún tramo de más de 1.5 s sin un evento nuevo (en la contact sheet a 6 fps).
- [ ] Cada corte y cada slam cae en la grilla. El golpe final de la música cae en el CTA.
- [ ] Ninguna transición se repite dos veces seguidas.
- [ ] La pieza no dura más de lo que necesita.

## Marca
- [ ] Paleta, tipografías y vocabulario del manual. Ninguna palabra prohibida.
- [ ] El logo nunca aparece espejado, estirado ni recoloreado fuera de sus versiones.
- [ ] Las captions aparecen solo donde la voz dice algo distinto del título.

## Técnica
- [ ] `npx hyperframes lint` sin errores y `npx hyperframes check` OK.
- [ ] Consola de Studio limpia en cada escena 3D.
- [ ] Sin choques, restos, vacíos ni texto ilegible en la última pasada de contact sheets.

## Audio
- [ ] La transcripción del draft tiene todas las palabras del guion.
- [ ] Ninguna línea de voz llega más de 0.35 s tarde a su corte.
- [ ] `mix.py measure --file` da OK (−14 ±1 LUFS, TP ≤ −1 dBTP).
- [ ] Hay una alternativa de audio lista: otra voz u otra música.

## Entrega
- [ ] Están el link de Studio, el draft, las alternativas, las decisiones a confirmar y
      lo que no se verificó.
- [ ] El render en alta no se corrió sin OK.
