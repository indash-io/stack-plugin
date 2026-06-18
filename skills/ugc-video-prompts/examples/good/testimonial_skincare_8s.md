# Ejemplo GOOD — Testimonial skincare 8s (Veo 3.1)

**Input del usuario:**
> "Armame un testimonial UGC de una mujer joven argentina mostrando un serum facial, para TikTok, 8 segundos, con diálogo."

---

# Paquete de video — Testimonial skincare matutino

## 1. Análisis de escena
- **Tipo de contenido:** testimonial
- **Sujeto principal:** persona (mujer argentina ~25) + producto (serum facial amber glass)
- **Plataforma:** TikTok
- **Aspect ratio:** 9:16
- **Mood:** íntimo confesional, matutino, sin pretensión
- **Asumidos:** acento argentino (default), resolución 1080p, mujer 25-30 (ajustar si necesitás otro cast)

## 2. Recomendación de modelo
**Elegido: Veo 3.1**

Razón: testimonial con diálogo a cámara dentro del cap de 8s. Lip-sync preciso es crítico → Veo 3.1 es superior a Kling 3.0 en este caso. Multi-shot no se necesita; movimiento simple.

## 3. Estructura
- **Shots:** single-shot continuo
- **Frames de referencia:** solo first frame
- **Razón first/last:** la acción es continua (habla + aplica gota), no hay transformación ni reveal que justifique last frame
- **Duración total:** 8s — una frase corta + aplicación del producto entran cómodo sin rellenar
- **Aspect ratio:** 9:16

## 4. Prompts de Nano Banana

### First frame
```
25-year-old Argentine woman, curly dark brown hair pulled into a loose low bun with two face-framing strands, no makeup, natural skin with faint freckles across the cheekbones and a small asymmetry in the eyebrows, wearing an oversized cream cotton sweatshirt slightly pulled up at the right shoulder. She holds a 30ml amber glass serum bottle with a white dropper cap between her thumb and index finger, close to the right side of her jawline. Her gaze is directed straight into the lens with a soft curious micro-smile — lips just barely parted. Her bedroom in morning: unmade white linen bed slightly blurred behind her, a small beige ceramic table lamp on the right edge of the frame, a green pothos plant leaf visible top-left corner. Soft warm morning window light from camera-left, gentle shadow on the right side of her face, no practicals. Medium close-up from mid-chest up, eye-level, 9:16 vertical framing, eyes placed at the upper third of the frame. Shot on iPhone 15 Pro, photorealistic, shallow depth of field, natural skin texture with visible pores and a faint sheen on the forehead, subtle film grain, no retouching.
```

### Last frame
N/A — el video es movimiento continuo sin necesidad de anclar estado final.

## 5. Prompt de video

**Modelo:** Veo 3.1
**Audio nativo:** on — diálogo a cámara necesita lip-sync
**Frames de referencia:** first

```
Medium close-up, 50mm lens, eye-level. As shown in reference: 25-year-old Argentine woman with curly dark brown hair in a loose low bun, no makeup, oversized cream cotton sweatshirt, holding a 30ml amber glass serum bottle with a white dropper cap near the right side of her jawline.

From 0-4s: she looks directly into the lens, tilts her head slightly left, and says in Argentine Spanish (Rioplatense accent): "Mirá qué rápido se absorbe este serum, te juro que no lo podía creer."

(Delivery: whispered-conversational, as if telling a close friend a small discovery. Slight smile on "rápido". No exaggeration, no pitch rise at the end.)

From 4-7s: she unscrews the dropper cap with her right hand — subtle click. A single drop of clear amber serum forms at the dropper tip. She presses the drop onto her right cheekbone and does two small circular rubs with her ring finger.

From 7-8s: she closes her eyes for a half-beat, opens them looking down at the bottle with a small satisfied exhale.

Camera: static hold for the first 4 seconds, then a subtle 8cm handheld push-in from 4s to 8s with organic micro-shake.

Lighting: soft warm morning window light from camera-left as key, white-wall bounce from camera-right as fill, no practicals. Shallow depth of field, background bedroom slightly blurred.

Sound: diegetic only — soft cotton sweatshirt rustle, faint dropper click at 4s, fingertip-on-skin sound at 5-6s, quiet room tone throughout. No music.

Duration: 8 seconds. 9:16 vertical.
```

## 6. Parámetros técnicos
- **Duración:** 8s
- **Aspect ratio:** 9:16
- **Resolución sugerida:** 1080p
- **Audio nativo:** on
- **Frames de referencia:** first
- **Modo:** N/A (Veo 3.1 no tiene modos)

## 7. Diálogo
- **Idioma + acento:** Español (argentino, Rioplatense)
- **Línea:** "Mirá qué rápido se absorbe este serum, te juro que no lo podía creer."
- **Dirección de actuación:** whispered-conversational, como si le contara a una amiga un descubrimiento chico. Sonrisa leve en "rápido". Sin exageración, sin subir el tono al final.
- **Alternativa:** "Mirá, te muestro el que me cambió la piel en dos semanas." (si querés más promesa explícita)

## 8. Notas de riesgo
- **Qué puede salir mal en el primer intento:**
  1. Lip-sync puede desincronizar en "absorbe" (doble consonante fuerte).
  2. Veo puede acelerar la aplicación del producto si no reiteramos timing.
  3. La gota de serum puede salir muy grande o con textura irreal.
- **Cómo mitigarlo si pasa:**
  1. Regenerar 2-3 veces; si persiste, acortar a "Mirá qué rápido se absorbe." y cortar el resto de la frase.
  2. Agregar "slowly, taking the full 3 seconds from 4s to 7s" al beat de aplicación.
  3. Cambiar "a single drop of clear amber serum forms at the dropper tip" por "a tiny pearl-sized drop of translucent amber serum, realistic viscosity".
