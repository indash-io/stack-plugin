---
name: ig-carousel
description: "Reglas de formato para carruseles de Instagram (4:5, N slides con narrativa cross-slide). Se carga cuando la pieza es un carrusel. Cubre: aspect ratio, narrativa hook→desarrollo→CTA, arquetipos, consistencia entre slides."
language: es
---

# Format — Instagram Carousel

Skill de **formato puro** para carrusel multi-slide.

## Specs técnicas

- **Aspect ratio**: 4:5 vertical (estándar de feed).
- **Resolución**: 1080x1350.
- **Slides típicos**: 3 a 8. **Default razonable: 4–5.**
- **Aspect ratio**: pasalo siempre como **`aspect_ratio: "4:5"`** en `generate_image`. NO lo escribas en el texto del prompt — es parámetro de la tool.
- **Cierre del prompt** (sí va en el texto, sin aspect): *"fotografía editorial de alto detalle, fotorrealista, foco nítido en el producto."*

## Narrativa cross-slide

A diferencia de stories (secuencia rápida con auto-advance), el carrusel **se navega manualmente**. El usuario decide swipear o no — la primera slide tiene que comprometer.

Estructura clásica:

| Slide | Función |
|---|---|
| 1 (hook) | Detener el scroll en el feed. Pregunta provocadora, claim contraintuitivo, número crudo, contraste visual fuerte. **Vende el resto del carrusel.** |
| 2..N-1 (desarrollo) | Cumplir con la promesa del hook. Cada slide aporta algo nuevo (un beneficio, un dato, una prueba, una escena). Variar ángulo y escena. |
| N (CTA) | Cerrar con acción clara: link en bio, código de descuento, próximo lanzamiento. Composición frontal, copy directo. |

## Copy on-image

- **Hook**: 4–8 palabras potentes. Centrado o jerarquizado.
- **Desarrollo**: 8–14 palabras. Puede ser claim + sub-claim.
- **CTA**: 3–6 palabras de acción + indicador visual ("→ link en bio", "ver más", flecha).

Una slide = un bloque de texto principal. No metas dos titulares enfrentados.

## Arquetipos de carrusel

Cuando proponés la idea (etapa 1), elegí un arquetipo y justificá en una línea por qué encaja con el pedido:

| Tipo | Cuándo usarlo | Ejemplo |
|---|---|---|
| **Educativo** | Producto cuyo valor requiere explicación (ingredientes, tecnología, uso). | "Por qué este shampoo funciona en pelo graso" |
| **Listicle** | Beneficios o razones numerables. | "3 razones para cambiar a esta crema" |
| **Hot take / contraste** | Hook contraintuitivo o polémico. | "No, NO necesitás 10 productos de skincare" |
| **Caso de estudio** | Antes/después, transformación, prueba social. | "Probamos la crema durante 30 días" |
| **Storytelling** | Marca con historia a contar. | "De cómo dejamos de usar parabenos" |
| **Promo** | Lanzamiento, descuento, evento. | "Nueva línea — descuento solo esta semana" |

## Consistencia entre slides

Aplica Ley 7 de `prompt-craft` (consistencia entre piezas). Para carrusel específicamente:

- **Lente igual** en todas. Mezclar 35mm y 85mm en el mismo carrusel desarma la sensación de "una sesión".
- **Paleta heredada** del producto + máximo 2 colores ambientales (madera, piedra, plantas).
- **Mood consistente** — una palabra que define el carrusel entero (*"calma editorial"*, *"oficio caliente"*, *"ritual matinal"*).
- **Variación sí**: ángulo, distancia (un slide cerrado, otro abierto), presencia/ausencia de persona.

## Cuándo el carrusel NO es la respuesta

- El user quiere algo rápido y de impacto único → mejor un **post (1 imagen)** o una **story**.
- El producto se entiende en una sola toma → no fuerces 5 slides solo por inercia.
- Es contenido secuencial efímero (24h) → eso es **stories**, no carrusel.

Si tenés dudas, sugerí el formato más simple primero al user y subí en complejidad si lo pide.
