# Formato — UGC de dos clips + placa (21-23 s)

El formato que más se entrega con clips de avatar: **clip A (10 s) → clip B
(10 s) → placa final (2.6-3.2 s)**, con captions karaoke, inserts del
producto y sonidos encima de todo. Es tan fijo que **no se escribe el HTML a
mano**: hay un generador. Cambiar *cómo se ve* = tocar
`templates/ugc-2clips.html`; cambiar *qué aparece y cuándo* = tocar el spec.
El `index.html` generado nunca se edita: el próximo build lo pisa.

Todo lo de esta skill sigue valiendo (intake, discovery, decisions, gates,
render con la tool). Este archivo es solo el paso 5 (composición) para este
formato.

## Qué hay en `composition/` al terminar

```
composition/
  PLAN.md          el plan de edición (el spec explicado, más lo que quedó afuera)
  ugc.json         el spec: tiempos, paleta, overlays, placa
  t1.json  t2.json las transcripciones (array de words) de los clips A y B
  index.html       GENERADO por scripts/build-ugc.py
  assets/
    clip-01.mp4  clip-02.mp4   los clips, RE-ENCODEADOS (regla 17)
    gameplay.mp4 …             material del cliente, cortado a 720x1280 nativo
    logo.mp4                   el fondo de la placa (el logo real del cliente, loopeado)
    Marca-Bold.ttf             la fuente real, si la marca tiene
    sfx/…                      solo si el humano soltó efectos en el Workbench
```

## Paso a paso

1. **Assets.** Copiá los clips vigentes y el material del cliente a
   `assets/` y **re-encodeá todo** con keyframes densos (comando en
   `instructions/05_composition.md` §1). Verificá con `ffprobe` que los
   cortes del cliente quedaron en el tamaño nativo de la composición.
2. **Transcribí los dos clips** (regla 16):
   ```bash
   npx hyperframes@0.8.33 transcribe assets/clip-01.mp4 -e whisper -m large-v3 -l es --json
   # assets/transcript.json → t1.json (solo el array de words); repetir con clip-02 → t2.json
   ```
   Imprimí los tiempos por palabra (`05_composition.md` §7) y guardalos:
   con eso se anclan los inserts y se saca el `cut`.
3. **Escribí `ugc.json`** (abajo). `cut` = donde termina de hablar el A más
   0.2-0.4 s. Cada overlay se ancla a la palabra exacta. Los primeros 2 s
   van limpios.
4. **Build:**
   ```bash
   python3 ~/.claude/skills/video-composition/scripts/build-ugc.py creatives/<brief>/<grupo>/<id>/composition
   ```
   El script frena si falta un asset, si un `mstart + dur` pasa la duración
   real del archivo o si la placa no tiene runway; avisa si un insert cae en
   los primeros 2 s. Imprime las correcciones de ASR aplicadas: **decíselas
   al humano**.
5. **Gates y render**, como siempre: `lint` → `check --snapshots` (mirá los
   PNG: un insert caído en una transición o un recuadro tapando la cara pasan
   el check) → `render_video draft` → `view_creative` → OK del humano →
   `render_video high`.

## El spec (`ugc.json`)

```json
{
  "cid": "main",
  "title": "TCG Battle — Nico",
  "width": 720, "height": 1280,
  "total": 22.70,
  "cut": 9.45,
  "avatar_dur": 10.0,
  "av1": "assets/clip-01.mp4",
  "av2": "assets/clip-02.mp4",
  "palette": { "accent": "#F02FA6", "kw": "#6FE9FF", "dark": "#140A22", "dark2": "#1E0F35", "cream": "#F5EEFF" },
  "fonts": {
    "disp": { "family": "MarcaRounded", "file": "assets/Marca-Black.ttf", "weight": 800 },
    "body": { "family": "MarcaSans",    "file": "assets/Marca-Bold.ttf",  "weight": 700 }
  },
  "watermark": "TCG BATTLE",
  "keywords": ["plata", "cartas", "ranking"],
  "splits": { "Ypara": ["Y", "para"] },
  "fixes":  { "TSG": "TCG" },
  "overlays": [
    { "kind": "cutaway", "src": "assets/gameplay.mp4", "label": "⚔️ TCG Battle", "start": 4.60, "dur": 2.60, "mstart": 0.3 },
    { "kind": "pill",    "text": "sin gastar un peso", "start": 5.90, "dur": 1.60 },
    { "kind": "stamp",   "text": "IGUAL\nQUE TODOS", "start": 7.95, "dur": 1.40 },
    { "kind": "cutaway", "src": "assets/sobre.mp4", "label": "🎁 los sobres", "start": 16.10, "dur": 2.30, "mstart": 0.2, "zoom": false },
    { "kind": "card",    "src": "assets/app.mp4", "label": "⚡ la app", "start": 11.00, "dur": 2.30, "mstart": 0.2 }
  ],
  "outro": {
    "start": 19.70, "dur": 3.00,
    "top": "buscá", "url": "OLA TCG BATTLE", "cta": "jugá sin gastar un peso",
    "band": "assets/logo.mp4", "bandstart": 0.2
  },
  "sfx": { "cut": "assets/sfx/whoosh.mp3", "stamp": "assets/sfx/impact.mp3", "pill": "assets/sfx/pop.mp3", "close": "assets/sfx/close.mp3" }
}
```

| Campo | Qué es |
|---|---|
| `width` / `height` | 720×1280 (nativo de omni, nada se escala) o 1080×1920. El escenario está dibujado en 720×1280 y se escala entero; = `canvas` del manifiesto (regla 9 y su excepción UGC) |
| `total` | cuándo termina la placa. Pieza completa **21-23 s** |
| `cut` | segundo en que arranca el clip B: fin de la voz del A + 0.2-0.4 s, leído en `t1.json` |
| `speed1`, `av1_dur` | solo si el clip A quedó lento y se aceleró (último recurso: el arreglo correcto es escribir más palabras en `video-clips`) |
| `palette` | `accent` (pastillas, chips, borde, flash), `kw` (keyword en los captions), `dark`/`dark2` (fondo de la placa), `cream` (pastilla clara de la placa). De `library/brand/brand.md` |
| `fonts` | por rol (`disp`, `body`, `mono`): archivo en `assets/` → `@font-face` con `font-display: block`. Sin archivo, stack del sistema. **Nunca un `<link>` remoto** |
| `keywords` | las palabras que cargan el mensaje (2-3 por clip), en minúscula; se pintan con `kw` |
| `splits` / `fixes` | lo que Whisper pegó (`"Ypara"` → `["Y","para"]`) y lo que oyó mal (`"TSG"` → `"TCG"`). Se declaran |
| `overlays[]` | `start`/`dur` en segundos de la PIEZA; `mstart` desde qué segundo del asset; `zoom: false` **obligatorio si hay algo que leer**; `scrim: <y>` banda oscura de 200 px centrada en esa y, solo si el texto quemado del cliente no cae bajo el bloque de captions |
| `outro` | `top` (línea chica), `url` (pastilla clara: acá va la URL o el nombre), `cta` (línea de color; en guiones de plata el CTA vive acá), `band` (video de fondo: el logo real del cliente) + `bandstart`. Runway obligatorio |
| `sfx` | opcional, por evento (`cut`, `stamp`, `pill`, `close`). Solo archivos que el humano soltó en el Workbench: sin ellos la pieza sale sin efectos y lo decís |

### Tipos de overlay

| Tipo | Qué es | Cuándo |
|---|---|---|
| `cutaway` | material a **pantalla completa** | gameplay, arte, cualquier cosa del producto — **mismo ratio nativo** que la composición |
| `card` | recuadro 470×305 arriba a la derecha | material que NO es del mismo ratio |
| `cardtall` | recuadro retrato 340×453 | material vertical que no se puede recortar |
| `pill` | pastilla de color con texto | un dato, un beneficio (también para reponer un dato del material que quedó tapado) |
| `chip` | etiqueta chica arriba | rotular qué se está viendo |
| `stamp` | placa grande rotada, entra de golpe | el remate de una frase |
| `danger` | viñeta roja que late | tensión |

Inserts de 2.4-2.8 s; **el que carga el beneficio dura más**. Un insert que
cruza el `cut` disimula la costura entre clips.

## Lo que el generador hace solo

- Captions karaoke (`style/captions_typography.md` §10) desde `t1.json` +
  `t2.json`, agrupados de a 4 palabras cortando en puntuación fuerte, con las
  keywords en color y **fondo opaco en la banda de los subtítulos quemados**.
- Overlays con su animación de GSAP y su SFX (si hay archivos).
- Flash del color de acento en el `cut` y en la placa, con el **hard-kill en
  cada borde de clip dentro del fade** (subtítulos incluidos) que exige el
  lint (`reference/hyperframes.md` §1.9).
- Watermark, barra de progreso, avatar `muted` + audio aparte del mismo mp4.

## Lo que no hace (y es tuyo)

- Elegir el momento del insert: **mirá una hoja de contactos del asset** y
  elegí el `mstart` viendo, no adivinando. El check no ve un insert caído en
  una nube de humo.
- Decidir qué va a pantalla completa y qué en recuadro (regla del ratio,
  `05_composition.md` §4).
- El CTA escrito y la URL: salen del plan y de `brand.md`, no se inventan.
