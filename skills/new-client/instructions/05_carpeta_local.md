# 05 — La carpeta local (opcional)

La carpeta del cliente es lo que las skills de ejecución heredan cuando producen desde Claude Code: `CLAUDE.md` de contexto, assets de marca, índice de productos, `exports/`. Es **opcional y va al final**, porque el onboarding ya quedó en Indash y `content-brief` no la necesita.

**La fuente es Indash. Nunca al revés.** El `CLAUDE.md` se escribe desde lo que el cliente cargó (`get_brand_context`), su brand kit (`get_brand_kit`) y su catálogo (`list_products`). No se analiza el sitio, no se infiere una paleta de una captura, no se describe el tono. Lo que el onboarding no tiene queda como placeholder. Y el `CLAUDE.md` nunca vuelve a Indash como fuente de un campo: lo escribió una máquina.

---

## 1. Preguntar, una vez

Solo si tenés filesystem (Claude Code, Cowork). En claude.ai no hay carpeta: salteá el paso sin mencionarlo.

> ¿Armamos también la carpeta local para producir desde acá (carruseles, stories, ads, video)? Queda con el contexto de la marca tal como está en Indash.

"No" o "después" → `06_handoff.md`. No insistas ni la crees "por las dudas".

---

## 2. Slug y carpeta

Derivá el slug del nombre en kebab-case (minúsculas, sin acentos, espacios → guiones): "Acme Foods" → `acme-foods`, "Café del Sur" → `cafe-del-sur`. Se crea en el directorio de trabajo actual.

Si `{slug}/` ya existe, frená y preguntá:

> Ya hay una carpeta `{slug}`. ¿La actualizo (completo lo que falte sin pisar lo existente) o creamos otra con otro nombre?

Nunca pises un archivo existente sin avisar. Un `CLAUDE.md` que ya está se actualiza sección por sección, no se reescribe entero.

---

## 3. La estructura

Creá todo lo de `templates/folder_structure.md` de una, con `.gitkeep` en las carpetas que arrancan vacías, y mostrá el árbol al final. Ni de más ni de menos: `brand/`, `versions/` y `.indash/` no se crean.

---

## 4. De dónde sale cada cosa

Antes de escribir, tres llamadas: `get_brand_context` (sin metodología; trae el contexto del onboarding, lo confirmado del análisis y el índice de material con URLs firmadas), `get_brand_kit` y `list_products`. Ya tenés `state` de `get_brand_onboarding`. Con eso se llena todo; no hay otra fuente.

| En el `CLAUDE.md` | Sale de | Si no está |
|---|---|---|
| Nombre, workspace, URL del onboarding | `workspace` y `onboarding.url` de `get_brand_onboarding` | Siempre está |
| Qué vende | `state.store.site` + los nombres de `list_products` | `PENDIENTE: sin tienda ni productos en Indash` |
| Mecanismo(s) | El contexto de `get_brand_context`, literal, con el producto al que apunta (`state.lists.mechanisms` tiene los ids y el `product_id`) | `PENDIENTE: cargar el mecanismo en el onboarding` |
| Voz | El perfil de voz **confirmado** que trae `get_brand_context`, más el texto de `voice.written_text` (entero en el contexto; `state.texts` lo recorta a 600 caracteres) | `PENDIENTE: análisis de voz sin confirmar` o `sin material escrito` |
| Qué evitar | `rules.forbidden_claims` literal (del contexto) + cuántas piezas hay en "esto no somos" (`state.lists.corpus_off_brand`) | `ninguno cargado` |
| Paleta, tipografía, logos | `get_brand_kit`; si está vacío, el sistema visual **confirmado** del análisis | `PENDIENTE: brand kit vacío en Indash` |
| Qué puede tocar la IA | `state.asset_freedom`, los seis flags | `PENDIENTE: sin responder en el onboarding` |
| Links | `state.store.site`, `assets.drive_url` y `brand.instagram` (en `state.texts`), `state.lists.links` | Se omite la línea |
| Catálogo | `list_products` → `assets/products/index.md` | `PENDIENTE: catálogo vacío` |
| Objetivo | `goals.objective` literal, del contexto | `PENDIENTE` |

Lo que está en Indash se copia literal (un mecanismo, un claim prohibido) o se referencia (el archivo, la lista). Lo que no está es un placeholder que dice qué falta y dónde se carga: en el onboarding, con esta skill o en la app. Nunca "completar a mano acá".

Lo que **no** entra al `CLAUDE.md`: las reseñas y las objeciones crudas (viven en Indash y las lee `content-brief`), y nada del análisis que siga `pending` o `rejected`.

---

## 5. Los archivos

- **Logos y tipografías**: los que devuelve `get_brand_kit`, bajados a `assets/logos/` y `assets/fonts/`. Nombre original.
- **Brand book y guidelines**: los archivos de `identity` del onboarding, por su URL firmada del índice de material de `get_brand_context` (vencen en unas dos horas; si venció, pedí el índice de nuevo), a `assets/brand-kit/`.
- **Fotos de producto**: no se bajan en el onboarding. El índice apunta a la URL de cada producto e imagen en Indash; las skills de ejecución las bajan cuando producen.
- **Piezas del corpus, ganadoras, capturas de objeciones**: no se bajan. Quedan en Indash con su veredicto y las abre `content-brief` cuando arma el brief.

Si la persona te pasa archivos a mano que no están en Indash, primero van al onboarding (`03_carga_masiva.md`), después a la carpeta. El disco no es un lugar donde vive material que Indash no tiene.

---

## 6. Los archivos que escribís

- **`CLAUDE.md`** → `templates/client_claude_md.md`. El operativo: manda sobre los defaults de las skills.
- **`assets/brand-kit/brand.md`** → `templates/brand_md.md`. Lo que sabe el cliente de su marca, en sus palabras.
- **`assets/brand-kit/brand-kit.md`** → paleta con hex, tipografías con su rol, reglas del logo, qué puede tocar la IA. Mismo origen que la sección Brand kit del `CLAUDE.md`, con más detalle.
- **`assets/products/index.md`** → `templates/product_index.md`.

Los cuatro salen de las mismas tres llamadas: no se contradicen entre sí y no dicen nada que Indash no diga. Rioplatense, conciso: los lee otro agente.

Con la carpeta armada → `eval/quality_checklist.md` y después `06_handoff.md`.
