# Template — `ad_performance`

Paid creative for Meta / TikTok / YouTube Shorts. The job is conversion, not art.

## Defaults
- Aspect ratio: `9:16` (default), or `1:1`/`4:5` if specified for feed
- Duration: 6–9s (default 8s)
- Audio: ON (sound-off design via captions, but audio enhances retention)
- Shots: 4–5 (default 4 for 8s)
- Arc: usually **A. Problem → Product → Payoff** or **C. Build arc**
- Pacing: 0.4–0.7 cuts/sec — fast

## Default API params
```
creativity_scale: 0.6
temporal_smoothing: 0.4
resolution: 1080p
fps: 24
generate_audio: true
```

## Shot job map (default 4-shot ad)

| Shot | Job        | Typical duration | Notes                                          |
|------|------------|------------------|------------------------------------------------|
| 1    | hook       | 1.0–1.5s         | Pattern interrupt. Face, motion, or contrast. |
| 2    | escalate   | 1.5–2.0s         | Introduce the pain or the contrast.           |
| 3    | demonstrate| 2.0–2.5s         | Product in action — outcome, not UI.          |
| 4    | resolve    | 1.5–2.5s         | After-state + brand/product visible.          |

## Hook patterns (pick one for shot 1)

- **Face hook**: human face in extreme close-up doing something unexpected.
- **Contrast hook**: before/after compressed into one frame (split, push-in, rack focus).
- **Motion hook**: object enters frame fast, snap to subject.
- **Question hook**: visual question — empty Slack channel, blank dashboard, ringing phone.
- **Number hook**: a striking on-screen number or stat as graphic insert (only if Seedance 2.0 can render legibly — keep numbers ≤ 4 chars).

## Filled-template skeleton (use this when generating)

```
[4 shots, 8s, 9:16, audio: on] — <Master line: genre, palette, light key>.

[0s]   Shot 1 — <Hook subject>. <Hook verb>. Camera: <ECU|close-up>, <movement>. <Light fragment>.
[1.2s] Shot 2 — <Pain/contrast subject>. <Verb>. Camera: <size>, <movement>. <Light fragment>.
[3.0s] Shot 3 — <Product-in-action subject>. <Verb>. Camera: <size>, <movement>. <Light fragment>.
[5.5s] Shot 4 — <Payoff subject + brand visible>. <Verb>. Camera: <size>, <movement>. <Light fragment>.

References:
- <only if user provided>

Audio:
<sting on shot 1 cut, beat-driven music under shots 2–3, voice or text-sync sting under shot 4>.

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

## Common failures to avoid in ads
- **Logo first**: never. Logos belong in shot 3 or 4.
- **Slow hook**: shot 1 over 1.5s for an ad means people are gone.
- **Talking head only**: at least one product/outcome shot, otherwise it's a podcast clip.
- **Over-long demo**: do not show the full UI flow. Show ONE moment of value.
- **Two CTAs**: one CTA. One.
