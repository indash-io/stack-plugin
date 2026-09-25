# Quality Checklist — Self-check antes de entregar

Correr antes de cada entrega. Si algo falla → arreglar y volver a chequear.

## Gate y contexto
- [ ] El conector `indash` estaba disponible; no inventé ningún audio ni sugerí otra herramienta
- [ ] Heredé tono, público, acento y palabras prohibidas del `CLAUDE.md` del cliente (si existe)
- [ ] Si el guion venía de otra skill, respeté su duración por shot y su hook

## Guion
- [ ] Hook en los primeros ~30 caracteres
- [ ] Frases de ≤12 palabras, una idea por frase
- [ ] Números, siglas y símbolos escritos como se dicen
- [ ] Nombres de marca/producto verificados (fonético si hizo falta) y anotados
- [ ] Caracteres hablados ≈ duración objetivo × 15 (±15%)
- [ ] Ningún item pasa 4.500 caracteres hablados
- [ ] Nada que no esté en el sitio/brief del producto
- [ ] Pasa el test "¿lo diría alguien en voz alta?"

## Dirección
- [ ] `style` con tono, ritmo, energía, **idioma y acento**, y a quién le habla
- [ ] Acotaciones solo en líneas que cambian; tags solo donde una persona real lo haría
- [ ] Sin MAYÚSCULAS para gritar ni `¡¡` dobles
- [ ] Voz elegida por audición o por decisión previa de la persona — no por el nombre ni por la descripción
- [ ] Edad, género y acento resueltos en la **voz** (estudio / biblioteca / diseñada), nunca pedidos en el `style`
- [ ] Si diseñé una voz: descripción de rasgos permanentes en 1-2 frases + `language_code`; sample escuchado por la persona; descartadas borradas con `delete_voice`; la ganadora anotada en el `CLAUDE.md` del cliente
- [ ] Dos voces: `speakers` de exactamente 2, nombres de persona, contraste de carácter, primera línea con `Nombre:`

## Decisión y costo
- [ ] Hubo **una sola** pregunta consolidada con defaults antes de generar
- [ ] Dije el costo en tiers antes (audición + diseño de voz + finales) y el cobrado después
- [ ] Modelo justificado (`gemini-tts` por default; `-lite` por volumen/narración plana)

## Generación
- [ ] **Una** llamada a `generate_speech` con todos los items (no en loop)
- [ ] `output_name` con el nombre canónico del set
- [ ] Cada item `completed`; los `error` leídos, explicados y corregidos (no relanzados a ciegas)
- [ ] `duration_seconds` dentro del ±15% del objetivo, o expliqué qué ajusto

## Entrega
- [ ] Dije explícitamente que **no escuché** el audio y qué sí chequeé
- [ ] Tabla con voz, dirección, duración real, objetivo, tier y URL por item
- [ ] Guion dirigido visible para editar
- [ ] Guardado en disco con nombre canónico (`exports/audio/…` o la carpeta del set de video), sin pisar
- [ ] Handoff claro (`hyperframes` / `edicion-ugc` / conversión a MP3) y ruta de guardado en una línea
- [ ] Mencioné `promote_creative` solo si eligieron un final
