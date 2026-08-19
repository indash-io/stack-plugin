# Template — `organic_social`

For TikTok / Reels / Shorts that should feel **native**, not paid. The job is brand association via algorithm-friendly form.

## Defaults
- Aspect ratio: `9:16` (default), `1:1` for IG feed
- Duration: 6–10s (default 8s)
- Audio: ON, often track-driven
- Shots: 4–5
- Arc: **D. Loop arc** (preferred) or **C. Build arc**
- Pacing: 0.4–0.6 cuts/sec

## Default API params
```
creativity_scale: 0.7        # native looseness
temporal_smoothing: 0.3      # keep handheld micro-motion
resolution: 1080p
fps: 30                      # social-native frame rate
generate_audio: true
```

## What "native" means by platform

| Platform | Visual code                                              | Audio code                                  |
|----------|----------------------------------------------------------|---------------------------------------------|
| TikTok   | handheld, vertical, jump cuts, on-screen text overlays   | trending track or POV monologue             |
| Reels    | slightly polished, color-graded, smoother cuts           | track-driven, beat-aligned                  |
| Shorts   | fast, info-dense, often "talking-to-camera"              | voice-forward                               |

If `organic_social` is the use case, ask which platform if not specified — it changes shot grammar.

## Shot job map (default 4-shot Loop arc, 8s)

| Shot | Job        | Typical duration | Notes                                                     |
|------|------------|------------------|-----------------------------------------------------------|
| 1    | hook       | 1.5–2.0s         | Native pattern interrupt — the kind that fits the FYP.    |
| 2    | escalate   | 2.0–2.5s         | Build curiosity or comedic tension.                       |
| 3    | reveal     | 2.0–2.5s         | The payoff (joke, insight, or aha).                       |
| 4    | loop-back  | 1.0–1.5s         | Visually rhymes with shot 1 so the reload feels seamless. |

## Filled-template skeleton (TikTok 9:16)

```
[4 shots, 8s, 9:16, audio: on] — Handheld native energy, varied natural light, casual <urban/home/office> setting.

[0s]   Shot 1 — <Hook subject>. <Casual native verb>. Camera: medium, handheld with micro-shake. <Light fragment>.
[1.8s] Shot 2 — <Tension/curiosity subject>. <Verb>. Camera: <size>, handheld. <Light>.
[4.0s] Shot 3 — <Reveal subject>. <Verb>. Camera: <size>, <movement>. <Light>.
[6.5s] Shot 4 — <Loop-back subject — visually echoes shot 1>. <Verb>. Camera: medium, handheld. <Light>.

References:
- <user-provided refs only>

Audio:
<trending-track-style beat from 0s; impact hit on cut to shot 3; track loops cleanly into shot 4 for rewatch>.

api_params:
  model: seedance-2.0
  duration_s: 8
  aspect_ratio: 9:16
  resolution: 1080p
  fps: 30
  generate_audio: true
  creativity_scale: 0.7
  temporal_smoothing: 0.3
```

## Common failures to avoid in organic
- **Looking like an ad**: high production value, perfect lighting, brand-saturated frames = scroll past.
- **Voice-of-God narrator**: kills native feel. Voice should sound like a person talking, or no voice.
- **Center-frame logo-on-product hero shots**: that's an ad framing. Keep brand peripheral.
- **No loop**: organic that doesn't loop wastes the second-watch boost the algorithm rewards.
