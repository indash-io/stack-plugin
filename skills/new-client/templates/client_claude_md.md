# Template — CLAUDE.md del cliente

Copiá esta plantilla a `{slug}/CLAUDE.md` y completala con lo que devolvieron `get_brand_context`, `get_brand_kit` y `list_products` (`instructions/05_carpeta_local.md`, tabla de fuentes). Lo que Indash no tiene queda como `> PENDIENTE: …` diciendo dónde se carga. **No se escribe nada desde el sitio, una captura o tu lectura de la marca.**

El bloque de abajo (entre las líneas de corte) es lo que va dentro del archivo del cliente.

---8<--- copiar desde acá ---8<---

```markdown
# CLAUDE.md — {Nombre del cliente}

> Contexto de **{Nombre del cliente}** para el stack de Indash, escrito desde su onboarding en Indash el {fecha}. Se carga cuando trabajás en esta carpeta y **gana sobre cualquier default genérico** de las skills en decisiones de marca. La fuente de verdad sigue siendo Indash: si esto y el onboarding se contradicen, manda el onboarding, y este archivo se vuelve a escribir desde ahí. No cargues nada de acá al onboarding.

## Identidad

- **Cliente:** {Nombre del cliente}
- **Workspace en Indash:** {slug} — onboarding: {onboarding.url}
- **Qué vende:** {tienda + los productos del catálogo, en una línea — o PENDIENTE: sin tienda ni productos en Indash}
- **Objetivo (en palabras del cliente):** {`goals.objective` literal — o PENDIENTE: sin responder en el onboarding}

## Mecanismo

Por qué funciona el producto, en palabras del cliente. Cada pieza explica a partir de esto; sin mecanismo, solo afirma.

- **{Producto o "todos"}:** {mecanismo literal — o PENDIENTE: cargar el mecanismo en el onboarding}

## Voz

- **Perfil de voz (derivado del corpus, confirmado por el cliente):** {persona, largo de frase, emojis, cómo nombran el producto, claims y CTAs que repiten, estructura del caption — o PENDIENTE: análisis de voz sin confirmar en Indash}
- **Material escrito propio:** {qué hay en `written` y `voice.written_text`, o "ninguno"}
- **Qué evitar:** {`rules.forbidden_claims` literal — o "ninguno cargado"}. Piezas "esto no somos" en Indash: {N} (las abre `content-brief`).

## Brand kit

- **Paleta** (manda sobre defaults): {color — `#hex`, uno por línea, de `get_brand_kit` o del sistema visual confirmado — o PENDIENTE: brand kit vacío en Indash}
- **Tipografía:** {familia y rol — o PENDIENTE}
- **Logos:** `assets/logos/` — {qué hay, o PENDIENTE}
- **Brand book / guidelines:** `assets/brand-kit/` — {archivo, o "no hay"}
- **Qué puede tocar la IA** (restricciones duras del generador): {los seis flags de `asset_freedom` con su valor — o PENDIENTE: sin responder en el onboarding}
- **Ficha técnica:** `assets/brand-kit/brand-kit.md`. Narrativa: `assets/brand-kit/brand.md`.

## Links

- **Tienda / sitio:** {`state.store.site`}
- **Instagram:** @{handle}
- **Drive:** {`assets.drive_url`}
- {otros links de `state.lists.links`}

## Catálogo

`assets/products/index.md`, traído de Indash. Cada producto con nombre exacto, URL e imagen: los dos inputs que piden las skills de ejecución.

## Cómo producir para este cliente

- Trabajá **dentro de esta carpeta** para heredar este contexto.
- El brief del período sale de `content-brief`, que lee el onboarding en Indash (no este archivo).
- Piezas: `carruseles` (4:5), `stories-nano-banana` (9:16), `ads`, `ugc-generator` / `ugc-video-prompts`, `all-videos`, `email-marketing-ecomm`. Entregables en `exports/<tipo>/`.
- La paleta, la tipografía y "qué puede tocar la IA" de este archivo mandan sobre cualquier default de las skills.
```

---8<--- hasta acá ---8<---
