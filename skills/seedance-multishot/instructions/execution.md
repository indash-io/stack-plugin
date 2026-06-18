# Execution

Now you assemble the final Seedance 2.0 prompt. The shot scratchpad from `strategy.md` is your input. The ref audit from `instructions/input_processing.md` is also required input. Use the matching template in `templates/` as the structural skeleton.

## Pre-flight: confirm the ref gate passed

Before writing a single line of prompt, verify the ref audit gate from `instructions/input_processing.md` passed (i.e., no `missing_critical` refs). If the gate fired and refs are still missing, **stop and ask the user**. Do not write the prompt.

## The Seedance 2.0 prompt anatomy

A correct multi-shot output has 6 blocks, in this order:

1. **Strategist context line** (above the prompt — 1 sentence)
2. **REFS A SUBIR callout** (above the prompt — operator-facing instructions on what to attach to the API)
3. **Header**: shot count + total duration + aspect ratio + audio flag
4. **Shot timeline**: numbered shots with timestamps
5. **Reference & audio addendum**: ref roles documented for the model + audio direction
6. **Suggested API params**: a small JSON-style block at the bottom

Blocks 1–2 are user-facing operator instructions. Blocks 3–6 are the prompt itself (what indash sends to Seedance).

## Block 1 — Header (always one line)

Format:
```
[N shots, Ts, A:R, audio: on/off] — [Master line]
```

Examples:
- `[5 shots, 8s, 9:16, audio: on] — High-contrast neon-noir office at 2 AM, cool blue + amber practicals.`
- `[3 shots, 6s, 16:9, audio: off] — Soft daylight studio, matte pastel surfaces, product hero on white.`

## Block 2 — Master atmosphere (already inside the header line)

Lock the world ONCE so the model doesn't drift. Contains:
- Genre / register (corporate-clean, neon-noir, golden-hour-doc, sterile-clinical, gritty-handheld, etc.)
- Color palette (2–3 colors max)
- Light key (high-key / low-key / motivated / practical)
- Optional: era/style reference (e.g., "shot on 35mm", "modern smartphone footage", "Apple keynote aesthetic")

## Block 3 — Shot timeline

Use timestamp markers. Each shot is a 4-part sentence:

```
[0s] Shot 1 — Subject. Action (one verb). Camera: size + movement. Light/atmosphere.
[1.5s] Shot 2 — ...
```

**Rules per shot**:
- ONE subject. ONE action. ONE camera move.
- Size keyword first in camera block: `ECU | close-up | medium | medium-wide | wide | extreme-wide`.
- Movement keyword from the allowed list in `reference/camera_vocabulary.md`.
- Last fragment is light/atmosphere — short, sensory, concrete.
- Never use: "cinematic", "stunning", "epic", "breathtaking", "mesmerizing".
- Avoid stacking adjectives. Two adjectives per noun max.

**Bad**: `Shot 1 — A beautiful, stunning, cinematic woman walks elegantly through a breathtaking office while the camera captures her epic energy from multiple angles with dynamic movement.`

**Good**: `[0s] Shot 1 — Founder at a glass desk. Types one keystroke. Camera: tight close-up on hands, slow dolly-in. Cool monitor glow on knuckles, otherwise dark.`

## Block 0 — Strategist context (1 line, above the prompt)

One sentence that names the arc, the hook, and the hero shot. Example:
> "4-shot, Problem→Product→Payoff. Hook = el dolor reconocido, no actuado. La marca se ve sola en Toma 3."

If RECOMMENDED refs are missing, append a half-sentence flag here. Example:
> "...La marca se ve sola en Toma 3. (Falta ref de talent — Seedance va a tirar una cara genérica; aceptable para esta iteración.)"

## Block 0.5 — REFS A SUBIR callout (operator-facing, above the prompt)

This block tells the indash user / operator EXACTLY which files to attach to the API call. It is NOT part of the prompt that goes to Seedance — it is instructions for the human/system between the skill and the API.

Format (always in user's `LANGUAGE`):

EN:
```
▸ REFS TO ATTACH BEFORE EXECUTING (n total)
1. <filename or concrete description of the asset> → role: <role(s)>
   Why: <one line explaining why this ref is needed and what breaks without it>
2. ...
```

ES:
```
▸ REFS A SUBIR ANTES DE EJECUTAR (n total)
1. <nombre del archivo o descripción concreta del asset> → role: <role(s)>
   Por qué: <una línea explicando por qué se necesita y qué se rompe sin ella>
2. ...
```

Rules for this block:
- Reference each ref by a concrete identifier the user can recognize ("the lifestyle photo of the model with the device", "el hero del producto en fondo blanco"). NOT abstract names like "ref_image_1" — those are for the model, not the human.
- Order: CRITICAL refs first, then RECOMMENDED, then OPTIONAL (including refs generated via Nano Banana in step 3.5). Numeric order MUST match the in-prompt `References:` block.
- Each ref has exactly ONE "Why" line, ≤ 25 words. State the consequence of missing it.
- If the user already attached the ref in this turn (e.g., they shared images directly in chat), say so: "(ya pasaste esta imagen — usar tal cual)".
- If a ref was generated via Nano Banana in step 3.5, tag it: "(generada con Nano Banana — guardar para reusar)" so the operator knows the provenance.
- If a RECOMMENDED ref is missing entirely (user picked C in the ASK), list it as "Recomendada (no provista — Seedance aproxima)" with a Why line — do NOT silently ignore.
- If NO refs are required (pure T2V case — generic concept, no specific brand element, and user said "skip todo"), replace this whole block with one line: `▸ No refs required (text-to-video).`

## Block 4 — Reference & audio addendum (in-prompt, model-facing)

This block is INSIDE the prompt that Seedance reads. It documents what each attached ref means in semantic terms so the model knows how to use them.

If refs were provided, list them with role:
```
References:
- ref_image_1 (style): matches the lighting key and matte texture
- ref_image_2 (subject): the founder's face/wardrobe
- ref_video_1 (motion): handheld energy of shot 3
- ref_audio_1 (audio): tone and BPM of the music bed
```

The numeric ID `ref_image_n` is positional — it must match the order in which the refs are attached to the API call (and therefore the order in the operator-facing "REFS A SUBIR" block above).

If audio is on, write a one-paragraph audio direction:
```
Audio: low synth pad enters at shot 1, builds tension. Single snare hit on the cut to shot 3. Founder voice (single line, soft): "We did this in a Tuesday." Music drops out under final shot. No ambient room tone.
```

If audio is off:
```
Audio: off (silent, designed for sound-off feed playback).
```

## Block 5 — Suggested API params (optional but useful)

Append a small JSON-ish block so indash can pass it directly:

```
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

**Defaults by use case** (override only with reason):
| Use case        | creativity_scale | temporal_smoothing | resolution |
|-----------------|------------------|--------------------|------------|
| ad_performance  | 0.6              | 0.4                | 1080p      |
| product_demo    | 0.35             | 0.6                | 1080p      |
| organic_social  | 0.7              | 0.3                | 1080p      |
| brand_film      | 0.5              | 0.6                | 1080p      |

Higher `creativity_scale` = more deviation from prompt. Higher `temporal_smoothing` = less flicker but less motion energy.

## Language switch

If `LANGUAGE = ES`, translate the prompt blocks into Spanish but **keep the camera vocabulary and parameter names in English** — Seedance is trained mostly on English camera terms, and `creativity_scale`/`generate_audio` are param keys. So:

- `Shot` → `Toma`
- `close-up` → `close-up` (keep)
- `dolly-in` → `dolly-in` (keep)
- `Audio` → `Audio`
- Atmosphere/action/subject text → translate

## Final delivery format

When you give the result to the user, format it exactly like this (and nothing else):

```
<Strategist context line — 1 sentence>

▸ REFS A SUBIR ANTES DE EJECUTAR (n total)
1. <concrete asset description> → role: <role(s)>
   Por qué: <one line>
2. ...

---

[Header line]

[0s] Shot 1 — ...
[Xs] Shot 2 — ...
...

References:
- ref_image_1 (<role>): <description for the model>
- ...

Audio:
...

api_params:
  ...
```

The `---` divider is a visual separator between the operator-facing layer (context + refs callout) and the prompt itself.

If no refs are required, replace the REFS A SUBIR block with:
```
▸ No refs required (text-to-video).
```

After delivering, run the validation in `eval/quality_checklist.md` against your own output. Fix and redeliver silently if it fails.
