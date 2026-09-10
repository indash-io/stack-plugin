# 01 — Conseguir el material y poder leerlo

Antes de opinar cualquier cosa, tenés que tener el brief **abierto y en texto**.
Revisar por el nombre del archivo o por lo que dice el mensaje que lo trae es
inventar.

## De dónde llega

**Desde una alerta de Slack** (el caso normal). El mensaje trae el nombre del
archivo y una **URL firmada** cruda de Supabase, además del id de submission.
Bajala:

```bash
curl -sL "<URL-del-mensaje>" -o /tmp/brief.<ext>
```

La URL dura 7 días desde que se generó. Si te da 400 o 403, está vencida:
pedila de nuevo en el thread en vez de adivinar el contenido.

**Pegado en el chat o una ruta local.** Igual de válido. Si el humano te pasa
una ruta, leela; si te pega el texto, usalo tal cual.

Si no tenés ninguna de las tres cosas, **frená y pedila**. No arranques el
diagnóstico sin el material.

## Convertirlo a texto

| Formato | Cómo |
|---|---|
| `.xlsx` / `.xls` | `python3 -c` con `openpyxl`, o `pip install openpyxl` primero. Recorré **todas las hojas** e imprimí fila por fila con su número. Los briefs de imágenes suelen ser una fila por pieza. |
| `.docx` | Descomprimilo (`unzip -p brief.docx word/document.xml`) y sacale los tags, o usá `python-docx` si está. |
| `.pdf` | `pdftotext -layout` si está disponible; si no, leelo como documento. |
| `.csv` / `.txt` / `.md` | Directo. |
| `.zip` | Descomprimí y tratá cada archivo por separado. Decí qué venía adentro. |

Reglas al leer una planilla:

- **Numerá las filas.** Los hallazgos tienen que poder decir "fila 12".
- **No te quedes con la primera hoja.** Las fechas y las ofertas suelen estar en
  una segunda hoja o en un bloque de notas al pie.
- **Las celdas vacías son información.** Una columna "foto de producto" vacía en
  9 de 12 filas es el hallazgo más importante del brief.
- **Anotá la estructura antes del contenido**: cuántas hojas, cuántas filas
  útiles, qué columnas. Eso ya te dice si el brief es un plan de piezas, un
  calendario o una lista de deseos.

## Antes de pasar al paso 2

Tené escrito para vos mismo (no lo muestres todavía):

- Qué archivo es y de qué tipo.
- Cuántas piezas propone y de qué formatos.
- Qué período cubre, si lo dice.
- Qué columnas o campos trae, y cuáles están vacíos.

Si el archivo **no es un brief** (te mandaron un catálogo, una factura, un
export de métricas), decilo en una línea y frená. No lo audites como si fuera un
brief.
