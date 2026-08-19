# Template de pedidos UGC — definición de columnas

Base: el template actual (una fila por video, hoja por mes) más los cambios
aprendidos en producción. **Ningún campo vacío bloquea: cada uno tiene default.**

| Columna | Qué pone el cliente | Default si viene vacío |
|---|---|---|
| ID | número de fila | — (obligatorio) |
| Estado | Pendiente / En producción / Entregado | Pendiente |
| Producto (link) | **URL de la ficha del sitio** (no el nombre suelto) | — (obligatorio; si mandan nombre, se busca la URL en el sitio y se confirma) |
| Ángulo / Tema | de qué habla el video, en sus palabras | se propone desde los beneficios del producto |
| **No negociables** | lo que SÍ o SÍ debe decirse/mostrarse | ninguno |
| Segundos | duración total | 20 |
| Formato | 9:16 / 16:9 | 9:16 |
| Avatar | descripción o referencia | el aprobado en la ficha de marca |
| Escenario | dónde pasa | Estudio de podcast |
| Tono | cómo habla | el de la ficha de marca |
| Cómo mostrarlo | producto en mano / en mesa / solo mencionado | visible + mencionado |
| Notas | lo que no entra en otra columna | — |

## Cambios vs el template viejo

1. **"No negociables" es columna nueva.** Antes venían enterrados dentro del texto
   del ángulo y era fácil pisarlos.
2. **El link del producto es obligatorio y es URL.** Antes venía a veces nombre,
   a veces URL; el nombre suelto obliga a adivinar.
3. **Defaults declarados por columna.** Antes un campo vacío frenaba la producción
   o se resolvía distinto cada vez.

## Qué NO va en el template

- Beneficios y precio del producto → viven en el producto cargado en Indash (paso 0).
- Tono general, tope de contenido, avatares → viven en la ficha de marca.
- El template es SOLO lo que cambia video a video.
