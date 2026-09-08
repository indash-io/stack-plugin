# Model Selection — el roster completo de `generate_video`

La skill ya no es Seedance-only. El MCP de indash expone 9 modelos de video. Elegir el modelo correcto por shot es parte del trabajo del strategist. Este archivo define cuándo usar cada uno.

> Actualizado 2026-09-07: entraron Seedance 2.5 y su ruta ark, omni pasó a Omni Flash 1.1 (API nativa de Google) y kling pasó a O3 Pro.

---

## Roster completo (vía `generate_video`)

| Modelo | Refs máx | Duración | Fortaleza | Debilidad |
|---|---|---|---|---|
| **seedance** (2.0 vía fal) | 9 img + 3 vid + 3 aud | 4–15s | Mejor balance fidelity/motion. Multi-ref. | Moderación ESTRICTA (personas, piel, niños, marcas suelen bloquearse). Cola a veces lenta. **El doble de caro que su ruta ark.** |
| **seedance-2.5** (2.5 vía fal) | 10 img + 10 vid + 10 aud | 4–30s | **30s en UN solo render** (nada más en el roster llega). Mejor control de referencias, last frame, y text-to-video. | ~1.55x el costo por segundo de 2.0. A 1080p es el render más caro del stack. |
| **seedance-ark** (2.0, backend ByteDance) | 9 img | 4–12s | Moderación permite personas AI-generated. **Mitad de créditos que fal.** Probar acá primero para escenas con gente. | LENTO: ~40s de render por segundo de clip. Sin auto-retry. Sin refs de video/audio. |
| **seedance-2.5-ark** (2.5, backend ByteDance) | 10 img | 4–12s | Lo mismo, sobre 2.5: mitad de precio y moderación permisiva. | Pierde los 30s y las refs de video/audio — eso vive solo en fal. |
| **omni** (Gemini Omni Flash 1.1) | 10 img + 3 vid (≤3s c/u) | 3–10s | El MÁS RÁPIDO. **360p a un tercio del precio de 720p** = el modelo para draftear. Acepta last frame y text-to-video. | Menor fidelity de producto. Máx 10s. |
| **veo** (Google Veo 3.1) | 3 img | 4/6/8s | Cinematográfico, buen motion natural. | Solo 4, 6 u 8s (y exactamente 8 con 2+ refs). Ignora generate_audio. |
| **kling** (Kling O3 Pro) | 2 img | 3–15s | Close-ups emocionales, caras. Buen fallback cuando Seedance se traba. | 2 refs, y la 2ª es el END frame. **Ya NO acepta negative prompt** (O3 no tiene el campo; veo es el único que queda). |
| **grok-imagine** (xAI 1.5) | 1 img | 3–15s | Moderación MÁS permisiva. Audio nativo. | 720p, 1 ref, fidelity de producto menor. |
| **minimax-h3-max** | 0–1 img | 5–15s | Rapidísimo, text-to-video real. | 768p máximo. Sin audio ni negative prompt. |

## Las dos palancas de costo que casi nadie usa

1. **La ruta ark cuesta la mitad.** `seedance-ark` y `seedance-2.5-ark` son el MISMO modelo que sus gemelos de fal, por el backend oficial de ByteDance, a la mitad de créditos. Si el shot no necesita refs de video/audio ni más de 12s, la ruta ark es la respuesta por defecto.
2. **La resolución mueve el precio.** La familia seedance y omni cobran por píxeles: 1080p sale ~2.25x lo que sale 720p, y el 360p de omni sale un tercio de su 720p. Draftear en 360p/480p y terminar en 720p no es una optimización menor — es la diferencia entre quemar el presupuesto en la exploración o en el entregable.

---

## Decision tree (aplicar en el paso 5 del workflow)

```
¿Es un draft / prueba de coreografía / iteración barata?
  → OMNI a 360p (lo más barato y rápido del roster por lejos)
  → Cuando la coreografía valide, re-render final en Seedance.

¿El shot necesita durar más de 15s?
  → Si tiene que ser UNA SOLA TOMA: SEEDANCE-2.5 (hasta 30s). Es el único.
    Pedilo a 720p salvo que el entregable justifique 1080p — a 30s duele.
  → Si puede construirse por partes: OMNI + extend_video (hasta 40s, de a
    3-10s por turno). Más barato y, sobre todo, el user APRUEBA los primeros
    10s antes de que pagues los otros 30.

¿Producto con label/marca específica, hasta 15s?
  → SEEDANCE-ARK primero (mismo modelo, mitad de precio)
  → SEEDANCE (fal) si necesitás refs de video/audio o más de 12s.

¿Escena con personas / piel / niños?
  → Las rutas -ARK primero (moderación permite personas AI)
  → Si bloquea: KLING o GROK (permisivo)
  → SEEDANCE vía fal probablemente bloquee — no quemar créditos ahí primero.

¿Close-up emocional de cara (ojos, expresión)?
  → KLING rinde sorprendentemente bien.

¿Necesitás un negative prompt?
  → VEO. Es el único que quedó con el campo (kling lo perdió al pasar a O3).

¿Necesitás arrancar sin ninguna referencia (text-to-video puro)?
  → SEEDANCE-2.5, OMNI o MINIMAX-H3-MAX. El resto exige al menos una imagen.

¿Seedance en cola muerta (>10 min processing)?
  → Re-fire en KLING (mismo frame-0). NO Veo si el frame-0 es base64.

¿Necesitás audio nativo en el render?
  → KLING / GROK / OMNI / la familia seedance. VEO lo ignora.
    En seedance el audio NO cambia el precio: si dudás, dejalo prendido.
```

## El workflow draft→final (validado, y ahora mucho más barato)

Para briefs caros (varios shots, hypermotion, coreografía compleja):
1. **Draft en Omni a 360p** (10s máx): validar coreografía de cámara, timing de beats, composición. Es el render más barato que existe en el stack.
2. Mostrar draft al user si hay dudas de dirección.
3. **Final en Seedance** (ruta ark si alcanza) con el mismo frame-0 y el motion prompt refinado según lo aprendido del draft.

Esto ahorra quemar renders caros de Seedance en coreografías que van a cambiar. Con el 360p de omni y la ruta ark del final, un ciclo draft→final cuesta hoy una fracción de lo que costaba.

---

## Extender en vez de renderizar largo

`extend_video` continúa un clip de omni agregando 3-10s por turno hasta 40s.
Cambia el orden del trabajo: en vez de apostar a un render largo, generás el
primer beat, lo mirás, y recién ahí seguís.

- **Solo omni.** Se apoya en la API con estado de Google; ningún otro
  proveedor del roster tiene equivalente.
- **Solo clips nuestros**, y generados desde el 2026-09-08. Los anteriores no
  guardaron el id que el proveedor necesita para continuarlos.
- **Serial**: un clip solo se continúa cuando terminó de renderizar. No se
  disparan los cuatro turnos juntos.
- **Encadenás sobre el último**, no sobre el original: cada turno devuelve un
  `run_id` nuevo cuyo clip es el más largo.
- **Cada turno deja su propio creative.** 40s encadenados = cuatro drafts en
  la galería; el último es el completo. Promocioná ese.
- **Se cobra lo agregado**, no lo que vuelve (el proveedor devuelve el clip
  entero cada vez).
- **El prompt describe SOLO lo nuevo.** El modelo ya tiene la escena, el
  sujeto, la luz y el lenguaje de cámara. Repetirle el prompt original lo hace
  pelear contra lo que ya construyó. "La cámara se aleja y aparece la barra
  entera" sí; "un vaso de cerveza sobre una barra de madera, luz cálida, la
  cámara se aleja" no.

## Best practices POR MODELO

### Seedance (2.0 y 2.5)
- Multi-ref = **soft conditioning, NO timeline anchoring**. Nunca pasar una ref esperando que sea "el frame del segundo N". Si un frame específico debe aparecer, ese frame es el frame-0 de su propio render.
- **Single-take multi-ref VALIDADO** para: producto ESTÁTICO + toda la coreografía en la cámara (caso real: bebida en lata, marca anonimizada). El producto nunca cambia de estado → hasta 15s en un solo render funciona.
- **Stop-motion discreto VALIDADO** para transformaciones: si el producto tiene N configuraciones (caso real: mobiliario infantil plegable, marca anonimizada), pedir saltos stop-motion instantáneos entre estados anclados con refs (una ref por configuración, mismo ángulo de cámara todas) en vez de morphing continuo. El modelo no anima bisagras — salta entre estados. Prohibir explícitamente "continuous morphing" en el prompt.
- Transformaciones mecánicas continuas (plegado, encastre): partir en shots, cada estado con su frame-0 real.
- Regla de las 3 fidelidades: máx 2 de {movimiento, transformación, label} por render.
- Repetir "no people, no text, no logos, no graphic overlays" EN CADA motion prompt si el brief lo exige — una sola mención al principio no alcanza.

### Omni (Flash 1.1)
- Máx 10s → comprimir el arc o partir en 2 renders. Las refs ya no aprietan: 10 imágenes y 3 clips de video de hasta 3s.
- **360p para draftear, 720p para entregar.** No usar para el entregable final de un cliente premium; sí para social rápido de baja exigencia.
- Es el modelo para ITERAR. Cada iteración de Seedance cuesta bastante más.
- Acepta last frame y renderiza sin referencias — sirve para tirar una idea de cámara sin tener todavía el frame-0.

### Kling
- 1 sola ref → elegir la más informativa (frame-0 del estado inicial).
- Grade sale distinta al set de Seedance → avisar al user que unifique con LUT en CapCut.

### Las rutas -ark
- Mismo prompt grammar que seedance.
- **Mitad de créditos que la ruta fal del mismo modelo.** Es la decisión de costo más grande del roster y la que menos se toma.
- En content-policy failure: UN solo resubmit manual vale la pena, después cambiar de modelo.
- Presupuestar el tiempo: un clip de 10s ≈ 6-7 min de render.

---

## Negative-space choreography (para overlays de CapCut)

Cuando el brief incluye contador / badges / logo / texto (que NUNCA se renderizan):
- Coreografiar el negative space POR SHOT y declararlo en el prompt: "left half remains clean empty negative space", "top third completely clean".
- Mapear cada overlay del brief a un shot y su espacio reservado.
- Documentar en la entrega qué overlay va en qué espacio y con qué timing.

Esto convierte el "no renderizamos texto" de limitación en ventaja: el texto animado de CapCut (contadores reales, estrellas que se llenan) siempre se ve mejor que texto generado.
