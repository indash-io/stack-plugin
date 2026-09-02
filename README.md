# Indash Stack — branch `studio`

> **Esta branch es el mundo nuevo.** Acá viven los **dos sets de skills curados**
> para el ecosistema Studio: el de **ejecución** (lo consume Indash Studio, la app
> de escritorio) y el de **ideación** (lo consume el armador de briefs hosteado).
> Las skills del mundo plugin clásico (claude.ai / Cowork, con el conector MCP
> hosteado) siguen viviendo en **`main`** — esta branch no las reemplaza allá.

## El modelo

El flujo objetivo es **95% brief-driven**: un agente hosteado arma el brief
(ideación), y el Studio lo ejecuta (producción por capas, candidatos versionados,
aprobación humana). La bisagra entre los dos mundos es **el bloque por pieza**:
un formato de decisión escrita que la ideación produce y `new-brief` vuelca a
`plan.json` mecánicamente, sin re-decidir nada.

- Contrato canónico: [`skills/content-brief/templates/bloque_por_pieza.md`](./skills/content-brief/templates/bloque_por_pieza.md)
- Espejo (para el set de ejecución, que se siembra standalone): [`skills/new-brief/reference/bloque-por-pieza.md`](./skills/new-brief/reference/bloque-por-pieza.md)

## SET EJECUCIÓN — 6 skills (destino: Indash Studio)

Se siembran **standalone** (cada carpeta se copia entera a `~/.claude/skills/` de
la máquina del usuario; el Studio gestiona el ciclo de vida). Ninguna referencia
archivos de otra skill. El contrato de disco (manifiestos `.indash`, candidatos
append-only, guard) vive en el `CLAUDE.md` que el Studio siembra en cada proyecto.

| Skill | Momento | Qué aporta esta versión sobre la del Studio 0.6.8 |
|---|---|---|
| `new-workspace` | Alta de una marca | + el interrogatorio de discovery (una pregunta consolidada, paleta en hex, placeholders — jamás inventar) |
| `new-brief` | Brief → Board | + el mapeo mecánico desde el bloque por pieza (`reference/bloque-por-pieza.md`) |
| `creative-execution` | Producir piezas estáticas | + las 7 leyes de prompting (mundo capas), recetas de composición de texto, dispositivos de diseño, **zonas seguras 2026** (Meta unificado marzo 2026 + grilla 3:4) |
| `video-execution` | Producir un video UGC | + referencia de modelos (omni/seedance/veo/kling), regla de las 3 fidelidades, disciplina de frame-0 |
| `export-creatives` | Entregar | (igual a la del Studio) |
| `save-learnings` | Guardar lo aprendido | Adaptada al Studio: usa la tool `mcp__indash__save_learnings` del MCP in-process (requiere workspace conectado + login) |

## SET IDEACIÓN — 6 skills (destino: el armador de briefs hosteado)

Corren en el contexto del agente hosteado, con el MCP de indash.ai (brand kit,
catálogo, referencias, kanban de briefs). **No generan imágenes ni videos**: su
output son bloques por pieza plan-ready. `content-brief` orquesta; las demás
aportan el oficio por formato.

| Skill | Qué decide |
|---|---|
| `content-brief` | La orquestadora: objetivo del período → mix de piezas + funnel → deriva a las de formato → brief final en bloques |
| `ideacion-carruseles` | Arquetipo, narrativa hook→desarrollo→CTA, slides, modo visual, copy on-image |
| `ideacion-stories` | Arquetipo de secuencia, copy ≤6-8 palabras, **sticker de engagement por story** |
| `ideacion-ads` | Ángulos scroll-stop, variaciones A/B reales, **copy de Meta completo** con límites |
| `ideacion-video` | Grupo `kind: video` + `seconds`, guion + registro + gesto por clip, UGC y video de marca |
| `ideacion-emails` | 3 ángulos, subjects + preheaders + hipótesis (la ejecución HTML no pasa por el Studio) |

## Zonas seguras canónicas (2026)

Fuente única en `skills/creative-execution/data/safe-zones.json`. Resumen sobre
canvas estándar (Meta unificó el 9:16 en marzo 2026; la grilla de perfil de IG es
3:4 desde fines de 2025):

| Formato | Canvas | Top | Bottom | Left | Right |
|---|---|---|---|---|---|
| story | 1080×1920 | 270 | 380 | 65 | 65 |
| reels | 1080×1920 | 270 | 670 | 65 | 120 |
| feed 4:5 | 1080×1350 | 64 | 64 | 100 | 100 |
| square | 1080×1080 | 64 | 64 | 140 | 140 |

Una pieza 9:16 que va a Stories **y** Reels se compone contra la zona de Reels.

## Qué pasó con las skills viejas

| Vieja (en `main`) | Destino |
|---|---|
| `new-client` | Absorbida por `new-workspace` |
| `carruseles` / `stories-nano-banana` / `ads` / `email-marketing-ecomm` | Partidas: estrategia → `ideacion-*`; producción → `creative-execution` |
| `ugc-video-prompts` / `ugc-generator` / `all-videos` | Cosechadas en `video-execution` + `ideacion-video` |
| `content-brief` | Reorientada como orquestadora de ideación |
| `save-learnings` | Adaptada al Studio |
| `core/` (prompt-craft + formatos IG) | Repartido: leyes → `creative-execution/reference/`; specs → `formats/`; narrativa → ideación |
| `stack-overview`, `hyperframes`, `edicion-ugc` | Quedan en `main` (mundo plugin); post-producción sin destino en Studio todavía |

## Estado

- `status: draft` en todas: pendientes de revisión humana (al aprobar, pasar a `published` y actualizar `reviewed`).
- La tool `save_learnings` del Studio (MCP in-process + endpoint en la Studio API) se está implementando en paralelo en `indash-io/studio` y `indash-io/mkt-agents`.
- Cómo consume el Studio esta branch (en vez de sus `resources/skills/` embebidas) se decide/cablea aparte.

Para la guía de desarrollo del repo, ver [`CLAUDE.md`](./CLAUDE.md) (escrita para `main`; en esta branch valen las convenciones de frontmatter, registro y validador).
