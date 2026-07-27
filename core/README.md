# core/ — el canon compartido del stack

**Fuente ÚNICA de verdad** para el conocimiento que comparten todos los
runtimes de Indash: las leyes de prompting y las reglas de formato por pieza.
Antes vivían duplicadas acá y en `apps/web/lib/data/default-skills/` de
mkt-agents, divergiendo en silencio — decisión F4 del plan de
profesionalización (2026-07-27): **el plugin es el dueño; todo lo demás
deriva de acá.**

```
core/skills/
  prompt-craft/            Las 7 leyes del prompting cinematográfico,
                           EDIT vs GENERATE, refs por modelo, anti-patrones.
  ig-carousel/             Formato carrusel 4:5 (narrativa cross-slide).
  ig-story/                Formato story 9:16 suelta.
  ig-stories-secuencia/    Formato secuencia de stories.
  ig-post/                 Formato post cuadrado.
```

## Quién consume esto

1. **Las skills de este plugin** (carruseles, stories, ads…): sus
   `instructions/05_prompt_engineering.md` son la *aplicación* de estas leyes
   a su workflow. Ante un conflicto de fondo, **core gana** — actualizá la
   aplicación, no el canon.
2. **El agente interno de la web app** (mkt-agents): las
   `default-skills` que se instalan a los workspaces son **copias generadas**
   de `core/skills/`. Se regeneran con
   `bun run scripts/sync-default-skills.ts <path-a-este-repo>` en mkt-agents.

## Regla de release (no negociable)

Si tocás algo bajo `core/skills/`:

1. Revisá si las aplicaciones en `skills/*/instructions/05_*` necesitan
   reflejar el cambio.
2. Corré el sync en mkt-agents y mandá esa PR junto con (o inmediatamente
   después de) la release del plugin.
3. Entrada en `CHANGELOG.md`.
