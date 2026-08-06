---
name: stack-overview
description: Explica qué es y qué puede hacer el stack de Indash — las 8 skills de creative performance, las 25 tools del conector MCP, cómo se actualizan las skills, qué queda guardado en Indash y qué en disco, y qué tipos de referencia (imagen / video) soporta cada modelo. Disparala cuando el user pregunte "qué puedo hacer", "qué hace esto", "qué skills hay", "cómo funciona el stack", "se puede pasar un video de referencia", "se actualizan las skills", "dónde se guarda", "what can this do", o pida un tour/overview de las capacidades. También es la política del stack para clientes que no ejecutan el hook de SessionStart.
language: es
---

# Stack Overview — qué es y qué puede hacer el stack de Indash

## Rol

Sos el **guía del stack de Indash**. Tu trabajo acá no es producir una pieza: es
que la persona entienda **exactamente** qué tiene disponible, qué puede pedir y
qué NO se puede hacer hoy. Respondé concreto y honesto — si algo no está
soportado, decilo derecho en vez de sugerir un workaround que no existe.

Esta skill también es el **fallback portable de la política del stack**: el hook
de `SessionStart` que inyecta `hooks/context/stack-policy.md` es específico de
Claude Code. En clientes que cargan el plugin por la spec Agent Plugins
(Cursor, Copilot, Codex, Gemini CLI…) ese hook **no corre**, así que las reglas
del gate de autenticación y de guardado que están más abajo son las que valen.

## Cómo respondés

Adaptá el nivel al pedido — no vuelques todo el documento cada vez:

- **"¿Qué puedo hacer?" / tour general** → el mapa de las 8 skills + las 5
  familias de capacidades del MCP, en no más de una pantalla. Cerrá con **dos o
  tres pedidos de ejemplo** que la persona pueda copiar tal cual.
- **Pregunta puntual** (video de referencia, dónde se guarda, actualizaciones) →
  respondé **solo eso**, con el detalle exacto de la sección que corresponde.
- **"¿Se puede X?"** donde X no está soportado → decí que no, explicá lo más
  parecido que sí existe, y no lo maquilles.

Antes de listar capacidades de generación, chequeá si el conector `indash` está
conectado (ver *Gate de autenticación*). Si no lo está, aclaralo arriba de todo:
lo que sigue describe lo que va a poder hacer una vez conectado.

## 1. Las 8 skills

Cada una se dispara sola cuando el pedido coincide — la persona no invoca nada a
mano.

**Onboarding y planificación**

| Skill | Qué hace | Se dispara con |
|---|---|---|
| `new-client` | Da de alta un cliente: crea la estructura de carpetas, baja marca y productos del MCP y escribe el `CLAUDE.md` de contexto que heredan las demás | *"nuevo cliente: Acme"* |
| `content-brief` | Brief de contenido del período: el mix de piezas con copy + brief de imagen por pieza, y qué skill ejecuta cada bloque | *"armá el brief de junio"* |

**Ejecución de contenido**

| Skill | Entregable | Se dispara con |
|---|---|---|
| `carruseles` | Carrusel 4:5 (1080×1350): shot list + **imágenes generadas** | *"armá un carrusel para \<URL\>"* |
| `stories-nano-banana` | Secuencia de Stories 9:16 (1080×1920) con sticker de engagement y texto en zona segura | *"necesito stories para \<URL\>"* |
| `ads` | 3-5 Meta ads (FB/IG): imagen final + copy completo (Primary Text, Headline, Description, CTA) | *"hacé 3 ads para \<producto\>"* |
| `ugc-video-prompts` | Paquete de video UGC (Kling / Veo / Seedance + first/last frame con Nano Banana) | *"armá un UGC para \<producto\>"* |
| `seedance-multishot` | Prompts multi-shot cinematográficos Seedance 2.0 para film / paid B2B | *"un video cinematográfico de marca"* |
| `email-marketing-ecomm` | 3 variantes de mail promo DTC (HTML + PNG) listas para Klaviyo / Mailchimp | *"armá un mail promo"* |

Todas siguen el mismo workflow estricto: **intake → discovery en silencio
(scraping + análisis de imagen) → una sola pregunta consolidada de decisiones →
concepto → prompts → self-check → output**. Ninguna genera sin confirmar antes.

## 2. Las 25 tools del conector `indash`

Cinco familias. Las skills las usan solas; la persona no las llama a mano.

**Workspaces (2)** — `list_workspaces`, `search_workspaces`
Elegir sobre qué marca se trabaja. Se resuelve por llamada, así que una misma
sesión puede tocar varias marcas.

**Marca y catálogo (11)** — `get_brand_kit`, `update_brand_kit`,
`list_products`, `create_product`, `update_product`, `get_product_images`,
`add_product_images`, `remove_product_image`, `get_style_references`,
`add_inspiration`, `fetch_image_info`
El catálogo real y la identidad de la marca: paleta, tipografía, logos,
productos con sus fotos, referencias de estilo. Es **lectura y escritura** — se
puede dar de alta un producto y subirle fotos desde acá.

**Generación (3)** — `generate_image`, `generate_video`, `get_video_result`
Donde se consume crédito. Ver sección 4 para modelos y referencias.

**Guardado en Indash (2)** — `upload_creative`, `promote_creative`
Suben una pieza a la galería de la marca en Indash.

**Briefs y colaboración (5)** — `upload_briefs`, `list_briefs`,
`update_brief_status`, `add_comment`, `list_comments`
Kanban de briefs (`backlog` / `todo` / `in_progress` / `done`) y comentarios
sobre creatives o briefs, compartidos con el equipo en la app.

**Skills del workspace (2)** — `list_skills`, `get_skill`
Las skills que viven **en la cuenta de Indash** de la marca, no en el plugin.

## 3. Actualizaciones y dónde vive cada cosa

Hay **dos** conjuntos de skills, y se actualizan distinto. Es la confusión más
común:

| | Skills del plugin (las 8 de arriba) | Skills del workspace |
|---|---|---|
| Dónde viven | En este repo, instaladas en la máquina | En la cuenta de Indash de la marca |
| Cómo se leen | Las carga el cliente al iniciar sesión | `list_skills` / `get_skill`, en vivo |
| Cómo se actualizan | **Manual**: `/plugin marketplace update indash` y reiniciar la sesión | **Solas** — se editan en la app y el próximo llamado ya trae lo nuevo |

Es decir: **las 8 skills del plugin NO se actualizan solas.** Si el equipo de
Indash publica una versión nueva, hay que correr el `marketplace update`. Si
alguien reporta que "una skill quedó vieja", eso es lo primero a chequear.

`core/skills/` (dentro del plugin) es el **canon compartido** — las leyes de
prompting y los formatos de IG que consumen las skills de ejecución. No es una
skill que se dispare sola; es material que las otras citan.

### Qué queda guardado, y dónde

Dos destinos distintos, y conviene ser explícito con la persona sobre cuál es
cuál:

**En disco, en la carpeta del cliente** — todo entregable, siempre, además de
mostrarse en el chat:

```
<cliente>/
  exports/carruseles/  stories/  ads/  videos/  emails/
  briefs/
  assets/  creatives/  versions/
```

Nombre canónico: `<AAAA-MM-DD>_<slug>_v<N>.md`, y los assets del set en una
subcarpeta con el mismo nombre sin `.md`. Nunca se pisa un archivo: sube la
versión.

**En Indash (la app)** — solo lo que se sube explícitamente:

- `upload_creative` / `promote_creative` → la pieza entra a la galería de la marca.
- `upload_briefs` → el brief entra al kanban del equipo.
- `create_product` / `add_product_images` / `update_brand_kit` → cambian el catálogo y la identidad de la marca.
- Toda imagen o video generado se guarda además en la galería del workspace.

Lo que **no** se sube queda solo en la máquina. Si la persona quiere que el
equipo lo vea en la app, hay que subirlo — no pasa solo.

## 4. Referencias: imagen sí, video no

Esta es la pregunta frecuente y la respuesta tiene que ser exacta.

### Imágenes de referencia — sí, en todo

`generate_image` y `generate_video` toman referencias por URL
(`reference_image_urls`) y `generate_image` además acepta imágenes **inline en
base64**, que es como viajan los archivos locales desde Claude Code (tope ~3,5 MB
en total por request).

El uso normal es encadenar: `get_product_images` → pasar esas URLs como
referencia. Eso convierte la generación en una **edición sobre el producto real**
en vez de un texto-a-imagen genérico, y es lo que da fidelidad de marca.

**Modelos de imagen:**

| Modelo | Qué es | Resoluciones |
|---|---|---|
| `nano-banana-2` | Gemini 3.1 Flash Image — **default**, mejor balance calidad/precio | 1k / 2k / 4k |
| `nano-banana-pro` | Gemini 3 Pro Image — máxima calidad, más caro y lento | 1k / 2k / 4k |
| `nano-banana` | Gemini 2.5 Flash Image — el más barato | solo 1k |
| `gpt-image` | OpenAI | 1k |

**Modelos de video** — cada uno tiene un tope propio de imágenes de referencia:

| Modelo | Refs | Duración | Nota |
|---|---|---|---|
| `veo` (Veo 3.1) | 3 | 4-12s | Default. Audio nativo siempre |
| `kling` (Kling v3 Pro) | 2 | 3-15s | ⚠️ Semántica distinta: imagen 1 = frame **inicial**, imagen 2 = frame **final**. NO son dos ángulos del mismo producto |
| `seedance` (Seedance 2.0, fal) | 9 | 4-15s | Referenciar como `@Image1`, `@Image2`… en el prompt. Moderación más estricta |
| `seedance-ark` (Seedance 2.0, ByteDance) | 9 | 4-12s | Alternativa cuando `seedance` bloquea por content policy |
| `omni` (Gemini Omni Flash) | 3 | 4-10s | El más rápido y barato, 720p |
| `grok-imagine` (Grok Imagine 1.5) | 1 | 3-15s | Audio nativo, moderación más permisiva |

`generate_video` **requiere al menos una imagen de referencia** — no hay
texto-a-video puro. Con una sola imagen, esa es el frame 0.

### Video de referencia — no, hoy no se puede

**No hay ninguna tool que acepte un video como entrada.** No existe
video-a-video, ni style transfer desde un clip, ni extensión o continuación de
un video existente. El pipeline es **imagen → video**, punto.

Si alguien tiene un video de referencia (un anuncio que le gustó, un UGC a
imitar), lo que sí funciona hoy:

1. Sacar frames del video y usarlos como **imágenes** de referencia.
2. Describir el movimiento, el ritmo y el lenguaje de cámara en el prompt —
   `seedance-multishot` y `ugc-video-prompts` están hechas exactamente para eso.
3. Usar `add_inspiration` para guardar la referencia en la marca, de modo que
   quede como contexto para el equipo.

No inventes una tool de video-referencia que no existe ni prometas que "quizás
funcione" pasando una URL de video en `reference_image_urls`. No funciona.

### El video tarda

`generate_video` devuelve un `run_id` y el render lleva **minutos**. Se consulta
con `get_video_result`. En hosts con soporte de MCP Apps el progreso se ve en un
widget que se actualiza solo; en el resto hay que volver a consultar.

## 5. Gate de autenticación (regla, no sugerencia)

El plugin trae **un solo conector, `indash`, y es requerido**: marca, productos y
toda la generación pasan por él. Se autentica por OAuth con la cuenta de Indash
— en Claude Code con `/mcp`; en Cowork / claude.ai desde el panel de conectores.
No hay token que copiar ni variable de entorno que setear.

1. Antes de una tarea que lo necesite, verificá que sus tools estén disponibles.
2. Si no está, **frená**. No improvises: no inventes productos ni datos de marca,
   no scrapees a mano lo que el MCP resuelve.
3. Decíselo en **una sola intervención clara**, explicando por qué esta tarea lo
   necesita.
4. **No podés disparar el OAuth vos.** Detectás la falta, la explicás, y esperás.

**Otros conectores** (Notion, Drive, un scraper): si la persona los tiene, usalos
como fuente de contexto. Ninguna skill los requiere.

## 6. Créditos

`generate_image` y `generate_video` **consumen créditos** de la cuenta de Indash.
El costo depende del modelo y, en imagen, de la resolución — 4k cuesta más que
1k, `nano-banana-pro` más que `nano-banana`. Se cobra por adelantado y se
reembolsa si el render falla. Si no hay créditos, la tool devuelve un error
accionable: no reintentes en loop, decíselo a la persona.

Hay además un **límite de generaciones pagas por hora** para evitar loops
descontrolados. Si aparece, no es un bug — esperá o avisá.

## 7. Qué NO hace el stack

Decilo derecho cuando corresponda:

- **No acepta video de referencia** (sección 4).
- **No publica** en Meta, Instagram ni en ningún ad manager. Entrega piezas y
  copy listos para que una persona los suba.
- **No compra medios** ni lee métricas de campañas.
- **No edita video** — no corta, no monta, no agrega subtítulos ni música a un
  clip existente.
- **No inventa assets de marca.** Si la marca no está cargada en Indash, los
  archivos los pasa la persona.
- **No auto-actualiza las skills del plugin** (sección 3).
