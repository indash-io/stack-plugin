# MALO — Voz con TTS de macOS (`say`) muxeada con ffmpeg para diálogo en español

## Contexto
UGC testimonial 10s, 9:16, seller mexicano hablando a cámara. Cliente: agencia de e-commerce (anonimizada). Requisito: **audio en español mexicano sí o sí**.

Veo (que haría voz nativa regional con lip-sync) estaba bloqueado en el pipeline de Indash (rechaza la imagen de referencia: `inlineData isn't supported`). Para "garantizar" el audio mexicano se tomó este atajo:

1. Video generado mudo con Kling (image-to-video desde el frame-0).
2. Voz generada con el TTS nativo de macOS: `say -v Reed` (es_MX).
3. Audio muxeado al video con ffmpeg (`atempo` + `adelay`) para calzar 10s.

## Por qué es MALO
- **Timbre robótico.** Las voces de sistema (`say`: Reed, Eddy, Paulina, etc.) suenan sintéticas y delatan "AI/automatizado". Para una pieza publicitaria es inaceptable — mata la credibilidad UGC, que depende de que la voz suene humana.
- **Lip-sync inexistente.** El video se generó con articulación genérica y el audio se pegó encima sin sincronización real: la boca no calza con las palabras. Se lee como doblaje barato.
- **`atempo` para forzar el calce** acelera la voz y la vuelve aún más artificial.
- Resultado: el cliente lo calificó de "pésimo".

## Regla que sale de acá
- **Nunca uses el TTS de `say`/sistema para la voz final de una pieza.** Sirve como máximo para un scratch interno de timing, jamás como entregable.
- **El lip-sync no se resuelve muxeando audio crudo sobre un video mudo.** Si el audio va aparte, hay que pasar por una herramienta de lipsync real (Sync.so, Enhancor) — y aun así, la voz tiene que ser de calidad (humana real o TTS premium tipo ElevenLabs con voz mexicana).
- **Orden de preferencia para diálogo en español regional con audio de calidad:**
  1. **Veo 3.1 con audio nativo** (si el pipeline lo permite) — voz + lip-sync en un pase.
  2. **Audio nativo del modelo** (Seedance/Kling) si en pruebas reales el acento/idioma sale bien para el caso.
  3. **Voz humana real** o **ElevenLabs (voz MX)** + **lipsync dedicado** (Sync.so/Enhancor).
- Si ninguna opción de calidad está disponible, **decirlo y no entregar un placeholder robótico como si fuera final.**

Ver también `street_vox_pop_skincare_seedance_iteraciones.md` y la tabla de audio en `instructions/analysis.md`.
