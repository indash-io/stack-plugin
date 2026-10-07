# 02 — Research

Objetivo: tres cosas escritas en el `STORYBOARD.md` antes de pensar una sola escena.

## 1. Capturá la fuente

- **Sitio** → `npx hyperframes capture <URL> -o capture`:
  - `screenshots/` (scroll completo y contact sheet);
  - `assets/` (imágenes y `logo-*.svg`);
  - `extracted/visible-text.txt`, `design-styles.json`, `tokens.json`, `fonts-manifest.json`.

  Los `logo-*.svg` son candidatos: rasterizalos y miralos antes de usar uno. Recorré
  también las páginas internas que mencione el home (precios, cómo funciona, FAQ).
- **App** → el guion es la estructura. Extraé un frame cada 0.5 s de cada grabación
  (`ffmpeg -i rec.mp4 -vf fps=2 f_%04d.png`), revisalos con `contact_sheet.py` y armá el
  índice de pantallas: pantalla → grabación → segundo del frame más limpio.
- **Manual de marca** → leelo entero. Anotá las páginas que tienen arte reutilizable
  (íconos, símbolos, ilustraciones, logo).

## 2. La UVP en una frase

Para quién, qué le resuelve, y por qué no es lo mismo que la alternativa. Si la marca
tiene una línea de campaña propia, esa es la columna de la pieza.

## 3. El ledger de claims

| Claim | Fuente (URL, página del PDF, escena del guion) | Literal en pantalla |
|---|---|---|
| 4.9★ en Google | marca.com, home | sí |

- Los números van exactos y con su unidad.
- Si el guion avisa una limitación ("tal estudio todavía se agenda por teléfono"), anotala
  como **no-claim**: la pieza no puede prometer lo contrario.
- Copy y locución salen solo de acá (regla 3).

## 4. La ficha de marca

- **Paleta**: hex y rol de cada color (fondo, texto, acento, estado). Cuáles combinan entre sí.
- **Tipografías**: los archivos reales (del sitio vía `fonts-manifest.json`, o del
  paquete de marca), servidos local con `@font-face`. Si no hay archivo, usá la de Google
  Fonts más cercana y anotalo para la entrega.
- **Logo**: SVG real y sus versiones aprobadas (positivo, negativo, sobre qué fondos).
- **Vocabulario**: palabras que la marca usa y palabras prohibidas (una marca para
  mayores puede decir "miembros" y prohibir "abuelitos").
- **Sistema de símbolos**: los íconos o personajes propios, que después son las metáforas
  de cada pilar (un animal, un paisaje, un objeto del manual).
- **Cómo se mueve la marca**: los easings y animaciones del sitio
  (`extracted/animations.json`), si dicen algo.

Listo cuando las tres secciones están en el `STORYBOARD.md`. Siguiente: `03_storyboard.md`.
