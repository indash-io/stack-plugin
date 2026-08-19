# Indash Stack

Plugin de Claude Code / Cowork **para clientes de Indash**: el combo de skills de creative performance + el conector MCP de Indash para que crees el contenido de tu marca vos mismo — carruseles, stories, ads, video y email, con tus productos y tu identidad de marca reales.

La idea: instalás el plugin, conectás tu cuenta de Indash con un login, y las skills producen entregables de calidad senior usando tu catálogo y tu brand kit. Sin configurar nada más. La misma carpeta de trabajo que arma el plugin es un proyecto del **Indash Studio**, así que todo lo que generes se abre nativo en el editor.

> **¿Vas a editar el plugin en vez de usarlo?** Leé [`CLAUDE.md`](./CLAUDE.md): es la guía técnica para desarrollar sobre este repo. Este README es para **usar** el stack.

---

## Qué incluye

### Skills

| Skill | Qué hace |
|---|---|
| **new-client** | Da de alta un cliente nuevo: crea la estructura de carpetas estándar (con `brand/`), baja marca y productos desde el MCP de Indash y genera el `CLAUDE.md` de contexto de marca que las demás heredan. Se dispara con *"nuevo cliente"*. |
| **content-brief** | Arma el **brief de contenido del período**: define el mix de piezas (ads, carruseles, stories, videos, emails) con copy + brief de imagen por pieza, y orquesta las skills de ejecución. Se dispara con *"armá el brief del mes"* / *"plan de contenido"*. |
| **carruseles** | Carruseles **4:5 (1080×1350)**: shot list + **genera las imágenes** con el MCP de Indash (elige modelo por slide) + prompts. |
| **stories-nano-banana** | Secuencias de **Stories 9:16 (1080×1920)**: shot list + prompts, con sticker de engagement por story y texto en zona segura de UI. |
| **ads** | Meta ads (FB/IG) para DTC e-commerce: 3-5 variaciones con imagen final (vía MCP) + copy de Meta completo (Primary Text, Headline, Description, CTA). |
| **ugc-video-prompts** | Paquetes de video UGC (Kling 3.0 / Veo 3.1 / Seedance 2.0 + first/last frame con Nano Banana). |
| **ugc-generator** | **Producción end-to-end de videos UGC**: del pedido (una frase, un sheet, un brief) a los clips generados vía MCP y verificados en carpeta — guiones, frames, QA de producto y 2 gates de aprobación. Se dispara con *"hacele 2 videos de 10s a `<cliente>` con `<producto>`"*. |
| **all-videos** | Videos de marketing multi-shot (ads, demos, brand films, hypermotion) con selección de modelo por shot — Seedance 2.0, Omni, Veo, Kling — en modo prompt-only o video generado según el MCP. |
| **email-marketing-ecomm** | Mails promo DTC: 3 variantes (HTML + PNG) brand-first, listas para Klaviyo / Mailchimp / Customer.io. |
| **stack-overview** | **Empezá por acá si es tu primera vez.** Te explica el stack: qué hace cada skill, las 25 tools del conector, cómo se actualizan las skills, qué queda guardado en Indash y qué en disco, y qué referencias soporta cada modelo (imagen, video y audio). Se dispara con *"¿qué puedo hacer?"*, *"¿se puede pasar un video de referencia?"* o cualquier pregunta sobre capacidades. |

Todas siguen un workflow estricto: intake → discovery (scraping + análisis de imagen) → **una sola pregunta consolidada de decisiones** → concepto → generación de prompts → self-check → output. Nunca generan sin confirmar con vos primero.

### MCP server (`.mcp.json`)

El plugin trae **un solo conector, y es todo lo que el stack necesita**:

| Conector | URL | Auth | Para qué |
|---|---|---|---|
| `indash` | `https://www.indash.ai/api/mcp` | OAuth | Tu marca, tus productos, toda la generación de imagen/video y el drive de creatives |

¿Usás Notion, Google Drive u otros MCPs? Las skills los aprovechan como fuentes de contexto si ya los tenés conectados (un brief en Notion, assets en Drive), pero **ninguna los requiere** — se agregan por tu cuenta con `claude mcp add` o desde el panel de conectores de claude.ai, fuera del plugin.

### Hook de SessionStart

Inyecta `hooks/context/stack-policy.md` al inicio de cada sesión. Es **el mecanismo por el que la política del stack le llega al agente** cuando usás el plugin: aplica el **gate de autenticación** (si `indash` no está conectado, frena y te pide que lo conectes — no improvisa workarounds ni inventa datos de marca) y hereda el contexto de la marca desde el `CLAUDE.md` de la carpeta de trabajo.

### Portabilidad — no es solo Claude Code

Desde la 0.7.0 el plugin se publica **en dos formatos a la vez**, sin que uno pise al otro:

| Formato | Archivos | Lo lee |
|---|---|---|
| Claude Code | `.claude-plugin/plugin.json` + `.mcp.json` | Claude Code / Cowork |
| [Agent Plugins 1.0.0](https://agent-plugins.org) | `plugin.json` + `mcp.json` (raíz) | Cualquier cliente conforme a la spec abierta: Cursor, Copilot, Codex, Gemini CLI… |

Agent Plugins es un estándar abierto y vendor-neutral para empaquetar skills + MCP servers en un plugin portable. Las skills (`skills/<nombre>/SKILL.md`) y el conector son idénticos en los dos casos.

**Una diferencia importante:** el hook de SessionStart es específico de Claude Code — la spec no define hooks. En otros clientes la política del stack **no se inyecta sola**; ahí la lleva la skill `stack-overview`, que el agente carga cuando preguntás qué hace el stack. Si usás el plugin fuera de Claude Code, arrancá con *"¿qué puedo hacer con el stack de Indash?"*.

---

## Instalación

El plugin se distribuye **vía marketplace** (no es un archivo que se baja a mano). El repo es **privado**: el control de acceso es el acceso al repo en GitHub.

### Requisito previo (importante para repo privado)

Antes de instalar, cada persona necesita:

1. **Acceso de lectura al repo** `indash-io/stack-plugin` en GitHub (te lo da el admin como colaborador o vía team de la org).
2. **GitHub autenticado localmente** — porque el `marketplace add` clona el repo privado con tus credenciales git. Verificá una de las dos:
   ```
   gh auth status          # si usás GitHub CLI
   ssh -T git@github.com    # si usás SSH
   ```
   Si no tenés acceso o no estás autenticado, el `marketplace add` falla con un error de clone.

### Como usuario del equipo

1. **Agregá el marketplace** que publica este plugin:
   ```
   /plugin marketplace add indash-io/stack-plugin
   ```
2. **Instalá el plugin:**
   ```
   /plugin install indash-stack
   ```
3. **Conectá `indash`:** abrí `/mcp`, elegí `indash` y seguí el login en el browser. Es tu cuenta de Indash de siempre — no hay ningún token que copiar ni variable de entorno que setear.

Listo. Eso es toda la instalación.

### Para probarlo en local (desarrollo)

```
claude --plugin-dir /ruta/a/este/repo
```

### Autenticación

**OAuth con tu cuenta de Indash. No hay ninguna variable de entorno que configurar.** La primera vez, abrí `/mcp`, elegí `indash` y completá el login en el browser. El token queda guardado y se refresca solo; si alguna vez caduca, Claude Code te avisa y te ofrece *Re-authenticate* en el mismo panel.

En Cowork / claude.ai la conexión se hace desde el panel de conectores en vez de `/mcp`; el resto es igual.

#### Sesiones headless (crons, CI, `claude -p`)

Un run no interactivo no puede abrir el browser, así que no completa un OAuth por su cuenta. Dos opciones:

- **Autenticar una vez desde una sesión interactiva en esa misma máquina** (`/mcp`, o `claude mcp login indash`). El token queda guardado y los runs headless posteriores lo usan.
- **API key**, para entornos donde no hay sesión interactiva posible (un contenedor de CI efímero, por ejemplo). Se genera desde la app de Indash y se registra el server aparte, fuera del plugin:
  ```
  claude mcp add --transport http indash https://www.indash.ai/api/mcp \
    --header "Authorization: Bearer indash_sk_xxxxxxxx"
  ```
  Es un camino **secundario y opcional**: sirve para automatizaciones, no para el uso normal del stack. Ojo que si configurás el header y el token es inválido, Claude Code reporta el server como `failed` en vez de caer al flujo OAuth.

---

## Uso

Pedile a Claude en lenguaje natural — las skills se disparan solas cuando el pedido coincide:

1. **Dar de alta un cliente** (primero) → *"Nuevo cliente: Acme Foods"* → dispara `new-client`: crea la carpeta del cliente (con `brand/`), baja marca y productos del MCP de Indash y genera el `CLAUDE.md` de marca. Después trabajás **dentro de esa carpeta** para que el contexto se herede.
2. **Planificar el período** (opcional, recomendado) → *"Armá el brief de junio para Acme"* → dispara `content-brief`: define el mix de piezas con copy + brief de imagen, y te dice qué skill ejecuta cada bloque.
3. **Producir cada pieza** → el pedido dispara la skill que corresponde:
   - **Carrusel** → *"Armá un carrusel para `<URL>`"* + imagen → `carruseles` (genera las imágenes).
   - **Stories** → *"Necesito stories para `<URL>`"* + imagen → `stories-nano-banana`.
   - **Meta ads** → *"Hacé 3 ads para `<producto>`"* → `ads`.
   - **Video (prompts)** → *"Armá un UGC / video para `<producto>`"* → `ugc-video-prompts` o `all-videos`.
   - **Video (producción completa)** → *"Hacele 2 videos de 10s a `<cliente>` con `<producto>`"* → `ugc-generator` (genera y verifica los clips).
   - **Email** → *"Armá un mail promo para `<marca>`"* → `email-marketing-ecomm`.

Las skills de producto necesitan **URL de producto + imagen de referencia** (si onboardeaste con `new-client`, ya los tenés en `assets/products/index.md`). Si falta algo, la skill te lo pide y frena. Antes de generar te hace **una sola pregunta consolidada** con defaults; confirmás o editás, y recién ahí genera. Todo entregable se **guarda** en `exports/<tipo>/` (o `briefs/`) con nombre `<AAAA-MM-DD>_<slug>_v<N>`.

El output siempre es: **shot list / brief creativo** + **N prompts numerados** listos para pegar en nano banana junto a la imagen del producto. Además de mostrarlo en el chat, **se guarda en disco** dentro de la carpeta del cliente, en `exports/carruseles/` o `exports/stories/`, con el nombre canónico `<AAAA-MM-DD>_<producto-slug>_v<N>.md` (versiona solo, no pisa). Así queda todo ordenado y trazable sin pensar la nomenclatura cada vez.

---

## Patrón de carpetas por cliente

Creá **una carpeta por cliente** y dejá adentro un `CLAUDE.md` con su contexto: marca, tono, paleta, links a su Drive/Notion, datos clave. Al abrir Cowork en esa carpeta, ese `CLAUDE.md` se carga como contexto del proyecto y el stack lo hereda en todo lo que produce.

Las skills funcionan igual en cualquier carpeta — lo único que cambia es el contexto del cliente. Así el mismo plugin sirve para todos los clientes sin tocar el plugin.

```
clientes/
  cliente-acme/
    CLAUDE.md        ← contexto de Acme (marca, tono, paleta, links)
    exports/
  cliente-beta/
    CLAUDE.md        ← contexto de Beta
    ...
```

> **Ojo — no confundir dos `CLAUDE.md` distintos:**
> - El `CLAUDE.md` en la **carpeta de un cliente** = contexto de marca de ese cliente. **Sí** se carga cuando trabajás en esa carpeta.
> - El `CLAUDE.md` en la **raíz de este repo** = guía técnica para desarrollar el plugin. **No** se carga cuando usás el plugin — solo cuando editás el repo. Ver [`CLAUDE.md`](./CLAUDE.md).

---

## Estructura del repo

```
.claude-plugin/plugin.json      Manifiesto del plugin (formato Claude Code)
.claude-plugin/marketplace.json Marketplace privado (lista el plugin para /plugin install)
.mcp.json                       Definición de los MCP servers (formato Claude Code)
plugin.json                     Manifiesto en la spec abierta Agent Plugins 1.0.0
mcp.json                        MCP servers en la spec abierta (streamable-http)
hooks/hooks.json                Hook de SessionStart (solo Claude Code)
hooks/context/stack-policy.md   Política inyectada en cada sesión (lo que recibe el end user)
skills/stack-overview/          Qué puede hacer el stack (+ la política, para clientes sin hooks)
skills/new-client/              Onboarding de cliente (estructura + brand/ + CLAUDE.md + productos)
skills/content-brief/           Brief de contenido del período (orquesta las skills de ejecución)
skills/carruseles/              Carruseles 4:5 (genera imágenes vía MCP)
skills/stories-nano-banana/     Stories 9:16
skills/ads/                     Meta ads DTC (imagen + copy)
skills/ugc-video-prompts/       Paquetes de video UGC (Kling/Veo/Seedance)
skills/ugc-generator/           Producción end-to-end de videos UGC (pedido → clips verificados)
skills/all-videos/      Videos de marketing multi-shot, multi-modelo (Seedance/Omni/Veo/Kling)
skills/email-marketing-ecomm/   Mails promo DTC (HTML + PNG)
scripts/validate-plugin.mjs     Validador de integridad (JSON + refs de SKILL.md)
.github/workflows/validate.yml  CI que corre el validador en cada push/PR
CLAUDE.md                       Guía técnica para desarrollar el plugin (solo en-repo)
README.md                       Este archivo — cómo usar el stack
```

Para todo lo técnico (cómo está armado el plugin, cómo agregar una skill o un MCP, cómo distribuir), andá a [`CLAUDE.md`](./CLAUDE.md).
