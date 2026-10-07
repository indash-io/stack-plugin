# 03 — Concepto y storyboard

Objetivo: un `STORYBOARD.md` (plantilla en `templates/storyboard.md`) donde cada segundo
está en la grilla y cada elemento tiene su fuente. Primero leé `style/energia.md`.

## 1. La forma

| Tramo | Sitio (~38 s) | App (30 s) | Qué tiene que pasar |
|---|---|---|---|
| Hook | 0–4 s | 0–3 s | La promesa o el dolor en palabras que golpean en el beat |
| Problema | 4–12 s | 3–7.5 s | Comedia concreta: el dolor actuado con objetos, un remate por compás |
| Giro | 12–16 s | 7.5–11 s | Transformación física: todo se chupa a un punto y nace la marca |
| Producto / prueba | 16–30 s | 11–25 s | Una promesa por escena, sobre material real |
| CTA + cierre | 30–38 s | 25–30 s | El golpe final del tema en el tap del CTA, después el end card |

En la rama app, la forma es la del guion. Respetá sus escenas y sus tiempos, y poné la
energía dentro de cada una.

## 2. Las escenas

- **Una idea por escena** y un título de ≤ 7 palabras. La palabra clave se marca con el
  acento de la marca (subrayado, cursiva o color).
- **La metáfora de cada pilar sale del sistema de símbolos de la marca**, no de un set de
  íconos genérico.
- **El problema se cuenta exagerado y físico**: el cable del teléfono que se estira
  hasta el horizonte, el pin que nunca se acerca, el inbox que desborda. Si el dolor es
  "esperar", la música de espera telefónica es el chiste (paso 5).
- **El producto se muestra en pantalla real**, con la UI que sale del teléfono hacia la
  cámara. Va el dato concreto de esa pantalla, no un adjetivo.
- **Cada escena entra en un downbeat** y sus eventos internos caen en beats o corcheas.
  Anotá el tiempo exacto de cada evento: esa lista son los cues de SFX del paso 5.
- **Escenas de sección musical**: el drop (o el estribillo) del tema va en el giro, y su
  golpe final en el CTA. Si ya tenés el tema, mirá su mapa de compases (`beat_phase.py`)
  antes de fijar tiempos.

## 3. La locución (si hay)

- Una línea por escena, y arranca en el corte de esa escena.
- Va escrita para el oído y dice solo lo que está en el ledger.
- Como presupuesto, contá ~2.5 palabras por segundo de escena para un locutor en
  español. Si no entra, cortá palabras: acelerar la toma más de 8% suena apurado.
- **Captions solo donde la voz dice algo distinto del título en pantalla.** Si repiten
  el título, sobran.

## 4. Revisá antes de construir

- ¿Hay algún tramo de más de 1.5 s sin un evento nuevo?
- ¿Se repite la misma transición dos veces seguidas?
- ¿Algún elemento que representa al producto no tiene fuente real?

Corregí lo que salga antes de pasar a `04_assets.md`.
