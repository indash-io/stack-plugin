# 03 — Carga masiva: una carpeta entera al onboarding

El caso central de la skill: alguien de Indash con lo que el cliente mandó por WhatsApp, o el cliente que tira 30 archivos. El orden es **inventariar → proponer → OK → subir → registrar → textos extraídos**. No se sube nada antes del OK, y después del OK no se pregunta nada más hasta que esté todo arriba: el objetivo es que la persona diga "dale" una vez y vea los archivos en Indash.

Necesita shell y los archivos en disco. Sin shell (claude.ai), ver *Según dónde corras* en `02_onboarding.md`.

## 1. Inventariar

Listá la carpeta entera con tamaño y tipo real (`find` + `stat` + `file --mime-type`; la extensión de un archivo de WhatsApp miente seguido). Abrí lo que haga falta para saber qué es: las imágenes las ves, los PDF y Word los leés. **Clasificás por contenido, no por nombre de archivo**: `IMG_4032.jpg` puede ser un packshot, una captura de un DM o una reseña.

Cruzá contra `state`: lo que ya está cargado (mismo nombre de archivo en la misma lista) no se sube de nuevo. Pasa cuando se retoma una carga que quedó por la mitad.

## 2. A qué lista va cada cosa

| Es… | `list` | Nota |
|---|---|---|
| Brand book, guidelines, logos, tipografías, paleta | `identity` | |
| Packshots, fotos de producto, lifestyle, video bruto, fotos de founders | `assets` | Es una compuerta: sin un packshot fiel no hay producción |
| Briefs viejos, guiones, captions aprobados, doc de tono | `written` | |
| Piezas publicadas que sí los representan | `corpus_on_brand` | El veredicto es del cliente, no tuyo |
| Piezas propias que no los representan, o de otras marcas a las que no quieren parecerse | `corpus_off_brand` | `origin: "own"` u `"other_brand"` |
| Piezas que funcionaron, pagas | `winner_paid` | `metric` solo si vino con el material |
| Piezas que funcionaron, orgánicas | `winner_organic` | Ídem |
| Capturas de DMs, comentarios, mails a soporte | `objections` | La captura va tal cual |
| Decks, mails, PDFs sueltos, lo que no entra arriba | `misc` | |
| Audios | — | `add_audio`, ver abajo |
| Reseñas en texto (un .txt, un .csv, un export) | — | `set_text` a `audience.reviews_raw`, literal y entero, en `append` |

**Lo que no podés decidir vos, se pregunta en la misma tabla.** Que una pieza esté en la carpeta no dice si es "esto somos" o "esto no somos", ni si una ganadora fue paga u orgánica. Si el nombre de la subcarpeta o el mensaje de la persona lo dicen, usalo y citá de dónde lo sacaste en la columna "por qué". Si no, esa fila va con la lista en duda y la pregunta al lado. Adivinar un veredicto es inferir, y el bucket "esto no somos" mal cargado le enseña al generador lo contrario de lo que quiere la marca.

Casos de borde:

- **Más de 50 MB**: no entra por acá. Va por la app, o como link de Drive (`set_text` a `assets.drive_url`, o `add_file` con `source: { url }`).
- **Más de 40 fotos de producto**: antes de subirlas, ofrecé conectar la tienda o pasar el link de Drive. Es la misma información sin subir archivo por archivo, y se mantiene sola.
- **Un tipo que el server rechaza**: lo dice el resultado de ese archivo. Avisalo en el resumen y seguí con el resto.
- **Un export de chat de WhatsApp** (`_chat.txt`): el archivo entero va a `misc`. Lo que quieras pasar de ahí a un campo es una extracción (sección 5).
- **Basura evidente** (duplicados, `.DS_Store`, stickers, capturas que no son de la marca): fila "no lo subo", con el motivo. No lo borres del disco.

## 3. Proponer y esperar el OK

Una sola tabla, con todos los archivos:

| Archivo | Va a | Por qué |
|---|---|---|
| `brandbook_2025.pdf` | `identity` | Manual de marca: paleta, logos y tipografías |
| `IMG_4032.jpg` | `objections` | Captura de un DM preguntando si mancha la ropa |
| `reel_marzo.mp4` | ¿`corpus_on_brand` o `winner_organic`? | Reel publicado. ¿Es de los que mejor anduvieron, o solo los representa? |
| `audio_founder.opus` | audio → ¿? | 4:12. ¿De qué habla? |
| `IMG_4032 (1).jpg` | no lo subo | Duplicado de `IMG_4032.jpg` |

Si son más de 30, agrupá las filas obvias ("`fotos/` — 24 packshots → `assets`") y dejá una fila por archivo solo donde hay una decisión. Cerrá con las preguntas pendientes juntas y pedí **un OK a la tabla entera**, no uno por archivo. Si la persona corrige filas, aplicá los cambios y subí; no hace falta mostrarla de nuevo salvo que cambie más de la mitad.

Por qué el OK antes de subir: en la app el cliente arrastra cada archivo a su cajón, y esa elección es suya. Acá la elección la propusiste vos. Sin el OK, la clasificación sería una inferencia tuya guardada como si fuera del cliente.

## 4. Subir y registrar, en lotes de 20

Por lote:

1. `create_onboarding_uploads` con hasta 20 archivos (`filename`, `mime_type`, `bytes` reales). Cada uno vuelve con su `status`: uno que no entra (tipo no permitido, más de 50 MB) no tira el lote.
2. Subí cada uno con el `curl --upload-file` que devuelve la tool, con su `method` y sus `headers` tal cual, y `--fail` para que un error HTTP no pase por éxito. Subí enseguida: las URLs vencen (`expires_at`). Si venció, pedí otra.
3. `update_brand_onboarding` con un `add_file` por archivo **que subió bien** (`source: { upload_id, filename }`: sin `filename` la app lo lista por su uuid). El límite es 25 cambios por llamada.
4. Leé `results[]` uno por uno (`status`, y en los que fallan `error` y `hint`). **El lote no es transaccional**: puede haber 18 `ok` y 2 `error`; `applied` y `failed` dan el total. Reintentá solo los que fallaron; reenviar el lote entero duplica los que ya entraron.
5. Una línea de avance: "40 de 63 cargados, 2 con error (`catalogo.ai`: tipo no permitido)".

`caption` solo si la persona dijo algo de ese archivo; va con sus palabras. No describas la imagen en el caption.

## Audios

El audio suele ser el material más rico de todo el onboarding: cuatro minutos del founder contando la marca valen más que cualquier formulario. No lo dejes colgado como adjunto en `misc`.

`add_audio` transcribe en el server y escribe el texto donde diga `save_to`, así que hay que saber de qué habla **antes** de subirlo, y vos no podés escucharlo: preguntale a la persona.

```
¿De qué habla el audio?
├── Cómo funciona un producto → `save_to: { mechanism: { name } }` crea el mecanismo; `{ mechanism: { id } }` suma a uno que ya existe
├── Un solo tema que es un campo de texto (qué usaban antes, el objetivo, los claims prohibidos)
│     → `save_to: { field }` con ese campo
└── De todo un poco ("contame de la marca"), o la persona no sabe
      → `save_to: { field: "goals.freeform" }`
```

La transcripción de lo que dijo el cliente es material suyo: se guarda entera sin pedir OK. Lo que necesita OK es lo que **vos** saques de ese `transcript` para otros campos: el mecanismo que aparece en el minuto dos, una objeción que menciona al pasar. Eso se muestra con sus palabras y espera el "¿lo guardo así?".

Si la transcripción falla, el resultado vuelve con `status: "error"` y `audio_attached: true`: el audio quedó adjunto. Reenviar el mismo `add_audio` reintenta la transcripción sin adjuntarlo de nuevo; si vuelve a fallar, avisale y ofrecé que lo escriba. Lo mismo con un audio que ya estaba sin transcribir: aparece en `next[]`. Si salta el tope diario de minutos, decilo y dejá los audios que falten para mañana o para la app.

## 5. Textos extraídos, al final y aparte

Después de los archivos, y en un bloque separado de la tabla, lo que sacaste de adentro del material para un campo de texto: las reseñas transcriptas de capturas, el mecanismo que explica un PDF, las preguntas frecuentes de un export de chat.

Por cada campo, mostrá el texto **entero y literal**, decí de qué archivo salió y preguntá si se guarda así. Transcribir una captura es copiar lo que dice, con sus errores. Si una parte no se lee, va `[ilegible]`: no la completes.

Es opcional. Si la persona prefiere no revisar textos ahora, los archivos ya quedaron cargados y los campos de texto siguen en `next[]` para el modo conversado.

Cuando termine la carga, volvé a `02_onboarding.md`: lo que quede en `next[]` se pide conversando (la tienda, el mecanismo si no vino en ningún archivo, los límites, el objetivo), y de ahí al cierre.
