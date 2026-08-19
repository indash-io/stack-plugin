# Template — `brand_film`

For brand storytelling, manifestos, founder pieces, recruitment films. The job is **emotional residue**, not conversion.

## Defaults
- Aspect ratio: `21:9` (cinematic) or `16:9`
- Duration: 12–15s (Seedance 2.0 hard cap is 15s)
- Audio: ON, scored
- Shots: 5–7 (slower cuts than ads)
- Arc: **B. Reveal arc** is canonical, but **C. Build arc** also works
- Pacing: 0.15–0.3 cuts/sec — slow

## Default API params
```
creativity_scale: 0.5
temporal_smoothing: 0.6     # smoother long shots
resolution: 1080p
fps: 24                     # cinematic
generate_audio: true
```

## Shot job map (default 6-shot, 14s, Reveal arc)

| Shot | Job          | Typical duration | Notes                                                              |
|------|--------------|------------------|--------------------------------------------------------------------|
| 1    | hook         | 2.0–2.5s         | Tight, ambiguous, intriguing. Object detail or facial fragment.    |
| 2    | establish    | 2.0–2.5s         | Pull back. Place us in time/space.                                 |
| 3    | escalate     | 2.0–2.5s         | Build emotional tension or thematic stakes.                        |
| 4    | reveal       | 2.5–3.0s         | The shift — the thing the film is actually about appears.          |
| 5    | resolve      | 2.0–2.5s         | Emotional landing — a face, a gesture, a held look.                |
| 6    | brand        | 1.5–2.0s         | Restraint. Logo can be implied, not slammed.                        |

## Cinematic vocabulary for brand films

Lean into:
- **Lensing**: 35mm or 50mm equivalent, shallow DoF, anamorphic flare (call it "anamorphic flare" not "cinematic")
- **Lighting**: motivated practicals, golden hour, blue hour, single hard key, low-key with rim
- **Camera**: slow dolly, crane, arc, slow rack focus — never handheld unless it's a docu-style brand film
- **Pacing**: room for held looks. A 2.5s static shot is fine here.

## Filled-template skeleton (16:9, 14s)

```
[6 shots, 14s, 16:9, audio: on] — <Genre: docu-cinematic | quiet-noir | sun-soaked-intimate>, <2-color palette>, <single light-key descriptor>.

[0s]    Shot 1 — <Tight ambiguous subject>. <Subtle verb>. Camera: extreme close-up, <slow movement>. <Light>.
[2.3s]  Shot 2 — <Establishing subject>. <Verb>. Camera: wide, slow dolly-out. <Light>.
[4.6s]  Shot 3 — <Tension subject>. <Verb>. Camera: <size>, <movement>. <Light>.
[7.0s]  Shot 4 — <Reveal subject>. <Verb (the shift)>. Camera: <size>, <movement>. <Light>.
[9.8s]  Shot 5 — <Held face/gesture>. <Verb>. Camera: medium close-up, locked or micro-drift. <Light>.
[12.0s] Shot 6 — <Implied brand element>. <Verb>. Camera: <size>, <movement>. <Light>.

References:
- <user-provided refs only>

Audio:
<scored music — strings or piano motif from shot 1; swell into shot 4 reveal; sustains under shot 5; clean tail under shot 6>. Optional voice: one line max, low and quiet, on shot 5.

api_params:
  model: seedance-2.0
  duration_s: 14
  aspect_ratio: 16:9
  resolution: 1080p
  fps: 24
  generate_audio: true
  creativity_scale: 0.5
  temporal_smoothing: 0.6
```

## Common failures to avoid in brand films
- **Feature dump in a manifesto wrapper**: pick one feeling. Not three values.
- **Logo too early**: kills the reveal arc. Logo earns its appearance.
- **Generic stock-film visuals**: meeting rooms, handshakes, walking-through-corridor cliches. Replace with one specific image with conviction.
- **Voice-over carrying the meaning**: the visuals should land alone. Voice is a layer, not the message.
- **Too many shots**: brand films breathe. 5–7 shots in 14s, not 10.
