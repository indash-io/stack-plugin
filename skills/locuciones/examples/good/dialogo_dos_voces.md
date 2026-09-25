# Ejemplo good — escena de dos voces para un ad de 20s

**Pedido:** *"Un ad tipo charla entre dos amigas sobre el sérum, una lo
probó y la otra duda."* Marca premium accesible, tuteo neutro (lo dice su
`CLAUDE.md`).

## Style de la pieza

> Conversación real entre dos amigas de treinta y pico, cerca del micrófono,
> ritmo natural con pequeñas superposiciones, español neutro latinoamericano,
> sin tono de anuncio.

## Speakers

| Nombre | Voz | Style |
|---|---|---|
| Ana | Despina (Smooth) | "segura, cálida, ya lo probó y le encanta" |
| Vale | Leda (Youthful) | "curiosa, un poco escéptica, se deja convencer" |

Contraste de carácter (Smooth + Youthful) y nombres de persona: el modelo
actúa mejor así que con `Speaker 1`.

## Guion dirigido

```
Vale: ¿Y? ¿Se nota algo o es otro sérum más?
Ana: (riéndose un poco) <chuckle> Se nota. En dos semanas.
Vale: |mhm| Dos semanas dice…
Ana: (bajando la voz, como un secreto) Es el ácido hialurónico. Pero el de verdad.
Vale: (cediendo) Bueno. Pasame el link.
Ana: (sonriendo) Te lo mando ahora.
```

**Caracteres hablados:** 231 · **Estimado:** ~15-20s (los diálogos rinden
más lento que la narración) · **Tier:** short

Por qué está bien:

- La primera línea nombra a un speaker (si no, la tool rechaza el item).
- Escrito como charla: frases cortas, una interjección `|mhm|`, una risa donde
  cabe, un secreto que baja la voz. Nada de dos monólogos alternados.
- Acotaciones solo en los giros; el `style` de cada una lleva el resto.
- El CTA lo dice el personaje ("pasame el link"), no una voz de anuncio.
- Sin claims que no estén en el sitio: "ácido hialurónico" está en la ficha
  del producto.

## Resultado

| Item | Speakers | Duración real | Tier |
|---|---|---|---|
| 1 | Ana (Despina), Vale (Leda) | 18.2s | short |

Entregado con la advertencia de siempre (no escuchado) y la sugerencia de
probar Sulafat en lugar de Despina si Ana suena "demasiado locutora".
