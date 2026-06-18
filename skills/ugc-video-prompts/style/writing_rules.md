# Writing Rules — Hard Rules for Every Prompt

No son sugerencias. Si un prompt viola alguna, no pasa el eval.

---

## Reglas estructurales

1. **Cada elemento visual tiene un detalle concreto**
   - Malo: "a bottle"
   - Bien: "a small amber glass serum bottle with a white dropper cap"

2. **Cada acción tiene un tiempo asociado**
   - Malo: "she applies the serum slowly"
   - Bien: "over 2 seconds, she presses one drop onto her cheekbone and massages in small circles"

3. **El diálogo va entre comillas, con idioma y acento explícitos**
   - Malo: *she says something about the product*
   - Bien: `She says in Argentine Spanish (Rioplatense accent): "Mirá qué rápido se absorbe."`

4. **El audio se desglosa en capas**
   - Diálogo / SFX diegéticos / Ambiente / Música (o "no music")

5. **La cámara se describe con verbo + dirección + duración**
   - Malo: "camera zooms in"
   - Bien: "slow 10cm push-in from MCU to tight CU over 3 seconds"

6. **El lighting lleva tipo + dirección + calidad (+ momento si aplica)**
   - Malo: "nice lighting"
   - Bien: "soft warm morning window light from camera-left, gentle shadow on the right side of her face"

7. **Identidad del sujeto = edad + origen + 2 rasgos físicos + wardrobe**
   - Malo: "a woman"
   - Bien: "25-year-old Argentine woman, curly dark brown hair in a loose low bun, faint freckles on cheekbones, oversized cream cotton sweatshirt"

8. **Productos = nombre + categoría + tamaño + material + color/packaging**
   - Malo: "a serum"
   - Bien: "a 30ml amber glass serum bottle with a white dropper cap and minimal beige label"

9. **Textura realista del sujeto**
   - **Si el sujeto es humano:** `natural skin texture with visible pores and slight imperfections`. Opcional: `no retouching`, `faint sheen`, `fine facial hair`, `minor redness around nostrils`.
   - **Si el sujeto NO es humano** (dummy, robot, mascote, peluche): adaptar a la textura del material real. Ejemplos: `matte gray polymer with faint scratches and scuff marks from real use`, `fabric weave with visible threads and slight pilling`, `ceramic glaze with hairline cracks`. El espíritu (evitar acabado plástico-perfecto / CGI-clean) se mantiene.
   - Regla: nunca dejar la textura sin especificar. Sin instrucción, los modelos default-ean a CGI-perfect y se nota.

10. **Siempre cerrar con duración + aspect ratio**
    - "Duration: 6 seconds. 9:16 vertical."

---

## Reglas anti AI-slop

11. **Prohibido sin descripción concreta:**
    - `professional`
    - `beautiful` / `gorgeous` / `stunning`
    - `cinematic`
    - `amazing` / `incredible`
    - `high-quality`

12. **Prohibidos como modificadores vagos:**
    - `some`, `various`, `different`, `several`
    - `nice`, `cool`, `good`
    - `a bit of`, `a sort of`

13. **Piel plástica / dientes blancos perfectos / ojos súper saturados** → siempre contrarrestar con `natural texture`, `slight asymmetry`, `realistic color grading`.

---

## Reglas de escritura

14. **Frases cortas.** Coma y punto. No "and-and-and" interminable.

15. **Un beat = una cláusula.** Si tenés que unir dos acciones con "and", separalas en dos frases con sus tiempos.

16. **No redundancia con la imagen de referencia.**
    Si el first frame ya muestra wardrobe, pelo y setting, el prompt de video dice `as shown in reference, she [acción]` — no repite la descripción entera.

17. **No emojis en prompts finales.**

18. **Sin adverbios fofos** (`beautifully`, `gracefully`, `nicely`). Reemplazar con la acción observable.

---

## Reglas de diálogo

19. Siempre entre **comillas**.
20. Siempre con **idioma + región** entre paréntesis.
21. Siempre con **dirección de actuación** entre paréntesis separados (tono, emoción, ritmo, volumen).
22. **Español auténtico**, no traducción literal del inglés. Si suena como "¿Has probado este increíble producto?", está mal. Debería sonar como "¿Probaste esto? Te juro que no lo podía creer."
23. **Para diálogo en español + Kling 3.0 o Seedance 2.0:** el diálogo NO va dentro del prompt como native audio. Va en la sección 7 "Diálogo" del output, separado, para que el usuario lo genere aparte (TTS o grabado) y lo aplique con lipsync. Dentro del prompt de video escribir: `lips move in minimal conversational articulation synced to off-camera voice (no native audio generation)`.
24. **Para diálogo en español + Veo 3.1:** native audio puede ir on, Veo respeta acentos regionales decentes.
25. **Para diálogo en inglés:** native audio on en cualquier modelo (Kling, Veo o Seedance).

---

## Reglas específicas de Seedance 2.0

26. **Cada referencia (`@image`, `@video`, `@audio`) lleva rol explícito.**
    - Malo: `@image1, @image2`
    - Bien: `@image1 as front-face reference of the protagonist, @image2 as product reference (maintain label exactly)`

27. **Verbos físicos > verbos abstractos.**
    - Malo: "the bottle becomes empty"
    - Bien: "the last drop slides down the inner wall of the bottle and falls onto the cheekbone"
    - Lista de verbos físicos preferidos: `snap`, `melt`, `fracture`, `twist`, `drip`, `stretch`, `implode`, `swell`, `pour`, `tilt`, `pull`, `press`, `release`.

28. **Timeline siempre estructurado.** Formato `0-Xs: ... / Xs-Ys: ...`. Nada de párrafo narrativo continuo. Aplica también a Kling cuando el video es multi-shot.

29. **Constraints negativos al final del prompt** (solo Seedance). Funciona como guardrail:
    - `Constraints: no on-screen text, no cuts, no commercial color grading, no studio lighting.`

30. **Para look UGC en Seedance:** sobre-dirigir explícitamente (no asumir).
    - Sumar: `subtle handheld micro-shake throughout`, `natural window light only`, `no studio lighting`, `no commercial color grading`, `iPhone POV framing if applies`.
    - Si tenés un clip UGC real, subilo como `@video1 as aesthetic and camera reference`.

31. **Transformaciones visuales sutiles de piel: pedir el delta exagerado en el frame final.**
    - Si la narrativa depende de un before/after visible de piel (acne, manchas, hinchazón, ojeras, glow), no pedir "noticeably faded" o "slightly improved" en el frame final. Seedance interpola y suaviza el cambio entre cuts — lo que en el frame parece "sutilmente mejorado" termina sin diferencia en el video.
    - Pedir: `skin in the final state is clearly cleared, acne scars significantly reduced, surface smoother with a visible healthy glow, the change should be obvious compared to the initial frame`.
    - Mismo principio para hinchazón → "visibly reduced", ojeras → "noticeably brighter under-eye area", etc.
    - Caso real documentado en `examples/bad/bloss_producto_describe_only_seedance.md`.

32. **Producto con packaging específico = imagen real obligatoria como reference.**
    - No alcanza con describir tipografía, layout y color del packaging por texto, por más detallado que sea el prompt. Nano Banana captura el "concepto" del producto (skincare beige minimalista, tubo dorado de cosmética, etc.) pero inventa tipografía, posición del lettering y matiz exacto de color.
    - Si el pedido involucra un producto con identidad de marca real, exigir la foto al usuario ANTES de redactar prompts. Resolverlo con: (a) producto cargado en workspace de Indash (`get_product_images`), (b) URL pública del usuario (Drive, Imgur), o (c) si no hay alternativa: generar UN hero anchor + iterar hasta fidelidad + reusarlo como reference en el resto. Marcar el riesgo en §8 en este caso.

33. **Audio nativo en español regional — política por variante (Kling 3.0 y Seedance 2.0).**

    La regla histórica era "OFF sin excepciones". La actualización: Seedance 2.0 **sí rinde** para **español porteño (Argentina)** si se cumplen requisitos específicos. El resto de variantes regionales sigue conservador hasta validación caso por caso.

    **Matriz de decisión:**

    | Variante | Seedance 2.0 native audio | Kling 3.0 native audio | Notas |
    |---|---|---|---|
    | Porteño (AR) | **ON OK** | OFF | Funcionó en MOUTHÉ + RestoHost ES con receta abajo |
    | Mexicano / chilango | **ON OK** | OFF | Funcionó en Snowball Partners + Snowprofit campaign con receta `older-brother conversational` (ver abajo) |
    | Neutro LATAM | **ON OK** | OFF | Funcionó en RestoHost ES |
    | Español de España | **ON OK** | OFF | Receta similar a neutro pero con `"vosotros" + "z/c" interdental + cadencia castellana confiada` |
    | Cubano (Miami-Cuban) | OFF (default conservador) | OFF | Sin caso validado |
    | Chileno | OFF (default conservador) | OFF | Sin caso validado |
    | Inglés | ON | ON | Default histórico |

    **Receta por variante (apuntes prácticos):**
    - **Porteño:** `"sh" sound on "ll"/"y", "vos" usage, sing-song intonation, mid-20s/30s influencer tone`
    - **Mexicano/chilango:** `fully pronounced "s", "ll"/"y" as [ʝ] (NOT porteño "sh"), "tú" never "vos", conversational casual cadence like talking to a friend over coffee, NOT a presenter, NOT a radio announcer. Soft warm "older-brother" tone, micro-pauses between clauses`
    - **Neutro LATAM:** `Spanish-language industry standard "español neutro" — no sing-song porteño, no Mexican slang, clear professional articulation, warm but direct`
    - **Español de España:** `"vosotros" usage, "z/c" interdental "th" sound (zapato → "thapato"), Iberian cadence, NOT LATAM`

    **Protocolo para acentos NO validados (cubano, chileno, otros):** correr un mini-test con 1 talking head 8s + 1 frase corta (5-6 palabras) + registro conversacional. Si sale creíble → escalar. Si no → TTS + lipsync en post.

    **Receta que SÍ funciona para porteño / neutro LATAM en Seedance 2.0:**
    ```
    NATIVE AUDIO: ON. Female voice in DISTINCT Buenos Aires PORTEÑO Argentine Spanish accent —
    "sh" sound on "ll"/"y", "vos" usage, sing-song intonation, mid-20s confident influencer tone.
    SFX: subtle ambient + soft music bed at low volume.
    SHE SAYS in porteño with lip-sync: "[línea exacta]"
    ```
    Claves: **edad del talent + tono específico + textura del acento descrita literalmente** ("sh sound on ll/y" para porteño, "vos usage"). Sin esos elementos la voz deriva a neutro plano o a otro acento.

    **Cuándo seguir OFF aunque la variante esté en "ON OK":**
    - Talent no-humano (dummy/robot/mascote): siempre OFF — no hay lip-sync humano.
    - Diálogo >40 palabras: Seedance pierde sync en frases largas → OFF + lipsync en post.
    - Múltiples voces alternándose en el mismo clip: OFF + voz aparte para cada persona.

    **Cuando va OFF**, mantener la receta histórica: `natural full conversational articulation as if speaking, lips move continuously and expressively. No native audio dialogue generation — voice will be added in post with lipsync`. NO escribir `minimal articulation` (lee muerto).

    Casos documentados:
    - **ON exitoso:** `examples/good/mouthe_lip_plumper_porteno_22s.md`
    - **OFF necesario:** `examples/bad/street_vox_pop_bloss_seedance_iteraciones.md` iteración 2 (diálogo largo derivó incluso con receta correcta).

34. **Minimalismo de props en escenas multi-subject de Seedance 2.0.**
    - Multi-subject consistency es debilidad oficial de Seedance 2.0. **Cada prop específico que tiene que mantenerse idéntico entre cuts es un punto de falla.**
    - **Regla:** en escenas con 2+ personas, minimizar props a lo esencial. Si un prop tiene color específico (rosa, dorado), marca visible (logo iPhone), o micro-detalles (clip-on mic con espuma), considerarlo de alto riesgo.
    - Si el concept "parece" necesitar un prop específico, primero preguntarse: **¿la narrativa se lee sin él?** Si sí → sacarlo. Si no → simplificar el prop a su versión más genérica posible (mic de mano corto genérico, no clip-on rosa específico).
    - Cada prop sacado libera capacidad del modelo para mantener cast + escena + producto consistentes.
    - Caso documentado en `examples/bad/street_vox_pop_bloss_seedance_iteraciones.md` iteración 2.

35. **Si cambio un elemento del concept visual, re-validar la narrativa.**
    - Sacar o reemplazar un elemento clave del concept (ej: un prop) puede romper la lectura de la escena aunque resuelva otro problema (ej: derivación).
    - **Antes de regenerar:** pensar `si saco X, ¿la escena se sigue leyendo como [vox-pop / testimonial / demo / etc.]?` Si la respuesta es ambigua → re-pensar el concept entero, no parchear.
    - Caminos posibles cuando un elemento clave deriva:
      - (a) **Simplificar el elemento** (versión más genérica del prop)
      - (b) **Reemplazarlo** por otro que cumpla la misma función narrativa
      - (c) **Sacarlo + adaptar el resto del concept** para que la narrativa funcione sin él
    - (c) es lo más radical pero a veces es lo correcto. Caso documentado: bloss vox-pop iteración 3 — terminamos sacando iPhone+mic + cambiando el concept a "amiga que se acerca a otra en la calle".

36. **Anchor frame propagation — si regenero un anchor, regenero todos los dependientes.**
    - Si un frame Nano Banana es **anchor** (se usa como `reference_image_url` de otros frames) y se regenera, **TODOS los frames que lo referencian deben regenerarse también** con el nuevo anchor.
    - Aplica a:
      - **Cast anchor:** primer frame con el cast → todos los frames que usen ese cast como ref.
      - **Product anchor:** hero shot del producto → todos los frames donde aparece el producto.
      - **Setting anchor:** frame establishing del setting → todos los frames del mismo setting.
    - Saltarse este paso = inconsistencia visible entre cuts (cast cambia de cara, producto cambia de packaging, setting cambia de lugar) — y el usuario lo va a notar antes que vos.
    - Caso documentado en `examples/bad/street_vox_pop_bloss_seedance_iteraciones.md` iteración 3 (regeneré Shot 1 v3 pero NO Shot 2 → cast desincronizado).

37. **Videos >15s = split en N clips de hasta 15s + ensamble en CapCut.**

    Seedance 2.0 cap es 15s por render, Kling 3.0 cap es 15s, Veo 3.1 cap es 8s. Para videos de 17s/20s/30s, no inventar formas de exceder el cap — partir el video en 2-3 clips y ensamblar en CapCut.

    **Reparto típico:**
    - 20s = clip A (10s, hook + setup) + clip B (10s, payoff + CTA)
    - 30s = clip A (15s, hook + problema) + clip B (15s, solución + CTA), o A (10) + B (10) + C (10) para narrativas más densas
    - 17s = clip A (8s, talking head) + clip B (9s, b-roll)

    **Continuidad obligatoria entre clips:**
    - **Wardrobe idéntica** (mismo top, mismo color, mismas joyas). Si el clip B cambia setting (cocina → living), el outfit se mantiene.
    - **Pelo idéntico** (mismo peinado, misma raya). Cambiarlo entre clips se nota muchísimo en cortes secos.
    - **Tono de piel + makeup idénticos** (mismo lipstick, misma luz cromática).
    - **Cast anchor compartido:** pasar el mismo `@image_cast` como reference en los 2-3 renders. No re-generar el cast por separado.
    - **Producto anchor compartido:** mismo `@image_product` en todos los clips donde aparezca.

    **Transición CapCut recomendada entre clips:**
    - Hard cut con flash blanco 2 frames sincronizado al beat de la música. NO fade, NO dissolve — el flash hace el corte legible sin perder energía.
    - Excepción: si los dos clips son ambos talking head del mismo setting, cut seco simple sin flash.

    **Casos documentados:**
    - `examples/good/mouthe_lip_plumper_porteno_22s.md` (2 clips × 11s ensamble)
    - `examples/good/panda_watch_pro_2clip_17s.md` (1 clip talking head + 1 clip b-roll)
    - `examples/good/pov_novio_mia_30s.md` (2 clips × 15s — caso histórico).

38. **Safety filter de Nano Banana — reformulación oblicua.**

    Nano Banana (Gemini 2.5 Flash Image) rechaza prompts con triggers de contenido sugerente aunque la imagen final sea totalmente modesta. **Triggers conocidos:**
    - `nipple`, `nipple cover`, `pasties` → rechazado
    - `under tank top`, `under bra`, `bottom hem lifted` → rechazado
    - `bare chest`, `topless`, `lingerie removal` → rechazado obvio

    **Reformulación oblicua que funciona:**
    - En vez de `placing a nipple cover under her tank top` → `palms flat over the front of the tank top fabric at chest level, as if smoothing or pressing the fabric gently from outside`. La acción se entiende por contexto narrativo + framing.
    - En vez de `lifting the hem to access` → `hands at chest level, fabric remains fully covering throughout`.
    - En vez de `silicone nipple cover` → `round silicone breast petal` o `silicone adhesive disc` (más clínico, menos sugerente).
    - Mantener la palabra del producto si el catálogo del cliente la usa (ej: "pezonera"), pero usarla en contexto comercial (`product reference`) no en contexto de acción corporal.

    **Cuándo activar este modo:** cuando el primer intento devuelve `Gateway returned no image` y el prompt menciona alguno de los triggers. Reformular sin pedir permiso al usuario, lanzar otra vez, mostrar resultado.

    Caso documentado: `examples/bad/pezonera_safety_filter_nano_banana.md`.

39. **Marcas no-dominantes + text rendering = imagen real como reference obligatoria.**

    Seedance 2.0 (y todos los modelos de video actuales) tienen text rendering en pantalla flojo. Para marcas dominantes (Coca-Cola, Apple, Nike) el wordmark suele salir bien por presencia en dataset. Para marcas chicas, regionales o sin presencia (Volaris, Bloss, MOUTHÉ, RestoHost, etc.), el wordmark **se inventa** y deriva a variantes raras ("volants" en vez de "volaris", "MOUTHIE" en vez de "MOUTHÉ").

    **Workflow obligatorio para marcas no-dominantes con wordmark visible en frame:**
    1. **Conseguir foto real** del producto/marca:
       - Producto en workspace de Indash → `get_product_images` (preferido).
       - Marca sin producto cargado → buscar en Wikimedia Commons (search WebSearch + descarga directa con curl).
       - Si no hay foto en internet → pedirla al usuario antes de redactar el prompt.
    2. **Pasarla como `@image_brand`** explícito en la lista de references del render.
    3. **Cláusula anti-derivación en el prompt:** `DO NOT spell it [variantes erradas comunes]. Spell V-O-L-A-R-I-S exactly`. Listar las variantes que el modelo tiende a inventar (las que viste en intentos previos).
    4. **Si después de 2 intentos el wordmark sigue derivado:** plan B = generar el shot crítico como still aparte con Nano Banana usando la foto real como reference + intercalar en CapCut como freeze frame de 1.5-2s.

    Caso documentado: `examples/bad/volaris_wordmark_text_rendering.md`.

40. **Plan B Ken Burns — cuando la cola de Seedance se atasca.**

    La cola de Seedance 2.0 se satura periódicamente (especialmente con renders que tienen 3+ references pesadas o duración >15s). Un render típico tarda 7-10 min. Si pasa de 30 min en `processing`, está atascado.

    **No esperar indefinidamente.** Activar Plan B:

    1. Dejar el render Seedance corriendo en background (créditos ya gastados, si sale eventual lo usás de bonus).
    2. Generar 5 stills × 3s con Nano Banana usando los anchors y producto ya validados.
    3. Ensamble en CapCut:
       - Cada still 3s con **Ken Burns** (zoom-in/zoom-out 5-8%, pan suave).
       - Cortes secos entre stills (no fade) — el ritmo TikTok hace el trabajo.
       - Música 95-115 bpm beat-synced al cambio de still.
       - Flash blanco 2 frames en transiciones clave (antes→después).
    4. Entrega total: 15s del video listo en menos tiempo del que tardó Seedance en atascarse.

    **Indistinguible en feed TikTok/Reels** del 90% del UGC orgánico. La animación natural del cuerpo que sacrifica Ken Burns no aporta cuando el formato narrativo es de cortes rápidos (que es el 95% del UGC publicitario).

    **Cuándo NO usar Plan B:** cuando el video específicamente necesita movimiento físico legible (ej: aplicación del producto en piel, gesto específico de cara, walk-cycle). En esos casos esperar Seedance o relanzar con menos references.

    Caso documentado: `examples/bad/pezonera_seedance_atascado_plan_b.md`.

41. **Cutaways de motion graphics fuera de Seedance.**

    Seedance 2.0 (y los modelos de video actuales en general) están entrenados mayormente en **footage real** — personas, objetos físicos, ambientes. Cuando se le pide animar motion graphics abstractos (mapa con nodos animados, iconos convergiendo en un hub, dashboard con gráficos rellenándose, ilustraciones vectoriales en movimiento) **alucina con casi total certeza**: iconos derivados, países en lugares equivocados, tipografía inventada, animación sin "snap".

    **Regla operativa: la pregunta clave es "¿esto se podría filmar con una cámara real?"**

    | Tipo de cutaway | ¿Seedance lo hace bien? |
    |---|---|
    | Talking head (cara persona hablando) | **Sí** — fortaleza principal |
    | Manos manipulando producto físico | **Sí** — footage real |
    | Pantalla de celular/laptop con UI real | **Sí, con cuidado** — pasar still real de la UI como reference |
    | Mapa animado con nodos lighting up | **No** — derivar a Nano Banana + animación en CapCut |
    | Iconos vectoriales convergiendo / animados | **No** — generar still en Nano Banana, animar fade-in secuencial en CapCut |
    | Dashboard con barras / gráficos rellenándose | **No** — captura real de UI o still + máscara en CapCut |
    | Ilustraciones / motion graphics estilo Loom | **No** — herramientas dedicadas (After Effects, Rive) |

    **Workflow correcto cuando el guión pide motion graphics:**
    1. Generar el frame estático en Nano Banana (o Figma si necesita branding específico).
    2. Pedir a Seedance SOLO los shots de footage real (talking head, manos, producto, ambient).
    3. Animar el motion graphic en CapCut con fade-in secuencial, Ken Burns, particle overlays, o masks.
    4. Ensamblar en CapCut intercalando los shots Seedance con los shots animados por separado.

    **Excepción:** si el cutaway es de un objeto físico que se podría filmar (un celular vibrando sobre una mesa, una hand-held shot de pantalla mirando un mapa real desde fuera), eso sí lo hace Seedance porque es footage. Pedirle siempre así, no como "graphic".

    Caso documentado: `examples/bad/snowball_cutaways_cgi_chilango.md`.

42. **Líneas de diálogo ≤8 palabras + registro conversacional.**

    Seedance 2.0 (y los modelos con audio nativo) **pierden sync limpio en frases >8 palabras** — la cara articula bien las primeras palabras y se desfasa al final. Además, frases con **registro corporate-marketing** ("socio de crecimiento", "todo jalando parejo", "diagnóstico estratégico") salen pronunciadas con cadencia de locutor de radio, no de persona real hablando UGC.

    **Reglas operativas:**

    1. **Cortar frases largas** en oraciones de ≤8 palabras antes de meterlas al prompt. Si el guión del cliente trae "No te mandamos tareas sueltas, somos tu socio de crecimiento" (11 palabras + jerga), partir: shot A "No te mandamos tareas sueltas." (5) + shot B "Somos tu socio." (3). El usuario lee ambas líneas en post si quiere conservar el copy original.

    2. **Reescribir copy formal/corporate en registro conversacional UGC.** Esto es viabilidad técnica del medio, no libertad creativa — acordarlo con el cliente antes de generar. Ejemplos:
       - "Somos tu socio de crecimiento" → "Te ayudamos a crecer."
       - "Todo jalando parejo" → "Todo en un solo equipo."
       - "Diagnóstico estratégico gratuito" → "Diagnóstico gratis."
       - "Optimización de presupuesto publicitario" → "Gastá menos en ads."

    3. **Si el cliente exige las frases originales tal cual:** descartar audio nativo, hacer el clip con `generate_audio: false` + lipsync en post con TTS pro (ElevenLabs). El TTS pro maneja largos sin perder sync y respeta cadencias específicas.

    4. **No empaquetar el script tal como llega del cliente.** Parte del trabajo del director es reescribirlo en cláusulas que el modelo pueda articular. Esto va en la sección 7 del output (Diálogo) — mostrar líneas originales del cliente + líneas adaptadas al medio, y explicar por qué.

    Caso documentado: `examples/bad/snowball_cutaways_cgi_chilango.md` (líneas largas corporate sonaron a locutor).

43. **DEFAULT operativo: una persona hablando a cámara. Punto.**

    Esta es la regla más importante de la skill en términos de output consistente. Acumulamos suficientes casos de derivación, alucinación y cutaways CGI fallidos como para fijar un default fuerte:

    **El video default ES:**
    - **Una sola persona** (talent humano) hablando a cámara.
    - **Mismo setting** durante todo el video (oficina sunlit / cocina sunlit / espejo de baño / dormitorio sunlit — uno solo, sin cambios).
    - **2 o 3 shots máximo por clip de 15s**, todos talking head, solo cambian micro-gestos (forward lean, palm-up, slight nod, soft smile, hand emphasis).
    - **Mismo framing dominante** (medium shot chest-up, eventualmente 1 close-up).
    - **Audio nativo del modelo** cuando el acento está en la matriz de la regla 33.
    - **Sin cutaways, sin b-roll de producto en mano, sin animaciones, sin motion graphics, sin maps, sin iconos animados, sin dashboards.**

    **Por qué este default es agresivo:**
    Talking head a cámara es lo único que Seedance 2.0 hace consistentemente bien. Todo lo demás (cutaways CGI, productos elaborados, multi-setting, b-roll dinámico) tiene tasa de fallo alta documentada en `examples/bad/`. Defaultear a talking head garantiza output usable >90% del tiempo. Cualquier otra cosa es "premium tier" con riesgo conocido.

    **Cuándo desviarse del default (con justificación explícita):**
    - **B-roll de producto en mano**: solo si el producto está cargado en Indash con foto real Y la cláusula PRODUCT LOCK está activa. Documentar el riesgo en §8 del output.
    - **Multi-setting** (mañana / oficina / cena): solo cuando el brief lo exige Y el cliente entiende que es multi-clip con cast anchor compartido. Avisar costo + complejidad.
    - **Cutaway de objeto físico real** (celular vibrando, mano agarrando producto): OK si se filma "como cámara real". NO motion graphics.
    - **Cutaway de motion graphics** (mapa con nodos, iconos animados, dashboard): NUNCA dentro de Seedance. Pasa por Nano Banana + animación en CapCut. Ver regla 41.

    **Antes de generar, validar contra el default:**
    1. ¿El brief pide cutaways CGI o motion graphics? → Avisar al cliente que va por CapCut, no Seedance.
    2. ¿El brief pide multi-setting? → Plantear si vale la pena vs talking head simple con texto en pantalla.
    3. ¿El brief pide acción compleja (cocinar, montar bici, multi-instancia producto)? → Considerar si la narrativa se sostiene con talking head + 1 cutaway físico simple.
    4. ¿El brief pide simulación de algo que no se puede filmar (datos animados, comparativas visuales, gráficos)? → Va a CapCut como overlay encima de talking head, no a Seedance.

    **Esta regla está por encima de la creatividad ambiciosa.** Si el brief es ambicioso visualmente, la responsabilidad del director (vos) es traducirlo a la versión más simple posible que aún cumpla el objetivo del ad. La complejidad visual se agrega en post (CapCut overlays, texto en pantalla, motion graphics agregados aparte) — no se delega al modelo de video.

    **Output del default talking head:**
    - 1 clip de 15s = 3 shots × 5s c/u, mismo setting, mismo framing.
    - Línea de diálogo por shot ≤8 palabras (regla 42).
    - Audio nativo del modelo según matriz regla 33.
    - Cero cutaways. Cero motion graphics. Cero cambios de setting.
    - Textos overlay, animaciones, logos: agregados después en CapCut.

    Casos documentados:
    - **Default talking head exitoso:** Snowball TACoS 15s, Snowball Partners 30s, Snowprofit campaign 4 videos (12 clips).
    - **Desvío del default que falló:** `examples/bad/snowball_cutaways_cgi_chilango.md` (cutaways CGI tiraron el video abajo).

---

## Regla maestra

> Si tu frase podría describir **cualquier otro video**, es demasiado genérica. Ajustá hasta que sea **irreemplazable**.
