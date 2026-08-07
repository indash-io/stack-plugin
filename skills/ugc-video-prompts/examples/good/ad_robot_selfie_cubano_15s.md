# Ejemplo GOOD — Ad crash test dummy selfie cubano 15s (Kling 3.0 Pro, voz aparte)

**Input del usuario:**
> "Hacer un UGC de un robot filmándose en modo selfie, en una oficina, super realista, después el guion en español-cubano de 15 segundos. Marca: estudio jurídico de accidentes, marca telefónica tipo 1-800 (marca.com)."
> (+ imágenes de referencia del dummy: maniquí crash-test gris con traje azul marino y corbata celeste)

**Qué hace este ejemplo interesante:**
- Sujeto no-humano (crash test dummy) — forza a adaptar reglas de "skin realista" a "polymer realista".
- Español cubano con marcadores fuertes (asere, qué bolá, kilo, piñazo, mi socio) y aspiración de "s".
- Voz aparte obligatoria — el dummy no tiene lip-sync humano + Kling aluciona español regional.
- Articulación de mandíbula puppet-style (no humana), clave para el carácter.
- Prompt final: 1856 caracteres (bajo el cap de 2500).

---

# Paquete de video — Crash test dummy selfie — estudio jurídico (15s, cubano)

## 1. Análisis de escena
- **Tipo de contenido:** ad testimonial con humor deadpan + CTA telefónico
- **Sujeto principal:** ambos — crash test dummy en traje navy con corbata teal + iPhone selfie en mano (el CTA es la marca telefónica del estudio)
- **Plataforma:** TikTok / Reels / YouTube Shorts
- **Aspect ratio:** 9:16
- **Mood:** deadpan corporativo con humor cubano callejero — el dummy habla "tranqui" desde una oficina legit
- **Asumidos:** plataforma TikTok/Reels 9:16 (CTA telefónico de ad vertical); oficina corporativa diurna; voz masculina cubana 35-45 años; resolución 1080p; audio nativo **off**

## 2. Recomendación de modelo
**Elegido: Kling 3.0 (Pro mode)**

Razón: 15s single-shot continuo (selfie sin cortes) + consistencia crítica del dummy (traje, marker del temple, corbata) a lo largo de toda la toma = Kling Pro con Element Consistency + first/last frame. Veo 3.1 queda afuera por cap de 8s. Native audio **off** — el dummy no tiene lip-sync humano y el audio nativo de Kling aluciona en español regional; voz aparte en TTS.

## 3. Estructura
- **Shots:** single-shot, toma selfie continua de 15s (sin cortes)
- **Frames de referencia:** first + last
- **Razón first/last:** selfie a arm's length con un personaje no-humano + oficina con detalles finos = drift alto si dejamos solo texto. First ancla el hook con el dedo apuntando; last ancla el cierre con thumbs up y lean-in. Lighting e identidad del dummy idénticos en ambos.
- **Duración total:** 15s — ad testimonial con hook + beat + CTA + cierre, full de Kling
- **Aspect ratio:** 9:16

## 4. Prompts de Nano Banana

### First frame
```
A gray plastic crash test dummy mannequin — smooth matte gray polymer head with no facial expression, two minimal dark oval eye sockets, a narrow flat horizontal mouth slot, a visible black articulated metal neck joint at the base of the skull, a small round yellow-and-green circular marker sticker on the right temple. Faint scratches and scuff marks on the polymer surface from real use, subtle matte sheen, no plastic shine. Wearing a dark navy blue wool two-button suit jacket, crisp white dress shirt with pointed collar, bright teal-turquoise silk tie loosely knotted, gray plastic articulated hands with visible knuckle seams. Dummy holding a modern black iPhone 15 Pro in its right gray plastic hand at arm's length, screen facing itself, front-facing camera pointing at its own face — standard selfie framing. Free left hand entering the frame from the left side, gray plastic index finger pointing upward next to its own face in a "listen up" gesture.

Setting: modern corporate law office behind the dummy — a light oak wood desk slightly out of focus on the right with a silver MacBook open and a stack of beige manila folders, a dark brown leather executive office chair visible at the mid-right edge, a large green snake plant in a terracotta pot in the upper-left corner, a framed diploma with gold trim on the beige wall in the background. Soft diffused daylight from an off-frame window on camera-left, cool overhead fluorescent fill from above, subtle lens flare from the ceiling light.

Framing: medium selfie shot, subject fills central two-thirds of the frame, slight iPhone front-camera wide-angle distortion on the dummy's face (pinched at the edges), dummy's head tilted slightly down toward the phone, top edge of the iPhone just visible at the very bottom of the frame, 9:16 vertical.

Style: photorealistic, shot as if captured through an iPhone 15 Pro front camera, natural imperfection of a real handheld selfie (subtle motion blur at the hand extremities, slight auto-focus shift), realistic reflections on the gray polymer head, natural office color grading, no CGI sheen, no retouching, faint sensor grain.
```

### Last frame
```
Same gray plastic crash test dummy as in first frame reference — same navy blue wool suit, same white shirt, same teal silk tie, same yellow-green temple marker sticker, same black articulated neck joint, same polymer scratches and matte sheen. Same iPhone 15 Pro held selfie-style in its right gray plastic hand, same office background (light oak desk with MacBook and manila folders, leather chair, snake plant upper-left, framed diploma on beige wall), same soft diffused window light from camera-left with same overhead fluorescent fill, same slight wide-angle selfie distortion.

Differences from first frame: the dummy has leaned approximately 5cm closer to the phone (head fills slightly more of the frame). The left hand is now raised into the lower-center of the frame just below the dummy's chin, giving a clear thumbs-up gesture (gray plastic fist closed with the thumb extended straight up). Head tilted slightly more forward than in the first frame. Mouth slot closed.

Framing unchanged: medium selfie shot, 9:16 vertical, top edge of the iPhone just visible at the bottom. Same photorealistic iPhone 15 Pro front-camera style.
```
**Qué cambia respecto al first frame:** (a) mano izquierda baja del "índice hacia arriba" a "thumbs up abajo del mentón"; (b) dummy leaneado ~5cm más cerca del phone; (c) cabeza un poco más inclinada hacia adelante. Todo lo demás idéntico.

## 5. Prompt de video

**Modelo:** Kling 3.0 (Pro mode)
**Audio nativo:** off — el dummy no tiene lip-sync humano; Kling aluciona español regional; voz en post con TTS cubano
**Frames de referencia:** first + last
**Caracteres del prompt:** 1856 / 2500 (verificado con `wc -c`)

```
Selfie video, 15s, 9:16 vertical, single continuous take. Crash test dummy and corporate law office as shown in first frame reference. Maintain element consistency of dummy, suit, tie and office throughout 15 seconds.

From 0-3s: dummy stares flatly into the lens, zero expression. Left hand index finger points upward next to the face at 0.5s, holds 2 seconds, lowers out of frame at 2.5s. Subtle organic handheld micro-sway of the selfie arm throughout all 15 seconds.

From 3-8s: dummy's lower jaw opens and closes in minimal rigid puppet-style articulation — 5 or 6 small stiff jaw-drops synced to off-camera speech beats, ventriloquist motion, NOT human lip-sync, mouth slot opens only 5-8mm. Left hand re-enters and gestures twice with a small open-palm "you know" motion, at 5s and 7s. At 6s dummy tilts head 5 degrees right.

From 8-12s: head returns upright. From 9s to 11s left hand rises next to the ear in a "call me" gesture (gray plastic thumb and pinky extended, middle fingers curled), holds 2 seconds, lowers at 11s. Jaw continues rigid puppet articulation.

From 12-15s: dummy leans 5cm closer to the phone. Left hand enters lower-center of the frame at 13s in a clear thumbs-up gesture below the chin. Jaw does one last small stiff articulation at 14s, then closes. Dummy holds pose into 15s — matching last frame reference.

Camera: iPhone 15 Pro front-camera selfie feel, subtle handheld micro-sway, slight wide-angle face pinch, no cuts or pans. Lighting as shown in reference.

Audio:
- Dialogue: NO native audio. Jaw puppet-style only, no words (voice added in post, Cuban Spanish TTS).
- SFX (diegetic): office ambience, muffled keyboard typing, distant phone ring at 6s, soft HVAC hum.
- Ambient: quiet carpeted office room tone.
- Music: none.

Closing state: as shown in last frame reference.

Duration: 15s. 9:16 vertical.
```

## 6. Parámetros técnicos
- **Duración:** 15s
- **Aspect ratio:** 9:16
- **Resolución sugerida:** 1080p
- **Audio nativo:** off
- **Frames de referencia:** first + last
- **Modo (Kling):** Pro

## 7. Diálogo
- **Idioma + acento:** Español cubano (Caribeño, Miami-Cuban) — se genera aparte con TTS (ElevenLabs, voz masculina 35-45, energética pero con pausas).
- **Línea 1 (0.5–3s, hook):** "Asere, ¿qué bolá? Escucha esto."
- **Línea 2 (3.5–7.5s, beat principal):** "Yo me doy piñazos todo el día pa' que tú, si te chocan, no sueltes ni un kilo."
- **Línea 3 (8–12s, CTA):** "Llamame al <1-800-MARCA>. 18 años defendiendo al que no tiene la culpa."
- **Línea 4 (12.5–14.5s, cierre):** "Cero billete, completo. Dale, confía."
- **Dirección de actuación para TTS:** voz masculina cubana confiada y relajada, ritmo rápido caribeño con aspiración de "s" final ("e'cucha", "piñazo'"), entonación ascendente al final de frase con caída rápida, sonrisa audible en "asere" y "dale", medio tono más grave en el CTA para gravitas legal, una respiración natural entre línea 2 y 3. Cero lectura "locutor" — conversacional.
- **Alternativa línea 2 (si "ni un kilo" no amplía bien fuera de Cuba):** "…no sueltes ni un peso."

## 8. Notas de riesgo
- **Articulación de mandíbula del dummy puede salir humana (mala) o totalmente estática (peor).** **Mitigación:** el prompt repite "ventriloquist-dummy motion, NOT human lip-sync, mouth slot opens only 5-8mm". Si igual sale mal: plan B = mouth totalmente cerrada fija los 15s + subtítulos cubanos grandes sobre el video en edición (estilo UGC de Miami típico, incluso suma).
- **Element consistency del dummy en 15s continuos es exigente.** El marker amarillo-verde del temple o la corbata teal pueden mutar. **Mitigación:** first y last frame anclan extremos; Pro mode ayuda. Si drifta: regenerar con seed distinto o partir el clip en 2.
- **iPhone 15 Pro en la mano de plástico puede renderizar deforme.** **Mitigación:** el first frame es clave — si Nano Banana ya genera la mano sosteniendo bien el phone, Kling lo mantiene; si Nano Banana falla, regenerar first frame hasta que la grip sea creíble antes de pasarlo a Kling.
- **La oficina puede leer "genérica AI-slop" si los detalles no se mantienen.** **Mitigación:** el prompt nombra objetos concretos (MacBook, carpetas manila, planta snake, diploma enmarcado); si aun así sale vacía, regenerar first frame con más densidad de props.
