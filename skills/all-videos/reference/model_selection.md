# Model Selection — Seedance 2.0 vs Google Omni (y el resto del roster)

La skill ya no es Seedance-only. El MCP de indash expone 6 modelos de video. Elegir el modelo correcto por shot es parte del trabajo del strategist. Este archivo define cuándo usar cada uno.

---

## Roster completo (vía `generate_video`)

| Modelo | Refs máx | Duración | Fortaleza | Debilidad |
|---|---|---|---|---|
| **seedance** (Seedance 2.0 vía fal) | 9 img | 4–15s | Mejor balance fidelity/motion. Multi-ref. | Moderación ESTRICTA (personas, piel, niños, marcas suelen bloquearse). Cola a veces lenta. |
| **seedance-ark** (mismo modelo, backend ByteDance) | 9 img | 4–12s | Moderación permite personas AI-generated. Probar acá primero para escenas con gente. | LENTO: ~40s de render por segundo de clip. Sin auto-retry. |
| **omni** (Gemini Omni Flash) | 3 img | 4–10s | El MÁS RÁPIDO y BARATO. Ideal para drafts, iteración y borradores de coreografía. | 720p. Menor fidelity de producto. Máx 10s. |
| **veo** (Google Veo 3.1) | 3 img | 4–12s | Cinematográfico, buen motion natural. | NO acepta refs inline (base64) — solo URLs. Ignora generate_audio. |
| **kling** (Kling v3 Pro) | 1 img | 3–15s | Close-ups emocionales, caras. Buen fallback cuando Seedance se traba. | 1 sola ref. Grade a veces distinta al resto del set (unificar con LUT). |
| **grok-imagine** (xAI 1.5) | 1 img | 3–15s | Moderación MÁS permisiva. Audio nativo. | 720p, 1 ref, fidelity de producto menor. |

---

## Decision tree (aplicar en el paso 5 del workflow)

```
¿Es un draft / prueba de coreografía / iteración barata?
  → OMNI (rápido, barato, 720p alcanza para validar el motion)
  → Cuando la coreografía valide, re-render final en Seedance.

¿Producto con label/marca específica + hasta 15s?
  → SEEDANCE (multi-ref hasta 9, mejor fidelity)

¿Escena con personas / piel / niños?
  → SEEDANCE-ARK primero (moderación permite personas AI)
  → Si bloquea: KLING (1 ref) o GROK (permisivo)
  → SEEDANCE vía fal probablemente bloquee — no quemar créditos ahí primero.

¿Close-up emocional de cara (ojos, expresión)?
  → KLING rinde sorprendentemente bien con 1 ref.

¿Seedance en cola muerta (>10 min processing)?
  → Re-fire en KLING (mismo frame-0). NO Veo si el frame-0 es base64.

¿Necesitás audio nativo en el render?
  → KLING / GROK / OMNI (seedance también). VEO lo ignora.
```

## El workflow draft→final (nuevo, validado)

Para briefs caros (varios shots, hypermotion, coreografía compleja):
1. **Draft en Omni** (10s máx, 720p, barato): validar coreografía de cámara, timing de beats, composición.
2. Mostrar draft al user si hay dudas de dirección.
3. **Final en Seedance** con el mismo frame-0 y el motion prompt refinado según lo aprendido del draft.

Esto ahorra quemar renders caros de Seedance en coreografías que van a cambiar.

---

## Best practices POR MODELO

### Seedance 2.0
- Multi-ref = **soft conditioning, NO timeline anchoring**. Nunca pasar una ref esperando que sea "el frame del segundo N". Si un frame específico debe aparecer, ese frame es el frame-0 de su propio render.
- **Single-take multi-ref VALIDADO** para: producto ESTÁTICO + toda la coreografía en la cámara (caso real: bebida en lata, marca anonimizada). El producto nunca cambia de estado → hasta 15s en un solo render funciona.
- **Stop-motion discreto VALIDADO** para transformaciones: si el producto tiene N configuraciones (caso real: mobiliario infantil plegable, marca anonimizada), pedir saltos stop-motion instantáneos entre estados anclados con refs (una ref por configuración, mismo ángulo de cámara todas) en vez de morphing continuo. El modelo no anima bisagras — salta entre estados. Prohibir explícitamente "continuous morphing" en el prompt.
- Transformaciones mecánicas continuas (plegado, encastre): partir en shots, cada estado con su frame-0 real.
- Regla de las 3 fidelidades: máx 2 de {movimiento, transformación, label} por render.
- Repetir "no people, no text, no logos, no graphic overlays" EN CADA motion prompt si el brief lo exige — una sola mención al principio no alcanza.

### Omni
- Máx 10s y 3 refs → comprimir el arc o partir en 2 renders.
- 720p: no usar para el entregable final de un cliente premium; sí para social rápido de baja exigencia.
- Es el modelo para ITERAR. Cada iteración de Seedance cuesta ~5-10x lo de Omni.

### Kling
- 1 sola ref → elegir la más informativa (frame-0 del estado inicial).
- Grade sale distinta al set de Seedance → avisar al user que unifique con LUT en CapCut.

### Seedance-ark
- Mismo prompt grammar que seedance.
- En content-policy failure: UN solo resubmit manual vale la pena, después cambiar de modelo.
- Presupuestar el tiempo: un clip de 10s ≈ 6-7 min de render.

---

## Negative-space choreography (para overlays de CapCut)

Cuando el brief incluye contador / badges / logo / texto (que NUNCA se renderizan):
- Coreografiar el negative space POR SHOT y declararlo en el prompt: "left half remains clean empty negative space", "top third completely clean".
- Mapear cada overlay del brief a un shot y su espacio reservado.
- Documentar en la entrega qué overlay va en qué espacio y con qué timing.

Esto convierte el "no renderizamos texto" de limitación en ventaja: el texto animado de CapCut (contadores reales, estrellas que se llenan) siempre se ve mejor que texto generado.
