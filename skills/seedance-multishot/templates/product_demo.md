# Template — `product_demo`

For SaaS / B2B feature demos. The job is to make the value legible in <15s, not to tour the UI.

## Defaults
- Aspect ratio: `16:9` (default), `9:16` for mobile demos
- Duration: 8–12s (default 10s)
- Audio: usually OFF (or minimal — UI clicks + ambient bed); copy on screen via the indash captions layer
- Shots: 4–5
- Arc: **A. Problem → Product → Payoff** or **C. Build arc**
- Pacing: 0.3–0.5 cuts/sec — measured

## Default API params
```
creativity_scale: 0.35      # stay close to brief — UI fidelity matters
temporal_smoothing: 0.6     # less flicker for screen content
resolution: 1080p
fps: 24
generate_audio: false
```

## Shot job map (default 5-shot demo)

| Shot | Job          | Typical duration | Notes                                                    |
|------|--------------|------------------|----------------------------------------------------------|
| 1    | hook         | 1.5–2.0s         | The pain or the after-state — never the dashboard.       |
| 2    | setup        | 1.5–2.0s         | The user/operator at their environment.                  |
| 3    | demonstrate  | 2.5–3.0s         | The single action of value (one click, one keystroke).   |
| 4    | result       | 2.0–2.5s         | The output — outcome on screen, in real space.           |
| 5    | brand/CTA    | 1.0–1.5s         | Logo + product name. Short.                              |

## Demoing UI inside Seedance — what works, what doesn't

**Works**:
- A laptop on a desk with a screen visible from a slight angle (the screen is suggestive, not pixel-perfect).
- A close-up on a hand interacting with a trackpad/keyboard.
- An abstracted "after-state" (a chart that grew, an inbox that emptied, a calendar that filled).
- A specific UI element shot tight (one button, one notification, one toast).

**Does NOT work**:
- Trying to render a full functional dashboard with live data — Seedance will hallucinate UI.
- Long readable paragraphs of text on screen.
- Specific brand typography or pixel-accurate logos (use the indash post-prod layer for logos).

**Rule**: imply the product, don't render it.

## Filled-template skeleton

```
[5 shots, 10s, 16:9, audio: off] — Clean modern workspace, soft daylight, matte surfaces, single accent color <X>.

[0s]   Shot 1 — <Pain or after-state subject>. <Verb>. Camera: <size>, <movement>. <Light>.
[1.8s] Shot 2 — <User at their setup>. <Verb>. Camera: <size>, <movement>. <Light>.
[3.5s] Shot 3 — <Hands + UI close-up>. <Single action verb>. Camera: tight close-up, slow dolly-in. <Light>.
[6.2s] Shot 4 — <Outcome subject>. <Verb (the result appearing)>. Camera: <size>, <movement>. <Light>.
[8.5s] Shot 5 — <Workspace wide with brand element>. <Verb>. Camera: medium-wide, locked. <Light>.

References:
- <user-provided refs only>

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

## Common failures to avoid in demos
- **Starting with the dashboard**: viewers tune out. Start with the human or the pain.
- **Trying to show 3 features**: pick one. Demos that fit in <15s show one moment.
- **Realistic-looking UI mockups**: Seedance will render fake text. Use abstract / blurred / off-axis screens.
- **Voice-over without sound design**: if audio is on, it must include UI sfx, not just narration.
