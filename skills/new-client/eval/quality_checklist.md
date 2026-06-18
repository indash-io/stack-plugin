# Self-check — New Client

Corré este checklist antes de entregar el handoff. Si algo falla, corregilo. No entregues con ítems en rojo sin avisarle al user.

## Estructura

- [ ] La carpeta del cliente usa **slug en kebab-case** derivado del nombre (sin acentos, sin espacios).
- [ ] La estructura coincide con `templates/folder_structure.md` (ni de más ni de menos).
- [ ] No pisé ninguna carpeta existente sin avisar.
- [ ] Las carpetas vacías quedaron versionables (`.gitkeep`).

## Marca (brand/)

- [ ] Intenté traer los assets de marca **desde el MCP de Indash** primero.
- [ ] Logos → `brand/logos/`, tipografías → `brand/typographies/`, brand kit crudo/PDF → `brand/assets/`. Cada cosa en su carpeta, nada mezclado.
- [ ] Si la marca no estaba en Indash, ofrecí al user pasar los archivos (PDF/logos/fuentes) y los guardé donde corresponde.
- [ ] Escribí `brand/brand.md` (narrativa) y `brand/brand-kit.md` (resumen estructurado), coherentes con el `CLAUDE.md`.
- [ ] **Nada inventado**: assets que no existen → carpeta vacía con `.gitkeep` + campo `⚠️ PENDIENTE`.

## CLAUDE.md del cliente

- [ ] Existe `{slug}/CLAUDE.md` y sigue `templates/client_claude_md.md`.
- [ ] Cubre los mínimos: identidad, tono, brand kit, links, catálogo, reglas, cómo producir contenido.
- [ ] **Nada inventado**: lo que no extraje con certeza quedó como `⚠️ PENDIENTE` accionable, no como dato falso.
- [ ] La paleta tiene hex donde se pudo extraer; si no, está marcada como pendiente.
- [ ] Menciona explícitamente que se usan las skills del stack y que esta paleta/tipografía manda sobre defaults.

## Productos / Indash

- [ ] Apliqué el **gate de Indash**: o traje productos con el MCP conectado, o dejé el índice como pendiente explicando que falta conectar.
- [ ] **No inventé productos** ni URLs ni imágenes.
- [ ] Cada producto traído tiene, cuando existe, **URL + imagen** (los inputs de las skills de contenido).
- [ ] `productos/index.md` sigue `templates/product_index.md`.

## Handoff

- [ ] Mostré el árbol **real** creado, no uno inventado.
- [ ] Listé los pendientes accionables (conectar Indash, links faltantes, paleta a confirmar).
- [ ] Expliqué cómo seguir: qué skill disparar (`carrusel-nano-banana` / `stories-nano-banana`) y qué inputs pide.
- [ ] Tono rioplatense, sin relleno.

Si todo está en verde (o los rojos están explicados como pendientes para el humano) → entregá.
