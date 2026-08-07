# Ejemplo GOOD — Testimonial de faja térmica, alivio de cólicos 15s (Kling Pro + voz aparte + lipsync)

**Input del usuario:**
> "Generame un UGC de 15 segundos para mi faja." (faja eléctrica para cólicos menstruales; marca anonimizada)
> Default: español argentino, multi-shot, plataforma TikTok/Reels.

**Qué hace este ejemplo interesante:**
- Producto íntimo (cólicos menstruales) — mood honesto sin sobre-dramatizar el dolor.
- Aplica el **default actual del skill** para diálogo en español regional: audio nativo **off** + voz aparte + lipsync en post.
- Articulación de labios mínima como anchor visual para Enhancor V4.
- Element consistency del dispositivo (rosa pastel + correa gris + pantalla LCD + logo de marca) entre wide + close-up.
- Prompt final: 2292 chars (bajo el cap de 2500, verificado con `wc -c`).

---

# Paquete de video — Confesión con faja térmica, alivio de cólicos (15s)

## 1. Análisis de escena
- **Tipo de contenido:** testimonial confesional + micro-demo
- **Sujeto principal:** ambos — mujer argentina ~28 años + la faja eléctrica (rosa pastel, correa gris, pantalla LCD circular, logo de marca)
- **Plataforma:** TikTok / Reels
- **Aspect ratio:** 9:16
- **Mood:** íntimo confesional, hogareño, tarde gris — "amiga que te cuenta lo que le funciona", sin sobre-dramatizar el dolor
- **Asumidos:** acento argentino (default); cast mujer 28 castaña sin maquillaje fuerte; setting living de departamento argentino; audio nativo **off** (voz aparte + lipsync); resolución 1080p

## 2. Recomendación de modelo
**Elegido: Kling 3.0 (Pro mode)**

Razón: 15s + 3 tomas narrativamente conectadas + el dispositivo tiene que mantenerse idéntico entre wide y close-up = Element Consistency + Multi-Shot Storytelling de Kling. Veo 3.1 queda afuera por cap duro de 8s. Audio nativo **off** porque Kling aluciona español argentino — voz aparte + lipsync en Enhancor V4.

## 3. Estructura
- **Total:** 15s single-clip
- **Shots:** multi-shot, 3 tomas
  - Shot 1 (0–5s): MCU mujer acurrucada en sillón, hook honesto
  - Shot 2 (5–10s): insert close-up — manos prenden la faja, pantalla LCD se enciende
  - Shot 3 (10–15s): vuelve a MCU, mujer relajada, alivio + cierre
- **Frames de referencia:** first + last
- **Razón first/last:** producto con detalles chicos (pantalla, logo de marca, correa) + transición emocional dolor→alivio. First ancla pain point; last ancla relief + producto visible.
- **Aspect ratio:** 9:16

## 4. Prompts de Nano Banana

### First frame
```
28-year-old Argentine woman, mid-length wavy chestnut brown hair fallen loosely over her shoulders, fair skin with natural texture, light freckles across the nose bridge and faint shadows under the eyes, no visible makeup, small silver hoop earring on the visible ear. Wearing an oversized heather-gray cotton t-shirt slightly stretched at the collar and soft charcoal-gray sweatpants. Sitting on a beige linen-upholstered couch, slightly curled forward, one hand resting on her knee, the other hand low near her abdomen. A cream-colored chunky knit throw blanket is draped diagonally across her lower waist and lap. Just visible peeking above the top edge of the blanket: a pastel-pink heating belt device — rounded rectangular pastel-pink plastic body with a small circular dark LCD display in the center (showing tiny abstract heat-level and battery icons), a small pink brand wordmark on the front face below the display, and a light gray adjustable fabric strap crossing visible at her side. Her expression: slightly tired and honest, faint brow furrow, mouth in a neutral slightly-pursed line — no dramatic pain, just real menstrual-day fatigue.

Setting: small Buenos Aires apartment living room — a tall narrow window behind the couch with soft overcast afternoon daylight coming through gauzy off-white curtains, a small ceramic beige mug of tea steaming faintly on a low side table on the right, a hanging pothos plant in the upper-left corner of the frame, a tall pale floor lamp turned off at the far left edge. Walls in a warm off-white.

Framing: medium close-up from chest up, eye-level, 9:16 vertical, subject's eyes on the upper third of the frame, the belt and the blanket edge visible in the lower third. Soft overcast afternoon light from camera-right as key, gentle shadow on the left side of her face, no hard highlights.

Style: photorealistic, shot on iPhone 15 Pro, shallow depth of field, natural skin texture with visible pores and slight under-eye softness, fine flyaway hair catching light, faint sensor grain, natural color grading slightly cool, no retouching.
```

### Last frame
```
Same 28-year-old Argentine woman, same chestnut wavy hair over her shoulders, same freckles and tired-eye softness, same heather-gray oversized t-shirt and charcoal sweatpants, same beige linen couch with same cream chunky knit blanket draped across her lower waist. Same pastel-pink heating belt with light gray strap visible above the blanket edge at her lower abdomen, same small circular LCD display, same small pink brand wordmark. Same Buenos Aires apartment living room behind her: same window with gauzy curtains and soft overcast afternoon light from camera-right, same ceramic beige mug on side table, same pothos plant upper-left, same floor lamp far left.

Differences from first frame: she is now leaning her head back gently against the back of the couch (more relaxed posture, less curled). Her previously-on-her-knee hand now rests open on the couch armrest, fingers relaxed. Her expression has shifted: brow smooth, mouth in a small warm closed-lip half-smile, eyes looking gently into the lens — calm relief, not exaggerated joy.

Framing unchanged: same medium close-up, eye-level, 9:16 vertical, eyes upper third, the belt in lower third. Same iPhone 15 Pro photorealistic style, same shallow DOF, same natural skin texture, same color grading.
```
**Qué cambia respecto al first frame:** (a) postura (acurrucada → cabeza apoyada); (b) mano libre (rodilla → reposabrazos); (c) expresión (ceño leve → sonrisa cerrada cálida). Resto idéntico.

## 5. Prompt de video

**Modelo:** Kling 3.0 (Pro mode)
**Audio nativo:** off — voz argentina se agrega en post con lipsync (Enhancor V4)
**Frames de referencia:** first + last
**Caracteres del prompt:** 2292 / 2500 (verificado con `wc -c`)

```
Multi-shot testimonial, 15s, 9:16 vertical. Subject, wardrobe, setting and pastel-pink heating belt (rounded pink body, gray fabric strap, small circular LCD display, brand wordmark in pink on the front) as shown in first frame reference. Maintain element consistency of subject and device throughout.

Shot 1 (0-5s): MCU as in reference, woman curled slightly forward on the couch with the cream knit blanket across her lower abdomen, the belt just visible above the blanket edge. Subtle organic handheld micro-sway. From 0.5s-4s her lips move in minimal conversational articulation synced to an off-camera voice track (no native audio generation). At 4s she lowers her right hand toward her abdomen, fingertips reaching under the blanket edge.

Shot 2 (5-10s): Cut to a tight close-up insert of her hands on the belt device — pastel pink belt body filling the frame, gray fabric strap visible to the sides. Her right thumb presses the top power button at 5.5s and the small circular LCD display lights up showing abstract heat-level and battery icons (no specific text). Camera slow 2cm push-in over the 5 seconds. At 7s her thumb taps a heat-up button, at 8s a vibration-mode button. Faint soft electronic beep on each press.

Shot 3 (10-15s): Cut back to MCU, same framing as Shot 1 but woman now leaning her head back against the couch, posture relaxed. At 10.5s she exhales softly, closes her eyes for half a second, opens them looking gently into the lens with a small warm closed-lip half-smile — matching last frame reference. From 11s-14.5s her lips move in minimal articulation synced to off-camera voice. The belt visible at her lower abdomen throughout.

Camera: subtle handheld micro-sway across all shots, cuts only between Shot 1->2 and Shot 2->3. Lighting as shown in reference: soft overcast afternoon daylight from camera-right.

Audio:
- Dialogue: NO native audio. Lips move minimally to off-camera voice (added in post with lipsync, Argentine Rioplatense Spanish).
- SFX (diegetic): soft fabric shift of the knit blanket; faint soft electronic beep at 5.5s, 7s and 8s on button presses; subtle exhale at 10.5s.
- Ambient: quiet apartment room tone, very faint distant traffic.
- Music: none.

Closing state: as shown in last frame reference.

Duration: 15s. 9:16 vertical.
```

## 6. Parámetros técnicos
- **Duración:** 15s
- **Aspect ratio:** 9:16
- **Resolución sugerida:** 1080p
- **Audio nativo:** off (voz argentina en post + lipsync con Enhancor V4)
- **Frames de referencia:** first + last
- **Modo (Kling):** Pro

## 7. Diálogo
- **Idioma + acento:** Español argentino (Rioplatense)
- **Modo de generación:** voz aparte + lipsync en post
- **Herramientas sugeridas:** grabación humana real con celular (mejor) o ElevenLabs/Play.ht. Lipsync con Enhancor V4 / Sync.so.
- **Línea 1 (0.5–4s, hook honesto, en Shot 1):** "Ya no le pido nada al ibuprofeno."
- **Línea 2 (5.5–9.5s, voice-over sobre close-up, Shot 2):** "Me pongo la faja, prendo el calor… y la vibración."
- **Línea 3 (11–13s, alivio íntimo, Shot 3):** "Y respiro. Te juro, respiro."
- **Línea 4 (13.5–14.5s, cierre, Shot 3):** "Esta faja. No vuelvo atrás."
- **Dirección de actuación:** voz femenina argentina ~28, conversacional íntima como hablándole a una amiga. Línea 1: cansancio honesto, casi suspiro en "ibuprofeno". Línea 2: pace calmo, listado suave, micro-pausa en "…" después de "calor". Línea 3: voz baja, confidencial, sonrisa apenas audible en "te juro". Línea 4: cierre seco y firme, sin tono publicitario. Cero locutora.
- **Alternativa línea 1 (si "ibuprofeno" no fluye bien en TTS):** "Ya no aguanto más la pastilla."

## 8. Notas de riesgo
- **La pantalla LCD circular de la faja puede renderizar gibberish.** Mitigación: el prompt pide solo "abstract heat-level and battery icons (no specific text)". No depende de números reales.
- **El logo de marca puede salir ilegible.** Mitigación: el nombre se dice en audio. Si querés legibilidad perfecta, overlay del logo real en post sobre el close-up.
- **Lipsync de Enhancor puede no calzar perfecto en Shot 1 o 3.** Mitigación: el prompt pide "minimal conversational articulation" para que tenga material. Si falla, regenerar la toma puntual. Shot 2 no requiere lipsync (close-up de manos).
- **Shot 1 puede salir demasiado "deprimido" y arruinar la conversión.** Mitigación: el prompt insiste en "honest, faint brow furrow… no dramatic pain, just real menstrual-day fatigue".
- **La faja puede cambiar tono de rosa entre Shot 1 y Shot 2.** Mitigación: first frame ancla el color; prompt repite "pastel-pink" en los 3 shots.

## 9. Flujo de producción
1. Generar first + last frame en Nano Banana usando los prompts de §4. Subir la imagen real del producto como referencia visual junto con el prompt de texto.
2. Pasar a Kling 3.0 Pro con ambos frames + el prompt de §5. Duración 15s, 9:16.
3. Generar la voz (las 4 líneas en una sola toma) — grabación humana argentina con celular o TTS multilingüe.
4. En Enhancor V4 → Lipsyncing → subir el video de Kling + el audio → Generate.
5. (Opcional) En CapCut: reemplazar SFX de beeps del Shot 2 si Kling no los puso bien; ajustar silencios entre líneas si hace falta.
