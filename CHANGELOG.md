# Changelog

## 0.6.0 — 2026-07-28

**`indash` pasa a OAuth. Se acabó el `INDASH_TOKEN`.** El conector era el
único del stack que se autenticaba con un header `Authorization: Bearer
${INDASH_TOKEN}`, y eso obligaba a cada usuario a generar una API key en la
app y setear una variable de entorno antes de poder hacer nada. Ahora el
`.mcp.json` no lleva `headers`: Claude Code recibe el 401 del server, hace el
discovery por `/.well-known`, se registra solo y abre el browser. Instalar el
plugin y conectarse es `/plugin install` + `/mcp`.

- El token queda guardado y se refresca solo (access 1h, refresh 30d con
  rotación). Si caduca, `/mcp` ofrece *Re-authenticate*.
- **Migración: un login único por máquina.** Al actualizar a 0.6.0, el
  conector deja de mandar el header y todavía no hay token OAuth guardado,
  así que Claude Code marca `indash` como "necesita autenticación" y te avisa
  al arrancar: `/mcp` → `indash` → login. De ahí en adelante es automático.
  Después podés borrar `INDASH_TOKEN` de tu `~/.zshrc` o de tu
  `settings.json` — ya no se lee.
- **Nada se rompe solo:** las API keys siguen siendo válidas del lado del
  server. Quien se quede en 0.5.0 sigue funcionando igual, sin fecha de corte.
- La API key sigue existiendo como camino **secundario** para entornos
  headless donde no hay browser (CI efímero). Se registra el server aparte con
  `claude mcp add --header`, nunca en el `.mcp.json` del plugin: un header
  explícito desactiva el flujo OAuth para todo el mundo.

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
