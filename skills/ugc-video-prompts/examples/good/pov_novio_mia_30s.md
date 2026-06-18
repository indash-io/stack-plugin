# Ejemplo GOOD — POV novio desesperado encuentra Mia 30s (split en 2 clips Kling Pro + lipsync)

**Input del usuario:**
> Guión completo (~28s de habla rápida argentina):
> 1. "Día 5 buscando un BUEN regalo para el cumpleaños de mi novia, porque sino me raja de casa."
> 2. "Ya fallamos con perfumes, un serum que 'no era el que usaba', y un desayuno en la cama. Pero anoche me encontré ESTO mientras miraba instagram."
> 3. "Es como un coso que básicamente le pone calor y masaje en la panza cuando le duele el período."
> 4. "Porque ella pasa de estar dos días tirada en cama muerta del dolor, a ponerse este coso, sentir el calorcito y la vibración, y seguir con su día normal. Como si nada."
> 5. "Se lo regalé, lo probó, y... funcionó. La verdad no esperaba clavarla con esto, pero LO RE USA."
> 6. "Si te interesa hacerle un buen regalo, hacé click acá abajo que lo conseguí en oferta."

**Qué hace este ejemplo interesante:**
- **Video de 30s** — supera el cap de 15s de Kling. Resuelto con **split en 2 clips Kling Pro de 15s** pegados en CapCut con corte seco.
- **Continuidad inter-clip crítica:** mismo actor + mismo wardrobe + mismo setting + misma luz + mismo color grading entre los 2 clips, para que el corte se sienta intencional y no chapucero.
- **Cast masculino** — diferente patrón al testimonial femenino estándar; gestos físicos exagerados al estilo POV humorístico argentino.
- **4 imágenes Nano Banana** (first + last por cada clip) para anclar ambos extremos de ambos clips.
- **Voz aparte + lipsync** porque diálogo argentino + Kling.
- **Beat clave entre clips:** Clip 1 termina con el actor sosteniendo el celular (encontrado en IG); Clip 2 arranca con el actor sosteniendo Mia física (ya lo tiene). El "salto temporal" es narrativamente claro.
- Prompts: Clip 1 = 2217 chars, Clip 2 = 2141 chars (ambos bajo cap 2500, verificados con `wc -c`).

---

# Paquete de video — Novio desesperado encuentra Mia (30s, 2 clips Kling)

## 1. Análisis de escena
- **Tipo de contenido:** ad POV humorístico (novio buscando regalo, encuentra Mia, "clavó la sorpresa")
- **Sujeto principal:** ambos — hombre argentino ~30 + Mia (faja eléctrica rosa pastel)
- **Plataforma:** TikTok / Reels (POV explicativo 30s funciona muy bien acá)
- **Aspect ratio:** 9:16
- **Mood:** desesperado-feliz, autoconsciente, humor argentino casual hogareño — "tipo que te está contando algo bueno mientras se ríe de sí mismo"
- **Asumidos:** cast hombre 30 castaño barba leve; setting living/cocina abierta de departamento argentino; audio nativo **off** (voz aparte + lipsync); resolución 1080p

## 2. Recomendación de modelo
**Elegido: Kling 3.0 (Pro mode), 2 clips de 15s pegados en edición**

Razón: el guión es de ~25-28s, supera el cap duro de 15s de Kling. Veo 3.1 queda afuera por su cap de 8s. Única vía: split en 2 clips Kling y pegarlos en CapCut con corte seco. Pro mode crítico porque hay que mantener identidad del actor + producto + setting idénticos entre los 2 clips (Element Consistency inter-clip). Audio nativo **off** (Kling aluciona español argentino; voz aparte + lipsync en Enhancor V4).

## 3. Estructura
- **Total:** 2 clips × 15s = 30s
- **Clip 1 (0–15s):** Setup → hook (día 5 de búsqueda) → flashback de fracasos → encuentra Mia en Instagram
- **Clip 2 (15–30s):** Solución → explica el producto → resultado con la novia → CTA "link abajo"
- **Single-shot por clip** (cámara fija con micro-sway, sin cortes intra-clip — más controlable)
- **Frames de referencia:** first + last **para cada clip** (4 imágenes Nano Banana en total)
- **Continuidad inter-clip:** mismo wardrobe + mismo setting + misma luz + mismo color grading. Transición narrativa lógica: termina Clip 1 con celular en mano (encontrado en IG) → arranca Clip 2 con Mia física (ya lo regaló).
- **Aspect ratio:** 9:16

## 4. Prompts de Nano Banana

### Clip 1 — First frame
```
30-year-old Argentine man, short tousled dark brown hair, three-day stubble (not a full beard, just light scruff), fair skin with natural texture and faint laugh lines around the eyes, dark brown eyes, wearing an oversized heather-gray cotton crewneck t-shirt slightly worn at the neckline. Standing in his living room/kitchen, one hand raised to the side of his head fingers loosely splayed in a "what am I gonna do" exasperated gesture, the other hand relaxed at his side. Expression: tired-amused, slight raised eyebrow on one side, mouth in a half-open mid-speech shape, eyes locked on the camera with a "you won't believe me" look — comedic-honest, not dramatic.

Setting: open-plan Buenos Aires apartment living-kitchen behind him — a low beige linen couch with two scattered throw pillows visible mid-frame, an open kitchen island on the right with a yerba mate gourd and metal bombilla on the counter, a hanging pothos plant trailing from a wooden shelf on the upper-left, a small framed couple's photo on the same shelf, warm off-white walls. Light wood floor.

Framing: medium close-up from mid-chest up, eye-level, 9:16 vertical, subject's eyes upper third of the frame, breathing room on both sides showing the setting. Soft warm late-afternoon natural light from camera-right (off-frame window), gentle shadow on the left side of his face.

Style: photorealistic, shot on iPhone 15 Pro front camera with subtle handheld feel, shallow depth of field on the background, natural skin texture with visible pores and fine stubble detail, slight asymmetry in features, faint sensor grain, natural color grading slightly warm, no retouching.
```

### Clip 1 — Last frame
```
Same 30-year-old Argentine man, same short tousled dark brown hair, same three-day stubble, same heather-gray oversized t-shirt, same living-kitchen setting (beige couch, mate on kitchen island, hanging pothos, framed couple's photo), same warm late-afternoon light from camera-right.

Differences from first frame: he is now holding a modern black smartphone in his right hand, raised up to about chin level next to his face, screen tilted slightly toward the camera. On the phone screen, visible is an abstract Instagram-feed-style layout with a rounded pastel-pink product shape centered in a card (no specific text or recognizable logos — just the abstract suggestion of a product post). His left hand is no longer raised to his head; it's now relaxed at his side. His expression has shifted: eyebrows raised in a "found it" look, mouth just-closed after speaking, faint amused smile starting at one corner.

Framing unchanged: same medium close-up, same eye-level, 9:16 vertical, same composition. Same iPhone 15 Pro photorealistic style, same DOF, same skin texture, same color grading.
```
**Qué cambia respecto al Clip 1 first:** (a) mano derecha levanta smartphone con pantalla mostrando feed de IG con producto rosa abstracto; (b) mano izquierda baja al costado; (c) expresión pasa de "exasperación" a "lo encontré". Resto idéntico.

### Clip 2 — First frame
```
Same 30-year-old Argentine man as in Clip 1 reference frames — same short tousled dark brown hair, same three-day stubble, same heather-gray oversized cotton t-shirt, same warm fair skin. Same open-plan Buenos Aires apartment living-kitchen behind him (beige couch, kitchen island with mate gourd, hanging pothos, framed couple's photo on the shelf, warm off-white walls, light wood floor). Same warm late-afternoon natural light from camera-right with the same shadow pattern on the left side of his face.

Differences from Clip 1: instead of the smartphone, he is now holding the Mia heating belt device in his right hand at mid-chest height, presented toward the camera. Mia is a pastel-pink rounded rectangular plastic body with a small circular dark LCD display in the center (off, dark), a small pink "Lumy" wordmark on the front face below the display, and a light gray adjustable fabric strap dangling from one end. His left hand is relaxed at his side. His expression: animated, eyebrows raised, mouth open mid-speech, eyes on the camera with a "let me explain this" energy.

Framing unchanged: same medium close-up from mid-chest up, eye-level, 9:16 vertical, eyes upper third, Mia visible mid-frame in front of his torso. Same iPhone 15 Pro photorealistic style, same DOF, same skin texture, same color grading.
```

### Clip 2 — Last frame
```
Same 30-year-old Argentine man, same hair stubble t-shirt setting and lighting as in Clip 2 first frame. Mia heating belt still in the picture but now held lower, against the left side of his chest with his left hand (cradled, no longer presented forward). Same pastel-pink body, same circular LCD, same "Lumy" wordmark.

Differences from Clip 2 first: (a) Mia switched from right hand presented to left hand held against chest; (b) his right hand now extends in front of his torso with index finger pointing downward in a clear "link below" gesture; (c) his expression closed-lip smug half-smile, slight raised eyebrow, eyes locked on the camera with a "trust me on this" look.

Framing unchanged: medium close-up, eye-level, 9:16 vertical, breathing room on both sides. Same iPhone 15 Pro photorealistic style.
```
**Qué cambia respecto a Clip 2 first:** Mia pasa de presentado adelante a apoyado en el pecho; mano derecha apunta hacia abajo (gesto link); expresión cierra con sonrisa pícara.

## 5. Prompts de video

**Modelo:** Kling 3.0 (Pro mode) para los 2 clips
**Audio nativo:** off — voz argentina se agrega en post con lipsync (Enhancor V4)
**Frames de referencia:** first + last para cada clip

### Clip 1 (0–15s del video final)
**Caracteres:** 2217 / 2500 (verificado con `wc -c`)

```
Single-shot POV testimonial, 15s, 9:16 vertical. Subject, wardrobe, setting and lighting as shown in Clip 1 first frame reference. Maintain element consistency of the man, his t-shirt, the apartment setting and the warm late-afternoon side light throughout the full 15 seconds.

From 0-3s: man stands as in first frame reference, right hand raised to the side of his head in an exasperated "what am I gonna do" gesture. Lips move in minimal conversational articulation synced to off-camera voice (no native audio). Subtle organic handheld micro-sway throughout.

From 3-9s: he lowers his right hand from his head. With expressive movement he counts three items on his fingers — at 4s the index finger goes up (gesture "one"), at 6s the middle finger joins (gesture "two"), at 7.5s the ring finger joins (gesture "three"). Brief facial micro-reactions between each: a small wince at 5s (the failed serum), a flat smirk at 6.5s (failed breakfast), an exhale at 8s. Lips continue articulating to off-camera voice.

From 9-12s: his right hand reaches off-frame to the side and returns at 10s holding a modern black smartphone, raises it up to chin level next to his face, screen tilted slightly toward the camera. On the phone screen: an abstract Instagram-feed card with a rounded pastel-pink product shape in the center (no specific text). He glances at the phone at 10.5s, then back to the lens at 11.5s with raised eyebrows.

From 12-15s: he holds the phone steady at chin height, expression settling into a "found it" amused look — eyebrows raised, mouth just closed after a final word, faint smile at one corner. Matches Clip 1 last frame reference at 14.5-15s.

Camera: handheld feel with subtle organic micro-sway, no cuts, single continuous take. Lighting as shown in reference throughout.

Audio:
- Dialogue: NO native audio. Lips articulate minimally to off-camera voice track (added in post with lipsync, Argentine Rioplatense Spanish).
- SFX (diegetic): soft cotton t-shirt fabric shifts; faint distant ambient sounds of an apartment (very low refrigerator hum).
- Ambient: quiet apartment room tone.
- Music: none.

Closing state: as shown in Clip 1 last frame reference.

Duration: 15s. 9:16 vertical.
```

### Clip 2 (15–30s del video final)
**Caracteres:** 2141 / 2500 (verificado con `wc -c`)

```
Single-shot POV testimonial, 15s, 9:16 vertical. Same man, wardrobe, setting, lighting and color grading as shown in Clip 1 reference frames — heather-gray oversized t-shirt, open-plan apartment living-kitchen behind, warm late-afternoon light from camera-right. Maintain element consistency throughout.

Holding pastel-pink Mia heating belt in right hand at mid-chest as shown in Clip 2 first frame reference (pink rounded body, small circular LCD, "Lumy" wordmark, gray fabric strap dangling).

From 0-7s: he holds Mia presented forward, slightly rotates it 15 degrees back and forth to show it. At 2s small "tired collapsed" gesture with his free left hand (palm down low, like "two days in bed"). At 4s he taps the surface of Mia twice with his left index finger (gesture "calor"), at 5s makes a tiny vibrating motion with left fingers (gesture "vibración"). At 6.5s a small "como si nada" smirk with one eyebrow up. Lips move in minimal conversational articulation synced to off-camera voice throughout (no native audio).

From 7-12s: he lowers Mia to chest level cradled in left hand. At 8s a small head nod ("regalé"). At 9s another nod ("probó"). At 10s eyebrows raise and a half-amused smile starts ("funcionó"). At 11s eyebrows raise higher with mouth open in mock-surprise on the beat of "LO RE USA". Lips continue minimal articulation to off-camera voice.

From 12-15s: he extends right index finger pointing downward in a clear "link below" gesture. Settles into a closed-lip smug half-smile with raised eyebrow and direct eye contact into the lens — matching Clip 2 last frame reference at 14.5-15s.

Camera: subtle handheld micro-sway, no cuts, single continuous take.

Audio:
- Dialogue: NO native audio. Lips articulate minimally to off-camera voice (added in post with lipsync, Argentine Rioplatense Spanish).
- SFX (diegetic): soft cotton t-shirt fabric shifts; faint finger taps on the plastic body of Mia at 4s and 5s.
- Ambient: quiet apartment room tone, very faint refrigerator hum continuing from Clip 1.
- Music: none.

Closing state: as shown in Clip 2 last frame reference.

Duration: 15s. 9:16 vertical.
```

## 6. Parámetros técnicos
- **Duración:** 30s total (Clip 1: 15s + Clip 2: 15s, pegados con corte seco en CapCut)
- **Aspect ratio:** 9:16
- **Resolución sugerida:** 1080p
- **Audio nativo:** off (voz argentina en post + lipsync con Enhancor V4)
- **Frames de referencia:** first + last por cada clip (4 imágenes Nano Banana)
- **Modo (Kling):** Pro

## 7. Diálogo
- **Idioma + acento:** Español argentino (Rioplatense)
- **Modo de generación:** voz aparte + lipsync en post
- **Herramientas sugeridas:** grabación humana real (recomendada — autenticidad POV) o ElevenLabs/Play.ht. Lipsync con Enhancor V4 / Sync.so.
- **Clip 1 (audio 0–15s):**
  - **L1 (0.5–3.5s, hook):** "Día 5 buscando un BUEN regalo para el cumpleaños de mi novia, porque sino me raja de casa."
  - **L2 (4–9.5s, flashback fracasos):** "Ya fallamos con perfumes, un serum que 'no era el que usaba', y un desayuno en la cama. Pero anoche me encontré ESTO mientras miraba instagram."
  - **L3 (10–14s, bridge):** "Es como un coso que básicamente le pone calor y masaje en la panza cuando le duele el período."
- **Clip 2 (audio 15–30s):**
  - **L4 (0–7s del Clip 2 = 15–22s, explicación):** "Porque ella pasa de estar dos días tirada en cama muerta del dolor, a ponerse este coso, sentir el calorcito y la vibración, y seguir con su día normal. Como si nada."
  - **L5 (7.5–11.5s del Clip 2 = 22.5–26.5s, resultado):** "Se lo regalé, lo probó, y... funcionó. La verdad no esperaba clavarla con esto, pero LO RE USA."
  - **L6 (12–14.5s del Clip 2 = 27–29.5s, CTA):** "Si te interesa hacerle un buen regalo, hacé click acá abajo que lo conseguí en oferta."
- **Dirección de actuación:** voz masculina argentina ~30, energía "desesperado-aliviado-amigo". Pace rápido (formato POV trending). Énfasis fuerte en "BUEN", "ESTO", "LO RE USA". Sonrisa audible en "como si nada" y en el CTA. Cero locutora, full conversacional. Pausas naturales entre L1-L2 y L3-L4 para el corte de clips.
- **Alternativa L4 (si se aprieta el timing):** acortar a "Pasa de estar dos días tirada del dolor, a ponérselo, sentir el calorcito y la vibración, y seguir como si nada."

## 8. Notas de riesgo
- **Continuidad inter-clip puede romperse** — wardrobe o luz o color grading distintos entre Clip 1 y Clip 2 hace que el corte se sienta chapucero. **Mitigación:** los 4 prompts de Nano Banana y los 2 prompts de video repiten textualmente "same heather-gray oversized t-shirt", "same warm late-afternoon natural light from camera-right", "same color grading". Si igual drifta, regenerar el Clip 2 hasta matchear.
- **El smartphone en Clip 1 last puede renderizar mal** — pantalla con texto raro, layout distorsionado. **Mitigación:** el prompt pide "abstract Instagram-feed-style layout with a rounded pastel-pink product shape (no specific text or recognizable logos)". Si igual sale feo, en post hacer un overlay de captura real de IG con el producto.
- **Mia en Clip 2 puede cambiar de color de rosa** vs lo que se ve en el celular en Clip 1 last. **Mitigación:** ambos prompts usan "pastel-pink rounded body". Si drifta, regenerar Clip 2.
- **Lipsync de Enhancor puede no calzar perfecto** en los 2 clips. **Mitigación:** ambos prompts piden "minimal conversational articulation" para que el lipsync tenga material visual. Si falla en alguna sección puntual, regenerar solo esa sección.
- **El gesto de "calor y vibración" en Clip 2 (4-5s) puede salir confuso** — el actor solo toca el producto. **Mitigación:** las direcciones son específicas ("taps Mia twice with left index finger" / "tiny vibrating motion with left fingers"). Si igual sale ambiguo, agregar texto overlay "calor + vibración" en post.

## 9. Flujo de producción
1. **Nano Banana ×4:** generar Clip 1 first, Clip 1 last, Clip 2 first, Clip 2 last. Subir la imagen real del producto Mia como referencia visual junto con los prompts de Clips 2.
2. **Kling 3.0 Pro ×2:** generar Clip 1 (con sus 2 frames) y Clip 2 (con sus 2 frames). 15s cada uno, 9:16.
3. **Voz:** generar las 6 líneas en una sola toma (o 2 tomas, una por clip) — grabación humana argentina con celular (mejor para autenticidad POV) o TTS argentino.
4. **Enhancor V4 / Sync.so ×2:** aplicar lipsync a cada clip con su porción de audio.
5. **CapCut:** pegar los 2 clips con corte seco entre 14.99s y 15s. Sin transición fade. Agregar subtítulos grandes argentinos sobre el video (típico de POV TikTok/Reels) — opcional pero suma conversión.
6. **Overlays opcionales:** si la pantalla del celular en Clip 1 last salió fea, overlay de IG real. Si el gesto "calor + vibración" en Clip 2 quedó ambiguo, overlay de texto.
