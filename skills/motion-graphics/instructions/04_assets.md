# 04 — Material real

Objetivo: cada elemento de la columna "fuente" del storyboard existe como archivo en `assets/`.

## Qué es "representar al producto"

| Sale del material real, siempre | Se puede diseñar |
|---|---|
| Pantallas, botones, cards y checks de la app | Títulos, captions y CTA del guion |
| Logo y sus versiones | Marcas de highlight, círculos de tap |
| Íconos, símbolos e ilustraciones de la marca | El "problema" (el competidor genérico, sin marca) |
| La tarjeta, el empaque, el producto | Partículas, fondos y mundos 3D en la paleta |
| End cards, badges y música oficiales | Transiciones hacia el end card |

Si algo de la columna izquierda no existe en el material, se omite o se pide. Nunca se dibuja.

## De las grabaciones (rama app)

1. **Frame limpio**: `ffmpeg -ss <t> -i rec.mp4 -frames:v 1 screen-<nombre>.png`, en un
   momento sin scroll ni transición. Mirá el frame antes de usarlo.
2. **Coordenadas**: `ui_crops.py boxes` (cards blancas y botones oscuros) y `ui_crops.py rows`
   (líneas de texto, para ubicar un highlight exacto).
3. **Pop-outs**:
   - con fondo: `ui_crops.py crop` (esquinas redondeadas, x2);
   - sin fondo (una ilustración sobre el color plano de la app): `ui_crops.py key --bg R,G,B`.
4. **El hueco que deja un pop-out** se tapa con un parche del color de fondo muestreado
   de la misma captura.
5. **El punto rojo de grabación de iOS** se tapa con un cover por pantalla, no uno global:
   si no, asoma en los push entre pantallas.
6. **Datos de la cuenta demo** (nombre, números de cuenta o de cliente): anotalos para
   la entrega. El cliente confirma si se pueden publicar.

## Del manual en PDF

- **Vectores** (íconos, símbolos, logo): `pdf_paths.py MANUAL.pdf <página> out/ --fill <hex>`.
  Cada path sale como SVG suelto: mirá cuáles son y renombralos.
- **Arte raster**: `pdftoppm -r 288 -f N -l N -png` y recorte. Si la página usa multiply
  sobre blanco, sacá el fondo con flood-fill desde el borde del recorte.
- Si los íconos son texto en una fuente de íconos, no hay vector: rasterizá en alta.

## Del sitio

`capture/assets/` trae imágenes y SVGs. Bajá también las tipografías del `fonts-manifest.json`
a `assets/fonts/`.

## Assets oficiales

- **End card**: va tal cual, sin recolorear ni recortar, a pantalla completa los últimos
  1.5–2.5 s. La transición hacia él sí se diseña (un iris desde el tap del CTA, la O del
  logo que se abre).
- **Variante**: elegí la que continúa el color en que termina la pieza, y nombrá las
  otras en la entrega.
- **Badges de tiendas**: los oficiales. Si no llegaron, una pastilla de texto, y lo avisás.

Listo cuando no queda ninguna fila del storyboard sin archivo. Siguiente: `05_audio.md`.
