# Master Output Template

This is the canonical shape every Seedance 2.0 multi-shot output must follow. Use-case templates inherit from this.

---

## The full output (operator-facing layer + prompt layer)

```
<Strategist context line — one sentence naming arc, hook, and hero shot.>

▸ REFS A SUBIR ANTES DE EJECUTAR (n total)
1. <concrete file/asset description> → role: <role(s)>
   Por qué: <one line on what breaks without it>
2. ...

---

[N shots, Ts, A:R, audio: on/off] — <Master atmosphere line: genre, palette, light key>

[0s]   Shot 1 — <Subject>. <Action verb>. Camera: <size>, <movement>. <Light/atmosphere>.
[Xs]   Shot 2 — <Subject>. <Action verb>. Camera: <size>, <movement>. <Light/atmosphere>.
[Ys]   Shot 3 — <Subject>. <Action verb>. Camera: <size>, <movement>. <Light/atmosphere>.
...
[Zs]   Shot N — <Subject>. <Action verb>. Camera: <size>, <movement>. <Light/atmosphere>.

References:
- ref_<type>_<n> (<role>): <one-line description of what this ref contributes>

Audio:
<one paragraph: instruments, dynamics, sync points, voice if any> | off (designed for sound-off playback).

api_params:
  model: seedance-2.0
  duration_s: <T>
  aspect_ratio: <A:R>
  resolution: <480p|720p|1080p>
  fps: <24|30>
  generate_audio: <true|false>
  creativity_scale: <0.0–1.0>
  temporal_smoothing: <0.0–1.0>
```

The two layers:
- **Above the `---` divider**: operator instructions for the human or backend code that will hit the Seedance API. This part is NOT sent to Seedance.
- **Below the `---` divider**: the actual prompt text + parameters. This is what indash sends to the API.

If no refs are required (pure T2V), replace the REFS A SUBIR block with one line:
```
▸ No refs required (text-to-video).
```

The `ref_image_n` IDs in the in-prompt `References:` block must match the **order** of the REFS A SUBIR list above. Position 1 in the upload list = `ref_image_1` in the prompt.

---

## Block-by-block contract

### Strategist context line (above divider)
- Exactly one sentence.
- Names the arc, the hook, and what lands in which shot.
- May include a half-sentence flag if a RECOMMENDED ref is missing.
- Forbidden: hedging ("might", "could", "perhaps"), emojis, multiple sentences.

### REFS A SUBIR block (above divider)
- Header line: `▸ REFS A SUBIR ANTES DE EJECUTAR (n total)` in user's language. EN variant: `▸ REFS TO ATTACH BEFORE EXECUTING (n total)`.
- Numbered list, ordered: CRITICAL → RECOMMENDED → OPTIONAL (refs generated via Nano Banana in step 3.5 keep this order based on their assigned role).
- Each entry: 2 lines — first line is the asset description + role tag, second line starts with `Por qué:` (or `Why:` in EN) and explains what breaks without it.
- Asset descriptions are CONCRETE (filename, "the lifestyle photo with the model", "el hero del producto en fondo blanco"). Never abstract names like `ref_image_1` — those are for the in-prompt block.
- Provenance tags (optional, appended to the asset description):
  - `(ya pasaste esta imagen — usar tal cual)` — user shared in chat
  - `(generada con Nano Banana — guardar para reusar)` — produced via the step 3.5 generation flow
- If no refs required (user picked "skip todo" or pure T2V): single line `▸ No refs required (text-to-video).`

### `---` divider
- Three hyphens on their own line. Separates operator-facing from model-facing layers.

### Header
- One line, period at the end of the master atmosphere fragment.
- `[ ]` brackets contain ONLY: shot count, total duration in seconds, aspect ratio, audio flag.
- Master atmosphere = ≤ 25 words.

### Shot lines
- Format: `[Ts] Shot N — Subject. Action. Camera: size, movement. Light/atmosphere.`
- Period-separated fragments. Em-dash after `Shot N`.
- Timestamps cumulative from `[0s]`.
- One subject, one verb, one camera move, one light fragment.
- ≤ 30 words per shot.

### References block
- Header line: `References:`
- One bullet per ref: `- ref_<image|video|audio>_<n> (<style|subject|motion|palette|audio>): description`.
- Omit the entire block if user provided no refs. Do not write "no refs provided".

### Audio block
- Header line: `Audio:`
- If on: 1 paragraph, ≤ 40 words, names instruments + sync points.
- If off: `Audio: off (designed for sound-off playback).`

### api_params block
- YAML-style indentation, 2 spaces.
- Always include: model, duration_s, aspect_ratio, resolution, fps, generate_audio.
- Conditionally include: creativity_scale, temporal_smoothing.
- Use defaults from `instructions/execution.md` unless brief justifies otherwise.

---

## Spanish version (when LANGUAGE = ES)

Same structure, with these replacements:
- `Shot N` → `Toma N`
- `References:` → `Referencias:`
- `Audio:` → `Audio:` (same word, no change)
- All free-text fragments translated. Camera terms in English.

---

## Forbidden in any template
- Markdown headers inside the prompt (no `#`, `##`)
- Bullet points inside shot descriptions
- Multiple paragraphs per shot
- Comments to the user mid-prompt ("// note: this part is important")
- Decorative dividers inside the prompt
