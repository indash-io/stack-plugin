# Changelog

## 0.9.0 — 2026-08-19

**Skill nueva: `ugc-generator`** — el proceso de producción end-to-end de
videos UGC (antes "indash-production", usado internamente): del pedido en
cualquier formato a los clips generados vía MCP y verificados en carpeta, con
2 gates de aprobación (scripts y frames), QA de producto bloqueante, ficha de
marca por cliente y registro por video en `SCRIPTS.md`.

- Importada casi como venía; se renombró a `ugc-generator` y se adaptó a la
  convención del repo (frontmatter con `language: es`, biblioteca de guiones
  en `style/guiones.md`, "Punto de entrada" al final).
- **Las fichas de clientes reales NO viajan**: la skill traía `fichas/` con
  workspace IDs, dominios y datos comerciales de clientes — quedó solo el
  template (`templates/ficha-marca-template.md`) y la ficha vive en la carpeta
  local de cada cliente. Se anonimizaron también las marcas mencionadas en el
  cuerpo y en los ejemplos de guiones, con el mismo criterio del barrido de
  0.7.x (categoría genérica, aprendizajes técnicos intactos).
- Sincronizados los cinco lugares que listan skills: `stack-policy.md`,
  `stack-overview` (8 → 9 skills), `README.md`, `marketplace.json` y
  `CLAUDE.md`.

## 0.8.0 — 2026-08-06

**Las skills enseñaban un workflow que el MCP no sabía ejecutar.** Esta release
lo cierra, en los dos sentidos.

### Referencias multimodales, cableadas de verdad

`ugc-video-prompts` documenta desde hace meses que Seedance 2.0 toma "hasta 9
imágenes + 3 videos + 3 audios", y `instructions/analysis.md` enseña la sintaxis
completa (`@video1 as camera movement reference`, `@audio1 as background music
reference`), incluido el consejo de que subir un `@video` de UGC real handheld
es la vía más rápida de pelearle al default commercial.

El MCP solo mandaba imágenes. Ahora acepta `reference_video_urls` (hasta 3 con
seedance, 1 con omni) y `reference_audio_urls` (hasta 3, solo seedance) — ver
mkt-agents#232.

- **Bug corregido**: el call spec de `seedance-multishot` decía
  `reference_image_url` (singular). Ese param no existe: es
  `reference_image_urls`, un array. La llamada fallaba. Normalizado también en
  la prosa de examples y checklists, para que el nombre equivocado no siga
  circulando en el contexto del agente.
- `analysis.md` gana la tabla `@Image1/@Video1/@Audio1` → param del MCP, con la
  regla de que **el orden del array numera los `@`**.
- `seedance-multishot` 5.2 pasa a listar los tres params.

### `stack-overview` al día

- Tabla de modelos con columnas separadas de **Img / Video / Audio**.
- **veo: 4, 6 u 8 segundos** — no 4-12. Y 8 obligatorio con 2+ imágenes. (La
  skill `ugc-video-prompts` ya lo decía bien: "8s es hard cap". El código estaba
  mal, no la skill.)
- **Último frame** (`last_frame_image_url`) para veo y kling.
- Video de referencia deja de ser "solo omni": **seedance es el mejor** (3 clips
  + 3 audios).
- **Extensión de clip**: seedance la hace nativa por prompt (`Extend @Video1 by
  5s`) ahora que se pueden mandar videos. Sin verificar punta a punta — se
  ofrece como algo a probar, no como garantía.
- "No edita video" queda acotado a lo que de verdad no hace: post-producción.

## 0.7.0 — 2026-08-06

**El plugin sale de Claude Code.** Dos cambios: el paquete ahora conforma a la
spec abierta [Agent Plugins 1.0.0](https://agent-plugins.org), y hay una skill
nueva que explica el stack.

### Conformidad con Agent Plugins 1.0.0

`agent-plugins.org` es un estándar abierto y vendor-neutral para empaquetar
skills + MCP servers en un plugin portable (TSC con Amazon, Cursor, Microsoft,
OpenAI y Vercel). El plugin ahora se publica en **los dos formatos a la vez**:

- **Nuevo** `plugin.json` en la raíz — manifiesto conforme al schema cerrado de
  la spec. Lo específico de Indash vive bajo `extensions["ai.indash.stack"]`.
- **Nuevo** `mcp.json` en la raíz — el mismo conector `indash`, declarado como
  `streamable-http` (el nombre que usa la spec para lo que Claude Code llama
  `http`).
- `.claude-plugin/plugin.json` y `.mcp.json` **quedan intactos**: Claude Code
  sigue leyendo los suyos. Cada cliente ignora el formato del otro.

Efecto: las 8 skills y el conector `indash` se pueden instalar en cualquier
cliente conforme (Cursor, Copilot, Codex, Gemini CLI…), no solo en Claude Code.
`skills/*/SKILL.md` ya cumplía la spec tal cual estaba — no se movió ninguna
skill.

**Lo que no es portable:** el hook de `SessionStart` es propio de Claude Code
(la spec no define hooks), así que en clientes conformes la política del stack
**no se auto-inyecta**. De ahí la skill nueva.

### Nueva skill: `stack-overview`

Responde "¿qué puede hacer esto?" — las 8 skills con su disparador, las 25 tools
del conector agrupadas por familia, y las preguntas que venían apareciendo
siempre:

- **Las skills del plugin NO se actualizan solas** (hace falta
  `/plugin marketplace update indash`), a diferencia de las skills del workspace,
  que se leen en vivo de la cuenta de Indash.
- **Qué queda en disco vs. qué queda en Indash**, y qué hay que subir a mano.
- **Imágenes de referencia**: sí, en todo, con la tabla de topes por modelo
  (veo 3, kling 2 —start/end frame—, seedance 9, omni 3, grok-imagine 1).
- **Video de referencia: no existe hoy.** No hay ninguna tool que acepte video
  como entrada — el pipeline es imagen → video. La skill dice explícitamente que
  no se invente lo contrario, y ofrece los caminos reales (frames del video como
  referencia, describir el movimiento, `add_inspiration`).
- Qué NO hace el stack: no publica en Meta, no compra medios, no edita video.

Doble función: es también la política del stack para clientes que no ejecutan el
hook.

### Validador

Chequea la conformidad con la spec (`$schema` exacto, patrón de `name`, schema
cerrado, namespaces reverse-domain, transportes válidos) y sobre todo el
**drift entre los dos formatos**: `name`/`version`/`description` iguales en los
dos manifiestos, versión alineada con `marketplace.json`, y mismos servers con
mismas URLs en `.mcp.json` y `mcp.json`.

## 0.6.0 — 2026-07-28

**El plugin pasa a ser el producto client-facing.** Decisión de identidad:
esto ya no es "el stack de trabajo interno de Indash" — es lo que le ofrecemos
a los clientes para que creen el contenido de su marca ellos mismos: skills +
el conector MCP de Indash. Dos cambios grandes:

### Un solo conector: `indash`

Se van del `.mcp.json` los 4 conectores opcionales (notion, google-drive,
apify, higgsfield). Eran el workflow interno del equipo, y para un cliente
eran puro costo: instalabas el plugin y aparecían 5 servers en `/mcp`, 4
pidiendo OAuth a servicios de terceros que quizás ni usabas, más las tools
de todos ellos ocupando contexto. Ninguna skill los requería (eran
"opcionales según la tarea" desde la 0.4.0).

- El stack completo funciona con `indash` solo.
- Si el usuario tiene sus propios MCPs (Notion, Drive, etc.), las skills los
  aprovechan como fuentes de contexto — pero nunca los exigen.
- El equipo interno que los quiera los agrega por su cuenta, una vez por
  máquina: `claude mcp add --transport http notion https://mcp.notion.com/mcp`
  (ídem los demás), o desde el panel de conectores de claude.ai.
- La política del gate ahora gatea solo `indash` y trata cualquier otro
  conector como extra del usuario.

### `indash` pasa a OAuth. Se acabó el `INDASH_TOKEN`.

El conector se autenticaba con un header `Authorization: Bearer
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
- Fuera el `brands/<cliente>` semilla (datos de un cliente real no viajan en el plugin).
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
