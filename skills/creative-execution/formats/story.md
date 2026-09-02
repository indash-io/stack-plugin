# Story / Reels — 1080×1920

## Safe zones (bloquean)

Números canónicos en `../data/safe-zones.json` — actualizados a la **zona
unificada de Meta (marzo 2026)**. Resumen:

- **Story**: nada de texto/logo en los **270px de arriba** (avatar, nombre,
  Sponsored), los **380px de abajo** (reply bar, CTA) ni los **65px de cada
  lado**.
- **Reels**: mismo top y lados, pero el bottom sube a **670px** (caption,
  audio, CTA) y la derecha a **120px** (rail de like/comment/share).
- **Regla de doble destino**: una pieza que va a Stories Y Reels se compone
  contra la zona de **Reels** (la estricta). Si es solo Story, ganás ~290px
  de alto útil abajo.

En capas: `marginTop`/`marginBottom`/`marginLeft`/`marginRight` ≥ la zona, y
verificalo mirando el `view_creative`.

## Estructura

Una story es UN mensaje que se lee en ≤3 segundos:

- **Un solo foco**: un claim O un beneficio O un precio — no los tres.
- Copy on-image corto: **máximo 6-8 palabras** en el título. El ojo escanea,
  no lee.
- Jerarquía vertical simple: título grande (`size` ≥ 72), sub opcional chico,
  CTA/precio como bloque aparte. Posicioná con `anchor` + `below`/`gap`.
- En secuencias (3-6 stories): hook → desarrollo → CTA. La última SIEMPRE es
  un CTA accionable (verbo + acción), no un cierre poético. El producto debe
  ser reconocible en todas.
- El sticker de engagement (si el brief lo trae) se agrega en Instagram al
  publicar, NO es parte del render — pero condiciona la composición: la story
  de CTA deja el pie libre para el sticker de link.

## Composición del texto (capas, no pixel)

El manual completo está en `../style/composicion-texto.md`. Lo mínimo:

- Texto sobre foto → **scrim degradé** detrás casi siempre (rect con
  gradient transparente→sólido). Contraste primero.
- Variá el placement entre stories de una secuencia (cabezal / pie /
  centrado / doble peso) — nunca clones la misma composición N veces.
- `maxWidth: "80%"` + `align: "center"` → wrapping por construcción.

## Imagen orgánica

- Pedí en el prompt espacio negativo donde va a caer el texto ("upper third
  clean and out of focus") — la escena se diseña para la capa de texto
  (Ley 5 de `../reference/prompt-craft.md`).
- Vertical nativo: encuadre 9:16 pensado como tal, no un cuadrado estirado.
- Con producto: el producto en el tercio dominante, no perdido en la escena.

## Checks específicos (además de los generales)

- ¿El título se lee de un vistazo a tamaño teléfono? (mirá el preview
  achicado: si dudás, es chico).
- ¿Texto/logo dentro de safe zone — la de REELS si la pieza tiene doble
  destino? (bloquea)
- ¿La story de CTA deja el pie libre para el sticker? (bloquea si el brief
  pide sticker de link)
- Secuencia: ¿el producto es reconocible y consistente entre stories? ¿el
  placement varía entre stories consecutivas?
