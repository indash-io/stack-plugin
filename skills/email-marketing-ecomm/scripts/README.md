# Scripts — Render

## Setup (una sola vez)

```bash
cd scripts
npm install
```

Esto instala Puppeteer (Chromium headless) en ~200MB. Solo hace falta una vez.

## Uso

Desde la raíz del skill:

```bash
node scripts/render.js exports/emails/2026-04-23_3x2-ice-roller_v1
```

(El script toma cualquier carpeta con `.html` como argumento; los exports viven en `exports/emails/<AAAA-MM-DD>_<campaña-slug>_v<N>/` de la carpeta del cliente.)

El script toma todos los `.html` de la carpeta y genera un `.png` full-page para cada uno, en la misma carpeta.

## Qué hace

- Abre cada HTML en un Chromium headless
- Setea viewport 600px (ancho real de email)
- Espera que carguen imágenes externas
- Captura screenshot full-page (scroll completo)
- Guarda como PNG a 2x (retina)

## Troubleshooting

- **Error de Chromium no encontrado:** `npx puppeteer browsers install chrome`
- **Imágenes en blanco:** revisar que las URLs de las imágenes sean accesibles públicamente
- **Mail cortado:** aumentar el viewport height inicial en `render.js` (línea con `setViewport`)
