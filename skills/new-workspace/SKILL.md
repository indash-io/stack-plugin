---
name: new-workspace
description: "Alta de una marca/cliente nuevo en Indash Studio — configurar el workspace desde cero: brand kit (paleta, tipografías, logos), productos con fotos reales, y referencias de estilo, dejando el proyecto listo para su primer brief. Usala cuando el humano diga \"cliente nuevo\", \"demos de alta a X\", \"configurá la marca\". En proyectos conectados a indash.ai puebla la fuente de verdad con las tools de escritura mcp__indash__*; en proyectos locales puebla library/."
language: es
tags: execution
owner: lburgwardtr
status: draft
reviewed: 2026-09-02
---

# New Workspace — alta de una marca nueva

El output es un proyecto donde `new-brief` puede arrancar sin pedir nada:
marca definida, productos con fotos utilizables, referencias cargadas.

## El orden importa (cada paso alimenta el siguiente)

### 1 · Identidad

**Pedí lo que falta en UNA sola pregunta consolidada** — no de a un dato por
vez. Lo único obligatorio para arrancar es el **nombre de la marca**; el resto
se pide junto y lo que no venga queda como pendiente explícito:

> Dale, doy de alta a **{marca}**. Para dejarla completa de una pasada, pasame
> lo que tengas a mano (lo que falte lo dejo como pendiente):
> - URL del sitio / tienda
> - Brand kit (PDF o guía), logos y tipografías
> - Fotos reales de los productos
> - 3-5 referencias de estilo (piezas que te gustan, propias o ajenas)
>
> Con el nombre solo ya puedo arrancar igual.

Tono al pedir: directo, breve, rioplatense. Sin AI-speak ni saludos largos.

Qué tiene que quedar resuelto (pedido al humano, o extraído de la web/PDF que
traiga):

- Nombre, URL, posicionamiento en 1 línea, tono de voz.
- **Paleta en hex** (primario, secundario, neutros) — "azul" no alcanza. Si la
  extraés del sitio o del PDF, anotá 3-5 colores con su hex; si no hay fuente,
  queda `⚠️ PENDIENTE` — **jamás inventes una paleta**.
- **Tipografías**: display y cuerpo. Si son de Google Fonts →
  `mcp__indash__pull_font` (te deja los archivos en `library/fonts/` y te da
  los ids `idf-...`). Si son propias → pedí los archivos. Sin certeza del
  nombre exacto, describí características (serif/sans, peso, contraste) en vez
  de afirmar una familia.
- **Logos**: variantes (principal, blanco, iso) → `library/logos/`.
  SVG siempre que exista (recoloreable con `recolor`, nítido a todo tamaño).
- **Tono y estética**: cómo escribe la marca (técnico, emocional, hablado…) y
  su mood en una palabra (editorial, minimal, heritage, playful…). Salen del
  material real, nunca de prejuicios sobre el rubro.

Docs fuente (PDF del brand kit, guías) → `library/brand/`. El resumen
operativo → `library/brand/brand.md` (si el proyecto está conectado, ese
archivo es generado — los datos van a indash.ai, ver paso 4).

**Regla de placeholders**: todo dato de marca que no consigas con certeza va
como `⚠️ PENDIENTE` para que un humano lo complete. Un alta con pendientes
honestos vale más que una completa con datos inventados.

### 2 · Productos

Por cada producto:

- Nombre + claims REALES (de la web/material del humano — no inventes).
- **Fotos reales, no renders**: packshots limpios + fotos en uso. Mínimo
  utilizable: 1 packshot bueno + 1 vista alternativa. Marcá lo inutilizable.
- Análisis visual: mirá las fotos y escribí
  `library/products/<producto>/product.json` (schema en
  `creative-execution`) — el alta incluye MIRAR, no solo archivar.
- Catálogo → `library/products/products.md` (local) o indash.ai (conectado).

### 3 · Referencias de estilo

`library/references/`: piezas que al humano le gustan (propias o ajenas),
anti-referencias si las hay. 3-5 buenas referencias valen más que 30 sueltas.

### 4 · Dónde queda la verdad

- **Proyecto conectado a indash.ai**: la fuente de verdad es el workspace
  remoto — productos, fotos, brand kit y referencias se cargan ahí con las
  tools de escritura: `mcp__indash__create_product` / `update_product`,
  `add_product_images` (con `label` por foto), `update_brand_kit` (paleta y
  tipografías COMPLETAS — reemplazan, no agregan), `add_brand_logo` (una por
  variante, con `label`) y `add_style_reference` (archivo local o `url`).
  Después de poblar: `mcp__indash__refresh_workspace` re-hidrata la library
  local (brand.md / products.md generados). La library local es cache: se
  baja on-demand.
- **Proyecto local**: `library/` ES la verdad — brand.md y products.md son tu
  memoria viva; mantenelos frescos.

### 5 · Checklist de salida (no des el alta por completa sin esto)

- [ ] Paleta con hex + tipografías resueltas (archivos o pulled) + logos en
      variantes (idealmente SVG).
- [ ] Cada producto con fotos utilizables y su `product.json` escrito.
- [ ] brand.md / products.md (o el workspace remoto) completos, con los
      pendientes marcados explícitos.
- [ ] Un creativo de PRUEBA compuesto y verificado con
      `mcp__indash__view_creative` (fondo de marca + título con la tipografía
      display + logo): valida fuentes, colores y assets de una pasada.

Cerrá reportando qué quedó cargado y qué faltó (fotos flojas, tipografía sin
licencia, paleta pendiente, etc.).

## Punto de entrada

Arrancá por el paso **1 · Identidad**: nombre de la marca primero, y una sola
pregunta consolidada por todo lo demás.
