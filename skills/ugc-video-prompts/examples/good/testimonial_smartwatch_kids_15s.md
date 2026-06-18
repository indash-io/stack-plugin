# Ejemplo GOOD — Testimonial mamá smartwatch infantil 15s (Kling 3.0 multi-shot)

**Input del usuario:**
> "Quiero hacer en español argentino, una chica hablando mostrando el producto, de 35 años, 15 segundos, el resto hacelo por default."
> (+ imagen de referencia del producto: Panda Watch PRO — smartwatch infantil, case rosa + correa negra, pantalla con cartoon. Landing: pandakidslab.com.ar)

---

# Paquete de video — Mamá argentina testimonial Panda Watch PRO (15s)

## 1. Análisis de escena
- **Tipo de contenido:** testimonial + micro-demo (mamá hablando a cámara, mostrando el producto)
- **Sujeto principal:** ambos — mujer argentina 35 años (madre) + Panda Watch PRO (smartwatch infantil rosa con correa negra)
- **Plataforma:** TikTok / Reels (default)
- **Aspect ratio:** 9:16
- **Mood:** íntimo confesional, matutino, honesto — tono "mamá que le habla a otra mamá en la cocina"
- **Asumidos:** TikTok/Reels 9:16; mood testimonial cálido-honesto; setting cocina/living hogareño argentino; cast mujer 35, castaña, maquillaje mínimo; resolución 1080p

## 2. Recomendación de modelo
**Elegido: Kling 3.0 (Pro mode)**

Razón: 15s + 3 tomas narrativamente conectadas + el mismo reloj tiene que leerse idéntico en los 3 planos → **Element Consistency + Multi-Shot Storytelling de Kling**. Veo 3.1 queda afuera por cap duro de 8s. Pro mode por densidad técnica y beats cronometrados.

## 3. Estructura
- **Shots:** multi-shot, 3 tomas conectadas
  - Shot 1 (0–5s): MCU mamá, hook a cámara, reloj en la palma
  - Shot 2 (5–10s): insert close-up del reloj (pantalla + botón SOS + cámara frontal)
  - Shot 3 (10–15s): pull-out a MCU mamá, cierre y apoya el reloj en la mesa
- **Frames de referencia:** first + last
- **Razón first/last:** producto con pantalla y detalles chicos es alto riesgo de drift visual en 15s. First ancla el hook; last ancla el packshot final con el reloj en frame y el mismo lighting — evita drift de color/forma.
- **Duración total:** 15s — testimonial multi-shot, máximo de Kling, permite hook + beat + cierre sin atropellar diálogo
- **Aspect ratio:** 9:16

## 4. Prompts de Nano Banana

### First frame
```
35-year-old Argentine woman, mid-length wavy chestnut brown hair with a few subtle grays at the temples loosely tucked behind one ear, fair skin with natural texture, visible pores and a light scatter of freckles across the nose bridge, small thin gold hoop earrings, minimal natural makeup with a hint of tinted lip balm. Wearing an oversized heather-gray cotton crewneck sweatshirt, sleeves pushed to mid-forearm. Sitting at a light oak wooden kitchen table, elbows resting on the surface, her right hand holding a kids' smartwatch in her open palm at chest height, slightly angled toward the camera. The smartwatch: square pink plastic case with a black silicone band draped over her fingers, small front-facing camera at the top-left of the bezel, a pink SOS side button, bright square LCD screen showing a simple colorful cartoon puppy on a coral-pink background. Background: warm beige kitchen wall slightly out of focus, a wooden open shelf with a small terracotta plant and a framed crayon child's drawing on the top-left of the frame, a half-full ceramic mug of coffee on the right. Soft warm morning window light from camera-left, gentle shadow on the right side of her face, no hard highlights. Medium close-up, eye-level, 9:16 vertical framing, subject's eyes on the upper third, watch visible in lower third. Shot on iPhone 15 Pro, photorealistic, shallow depth of field, natural skin texture with visible pores and slight asymmetry, fine facial hair catching light on the upper lip, subtle film grain, no retouching.
```

### Last frame
```
Same 35-year-old Argentine woman, same chestnut wavy hair tucked behind ear, same freckles and minimal makeup, same heather-gray oversized crewneck sweatshirt, same light oak kitchen table, same background (beige wall, shelf with terracotta plant, framed crayon drawing, ceramic mug). Same soft warm morning window light from camera-left with the same shadow pattern on the right side of her face. She has just set the pink-and-black kids' smartwatch flat on the table in front of her, screen facing up and tilted slightly toward the camera. Her right hand rests next to the watch, fingers relaxed. She looks directly into the lens with a small, warm, closed-lip half-smile, chin slightly lowered. Same framing: medium close-up, eye-level, 9:16 vertical, eyes upper third, watch in lower third now flat on the table instead of in her palm. Same shot on iPhone 15 Pro, same shallow depth of field, same natural skin texture, same film grain.
```
**Qué cambia respecto al first frame:** el reloj pasa de estar en la palma abierta a estar apoyado plano sobre la mesa (packshot suave); expresión pasa de neutral-curiosa a sonrisa cerrada cálida; el resto es idéntico para que Kling no reinterprete wardrobe, luz ni setting.

## 5. Prompt de video

**Modelo:** Kling 3.0 (Pro mode)
**Audio nativo:** off — el diálogo se genera aparte con TTS argentino (ElevenLabs). Kling 3.0 aluciona diálogo en español regional; mejor mantenerlo muteado y pegarlo en edición.
**Frames de referencia:** first + last

```
Multi-shot testimonial, 15s, 9:16. Subject, wardrobe, setting, lighting and smartwatch (pink case, black silicone band, coral-pink screen with cartoon puppy, pink SOS side button) as shown in first frame reference. Maintain element consistency of the watch across all shots.

Shot 1 (0–5s): MCU as in reference, watch in her open right palm. Subtle handheld micro-sway. She glances at the watch for half a second, then up to the lens. Her lips move in minimal conversational articulation from 1s–5s, synced to an off-camera voice track (no native audio generation). At 4.5s she tilts the watch toward the lens.

Shot 2 (5–10s): Cut to tight close-up insert of the watch held between her thumb and index finger, screen sharp, fingers in soft focus. Slow 3cm push-in over 5s. At 7s her thumb taps the pink SOS side button — faint plastic click.

Shot 3 (10–15s): Cut back to MCU, camera slightly wider (~20cm pulled back). She sets the watch flat on the wooden table (soft wood tap at 10.5s), hand resting beside it, looks into the lens with a closed-lip half-smile. Lips move in minimal articulation from 11s–14s, synced to off-camera voice track. From 14s–15s she holds the small smile — matching last frame reference.

Audio:
- Dialogue: NO native audio generation. Voice added in post-production with Argentine Rioplatense TTS (ElevenLabs).
- Diegetic SFX: faint plastic click on SOS button at 7s; soft wood tap when watch is set on table at 10.5s; subtle fabric shift of sweatshirt sleeves.
- Ambient: quiet morning kitchen room tone, faint distant street murmur.
- Music: none.

Closing state: as shown in last frame reference.

Duration: 15s. 9:16 vertical.
```

## 6. Parámetros técnicos
- **Duración:** 15s
- **Aspect ratio:** 9:16
- **Resolución sugerida:** 1080p
- **Audio nativo:** off (voz en post con TTS argentino; SFX nativos de Kling pueden quedar si salen bien, si no, también en post)
- **Frames de referencia:** first + last
- **Modo (Kling):** Pro

## 7. Diálogo
- **Idioma + acento:** Español argentino (Rioplatense) — se genera aparte con TTS. NO se pide a Kling que lo genere.
- **Línea 1 (0.5–5s, hook):** "Che, me preguntan mil veces qué reloj le compré a Mateo…"
- **Línea 2 (5.5–9.5s, beat features, voice-over sobre close-up):** "Mirá — GPS, videollamadas, botón de SOS, y lo bloqueo cuando está en la escuela."
- **Línea 3 (11–14s, cierre):** "Panda Watch PRO. Dejé de estar pendiente del celu, te juro."
- **Dirección de actuación para TTS:** voz femenina argentina 35, conversacional cálido como hablándole a una amiga en la cocina. Mid-volume en hook, pace más rápido y listado en línea 2, voz más baja y confidencial en cierre. Sonrisa audible en "te juro". Sin tono publicitario.
- **Alternativa (si el nombre "Mateo" no matchea al cliente):** "Che, me preguntan mil veces qué reloj le compré al nene…"

## 8. Notas de riesgo
- **Articulación labial puede desincronizar del voice-over pegado en post.** Al no usar native audio, los labios de la mamá se mueven genéricamente. **Mitigación:** en edición, alinear picos de apertura labial con sílabas fuertes del TTS; si drifta, agregar un corte de producto (Shot 2) más largo para tapar el desfase visual.
- **Consistencia del reloj entre Shot 1 y Shot 2.** Element Consistency puede derivar en color/forma. **Mitigación:** first y last frame anclan los extremos + prompt repite la descripción del reloj. Si aun así drifta, generar Shot 2 por separado con su propio first frame (close-up del reloj) y pegar en edición.
- **Texto en la pantalla del reloj puede renderizar ilegible.** **Mitigación:** el prompt pide solo "cartoon puppy on coral-pink background" (sin números ni logos). El nombre de marca va por el TTS, no depende de lectura visual.
- **15s con 3 cortes puede acelerarse si el modelo no respeta timing.** **Mitigación:** cada shot tiene rango explícito; si igual se apura, bajar a 12s y sacar la frase final de Shot 1.
