# GOOD — Ad performance, B2B SaaS (indash itself)

## Brief received
> "Ad para Meta 9:16, 8 segundos, mostrando que indash genera 100 ads en 1 hora vs 1 semana de un equipo creativo. Tono: directo, un poco rebelde. Audio sí. Idioma: ES."

## Strategist context (one line above the prompt)
> 4-shot, Problem→Product→Payoff. Hook = el reloj contra el founder. Brand land en shot 4.

## The output (this is what gets delivered)

```
[4 shots, 8s, 9:16, audio: on] — Oficina vacía a las 2 AM, paleta azul frío + ámbar de lámpara, low-key con prácticos en escritorio.

[0s]   Toma 1 — Reloj de pared marcando 02:00. Segundero salta una vez. Camera: extreme close-up, slow dolly-in. Único haz ámbar sobre las agujas, fondo en negro.
[1.2s] Toma 2 — Founder sola en escritorio rodeada de 14 mockups impresos. Empuja una pila al piso. Camera: medium-wide, handheld con micro-shake. Monitor azul como key, ámbar de lámpara como rim.
[3.0s] Toma 3 — Mano sobre trackpad. Un solo click. Camera: tight close-up sobre nudillos, locked. Resplandor azul del monitor sobre la piel, sin más luz.
[5.5s] Toma 4 — Pantalla del laptop en grilla 4x4 de variantes de ad apareciendo simultáneas, logo "indash" abajo a la derecha. Camera: medium-wide, slow dolly-out. Azul monitor llena el cuarto, ámbar atenuado.

References: 
- (none provided)

Audio:
Pulso de sub-bajo desde 0s, snare seco en el corte a Toma 2, glitch eléctrico corto en el click de Toma 3, sting con sub-bajo + voz suave femenina ("100 ads. Una hora.") sobre Toma 4. Sin música ambiente entre shots.

api_params:
  model: seedance-2.0
  duration_s: 8
  aspect_ratio: 9:16
  resolution: 1080p
  fps: 24
  generate_audio: true
  creativity_scale: 0.6
  temporal_smoothing: 0.4
```

## Why this is GOOD
- **One subject per shot**, one verb, one camera move.
- **Hook is a pattern interrupt**: a clock, not a person. Stops the scroll because it's not what an ad usually opens with.
- **Paleta concreta**: "azul frío + ámbar" — Seedance can render that. Not "moody lighting".
- **Brand lands in shot 4**, never shot 1. Logo is small in frame, peripheral.
- **Audio is specific**: instruments, sync points, voice copy with timing.
- **Shot durations sum to 8.0s**. Math works.
- **No banned words**: no "stunning", no "epic", no "cinematic" alone.
- **Spanish output but camera terms in English**: `dolly-in`, `close-up`, `handheld`, `locked` — keeps Seedance fidelity.
- **Concrete numbers in voice ("100 ads. Una hora.")** are short enough to render legibly + match the brief's value prop.
