# 01 — Intake

Del pedido (una frase, un guion pegado, el `.md` de otra skill) extraés estos
campos. Lo que falta lo tapa el default: **no preguntes en serie**, lo que
quede en duda va a la única pregunta consolidada del paso 4.

| Campo | Default si falta |
|---|---|
| **Pieza** (para qué es el audio) | Voz en off de un video corto (reel / UGC / ad) |
| **Plataforma** | Instagram / TikTok (vertical, se escucha con auriculares o sin) |
| **Duración objetivo** | La del video si existe; si no, **10-15s** para VO, 30s para ad, sin tope para narración |
| **Idioma y acento** | El del `CLAUDE.md` del cliente; si no hay, **español rioplatense con voseo** |
| **Voces** | Una. Dos solo si el pedido es un diálogo o una escena |
| **Guion** | Si vino, se adapta al oído (paso 2). Si no vino, se escribe desde el brief/producto |
| **Voz** | Si el `CLAUDE.md` tiene "Voz de marca" (`voice_id`), esa. Si no: sin acento específico → estudio; idioma/acento concreto → biblioteca (`list_voices`); persona específica → `design_voice`. Siempre **audición** de 2-3 |
| **Tono** | El de la marca (`CLAUDE.md`); si no hay, el que pide la pieza (UGC = natural, ad = claro, premium = pausado) |
| **Variantes** | **1** final (más la audición si hace falta). Más de 3 → confirmar que quieren pagar N |
| **Modelo** | `gemini-tts`. `gemini-tts-lite` si son muchas variantes de lo mismo o narración sin dirección |
| **Destino** | Galería del workspace (siempre) + disco (`exports/audio/` o la carpeta del set de video) |

## Señales que cambian el plan

- **"Que dure X segundos"** → el largo del guion sale de X (`02_guion.md`), no
  al revés. Si el texto que trajeron no entra, lo decís y proponés el recorte.
- **"Con la voz de <persona real>"** → no se puede (clonado no expuesto). Lo
  decís derecho y ofrecés `design_voice` con una descripción de esa voz,
  aclarando que es parecida, no la suya.
- **"Un argentino de 20 años" / "una voz de mujer de 40, ronca"** → eso es
  **voice design**, no `style`: `design_voice` con la descripción de rasgos
  permanentes + `language_code`. Si el pedido es solo el idioma/acento
  ("que sea mexicano"), alcanza con la biblioteca (`list_voices`).
- **Guion en inglés para público hispano** (o al revés) → preguntá en qué
  idioma se dice; no traduzcas por tu cuenta.
- **Viene de `all-videos` / `ugc-generator` / `hyperframes`** → leé el `.md`
  de la pieza: duración por shot, tono, hook. El audio se guarda **en la
  carpeta de ese set**, no en `exports/audio/`.
- **Muchas piezas iguales con distinto producto** (8 productos, mismo copy) →
  `gemini-tts-lite`, un item por producto, una llamada.

## Salida de este paso

Una ficha corta en tu cabeza (no se la mostrás todavía): pieza, plataforma,
duración objetivo, idioma/acento, 1 o 2 voces, guion sí/no, voz decidida
sí/no, variantes, modelo. Seguís a `02_guion.md`.
