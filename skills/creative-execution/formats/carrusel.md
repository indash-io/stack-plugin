# Carrusel — 1080×1350 por slide (3-7 slides, default 4)

Un carrusel en Studio son N creativos hermanos en un grupo del plan (un
manifiesto por slide), no una imagen larga.

## Por qué se navega distinto (y qué cambia en el diseño)

A diferencia de la secuencia de stories (auto-advance: el ojo no elige), el
carrusel **se navega a mano**: el usuario decide swipear o no. Consecuencias
directas:

- El slide 1 **vende el resto del carrusel** — se diseña como un feed post
  con scroll-stop propio (compite solo en el feed).
- El swipe se gana slide a slide: cada uno tiene que pagar el anterior.
- El borde derecho puede sugerir continuidad (elemento cortado, flecha) — es
  legítimo y funciona.

## Estructura narrativa

Cada slide tiene UNA función — el carrusel se diseña como secuencia (el
arquetipo y el copy vienen decididos en el bloque del brief):

1. **Hook** (slide 1): la promesa o el problema. Pregunta provocadora, claim
   contraintuitivo, número crudo, contraste visual fuerte.
2. **Desarrollo** (slides 2..n-1): un beneficio/prueba/feature POR slide.
   No metas dos ideas en un slide; agregá un slide.
3. **CTA** (último): accionable — verbo + acción concreta ("→ link en bio",
   código, lanzamiento). Nunca un "gracias" ni un cierre poético.

Largo del copy por función (guía, el texto exacto viene del brief): hook 4-8
palabras · desarrollo 8-14 (claim + sub-claim) · CTA 3-6 + indicador visual.
**Un slide = un bloque de texto principal** — no metas dos titulares
enfrentados.

## Consistencia entre slides (lo que hace carrusel al carrusel)

- **Mismo sistema visual**: mismo modo (minimalista / lifestyle /
  brand-flat), misma paleta, misma tipografía, mismo tratamiento de fondo.
  Un template claro U oscuro — no alternes.
- **El producto reconocible en todos los slides** donde aparece: mismas refs
  en cada generación (no "parecidas" — las mismas). Mismo lente y mismo mood
  en toda la secuencia (Ley 7 de `../reference/prompt-craft.md`).
- Sistema gráfico recurrente como capas compartidas: indicador de progreso
  (2/5), brand mark, mismo placement del título. Armá el primer slide,
  verificalo, y usá su manifiesto como base de los demás.
- **Lo que SÍ varía**: ángulo, distancia (un slide cerrado, otro abierto),
  escena, y el placement del texto entre slides de desarrollo
  (`../style/composicion-texto.md`).

## Densidad de diseño

Un slide "objeto flotando + título" repetido N veces se ve virgen de diseño.
Cada slide de desarrollo lleva al menos un dispositivo: dato destacado
(número grande como capa de texto), comparación, pill/badge, detalle de
producto en zoom. Todo lo que tenga respuesta exacta (números, labels) va
como CAPA, no generado. Catálogo completo en `../style/composicion-texto.md`.

## Checks específicos

- ¿El slide 1 funciona SOLO en el feed? (es la puerta de entrada)
- ¿Producto idéntico entre slides? (mismas refs → bloquea si muta)
- ¿Sistema visual consistente (paleta/tipo/template) en toda la secuencia?
- ¿Cada slide de desarrollo tiene su dispositivo de diseño?
- ¿El último slide es CTA accionable?
- Safe zones de feed 4:5 en cada slide (`../data/safe-zones.json`) — incluido
  el crop 3:4 de la grilla en el slide 1 (es el que aparece en el perfil).
