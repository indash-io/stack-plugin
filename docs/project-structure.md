# Spec: estructura unificada de carpeta cliente-proyecto

> **Estado: ADOPTADA en la release 0.4.0 del plugin (2026-07-23).** El dueño
> del scaffolding es este plugin (skill `new-client`); el Studio abre estas
> carpetas nativo y solo exige `creatives/`. Una sola carpeta = un cliente =
> un proyecto del Studio. Esta página (en el repo del plugin) es la fuente
> canónica de la convención; `hooks/context/stack-policy.md` la inyecta en
> runtime.

## El problema que resuelve

Hoy conviven dos convenciones: el Studio scaffoldea `assets/{fonts,logos,…}`,
`creatives/`, `exports/`, `versions/`; la skill `new-client` crea
`brand/{logos,typographies,assets}`, `productos/`, `entregables/`, `briefs/`.
Las skills de contenido, el Studio y el agente terminan adivinando dónde vive
cada cosa. Se unifica en UNA estructura (nombres en inglés, gana la convención
del Studio) y se define quién escribe qué.

## La estructura

```
<cliente>/                      kebab-case del nombre del cliente
  CLAUDE.md                     Contexto de marca + guía del proyecto. Fuente de
                                verdad que hereda todo agente. La escribe el
                                plugin (rica); el Studio solo seedea una mínima
                                si NO existe (nunca pisa).
  creatives/                    Scene graphs JSON (el formato del Studio).
                                Subcarpetas permitidas (campañas).
  assets/                       Content-addressed (sha256[0..8].ext) cuando los
                                escribe el Studio; los curados a mano conservan
                                nombre. Categorías:
    logos/                      Todos los logos del cliente.
    fonts/                      Tipografías (.ttf/.otf/.woff2).      [antes brand/typographies]
    brand-kit/                  Brand kit crudo + guidelines (PDF…) y
                                brand.md / brand-kit.md (narrativa + resumen).  [antes brand/]
    products/                   Imágenes de producto + index.md del catálogo.   [antes productos/]
    references/                 Referencias de estilo / competidores.
  briefs/                       Briefs y pedidos del cliente (.md, links Notion).
  exports/                      Renders finales (PNG/JPG). El Studio exporta acá. [antes entregables]
  versions/                     Snapshots durables por creative (los maneja el Studio).
  .indash/                      PRIVADO del Studio (comments.jsonl,
                                agent-session.json, render-requests). Ningún
                                agente lo toca; no se versiona en git.
```

## Quién escribe qué

| Artefacto | Writer | Notas |
|---|---|---|
| Estructura inicial + CLAUDE.md rico | **plugin `new-client`** | Trae productos/brand del MCP de Indash |
| `creatives/*.json` | Studio ↔ Claude (dos manos) | Serialización canónica 2-space+`\n` |
| `assets/*` | Studio (imports), plugin (onboarding), Claude (generación) | Content-addressed cuando aplica |
| `exports/`, `versions/` | Studio | |
| `.indash/*` | **SOLO el Studio** | Invisible al watcher; single-writer |
| `briefs/` | Humanos + plugin | |

## Migración desde las convenciones viejas

Renames mecánicos (los hace una skill de "upgrade" del plugin, NO el Studio):
`brand/typographies→assets/fonts` · `brand/logos→assets/logos` ·
`brand/assets + brand/brand*.md→assets/brand-kit` ·
`productos/referencias→assets/products` · `productos/index.md→assets/products/index.md` ·
`entregables→exports`. Los proyectos del Studio viejo ya cumplen la spec.

## Follow-ups

- [x] `new-client` y todas las skills leen/escriben los paths nuevos (0.4.0).
- [ ] Skill de upgrade para migrar carpetas de clientes existentes (renames
      mecánicos de la tabla de arriba).
- [ ] El Studio deja de scaffoldear el árbol completo en `/create` (queda
      `creatives/` lazy + CLAUDE.md mínimo) — va en el repo del Studio.
