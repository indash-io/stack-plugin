# 02 — Discovery

**Trabajo silencioso.** No narres lo que estás haciendo ("voy a revisar la
carpeta…", "ahora mido los clips…"). Hacelo y aparecé en Decisions con el
inventario listo.

Salís de acá con **dos cosas**: la tabla de material y el contexto de marca.
(El diagnóstico del entorno para el mode switcher ya lo hiciste en el paso 0.)

---

## 1. Inventario de material

### La carpeta del Workbench del creativo

En este orden, leyendo — no adivinando:

1. El manifiesto `creatives/<brief>/<grupo>/<id>/<id>.indash`: `canvas`
   (formato), `video.seconds` (duración objetivo), `video.active` (si ya hubo
   renders — una iteración, no un montaje de cero), `meta.status`.
2. `briefs/<brief>/plan.json` → las `notes` del creativo: qué cuenta, qué
   producto, si lleva packshot/placa, claims permitidos.
3. `workbench/<brief>/*/.folder.json` → la carpeta vinculada. Adentro:
   - `clips/clip-NN-vK.mp4` → los clips, en orden por NN. Si un NN tiene
     varias `-vK` y nadie dijo cuál, **marcalo para Decisions** (default: la
     más alta).
   - `scripts/clip-NN.md` → lo que dice cada clip (la fuente de los captions).
   - `stills/` → planos fijos útiles para inserts o para tapar un glitch.
   - Todo lo demás: música (`.mp3/.wav/.m4a`), b-roll, logos, referencias que
     el humano soltó. **Es el único audio que existe**: no hay TTS ni música
     generada en este proceso.
4. Si ya existe `composition/` (iteración): leé `PLAN.md` e `index.html` —
   el trabajo es un diff, no un montaje nuevo.

### Otras fuentes de material

| Dónde | Qué esperás encontrar |
|---|---|
| `library/products/<producto>/` | Fotos reales del producto para inserts y packshots (el `product.json` te dice qué es cada foto) |
| `creatives/<brief>/<grupo>/<otro-id>/layers/<capa>/<active>` | Un still/packshot ya aprobado de una imagen del brief (el `active` de la capa; `v3` pelado = `v3.png`) |
| `library/logos/` | El logo del cierre (SVG o PNG — en HyperFrames se usa el archivo tal cual) |
| `library/fonts/<Familia>/` | Las tipografías REALES de la marca (TTF) |
| `library/generated/` | Imágenes sueltas generadas antes |
| `.indash/chat-files/` | Adjuntos que el humano tiró al chat — solo lectura, copialos a `assets/` |

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
| 1 | `clips/clip-01-v2.mp4` | 10.0s | 1080×1920 | sí (voz) | "No, no, pará. ¿Viste esto?…" | Hook + desarrollo |
| 2 | `clips/clip-02-v1.mp4` | 10.0s | 1080×1920 | sí (voz) | "…y me llegó en dos días" + CTA | Desarrollo + CTA |
| 3 | `library/products/x/3c8c….webp` | — | 1600×2000 | — | Packshot frontal | Cierre |
| 4 | `musica.mp3` | 42.0s | — | sí | Cama que trajo el humano | Bajo la voz |

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
  `@font-face` apuntando al archivo copiado a `assets/`. Un "parecido" de
  Google Fonts es un error de marca, no un atajo.
- El logo del cierre: `library/logos/` (si hay variantes, la que el brand.md
  marque para fondos como el del cierre).
- Claims permitidos: `library/products/products.md` + las `notes` del plan +
  los guiones. **Nada on-screen que no salga de ahí.**

Si el proyecto no tiene marca cargada (brand.md con placeholders): la estética
sale del material que estás editando (paleta dominante de los clips, packaging
visible), nunca de prejuicios sobre la categoría — y lo decís en Decisions.

---

## 3. Qué NO hacés en Discovery

- ❌ No hablás con el humano todavía.
- ❌ No abrís el material clip por clip narrando lo que ves.
- ❌ No decidís el encuadre de un clip con resolución distinta: lo **marcás**
  para proponerlo.
- ❌ No elegís entre `-v2` y `-v3` de un clip por tu cuenta si nadie lo dijo:
  lo marcás y se decide en Decisions (o volvés a `video-clips` si ninguna sirve).
- ❌ No inventes qué muestra un clip si el guion no alcanza para inferirlo. Si
  no sabés, ponelo como *"sin identificar — decime qué es"* en la tabla.
- ❌ No escribís nada todavía: ni `composition/`, ni el manifiesto.

---

## Salida de este paso

- Tabla de material con duraciones reales medidas y versiones vigentes resueltas.
- Paleta, tipografía, tono y claims permitidos de la marca.
- Lista de mismatch de formato y versiones ambiguas a resolver.

→ Pasá a `instructions/03_decisions.md`.
