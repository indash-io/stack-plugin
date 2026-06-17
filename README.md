# Indash Stack

Plugin de Claude Code / Cowork que empaqueta el stack de creative performance de Indash: las **skills de la empresa** (carruseles y stories nano banana) montadas sobre un set de **MCPs casi obligatorios** y un **gate de autenticación** que se carga al iniciar cada sesión.

La idea: cualquier persona del equipo instala este plugin y obtiene los mismos resultados que el flujo de trabajo de referencia — mismas skills, mismos conectores, mismas reglas — sin reconfigurar nada a mano.

> **¿Vas a editar el plugin en vez de usarlo?** Leé [`CLAUDE.md`](./CLAUDE.md): es la guía técnica para desarrollar sobre este repo. Este README es para **usar** el stack.

---

## Qué incluye

### Skills

| Skill | Qué hace |
|---|---|
| **carrusel-nano-banana** | Genera un shot list creativo + N prompts de nano banana (Gemini 2.5 Flash Image) para carruseles **4:5 (1080×1350)** de Instagram, a partir de una URL de producto + una imagen de referencia. |
| **stories-nano-banana** | Igual, pero para secuencias de Instagram **Stories 9:16 (1080×1920)**, con sugerencia de sticker de engagement por story y texto dentro de la zona segura de UI. |

Ambas siguen un workflow estricto: intake → discovery (scraping + análisis de imagen) → **una sola pregunta consolidada de decisiones** → concepto → generación de prompts → self-check → output. Nunca generan sin confirmar con vos primero.

### MCP servers (`.mcp.json`)

El stack depende de estos 5 conectores. Tratalos como requeridos.

| Conector | URL | Auth | Para qué |
|---|---|---|---|
| `indash` | `https://www.indash.ai/api/mcp` | Bearer `${INDASH_TOKEN}` | Datos y operaciones de Indash |
| `higgsfield` | `https://mcp.higgsfield.ai/mcp` | OAuth | Generación de imagen/video (nano banana, Sora, Veo, Kling, Flux) |
| `google-drive` | `https://drivemcp.googleapis.com/mcp/v1` | OAuth | Lectura/escritura de archivos y entregables |
| `notion` | `https://mcp.notion.com/mcp` | OAuth | Briefs y bases de conocimiento de clientes |
| `apify` | `https://mcp.apify.com` | OAuth | Scraping robusto de URLs de producto y datos web |

### Hook de SessionStart

Inyecta `hooks/context/stack-policy.md` al inicio de cada sesión. Es **el mecanismo por el que la política del stack le llega al agente** cuando usás el plugin: le recuerda los MCPs requeridos, aplica el **gate de autenticación** (si falta un conector que la tarea necesita, frena y te pide que lo conectes — no improvisa workarounds) y hereda el contexto del cliente desde el `CLAUDE.md` de la carpeta de trabajo.

---

## Instalación

El plugin se distribuye **vía marketplace** (no es un archivo que se baja a mano).

### Como usuario del equipo

1. **Agregá el marketplace** que publica este plugin:
   ```
   /plugin marketplace add indash-io/stack-plugin
   ```
2. **Instalá el plugin:**
   ```
   /plugin install indash-stack
   ```
3. **Configurá `INDASH_TOKEN`** como variable de entorno (ver abajo).
4. **Conectá los MCPs OAuth** la primera vez que los uses — el agente te frena y te pide que los conectes desde el panel de conectores de Cowork.

### Para probarlo en local (desarrollo)

```
claude --plugin-dir /ruta/a/este/repo
```

### Variables de entorno

| Variable | Requerida | Qué es |
|---|---|---|
| `INDASH_TOKEN` | Sí | Secret key de acceso al MCP de Indash (formato `indash_sk_...`). **No se incluye en el plugin** — cada usuario o la organización la configura como variable de entorno. |

### Autenticación de los conectores

- **`higgsfield`, `google-drive`, `notion`, `apify`** → OAuth. Se autentican la primera vez que se usan: el agente te frena y pide que los conectes desde el panel de conectores de Cowork. No hay nada que configurar a mano.
- **`indash`** → usa `INDASH_TOKEN` (no es OAuth). Es la única variable de entorno que tenés que configurar.

---

## Uso

Pedile a Claude en lenguaje natural — las skills se disparan solas cuando el pedido coincide:

- **Carrusel** → *"Armá un carrusel para este producto: `<URL>`"* + adjuntás una imagen de referencia → dispara `carrusel-nano-banana`.
- **Stories** → *"Necesito una secuencia de stories para `<URL>`"* + imagen → dispara `stories-nano-banana`.

En ambos casos necesitás **URL de producto + imagen de referencia**. Si falta alguno, la skill te lo pide y frena. Antes de generar nada, te hace **una sola pregunta consolidada** (tipo, cantidad de slides/stories, modo visual, hook) con propuestas por default; confirmás o editás, y recién ahí genera.

El output siempre es: **shot list / brief creativo** + **N prompts numerados** listos para pegar en nano banana junto a la imagen del producto.

---

## Patrón de carpetas por cliente

Creá **una carpeta por cliente** y dejá adentro un `CLAUDE.md` con su contexto: marca, tono, paleta, links a su Drive/Notion, datos clave. Al abrir Cowork en esa carpeta, ese `CLAUDE.md` se carga como contexto del proyecto y el stack lo hereda en todo lo que produce.

Las skills funcionan igual en cualquier carpeta — lo único que cambia es el contexto del cliente. Así el mismo plugin sirve para todos los clientes sin tocar el plugin.

```
clientes/
  cliente-acme/
    CLAUDE.md        ← contexto de Acme (marca, tono, paleta, links)
    entregables/
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
.claude-plugin/plugin.json     Manifiesto del plugin
.mcp.json                      Definición de los MCP servers
hooks/hooks.json               Hook de SessionStart
hooks/context/stack-policy.md  Política inyectada en cada sesión (lo que recibe el end user)
skills/carrusel-nano-banana/   Skill de carruseles 4:5
skills/stories-nano-banana/    Skill de stories 9:16
scripts/validate-plugin.mjs    Validador de integridad (JSON + refs de SKILL.md)
.github/workflows/validate.yml CI que corre el validador en cada push/PR
CLAUDE.md                      Guía técnica para desarrollar el plugin (solo en-repo)
README.md                      Este archivo — cómo usar el stack
```

Para todo lo técnico (cómo está armado el plugin, cómo agregar una skill o un MCP, cómo distribuir), andá a [`CLAUDE.md`](./CLAUDE.md).
