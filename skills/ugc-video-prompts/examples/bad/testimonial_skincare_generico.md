# Ejemplo BAD — Testimonial skincare (NO hacer esto)

Mismo input que el ejemplo GOOD de 8s. Este es el output que **NO** queremos. Estudiar por qué cada parte es floja.

---

# Paquete de video — Skincare testimonial

## 1. Análisis de escena
- **Tipo de contenido:** ad
- **Sujeto principal:** una mujer con un producto
- **Plataforma:** redes sociales
- **Aspect ratio:** vertical
- **Mood:** bueno y profesional

> ❌ "redes sociales" no es plataforma. "vertical" no es ratio. "bueno y profesional" es AI-slop sin contenido.

## 2. Recomendación de modelo
**Elegido: Veo 3.1**

Razón: es un buen modelo para este tipo de videos.

> ❌ "Buen modelo" no es criterio. No compara con Kling. No referencia el pedido concreto.

## 3. Estructura
- **Shots:** uno
- **Frames de referencia:** first frame
- **Duración total:** 8s

> ❌ No explica por qué first frame solo. No justifica duración. "Uno" no es respuesta sobre shots (single-shot continuo? con cortes?).

## 4. Prompts de Nano Banana

### First frame
```
A beautiful young woman holding a skincare product in her bedroom, looking at the camera with a professional smile. Nice lighting, cinematic, high quality.
```

> ❌ "Beautiful", "nice", "cinematic", "high quality", "professional" — todos AI-slop. Sin edad, sin origen, sin rasgos, sin wardrobe, sin producto concreto (qué tipo de skincare? qué tamaño? qué color?), sin lighting específico (qué tipo? de dónde viene?), sin framing (shot size? ángulo? ratio?), sin style (dispositivo? film stock?). Piel perfecta sin contrarrestar → va a salir plástica.

## 5. Prompt de video

**Modelo:** Veo 3.1

```
The woman smiles and talks to the camera about the serum. She applies it to her face. Nice and professional video, cinematic style.
```

> ❌ Sin dialogue explícito (qué dice? en qué idioma? con qué tono?). Sin timing (cuándo pasa cada beat?). Sin cámara (se mueve? cuánto?). Sin audio desglosado. "Nice and professional / cinematic" es exactamente el flag AI-slop. El modelo va a inventar todo.

## 6. Parámetros técnicos
- **Duración:** 8 segundos
- **Aspect ratio:** vertical
- **Audio:** sí

> ❌ "Vertical" ≠ 9:16. "Audio sí" sin desglose de qué tipo.

## 7. Diálogo
Va a decir algo sobre el producto.

> ❌ No hay línea, no hay idioma, no hay dirección de actuación. El modelo va a inventar la frase, y probablemente en inglés.

## 8. Notas de riesgo
Puede salir mal a veces.

> ❌ Inútil. No identifica riesgos específicos ni mitigaciones.

---

## Resumen — por qué este output es malo

1. **Vaguedad total** — cualquier producto/persona/escena podría caer en este prompt. No es irreemplazable.
2. **AI-slop everywhere** — beautiful, nice, professional, cinematic, high quality.
3. **Sin criterio técnico** — ningún número, ninguna dirección, ningún tiempo.
4. **Sin performance** — el diálogo no existe como línea concreta, la actuación no está dirigida.
5. **Sin audio real** — "audio sí" no es un plan de sonido.
6. **Sin defensa contra el fallo** — riesgos genéricos, sin mitigación aplicable.

**Regla:** si tu output se parece a esto, tirarlo y empezar de nuevo. El eval checklist te lo va a marcar.
