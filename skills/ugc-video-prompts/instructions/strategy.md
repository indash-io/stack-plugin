# Creative Strategy

Pensá como director, no como redactor de prompts.

---

## UGC Authenticity markers

Lo que hace que un video generado con IA **lea como UGC real** y no como ad:

### Cámara
- **Handheld feel** — ligero sway, no estabilización perfecta. Describirlo: "subtle handheld micro-shake".
- **No perfectamente centrado** — offset leve, cabeza más arriba que el centro del frame.
- **Ángulos humanos** — eye-level o ligeramente arriba (selfie angle), no grúas ni dolly-zooms.

### Lighting
- **Natural window light** > studio lighting.
- **Una dirección clara** (camera-left, camera-right) — no iluminación plana.
- **Hora específica** — "morning soft light", "late afternoon warm light", "overcast diffused daylight".
- Evitar "professional studio lighting" — es el flag AI-slop #1.

### Wardrobe & grooming
- **Ropa realista** — hoodies, t-shirts, oversized, colores neutros o con lógica.
- **Sin styling publicitario** — no "effortlessly chic".
- **Minimal o no makeup** (para look UGC) — especificar "no makeup" o "minimal natural makeup".
- **Pelo con textura real** — "slightly messy bun", "natural curls", no "perfect blowout".

### Framing
- **Close-up con aire** — no corte en el mentón; dejar respiración arriba o abajo.
- **Fondos con profundidad real** — objetos cotidianos identificables (lámpara, planta, cuadro), no "fondo limpio".

### Performance
- **Micro-expresiones** > sobreactuación.
- **Pausas naturales** — un "eh", un "mirá", una respiración.
- **Mirada no perfecta** — a veces mira al producto, a veces a cámara, a veces al costado.

### Articulación de boca cuando hay diálogo + audio nativo OFF (flujo de lipsync)
Si la voz se va a agregar en post con lipsync (Enhancor V4 / Sync.so / etc.), el video tiene que mostrar **algún movimiento de boca genérico** para que la herramienta de lipsync tenga material visual donde sincronizar el audio.
- Pedir explícitamente: `"lips move in minimal conversational articulation synced to off-camera voice (no native audio generation)"`.
- NO pedir boca cerrada los X segundos del diálogo — el lipsync no funciona sobre boca completamente fija.
- Tampoco pedir lip-sync preciso al modelo — vamos a sobreescribir con el lipsync de post.
- Si el sujeto es **no-humano** (dummy, robot), pedir movimiento **puppet-style rigid jaw**, NO lip-sync humano. Funciona como anchor para lipsync de igual forma.

---

## Minimalismo de elementos en multi-subject Seedance 2.0

Multi-subject consistency es **debilidad oficial admitida** de Seedance 2.0. Cuando hay 2+ personas en frame y deben mantenerse consistentes entre cuts, cada elemento extra que el modelo tiene que tracker simultáneamente es un punto de falla.

### Inventario de elementos que cuestan capacidad del modelo

| Elemento | Costo de tracking |
|---|---|
| Cara y peinado de cada persona | Alto — es lo principal a preservar |
| Outfit (color, tipo de ropa) | Medio — el modelo lo respeta razonable |
| Props con marca / color específico (iPhone, mic clip-on rosa, marca visible) | Muy alto — derivan entre cuts |
| Props genéricos (libro, vaso, micro de mano sin color) | Bajo |
| Setting con detalles específicos (textos legibles, logos al fondo) | Alto |
| Setting genérico (calle, cocina, cuarto) | Bajo |
| Transformación visual (piel mejorando, producto cambiando) | Alto — pedir delta exagerado |

### Regla operativa

**En escenas multi-subject de Seedance, minimizar props específicos a lo esencial.** Para cada prop, preguntarse: ¿la narrativa se lee sin él?
- **Sí** → sacarlo. Menos props = más capacidad para mantener caras + escena.
- **No** → simplificar a la versión más genérica posible (mic de mano corto sin color, no clip-on rosa específico).

### Caso real del framework

**Street vox-pop bloss** — iteré 3 versiones del mismo video. El clip-on mic rosa específico costó tanto tracking del modelo que el iPhone+mic derivaba entre cuts. Sacarlo + reemplazar el concept por "amiga que se acerca a otra en la calle" (sin iPhone, sin mic) resolvió en una iteración lo que las anteriores no pudieron. Ver `examples/bad/street_vox_pop_bloss_seedance_iteraciones.md`.

### Si el formato "exige" un prop específico para leer

Considerá un concept alternativo que cumpla la misma función comunicacional sin el prop:
- "Street vox-pop con mic" → "amiga que se topa con otra en la calle"
- "Influencer review con iPhone ring light" → "selfie a cámara casual sin equipo visible"
- "Doctor con bata y estetoscopio" → "profesional con buzo casual en consultorio"

El público lee el contexto por el guión + gesto + setting. El prop a veces es una muleta innecesaria que cuesta más de lo que aporta.

---

## Sujetos no-humanos (dummies, robots, mascotes)

Si el "personaje" del UGC no tiene cara humana, varias reglas estándar dejan de aplicar y otras toman su lugar.

### Qué NO usar
- "Natural skin texture with visible pores" → no aplica.
- "Micro-expresiones faciales" → no aplica (cara fija o de articulación limitada).
- Lip-sync humano nativo → falla.

### Qué SÍ usar
- **Textura del material real:** "matte gray polymer head with faint scratches and scuff marks", "fabric weave with visible threads", "ceramic glaze with hairline cracks". El espíritu de "skin realista" (evitar plástico-perfecto) se traslada a "evitar CGI-perfecto" en cualquier material.
- **Performance gestual:** la cara fija obliga a comunicar con manos, postura, head tilt, ritmo de movimiento. Sobre-dirigir los gestos: "left hand small open-palm 'you know' motion at 5s and 7s".
- **Articulación de boca puppet-style** si habla: "rigid ventriloquist-dummy jaw-drops, mouth slot opens only 5-8mm, NOT human lip-sync".
- **Identidad anchor visible:** marker, sticker, logo, color — algo único que el modelo pueda mantener entre shots. Para un crash test dummy: el círculo amarillo-verde en el temple. Para un robot: una LED de color. Sin un anchor, los modelos derivan rápido.

Ver `examples/good/ad_robot_selfie_cubano_15s.md`.

---

## Hook principle (primeros 1-2 segundos)

El primer segundo decide si el video convierte. Opciones que funcionan:

1. **Movimiento sorpresivo** — algo entra, se rompe, se derrama.
2. **Expresión facial intensa** — shock, risa, asco, duda.
3. **Pain point visual** — mostrar el problema antes del producto.
4. **Close-up de textura** — producto ultra cerca, piel, líquido.
5. **Frase-gancho** (testimonial) — "Nunca pensé que iba a decir esto, pero…"

El hook se **diseña en el first frame de Nano Banana**. Si el first frame es aburrido, el video arranca aburrido.

---

## Shot selection por tipo

### Testimonial
- **MCU (medium close-up)**: pecho hasta arriba de la cabeza. Cámara a altura de ojos.
- **Fondo con profundidad** — objeto identificable atrás, desenfocado.
- **Push-in muy lento** durante la toma para intensificar (Veo 3.1 lo hace limpio).

### Product demo
- **Alternar**: close-up producto en mano → hands-on action → reaction shot (cara).
- Usá **multi-shot de Kling 3.0** si entra en 10-15s.
- Si es single-shot: empezar con producto, pull-out a persona.

### Transformation
- **First frame = estado inicial explícito** (ej: piel sin producto).
- **Last frame = estado final explícito** (ej: piel con producto, luz igual).
- Lighting y framing **deben matchear** entre first y last — si no, el video mete saltos raros.

### B-roll
- **Single beat visual**, sin narrativa.
- Cámara estática o un solo movimiento (push-in, orbit).
- 3-5 segundos máximo.

---

## Movimiento de cámara — cuándo usar qué

| Movimiento | Efecto | Cuándo |
|-----------|--------|--------|
| Static hold | peso, atención | testimonial directo |
| Slow push-in | intensifica emoción | testimonial emocional, reveal |
| Pull-out | revela contexto | abrir escena, mostrar entorno |
| Handheld sway | autenticidad UGC | ad casual, selfie-style |
| Orbit | producto hero | beauty shot de producto |
| Whip-pan | transición rápida | multi-shot, corte de ritmo |
| Tilt down/up | descubrir | producto de pies a cabeza, o al revés |

**Siempre dar duración del movimiento** (ej: "slow push-in from MCU to CU over 3 seconds"). Sin duración, el modelo acelera o desacelera arbitrariamente.

---

## Audio design

Cuatro capas independientes. Especificar cada una. Ver `instructions/analysis.md` "Modo de audio" para la decisión native vs voz aparte.

1. **Diálogo** — qué, quién, cómo (ver execution.md). Si español regional + Kling: **NO native, voz aparte**.
2. **SFX diegéticos** — sonidos del mundo de la toma (fricción, líquido, puerta, teclado, beep de un dispositivo, click).
3. **Ambiente** — ruido de fondo de la locación (cuarto vacío, calle, café, room tone de departamento).
4. **Música** — sí/no. Si sí, decir género + función (diegética desde un parlante? no-diegética underscoring?).

Mood → audio default:
- **ASMR / sensorial:** sin música, SFX diegéticos amplificados.
- **Testimonial íntimo:** ambiente suave, sin música, diálogo prominente (voz aparte si es español).
- **Ad energético:** música no-diegética desde segundo 0, SFX en beats clave.
- **POV humorístico:** ambiente seco de casa, sin música (o muy ligera al final), SFX mínimos.

**Nota sobre SFX nativos:** Kling y Veo generan SFX nativos decentes (un beep, una puerta, fricción de tela) aunque el diálogo se haga off. Está OK dejar SFX on en el prompt; si salen mal se reemplazan en CapCut.
