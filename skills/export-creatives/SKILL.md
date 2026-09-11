---
name: export-creatives
description: "Entregar los creativos de un proyecto de Indash Studio — exportar una ronda, un grupo o el brief completo en los formatos que pide el destino (PNG/JPG escala web, PSD editable; los videos salen como su render activo, tal cual), con estructura y nombres consistentes. Usala cuando el humano pida \"exportame\", \"pasame los finales\", \"prepará la entrega\". Hoy el destino es la carpeta Descargas; cuando exista el drive de indash, esta skill entrega ahí."
language: es
tags: execution
owner: lburgwardtr
status: draft
reviewed: 2026-09-02
---

# Export Creatives — la entrega

Exportar no es "sacar un PNG": es preparar UNA entrega coherente. El export
sale por `mcp__indash__view_creative` con `export: true` (una llamada por
creativo) y aterriza en la carpeta **Descargas** del humano. El destino va a
cambiar (drive de indash) — el proceso es el mismo, cambia dónde aterriza.

**Un video se entrega como está.** Para un creativo `kind: "video"` el export
es una **copia** de `renders/<active>.mp4` (lo hace la misma llamada con
`export: true`; el botón Export de la app hace exactamente lo mismo). Nunca
se re-renderiza para entregar: el render activo ES lo aprobado, y un render
nuevo sería otro `vN` que el humano no vio. Si el video no tiene `active`
(`null`), no hay nada que entregar — falta el render, y eso es
`video-composition`, no esta skill.

## 1 · Qué se entrega

- Alcance: lo que pida el humano — un creativo, un grupo, la ronda, el brief
  completo. Si dice "los finales", el criterio es `meta.status`: `approved`
  primero; si no hay aprobados, preguntá si van los `review`.
- **Avisá qué NO va y por qué**: piezas en `changes` o `draft` no se
  entregan en silencio — se listan ("quedan afuera f12 y f15, están en
  cambios").

## 2 · En qué formato (según destino, no por default)

- **Pauta / uso final**: PNG escala 2 (el default de la app).
- **Web / preview liviano**: `{ format: "jpg", scale: 1 }`.
- **El cliente quiere editar**: `{ format: "psd" }` — capas y texto editable
  en Photoshop (sale a escala 1).
- **Videos**: siempre el mp4 activo tal cual; `format`/`scale` no aplican. Si
  piden otro contenedor o un máster distinto (ProRes, alpha), es un pedido
  aparte que se resuelve con la composición, no con el export.
- Mezclado si el humano lo pide (ej: PNG para pauta + PSD de las 3 piezas
  hero).

## 3 · Nombres y estructura

Los archivos salen con el id del creativo. Para entregas grandes, decile al
humano la convención al reportar: `<brief>/<grupo>/<id>.<ext>` — el id del
manifiesto ES el nombre, no inventes otros (la trazabilidad
pieza↔archivo↔Board vale más que un nombre "lindo").

## 4 · Antes de entregar

- Verificá 2-3 piezas al azar MIRANDO (`view_creative` sin export): lo que
  exporta es lo que se ve — si una capa quedó rota, mejor encontrarla vos
  que el cliente. En un video la misma llamada te da la hoja de contactos del
  render activo: confirmá que es el corte que el humano aprobó.
- Reportá al final: N piezas exportadas, formato/escala, qué quedó afuera.

## Futuro (no lo intentes hoy)

Cuando exista el drive de indash, la entrega sube ahí (con estructura por
cliente/brief/ronda) y esta skill se actualiza sola con la app. Mientras
tanto: Descargas + que el humano suba a su drive.

## Punto de entrada

Definí el **alcance** (paso 1) con lo que pidió el humano y de ahí seguí en
orden. No exportes nada sin saber qué queda afuera y por qué.
