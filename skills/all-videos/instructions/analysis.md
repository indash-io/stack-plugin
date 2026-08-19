# Analysis

You have a structured brief. Now do the strategist's job: figure out **what this video has to do** before deciding what it shows.

## The three questions every shot list must answer

Before any shot exists, you must be able to answer:

1. **Why will someone stop scrolling?** (the hook — what visual pattern interrupt happens in the first 1.5s)
2. **Why will they keep watching?** (the retention engine — what changes shot to shot)
3. **What do they leave with?** (the takeaway — one product truth or emotional residue, never two)

If you cannot answer all three in one sentence each, your brief is too thin. Go back to `input_processing.md` and ask.

## Use-case-specific analysis

### `ad_performance`
- **Hook**: must be in the first 0.5–1.5s. Contrast, motion, face, or surprise.
- **Retention**: 1 idea per shot. No more than 2.5s per shot. Pattern interrupts every shot.
- **Takeaway**: product name visible + one benefit. Always.
- **Format bias**: 9:16 vertical. Faces work. UI screens that don't fill the frame don't work.
- **Common failure**: too many shots, each too long, too generic. Cut more.

### `product_demo`
- **Hook**: show the *outcome* the product produces, not the product UI.
- **Retention**: cause → effect → result arc. The viewer should understand the workflow without audio.
- **Takeaway**: one specific feature, one specific benefit. Don't list 5 features.
- **Format bias**: 16:9 (web) or 9:16 (mobile demo). UI screens require legible scale.
- **Common failure**: starting with a logo or a UI tour. Start with the user's pain or the after-state.

### `organic_social`
- **Hook**: tonally aligned with the platform's native vibe (TikTok ≠ LinkedIn ≠ IG Reels).
- **Retention**: rhythm with audio is more important than tight cuts. Trends, formats, in-jokes.
- **Takeaway**: brand association more than specific product feature.
- **Format bias**: 9:16, 1:1, sometimes 4:5.
- **Common failure**: looking like an ad. Organic must feel native, not paid.

### `brand_film`
- **Hook**: a question, a contradiction, or a single striking image. Not a logo.
- **Retention**: emotional arc, not feature list. Slower cuts, longer shots OK (but still ≤15s total).
- **Takeaway**: brand value or worldview, not product spec.
- **Format bias**: 21:9 or 16:9 cinematic.
- **Common failure**: feature dump dressed up as a manifesto. Pick a single emotional beat.

## Output of analysis (internal — not shown to user)

Produce these four sentences for yourself before moving to strategy:

```
HOOK_SENTENCE      : "In the first second, [visual pattern interrupt] makes the viewer stop because [reason]."
RETENTION_SENTENCE : "Each shot adds [new info / new motion / new contrast] so the viewer keeps watching."
TAKEAWAY_SENTENCE  : "The viewer leaves remembering [one specific thing], not [common distractor]."
SUCCESS_METRIC     : "If this works, the viewer [does X observable behavior]."
```

If any of these sentences are vague or generic, the rest of the prompt will be vague and generic. Tighten them now.

## Strategic posture by use case

| Use case          | Cuts/sec | Camera energy        | Lighting bias        | Audio bias                    |
|-------------------|----------|----------------------|----------------------|-------------------------------|
| ad_performance    | 0.4–0.7  | handheld, fast push  | high contrast, vivid | upfront sting + voice/sfx     |
| product_demo      | 0.3–0.5  | locked, slow dolly   | clean, soft, natural | minimal music + UI sfx        |
| organic_social    | 0.4–0.6  | handheld, native     | natural, varied      | trending track or none        |
| brand_film        | 0.15–0.3 | crane, slow dolly    | motivated, warm      | scored music, ambient design  |

Use this as a default — break it deliberately, never accidentally.
