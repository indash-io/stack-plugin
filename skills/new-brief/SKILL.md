---
name: new-brief
description: "Armado de un brief en un proyecto de Indash Studio (cwd con .indash/) — del insight crudo al Board listo para disparar producción: conseguir el material del humano (PDF, Word, texto), guardarlo como source, preparar los productos (fotos + product.json), proponer el plan con decisiones escritas por pieza (imágenes y videos), y scaffoldear los manifiestos. Usala cuando el humano la invoque en el chat de un brief o pida \"armá el brief / el plan del mes\", y cuando la app la dispare sola con un brief bajado del hub (existe source/brief.json: el material ya está, no se pide nada). No genera imágenes ni videos: eso es creative-execution / video-clips / video-composition — salvo que el brief venga del hub, donde después del scaffold seguís de corrido hasta el v1 de las imágenes y los stills de los videos."
language: es
tags: execution
owner: lburgwardtr
status: draft
reviewed: 2026-09-16
---

# New Brief — del insight crudo al Board listo

El output de esta skill es un Board disparable: plan aprobado, productos
preparados, manifiestos scaffoldeados. **Acá no se genera ni una imagen ni un
clip** — producir es `creative-execution` (imágenes), `video-clips` +
`video-composition` (videos).

## 0 · Punto de partida: el brief YA existe

El humano crea el brief desde la app, y eso ya creó la carpeta
`briefs/<brief>/` y esta sesión atada a él. **No crees ni nombres un brief
nuevo** — identificá el tuyo:

- El contexto de la conversación trae `Active brief: "<brief>"`, o
- `INDASH_SESSION_ID` (env) → buscá esa sesión en `.indash/sessions.json`
  y su campo `brief`.

Solo si nada de eso resuelve (sesión suelta, proyecto viejo), preguntale al
humano sobre qué brief trabaja.

## 1 · El insight (GATE — sin material no se propone nada)

Lo primero es el insumo: qué quiere lograr el humano con este brief.

- **¿Existe `briefs/<brief>/source/brief.json`? Entonces el brief bajó del
  hub (indash.ai) y el material YA está: no le pedís nada al humano.** La
  app lo dejó ahí al crear la sesión (`brief.json` es la fuente citable,
  `brief.md` la versión legible, y los adjuntos al lado) y mandó `/new-brief`
  sola. Leé `brief.json`: si `source` es `draft`, el brief es su `doc` (un
  `BriefDoc`, mapeo mecánico en el paso 3); si es `submission`, el brief son
  los archivos de `files[]`, que leés desde `source/<path>` (el `path` es
  relativo a `source/`, no hay URL) más `note`. Contrato completo:
  `reference/brief-doc.md`.
- ¿Ya está de otra forma? Mirá `briefs/<brief>/source/` y lo que vino en el
  chat.
- Si NO está, **pedíselo antes de proponer nada**: por lo general lo va a
  adjuntar como PDF o Word (a veces texto pegado o un link). Preguntá qué
  quiere lograr, para cuándo, y qué productos toca.
- Todo material que llegue por chat guardalo en `briefs/<brief>/source/`
  (es la fuente citable; los adjuntos ya referencian su archivo).
- Con el insight en mano, leé `library/brand/brand.md` y
  `library/products/products.md` ANTES de proponer nada.

## 2 · Preparación de producto (GATE — no se planifica sin esto)

Por cada producto que el brief toca:

1. ¿Están las fotos? `library/products/<producto>/` — si no,
   `mcp__indash__pull_product_images` (proyecto conectado) o pedíselas al
   humano (local).
2. ¿Existe `library/products/<producto>/product.json` y refleja las fotos
   actuales? Si no: **abrí TODAS las fotos con Read, miralas y escribilo**
   (schema en la skill `creative-execution`, sección "product.json"). Es el
   paso que garantiza que después no generes "de memoria": mirás las 30
   fotos UNA vez acá, y cada pieza (y cada sesión futura) lee tus
   conclusiones.
3. Fotos inutilizables (watermark, render que no coincide, pixelada) → al
   campo `avoid`, y avisale al humano si un producto quedó sin fotos buenas.

## 3 · El plan, con las decisiones ESCRITAS

Escribí `briefs/<brief>/plan.json` (schema en CLAUDE.md). Además de la
estructura (grupos por formato, ids kebab-case), cada creativo lleva en
`notes` las decisiones que después nadie tiene que adivinar:

- **¿Componer o generar?** Si la pieza es puramente tipográfica (sin
  producto ni escena: solo texto, logo, color) → se COMPONE (capas, sin
  generación). Todo lo que lleva producto o escena → se GENERA, también
  brand-flat y packshot sobre fondo liso (el producto va generado con sus
  fotos en `refs`). "Componer" nunca significa recortar la foto del producto
  con `remove_background`: eso es un último recurso de la ejecución, no una
  decisión del plan.
- **¿Capas o flat?** No es una decisión del plan: es el **modo de la sesión**
  (el humano lo prende para todo el brief desde la toolbar del Board; te
  llega en el bloque de foco y en `.indash/sessions.json`). Con flat prendido,
  cada imagen se genera de un saque, texto y logo en el pixel, sin capas — el
  scaffold cambia (abajo), el plan no.
- **¿Producto en escena o no?** Lifestyle sin producto es legítimo, pero se
  decide ACÁ y queda escrito — no se improvisa en el momento de producir.
- Con producto: cuál (`product_id`) y qué vista pide la pieza.

**Videos.** Un video es UN creativo del plan, no un grupo: lleva
`"kind": "video"` y `"seconds"` (obligatorio), y va en el grupo de su formato
junto a las imágenes. El grupo conserva solo `format`; `kind` y `seconds` son
del creativo. Un video es **un formato** — el 1:1 del mismo corte es otro
creativo en el grupo 1:1. En `notes` escribí lo que después nadie tiene que
adivinar: qué cuenta, cuántos clips UGC lleva (≈ `ceil(seconds / 10)`,
descontando packshot/placas), qué producto, si lleva packshot o logo al
cierre, y de dónde sale la música (la trae el humano — nunca se genera).

```json
{ "id": "g-story", "format": { "width": 1080, "height": 1920 }, "creatives": [
  { "id": "promo-01", "title": "Promo verano", "kind": "video", "seconds": 20,
    "notes": "UGC 2 clips + packshot al cierre, música del cliente" },
  { "id": "promo-01-still", "title": "Still promo" }
]}
```

El plan se corrige barato ANTES de correr 45 piezas; después cuesta 45
regeneraciones. Contale el plan al humano en 2-4 líneas y ajustá si te
corrige. plan.json es SOLO estructura — el estado vivo va en cada
manifiesto; y tiene un único escritor: vos, el chat de este brief.

### Si el brief viene del armador de briefs

Cuando el material de `source/` ya llega como **bloques por pieza** (el
formato de `reference/bloque-por-pieza.md` — el contrato entre ideación y
ejecución), el trabajo de este paso es **mecánico, no creativo**: cada bloque
ya trae la decisión componer/generar, el producto con su vista, el copy
on-image y las restricciones. Volcalo a `plan.json` + `notes` siguiendo la
tabla de mapeo del reference, **sin re-decidir nada** — y preguntá únicamente
lo que el bloque no trae. Un bloque completo = cero preguntas.

### Si el brief viene del hub (`source/brief.json` con `doc`)

Mismo espíritu, otro formato: el `BriefDoc` del hub (`doc` de
`source/brief.json`, contrato en `reference/brief-doc.md`) ya decidió QUÉ se
dice, en qué formato y con qué copy. Lo volcás así — cada tipo de pieza tiene
su tabla completa en el reference:

| Pieza del BriefDoc | En `plan.json` |
|---|---|
| `estatico` (`ratio`, `copy`, `kind`, `adBase`, `changes`) | Un creativo en el grupo de su ratio: `4:5` → `g-feed` 1080×1350 · `1:1` → `g-square` 1080×1080 · `9:16` → `g-story` 1080×1920. El `copy` va **literal** en capas de texto; arquetipo, base y cambios en `notes` |
| `carrusel` (`slides[{text, role, accent}]`, `visual`, `continuity`, `caption`) | Un grupo 4:5 propio (`id` de la pieza) con un creativo por slide, `<pieza>-s<N>`; `text` en capas, rol y acento en `notes`, visual + continuidad en `notes` de todos; `caption` no se renderiza |
| `historia` (`frames[{text, role, link}]`, `visual`) | Un grupo 9:16 propio con un creativo por frame, `<pieza>-f<N>`; `text` en capas, rol y `link` (publicación, no render) en `notes` |
| `video` (`hook`, `body`, `cta`, `cast`, `angle`) | **UN** creativo `"kind": "video"` en `g-story` 1080×1920, `seconds: 20` por defecto (el doc no trae duración; si hook/body/cta lo sugieren, ajustá a ~32 palabras por clip de 10s y decí por qué). Hook, body, cta, cast y ángulo **textuales** en `notes`, más clips, producto, packshot y música |
| `messages[]` (por `messageId`), `rules[]`, `note`, `production` | `notes` de cada pieza, textuales |

**Lo que el BriefDoc no decide lo decidís vos y queda escrito en `notes`**:
componer o generar, `product_id` y vista (o lifestyle sin producto,
declarado), el título del video, y cualquier formato extra. `plan.json`
apunta al brief crudo: `"source": ["source/brief.json"]`. Si `doc` es `null`
(submission), no hay tabla: leés los archivos y es el camino de arriba.

## 4 · Scaffold

**Imagen**: carpeta + manifiesto `<id>.indash` con `meta.status: "draft"`,
canvas del formato del grupo, capas de intención (texto con el copy del plan,
logo, scrim, capa `ai-gen` con `active: null` si se genera). Si la sesión está
en modo flat: `meta.compose: "flat"` y UNA sola capa ai-gen full-bleed, sin
capas de texto ni logo — el copy queda en `notes` para el prompt. Formatos y safe
zones: skill `creative-execution`, `formats/` y `data/safe-zones.json`.

**Video**: carpeta + manifiesto **sin capas** — el contenido va a ser la
carpeta `composition/` que escribe `video-composition`, y los renders los pone
`render_video`. No crees `composition/` ni `renders/` acá, ni carpetas del
Workbench (son lazy: las crea la skill que las necesita).

```json
{
  "version": 2,
  "kind": "video",
  "meta": { "id": "promo-01", "brief": "<brief>", "group": "g-story",
            "status": "draft", "generating": false, "round": null,
            "updatedAt": "<ISO-8601>" },
  "canvas": { "width": 1080, "height": 1920, "background": "#000000" },
  "layers": [],
  "video": { "seconds": 20, "fps": 30, "active": null }
}
```

`canvas` = el formato del grupo (tamaño del render); `video.seconds` = el
`seconds` del plan; `active: null` hasta el primer render.

## 5 · Listo para disparar

Resumile al humano: N piezas en M grupos, qué productos se preparan, qué
piezas se componen vs generan, cuáles van flat, cuántos videos. Cuando dispare ("generá las
stories", "generá todo"), la producción la hacés vos desde este mismo chat:
`creative-execution` por cada imagen; para cada video, `video-clips` (guiones
→ parás → stills → clips, en el Workbench) y después `video-composition`
(composición + render). Si el lote es grande podés repartirlo en subagents que
sigan esas mismas skills — es una táctica de reparto, no el proceso.

**Si el brief vino del hub (existe `source/brief.json`), NO frenás acá.** El
humano ya aprobó ese brief en indash.ai y la app disparó esta skill sola:
lo que espera es ver material, no un resumen esperando un «dale». Después
del scaffold, mandá el resumen igual y seguí de corrido en este mismo chat:

1. `creative-execution` para el **v1 de todos los creativos de imagen**:
   1K, **un candidato por pieza**, sin regenerar salvo defecto flagrante (la
   lista de esa skill). No es la ronda final: es el primer material para que
   el humano corrija barato.
2. `video-clips` para **cada video, hasta los stills**: guiones y stills de
   corrido, sin la parada de guiones (la skill tiene esa excepción escrita),
   y **parás en los stills**, como siempre.

**Nunca clips ni render sin que el humano lo pida**: un clip cuesta plata que
no vuelve y el render es `video-composition`. Al terminar, contale qué quedó
(imágenes en v1, guiones y stills por video) y qué espera de él.

## Punto de entrada

Arrancá por el paso **0**: identificá tu brief. Después los dos gates (insight
y producto), y recién ahí el plan. Si `source/brief.json` existe, el primer
gate ya está cerrado (paso 1), el plan sale del `BriefDoc` (paso 3) y después
del scaffold seguís de corrido hasta los stills (paso 5).
