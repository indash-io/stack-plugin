---
name: new-brief
description: "Armado de un brief en un proyecto de Indash Studio (cwd con .indash/) — del insight crudo al Board listo para disparar producción: conseguir el material del humano (PDF, Word, texto), guardarlo como source, preparar los productos (fotos + product.json), proponer el plan con decisiones escritas por pieza, y scaffoldear los manifiestos. Usala cuando el humano la invoque en el chat de un brief o pida \"armá el brief / el plan del mes\". No genera imágenes: eso es creative-execution."
language: es
tags: execution
owner: lburgwardtr
status: draft
reviewed: 2026-09-02
---

# New Brief — del insight crudo al Board listo

El output de esta skill es un Board disparable: plan aprobado, productos
preparados, manifiestos scaffoldeados. **Acá no se genera ni una imagen** —
producir es `creative-execution`.

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

- ¿Ya está? Mirá `briefs/<brief>/source/` y lo que vino en el chat.
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
   paso que garantiza que ningún ejecutor genere "de memoria": vos mirás las
   30 fotos UNA vez, todos los demás leen tus conclusiones.
3. Fotos inutilizables (watermark, render que no coincide, pixelada) → al
   campo `avoid`, y avisale al humano si un producto quedó sin fotos buenas.

## 3 · El plan, con las decisiones ESCRITAS

Escribí `briefs/<brief>/plan.json` (schema en CLAUDE.md). Además de la
estructura (grupos por formato, ids kebab-case), cada creativo lleva en
`notes` las decisiones que después nadie tiene que adivinar:

- **¿Componer o generar?** Si la pieza es tipográfica/brand-flat/precio →
  se COMPONE (capas, sin generación). Si lleva escena orgánica → se genera.
- **¿Producto en escena o no?** Lifestyle sin producto es legítimo, pero se
  decide ACÁ y queda escrito — no lo decide un ejecutor solo.
- Con producto: cuál (`product_id`) y qué vista pide la pieza.

El plan se corrige barato ANTES de correr 45 piezas; después cuesta 45
regeneraciones. Contale el plan al humano en 2-4 líneas y ajustá si te
corrige. plan.json es SOLO estructura — el estado vivo va en cada
manifiesto; único escritor del plan: el chat principal.

### Si el brief viene del armador de briefs

Cuando el material de `source/` ya llega como **bloques por pieza** (el
formato de `reference/bloque-por-pieza.md` — el contrato entre ideación y
ejecución), el trabajo de este paso es **mecánico, no creativo**: cada bloque
ya trae la decisión componer/generar, el producto con su vista, el copy
on-image y las restricciones. Volcalo a `plan.json` + `notes` siguiendo la
tabla de mapeo del reference, **sin re-decidir nada** — y preguntá únicamente
lo que el bloque no trae. Un bloque completo = cero preguntas.

## 4 · Scaffold

Por cada creativo: carpeta + manifiesto `<id>.indash` con `meta.status:
"draft"`, canvas del formato del grupo, capas de intención (texto con el
copy del plan, logo, scrim, capa `ai-gen` con `active: null` si se genera).
Formatos y safe zones: skill `creative-execution`, `formats/` y
`data/safe-zones.json`.

## 5 · Listo para disparar

Resumile al humano: N piezas en M grupos, qué productos se preparan, qué
piezas se componen vs generan. Cuando dispare ("generá las stories", "generá
todo"), la producción sigue con `creative-execution` — directo o despachando
subagents según el tamaño del lote (el template de despacho está en
`.indash/executor-prompt.md`).

## Punto de entrada

Arrancá por el paso **0**: identificá tu brief. Después los dos gates (insight
y producto), y recién ahí el plan.
