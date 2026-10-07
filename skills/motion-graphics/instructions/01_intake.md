# 01 — Intake

Objetivo: saber qué vino, qué rama es y dónde vive el proyecto, con una sola pregunta como mucho.

## 1. Inventariá todo lo que vino

| Entrada | Cómo la abrís | Qué anotás |
|---|---|---|
| URL | todavía nada (es el paso 2) | — |
| Video (grabaciones) | `ffprobe -v error -show_entries stream=width,height,r_frame_rate:format=duration` | resolución, duración, fps |
| PDF (guion, manual) | `pdftotext -layout` + `pdftoppm -r 72` para ver páginas | escenas, líneas de VO, specs de color/tipo/captions, advertencias |
| DOCX | `textutil -convert txt` (macOS) o `pandoc` | ídem |
| ZIP | `unzip -l` y después extraé | qué hay: end cards (variantes y tamaños), temas (versiones full/short) |

Los ZIP de música suelen traer ZIPs adentro, con varias duraciones del mismo tema: el
"short" de ~30–40 s suele ser un edit del compositor con final propio, y para un reel vale oro.

## 2. Decidí formato y defaults

| | Sitio | App |
|---|---|---|
| Aspecto | 16:9 · 1920×1080 | 9:16 · 1080×1920 |
| Duración | 35–40 s | la del guion (típico 30 s) |
| BPM | 120 (beat 0.5 s, compás 2 s) | 120 |
| Idioma y registro | el del sitio (voseo AR, tú MX…) | el del guion |

Lo que diga el guion o la persona le gana a esta tabla.

## 3. La carpeta del proyecto

- En una carpeta de cliente del stack: `exports/videos/<AAAA-MM-DD>_<slug>/`.
- Fuera de una: una carpeta hermana `<marca>-<pieza>/` en el directorio actual.
- Las variantes van en hermanas de la principal (`…-v2`, `…-vo`, `…-relax`).

## 4. Una sola pregunta, y solo si bloquea

Juntá en **un** mensaje lo que no podés resolver con defaults:
- ¿Música propia o licenciada? Si no hay, el score provisorio es lo más flojo de la pieza.
- ¿Locución? Si sí, ¿en qué workspace de Indash generarla? Si hay uno de prueba, va ahí:
  no le cargues borradores ni créditos al del cliente.
- ¿A qué pieza van los assets oficiales? Preguntalo solo si llegaron para más de una.

Lo que no bloquea, no lo preguntes: decidilo y anotalo para la entrega. Si el pedido trae
algo que no cuadra con la marca (el nombre de otra marca que quedó de una plantilla),
seguí con la marca real y avisalo en la entrega.

Siguiente: `02_research.md`.
