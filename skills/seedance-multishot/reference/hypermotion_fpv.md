# Hypermotion — FPV / drone race (Seedance 2.0)

Movimiento de cámara continuo, agresivo, sin cortes internos: la cámara "vuela" como un drone FPV de racing atravesando el espacio, el producto, o entre obstáculos. Es la flavor de hypermotion más útil para B2B ads, brand films energéticos, recorridos de producto/espacio y hooks de retención alta.

**No confundir con**: dolly-in cinemático lento, tracking shot estándar, o steadycam. FPV es **velocidad + libertad de eje + parallax extremo**.

---

## Cuándo usar FPV (y cuándo NO)

### Sí — casos donde FPV gana
- **Hook de ad performance**: primeros 1.5s necesitan pattern interrupt visual. FPV atravesando algo lo da gratis.
- **Recorrido de producto multi-ángulo en un solo shot**: en vez de cortar a 3 planos, la cámara vuela 360° alrededor.
- **Recorrido de espacio (oficina, fábrica, retail)**: muestra escala + detalle en 4s sin cortes.
- **Transición A→B**: la cámara entra por una ventana / sale por otra / atraviesa un objeto y aparece en otra escena.
- **Brand film de marca con energía** (no luxury, no lujo silencioso).

### No — casos donde FPV mata el brief
- **Product demo educativo**: el viewer necesita entender una UI / proceso paso a paso. FPV lo marea.
- **Brand film luxury / quiet**: rompe el código del segmento. Usar dolly lento.
- **Talking head / testimonial**: la cara necesita estar quieta. Solo un FPV de entrada de 1s al inicio.
- **Duración >7s en un solo FPV continuo**: el modelo pierde coherencia. Cortá o reseteá.

---

## Gramática del prompt FPV

### Verbos de tránsito (elegir UNO por shot — no mezclar)
- `FPV drone races through [X]`
- `Camera hurtles past [X] toward [Y]`
- `Drone barrels into [X], threading between [Y] and [Z]`
- `FPV tears across [space], banking hard around [obstacle]`
- `Camera blasts through [opening], emerging into [new space]`
- `Drone weaves between [obstacles], climbing toward [target]`

### Movimiento de eje (clave de FPV — no es estable)
Sumar al verbo de tránsito uno de estos:
- `banking left/right`
- `rolling 90° as it passes [X]`
- `pitching up over [X]`
- `corkscrewing around [X]`
- `dipping under [X] and climbing past [Y]`

### Motion blur — explícito siempre
- `heavy motion blur on foreground elements`
- `streaks of [color/light] trailing past the lens`
- `parallax-heavy: near objects whip past, far objects drift`
- `lens distortion at edges from speed`

### Escala dinámica
- `starts tight on [detail], pulls wide as it exits`
- `macro on [X] at 0s, reveals full [space] by 2s`
- `enters at eye-level, climbs to bird's-eye by end`

### Anchor points (CRÍTICO)
FPV sin anchor points hace que Seedance alucine. Mencionar mínimo 2–3 objetos/superficies específicos por los que la cámara pasa, en orden:
- `passes the [bottle on counter] at 0.5s, banks past [signage] at 1.2s, threads between [two columns] at 2s, lands on [product hero] at 3s`

Sin esto, el modelo improvisa una trayectoria genérica.

---

## Parámetros técnicos óptimos

| Param | Valor | Por qué |
|---|---|---|
| `duration_seconds` | **3–5s** | >6s pierde coherencia de trayectoria. Si necesitás más, son 2 FPV cortos stitched. |
| `fps` | **30** | La cadencia rápida lee mejor el movimiento. 24 se ve "lento" para FPV. |
| `temporal_smoothing` | **0.1–0.2** | Alto aplana el motion blur. Bajo preserva la sensación de velocidad. |
| `creativity_scale` | **0.65–0.75** | Bajo (<0.5) frena el movimiento. Alto (>0.8) aluciona trayectoria. |
| `aspect_ratio` | **9:16 o 16:9** | 9:16 vende más en social — el FPV vertical es viral. |
| `resolution` | **1080p** | 480p destruye el motion blur fino, queda jelly. |
| `generate_audio` | **true** | FPV sin whoosh + impact sound queda muerto. |

**Nota MCP**: hoy el MCP de indash NO expone `fps`, `temporal_smoothing`, `creativity_scale`, `resolution`. Hasta que se exponga (ver MCP_GAPS_PROPOSAL.md), forzar estos params verbalmente dentro del prompt: `"shot at 30fps, low temporal smoothing, heavy motion blur preserved"`. El modelo lo respeta parcialmente.

---

## Audio direction para FPV (mandatory)

FPV sin audio sincronizado se siente plano. Patrón estándar:
- **0s — 0.3s**: low rumble building (drone takeoff feel)
- **Mid-shot — peak motion point**: whoosh sweep, panned hard (L→R o R→L según trayectoria)
- **Anchor points**: micro-impacts (sub kick) en cada pasada de objeto
- **Climax / landing**: sub drop + reverb tail
- **Voiceover (si hay)**: solo en el último 1.5s, después de que el motion se asienta. Nunca durante el peak.

Ejemplo de bloque `Audio:`:
```
Audio: Low sub rumble at 0s, builds. Hard whoosh sweep panning R→L
at 1.2s synced to camera bank. Three sub-kicks at 0.5s, 1.5s, 2.4s
matching object pass-bys. Sub drop + reverb tail at landing (3.2s).
No music bed — sound design only.
```

---

## Refs strategy para FPV

| Ref type | Necesidad | Por qué |
|---|---|---|
| **Imagen de producto** | CRITICAL si el producto es protagonista | Sin ref, Seedance aluciona forma/color/logo durante el flythrough |
| **Imagen de espacio/set** | RECOMMENDED | Define la "pista" del FPV — sin esto el espacio es genérico |
| **Video ref de motion FPV** | OPTIONAL pero gold | Si la pasás (nativo Seedance, no el MCP actual), el motion sale calcado |
| **Ref de paleta/luz** | RECOMMENDED | FPV con luz inconsistente entre anchor points queda raro |

**Nano Banana para frame 0 FPV**: el frame 0 debe ser el **punto de entrada** del FPV (no el final), con composición que deje "espacio hacia adelante" para que el motion tenga lugar a dónde ir. Ver `nano_banana_prompts.md` variante "frame 0 protagonista" + agregar `"composed with deep negative space in the direction of camera travel"`.

---

## Estructura del prompt FPV (single-shot 4–5s)

```
FPV drone races through [SPACE], threading between [ANCHOR_1] and
[ANCHOR_2], banking [LEFT/RIGHT] past [ANCHOR_3], landing tight on
[HERO_OBJECT/SUBJECT].

Camera: FPV drone, 30fps, heavy motion blur preserved, low temporal
smoothing. Lens distortion at edges. Starts [SCALE_IN], ends
[SCALE_OUT].

Lighting: [KEY_LIGHT_DESCRIPTION], consistent across the flythrough.
[Optional: practical light sources passing by at anchor points].

Pacing: continuous motion, no internal cuts. Peak speed at 1.5s,
slight deceleration on landing.

References: [REF_1 role: subject], [REF_2 role: space/palette].

Audio: [audio direction block].

api_params:
  model: seedance
  aspect_ratio: 9:16
  duration_seconds: 4
  generate_audio: true
```

---

## Ejemplos de output

### Ejemplo 1 — Ad performance, producto B2B (suplemento Omega 3)

```
FPV drone races through a minimal kitchen at dawn, threading
between a glass carafe and a ceramic bowl, banking right past a
sunlit window, landing tight on the Omega 3 bottle resting on
white marble.

Camera: FPV drone, 30fps, heavy motion blur preserved, low temporal
smoothing. Lens distortion at edges. Starts wide at room scale,
ends macro on bottle label.

Lighting: cool morning daylight from window-left, soft bounce on
marble. Practical warm pendant light passes overhead at 1.5s.

Pacing: continuous motion, no internal cuts. Peak speed at 2s,
slight deceleration as it approaches the bottle.

References: ref_1 (role: subject — product bottle), ref_2 (role:
space/palette — kitchen).

Audio: Low sub rumble building from 0s. Hard whoosh sweep L→R at
1.2s synced to bank. Sub kicks at 0.8s and 1.8s on object pass-bys.
Sub drop with short reverb tail as bottle fills frame at 3.5s.
No music bed.

api_params:
  model: seedance
  aspect_ratio: 9:16
  duration_seconds: 4
  generate_audio: true
```

### Ejemplo 2 — Brand film, recorrido de oficina/fábrica

```
FPV drone tears across an open-plan workspace, threading between
two standing desks, corkscrewing around a central pillar, blasting
through an open doorway, emerging into a warehouse where a single
worker assembles a unit.

Camera: FPV drone, 30fps, heavy motion blur on foreground,
parallax-heavy. Banks 45° around pillar at 2s. Ends eye-level on
worker's hands.

Lighting: cool office fluorescents transition to warm warehouse
tungsten as it crosses the doorway. Light shift sells the cut
without a cut.

Pacing: continuous, no internal cuts. Acceleration through pillar,
peak speed through doorway, deceleration on worker landing.

References: ref_1 (role: space — office), ref_2 (role: space —
warehouse), ref_3 (role: subject — worker hands).

Audio: Sub rumble + faint office ambience 0–1s. Whoosh sweep L→R
at 1.8s through doorway, ambience swap to warehouse tone. Single
metallic clink sync on hands at 3.8s. No VO.

api_params:
  model: seedance
  aspect_ratio: 16:9
  duration_seconds: 4
  generate_audio: true
```

---

## ⚠ Anti-pattern crítico: FPV + producto + persona en un solo shot

**No funciona.** Seedance se rompe consistentemente cuando le pedís:
- Mantener fidelidad de un producto específico (LCD, logo, color exacto)
- + Mantener fidelidad de una persona específica (cara, vestuario)
- + Movimiento FPV continuo de 4-5s

Una de las tres se aluciona, casi siempre. El producto cambia de forma a mitad de camino, o la mujer aparece con otra cara/ropa, o la trayectoria pierde coherencia.

**Solución obligatoria:** partir en 2 tomas stitched.
- Shot 1: FPV + producto. Sin persona. Landing en macro del producto.
- Shot 2: Persona + producto. Sin FPV. Motion sutil (respiración, mano).
- Stitch externo con whoosh + crossfade.

Si el brief pide las 3 cosas, **forzar `stitched_multishot` y avisar al user del costo extra antes de ejecutar**. Nunca prometer un single shot acá.

---

## Self-check FPV (correr antes de entregar)

- [ ] Un solo verbo de tránsito principal (no se mezclan).
- [ ] Mínimo 2 anchor points específicos mencionados en orden temporal.
- [ ] Motion blur explícito en el prompt.
- [ ] Escala dinámica declarada (start scale → end scale).
- [ ] Duración entre 3–5s (si pide más, partir en 2 FPV stitched).
- [ ] Audio direction con whoosh sync al peak motion.
- [ ] `fps: 30` declarado verbalmente si MCP no lo expone.
- [ ] Frame 0 (si se genera con Nano Banana) tiene negative space en la dirección de viaje.
- [ ] Refs de producto/espacio resueltas — no se confía al modelo a alucinar logo/cara.
- [ ] El prompt no contiene 2 movimientos contradictorios en el mismo shot.
