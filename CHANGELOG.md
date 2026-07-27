# Changelog

## 0.5.0 — 2026-07-27

**F4: el plugin es la fuente única de skills.** Nuevo `core/skills/` con el
canon compartido del stack (prompt-craft con las 7 leyes + EDIT vs GENERATE +
refs por modelo, y los formatos ig-carousel / ig-story / ig-stories-secuencia
/ ig-post). Las `default-skills` del agente interno de la web (mkt-agents)
pasan a ser copias GENERADAS de acá (script de sync en ese repo). Las
aplicaciones en `skills/*/instructions/05_prompt_engineering.md` declaran que
core gana ante conflicto. Validador cubre también `core/skills/`. Regla de
release en `core/README.md`.

## 0.4.0 — 2026-07-23

**Convención de carpetas unificada (breaking para carpetas existentes).** La
carpeta de cliente ahora ES un proyecto del Indash Studio — una sola
estructura para skills, editor y agente:

- `brand/logos` → `assets/logos` · `brand/typographies` → `assets/fonts` ·
  `brand/{assets,brand.md,brand-kit.md}` → `assets/brand-kit/` ·
  `productos/` → `assets/products/` · `entregables/` → `exports/` ·
  nuevo `creatives/` (scene graphs del Studio). `versions/` y `.indash/`
  son del Studio (las skills no las tocan).
- Las carpetas viejas siguen funcionando pero conviene migrarlas (renames
  mecánicos, ver `docs/project-structure.md`).

**Gate de MCPs honesto**: solo `indash` es requerido; notion/google-drive/
apify/higgsfield pasan a opcionales según la tarea.

**Limpieza**:
- Fuera los artefactos de distribución standalone (INSTALL.md, install.sh,
  READMEs con instrucciones de symlink) que contradecían el modelo plugin.
- Fuera `brands/smud` (datos de un cliente real no viajan en el plugin).
- `seedance-multishot`: frontmatter estándar en español (era
  "Cinematografic Video" en inglés con typo), refs rotas a
  MCP_GAPS_PROPOSAL.md eliminadas.
- Nombre viejo `carrusel-nano-banana` → `carruseles` (9 menciones);
  skill fantasma `indash-b2b-mail` neutralizada; `skill.md` → `SKILL.md`
  (case-sensitivity).
- Un solo número de versión (plugin.json y marketplace.json decían 0.3.0 y
  0.1.0); description del marketplace al día (decía 3 skills, hay 8).

## 0.3.0 y anteriores

Prehistoria sin changelog (2 commits): estructura inicial + marketplace.
