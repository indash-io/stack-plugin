# Scene Analysis

Decidí modelo, estructura, frames de referencia y duración con criterio concreto. Nada de "porque sí".

---

## 1. ¿Kling 3.0, Veo 3.1 o Seedance 2.0?

### Usar Kling 3.0 cuando:
- Duración requerida **> 8 segundos**
- Necesitás **multi-shot storytelling** (varias tomas narrativamente conectadas)
- El **producto debe mantenerse visualmente idéntico** a lo largo de varios planos (Element Consistency comprobada)
- El video tiene **physics compleja** (líquidos, telas, partículas, interacciones)
- Necesitás **ambient + SFX denso** más que diálogo preciso
- Diálogo en español regional pero **no tenés referencias multimodales** y querés flujo conocido (Kling + voz aparte + lipsync)

### Usar Veo 3.1 cuando:
- Duración ≤ **8 segundos**
- Hay **diálogo a cámara** que necesita **lip-sync perfecto**
- Close-up humano extremo (cara, ojos, piel) — Veo da más realismo
- Cámara con movimiento **cinematográfico complejo y muy específico**
- La **adherencia al prompt** es crítica (cada detalle tiene que salir como lo pediste)

### Usar Seedance 2.0 cuando:
- Tenés **referencias multimodales reales** (foto del producto, foto del cast, clip de cámara/mood, audio de música o voiceover) — hasta 9 imgs + 3 videos + 3 audios. Es donde Seedance brilla por encima de Kling/Veo.
- Necesitás **multi-shot largo (≤15s) con audio sincronizado a la acción** generado en un solo pass (música + SFX matcheando los beats, no agregado en post).
- Querés **video extension nativa** (continuar un clip ya generado sin corte visible) — Seedance lo soporta nativamente, los otros no.
- El pedido es **commercial/premium aesthetic** (hero shots de producto, beauty shots con reflective surfaces, motion graphics estilizado). Seedance default-ea a este look.
- Necesitás **storyboard beat-synced** (cuts en strong beats de música de referencia).

### NO usar Seedance 2.0 cuando:
- El sujeto principal es **persona en close-up extremo con diálogo a cámara** — Veo 3.1 es mejor en hyper-realismo facial y lip-sync (debilidad admitida de Seedance).
- Necesitás **texto on-screen preciso** (carteles, logos legibles, números) — Seedance tiene text rendering flojo.
- **Múltiples personajes humanos** interactuando con consistencia entre ellos — multi-subject consistency aún en optimización.
- El audio nativo en español regional es no-negociable (no hay garantía oficial; usar voz aparte).
- Querés **look UGC handheld auténtico** y no tenés ganas de sobre-dirigirlo — Seedance no documenta el look UGC y default-ea a commercial. Si insistís en Seedance para UGC, sobre-especificá `subtle handheld micro-shake, natural window light, iPhone selfie framing, no studio lighting, no color grading`. Kling lee UGC más natural sin pelearle.

### Empates rápidos
- **Humano hablando 6-8s, lip-sync no negociable** → Veo 3.1.
- **Producto + narrativa multi-shot 10-15s, sin referencias multimodales** → Kling 3.0.
- **Producto + narrativa multi-shot 10-15s, con foto del producto + clip de cámara + audio de música** → Seedance 2.0.
- **Audio sincronizado a beats musicales (drop, cut on beat)** → Seedance 2.0.
- **POV testimonial UGC raw** → Kling 3.0 (Seedance fuerza el look pulido).

### Caso imposible
Si el pedido necesita >8s con lip-sync perfecto y cámara muy compleja, avisar: "Ningún modelo hace esto perfecto; propongo dividirlo en 2 clips (uno Veo 3.1, otro Kling 3.0 o Seedance 2.0) y pegarlos en edición."

### Caso imposible #2 — Multi-instance packshot
Si el ángulo creativo requiere mostrar **el mismo producto en N estados/configuraciones simultáneamente en un mismo shot** (ej: una butaca convertible en sus 3 modos alineados, un envase en 3 tamaños lado a lado, una persona en 3 outfits a la vez), **NO se puede hacer en un solo shot**. Element Consistency está pensada para un sujeto principal, no para N instancias coherentes. Cada copia se sintetiza independiente y deriva (color, textura, geometría).

**Avisar al usuario ANTES de generar** y proponer uno de estos 3 patrones:
1. **3 mini-clips Kling** (recomendado) — generar N imágenes Nano Banana (una por estado) + N mini-clips Kling de ~1.5s + pegar en edición. Suma costo de N-1 generaciones extra pero es la única vía predecible.
2. **N imágenes Nano Banana montadas como secuencia en CapCut/Premiere** — más barato; lee más "carrusel" que "video continuo".
3. **Collage publicitario explícito** — UNA imagen Nano Banana donde el prompt asume "three different units" (no "same product in three configs"). Solo si el cliente acepta variabilidad visual entre instancias.

Ver `examples/bad/multi_instance_packshot.md` para el caso real que originó esta regla.

---

## 1.5. Referencias multimodales (solo Seedance 2.0)

Seedance 2.0 acepta hasta **9 imágenes + 3 videos + 3 audios** de referencia simultáneos (máx 12 archivos). Cada referencia debe declarar su rol explícitamente con la sintaxis `@image1 as [rol]`. Es la diferencia más fuerte vs Kling/Veo.

### Roles típicos de referencias

| Slot | Rol típico | Ejemplo de uso |
|---|---|---|
| `@image1` | front-face del cast | `@image1 as front-face reference of the protagonist` |
| `@image2` | side-profile / 3/4 view del mismo cast | `@image2 as side-profile reference, same person` |
| `@image3` | wardrobe / outfit | `@image3 as outfit reference (cream cotton sweatshirt)` |
| `@image4` | producto (packshot real) | `@image4 as product reference, maintain label and color exactly` |
| `@image5..9` | setting, props, mood-board, paleta | `@image5 as setting reference (bedroom interior tone)` |
| `@video1` | referencia de cámara/movimiento | `@video1 as camera movement reference, copy the push-in pacing` |
| `@video2` | referencia de mood/grading | `@video2 as color grading and mood reference` |
| `@video3` | referencia de acción/timing | `@video3 as action reference (how the hand twists the dropper)` |
| `@audio1` | música / beat | `@audio1 as background music reference, cut on strong beats` |
| `@audio2` | voiceover tone / acento | `@audio2 as voiceover tone reference, conversational intimate` |
| `@audio3` | ambient / SFX mood | `@audio3 as ambient reference (rainy street, distant traffic)` |

### Priorización cuando faltan slots

Si el pedido requiere más referencias que las disponibles, priorizar en este orden:
1. **Cámara/movimiento** (un `@video` de cámara salva descripciones largas)
2. **Consistencia de sujeto** (front-face + outfit es lo mínimo viable)
3. **Mood/audio** (un `@audio` de música define ritmo y atmósfera mejor que texto)

Las referencias que no entran se describen en texto plano dentro del prompt.

### Reglas para usar referencias bien

- **Cada referencia subida tiene que declarar rol.** Si subís sin rol, Seedance infiere y el output deriva.
- **No subir referencias contradictorias** (dos `@image` que muestren outfits distintos del mismo cast → el modelo mezcla).
- **Foto del producto real** > prompt textual del producto. Si el usuario tiene la imagen del producto, usarla siempre como `@image` con rol explícito.
- **Para look UGC con Seedance:** subir un `@video` de un UGC real handheld como `camera movement and aesthetic reference`. Es la vía más rápida de pelearle al default commercial.

---

## 2. ¿First frame solo, o First + Last frame?

### Solo first frame
- Movimiento **simple y continuo** (persona hablando, caminar, girar, push-in, pull-out)
- Escena **estática** con poco cambio
- Testimonial a cámara
- Producto en mano sin transformación

### First + Last frame
- **Transformación** (antes/después — maquillaje, limpieza, montaje)
- **Reveal** (objeto oculto pasa a visible)
- **Cambio grande de encuadre** que queremos forzar con precisión
- **Última pose / estado final** tiene que ser pixel-específico (ej: packshot final de marca)
- Cuando el riesgo de "drift" del modelo es alto y queremos acotarlo

### Regla práctica
Si no podés describir el último segundo con la misma precisión que el primero usando solo texto → generá last frame con Nano Banana y pasalo como referencia.

---

## 3. Duración por tipo de contenido

| Tipo | Default | Razón |
|------|---------|-------|
| Hook ad (TikTok) | 3-6s | Retener scroll |
| Testimonial corto | 6-8s | Una frase + respiración |
| Testimonial largo | 10-15s (Kling) | Argumento completo |
| Product demo | 5-10s | Mostrar uso + beneficio |
| Transformation | 4-8s | Before + pivot + after |
| B-roll | 3-5s | Textura para editar |
| Narrative multi-shot | 10-15s (Kling) | 2-3 beats |

---

## 4. Aspect ratio

| Plataforma | Ratio |
|------------|-------|
| TikTok / Reels / Shorts | **9:16** |
| YouTube landscape / LinkedIn | **16:9** |
| Feed IG estándar | **1:1** |
| Feed IG vertical | **4:5** |

**Regla:** el aspect ratio de la imagen Nano Banana **debe coincidir** con el del video. Si no, el modelo de video la reencuadra y rompe composición.

---

## 5. Modo de audio

Decisión basada en **idioma del diálogo + modelo elegido**, no solo en tipo de contenido.

### Tabla de decisión

| Contenido + idioma | Modelo | Audio nativo | Cómo se resuelve la voz |
|---|---|---|---|
| Testimonial con diálogo en **inglés** | Veo 3.1 | **on** | nativo (lip-sync excelente) |
| Testimonial con diálogo en **inglés** | Kling 3.0 | **on** (decente) | nativo |
| Testimonial con diálogo en **inglés** | Seedance 2.0 | **on** (decente, audio sincronizado a la acción) | nativo |
| Testimonial con diálogo en **español regional** (argentino, mexicano, cubano, etc.) | Veo 3.1 | on (acentos OK) | nativo |
| Testimonial con diálogo en **español regional** | **Kling 3.0** | **OFF** | **voz aparte + lipsync en post** |
| Testimonial con diálogo en **español regional** | **Seedance 2.0** | **OFF** (sin garantía oficial de acentos LATAM/ES + audio distortion ocasional) | **voz aparte + lipsync en post** |
| Música + SFX sincronizados a beats (sin diálogo) | Seedance 2.0 | **on** (es su fuerte: audio-video joint generation) | nativo |
| Sujeto no-humano (dummy, robot) hablando, cualquier idioma | cualquiera | **OFF** | voz aparte + lipsync |
| Product demo con voice-over (sin diálogo a cámara) | cualquiera | off | voice-over en post |
| ASMR / sensorial (sin diálogo) | cualquiera | **on** (SFX nativos clave) | — |
| B-roll silencioso | cualquiera | off | — |

### Regla del español regional en Kling y Seedance

**Kling 3.0** está entrenado fuerte en inglés/mandarín, débil en español. Su audio nativo en español **aluciona sistemáticamente**: pronuncia palabras inventadas, pierde el acento regional, desincroniza.

**Seedance 2.0** documenta mejoras en chino (incluyendo opera tradicional) e inglés, pero **no garantiza acentos LATAM ni español regional**. Sumado a "audio distortion ocasional" que admite ByteDance, el riesgo es alto.

**Nunca pedir native dialogue en Kling ni en Seedance para español.** Default: voz aparte + lipsync. Solo en Veo 3.1 el español regional en native audio es aceptable.

### Workflow voz aparte + lipsync

Cuando audio nativo es **off** y hay diálogo:

1. El prompt de video pide al modelo: `"lips move in minimal conversational articulation synced to off-camera voice (no native audio generation). Voice added in post."` — esto asegura que la boca se mueva genéricamente, dando material a la herramienta de lipsync.
2. La voz se genera o se graba aparte:
   - **Voz humana real** (recomendada para máxima autenticidad) — alguien con el acento real lee el script en un cuarto silencioso con celular.
   - **TTS multilingüe** — ElevenLabs (best in class), Play.ht, Murf, Speechify, Resemble.ai.
3. La voz se aplica al video con una herramienta de lipsync: Enhancor V4, Sync.so, HeyGen, Kling Lipsync nativo, Runway Lipsync.

Ver `examples/good/testimonial_mia_15s.md` y `examples/good/ad_robot_selfie_cubano_15s.md` para casos completos del flujo.
