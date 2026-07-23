# Template — CLAUDE.md del cliente

Copiá esta plantilla a `{slug}/CLAUDE.md` y completala con el brief del Discovery. Lo que no sepas, dejalo como `> ⚠️ PENDIENTE: ...` accionable. **No inventes.**

El bloque de abajo (entre las líneas de corte) es lo que va dentro del archivo del cliente.

---8<--- copiar desde acá ---8<---

```markdown
# CLAUDE.md — {Nombre del cliente}

> Contexto canónico de **{Nombre del cliente}** para el stack de Indash. Este archivo se carga como contexto del proyecto cuando trabajás en esta carpeta y **gana sobre cualquier default genérico** en decisiones de marca (paleta, tono, tipografía, estética). Mantenelo al día.

## Identidad

- **Cliente:** {Nombre del cliente}
- **Vertical / categoría:** {categoría — o ⚠️ PENDIENTE}
- **Qué vende (una línea):** {descripción — o ⚠️ PENDIENTE}

## Tono de marca

- **Cómo habla la marca:** {técnico / emocional / minimalista / hablado / … — o ⚠️ PENDIENTE}
- **Qué evitar:** {anti-patrones de copy, claims prohibidos — o ⚠️ PENDIENTE}

## Brand kit

- **Paleta** (manda sobre defaults):
  - {Color 1} — `#hex`
  - {Color 2} — `#hex`
  - {Color 3} — `#hex`
  - > ⚠️ Si está vacío: completar desde logo/sitio/brand kit.
- **Tipografía:** {familia + características: serif/sans, peso, contraste — o ⚠️ PENDIENTE}
- **Estética / mood:** {editorial / lifestyle / minimal / heritage / … — o ⚠️ PENDIENTE}
- **Material de marca**: logos en `assets/logos/`, tipografías en `assets/fonts/`, brand kit crudo en `assets/brand-kit/`.
- **Más contexto**: narrativa en `assets/brand-kit/brand.md`, ficha técnica en `assets/brand-kit/brand-kit.md`.

## Links operativos

- **Sitio / tienda:** {URL — o ⚠️ PENDIENTE}
- **Indash (handle/ID):** {id — o ⚠️ PENDIENTE: linkear cliente en Indash}
- **Google Drive:** {link — o ⚠️ PENDIENTE}
- **Notion:** {link — o ⚠️ PENDIENTE}

## Catálogo

Los productos viven en `assets/products/index.md` (traídos del MCP de Indash). Cada uno tiene nombre + URL + imagen de referencia — los dos inputs que piden las skills de contenido.

## Reglas del cliente

- **Claims que NO se pueden hacer:** {restricciones legales/regulatorias — o "ninguna conocida"}
- **Do's & don'ts visuales:** {si los hay — o ⚠️ PENDIENTE}

## Cómo producir contenido para este cliente

- Trabajá **dentro de esta carpeta** para heredar este contexto.
- **Carrusel** (4:5) → skill `carruseles`, con la URL + imagen del producto.
- **Stories** (9:16) → skill `stories-nano-banana`, con la URL + imagen del producto.
- La **paleta y tipografía de este archivo mandan** sobre cualquier default de las skills.
- Entregables → `exports/carruseles/` y `exports/stories/`.
```

---8<--- hasta acá ---8<---
