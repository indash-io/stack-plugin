# BriefDoc → `plan.json` — el brief que baja del hub (indash.ai)

Cuando Indash Studio crea una sesión con un **brief pendiente de indash.ai**,
la app deja el material completo en `briefs/<brief>/source/` ANTES de mandar
`/new-brief` al chat por su cuenta:

```
briefs/<brief>/source/
  brief.json      ← la respuesta del endpoint de detalle, tal cual (la fuente citable)
  brief.md        ← el mismo brief en versión legible (para leerlo de corrido)
  <adjuntos>      ← los archivos de una submission, ya bajados (el `path` de `files[]`)
```

**Si `source/brief.json` existe, el insight ya está: no se le pide nada al
humano.** Este archivo es el contrato: qué trae `brief.json`, y cómo se
vuelca a `plan.json` + `notes` sin re-decidir lo que el hub ya decidió.

## Shape de `brief.json`

| Campo | Qué es |
|---|---|
| `source` | `draft` (armado con el armador guiado del hub y aprobado por un admin) o `submission` ("ya tengo el brief": archivos que subió el cliente) |
| `title` | Título del brief |
| `cadence` | `quincenal` \| `mensual` \| `null` (solo draft) |
| `period` | Período que cubre (solo draft) |
| `pieces` | Conteo por tipo `{ video, estatico, carrusel, historia }` (solo draft) |
| `note` | Nota del cliente (submission; `""` en draft) |
| `files[]` | `{ file_id, name, mime, bytes, path }` — **`path` es la ruta local relativa a `source/`, no hay `url`**: la app ya los bajó |
| `doc` | El `BriefDoc` completo (draft) o `null` (submission) |

### Los dos caminos

- **`source: "draft"`** → `doc` trae el `BriefDoc` y el mapeo de abajo es
  **mecánico, no creativo**: cero preguntas.
- **`source: "submission"`** → `doc` es `null`; el brief SON los archivos de
  `files[]` (PDF, Word, imágenes) más `note`. Abrilos con Read desde
  `source/<path>` y de ahí en más es el camino de siempre: si vienen como
  bloques por pieza, `reference/bloque-por-pieza.md`; si no, el plan lo
  proponés vos con las decisiones escritas en `notes`. Lo único que cambia
  respecto de un brief pegado en el chat es que **no lo pedís**: ya está.

## El `BriefDoc`

```
doc: { cadence, period, diagnosis, messages[], pieces[], ficha, rules[], validations[], ready }
```

| Campo | Para qué lo usás |
|---|---|
| `diagnosis` | El porqué del período. Es el contexto de las decisiones que el doc NO toma (componer/generar, producto, vista) |
| `messages[]` | Los mensajes del período; cada pieza apunta a uno por `messageId`. El texto del mensaje va a `notes` de la pieza («Mensaje: …») |
| `pieces[]` | Las piezas — lo que se vuelca a `plan.json` |
| `ficha` | Ficha de marca/producto del hub. Contrastala con `library/brand/brand.md` y `library/products/products.md`: si difieren, gana `library/` y lo anotás |
| `rules[]` | Restricciones (claims prohibidos, no-negociables). Van a `notes` de **toda** pieza a la que apliquen, textuales |
| `validations[]`, `ready` | Estado del armador; `ready` debería venir `true`. No van al plan |

Toda pieza trae `{ id, messageId, n, status, note, production, type }` más los
campos de su tipo (`type` ∈ `video` \| `estatico` \| `carrusel` \| `historia`):

- `id` → id del creativo (o del grupo, en carrusel/historia). Si no es
  kebab-case sin acentos, normalizalo y anotá el original en `notes`.
- `n` → orden dentro del período: respetalo en el orden de `creatives[]`.
- `status` → solo entran al plan las piezas vigentes; si una viene descartada
  no la scaffoldeás y lo decís en el resumen.
- `note` y `production` → a `notes`, textuales (indicaciones del cliente y de
  producción que la ejecución no puede adivinar).

## Mapeo por tipo

Los grupos por formato se llaman igual en todos los briefs del hub:

| Ratio | Grupo | `format` |
|---|---|---|
| `4:5` | `g-feed` | 1080×1350 |
| `1:1` | `g-square` | 1080×1080 |
| `9:16` | `g-story` | 1080×1920 |

Un carrusel y una historia son **su propio grupo** (la secuencia es la
unidad, como en `reference/bloque-por-pieza.md`); estáticos y videos van al
grupo compartido de su ratio.

### `estatico` → un creativo en el grupo de su `ratio`

`{ title, kind, copy, adBase, changes, ratio }`

| Del BriefDoc | Al disco |
|---|---|
| `ratio` | grupo (`g-feed` / `g-square` / `g-story`, tabla de arriba) |
| `id`, `title` | `creatives[].id` / `.title` |
| `copy` | **literal**, como capas `text` del manifiesto scaffoldeado — jamás al modelo de imagen |
| `kind` | arquetipo → `notes` («Arquetipo: …») |
| `adBase` + `changes` | `notes`: sobre qué anuncio se apoya y qué cambia respecto de él |

### `carrusel` → un grupo 4:5, un creativo por slide

`{ title, kind, why, slides[{ text, role, accent }], visual, continuity, caption }`

| Del BriefDoc | Al disco |
|---|---|
| la pieza | grupo `{ "id": "<pieza>", "format": 1080×1350 }` |
| `slides[N]` | creativo `<pieza>-s<N>` (`-s1`, `-s2`… en orden), título «<title> · slide N» |
| `slides[N].text` | capas `text` del slide, literal |
| `slides[N].role` + `.accent` | `notes` del slide («Rol: hook · Acento: …») |
| `visual` + `continuity` | `notes` de **todos** los slides (qué se ve, y qué se mantiene igual de slide a slide) |
| `kind`, `why` | `notes` del s1 (arquetipo y razón de la pieza) |
| `caption` | **no se renderiza**: queda en `source/brief.md` para quien publica; referencialo en `notes` del s1 |

### `historia` → un grupo 9:16, un creativo por frame

`{ title, kind, why, frames[{ text, role, link }], visual }`

| Del BriefDoc | Al disco |
|---|---|
| la pieza | grupo `{ "id": "<pieza>", "format": 1080×1920 }` |
| `frames[N]` | creativo `<pieza>-f<N>` (`-f1`, `-f2`…), título «<title> · frame N» |
| `frames[N].text` | capas `text` del frame, literal |
| `frames[N].role` + `.link` | `notes` del frame; `link` es el sticker de link, **instrucción de publicación, no de render** |
| `visual` | `notes` de todos los frames |
| `kind`, `why` | `notes` del f1 |

### `video` → UN creativo `kind: video` en el grupo 9:16

`{ hook, body, cta, cast, angle }`

| Del BriefDoc | Al disco |
|---|---|
| la pieza | creativo en `g-story` con `"kind": "video"` y `"seconds"` |
| `id` | `creatives[].id`; el `title` lo escribís vos, corto y legible (es el nombre de la carpeta del Workbench: «UGC creatina — confesión»), porque el video del hub no trae título |
| `seconds` | **20 por defecto** — el BriefDoc no trae duración. Si hook + body + cta lo sugieren, ajustá: a ~32 palabras por clip de 10s (regla de `video-clips`), `seconds ≈ ceil(palabras / 32) × 10`, mínimo 10. Escribí en `notes` por qué elegiste esa duración |
| `hook`, `body`, `cta`, `cast`, `angle` | `notes`, **textuales y completos** («Hook: … · Body: … · CTA: … · Cast: … · Ángulo: …»): son la materia prima de los guiones que escribe `video-clips` |
| — | `notes` además: cuántos clips (`ceil(seconds / 10)`), qué producto, si lleva packshot o logo al cierre, y que la música la trae el humano |

Un video es un formato: si además hace falta el 1:1, es otro creativo en
`g-square`, y lo decidís vos (no lo trae el doc).

## Lo que el BriefDoc NO decide — lo decidís vos, y queda escrito

El hub decide QUÉ se dice y en qué formato. Lo que sigue lo decidís en este
paso, con `diagnosis`, `ficha`, `messages[]` y `library/` en la mano, y
**queda escrito en `notes`** para que nadie lo adivine al producir:

- **¿Componer o generar?** — misma regla del paso 3: solo texto/logo/color →
  se COMPONE; producto o escena → se GENERA.
- **`product_id` y vista** — cuál de `library/products/` y qué vista pide la
  pieza (frente / perfil / detalle / en-uso / packshot), o «lifestyle sin
  producto», declarado.
- **Título del video** y su `seconds` (arriba).
- **Formato extra** de un video (1:1) si el período lo pide.

## `plan.json`

`plan.json.source` apunta al brief crudo: `"source": ["source/brief.json"]`.

```json
{
  "source": ["source/brief.json"],
  "groups": [
    { "id": "g-feed", "format": { "width": 1080, "height": 1350 }, "creatives": [
      { "id": "ad-oferta-01", "title": "Oferta creatina",
        "notes": "Mensaje: … · Arquetipo: oferta · GENERAR · producto: creatina-300 (packshot) · Base: ad-01, cambia el precio · Reglas: sin 'el mejor'" }
    ]},
    { "id": "carr-rutina", "format": { "width": 1080, "height": 1350 }, "creatives": [
      { "id": "carr-rutina-s1", "title": "Rutina · slide 1", "notes": "Rol: hook · Acento: 'sin excusas' · Visual: … · Continuidad: … · COMPONER" },
      { "id": "carr-rutina-s2", "title": "Rutina · slide 2", "notes": "Rol: desarrollo · …" }
    ]},
    { "id": "g-story", "format": { "width": 1080, "height": 1920 }, "creatives": [
      { "id": "ugc-creatina-01", "title": "UGC creatina — confesión", "kind": "video", "seconds": 20,
        "notes": "Hook: … · Body: … · CTA: … · Cast: mujer 25-30, a cámara · Ángulo: confesión de compra · 2 clips + packshot al cierre · producto: creatina-300 · música del humano · 20s por defecto (≈60 palabras)" }
    ]}
  ]
}
```

Después del scaffold, con un brief del hub **no frenás**: seguís de corrido
con `creative-execution` (v1 de cada imagen, 1K, un candidato) y `video-clips`
(guiones y stills de cada video) hasta los stills — ahí parás. Está escrito en
el paso 5 de la skill.
