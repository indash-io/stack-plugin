---
name: ig-stories-secuencia
description: "Reglas de formato para una secuencia de N stories de Instagram (9:16) con narrativa cross-story (hook → desarrollo → CTA). Se carga cuando la pieza es múltiples stories que cuentan algo juntas. Para una sola story, ver ig-story."
language: es
---

# Format — Instagram Stories Secuencia (N stories)

Skill de **formato puro** para una secuencia narrativa de N stories. Para UNA story sola, ver `ig-story` (ahí están las specs base, zona segura UI y reglas de copy on-image que también aplican acá).

## Specs técnicas

- **Aspect ratio**: 9:16 vertical (igual que story sola).
- **Resolución**: 1080x1920.
- **Cantidad típica**: 3 a 6 stories. **Default razonable: 4.**
- **Aspect ratio**: pasalo siempre como **`aspect_ratio: "9:16"`** en `generate_image`. NO lo escribas en el texto del prompt — es parámetro de la tool.
- **Cierre del prompt** (igual que `ig-story`, sin aspect): *"fotografía editorial de alto detalle, fotorrealista, foco nítido en el producto, composición que respeta la zona segura de UI con el texto fuera del 14% superior y del 15% inferior del cuadro."*

## Narrativa cross-story

A diferencia del carrusel (manual), la secuencia de stories tiene **auto-advance**. El user pasa solo si tu primer segundo no engancha. Hook fuerte o se va.

Estructura clásica:

| Story | Función |
|---|---|
| 1 (hook) | Detener el scroll. Texto grande centrado dentro de zona segura. Producto en presencia, no en uso. Pregunta provocadora o claim corto. |
| 2..N-1 (desarrollo) | Variar ángulo y escena. Si hay humanos, van acá (demostración, contexto de uso, lifestyle). Cada story aporta algo nuevo. |
| N (CTA) | Composición frontal, máxima legibilidad del texto, foco total en producto + acción. **Espacio limpio en el último 15% para el sticker de link.** |

## Stickers de engagement por rol

Cuando proponés la secuencia, sugerí **un sticker por story**:

| Rol | Sticker típico |
|---|---|
| Hook (story 1) | Pregunta, poll abierto, GIF |
| Desarrollo | Pregunta, slider de emoji, countdown |
| Prueba/educativo | Quiz, "did you know" |
| CTA (última) | Link sticker, swipe-up, countdown a launch |

Los stickers NO van dentro de la imagen generada (son overlays nativos de Instagram). Solo los sugerís como nota al user.

## Ritmo de la secuencia

- Variá **placement del texto** entre stories — no clones la misma posición.
- Variá **ángulo y escena** — no repitas la misma toma.
- Mantené **lente, mood, paleta, luz** consistentes (Ley 7 de prompt-craft).
- Hook agarra atención en el primer segundo. CTA cierra con acción clara.

## Consistencia entre stories

Aplica Ley 7 de `prompt-craft`. Para secuencia de stories específicamente:

- **Lente igual** en todas. Mezclar 35mm y 85mm en la misma secuencia desarma la sensación de "una sesión".
- **Paleta heredada** del producto + máximo 2 colores ambientales.
- **Mood consistente** — una palabra que define la secuencia entera.
- **Variación sí**: ángulo, distancia, presencia/ausencia de persona, placement del texto.

## Cuándo la secuencia NO es la respuesta

- El user quiere algo de impacto único → mejor una **story sola** o un **post**.
- El producto se entiende en una sola toma → no fuerces 4 stories por inercia.
- Es contenido pensado para quedar permanente en el feed → eso es **carrusel**, no stories.
- El user quiere "3 versiones" o "3 conceptos" del mismo mensaje → eso son **drafts independientes** de UNA story (`ig-story` × N), NO una secuencia narrativa.
