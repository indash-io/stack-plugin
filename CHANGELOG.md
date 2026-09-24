# Changelog

## 0.19.0 — 2026-09-22

**Una sola puerta: `/new-client` es el onboarding entero.** Acompaña a las
tools `analyze_brand` y `confirm_brand_analysis` del conector
(indash-io/mkt-agents). Las cuatro tools de onboarding siguen siendo
requeridas; las dos de análisis no: si el conector no las tiene, la skill
saltea ese paso y lo dice.

- **`new-client` absorbe a `brand-onboarding`.** Eran dos puertas para el
  mismo cliente, y `new-client` (el nombre que el equipo ya usa) llevaba por
  el camino viejo: carpeta local y `CLAUDE.md` analizando el sitio, sin tocar
  el onboarding de la app. Ahora conduce el onboarding entero, en este orden:
  nombre y workspace en Indash (si la marca no existe, el workspace lo crea
  Indash en la app; no hay tool, y sin workspace no hay onboarding); la carga
  al mismo onboarding de la app, conversada o masiva desde una carpeta (tabla
  de clasificación, un OK, subida por URL firmada en lotes); tienda temprano;
  Instagram solo con un sí; cierre con inventario y veredicto.
- **El análisis, nuevo.** Con el inventario en `can_start` o
  `can_start_with_pending`, la skill ofrece `analyze_brand`: el server produce
  lo derivado (perfil de voz, objeciones priorizadas, verbatims, avatar,
  sistema visual) solo con el material del cliente. Nace `pending` y **el
  agente de briefs no lo ve hasta que un humano lo confirme**: la skill muestra
  el resumen rama por rama y guarda las decisiones con
  `confirm_brand_analysis`. Sin reseñas y sin corpus, `not_enough_material`:
  se dice qué falta y no se insiste.
- **La carpeta local pasa a ser opcional y va al final.** "¿Armamos también
  la carpeta local para producir desde acá?". El `CLAUDE.md` del cliente ya
  no se escribe desde el sitio: su fuente es lo que hay en Indash
  (`get_brand_context` + `get_brand_kit` + `list_products`), y lo que el
  onboarding no tiene queda como placeholder que dice dónde se carga. Nunca al
  revés: el `CLAUDE.md` no es fuente del onboarding. Los templates
  (`client_claude_md.md`, `brand_md.md`, `product_index.md`) se reescriben
  con esa fuente; desaparece el "análisis de marca" desde la URL y los
  adjetivos de personalidad.
- **`brand-onboarding` se elimina.** Salió en la 0.18.0 como `draft` y nunca
  se publicó: no hay nadie que se quede sin ella. Sus disparadores ("cargá mi
  marca", "onboarding de marca", "el cliente me mandó todo esto, cargalo") y
  su materia prima (la regla de procedencia, "material, no adjetivos", la
  carga masiva) pasan a `new-client`, que queda `published`.
- `content-brief`, `stack-overview`, la política del hook, el README y
  `CLAUDE.md` dejan de nombrar `brand-onboarding`: **11 skills** (eran 12) y
  **37 tools** (eran 35), con la familia "El onboarding de marca" en 6.

## 0.18.0 — 2026-09-20

**El onboarding de marca se puede hacer conversando.** Acompaña a las tools
`get_brand_onboarding`, `update_brand_onboarding`, `create_onboarding_uploads`
y `run_brand_onboarding_action` del conector (indash-io/mkt-agents). **Requiere
ese server desplegado**: sin las cuatro tools la skill frena y manda al
onboarding de la app.

- **Skill nueva: `brand-onboarding`.** Es el mismo onboarding de la app (6
  pasos) y escribe al mismo lugar, así que se puede hacer mitad en Claude y
  mitad en `/w/<slug>/onboarding`, y lo cargado lo lee después `content-brief`.
  Arranca siempre leyendo lo que ya hay y no repregunta.
- **Dos modos.** Conversado, para el cliente: de a una cosa, con la pregunta
  literal de la app, aceptando lo incompleto y el "ninguno". Carga masiva, para
  quien llega con una carpeta (el equipo con lo que el cliente mandó por
  WhatsApp): inventario, **tabla de clasificación archivo → lista → por qué**,
  un OK, y recién ahí la subida por URL firmada en lotes de 20. Los audios se
  transcriben en el server.
- **La regla de procedencia.** A ningún campo entra nada que la persona no haya
  dicho, pegado, subido o aprobado explícitamente en la conversación. El
  material va crudo (las reseñas, con sus errores de tipeo). Lo que Claude saca
  de un material largo se muestra entero y espera su OK. Un resumen devuelve
  lenguaje de marketing y el copy sale genérico; un hueco a la vista se resuelve
  con un mensaje, uno tapado aparece en la ronda de revisión.
- **Opt-ins explícitos**: `read_instagram` solo si la persona lo pide o lo
  acepta, y `complete` solo cuando dice que terminó. El cierre muestra el
  inventario con su veredicto: compuertas, no porcentajes.
- **Como `content-brief`, es un wrapper fino**: las preguntas de cada paso y
  qué acepta cada campo los sirve el conector con `include_guide`. La skill no
  los copia.
- `new-client` y `brand-onboarding` se nombran entre sí: una arma la carpeta
  local, la otra carga Indash, y ninguna exige a la otra. `content-brief`, sin
  contexto de marca, ofrece completar el onboarding acá mismo.
- `stack-overview`, la política del hook y el README: **12 skills** (eran 11) y
  **35 tools** (eran 31), con la familia nueva "El onboarding de marca".
- La skill sale en `status: draft`: falta la lectura de un humano.

## 0.17.0 — 2026-09-18

**El brief del período se arma con el contexto y la metodología de la app.**
Acompaña a las tools `get_brand_context` y `save_brief` del conector
(indash-io/mkt-agents, rama `manuel-soria/mcp-brand-context`). **Requiere ese
server desplegado**: sin las dos tools la skill frena y lo dice.

- **`content-brief` pasa a ser un wrapper fino.** Antes traía su propia
  metodología (intake, discovery, plan, bloques por pieza), distinta de la del
  agente de briefs de la app: un brief armado en Claude y uno armado en Indash
  salían de criterios distintos. Ahora la metodología (`AGENT.md` +
  `ecom-founder` + `content-brief-builder`) la sirve el conector en vivo, la
  misma que usa la app, y la skill solo fija el orden: `get_brand_context` con
  `include_methodology` → armar → `save_brief` → corregir según los chequeos →
  `send: true` cuando la persona lo confirma. Se borran `instructions/`,
  `templates/` y `eval/` de la skill: **una sola fuente**.
- **El contexto de marca sale del onboarding del cliente** (el CKB), con sus
  archivos originales: las imágenes se abren como imágenes, el resto llega como
  URL firmada que en Claude Code se puede bajar y leer local. Si el workspace
  no tiene onboarding ni `CONTEXT.md`, la skill lo dice, ofrece completarlo y
  avanza con el mínimo marcando el resto como pendiente.
- **El brief queda guardado en Indash**, con su URL y los mismos chequeos que
  ve el equipo al aprobar. La copia en `briefs/` sigue, como copia de trabajo.
- El brief cubre los cuatro formatos de la metodología (video UGC, estático,
  carrusel, historia). Emails y videos que no son UGC ya no salen del brief:
  van directo a `email-marketing-ecomm` y `all-videos`.
- `stack-overview`, la política del hook y el README: **31 tools** (eran 29), la
  familia nueva "El brief del período", y el kanban de `upload_briefs`
  renombrado a "pedidos" para que no se confunda con el brief. De paso entran
  al listado `list_creatives` y `update_product_images`, que estaban contadas
  pero no nombradas.

## 0.16.0 — 2026-09-08

**Videos de hasta 40 segundos y la familia GPT Image 2.5.** Acompaña a
indash-io/mkt-agents#286, #287 y #288.

- **`extend_video`**: continúa un clip de `omni` agregando 3-10s por turno,
  hasta **40s**. Cambia el orden del trabajo: generás el primer beat, el
  cliente lo aprueba, y recién ahí pagás la continuación — en vez de apostar a
  un render largo que no podés ver hasta que termina. `model_selection.md`
  ahora ramifica por ahí, y `stack-overview` explica las cuatro reglas del
  encadenado (serial, sobre el último `run_id`, un creative por turno, se
  cobra lo agregado).
- **GPT Image 2.5** en sus dos variantes: `gpt-image-2.5-flare` (mejor que el
  2 a la mitad de latencia) y `gpt-image-2.5-sunburst` (control fino en
  ediciones, para el entregable final). **Cuestan lo mismo que gpt-image-2.**
- **`gpt-image` pasa a llamarse `gpt-image-2`.** El nombre genérico era parte
  del problema: durante cuatro meses renderizó `gpt-image-1` sin que nada lo
  delatara. El nombre viejo sigue funcionando como alias, pero las skills ya
  nombran el nuevo.
- Las tablas de modelos de `prompt-craft` y `ads` dejan de recomendar
  `openai/gpt-image-1`, que no era ni el que corría ni el que convenía.
- El conteo de tools del conector estaba viejo: eran 26 en la doc y hoy son
  **29**.

## 0.15.0 — 2026-09-07

**El roster de modelos del MCP cambió, y con él las decisiones de costo.** Las
skills decían "máx 15s" y recomendaban 1080p por defecto; las dos cosas ya no
son ciertas. Acompaña a indash-io/mkt-agents#281.

- **Seedance 2.5** (`seedance-2.5` y `seedance-2.5-ark`): 4-30s en UN render
  — nada más en el roster llega a 30 — con 10 referencias de imagen, video y
  audio, last frame y text-to-video. `reference/model_selection.md` y
  `reference/seedance_2_params.md` cubren 2.0 y 2.5.
- **Omni Flash 1.1** (`omni`): pasa a la API nativa de Google. 10 refs de
  imagen, 3 clips de video de hasta 3s, last frame, text-to-video, y un tier
  de **360p que sale un tercio de 720p** — el modelo para draftear.
- **Kling O3 Pro** (`kling`): más nuevo y más barato. **Perdió el negative
  prompt**; `veo` es el único que queda con ese campo, y las skills lo dicen.
- **Nano Banana 2 Lite** (`nano-banana-2-lite`): tier de imagen para draftear,
  mitad de créditos que `nano-banana-2`.
- **La resolución ahora es una decisión de costo, no de calidad.** La familia
  seedance y omni cobran por píxeles: 1080p sale ~2.25x lo que sale 720p. Las
  skills pasan a recomendar 720p por defecto (antes `seedance_2_params.md`
  decía 1080p) y a draftear en 360p/480p.
- **Las rutas `-ark` cuestan la mitad** que sus gemelas de fal por el mismo
  modelo. Estaba disponible desde julio y ninguna skill lo decía.
- `seedance_2_params.md` aclara además qué parámetros del archivo **no viajan**
  por `generate_video` (`fps`, `creativity_scale`, `temporal_smoothing` no
  tienen campo en la tool).

## 0.14.0 — 2026-08-28

**Tres bugs de carga que no se veían en el repo y sí en la máquina de cada
uno.** El validador ahora los atrapa.

- **El plugin no cargaba en Claude Code ≥ 2.1.25x**: `hooks/hooks.json` usaba el
  formato viejo (`SessionStart` en el top-level). El formato oficial es
  `{ "hooks": { "SessionStart": [...] } }`; sin eso Claude Code rechaza el
  plugin entero ("Hook load failed") y no carga ni una skill.
- **Tres skills desaparecían en Claude Desktop** (`all-videos`, `carruseles`,
  `stories-nano-banana`): la `description` tenía `: ` adentro y el parser YAML
  real la rechazaba — el plugin mostraba 11 skills de 12. Van entre comillas y
  el validador falla si un valor plano tiene `: ` o ` #`.
- **`/save-learnings` pasa de `commands/` a `skills/save-learnings/`** con
  `disable-model-invocation: true`: Claude Desktop y Cowork no listan los
  commands de un plugin, y la doc oficial recomienda `skills/`. Se invoca
  `/save-learnings` en todos los clientes; el modelo sigue sin poder dispararla.

## 0.13.0 — 2026-08-27

**`/save-learnings` ahora entrevista antes de redactar.** El feedback de la
daily del 2026-08-26: el challenge está en quien corre el comando, no en quien
lee el issue. Hasta ahora el agente armaba el borrador solo y el "por qué" salía
de su inferencia — que es justo el dato que hace triageable un learning.

- **Paso nuevo de entrevista**, después de detectar las skills y antes de
  clasificar: **una sola pregunta consolidada** (la convención del stack, no una
  batería de preguntas sueltas) con qué hiciste (el agente lo pre-llena desde el
  contexto y la persona confirma), dónde se trabó, qué cambiarías concretamente
  y **por qué**. Si la persona invocó el comando con una nota, esa nota es la
  primera respuesta y solo se pide lo que falte.
- **El "por qué" lo escribe la persona.** Regla no negociable: si no lo contesta,
  el agente lo pide una vez más y, si sigue sin venir, **el learning queda
  afuera** — lo dice en el borrador. Nunca lo inventa ni lo rellena con una
  inferencia.
- **Formato antes / propongo / por qué** para cada learning de skill: `skill`,
  `before`, `after`, `why` y `example?` (reemplaza a `text` + `suggested_change`
  en el payload de `save_learnings`). Cada learning es **un cambio concreto y
  acotado** — nunca "reescribir la skill" ni cuatro cambios en un ítem — y el
  comando trae ejemplos buenos y malos para calibrarlo. La anonimización se
  aplica a los cuatro campos, no solo al primero.
- **Se corre a conciencia**, no como cierre automático de cada entrega: llenar el
  inbox de ruido es peor que no reportar. `stack-policy.md` y `stack-overview`
  ahora dicen que el agente lo sugiera **solo si en la sesión hubo fricción con
  una skill** (se pidió rehacer algo, se corrigió a la skill, algo no sirvió).
- Los learnings **del cliente** (`brand_learnings`) no cambian de formato.
- De paso: el paso 1 del comando listaba 10 skills: ahora lista las 12, con
  `hyperframes` y `edicion-ugc`.

## 0.12.0 — 2026-08-26

**Skill nueva: `edicion-ugc`** — el **montaje determinístico** de clips de
avatar/UGC. Es la segunda skill de post-producción del stack y la primera con
**código ejecutable**: `scripts/editar.py` (FFmpeg + whisper-cpp + Pillow) y
`scripts/setup.sh`.

- **Todo lo que hace sale de medir 21 ediciones manuales reales** (n=10 y n=11
  en dos marcas), validadas después en 4 marcas: recorta silencios de cabeza y
  cola siempre, comprime pausas internas de más de 0.50s a 0.45s, entra a cada
  clip 3 frames antes de la voz para no repetir la pose del still en el empalme,
  detecta morphs y los tapa con un bloque único de B-roll que termina al 72% del
  diálogo, quema subtítulos de 2-4 palabras en Montserrat SemiBold 32 (y=1027) y
  pega la placa final (1.50s si es imagen; entera si es video). Export 720×1280,
  24fps, ~6 Mbps. La procedencia de cada número, con su tamaño de muestra, está
  en el `SKILL.md`: la placa sale de 21 casos y el largo del B-roll de 4 — no
  valen lo mismo y la skill lo dice.
- **Dos modos**: `revisar` mide y reporta morphs con timestamp sin renderizar
  nada (paso obligatorio), `montar` hace la edición completa.
- **Límites explícitos, no tapados**: el detector de morph es ciego a las
  derivas graduales (`morph 0.000` significa "sin saltos secos", no "clip
  limpio"), un pico de score no siempre es un morph, Whisper escribe mal los
  nombres de marca, y nadie escucha el audio.
- **Gate del conector `indash`: condicional**, como en `hyperframes`. Edita
  material que ya está en disco, así que no lo necesita — salvo que haya que
  generar un B-roll para tapar un morph sobre voz, y ahí sí frena y lo pide.
  No consume créditos.
- **Config y placa por cliente, no en el plugin.** Reemplaza los perfiles por
  marca que traía la skill original por la convención del stack: busca
  `brand/edicion-ugc.json` y `brand/placa.*` en la carpeta del cliente (también
  en `assets/brand-kit/` y `assets/logos/`), además de la detección que ya tenía
  (`Placa/`, `Logos/`, nombre con `placa|outro|cierre|endcard`). El plugin es
  público: no lleva datos, placas ni perfiles de ningún cliente. Formato
  documentado en `templates/brand-edicion-ugc.example.json`.
- **Salida por convención del stack**: sin `salida` explícita, el MP4 va a
  `exports/videos/<AAAA-MM-DD>_<slug>_v<N>.mp4` de la carpeta del cliente, y
  **nunca pisa** — sube la versión.
- **Requisitos, dichos arriba de todo**: macOS + Homebrew, ffmpeg, whisper-cpp,
  el modelo `ggml-large-v3-turbo` (1.5 GB) y Montserrat. Los instala
  `scripts/setup.sh`, que es idempotente. Si falta algo, `editar.py` frena con
  la lista de lo que falta y manda a correr el setup, en vez de tirar un
  traceback.
- **El venv vive fuera del plugin**, en `~/.indash/edicion-ugc/venv`: la carpeta
  del plugin es una cache que se pisa entera en cada auto-update del
  marketplace. El modelo de whisper sigue en `~/.cache/whisper-cpp/`.

**`edicion-ugc` vs. `hyperframes`** — las dos son post-producción y ahora ambas
lo aclaran: `edicion-ugc` es el pipeline determinístico para montar clips de
avatar (análisis + reglas medidas + render FFmpeg); `hyperframes` es composición
creativa. *"Montame estos clips de avatar"* → `edicion-ugc`; *"armame una pieza
con estos assets / captions con estilo / placa animada"* → `hyperframes`. **Está
planificado** que `edicion-ugc` emita un plan de edición que `hyperframes`
renderice (v2); **hoy no lo hace**, y las dos skills lo dicen para que nadie
prometa un handoff que no existe.

**Convenciones nuevas del repo**

- Una skill puede traer `scripts/`. Regla dura documentada en `CLAUDE.md`: nada
  mutable adentro de la carpeta del plugin, y `${CLAUDE_PLUGIN_ROOT}` siempre
  con fallback explícito.
- `brand/` vuelve a la estructura del cliente como carpeta **opcional** de config
  de skills locales (`brand/placa.*`, `brand/edicion-ugc.json`). No la crea
  `new-client`: aparece cuando hace falta.

El stack pasa de 10 a **11 skills**.

## 0.11.0 — 2026-08-25

**El plugin pasa a tener mantenimiento de verdad.** Esta release trae la
primera skill de post-producción (`hyperframes`), el lado cliente del feedback
loop de learnings (`/save-learnings`) y la metadata que necesita el skills hub
interno de Indash para auditar el inventario.

### Command nuevo: `/save-learnings`

- Al cerrar una sesión, revisa qué skills se usaron, separa los learnings **del
  cliente** (DOs/DON'Ts y contexto → `LEARNINGS.md` del workspace en Indash, vía
  la tool nueva `save_learnings` del conector) de los **de la skill**
  (universales, anonimizados → issue privado del equipo). Muestra el borrador y
  **no manda nada sin confirmación**. `disable-model-invocation: true`: lo
  dispara la persona, nunca el modelo.
- `stack-policy.md` y `stack-overview` lo explican; al terminar una entrega el
  agente lo sugiere en una línea.
- El conector pasa de 25 a **26 tools** (`save_learnings`, gratis).

### Metadata de mantenimiento en cada skill

- Frontmatter con tres campos nuevos y obligatorios: `owner` (login de GitHub
  de quien la mantiene), `status` (`published | draft | deprecated` —
  `deprecated` es el primer paso de la baja) y `reviewed` (última revisión
  humana, `YYYY-MM-DD`). El validador los exige, en `skills/` y en
  `core/skills/`.

### Higiene del repo

- El repo es **público**: README y marketplace ya no dicen "privado".
- `.github/CODEOWNERS`, templates de issue (`suggestion`, `new-skill`) y
  `scripts/setup-github.sh` (labels + branch protection, lo corre un humano).
- Tags `v0.9.0` y `v0.10.0` que faltaban.


**Skill nueva: `hyperframes`** — el paso de **post-producción** que le faltaba
al stack. Agarra los clips, frames e imágenes que ya generaron `all-videos`,
`ugc-generator` y `carruseles`, y los ensambla en la pieza final con
[HyperFrames](https://github.com/heygen-com/hyperframes), el framework open
source de HeyGen (Apache 2.0) que renderiza video determinístico a partir de
HTML/CSS + media + animaciones seekables.

- **Es `prompt-only`**: no agrega ninguna tool al MCP de Indash ni consume
  créditos. El render corre **local** con la CLI de HyperFrames (requiere
  Node.js 22+ y FFmpeg), con un mode switcher `full_render` / `plan_only`
  según lo que banque la máquina.
- **Workflow del stack**: intake → discovery (inventario de `exports/`,
  duraciones medidas con `ffprobe`, marca) → una sola pregunta consolidada →
  plan de edición por segundos con hook en 1-3s → composición HyperFrames +
  comando de render → self-check → escalera de gates (`lint` → `check` →
  `draft` → aprobación del user → `high`) → guardado en `exports/videos/`
  con la nomenclatura canónica.
- **`reference/hyperframes.md`**: todo lo verificado en fuentes primarias
  (README del repo y docs oficiales, 2026-08-25), separando **confirmado** /
  **inferido** / **verificar**. Es la única fuente de sintaxis que la skill
  puede citar; `examples/bad/api_inventada.md` documenta los diez atributos y
  flags que un agente inventa por analogía y que **no existen**.
- **`style/safe_zones.md`** extiende a Reels/TikTok/ads la convención de zona
  segura que ya usaba `stories-nano-banana` (14%–85% vertical), incluyendo el
  rail de acciones lateral en 9:16.
- Sincronizados los lugares que listan skills: `stack-policy.md`,
  `stack-overview` (9 → 10 skills, y se corrigió la sección que decía que la
  post-producción "sigue sin existir"), `README.md`, los dos `plugin.json`,
  `marketplace.json`, `CLAUDE.md`, y las referencias cruzadas en
  `content-brief` y `new-client`.

## 0.10.0 — 2026-08-19

**`seedance-multishot` evoluciona a `all-videos`** — la skill de video deja de
ser Seedance-only y pasa a ser la skill general de videos de marketing, con
selección de modelo por shot. Se integró desde un zip externo (`all-videos`)
que era un fork de `seedance-multishot`: se tomó lo nuevo del fork sobre la
base ya alineada del repo (persistencia, herencia de marca, gate, params
multimodales de 0.8.0), en vez de copiarlo verbatim.

- **Nuevo `reference/model_selection.md`**: roster de los 6 modelos del MCP
  (seedance, seedance-ark, omni, veo, kling, grok-imagine), decision tree por
  shot, workflow draft-en-Omni → final-en-Seedance, y best practices por
  modelo.
- **SKILL.md**: la hard rule "One model, one purpose" se reemplaza por
  "Model selection is strategist work"; se suman al multi-ref discipline los
  aprendizajes validados (refs = soft conditioning, single-take multi-ref con
  producto estático, stop-motion discreto para transformaciones,
  negative-space choreography, constraints por motion prompt); y se agrega la
  sección "Generalist intake" para briefs que no matchean los 4 templates.
- **Anonimización**: el fork traía marcas de clientes (casos reales) que acá
  se reemplazaron por categoría genérica, con el criterio del barrido de
  0.7.x. Las versiones del fork de los archivos compartidos NO se copiaron:
  eran anteriores a la anonimización y al cableado multimodal de 0.8.0.
- Sincronizados los lugares que listan skills: `stack-policy.md`,
  `stack-overview`, `README.md`, `marketplace.json`, `CLAUDE.md`, y las
  referencias cruzadas en `content-brief` y `new-client`.

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
