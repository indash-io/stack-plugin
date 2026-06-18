# Output Template — Paquete de video

Usar LITERAL. No cambiar orden. No agregar secciones. No omitir secciones (si algo no aplica, escribir "N/A" con razón breve).

Si el video es **multi-clip** (>15s, partido en N clips Kling pegados en post), las secciones 4 y 5 se repiten una vez por clip. Ver `examples/good/pov_novio_mia_30s.md`.

---

```markdown
# Paquete de video — [Título breve del concepto]

## 1. Análisis de escena
- **Tipo de contenido:** [ad / testimonial / demo / transformation / b-roll / narrative / POV]
- **Sujeto principal:** [persona / producto / ambos / sujeto no-humano — con 1 línea de descripción]
- **Plataforma:** [TikTok / Reels / YouTube / feed IG / otro]
- **Aspect ratio:** [9:16 / 16:9 / 1:1 / 4:5]
- **Mood:** [1 línea concreta — ej: "íntimo confesional, matutino"]
- **Asumidos (si aplica):** [lista breve de defaults aplicados por falta de info]

## 2. Recomendación de modelo
**Elegido: [Kling 3.0 / Veo 3.1 / Seedance 2.0] [+ Pro mode si aplica] [+ multi-clip si >15s]**

Razón: [1-2 líneas con criterio concreto del pedido — duración, multi-shot, lip-sync, español regional, referencias multimodales disponibles, look UGC vs commercial, etc. Mencionar por qué los otros 2 modelos quedan afuera. Si audio nativo es off, explicar por qué.]

## 3. Estructura
- **Total:** [Xs single-clip / Xs partidos en N clips Kling/Seedance de 15s c/u]
- **Shots por clip:** [single-shot / multi-shot: N tomas — listar beats breves]
- **Frames de referencia:** [first / first + last / first + last por cada clip]
- **Razón first/last:** [1 línea por qué se decidió así]
- **Continuidad inter-clip (si multi-clip):** [qué hay que mantener idéntico entre clips para que el corte se sienta limpio]
- **Aspect ratio:** [repetir]
- **Referencias multimodales (si Seedance 2.0):** [listar slots usados — `@image1 as ..., @image2 as ..., @video1 as ..., @audio1 as ...` — con rol explícito. Si no hay referencias adjuntadas, N/A.]

## 4. Prompts de Nano Banana

[Si single-clip:]

### First frame
\`\`\`
[prompt en inglés según `instructions/execution.md` + `style/writing_rules.md`]
\`\`\`

### Last frame
[Si aplica:]
\`\`\`
[prompt en inglés manteniendo idénticos sujeto, wardrobe, lighting, setting y framing del first frame, cambiando solo lo que el beat final exige]
\`\`\`
**Qué cambia respecto al first frame:** [lista breve]

[Si no aplica:] N/A — el video es movimiento continuo sin necesidad de anclar estado final.

[Si multi-clip — repetir el bloque por cada clip:]

### Clip 1 — First frame
\`\`\`...\`\`\`

### Clip 1 — Last frame
\`\`\`...\`\`\`

### Clip 2 — First frame
\`\`\`...\`\`\` (debe matchear wardrobe + setting + lighting del Clip 1)

### Clip 2 — Last frame
\`\`\`...\`\`\`

## 5. Prompt(s) de video

**Modelo:** [Kling 3.0 / Veo 3.1 / Seedance 2.0] [+ Pro mode si aplica]
**Audio nativo:** [on / off] — razón breve (ver tabla de `instructions/analysis.md`)
**Frames de referencia:** [first / first + last / por cada clip]
**Referencias multimodales (si Seedance):** [lista de `@asset as [rol]` — o N/A]

[Si single-clip:]

**Caracteres del prompt:** [N] / 2500 (verificado con `wc -c`)

\`\`\`
[prompt en inglés completo. Si audio off, incluir: "lips move in minimal conversational articulation synced to off-camera voice (no native audio generation). Voice added in post."]
\`\`\`

[Si multi-clip — repetir el bloque por cada clip, cada uno con su conteo de chars:]

### Clip 1 (0–15s del video final)
**Caracteres:** [N] / 2500
\`\`\`...\`\`\`

### Clip 2 (15–30s del video final)
**Caracteres:** [N] / 2500
\`\`\`...\`\`\`

## 6. Parámetros técnicos
- **Duración:** Xs [total] [+ desglose por clip si multi-clip]
- **Aspect ratio:** 9:16 / 16:9 / 1:1 / 4:5 / 21:9 (21:9 solo Seedance)
- **Resolución sugerida:** 720p / 1080p (si Seedance + audio nativo: 480p o 720p)
- **Audio nativo:** on / off
- **Frames de referencia:** first / first + last [por clip si multi-clip]
- **Modo (si Kling):** Standard / Pro / Master
- **Modo (si Seedance):** T2V / I2V / R2V (multimodal con `@asset`) / video extension

## 7. Diálogo
[Si aplica:]
- **Idioma + acento:** Español ([argentino / mexicano / colombiano / español ES / chileno / cubano / neutro LATAM]) o Inglés
- **Modo de generación:** [native audio del modelo / voz aparte + lipsync en post]
- **Si voz aparte:** herramienta sugerida para la voz (ElevenLabs / Play.ht / Murf / grabación humana real) + herramienta de lipsync (Enhancor V4 / Sync.so / HeyGen / Kling Lipsync).
- **Línea 1 ([rango de timing], [rol — hook/beat/CTA]):** "..."
- **Línea 2 ([rango], [rol]):** "..."
- [N líneas según el guión]
- **Dirección de actuación:** [tono, volumen, emoción, ritmo — específico, no genérico. Ej: "voz femenina argentina ~28, conversacional íntima, suspiro en 'ibuprofeno', cero tono publicitario"]
- **Alternativas (opcional):** variantes por si el TTS o el actor humano no calza la primera

[Si no aplica:] N/A — sin diálogo. Audio: [describir breve el sonido principal].

## 8. Notas de riesgo
- **Qué puede salir mal en el primer intento:** [1-4 puntos ESPECÍFICOS a este pedido — no genéricos]
- **Cómo mitigarlo si pasa:** [1-2 ajustes concretos por riesgo]

## 9. Flujo de producción (si audio off / multi-clip / sujeto no-humano)
[Si el video tiene alguna complejidad de post, listar pasos numerados:]
1. Generar [first + last frame] en Nano Banana usando los prompts de §4. Si hay imagen real del producto, subirla como referencia visual junto con el prompt de texto.
2. Pasar a [Kling 3.0 Pro / Veo 3.1] con los frames + el prompt de §5. [Si multi-clip: generar los N clips en orden.]
3. [Si audio off:] generar la voz aparte. Opción recomendada: [voz humana real / TTS específico]. Script en §7.
4. [Si audio off:] aplicar lipsync con [Enhancor V4 / Sync.so / otro]. Subir el video + el audio, generate.
5. [Si multi-clip:] pegar los N clips en CapCut / Premiere con corte seco.
6. [Si SFX nativos quedaron mal:] reemplazar en CapCut.
[Si single-clip + native audio + sujeto humano:] N/A — el video sale completo de Kling/Veo.
```

---

## Reglas de uso del template

- **No** agregar introducción ni cierre al paquete. El output empieza con el título H1 y termina con la última nota de riesgo o el flujo de producción.
- **No** explicar la skill antes de entregar. El paquete habla por sí solo.
- **Contar caracteres** de cada prompt de video con `wc -c` ANTES de entregar. Documentarlo en §5. Si excede 2500, comprimir según `instructions/execution.md` regla 9 y volver a contar.
- Si el pedido es **de revisión/mejora** de un prompt existente, entregar el paquete nuevo + al final una sección adicional `## 10. Cambios vs original` con diffs breves.
- Todo el paquete debe poder **copiar-pegarse a Notion/Docs** y leerse limpio.
