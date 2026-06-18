# Strategy

Now decide the shape of the video. Inputs: the structured brief + the four analysis sentences + **the resolved ref map from step 3.5** (`instructions/ref_maximization.md` — every shot's ref status is now known: user-provided, generated via Nano Banana, or explicitly skipped). Outputs: a shot list with arc, count, and timing — but **not yet** the Seedance text.

Do not enter this step until the ref maximization ASK has been resolved. The shot subjects you write here must agree with the ref decisions the user made.

## Step 1 — Decide shot count

| Total duration | Default shots | Floor | Ceiling |
|----------------|---------------|-------|---------|
| 4–6s           | 3             | 2     | 4       |
| 7–9s           | 4             | 3     | 6       |
| 10–12s         | 5             | 4     | 7       |
| 13–15s         | 6             | 5     | 8       |

Bias **lower** for `brand_film` (slower cuts), **higher** for `ad_performance` and `organic_social`. Never pad to look more cinematic.

## Step 2 — Decide the arc

Use one of these four arcs. Pick deliberately.

### A. Problem → Product → Payoff (ads, demos)
- Shot 1: visualize the pain (visceral, not abstract)
- Shot 2–3: introduce the product/action
- Shot 4–N: show the after-state / payoff

### B. Reveal arc (brand films, premium ads)
- Shot 1: tight, ambiguous, intriguing
- Shot 2–3: pull back, reveal context
- Shot N: full reveal + brand association

### C. Build arc (demos, explainers, escalation ads)
- Shot 1: small/quiet
- Shot 2–N: each adds energy, scale, or stakes
- Final shot: peak — the result

### D. Loop arc (organic, repeatable)
- Shots 1–N circle back so shot N visually rhymes with shot 1
- Designed for replay (TikTok loops boost the algorithm)

## Step 3 — Assign each shot a job

For every shot in the list, write down:

```
SHOT_N
  job        : hook | escalate | reveal | demonstrate | resolve | brand
  duration_s : (must sum to total)
  size       : ECU | CU | MS | MWS | WS | EWS
  movement   : fixed | dolly_in | dolly_out | pan | tilt | tracking | orbit | handheld | dolly_zoom | crane | arc | rack_focus
  subject    : one concrete noun phrase
  action     : one verb in present tense
  light_mood : single descriptor (golden, neon, overcast, low-key, practical, high-key)
  ref_used   : (optional) which provided ref informs this shot
```

This is your scratchpad. The output prompt is built FROM this in `execution.md` — you do not show this scratchpad to the user.

## Step 4 — Pacing sanity-check

Sum the durations. They must equal the requested total. They must not violate Seedance 2.0 limits.

- Per-shot floor: ~0.7s (anything shorter is a frame, not a shot)
- Per-shot ceiling: depends on use case (see `analysis.md` table)
- Check: does the duration of each shot match its job? A "hook" shot rarely needs >1.5s. A "resolve" shot can be longer.

## Step 5 — Pattern-interrupt audit

For ads/organic, verify there is a **change** between consecutive shots in at least one of:
- Subject (different person/object)
- Scale (close → wide or vice versa)
- Movement (static → moving or vice versa)
- Light (warm → cool, indoor → outdoor)
- Frame energy (calm → kinetic)

If two consecutive shots only differ in micro-detail, merge them or replace one.

## Step 6 — Audio strategy (only if AUDIO_ON = true)

Decide and write down:
- **Music presence**: none / ambient bed / score / track-driven
- **SFX**: list of diegetic sounds tied to specific shots
- **Voice**: present? if yes, sync to which shots and how long

Seedance 2.0 generates audio from prompt context. Be **specific**: "soft synth pad swelling under shot 3, snare hit on shot 4 cut" beats "uplifting music".

## Output of strategy step
A shot scratchpad ready for `execution.md`. Do not write the final Seedance prompt here — go to execution next.
