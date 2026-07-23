# Template — Estructura de carpetas del cliente

Esta es la estructura estándar que crea la skill. `{slug}` es el nombre del cliente en kebab-case (ej: `acme-foods`). Se crea en el directorio de trabajo actual. Es la **convención unificada del stack Indash**: la misma carpeta es un proyecto del **Indash Studio** (el editor de piezas), así que todo lo que produzcas acá se puede abrir/editar ahí sin migración.

```
{slug}/
  CLAUDE.md                  Contexto de marca del cliente (fuente de verdad). Lo escribe el paso 4.
  creatives/                 Scene graphs JSON del Indash Studio. Arranca vacía (.gitkeep).
  assets/
    logos/                   TODOS los logos del cliente (de Indash o del user). .gitkeep.
    fonts/                   TODAS las tipografías (.otf/.ttf/.woff2). .gitkeep.
    brand-kit/               brand.md (narrativa) + brand-kit.md (resumen estructurado:
                             paleta hex, tipografía, do's & don'ts) + guidelines crudas (PDF).
    products/                index.md (catálogo del MCP de Indash, paso 5) + imágenes de
                             referencia por producto. .gitkeep.
    references/              Referencias de estilo / competidores. .gitkeep.
  exports/
    carruseles/              Output de carruseles. Archivos: <AAAA-MM-DD>_<slug>_v<N>.md
    stories/                 Output de stories-nano-banana. Misma nomenclatura.
    ads/                     Output de ads.
    videos/                  Output de ugc-video-prompts y seedance-multishot.
    emails/                  Output de email-marketing-ecomm.
  briefs/                    Briefs, pedidos y notas del cliente. .gitkeep.
```

## Notas

- **`CLAUDE.md`** es el archivo crítico: es lo que las skills (y el claude embebido del Studio) heredan al trabajar en esta carpeta. Su contenido gana sobre defaults genéricos.
- **NO crees** `versions/` ni `.indash/` — son del Studio y las maneja él (`versions/` = snapshots de creatives; `.indash/` = estado privado: comments, sesión del agente). Si existen, no las toques.
- **Dónde va cada asset de marca** (regla fija):
  - **Logos** → `assets/logos/` (siempre, todos).
  - **Tipografías** (archivos de fuente) → `assets/fonts/` (el Studio las levanta de acá para el canvas).
  - **Brand kit crudo / guidelines** (PDF u otros) + `brand.md` + `brand-kit.md` → `assets/brand-kit/`.
  - **Imágenes de referencia de producto** → `assets/products/` (junto al `index.md`).
  - **Referencias de estilo / competidores** → `assets/references/`.
- **De dónde salen los assets**: primero se intentan **descargar desde el MCP de Indash**. Si la marca no está en Indash, el user pasa los archivos a mano y se ordenan en `assets/`. Ver `instructions/02_discovery.md`.
- **`assets/products/index.md`** es el puente con el MCP de Indash: nombre + URL + imagen de cada producto, inputs de las skills de contenido.
- Las carpetas que arrancan vacías llevan un `.gitkeep` para quedar versionables.
- **Nomenclatura de entregables**: `<AAAA-MM-DD>_<producto-slug>_v<N>.md` dentro de `exports/<tipo>/` (convención global del stack, vive en `stack-policy.md`). No la redefinas por cliente.
- Si la carpeta `{slug}/` ya existe, la skill frena y pregunta antes de tocar nada (no pisa).
