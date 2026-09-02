# 02 — Discovery

**Trabajo silencioso.** No narres lo que estás haciendo ("voy a revisar la
carpeta…", "ahora mido los clips…"). Hacelo y aparecé en Decisions con el
inventario listo.

Salís de acá con **dos cosas**: la tabla de material y el contexto de marca.
(El diagnóstico del entorno para el mode switcher ya lo hiciste en el paso 0.)

---

## 1. Inventario de material

### Resolver los clips vigentes de un grupo video

En este orden, leyendo — no adivinando:

1. `briefs/<brief>/plan.json` → el grupo: `kind`, `seconds`, `format` y el
   **orden** de sus `creatives`. Ese orden ES el orden de concatenación.
2. Por cada clip, su manifiesto `creatives/<brief>/<grupo>/<id>/<id>.indash`:
   - `meta.video.render.version` → el MP4 vigente: `clips/<version>.mp4`.
   - `meta.video.render.fromStill` vs el `active` de la capa still → si no
     coinciden, el render está **desactualizado**: marcalo para Decisions.
   - `meta.video.script` → lo que dice ese clip (la fuente de los captions).
   - `meta.status` → un clip `approved` se puede leer tranquilo; uno en
     `changes` probablemente se re-renderice — marcalo.
3. Stills útiles como planos fijos: `layers/<layerId>/<active>.png` de los
   manifiestos (el cierre con packshot casi siempre sale de acá o de
   `library/products/`).

### Otras fuentes de material

| Dónde | Qué esperás encontrar |
|---|---|
| `library/products/<producto>/` | Fotos reales del producto para inserts y packshots (el `product.json` te dice qué es cada foto) |
| `library/logos/` | El logo del cierre (SVG o PNG — en HyperFrames se usa el archivo tal cual) |
| `library/fonts/<Familia>/` | Las tipografías REALES de la marca (TTF) |
| `library/generated/` | Imágenes sueltas generadas antes |
| `.indash/chat-files/` | Adjuntos que el humano tiró al chat (música, VO, clips externos) — solo lectura, copialos al proyecto |

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

| # | Archivo | Dur. real | Resolución | Audio | Qué muestra / dice | Uso propuesto |
|---|---|---|---|---|---|---|
| 1 | `…/clip-01/clips/v2.mp4` | 10.0s | 720×1280 | sí (voz) | "No, no, pará. ¿Viste esto?…" | Hook + desarrollo |
| 2 | `…/clip-02/clips/v1.mp4` | 10.0s | 720×1280 | sí (voz) | "…y me llegó en dos días" + CTA | Desarrollo + CTA |
| 3 | `library/products/x/3c8c….webp` | — | 1600×2000 | — | Packshot frontal | Cierre |

**Marcá los mismatch de resolución.** Un clip 720×1280 en una composición
1080×1920 escala 1.5× (aceptable para UGC — decilo); un clip horizontal en una
pieza vertical necesita decisión de encuadre (ver
`instructions/05_composition.md`, sección "Encuadre y `object-fit`"). Eso **se
propone en Decisions**, no se decide en silencio.

**El audio de los clips de avatar es la voz**: casi siempre es audio nativo que
se conserva (`data-has-audio="true"`) con música muy abajo. Anotalo en la tabla.

---

## 2. Contexto de marca

- Leé `library/brand/brand.md`: paleta (hex), tipografías, tono, do's & don'ts.
- Listá las fuentes reales disponibles en `library/fonts/`. **Usá esas**, con
  `@font-face` apuntando al archivo copiado al proyecto. Un "parecido" de
  Google Fonts es un error de marca, no un atajo.
- El logo del cierre: `library/logos/` (si hay variantes, la que el brand.md
  marque para fondos como el del cierre).
- Claims permitidos: `library/products/products.md` + las `notes` del plan.
  **Nada on-screen que no salga de ahí o de los guiones.**

Si el proyecto no tiene marca cargada (brand.md con placeholders): la estética
sale del material que estás editando (paleta dominante de los clips, packaging
visible), nunca de prejuicios sobre la categoría — y lo decís en Decisions.

---

## 3. Qué NO hacés en Discovery

- ❌ No hablás con el humano todavía.
- ❌ No abrís el material clip por clip narrando lo que ves.
- ❌ No decidís el encuadre de un clip con resolución distinta: lo **marcás**
  para proponerlo.
- ❌ No "arreglás" un render desactualizado re-renderizando por tu cuenta: lo
  marcás y se decide en Decisions (re-render = `video-execution`).
- ❌ No inventes qué muestra un clip si el guion no alcanza para inferirlo. Si
  no sabés, ponelo como *"sin identificar — decime qué es"* en la tabla.

---

## Salida de este paso

- Tabla de material con duraciones reales medidas y clips vigentes resueltos.
- Paleta, tipografía, tono y claims permitidos de la marca.
- Lista de mismatch de formato y renders desactualizados a resolver.

→ Pasá a `instructions/03_decisions.md`.
