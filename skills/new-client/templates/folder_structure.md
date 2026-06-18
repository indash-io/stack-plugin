# Template — Estructura de carpetas del cliente

Esta es la estructura estándar que crea la skill. `{slug}` es el nombre del cliente en kebab-case (ej: `acme-foods`). Se crea en el directorio de trabajo actual.

```
{slug}/
  CLAUDE.md                  Contexto de marca del cliente (fuente de verdad). Lo escribe el paso 4.
  brand/
    brand.md                 Narrativa de marca: qué es, de qué se trata, posicionamiento, tono. Complemento legible.
    brand-kit.md             Resumen estructurado: paleta (hex), tipografía, do's & don'ts. Lo arma Discovery.
    logos/                   TODOS los logos del cliente (descargados de Indash o provistos por el user). .gitkeep.
    typographies/            TODAS las tipografías del cliente (archivos .otf/.ttf/.woff). .gitkeep.
    assets/                  Brand kit crudo y guidelines originales (PDF, etc.) tal como los baja Indash o los tira el user. .gitkeep.
  productos/
    index.md                 Índice de productos traído del MCP de Indash. Lo llena el paso 5.
    referencias/             Imágenes de referencia por producto (input de las skills). .gitkeep.
  entregables/
    carruseles/              Output de carrusel-nano-banana. .gitkeep.
                             Archivos: <AAAA-MM-DD>_<producto-slug>_v<N>.md
    stories/                 Output de stories-nano-banana. .gitkeep.
                             Archivos: <AAAA-MM-DD>_<producto-slug>_v<N>.md
  briefs/                    Briefs, pedidos y notas del cliente. .gitkeep.
```

## Notas

- **`CLAUDE.md`** es el archivo crítico: es lo que las skills heredan al trabajar en esta carpeta. Su contenido gana sobre defaults genéricos.
- **`brand/`** es el hogar de TODO lo de marca. Regla fija de dónde va cada cosa:
  - **Logos** → `brand/logos/` (siempre, todos).
  - **Tipografías** (archivos de fuente) → `brand/typographies/` (siempre, todas).
  - **Brand kit crudo / guidelines** (PDF u otros) → `brand/assets/`.
  - **`brand/brand.md`** = narrativa legible de la marca (qué es, posicionamiento, tono). **`brand/brand-kit.md`** = el resumen estructurado (paleta con hex, tipografía, do's & don'ts).
- **De dónde salen los assets de marca**: primero se intentan **descargar desde el MCP de Indash** (la brand cargada en la app). Si la marca no está en Indash, el user puede **pasar los archivos a mano** (un PDF del brand kit, los logos, las fuentes) y se guardan en las carpetas de `brand/` que correspondan. Ver `instructions/02_discovery.md`.
- **`productos/index.md`** es el puente con el MCP de Indash: ahí viven nombre + URL + imagen de cada producto, que son los inputs de las skills de contenido.
- Las carpetas que arrancan vacías llevan un `.gitkeep` para quedar versionables.
- **Nomenclatura de entregables**: las skills de carrusel y stories guardan acá con el nombre canónico `<AAAA-MM-DD>_<producto-slug>_v<N>.md` (la convención completa vive en la política del stack, `stack-policy.md`). No la redefinas por cliente — es global.
- Las imágenes de **referencia de producto** van en `productos/referencias/`; las pesadas conviene linkearlas al Drive.
- Si la carpeta `{slug}/` ya existe, la skill frena y pregunta antes de tocar nada (no pisa).
