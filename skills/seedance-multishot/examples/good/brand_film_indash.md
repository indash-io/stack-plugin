# GOOD — Brand film, founder/manifesto piece

## Brief received
> "Brand film for indash. 14s, 21:9. Tone: quiet, confident, slightly defiant. The idea: 'Marketing teams shouldn't be content factories. They should be operators.' Audio on. Language: EN. Refs: ref_image_1 (founder portrait, low-key, blue-grey palette), ref_video_1 (a slow handheld walk through an empty office)."

## Strategist context
> 6-shot Reveal arc. Hook on a single typed word; reveal on shot 4 = empty content factory becomes empty operator's room. Held face on shot 5 lands the line.

## The output

```
[6 shots, 14s, 21:9, audio: on] — Quiet contemporary office at dusk, blue-grey + warm tungsten practicals, low-key with single key window.

[0s]    Shot 1 — Cursor blinking on a single word "stop" on a black screen. Holds, then deletes. Camera: extreme close-up on screen, locked. Cool monitor glow only.
[2.3s]  Shot 2 — Empty open-plan office, rows of desks, soft tungsten practicals on. Camera: wide, slow dolly-back. Blue-grey ambient + amber practicals as warm accents.
[4.6s]  Shot 3 — Stack of printed ad mockups on a desk, slowly toppling sideways. Camera: medium close-up, low angle, locked. Single tungsten practical as warm rim.
[7.0s]  Shot 4 — Same desk, mockups gone, one laptop open with a quiet dashboard glow. Camera: medium-wide, slow dolly-in. Cool monitor glow becomes new key, tungsten falls to rim.
[9.8s]  Shot 5 — Founder's face in 3/4 profile, mid-40s, looking off-camera. Holds a small, defiant half-smile. Camera: medium close-up, locked with micro-drift. Cool key from monitor, warm rim from practical.
[12.0s] Shot 6 — Lowercase "indash" wordmark forming in soft white serif on a black field. Camera: locked, no movement. Single soft directional light on the type.

References:
- ref_image_1 (subject + palette): defines the founder's face, wardrobe, and the blue-grey + tungsten palette across all shots.
- ref_video_1 (motion): informs the slow dolly-back of shot 2 and the locked-but-breathing energy of shots 3–5.

Audio:
Single sustained piano note from 0s, second note enters at shot 2, light string pad swells under shot 4 (the reveal). Founder voice on shot 5, low and quiet: "Operators, not factories." Music holds clean under shot 6, then a single soft tail.

api_params:
  model: seedance-2.0
  duration_s: 14
  aspect_ratio: 21:9
  resolution: 1080p
  fps: 24
  generate_audio: true
  creativity_scale: 0.5
  temporal_smoothing: 0.6
```

## Why this is GOOD
- **Hook is a single word, deleted.** That's a brand film hook, not an ad hook — quiet, intriguing, ambiguous.
- **Reveal arc executed cleanly**: shots 1–3 build the question (mockups, factory imagery), shot 4 shifts the meaning, shot 5 lands the human, shot 6 brands.
- **Logo lands in shot 6**, late, restrained — earns its presence.
- **Refs explicitly assigned roles** (subject+palette, motion). Not just dumped.
- **Voice is one line, on the right shot.** Not narration over the whole film.
- **21:9 supports the cinematic register** — wider frame = more breathing room.
- **`creativity_scale: 0.5`, `temporal_smoothing: 0.6`** balanced for slow movement + clean grade.
- **Word count** stays under the 400-word budget for 14s pieces.
- **Specific cinema vocabulary** ("3/4 profile", "low angle", "rim", "key", "practical") instead of "cinematic".
