# Motion Prompts — Para `generate_video` del MCP de indash

Este archivo aplica **solo cuando se está ejecutando vía el MCP de indash** (`generate_video`), no cuando se entrega un shot list de texto para copy-paste a Seedance externo.

El motion prompt es un género distinto al shot list multi-shot. Su trabajo: describir **qué se mueve y cómo en los N segundos del render**, partiendo de un frame 0 que ya define la composición.

---

## Restricciones duras del MCP

- **Budget**: 30–60 palabras óptimo. Más de 80 baja la coherencia.
- **Sin timestamps** (`[Xs]`) — el MCP no usa Seedance multi-shot interno. Un motion prompt = una toma continua.
- **Sin `Camera:` blocks formales** — el vocabulario sigue siendo cinematográfico pero en prosa, no en estructura.
- **Sin `References:` block** — los roles de refs se manejan vía la API (`reference_image_url`).
- **Sin `Audio:` block** — el audio se controla con `generate_audio: bool` (o `audio_direction` si el MCP lo expone).

---

## Anatomía del motion prompt

Cuatro elementos, en orden:

1. **Acción inicial** — qué pasa en el frame 0 (vincula con la imagen que vio el modelo).
2. **Movimiento de cámara** — un solo verbo del [`camera_vocabulary.md`](camera_vocabulary.md).
3. **Cambio durante la toma** — qué se mueve, cómo evoluciona la escena.
4. **Estado final** — opcional, el "donde termina".

Pattern:
```
<Acción inicial>. Camera <movement keyword>. <Cambio durante la toma>. <Estado final, opcional>.
```

---

## Reglas (heredan de `style/writing_rules.md`)

- ≤2 adjetivos por sustantivo, ambos observables.
- Sin banned words (stunning, cinematic alone, epic, etc.).
- **Un solo movimiento de cámara** por motion prompt (este MCP no soporta cortes internos — no podés "pan then dolly").
- Vocabulario de cámara cerrado, en inglés (Seedance lee EN).
- Acción inicial debe ser **consistente con el frame 0** — no contradecir lo que el modelo ya tiene como ref.
- El verbo de cámara va en inglés (`slow dolly-in`, `tracking left`, `slow push-in`); el resto puede ir en el idioma del brief.

---

## Templates por intención

### Hero shot estático con vida (frasco, producto)
```
The <subject> rests on a matte surface. Slow dolly-in over 6 seconds, holding the subject centered. Warm key light grazes the label as the camera approaches; rim light deepens. Final frame: subject fills frame, label legible.
```
(~45 palabras)

### Action shot — algo cae / impacta
```
A <object> drops into frame from above and bounces once on the surface. Camera locked, shallow depth of field. Subtle ripple in shadows on impact, dust settling. Final frame: subject at rest, single highlight on its top edge.
```
(~40 palabras)

### Human gesture — mano, cara parcial
```
The <subject>'s hand enters frame from the right, picks up the <object>, lifts it 5cm. Camera in tight close-up, slow push-in following the hand. Warm light on knuckles, soft fall-off behind.
```
(~35 palabras)

### Reveal — pull back desde detalle
```
Start tight on <detail>. Slow dolly-out reveals <wider context> over 8 seconds. Light shifts from single key to ambient as more of the scene appears. Final frame: <wider composition with subject still anchored>.
```
(~40 palabras)

### Reposed product card — para final brand land
```
The <product> sits centered, surrounded by negative space. Camera locked with micro-drift. Light pulses once, very subtle, warm-to-cool. Final frame: product unchanged, badge "<X>" remains legible.
```
(~35 palabras)

---

## Lo que no funciona en motion prompts (anti-patrones)

### Multi-shot disfrazado de uno
**Mal**: `The bottle drops. Then the hand picks it up. Then we see the person smiling.`
→ Son 3 tomas. Este MCP hace 1 toma. Resultado: el modelo intenta meter cortes y sale glitchy.

### Acción inconsistente con el frame 0
Frame 0: cápsula apoyada quieta sobre mesa.
**Mal**: `The capsule falls from above and bounces.`
→ El modelo arranca con la cápsula ya en reposo y trata de animar una caída desde reposo. Sale antinatural.
**Bien**: `The capsule rests on the surface. Slow dolly-in. A subtle shadow shifts as the light pulses.`

### Verbos vagos
**Mal**: `Beautiful camera movement showcasing the product dynamically.`
→ Banned words + sin dirección.
**Bien**: `Camera slow dolly-in. Subject holds position. Light hardens on the label edge.`

### Demasiada narrativa
**Mal**: `The product represents wellness and balance in modern life, the camera capturing its essence.`
→ El modelo no procesa intención abstracta. Solo física.
**Bien**: `Slow orbit around the product, holding it centered. Light rotates from camera-left to camera-right with the movement.`

---

## Audio direction (cuando el MCP la soporte)

Si el MCP expone `audio_direction: string` aparte del bool `generate_audio`, escribir en paralelo al motion prompt, ≤40 palabras:

```
Sub-bass pulse from 0s. Soft synth pad swells through the dolly-in. Single warm bell tone on final frame. No voice.
```

Mientras `audio_direction` no exista (estado actual del MCP), el audio sale **genérico** y no se puede controlar finamente — aceptarlo o pedir el feature (gap E del [`la documentación del MCP de Indash`](../../la documentación del MCP de Indash)).

---

## Sanity checklist antes de mandar a `generate_video`

- [ ] ≤60 palabras.
- [ ] Una sola acción principal + un solo movimiento de cámara.
- [ ] Sin timestamps `[Xs]`.
- [ ] Sin banned words.
- [ ] La acción inicial es **plausible** desde el frame 0 (no contradice la pose congelada).
- [ ] El verbo de cámara está en el vocabulario cerrado.
- [ ] Si el brief pedía audio narrado, está en `audio_direction` (cuando exista) — no embebido en el motion prompt.
