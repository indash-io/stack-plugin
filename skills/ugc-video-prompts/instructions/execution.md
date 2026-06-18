# Execution — How to Write Each Prompt

Acá se redactan los prompts finales. Todos en **inglés** (los modelos rinden mejor). Diálogos dentro del prompt en **español con acento regional** entre comillas.

---

## Nano Banana — Structure

```
[Subject with specific identity] +
[Action / pose / expression] +
[Setting with concrete named objects] +
[Lighting: type + direction + quality + time of day] +
[Framing: shot size + angle + aspect ratio] +
[Style markers: photorealistic, device/film stock, lens] +
[Technical: DOF, grain, skin texture notes]
```

### Ejemplo (first frame — testimonial skincare)

```
25-year-old Argentine woman, curly dark brown hair pulled into a loose low bun with face-framing strands, no makeup visible skin with natural texture and faint freckles on cheekbones, wearing an oversized cream cotton sweatshirt. Holding a small amber glass serum bottle with a white dropper cap close to her jawline, looking down at the product with a soft curious micro-smile. Her own bedroom in morning: unmade white linen bed slightly blurred in the background, small ceramic lamp on the right, a green pothos plant barely visible top-left. Soft warm morning window light from camera-left, gentle shadow on the right side of her face. Medium close-up, eye-level, 9:16 vertical framing, subject's eyes at the upper third of the frame. Shot on iPhone 15 Pro, photorealistic, shallow depth of field, natural skin texture with visible pores and a slight sheen, subtle film grain, no retouching.
```

### Checklist por prompt de Nano Banana
- Sujeto: edad + origen/etnia + 2 rasgos físicos específicos + wardrobe concreto
- Acción o pose con **expresión** (no solo "posing")
- Setting: mínimo 2 objetos concretos nombrados
- Lighting: tipo (soft window / overcast / golden hour / practical lamp) + dirección (camera-left/right/behind) + momento del día
- Framing: shot size + ángulo + aspect ratio EXACTO
- Style: dispositivo o film stock (iPhone, 35mm film, Super 8, etc.)
- Skin: "natural skin texture with visible pores" si hay persona
- **Prohibido:** "beautiful", "professional", "amazing", "cinematic" solos sin descripción concreta

### Last frame — diferencias respecto al first
Si hay last frame, **mantener idénticos**: sujeto (mismo wardrobe, mismo pelo, misma iluminación), setting (mismos objetos), framing. Solo cambiar lo que tiene que cambiar (pose, expresión, estado del producto, etc.). Describir el cambio explícito.

---

## Kling 3.0 — Video Prompt Structure

Kling 3.0 premia **claridad narrativa + timing**. Menos terminología cinematográfica densa, más descripción de acción con tiempos.

```
[Opening state — describe what the first frame looks like] →
[Camera movement with timing] →
[Subject action with beat-by-beat timing] →
[Environmental motion if applies] →
[Audio: "dialogue in regional Spanish" + SFX + ambient + music (or "no music")] →
[Closing state if last frame used]
[Duration: Xs]
```

### Ejemplo A — Kling 3.0, 10s, **diálogo nativo en inglés** (lip-sync nativo OK)

```
Opens on a 25-year-old woman in a cream sweatshirt holding an amber serum bottle near her jawline, soft morning window light from the left, her bedroom slightly blurred behind her.

From 0-3s: camera holds steady in medium close-up, she looks into the lens with a small curious smile and says in English: "Look, this is the one that changed my skin in two weeks."

From 3-6s: she unscrews the dropper cap with her right hand — subtle click sound. Camera does a slow 5cm push-in toward her jawline.

From 6-10s: she places the drop on her cheekbone, massages it gently with her ring finger in small circles. Soft fingertip-on-skin sound. She closes her eyes for half a second and opens them looking down at the bottle with a satisfied exhale.

Audio: diegetic only — fingertip-on-skin, fabric rustle, soft ambient bedroom tone. No music.

Duration: 10 seconds. 9:16 vertical.
```

### Ejemplo B — Kling 3.0, 15s, **diálogo en español + voz aparte + lipsync en post** (default actual)

```
Multi-shot testimonial, 15s, 9:16. Subject, wardrobe and setting as shown in first frame reference. Maintain element consistency throughout.

Shot 1 (0-5s): MCU as in reference, woman holding the amber serum bottle near her jawline. From 0.5s-4s her lips move in minimal conversational articulation synced to off-camera voice (no native audio generation). Subtle handheld micro-sway.

Shot 2 (5-10s): Cut to tight close-up of the dropper releasing one drop onto her cheekbone. Slow 3cm push-in over 5s. Fingertip-on-skin sound at 7s.

Shot 3 (10-15s): Cut back to MCU. From 11s-14s her lips articulate minimally to off-camera voice. Closes with a small closed-lip half-smile into the lens — matching last frame reference.

Audio:
- Dialogue: NO native audio. Lips articulate minimally to off-camera voice (added in post with lipsync, Argentine Rioplatense Spanish).
- SFX (diegetic): fingertip-on-skin at 7s, soft fabric rustle, room tone.
- Music: none.

Closing state: as shown in last frame reference.

Duration: 15s. 9:16 vertical.
```

**Cuándo elegir qué ejemplo:** ver `instructions/analysis.md` "Modo de audio". Resumen: español regional + Kling → siempre el formato del Ejemplo B (audio off, voz aparte, lipsync).

### Multi-shot syntax (Kling 3.0)
Si son varias tomas, enumerarlas con "Shot 1 / Shot 2 / Shot 3" y dar duración de cada una. Element Consistency se activa solo cuando el prompt referencia al mismo sujeto/producto ("the same woman", "the same amber bottle from Shot 1").

### Multi-clip syntax (Kling 3.0, para videos >15s)

Cuando el video supera 15s, se parte en N clips Kling separados y se pegan en CapCut. **Cada clip es un prompt independiente**, no un mega-prompt con "Clip 1 / Clip 2".

Para que el corte entre clips no se sienta rupturado:
- **Wardrobe + setting + lighting idénticos** en first frame de cada clip.
- **Mismo color grading** en todos los prompts (ej: "warm late-afternoon natural light from camera-right").
- **Continuidad lógica de acción** entre last frame del Clip N y first frame del Clip N+1 (ej: termina el Clip 1 con el actor sosteniendo el celular, arranca Clip 2 con el mismo actor sosteniendo ya el producto físico — el corte se entiende como "más tarde ese día").
- **Repetir element consistency anchor** en cada prompt: "Same 30-year-old Argentine man as shown in Clip 1 reference frames".

Ver `examples/good/pov_novio_mia_30s.md`.

---

## Veo 3.1 — Video Prompt Structure

Veo 3.1 premia **densidad técnica cinematográfica + direcciones de actuación**.

```
[Shot type + lens + angle] +
[Subject + wardrobe + specific action with beats] +
["Dialogue" in regional Spanish (delivery direction in parens)] +
[Camera movement: specific term + distance + duration] +
[Lighting: key + fill + practicals] +
[Sound design: diegetic + non-diegetic] +
[Duration]
```

### Ejemplo (Veo 3.1, 6s testimonial con diálogo)

```
Medium close-up, 50mm lens, eye-level. 25-year-old Argentine woman with curly dark brown hair in a loose low bun, no makeup, wearing an oversized cream cotton sweatshirt. She holds a small amber glass serum bottle with a white dropper cap near her jawline. She tilts her head slightly left and looks directly into the lens.

She says in Argentine Spanish, softly and intimately, as if sharing a secret with a friend: "Mirá qué rápido se absorbe este serum."

(Delivery: whispered-conversational, slight smile on "rápido", no exaggeration.)

Slow 10cm handheld push-in over the full duration, subtle organic micro-shake. Warm natural window light from camera-left as key, soft bounce from a white wall on camera-right as fill, no practicals. Shallow depth of field, background bedroom slightly blurred.

Sound: diegetic fingertip-on-skin and subtle fabric shift at 4s. Quiet room tone. No music.

Duration: 6 seconds. 9:16 vertical.
```

### Reglas específicas de Veo 3.1
- **Lens** explícito (35mm / 50mm / 85mm) — mejora la consistencia.
- **Movimiento de cámara** en términos técnicos (dolly, track, whip-pan, crane, push-in, pull-out, orbit).
- **Dirección de actuación** entre paréntesis después de la línea — Veo la respeta.
- **Key / fill / practicals** — desglose explícito de luces si hay más de una.

---

## Seedance 2.0 — Video Prompt Structure

Seedance 2.0 premia **claridad estructural + referencias declaradas + timeline explícito**. El estilo es "shot list", no "creative writing". La frase rectora del modelo: *"do not sound clever. sound clear."*

```
[Asset declarations: @image1 as [role], @video1 as [role], @audio1 as [role], ...] →
[Subject + identity anchors from references] →
[Timeline beat-by-beat: 0-Xs: action / Xs-Ys: action / ...] →
[Camera behavior per beat: physical verb + distance + duration] →
[Environment + lighting per beat] →
[Sound design per beat: dialogue / music / SFX / ambient] →
[Constraints: aspect ratio, duration, what NOT to do]
```

### Sintaxis de referencias multimodales

- **Imágenes:** `@image1 as front-face reference`, `@image2 as outfit reference`, `@image3 as product reference (maintain label and color exactly)`.
- **Videos:** `@video1 as camera movement reference, copy the push-in pacing`, `@video2 as color grading and mood reference`.
- **Audio:** `@audio1 as background music reference, cut on strong beats`, `@audio2 as voiceover tone reference (conversational intimate)`.
- Cada slot tiene rol explícito. Sin rol, el modelo infiere y deriva.

### Ejemplo A — Seedance 2.0, 12s I2V + R2V, **inglés native audio** (look commercial/premium)

```
@image1 as product reference (30ml amber glass serum bottle, white dropper cap, beige minimal label — maintain exactly).
@image2 as cast reference (28-year-old Argentine woman, curly dark brown hair in low bun, no makeup, cream cotton sweatshirt).
@video1 as camera reference (copy the slow handheld push-in pacing).
@audio1 as music reference (use as background score, restrained downtempo with airy synth pads).

0-3s: Centered MCU of the woman from @image2 holding the serum bottle from @image1 near her jawline. She looks into the lens, small curious half-smile. Soft warm morning window light from camera-left.

3-7s: Slow 8cm handheld push-in toward her jawline matching the pacing of @video1. She unscrews the dropper with her right hand — clean click. She says in English: "This is the one that actually changed my skin."

7-12s: She places one drop on her cheekbone, massages in two small circles with the ring finger over 3s. Camera holds steady. Closes with a slow exhale, eyes drifting down to the bottle.

Sound: dialogue native English (intimate conversational delivery, close-mic). Music from @audio1, ducked under the dialogue from 3-7s. Diegetic SFX: dropper click at 4.5s, fingertip-on-skin from 7s onward. Room tone underneath.

Constraints: 9:16 vertical, 12 seconds, 1080p. No on-screen text. Single continuous handheld take, no cuts.
```

### Ejemplo B — Seedance 2.0, 15s multi-shot, **español argentino + voz aparte + lipsync en post**

```
@image1 as cast reference (28-year-old Argentine woman, low bun, oversized cream sweatshirt — same person across all shots).
@image2 as product reference (amber serum bottle, white dropper, beige label).
@image3 as setting reference (bedroom interior tone: white linen, ceramic lamp, pothos plant).

Shot 1 (0-5s): MCU of the woman from @image1 in the setting from @image3, holding the product from @image2 near her jawline. From 0.5-4s her lips move in minimal conversational articulation synced to off-camera voice (no native audio generation). Subtle handheld micro-sway. Soft warm morning window light from camera-left.

Shot 2 (5-10s): Cut to tight close-up of the dropper releasing one drop onto her cheekbone. Slow 4cm push-in over 5s. Fingertip-on-skin SFX at 7s.

Shot 3 (10-15s): Cut back to MCU as in Shot 1. From 11-14s her lips articulate minimally to off-camera voice. Closes with a small closed-lip half-smile into the lens.

Sound: dialogue OFF — lips articulate to off-camera voice, added in post with lipsync (Argentine Rioplatense Spanish). SFX diegetic ON: dropper click, fingertip-on-skin, fabric rustle, soft bedroom room tone. Music: none.

Constraints: 9:16 vertical, 15 seconds, 1080p. Maintain element consistency for cast (@image1), product (@image2), and setting (@image3) across all three shots. UGC handheld feel: subtle micro-shake throughout, natural window light only, no studio lighting, no commercial color grading.
```

### Reglas específicas de Seedance 2.0

- **Verbos físicos específicos** (snap, melt, fracture, twist, drip, stretch, implode) > verbos abstractos (becomes, transforms, changes). El modelo responde mejor a lo concreto.
- **Timeline obligatorio** en formato `0-3s: ... / 3-6s: ...`. La descripción narrativa en paragraph form rinde peor.
- **Cada `@asset` con rol explícito.** Subir referencias sin declarar rol es la causa #1 de output que deriva.
- **Sound como parte del brief**, no como afterthought. Especificar diálogo / música / SFX / ambient por beat.
- **Look UGC requiere sobre-dirección.** Seedance default-ea a commercial/premium. Para UGC: `subtle handheld micro-shake, natural window light, no studio lighting, no color grading, iPhone POV framing`. Si tenés un clip UGC real de referencia, subilo como `@video1 as aesthetic reference`.
- **Constraints negativos al final** ayudan ("no on-screen text", "no cuts", "no commercial polish") — el modelo respeta la lista de "no".
- **Multi-shot en un solo prompt** funciona (sin necesidad de split). Es preferible a multi-clip cuando entrás en 15s.
- **Video extension nativa:** si el pedido es "continuar un video existente", usar la sintaxis `Extend @video1 by Xs + [solo describir lo nuevo, no repetir el clip original]`. No reescribir el clip entero.
- **Text rendering flojo:** evitar carteles, números o logos legibles dentro del frame. Si son no-negociables, agregarlos en post.
- **Audio distortion ocasional:** revisar el clip exportado al recibirlo. Si hay distorsión, regenerar con menos densidad de capas de audio o mover una capa a post.
- **Articulación expresiva sin necesidad de audio ON.** Para escenas con personas hablando donde el audio nativo está OFF (regla del framework para español regional), NO escribir `minimal conversational articulation` (el video queda muerto). Escribir: `natural full conversational articulation as if speaking, lips move continuously and expressively, full mouth movement, not minimal, not stiff. No native audio dialogue generation — voice will be added in post with lipsync`. Esto da articulación rica al lipsync de post sin alucinar audio. NO activar `generate_audio: true` pensando que ayuda al dinamismo en español — es trade-off falso, el audio en español aluciña siempre. Ver `style/writing_rules.md` regla 33 y `examples/bad/street_vox_pop_bloss_seedance_iteraciones.md` iteración 2.
- **Multi-subject = minimalismo de props.** En escenas con 2+ personas, cada prop específico (color exacto, marca visible, micro-detalle) que tiene que mantenerse consistente entre cuts es punto de falla. Minimizar a lo esencial. Si un prop "parece necesario" para leer el formato, preguntarse: ¿la narrativa se lee sin él? Si sí → sacarlo. Ver `instructions/strategy.md` sección "Minimalismo de elementos en multi-subject Seedance".

---

## Reglas comunes a los tres modelos de video

1. **Cada beat de acción lleva un tiempo** ("at 3s", "from 0-2s", "over the full duration").
2. **Diálogo entre comillas + idioma + acento + dirección** en paréntesis.
3. **Audio desglosado** en capas: diálogo / SFX / ambiente / música (o "no music").
4. **Cámara con verbo + dirección + duración**.
5. **Lighting con tipo + dirección + calidad + momento** si aplica.
6. **Duración total y aspect ratio siempre al final** del prompt.
7. Si hay last frame, describir **closing state** al final del prompt (ambos modelos lo usan como guía).
8. **No redundancia** con el frame de referencia — si el first frame ya muestra wardrobe/setting/lighting, el prompt de video solo dice "as shown in reference" y se enfoca en acción + cámara + audio.
9. **Cap duro: 2500 caracteres** (incluyendo espacios y saltos de línea), aplica a Kling 3.0, Veo 3.1 y Seedance 2.0. Si el draft pasa, comprimir en este orden: (a) reemplazar descripciones de sujeto/wardrobe/setting/lighting por `as shown in reference` o `as in @image1`; (b) consolidar delivery directions en una sola paréntesis por línea; (c) sacar la descripción del producto en shots 2+ si ya está en shot 1 + frame (`the same watch`, `the bottle from @image2`); (d) cortar adverbios y frases de relleno. Nunca comprimir sacando beats con timing, diálogo literal ni desglose de audio.

---

## Persistencia del paquete

El paquete final **no se muestra solo en el chat: se guarda en disco**. Es la última acción del workflow (paso 10), después de pasar el checklist.

**Dónde:** en `entregables/videos/` de la carpeta del cliente.
- Si la subcarpeta `videos/` no existe dentro de `entregables/`, creala.
- Si estás trabajando **dentro de una carpeta de cliente** (tiene `entregables/`), guardá ahí.
- Si **no** hay estructura de cliente en el directorio actual, guardá en `./entregables/videos/` del directorio de trabajo (creándolo) y avisale al usuario que conviene dar de alta el cliente con `new-client` para tener todo ordenado.

**Nombre del archivo:** `<AAAA-MM-DD>_<concepto-slug>_v<N>.md`
- `<AAAA-MM-DD>` = fecha del día.
- `<concepto-slug>` = nombre del concepto del video en kebab-case, sin acentos (ej: "Testimonial Serum AM" → `testimonial-serum-am`).
- `v<N>` = versión; `v1` la primera, subí el número en cada regeneración del mismo concepto/día.
- A/B → sufijo `-A` / `-B` (ej: `2026-06-17_testimonial-serum-am_v1-A.md`).

**Reglas de guardado (no negociables):**
1. **Siempre** mostrás el paquete en el chat **y además** lo guardás con el nombre canónico.
2. **Nunca** pises un archivo existente: si el nombre ya existe, subí la versión (`v2`, `v3`…).
3. Al entregar, decí en una línea exactamente dónde lo guardaste (la ruta).
4. Los **assets generados** de ese set (frames de Nano Banana, clips de video) van en una subcarpeta con el **mismo nombre sin `.md`**: `entregables/videos/2026-06-17_testimonial-serum-am_v1/`.

---

## Dialogue — regional Spanish

| Región | Marcadores |
|--------|-----------|
| Argentino | "vos", "mirá", "dale", "che", "re [adjetivo]", "está buenísimo", entonación rioplatense |
| Mexicano | "mira", "wey/güey" (contexto), "está padre", "checa", entonación mexicana |
| Colombiano | "mire", "parce", "qué chévere", "bacano", entonación paisa/bogotana |
| Español (ES) | "mira", "tío/tía", "mola", "vale", "joder" (contexto), entonación peninsular |
| Neutro LATAM | sin marcadores regionales, "mira", "está muy bueno", entonación plana |

**Siempre** aclarar el acento entre paréntesis después de la línea:
`"Mirá qué rápido se absorbe." (Argentine Spanish, Rioplatense accent)`

Esto le da a Veo 3.1 en especial la clave para el acento correcto.
