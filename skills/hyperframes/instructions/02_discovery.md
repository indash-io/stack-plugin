# 02 — Discovery

**Trabajo silencioso.** No narres lo que estás haciendo ("voy a revisar la
carpeta…", "ahora mido los clips…"). Hacelo y aparecé en Decisions con el
inventario listo.

Salís de acá con **tres cosas**: la tabla de material, el contexto de marca, y
el diagnóstico del entorno (para el mode switcher).

---

## 1. Inventario de material

### Dónde mirar, en este orden

| Carpeta | Qué esperás encontrar |
|---|---|
| `exports/videos/` | Clips de `all-videos` y `ugc-video-prompts`, frames 0, MP4 descargados |
| `<Cliente>/V<N>-<Producto>/` | Salida de `ugc-generator` (estructura propia por video, con `SCRIPTS.md`) |
| `exports/carruseles/` · `exports/stories/` · `exports/ads/` | Imágenes generadas, útiles como slides fijos o cierres |
| `assets/products/` | Fotos de producto para inserts y packshots |
| `assets/logos/` · `assets/fonts/` | Logo del cierre y la tipografía real de la marca |
| `briefs/` | Brief del período: ángulo, claims permitidos, CTA |

Leé también los `.md` de entregable que acompañan a cada set
(`2026-08-20_<slug>_v1.md`): ahí está el shot list original, el concepto y los
prompts. **Te dicen qué es cada clip sin que tengas que mirarlo.**

### Medí cada archivo — no adivines la duración

```bash
ffprobe -v error -show_entries format=duration \
  -show_entries stream=width,height,codec_type,codec_name \
  -of default=noprint_wrappers=1 <archivo>
```

Con eso armás la tabla. **Nunca escribas un `data-duration` mayor que la
duración real del clip**: HyperFrames congela el último frame y se lee como un
error.

### Tabla de material (la vas a mostrar en Decisions)

| # | Archivo | Dur. real | Resolución | Audio | Qué muestra | Uso propuesto |
|---|---|---|---|---|---|---|
| 1 | `assets/shot-01.mp4` | 6.0s | 1080×1920 | no | Producto girando sobre mármol | Hook (0–1.8s, recortado) |
| 2 | `assets/shot-02.mp4` | 8.0s | 1080×1920 | sí | Mano aplicando el producto | Desarrollo |
| 3 | `assets/packshot.png` | — | 1080×1350 | — | Packshot frontal | Cierre + CTA |

**Marcá los mismatch de resolución.** Un clip 1920×1080 dentro de una
composición 1080×1920 necesita decisión de encuadre (ver
`instructions/05_composition.md`, sección "Encuadre y `object-fit`"): o se
recorta con `object-fit: cover`, o se deja con barras, o se usa como fondo
desenfocado. Eso **se propone en Decisions**, no se decide en silencio.

---

## 2. Contexto de marca

- Leé el `CLAUDE.md` del cliente: paleta (hex), tipografía, tono, do's & don'ts,
  claims permitidos.
- Leé `assets/brand-kit/brand-kit.md` y `assets/brand-kit/brand.md` si existen.
- Listá las fuentes reales disponibles en `assets/fonts/`. **Usá esas**, con
  `@font-face` apuntando al archivo local. Un "parecido" de Google Fonts es un
  error de marca, no un atajo.
- Si el conector `indash` está disponible y falta algo (paleta, logo), traelo con
  `get_brand_kit`. Si no está, seguí con lo que hay en disco y decilo.

Si **no** hay carpeta de cliente: la estética sale del material que estás
editando (paleta dominante de los clips, tipografía visible en el packaging),
nunca de prejuicios sobre la categoría.

---

## 3. Diagnóstico del entorno (alimenta el mode switcher)

```bash
node --version          # necesita 22+
ffmpeg -version         # tiene que existir
npx hyperframes --version   # anotá la versión real; no asumas ninguna
```

Si los tres responden bien → `full_render`. Si falla Node o FFmpeg →
`plan_only`, y en Decisions le decís al user exactamente qué instalar:

> Node 22+ y FFmpeg son los dos requisitos de HyperFrames. Te dejo el proyecto y
> los comandos para que lo corras cuando los tengas.

En `full_render`, si el proyecto ya existe podés correr `npx hyperframes doctor`
para ver el estado real del entorno de render.

---

## 4. Qué NO hacés en Discovery

- ❌ No hablás con el user todavía.
- ❌ No abrís el material clip por clip narrando lo que ves.
- ❌ No decidís el encuadre de un clip con resolución distinta: lo **marcás**
  para proponerlo.
- ❌ No inventes qué muestra un clip si no lo podés inferir del `.md` del
  entregable o del nombre. Si no sabés, ponelo como *"sin identificar — decime
  qué es"* en la tabla de Decisions.

---

## Salida de este paso

- Tabla de material con duraciones reales medidas.
- Paleta, tipografía y tono del cliente.
- Modo (`full_render` / `plan_only`) resuelto.
- Lista de mismatch de formato a resolver.

→ Pasá a `instructions/03_decisions.md`.
