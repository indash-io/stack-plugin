# GOOD — Product demo, B2B dashboard (silent, sound-off)

## Brief received
> "Product demo for a content analytics dashboard. 16:9, 10s, no audio (will be played in feed silently with captions). Show: marketer logs in, sees a spike in performance, smiles. Language: EN."

## Strategist context
> 5-shot Build arc. After-state revealed in shot 4 — the spike. Smile lands in shot 5 as the human payoff.

## The output

```
[5 shots, 10s, 16:9, audio: off] — Soft daylight studio workspace, matte oak desk + warm white walls, single coral accent on water bottle.

[0s]   Shot 1 — Coffee cup with steam. Steam rises slowly. Camera: tight close-up, locked. Soft window light from camera-left, warm.
[1.8s] Shot 2 — Marketer at her desk, mid-30s, hoodie. Lifts the laptop lid. Camera: medium, slow dolly-in. Same daylight key, soft fill from white wall.
[3.5s] Shot 3 — Hands on trackpad. Single tap. Camera: extreme close-up, locked. Cool monitor glow on knuckles, warm rim from window.
[6.2s] Shot 4 — Laptop screen at 30-degree angle showing a green line graph rising sharply, single coral data point at the peak. Camera: medium close-up, slow dolly-in. Cool monitor glow dominates frame.
[8.5s] Shot 5 — Marketer's face in 3/4 profile, holds a quiet smile. Camera: medium close-up, locked with micro-drift. Soft daylight on cheek, monitor glow on glasses.

References:
- (none provided)

Audio: off (designed for sound-off playback inside indash; captions handled by the editor layer).

api_params:
  model: seedance-2.0
  duration_s: 10
  aspect_ratio: 16:9
  resolution: 1080p
  fps: 24
  generate_audio: false
  creativity_scale: 0.35
  temporal_smoothing: 0.6
```

## Why this is GOOD
- **Doesn't start with the dashboard.** Opens on coffee → human → action → result → human reaction. Demo arc, not UI tour.
- **The screen is shown at 30°**, not pixel-perfect. Avoids Seedance UI hallucination.
- **One feature illustrated**: a rising line. Not 5 charts. Not a navigation tour.
- **Single accent color (coral)** keeps the data point legible against the cool monitor glow.
- **Final smile is held**, not exaggerated. "Quiet smile" + "micro-drift" is a directorial choice that reads on a feed.
- **`creativity_scale: 0.35`** — low, because UI fidelity matters here.
- **`temporal_smoothing: 0.6`** — high, to keep screen content stable.
- **Audio off, explicit reason given.** Tells indash's post-prod layer it's a captions-only video.
