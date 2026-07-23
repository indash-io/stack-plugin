# 04 — Client Context (el CLAUDE.md del cliente)

Escribís el `CLAUDE.md` del cliente: **la fuente de verdad de marca** que `carruseles` y `stories-nano-banana` heredan al trabajar en esta carpeta. Usá `templates/client_claude_md.md` como base.

---

## Por qué importa este archivo

Según la política del stack, cuando la carpeta de trabajo tiene un `CLAUDE.md` de cliente, **ese contenido gana sobre cualquier default genérico** en decisiones de marca (paleta, tono, tipografía, estética). Es lo que hace que el mismo plugin produzca contenido on-brand para cada cliente sin tocar el plugin. Si este archivo está flojo o inventado, todo el contenido que salga después también lo estará.

---

## Cómo lo escribís

1. Partí de `templates/client_claude_md.md` y completá cada sección con el brief silencioso del Discovery.
2. **Lo que extrajiste con certeza** (paleta con hex, tono, links, productos) → va como dato.
3. **Lo que no conseguiste** → va como placeholder explícito y accionable, no como invento. Ejemplos:
   - `> ⚠️ PENDIENTE: completar paleta de marca (no había URL ni imágenes en el onboarding).`
   - `> ⚠️ PENDIENTE: linkear cliente en Indash para traer el catálogo.`
4. Mantené el registro rioplatense y conciso. Este archivo lo lee otro agente, no es marketing.

---

## Además del CLAUDE.md: brand.md y brand-kit.md

En este paso también escribís los dos `.md` de marca dentro de `brand/`. Son complementos, no reemplazan al `CLAUDE.md`:

- **`assets/brand-kit/brand.md`** — narrativa legible de la marca (qué es, posicionamiento, audiencia, tono, estética). Usá `templates/brand_md.md`.
- **`assets/brand-kit/brand-kit.md`** — resumen estructurado y operativo: paleta con hex, tipografía (familia + características), do's & don'ts. Es lo que las skills consultan rápido.

El `CLAUDE.md` es el operativo (manda sobre defaults); `brand.md` es el "quién es"; `brand-kit.md` es la ficha técnica. Los tres salen del mismo brief de Discovery — no te contradigas entre ellos. Lo que no sepas, placeholder explícito en los tres.

---

## Qué tiene que cubrir (mínimos)

- **Identidad**: nombre, vertical/categoría, una línea de qué vende.
- **Tono de marca**: cómo habla la marca; qué evitar.
- **Brand kit**: paleta (con hex), tipografía (familia + características), estética/mood.
- **Links operativos**: sitio, Drive, Notion, handle/ID en Indash.
- **Catálogo**: puntero al índice de productos de la carpeta.
- **Reglas del cliente**: claims que NO se pueden hacer, restricciones legales, do's & don'ts si los hay.
- **Cómo producir contenido para este cliente**: recordatorio de que se usan las skills del stack (`carruseles`, `stories-nano-banana`) con la URL + imagen de cada producto, y que la paleta/tipografía de este archivo manda.

---

## Reglas de Client Context

1. **Nunca inventes** marca, claims ni links. Lo que falta es placeholder explícito.
2. **Un cliente = un `CLAUDE.md`.** No mezcles contexto de otros clientes.
3. **Coherencia con la política del stack**: este archivo gana sobre defaults, pero no contradice las reglas de las skills (aspect ratios, gate de auth, etc.).
4. **Accionable**: cada placeholder dice qué falta y cómo conseguirlo.

Con el `CLAUDE.md` escrito → pasá a llenar el índice de productos (`templates/product_index.md`) y después al self-check.
