# Feed — 4:5 (1080×1350) y cuadrado (1080×1080)

## Safe zones (bloquean)

`../data/safe-zones.json`: en el feed no hay UI encima, pero dos cosas comen
bordes:

- **Respiración**: nada pegado al borde — 64px mínimos arriba/abajo.
- **La grilla de perfil recorta a 3:4** (cambio de Instagram, fines de 2025):
  a un 4:5 le come **~34px por lado**; a un cuadrado, **~135px por lado**.
  Por eso los márgenes laterales canónicos son 100px en 4:5 y 140px en 1:1.
  Lo esencial (producto + claim + logo) tiene que sobrevivir ese crop.

## Estructura

El feed aguanta más densidad que una story, pero la jerarquía sigue siendo
una sola:

- **Título** con peso (display de la marca), **beneficio o claim** como
  apoyo, **logo** discreto (esquina o centrado arriba), precio/badge como
  bloque si aplica.
- El post compite en un feed infinito: el scroll-stop lo da la IMAGEN (luz,
  color, composición), no la cantidad de texto.
- Modos visuales (elegí uno, no mezcles): **minimalista** (producto +
  espacio negativo + tipografía), **lifestyle** (producto en contexto de
  uso, luz natural), **brand-flat** (fondo de color de marca + composición
  gráfica — acá casi siempre conviene COMPONER, no generar: cutout de la
  foto real con `remove_background` sobre un `rect` de marca).

## Composición

Manual completo en `../style/composicion-texto.md`. Lo mínimo:

- Texto sobre foto → scrim degradé (rect + gradient) o zona de la imagen
  pedida limpia en el prompt.
- Bloques de color/pills → capas `rect` con `cornerRadius`, no pedidos al
  modelo.
- Logo → capa `image` desde `library/logos/` (SVG directo, `recolor` si hace
  falta invertirlo), nunca generado.
- Piezas de desarrollo: al menos un dispositivo de diseño (dato destacado,
  pill, comparación) — nada de "objeto flotando + título".

## Imagen orgánica

- Con producto: `nano-banana-2` + 2-3 refs (`resolution: "4K"` si el label
  del producto tiene texto chico); encuadre que deje aire donde va el texto.
- Cuadrado: pensá la composición radial/centrada — el 4:5 recortado no es un
  cuadrado bien compuesto.

## Checks específicos

- ¿Sobrevive el crop 3:4 de la grilla? (producto + claim + logo dentro de la
  franja central — bloquea)
- ¿Texto a ≥64px de arriba/abajo y ≥100px (4:5) / ≥140px (1:1) de los lados?
  (bloquea)
- ¿El logo es capa (nítido) y no salió generado en el pixel? (bloquea)
