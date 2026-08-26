---
name: edicion-ugc
description: Monta clips de avatar/UGC generados con IA en la pieza publicada, con un pipeline determinístico medido contra 21 ediciones manuales reales — recorta silencios muertos, detecta y tapa morphs con B-roll, quema subtítulos en Montserrat y pega la placa final de la marca. Corre local con FFmpeg + whisper-cpp; no usa el conector ni consume créditos. Disparala cuando pidan "editá estos clips de UGC", "montá estos clips", "revisá si hay morph", "sacale los silencios a este video" o cuando haya que armar la pieza final a partir de clips de avatar recién generados. No la uses para edición creativa libre, para material filmado con cámara real ni para composiciones con transiciones y texto animado — eso es `hyperframes`.
language: es
owner: manuel-soria
status: published
reviewed: 2026-08-26
---

# Edición de UGC generado con IA

Convierte clips crudos de avatar en una pieza publicada. Todo lo que hace sale
de medir **21 ediciones manuales reales** (marca A n=10, marca B n=11), no de
criterio inventado, y se validó después en **4 marcas**.

Es un pipeline **determinístico**: mismo material y mismo config → mismo MP4.
No hay decisión estética por sesión.

## Lo que hace falta tener instalado (decilo antes de arrancar)

Esta skill **corre local** y necesita cosas que no vienen con el plugin:

| | Qué | Cómo |
|---|---|---|
| Sistema | **macOS** | El setup usa Homebrew y las fuentes de `~/Library/Fonts`. En Linux/Windows hay que instalar todo a mano — no está probado. |
| | **Homebrew** | https://brew.sh |
| Binarios | **ffmpeg** y **whisper-cpp** | `brew install ffmpeg whisper-cpp` |
| Modelo | **ggml-large-v3-turbo** (~1.5 GB) | lo baja el setup a `~/.cache/whisper-cpp/` |
| Fuente | **Montserrat** | `brew install --cask font-montserrat` |
| Python | un venv con **Pillow** en `~/.indash/edicion-ugc/venv` | lo crea el setup |

El `setup.sh` hace todo eso y es **idempotente**: la primera vez tarda unos
minutos (el modelo pesa), las siguientes no hace nada.

**Nada de esto pasa por el conector `indash`**: no hay generación, no se consume
crédito. El venv y el modelo viven **fuera** de la carpeta del plugin a propósito
— esa carpeta es una cache que se pisa entera en cada `marketplace update`.

## Gate del conector `indash` — condicional

Esta skill **edita material que ya existe en disco**, así que el conector **no
es requerido**. Chequealo así:

- Si todo el material (clips, placa) ya está en disco → **avanzá**, y decilo en
  una línea: *"Voy sin `indash`: edito los clips que ya están en disco."*
- Si hace falta **generar un B-roll** (hay morph sobre voz y no hay clip de
  producto) → ahí sí necesitás `indash`. Si no está conectado, **frená** y
  pedile al user que lo conecte (`/mcp` en Claude Code, panel de conectores en
  Cowork), explicando por qué. **No dispares el OAuth por tu cuenta.**
- El clip de producto lo genera `all-videos` o `ugc-generator`. Derivá, y volvé
  con el archivo.

## Antes de nada: verificar el entorno

```bash
SK="${CLAUDE_PLUGIN_ROOT}/skills/edicion-ugc/scripts"
PY=~/.indash/edicion-ugc/venv/bin/python

ls "$PY" >/dev/null 2>&1 || bash "$SK/setup.sh"
```

> Si `${CLAUDE_PLUGIN_ROOT}` no está definida (pasa fuera de Claude Code),
> reemplazala por la ruta real del plugin — típicamente
> `~/.claude/plugins/cache/indash-stack` si se instaló desde el marketplace, o
> la carpeta del repo si se está corriendo con `claude --plugin-dir`.

**Siempre invocá el script con el python del venv**, nunca con el `python3` del
sistema (no tiene Pillow):

```bash
S="$SK/editar.py"
```

Si falta algo, `editar.py` **frena con la lista de lo que falta y te manda a
`setup.sh`** — no tira un traceback.

## Flujo

### Paso 1 — Revisar (siempre, antes de montar)

```bash
$PY $S revisar "/ruta/a/la/carpeta/de/crudos"
```

Mide y reporta. No renderiza nada. Devuelve por clip: duración, silencio de
cabeza, pausas a comprimir, y **morphs con timestamp**.

Leer el reporte y actuar:

| Lo que dice | Qué hacer |
|---|---|
| `sin morphs sobre voz` | montar directo |
| `MORPH SOBRE VOZ [8.4]` | **generar un clip de producto** y pasarlo como `broll` |
| `MORPH DE CABEZA` + *"el silencio ya lo tapa"* | nada, se resuelve solo |
| `MORPH DE CABEZA` + *"ATENCION: el silencio es MAS CORTO"* | nada, el paso 2 ajusta el corte |
| `taparlo se comeria Xs de voz` | **avisar al humano**, salió con un problema |

### Paso 2 — Montar

Escribir un config JSON en la carpeta del trabajo. Lo mínimo es esto:

```json
{
  "clips": ["parte1.mp4", "parte2.mp4"],
  "slug": "crema-noche"
}
```

```bash
$PY $S montar /ruta/config.json
```

Campos: `clips` (en orden) es el único obligatorio. Opcionales: `slug`
(identificador de la pieza para el nombre del archivo), `salida` (ruta explícita
— sin esto se aplica la convención del stack, ver abajo), `broll` (clip de
producto para tapar un morph sobre voz), `broll_dur` (default 4.5), `producto`
(palabras que marcan la mención del producto; si no se pasa usa los valores de
`marcas_whisper`), `placa` (ruta explícita), `marcas_whisper` (correcciones de
nombres propios; se aplican **por frase**, así que sirven para arreglar nombres
que Whisper parte en dos), `subtitulos: false`, `idioma` (default `es`),
`config_marca` (ruta explícita al config de marca).

El formato completo, campo por campo, está en `templates/config.example.json`.

### Dónde queda el archivo

Si no pasás `salida`, se aplica la **convención del stack**:
`exports/videos/<AAAA-MM-DD>_<slug>_v<N>.mp4` de la carpeta del cliente (la
primera carpeta hacia arriba con `exports/` o un `CLAUDE.md` de marca). **Nunca
pisa**: si el nombre existe, sube la versión. Decile al user la ruta al entregar.

### Config y placa por cliente

Una marca nueva **no necesita configurar nada**: alcanza con dejar la placa en
`brand/placa.png` de la carpeta del cliente (o en una subcarpeta `Placa/` al
lado de los crudos) y montar.

Si la marca se vuelve recurrente — sobre todo si Whisper le escribe mal el
nombre — conviene crearle un `brand/edicion-ugc.json` en su carpeta:

```json
{
  "marca": "Marca Ejemplo",
  "placa": "placa.png",
  "marcas_whisper": { "marca lynda": "Marcalinda" },
  "nota": "ampliar marcas_whisper cuando salga una variante nueva"
}
```

El formato completo está en `templates/brand-edicion-ugc.example.json`. Se busca
en `brand/` y en `assets/brand-kit/` de la carpeta de los crudos, de su carpeta
padre, de la carpeta del cliente y del cwd. **Ese archivo vive en la carpeta del
cliente, nunca en el plugin** — el plugin es público.

### La placa

**Convención: la placa se entrega ya armada, a pantalla completa (720×1280).**
Puede ser imagen fija o video. La skill la usa **tal cual** — no compone, no
recolorea, no interpreta nada.

> Antes componía un logo suelto sobre un fondo del color muestreado de la imagen.
> Funcionaba, pero obligaba a deducir el color, y deducir deja residuo: contra la
> edición manual quedaba a ~12 unidades de distancia por la conversión de espacio de
> color (los logos de Mac vienen en Display P3). Con la placa ya armada el color es
> exacto — medido: 1 unidad de diferencia, que es redondeo del encoder.

Se detecta en este orden:

1. `placa` del config del trabajo
2. `placa` del `brand/edicion-ugc.json` de la marca
3. `brand/placa.*` (o `assets/logos/placa.*`) de la carpeta del cliente
4. Único archivo en una subcarpeta `Placa/` o `Logos/` (busca también un nivel
   arriba: los clips suelen vivir en `<cliente>/Crudo/` y la placa en
   `<cliente>/Placa/`)
5. Archivo cuyo nombre contenga `placa`, `outro`, `cierre` o `endcard` — así se
   puede reconocer una placa en video sin confundirla con los clips de diálogo
6. La única imagen suelta de la carpeta

Ante **cualquier ambigüedad avisa y no elige**: quien usa la skill puede no darse
cuenta de que agarró la imagen equivocada. Si la placa no es 9:16, avisa que la va a
recortar.

## Qué hace, paso por paso

0. **Mide** cada clip y reporta morphs.
1. **Entra a cada clip 3 frames antes de que arranque la voz.** Los clips se generan
   desde el mismo still, así que todos abren en la misma pose; si se concatenan
   enteros esa pose se repite en el empalme y se nota. Entrando pegado a la voz, el
   clip ya está en movimiento cuando se corta. Si hay morph de cabeza, la entrada
   nunca cae antes de que termine.
2. **Recorta silencios.** Cabeza y cola **siempre**, sin importar el largo. Pausas
   internas solo si pasan 0.50s con 15% de margen, y se comprimen a 0.45s.
3. **Re-chequea morph de cabeza sobre el resultado.** Si el recorte de silencio cortó
   en medio de un morph, corre el corte hasta pasarlo. Si eso se comería más de 0.15s
   de voz, no lo hace y avisa.
4. **Transcribe** (Whisper). Va antes del B-roll porque sin el texto no se puede saber
   cuándo se menciona el producto.
5. **B-roll** — solo si hay archivo. **Un solo bloque**, armado con todos los clips
   que se pasen, pegados uno detrás del otro.
   - **Posición: el bloque termina al 72% del diálogo.** Es lo único que se sostiene
     en las 4 ediciones manuales con B-roll (70–75% en las cuatro). El inicio se
     deriva del final y del largo, porque el inicio varía mucho (25–47%).
   - **Largo: 40% del diálogo**, entre 2.5s y 6.5s.
   - **Corrección**: si hay un morph fuerte y cae *fuera* del bloque, el bloque se
     corre para taparlo. Si cae adentro, no se mueve nada.

   > La mención del producto **no** sirve como ancla, aunque lo parezca. En una de
   > las ediciones medidas la persona nombra el producto y sigue en cámara — el
   > B-roll entra después, sobre los beneficios. Se reporta como referencia y nada
   > más.

   De cada clip usa **el tramo más estable**, no el clip entero: los B-roll también se
   generan con IA y traen defectos, casi siempre al arranque o al final.

   **Los bordes se alinean con los cortes que ya existen.** Si un corte de aire muerto
   cae a menos de 0.6s del borde del B-roll, el borde se pega a ese corte. Si no,
   quedan dos cortes separados por unos frames y el video trastabilla: se ve un corte,
   3 frames de diálogo, y otro corte al B-roll. Los cortes que caen *adentro* del
   bloque no molestan — los tapa.
6. **Subtítulos**: frases de 2-4 palabras → Montserrat SemiBold 32, blanco,
   contorno suave, centrado, y=1027.
7. **Placa final**, según el tipo:
   - **Video** → va **entero**, con su propia duración. Truncar un outro animado lo
     cortaría a la mitad.
   - **Imagen fija** → **1.50s**.
8. **Export**: 720×1280, 24fps, ~6 Mbps, a `exports/videos/` con el nombre canónico.

## De dónde salen los números

| Regla | Valor | Evidencia |
|---|---|---|
| Duración de placa fija | **1.50s** | medido daba 1.25–1.34 en 21/21 (la constante más fuerte del corpus); el equipo la subió a 1.50 (ago 2026) |
| Duración de placa en video | la del archivo | va entera |
| Techo de pausa | **0.50s** | medido daba 0.76 (techo de 21); el equipo lo bajó a 0.50 para un ritmo más dinámico (ago 2026) |
| Silencio de cabeza | siempre se elimina | 17/21 en 0.00 |
| Subtítulo: agrupación | 2 a 4 palabras | 24/24 muestras, ambas marcas |
| Subtítulo: posición | centrado, y=1027 | idéntico entre marcas |
| Subtítulo: tamaño | Montserrat SemiBold 32 | calibrado por ancho de string real |
| Export | 720×1280, 24fps, ~6 Mbps | 5447–6404 medidos |
| B-roll: dónde termina | **72% del diálogo** | 70.4 / 75.3 / 69.8 / 73.2% en las 4 ediciones con B-roll — el ancla más firme |
| B-roll: largo | 40% del diálogo | medido 26 / 37.5 / 40.5 / 45.4% — más disperso, se pisa con `broll_dur` |
| Dónde entra el B-roll | morph > mención de producto > peor momento | en una edición el bloque manual arranca en 2.50s y la frase que nombra al producto en 2.39s |

**Lo que deliberadamente NO se automatiza**: la cantidad de cortes internos (17 de 21
ediciones no tienen ninguno — lo dicta el material) y la duración total (8.4s a 20.3s).

**Cuidado con confundir coincidencia con regla.** Los números de la tabla no valen todos
lo mismo: la placa sale de 21 casos, el largo del bloque de B-roll de 2. Cuando la
evidencia es finita el valor va como sugerencia ajustable y el log lo dice, para que
nadie lo tome por ley.

## Límites — decirlos, no taparlos

- **El detector de morph es ciego a las derivas graduales.** Solo ve saltos secos.
  Cuando reporta `morph 0.000` significa *"sin saltos secos"*, **no** *"clip limpio"*.
  Si un clip vuelve despacio a la pose del frame de referencia, pasa derecho.
- **Un pico de score no siempre es un morph.** Un gesto rápido o un cambio de luz dan
  la misma señal. Por eso el B-roll lo dispara *la presencia del archivo*, nunca el
  detector solo.
- **Whisper escribe mal los nombres de marca.** Para eso está `marcas_whisper` en el
  `brand/edicion-ugc.json` del cliente; ampliarlo cuando aparezca un error nuevo.
- **Nadie escucha el audio.** Música, tono, si la voz suena robótica: no se mide.
- **Nada de esto reemplaza mirar el video.** Es la última línea, siempre.

## Marca nueva

**No hace falta configurar nada.** Poner la placa a pantalla completa en
`brand/placa.png` (o en `Placa/`, o suelta con `placa` en el nombre) y montar.

Si Whisper escribe mal el nombre de la marca, agregar `marcas_whisper` al config del
trabajo. Recién si la marca se vuelve recurrente conviene crearle su
`brand/edicion-ugc.json` para no repetir esas correcciones en cada trabajo.

Las reglas universales no se tocan — se validaron en cuatro marcas.

## Reportar al usuario

Después de montar, decir siempre: duración final, qué se recortó, si hubo morph y si
se tapó o no, y **la ruta donde quedó el archivo**. **Si algo quedó sin resolver,
decirlo explícitamente.** Quien usa esta skill puede no saber editar y no va a
detectar el problema mirando el video.

El self-check completo antes de entregar está en `eval/quality_checklist.md`.

## Relación con `hyperframes`

Las dos son post-producción, pero no son la misma cosa:

| | `edicion-ugc` | `hyperframes` |
|---|---|---|
| Qué es | Pipeline **determinístico** para montar clips de avatar/UGC: análisis + reglas medidas + render FFmpeg | **Composición creativa**: plan de edición por segundos, transiciones, captions con estilo, música, formatos |
| Decide | Nada estético: aplica constantes medidas | Todo: ritmo, hook, tipografía, transición |
| Entrada | Clips de avatar hablando + placa | Cualquier material: clips, frames, fotos, VO, música |
| Salida | Un MP4 9:16 con el corte estándar | Proyecto HyperFrames + MP4 en 9:16 / 4:5 / 1:1 / 16:9 |

Cómo elegir:

- *"montame estos clips de avatar"* / *"editá este UGC"* / *"revisá si hay morph"*
  → **`edicion-ugc`**.
- *"armame una pieza con estos assets"* / *"captions con estilo"* / *"placa
  animada"* / *"adaptalo a 4:5"* → **`hyperframes`**.

**Está planificado** que `edicion-ugc` emita un plan de edición que `hyperframes`
renderice (v2). **Hoy no lo hace**: son dos caminos separados y cada una renderiza lo
suyo. No le prometas al user un handoff que todavía no existe.

## Punto de entrada

Cuando te disparen, **verificá el entorno** y **arrancá por el paso 1 (`revisar`)**.
No montes sin revisar antes.
