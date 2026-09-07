---
name: creative-execution
description: "Cómo se produce cada pieza en un proyecto de Indash Studio (cwd con .indash/ y manifiestos .indash) — el proceso completo por creativo: conocer el producto con sus fotos reales, elegir refs, componer por capas, generar candidatos versionados, verificarse con view_creative y commitear. Usala SIEMPRE que haya que generar/regenerar la imagen de un creativo de Studio, sea trabajo directo o despachado como subagent. Las decisiones de QUÉ producir (arquetipo, copy, componer/generar) vienen escritas del brief; esta skill es el CÓMO."
language: es
tags: execution
owner: lburgwardtr
status: draft
reviewed: 2026-09-02
---

# Creative Execution — producir una pieza en Studio

Sos el que produce UNA pieza (o varias, de a una). Da igual si sos el chat
principal trabajando directo o un subagent despachado: **el proceso es el
mismo**. El contrato de disco (schema, candidatos, orden de escritura) está en
el CLAUDE.md del proyecto; acá está el OFICIO.

## Antes que nada: acá todo se construye por CAPAS

Un creativo NO es una imagen plana. Es un manifiesto `.indash` con un scene
graph: la escena/fondo como capa `image`, el texto como capas `text`, el logo
como capa `image` (SVG de `library/logos/`, recoloreable), scrims y bloques
como `rect`. La IA genera SOLO lo orgánico — todo lo que tiene respuesta
exacta (texto, logo, precio, badges, iconos) va como capa y se renderiza
nítido en cualquier export. El schema completo está en el CLAUDE.md del
proyecto. **Si te encontrás pidiéndole texto o logos al modelo de imagen,
pará: eso es una capa.**

Cómo se compone esa capa de texto (placement, jerarquía, contraste, densidad
de diseño) vive en `style/composicion-texto.md` — leelo antes de armar las
capas de una pieza con texto.

## La foto real es una OPCIÓN — tenela siempre en el radar

Generar no es la única vía: la pieza también puede armarse CON la foto real.
Es una decisión por pieza (idealmente ya escrita en el plan como
componer/generar), no una jerarquía fija:

- Producto-sobre-fondo, brand-flat, precio+packshot → suele ganar el
  **cutout de la foto real** (`mcp__indash__remove_background` te da el PNG
  con alpha) como capa `image` sobre un `rect`/gradient de marca: cero
  alucinación, fidelidad perfecta.
- La foto real (cruda o procesada) también puede SER el candidato de la capa
  ai-gen: copiala como `vN.<ext>` (su formato original) + sidecar anotando el origen
  (`"source": "library-photo"`, sin `model`).
- Lifestyle, contexto, escena → se genera (con las fotos reales de `refs`,
  como siempre).

## El proceso por pieza (en orden, sin saltear)

### 1 · Conocé el producto ANTES de generar

Si la pieza lleva producto en escena (lo dice el plan / las instrucciones):

- Leé `library/products/<producto>/product.json`. Si **no existe**, crealo
  ahora (ver "product.json" abajo): abrí con Read TODAS las fotos de
  `library/products/<producto>/` (si no hay fotos, bajalas con
  `mcp__indash__pull_product_images`), miralas de verdad y anotá.
- **Nunca** generes desde la descripción de `products.md`: es copy de
  e-commerce, no descripción visual. De ahí salen productos deformados.

Si la pieza NO lleva producto (lifestyle puro, pieza de marca): la decisión
tiene que estar escrita en el plan o en tus instrucciones. Si no está escrita,
frená y preguntá — no la tomes solo.

### 2 · Elegí refs con criterio

- 2-3 fotos del producto según lo que pide la pieza (frente / perfil /
  detalle / en uso), elegidas leyendo `product.json` (campo `use` de cada
  foto). Una foto **clara** del producto vale más que cualquier descripción.
- Las refs van SIEMPRE en `refs` de `mcp__indash__generate_image`. Una pieza
  con producto y `refs: []` está mal hecha, sin excepciones.

### 3 · El prompt: la foto manda, el texto acompaña

El manual completo de escritura del prompt — las 7 leyes del prompting
cinematográfico, edit vs generate, personas, trucos por tipo de producto y
anti-patrones — está en `reference/prompt-craft.md`. **Leelo antes de escribir
el primer prompt de la sesión.** Lo innegociable:

- Identificación textual **mínima** del producto: qué es + color base
  ("black baby stroller"). Los atributos los pone la foto. Describir el
  producto en detalle por texto es la causa #1 de deformación: si el texto
  está mal, el producto sale mal. Subir el peso del texto es una excepción
  deliberada que se anota en el sidecar, no un default.
- **Los logos DEL producto se quedan.** Si la pieza pide "sin logos", eso
  significa sin logos/watermarks *agregados* — jamás le pidas al modelo que
  borre el branding del propio producto. En caso de duda: el producto va
  siempre con sus logos.
- El prompt describe SOLO la escena orgánica (fondo, luz, encuadre, **espacio
  negativo donde van a caer las capas de texto**). Texto, logo de marca,
  precio, badges → **capas del manifiesto**, nunca quemados en el pixel.

### 4 · Modelo y resolución (decisión explícita, no default ciego)

**La escalera de modelos** — se arranca abajo y se sube solo si hace falta:

1. `nano-banana-2` — **el default, para casi todo**: es el que mejor rinde
   en general (producto, lifestyle, personas, fondos).
2. `gpt-image-2` — el segundo intento de fidelidad cuando nano-banana-2 no
   sale, o cuando manda una gráfica orgánica compleja dentro de la imagen.
3. `nano-banana-pro` — el último recurso, para el caso puntual de fidelidad
   que los dos anteriores no resolvieron.

**No existe "gpt-image para texto".** Esa matriz era del mundo viejo, donde
el texto se le pedía al modelo. Acá el texto es una capa: si sentís que
necesitás un modelo "que renderice texto legible", la pieza se COMPONE — pará
y armá las capas.

**Resolución** (`resolution`, modelos nano): **`1K` por default; `4K` cuando
la pieza pide detalle fino** — texto chico DENTRO de la imagen (el del propio
producto), labels y logos del producto que tienen que quedar legibles. Subir
a 4K arregla más problemas de texto/logo ilegible que cambiar de modelo.

Banderas rojas → no insistas con lo mismo: texto alucinado/espejado en la
imagen → era una capa (o 4K si es texto del propio producto); producto que
pierde detalles del label → mejores refs + 4K antes que otro modelo.

### 5 · Generá al candidato, versionado completo

- `out_dir: "<carpeta-del-creativo>/layers/<layerId>"`, `name: "vN"` donde
  vN = máximo existente + 1 contando cualquier extensión (nunca pises un vN:
  son append-only y el guard te va a frenar).
- La tool guarda en el formato que devuelve el modelo (casi siempre `vN.jpg`)
  y te devuelve el path exacto. **Nunca lo conviertas a PNG**: son los mismos
  píxeles a 5–10× el peso. Guardá ese nombre para el commit.
- Sidecar `vN.json` INMEDIATAMENTE después de generar — no al final, no
  "después lo escribo": modelo, prompt, refs, `by`, `createdAt`. **Un
  candidato sin sidecar no existe**: es una generación imposible de auditar
  y de reproducir. (Caso real: la pieza más retrabajada de un brief terminó
  con candidatos sin sidecar justo donde más importaba el registro.)

### 6 · Reintentos: se ESCALA, nunca se degrada

Si el candidato salió mal, el siguiente intento lleva:

- **mismas refs o más** (o una ref mejor elegida — releé `product.json`),
- **un peldaño ARRIBA en la escalera** (nano-banana-2 → gpt-image-2 →
  nano-banana-pro) o `resolution: "4K"` si lo que falla es detalle fino,
- **prompt más preciso** (corregí LO que falló, no reescribas todo — ver
  "EDIT vs GENERATE" en `reference/prompt-craft.md`),
- o el cambio de vía: **la foto real** (cutout + composición) si generando no
  sale.

Prohibido soltar refs o aflojar restricciones para "probar otra cosa": ese
camino termina siempre igual — producto inventado y el humano subiendo la
foto a mano. Si después de 3 candidatos no sale: **pará y reportá** qué
probaste y qué falla (el humano decide), no aflojes.

### 7 · Verificate MIRANDO, contra el checklist del formato

`mcp__indash__view_creative { creative: "<carpeta>" }` después de CADA
candidato — la imagen compilada te llega en el resultado. **No uses `Read`
sobre los `vN.<ext>`**: son imágenes de 4096² que entran enteras al transcript
y no muestran la composición; view_creative ya te da la
pieza compilada al tamaño justo. Chequeá contra
`formats/<formato>.md` de esta skill (y sus safe zones en
`data/safe-zones.json`):

- **Bloquean** (→ candidato nuevo o ajuste de capas): texto/logo fuera de
  safe zone, overflow de texto, producto deformado o sin sus logos.
- **Advierten** (seguí, pero anotalo en tu reporte): contraste justo, paleta
  que se aleja de la marca, composición de texto perezosa (placement clonado
  entre piezas hermanas — ver `style/composicion-texto.md`).

Ajustes de capas no-AI (márgenes, tamaño de texto, scrim) se hacen acá y no
gastan candidato.

### 8 · Commit

Una sola edición final del manifiesto: `active` = el nombre del archivo que
guardó la tool (`"vN.jpg"`; `"vN"` a secas significa `vN.png`), `meta.status:
"review"`, `meta.generating: false`, `meta.updatedAt`. Después una línea en
`history.jsonl`. El orden candidatos-PRIMERO / manifiesto-AL-FINAL no es
opcional: el manifiesto es el commit point que dispara el Board.

## product.json — la memoria visual del producto

`library/products/<producto>/product.json`. Lo escribe el PRIMERO que
necesita el producto (idealmente en `new-brief`, si no acá); los demás lo
leen en vez de re-mirar 30 fotos por pieza. Se re-escribe libre cuando
cambian las fotos.

```json
{
  "product": "carriola-kobu",
  "analyzedAt": "2026-08-13T12:00:00Z",
  "summary": "Carriola negra de bastidor plateado, capota 300D mate, ruedas de goma negras. 3 líneas FACTUALES: lo que se VE en las fotos, no el copy.",
  "photos": [
    { "file": "3c8cc6de849482cf.webp", "view": "perfil", "quality": "buena",
      "use": "hero lateral, modo moisés", "notes": "fondo gris limpio" },
    { "file": "c39d7b98...webp", "view": "frente", "quality": "regular",
      "use": "solo como ref secundaria", "notes": "sombra dura" }
  ],
  "avoid": ["render 3D del fabricante", "fotos con watermark"]
}
```

- `view`: frente | perfil | 3-4 | detalle | en-uso | packshot.
- `quality`: buena | regular | mala — una foto `mala` no se usa de ref.
- `summary` y `notes` salen de MIRAR las fotos. Si una foto está pixelada,
  con watermark o es un render que no coincide con el producto real: a
  `avoid`.

## Formatos

| Formato | Archivo | Canvas |
|---|---|---|
| Story / Reels | `formats/story.md` | 1080×1920 |
| Feed 4:5 y cuadrado | `formats/feed.md` | 1080×1350 / 1080×1080 |
| Carrusel | `formats/carrusel.md` | 1080×1350 por slide |

Los números de safe zones viven en `data/safe-zones.json` (una sola fuente).
Se actualizaron a la zona unificada de Meta (marzo 2026) y al crop 3:4 de la
grilla de perfil — no uses números de memoria: leé el JSON.

## Estilo y referencia

- Cómo escribís el PROMPT (7 leyes, edit vs generate, personas, anti-patrones)
  → `reference/prompt-craft.md`
- Cómo componés el TEXTO y la gráfica por capas (placement, jerarquía,
  contraste, densidad de diseño) → `style/composicion-texto.md`

## Si sos un subagent despachado

Tu nota de despacho trae el scope (tu carpeta) y las instrucciones de TU
pieza. Además del proceso de arriba:

- Primera acción: `meta.generating: true` en TU manifiesto (el humano ve la
  card pulsar). Última acción: el commit (paso 8).
- Escribís SOLO dentro de tu carpeta. No toques otros creativos, plan.json,
  rounds/, .indash/.
- Tu último mensaje: 1-2 líneas — qué generaste, cuántos candidatos, y
  cualquier warning (advertencias del paso 7, refs dudosas, product.json
  desactualizado).

## Reglas no-negociables

1. **Siempre** todo lo que tiene respuesta exacta (texto, logo, precio,
   badge, ícono) va como CAPA del manifiesto. Pedírselo al modelo de imagen
   está prohibido — y necesitar "un modelo que renderice texto" es la señal
   de que la pieza se COMPONE, no se genera.
2. **Siempre** leés `product.json` (o lo creás mirando TODAS las fotos) antes
   de generar una pieza con producto. Nunca generás desde el copy de
   `products.md`.
3. **Siempre** las fotos reales del producto van en `refs`. Una pieza con
   producto y `refs: []` está mal hecha, sin excepciones.
4. **Siempre** la escalera de modelos se sube, nunca se baja: nano-banana-2 →
   gpt-image-2 → nano-banana-pro, y `4K` para detalle fino. Reintentar
   soltando refs o bajando de modelo está prohibido.
5. **Siempre** candidato `vN` = máximo + 1 contando cualquier extensión
   (append-only), guardado en el formato que devolvió la tool — nunca
   convertido a PNG — y sidecar `vN.json` inmediato. Un candidato sin sidecar
   no existe.
6. **Siempre** candidatos y sidecars PRIMERO, manifiesto AL FINAL. El
   manifiesto es el commit point.
7. **Siempre** verificás MIRANDO con `view_creative` después de cada
   candidato, contra el checklist del formato y las safe zones del JSON.
8. **Nunca** editás un creativo `approved`, ni tocás `rounds/`, `versions/`,
   `.indash/` ni `plan.json` (si sos ejecutor).
9. **Siempre** después de 3 candidatos fallidos parás y reportás. No aflojás
   restricciones para "probar otra cosa".
10. **Agnóstico** por marca, vertical y categoría: la estética sale del brief,
    la marca del proyecto y las refs — nunca de prejuicios sobre el rubro.

## Punto de entrada

Leé las instrucciones de TU pieza (plan/notes o nota de despacho) y **arrancá
por el paso 1: conocé el producto**. Si la pieza tiene texto, pasá por
`style/composicion-texto.md` antes de armar las capas.
