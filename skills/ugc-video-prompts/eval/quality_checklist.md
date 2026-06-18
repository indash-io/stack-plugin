# Quality Checklist — correr antes de entregar

Si CUALQUIER ítem falla, **no entregues** — corregí y volvé a correr. No es opcional.

Formato: ✅ pasa / ❌ falla. Si ❌, nota qué corregir.

---

## A. Cobertura del pedido
- [ ] Se identificó tipo de contenido (ad / testimonial / demo / etc.)
- [ ] Se identificó sujeto principal con detalle (persona: edad + origen + 2 rasgos + wardrobe / producto: nombre + categoría + material + color)
- [ ] Se identificó plataforma (TikTok / Reels / YouTube / feed IG)
- [ ] Aspect ratio coincide entre imagen de referencia y video
- [ ] Mood está en 1 línea concreta (no "bueno", no "profesional")
- [ ] Asumidos (si los hay) están listados explícitamente

## B. Elección de modelo
- [ ] Se justificó la elección entre **Kling 3.0 / Veo 3.1 / Seedance 2.0** con criterio concreto del pedido (duración, multi-shot, lip-sync, referencias multimodales disponibles, look UGC vs commercial, etc.)
- [ ] Se explicita por qué los otros 2 modelos quedan afuera
- [ ] Si el modo de Kling se aplica (Standard/Pro/Master), está especificado
- [ ] Si el modo de Seedance se aplica (T2V / I2V / R2V / video extension), está especificado
- [ ] **Si el usuario adjuntó referencias multimodales (imgs / videos / audios) y NO se eligió Seedance 2.0**, hay justificación explícita (ej: "el cast hablando close-up exige Veo 3.1 por lip-sync, las referencias del producto se usan como anchor textual en lugar de `@asset`")

## C. Estructura
- [ ] Se decidió single-shot o multi-shot (y cuántas tomas si multi)
- [ ] Se decidió first-frame-only o first+last, con razón
- [ ] Duración justificada por tipo de contenido
- [ ] Aspect ratio coincide con plataforma
- [ ] **Ningún shot exige mostrar el mismo producto en N estados/configuraciones simultáneamente en un mismo frame.** Si el ángulo lo requiere, partir en N inserts (cada uno con su Nano Banana + mini-clip) y avisar al usuario ANTES de generar. Ver `instructions/analysis.md` "Caso imposible #2" y `examples/bad/multi_instance_packshot.md`.

## D. Prompt de Nano Banana (first frame)
- [ ] Sujeto: edad + origen + 2 rasgos físicos + wardrobe específico (si humano) / material + textura específica (si no-humano)
- [ ] Acción/pose con expresión explícita (no solo "posing")
- [ ] Setting: ≥2 objetos concretos nombrados
- [ ] Lighting: tipo + dirección + calidad + momento del día
- [ ] Framing: shot size + ángulo + aspect ratio
- [ ] Style: dispositivo o film stock específico
- [ ] **Textura realista marcada**: si humano → "natural skin texture with visible pores"; si no-humano → adaptación al material ("matte polymer with faint scratches", "fabric weave with visible threads", etc.). Ver `style/writing_rules.md` regla 9.
- [ ] Cero palabras prohibidas: beautiful / professional / nice / amazing / cinematic (sueltas)
- [ ] **Imagen real del producto como `reference_image_url` (regla dura, no negociable).** Si el pedido involucra un producto con packaging específico (tipografía, color, layout, logo), **NO se entrega sin la foto real** del producto pasada como reference image al Nano Banana (y al Seedance si aplica). Describir-only del packaging falla sistemáticamente — Nano Banana captura el concepto pero inventa tipografía, layout y matiz de color. Si el usuario no tiene la foto accesible al MCP, resolverlo ANTES de generar: (a) cargar el producto al workspace de Indash y usar `get_product_images`; (b) pedir URL pública (Drive, Imgur, Dropbox); (c) en último caso, generar UN packshot hero anchor con descripción quirúrgica + iterar + usar como reference en el resto, marcando el riesgo en §8. Ver `examples/bad/bloss_producto_describe_only_seedance.md`.

## E. Prompt de Nano Banana (last frame, si aplica)
- [ ] Mantiene idénticos: sujeto, wardrobe, lighting, setting, framing
- [ ] Cambia solo lo que el beat final exige
- [ ] Lista explícita de qué cambia vs first frame
- [ ] Mismo aspect ratio que first frame y video
- [ ] **Si la transformación depende de un cambio visual sutil de piel** (acne, manchas, hinchazón, ojeras, brillo), el delta debe pedirse **exagerado en el frame final** — no "sutilmente faded" sino "clearly cleared, scars significantly reduced, skin smoother with visible glow". Seedance suaviza al interpolar entre cuts: el extremo del Nano Banana es lo que llega a "lo realista" en el render. Sub-shoot deliberado del delta = no se ve el cambio. Ver `examples/bad/bloss_producto_describe_only_seedance.md` (sección "Shot 2 sin mejora real de piel") y `style/writing_rules.md` regla 31.

## F. Prompt de video
- [ ] Cada beat de acción tiene tiempo asociado ("at 3s", "from 0-2s", etc.). **Si Seedance 2.0:** timeline en formato `0-Xs: ... / Xs-Ys: ...` (no paragraph narrativo).
- [ ] Cámara descripta con verbo + dirección + duración
- [ ] Audio desglosado en capas: diálogo / SFX / ambiente / música (o "no music" explícito)
- [ ] **Estrategia de audio correcta según tabla de `instructions/analysis.md`**: si diálogo es español regional + modelo Kling o Seedance, audio nativo OFF y el prompt incluye `"lips move in minimal conversational articulation synced to off-camera voice (no native audio generation)"`. Si es inglés, audio puede ir on en los tres modelos. Si es español + Veo 3.1, audio puede ir on.
- [ ] Diálogo native (solo si audio on): entre comillas + idioma + región + dirección de actuación en paréntesis
- [ ] Si audio off, **el diálogo NO va dentro del prompt** — va separado en la sección 7 del output
- [ ] No redundancia con el frame de referencia ("as shown in reference" o "as in @image1" cuando aplica)
- [ ] **Si Seedance 2.0:** cada `@asset` (imagen/video/audio de referencia) tiene **rol explícito declarado** (`@image1 as front-face reference`, `@audio1 as music reference, cut on strong beats`). Cero referencias subidas sin rol.
- [ ] **Si Seedance 2.0:** verbos físicos específicos (snap, melt, twist, drip, fracture). Cero verbos abstractos sueltos (becomes, transforms, changes).
- [ ] **Si Seedance 2.0 + look UGC pedido:** el prompt sobre-dirige el look (`subtle handheld micro-shake`, `natural window light`, `no studio lighting`, `no commercial color grading`, `iPhone POV framing`). Sin esto, Seedance default-ea a commercial.
- [ ] **Si Seedance 2.0:** sin texto on-screen pedido en el prompt (text rendering flojo). Si los carteles son no-negociables, marcarlo en §8 riesgos y agregarlos en post.
- [ ] Si hay last frame, closing state descripto al final
- [ ] Duración total + aspect ratio al final del prompt
- [ ] Cero palabras prohibidas en AI-slop
- [ ] **≤ 2500 caracteres** (incluyendo espacios y saltos de línea), aplica a Kling, Veo y Seedance. **Contar con `wc -c` o herramienta equivalente — nunca estimar a ojo**. Si excede, aplicar orden de compresión de `instructions/execution.md` regla 9, y volver a contar. No entregar hasta ver el número exacto bajo 2500.
- [ ] **Si multi-clip (>15s):** cada clip tiene su propio prompt, cada uno ≤2500 chars verificado con `wc -c`. Cada prompt repite el anchor de element consistency (mismo wardrobe + mismo setting + misma luz + mismo color grading) para que la unión en CapCut se sienta limpia.

## G. Parámetros técnicos
- [ ] Duración exacta
- [ ] Aspect ratio exacto (formato "9:16" no "vertical"). 21:9 solo si el modelo es Seedance 2.0.
- [ ] Resolución sugerida (si Seedance + audio nativo on: 480p o 720p, no 1080p)
- [ ] Audio nativo on/off con razón
- [ ] Frames de referencia: first / first+last
- [ ] Modo de Kling si aplica
- [ ] Modo de Seedance si aplica (T2V / I2V / R2V / video extension)

## H. Diálogo (si aplica)
- [ ] Idioma + acento regional explícito
- [ ] **Modo de generación explícito:** native audio del modelo o voz aparte + lipsync
- [ ] **Si voz aparte:** herramienta sugerida para la voz (ElevenLabs / Play.ht / Murf / grabación humana) + herramienta de lipsync (Enhancor V4 / Sync.so / HeyGen)
- [ ] Línea concreta por cada beat (no "dice algo sobre...")
- [ ] Cada línea tiene timing/rango asociado al video
- [ ] Dirección de actuación (tono, volumen, emoción, ritmo) — específica, no genérica
- [ ] Suena natural en la región (no traducción literal del inglés)
- [ ] Opcional: alternativa de línea por si el TTS o el actor no calza la primera

## I. Notas de riesgo
- [ ] 1-3 riesgos ESPECÍFICOS a este pedido (no genéricos tipo "puede salir mal")
- [ ] Cada riesgo tiene mitigación concreta y aplicable

## J. Anti AI-slop
- [ ] Ningún "beautiful" / "professional" / "cinematic" / "amazing" / "high quality" sin reemplazar con concreto
- [ ] Ningún "some" / "various" / "different" vago
- [ ] Skin realista marcada (si hay persona)
- [ ] Si una frase podría aplicarse a cualquier otro video → corregir

## K. Forma del output
- [ ] Usa el template literal (secciones 1-8, en orden; sección 9 si audio off / multi-clip / sujeto no-humano)
- [ ] Sin introducción ni cierre extra fuera del paquete
- [ ] Bloques de código para prompts (copy-paste limpio)
- [ ] Conteo de chars del prompt de video visible en §5 (formato "N / 2500")
- [ ] Markdown válido

## L. Flujo de producción (§9, si aplica)
- [ ] Si audio off → §9 lista pasos: Nano Banana → Kling/Veo → voz aparte → lipsync → CapCut
- [ ] Si multi-clip → §9 menciona pegado en CapCut con corte seco
- [ ] Si sujeto no-humano y la generación necesita varios intentos → §9 menciona regenerar el first frame hasta que la grip/articulación sea creíble antes de pasar a video

## M. Anchor frame propagation (si hay regeneraciones)
- [ ] **Si regeneré un frame que es anchor de otros** (usado como `reference_image_url` por otros frames del paquete), **regeneré también TODOS los frames dependientes** con el nuevo anchor.
- [ ] Verifiqué que el cast en todos los frames de un mismo personaje matchea identidad (cara, pelo, outfit) — si algún frame se generó con un anchor distinto al actual, hay que regenerarlo.
- [ ] Verifiqué que el producto en todos los frames donde aparece matchea la imagen del producto real (idealmente la del workspace de Indash o URL pública del usuario).
- [ ] Verifiqué que el setting en frames de la misma escena matchea (color palette, lighting, props del entorno).
- [ ] Si encuentro inconsistencia entre frames por anchors desactualizados, regenero **antes** de pasar al video. Ver `examples/bad/street_vox_pop_bloss_seedance_iteraciones.md` iteración 3.

## N. Self-validation pre-entrega al usuario (regla dura)
- [ ] **Antes de mostrar cualquier frame o video al usuario**, corrí internamente el checklist A→M. Marqué inconsistencias YO. No estoy delegando validación crítica al usuario.
- [ ] **Si encontré algo que falla, lo digo explícitamente al usuario** (no espero que él lo note) y propongo el fix concreto.
- [ ] **Si saqué/cambié un elemento clave del concept visual** (ej: un prop), me pregunté: ¿la escena se sigue leyendo como [vox-pop / testimonial / demo / lo que sea]? Si la respuesta es ambigua, re-pensé el concept entero antes de mostrar al usuario.
- [ ] **Reduje el número de elementos cambiantes en escenas multi-subject de Seedance.** Cada prop específico, color exacto, micro-detalle que tiene que mantenerse consistente entre cuts es punto de falla. Minimicé a lo esencial. Ver `style/writing_rules.md` regla 34.
- [ ] **Audio nativo OFF para español regional, sin excepciones.** No activé `generate_audio: true` pensando que "ayuda al dinamismo" — uso `natural full conversational articulation` en el prompt y dejo audio OFF. Ver `style/writing_rules.md` regla 33.
- [ ] Yo soy el experto del framework. El usuario decide dirección creativa. **Yo decido si el output cumple el estándar técnico.** Si no cumple, no se muestra hasta que cumpla — o se muestra con el fallo declarado y la propuesta de fix.

---

## Threshold

- **100% ✅:** entregar.
- **1-2 ❌ menores (cobertura/forma):** corregir y reenviar.
- **Cualquier ❌ en D/E/F (los prompts en sí):** reescribir el prompt, no parcharlo.

---

## Cómo correr rápido

1. Leer el output entero una vez sin checklist, como lector.
2. Volver arriba y correr A → K.
3. Marcar ❌ con nota de qué corregir.
4. Corregir SOLO lo marcado (no reescribir todo).
5. Volver a correr el checklist.
6. Entregar cuando todo sea ✅.
