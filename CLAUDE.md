# CLAUDE.md — Guía técnica del plugin Indash Stack

**Alcance de este archivo.** Esto es la guía para **desarrollar el plugin** (no para usarlo). Solo se carga como contexto cuando abrís *este repo* como directorio de trabajo. **No viaja con la instalación**: cuando alguien instala el plugin y lo usa en la carpeta de su cliente, este `CLAUDE.md` no se carga (lo dice la doc oficial de plugins). La política que recibe el *usuario* del stack vive en `hooks/context/stack-policy.md`, inyectada por el hook de SessionStart.

> Si estás buscando **cómo usar** el stack (instalar, generar carruseles/stories), eso está en `README.md`.

### El stack cruza dos repos

Este repo es **el cliente**: el plugin que se instala en Claude Code (skills, política del hook, `.mcp.json`). **El servidor está en `indash-io/mkt-agents`**: el MCP de Indash, su auth OAuth, el gate económico, la generación real y el billing. Si la respuesta que buscás no está acá, está allá:

| Buscás… | Está en `indash-io/mkt-agents` |
|---|---|
| Estado y plan del stack completo (audit, fases F0→F4) | `docs/agents/mcp-stack-professionalization.md` — **la fuente de verdad** |
| Mapa visual de todo el stack en una pantalla | `docs/agents/stack-map.excalidraw` |
| Qué hace cada tool del MCP, transportes, resolución de workspace | `packages/indash-mcp/README.md` |
| Cómo se cobran las generaciones (créditos, refunds) | `docs/agents/billing.md` |
| Cómo se autentica el conector `indash` (OAuth 2.1, DCR, PKCE) | `apps/web/app/api/oauth/*` y `app/.well-known/oauth-*` |

**Tres cosas se rompen en silencio si tocás un solo lado:**

1. **`core/skills/` es la fuente única de skills.** Las copias en
   `apps/web/lib/data/default-skills/` de mkt-agents son **generadas** — allá se
   regeneran con `bun run scripts/sync-default-skills.ts <path-a-este-repo>`.
   Si cambiás el canon acá, hay que correrlo y abrir PR allá.
2. **Las tools que invocan las skills** viven allá. Si allá renombran o sacan
   una tool, las skills de acá que la llaman quedan rotas.
3. **El `.mcp.json` de acá decide cómo se autentica el usuario contra el server
   de allá.** Un `headers.Authorization` acá desactiva el flujo OAuth de allá.

---

## Modelo mental: cómo funciona un plugin de Claude Code

Un plugin es un repo con un manifiesto `.claude-plugin/plugin.json`. Claude Code **autodescubre** los componentes en ubicaciones default — no hace falta declararlos en el manifiesto:

| Componente | Ubicación default | Qué aporta |
|---|---|---|
| Skills | `skills/<nombre>/SKILL.md` | Capacidades que el agente dispara solo o el usuario invoca |
| Commands | `commands/*.md` | Slash commands |
| Agents | `agents/*.md` | Subagentes con system prompt propio |
| Hooks | `hooks/hooks.json` | Automatización en eventos del ciclo de vida |
| MCP servers | `.mcp.json` | Conectores externos como herramientas |

**Lo clave a entender (y la fuente de confusión típica):**

- Un plugin **inyecta contexto vía skills, agents y hooks** — NO vía un `CLAUDE.md`. La doc oficial: *"A `CLAUDE.md` file at the plugin root is not loaded as project context."*
- Por eso la política operativa del stack está en `hooks/context/stack-policy.md` + un hook de SessionStart que la `cat`-ea. Ese es el patrón estándar para inyectar una política en cada sesión del usuario.
- Distribución: **vía marketplace**, no como bundle descargable. Un repo con `.claude-plugin/marketplace.json` lista plugins; el usuario hace `/plugin marketplace add` + `/plugin install`. Claude Code lo copia a `~/.claude/plugins/cache/`.
- Para iterar en desarrollo: `claude --plugin-dir <ruta-a-este-repo>` carga el plugin desde disco (y ahí sí se carga este `CLAUDE.md`, porque el repo es tu CWD).

---

## Mapa del repo (qué es cada cosa y quién lo lee)

| Archivo / carpeta | Rol | Lo lee… |
|---|---|---|
| `.claude-plugin/plugin.json` | Manifiesto: nombre, versión, metadata | Claude Code al instalar |
| `.claude-plugin/marketplace.json` | Marketplace privado: lista el plugin para `/plugin install` | Claude Code al hacer `marketplace add` |
| `.mcp.json` | Definición del MCP server `indash` (el único que trae el plugin) | Claude Code (autodescubierto) |
| `plugin.json` (raíz) | **Mismo manifiesto en formato [Agent Plugins 1.0.0](https://agent-plugins.org)** | Clientes conformes a la spec (Cursor, Copilot, Codex, Gemini CLI…) |
| `mcp.json` (raíz) | Mismo server `indash`, con `type: "streamable-http"` (el nombre que usa la spec) | Ídem |
| `hooks/hooks.json` | Registra el hook de SessionStart | Claude Code (autodescubierto) |
| `hooks/context/stack-policy.md` | **Política operativa del stack** | El **agente del usuario**, cada sesión |
| `skills/<skill>/SKILL.md` | Orquestador de cada skill | El agente, al disparar la skill |
| `skills/<skill>/{instructions,style,templates,examples,eval}/` | Detalle de cada skill | El SKILL.md las referencia |
| `scripts/validate-plugin.mjs` | Validador de integridad | Vos / CI |
| `.github/workflows/validate.yml` | CI que corre el validador | GitHub Actions |
| `CLAUDE.md` (este) | Guía técnica de desarrollo | Vos, editando el repo |
| `README.md` | Cómo usar e instalar | Humanos que miran el repo |

---

## Anatomía de una skill

Cada skill es una carpeta en `skills/` con esta estructura. El `SKILL.md` es el **orquestador** (workflow + reglas no-negociables + tabla de referencias); los `.md` de las subcarpetas son el **detalle**. Mantené esa separación — no metas todo el detalle en el SKILL.md.

```
skills/<skill>/
  SKILL.md              Frontmatter (name, description, language) + workflow en pasos + reglas
  instructions/         Un .md por paso del workflow (01_intake … 06_output_format)
  style/                Tono, reglas de escritura, modos visuales, composición de texto
  templates/            Plantillas de shot list, prompt, arquetipos
  examples/good/        Ejemplos a imitar
  examples/bad/         Anti-patrones (qué NO hacer)
  eval/quality_checklist.md   Self-check obligatorio antes de entregar
```

El `SKILL.md` referencia esos archivos por ruta relativa (ej: `` `instructions/01_intake.md` ``). **Si renombrás o movés uno, la referencia queda rota y la skill se degrada en silencio** → por eso existe el validador.

El plugin tiene tres familias de skills:

- **Onboarding / planificación**: `new-client` (crea la estructura del cliente, baja marca + productos del MCP de Indash, escribe el `CLAUDE.md` de marca) y `content-brief` (arma el brief del período y orquesta a las de ejecución). No tienen `style/` de prompts; sus templates son de scaffolding/brief.
- **Contenido visual de Instagram**: `carruseles` (genera las imágenes vía MCP, elige modelo por slide) y `stories-nano-banana`. Comparten el esqueleto intake → discovery → decisions → concept → prompts → output. Al tocar una, fijate si aplica a la otra.
- **Otras piezas de performance**: `ads` (Meta), `ugc-video-prompts` y `seedance-multishot` (video), `email-marketing-ecomm`. Varias se importaron de skills externas y se alinearon a la convención del stack (gate, persistencia en `exports/<tipo>/`, herencia de marca del cliente).

**Convención transversal que comparten todas**: aplican el gate del MCP `indash`, heredan la marca del `CLAUDE.md` + `brand/` del cliente, y **guardan el entregable en disco** en `exports/<tipo>/` (o `briefs/`) con nombre `<AAAA-MM-DD>_<slug>_v<N>.md`. Esa convención vive en `hooks/context/stack-policy.md` (fuente única) y se inyecta en cada sesión — no la dupliques por skill.

---

## Convenciones de desarrollo

### Skills
- Idioma: **español rioplatense (voseo)**. Mantené el registro al editar.
- El `SKILL.md` arranca con frontmatter (`name`, `description`, `language: es`) y termina con un "Punto de entrada" que manda al paso 1.
- Reglas no-negociables explícitas y numeradas. Si agregás una regla, numerala en la misma lista.
- Toda ruta referenciada en el SKILL.md debe existir (lo verifica el validador).

### MCPs (`.mcp.json`)
- **El plugin trae UN solo conector (`indash`), es OAuth y no lleva `headers` en el `.mcp.json`.** Es un producto client-facing: conectores extra (Notion, Drive, scrapers) los agrega cada usuario por su cuenta, no el plugin. No hay secretos ni variables de entorno en el repo, y tampoco hay que agregarlas: un `headers.Authorization` explícito **desactiva** el flujo OAuth (el cliente nunca recibe el 401 que dispara el discovery, y si el token es inválido el server queda `failed` en vez de caer a OAuth). Si alguna vez hace falta autenticar por API key para un entorno headless, se registra el server aparte con `claude mcp add --header`, nunca acá.
- Si agregás/sacás un conector, actualizá la lista en **tres lugares a la vez** (ver regla de sincronización abajo).

### Política del stack (`hooks/context/stack-policy.md`)
- Es la única política que recibe el usuario. Si cambiás el gate de autenticación o la lista de MCPs, se edita acá.

### Manifiesto — se publica en DOS formatos a la vez
- Subí la `version` (semver) al hacer cambios con impacto.
- El repo tiene **dos manifiestos que describen el mismo plugin**:
  - `.claude-plugin/plugin.json` + `.mcp.json` → el formato propio de **Claude Code**.
  - `plugin.json` + `mcp.json` en la raíz → la spec **[Agent Plugins 1.0.0](https://agent-plugins.org)** (open, vendor-neutral; TSC con Amazon, Cursor, Microsoft, OpenAI y Vercel).

  Conviven sin pisarse: cada cliente lee el suyo y **ignora el del otro**. Es lo que hace que las 8 skills + el conector `indash` se puedan instalar fuera de Claude Code.
- El `plugin.json` de la raíz usa un **schema cerrado**: los únicos campos top-level permitidos son `$schema`, `name`, `version`, `description`, `author`, `homepage`, `repository`, `license`, `keywords` y `extensions`. Cualquier otra cosa se pone bajo `extensions["ai.indash.stack"]`. El validador lo hace cumplir.
- **Lo que NO viaja a clientes conformes:** el hook de `SessionStart` es específico de Claude Code — la spec no define hooks. En Cursor/Copilot/Codex la política **no se auto-inyecta**; el equivalente portable es la skill `stack-overview`, que la lleva adentro. Si cambiás la política, cambian **los dos**.
- `core/skills/` no es un segundo directorio descubrible: la spec solo mira `skills/*/SKILL.md`. Sigue siendo canon consumido por referencia desde las skills de ejecución.

### Regla de sincronización (importante)
El gate de autenticación y la lista de MCPs aparecen en **cinco** archivos. Si tocás cualquiera de los dos, actualizalos juntos para que no se desincronicen:
1. `hooks/context/stack-policy.md` (lo que recibe el usuario en Claude Code)
2. `skills/stack-overview/SKILL.md` (lo que reciben los clientes sin hooks)
3. `README.md` (la tabla de MCPs)
4. `.mcp.json` **y** `mcp.json` (los dos formatos — el validador falla si divergen)
5. Este `CLAUDE.md` si cambia algo conceptual del flujo

Ídem la versión: `plugin.json`, `.claude-plugin/plugin.json` y el `metadata.version` de `marketplace.json` tienen que ser el mismo número. El validador lo chequea.

---

## Validación

Antes de commitear, corré el validador (sin dependencias):

```
node scripts/validate-plugin.mjs
```

Chequea: JSON de config parsean y tienen campos mínimos, frontmatter de cada `SKILL.md`, **que toda referencia de archivo dentro de los SKILL.md exista**, que el hook de SessionStart apunte a un archivo real, y que el `marketplace.json` liste plugins con un `source` que tenga su `plugin.json`.

Además, **conformidad con Agent Plugins 1.0.0**: `$schema` exacto en `plugin.json` y `mcp.json`, `name` contra el patrón de la spec, schema cerrado (ningún campo top-level de más), namespaces de `extensions` en reverse-domain, transportes MCP válidos (`stdio` | `streamable-http` | `sse`) con URL https — y **anti-drift** entre los dos formatos: mismo `name`/`version`/`description` en los dos manifiestos, misma versión en `marketplace.json`, y mismos servers con mismas URLs en `.mcp.json` y `mcp.json`. Sale con código ≠0 si algo falla. El mismo chequeo corre en CI (`.github/workflows/validate.yml`) en cada push y PR.

---

## Cómo extender

**Agregar una skill nueva:**
1. Creá `skills/<nombre>/SKILL.md` con frontmatter + workflow + reglas.
2. Armá las subcarpetas (`instructions/`, `style/`, `templates/`, `examples/`, `eval/`) y referencialas desde el SKILL.md.
3. Corré el validador para confirmar que no hay refs rotas.
4. Mantené el registro rioplatense y la estructura orquestador/detalle.

**Agregar un MCP:**
1. Definilo en `.mcp.json` (token por env var si aplica).
2. Sumalo a la tabla en `stack-policy.md` y en `README.md` (regla de sincronización).
3. Si es requerido para una skill, sumalo al gate.

**Cambiar la política operativa:**
- Editá `hooks/context/stack-policy.md`. No dupliques esa política acá — este archivo es para desarrollo, no para runtime del usuario.

**Distribuir / publicar:**
- Para que el equipo lo instale, este plugin tiene que estar listado en un marketplace (un repo con `.claude-plugin/marketplace.json`). Puede ser este mismo repo o un repo de marketplace de Indash.

---

## Contexto por cliente (cuando se usa, no cuando se edita)

Esto aplica al **uso** del stack, no al desarrollo, pero conviene tenerlo presente: si la carpeta de trabajo de un cliente tiene su propio `CLAUDE.md`, ese es el contexto canónico del cliente (marca, tono, paleta) y **gana** sobre defaults genéricos. La política completa está en `hooks/context/stack-policy.md`.

## Releases

- **Un solo número de versión**: `plugin.json` y `marketplace.json` (metadata)
  deben decir lo mismo. Al release: bump en ambos + entrada en `CHANGELOG.md`
  + tag `v<version>` en el merge a main.
- La convención de carpetas de cliente vive en `docs/project-structure.md`
  (fuente canónica) y se inyecta vía `hooks/context/stack-policy.md` — si
  cambia una, cambia la otra.
