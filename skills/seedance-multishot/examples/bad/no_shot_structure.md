# BAD — Shot list without structure (do not produce this)

## Brief received
> "Demo de 10s, 16:9, mostrando un dashboard. Sin audio."

## The bad output

```
A 10-second product demo video showing a dashboard. The video should have multiple scenes:

- First, the user opens their laptop and looks at the screen with intent
- Then we see the dashboard with all of its many features and powerful insights, the user clicks around and explores everything
- Then we see them happy and satisfied with the results, smiling at the camera
- The brand logo appears at the end

Camera should move dynamically throughout. Lighting should be modern and clean.

Use 16:9, 10 seconds, no audio.
```

## Why this is BAD

1. **No timestamps.** Seedance does not know when shot 2 starts.

2. **Bullet list of "scenes"** instead of timeline-prompted shots. Seedance cannot parse this into discrete shots.

3. **Multi-action shots.** "User clicks around and explores everything" is 5 actions in one shot. Multi-shot model expects ONE action per shot.

4. **"All of its many features"** = guarantees Seedance hallucinates a fake UI. Demo prompts must imply ONE moment of value, not the whole product.

5. **Header buried at the end.** The format spec ("16:9, 10 seconds, no audio") is at the bottom, not in the canonical header line.

6. **No master atmosphere line.** The world isn't locked. Seedance will drift in palette and light shot to shot.

7. **"Dynamic camera"** is a non-direction. Seedance needs `dolly-in`, `pan-left`, `tracking shot`, etc.

8. **"Looks at the screen with intent"** — "with intent" is a feeling, not an observable action. Replace with the actual physical action ("leans forward 5cm" or "narrows eyes briefly").

9. **No api_params block.**

10. **No reference handling.** Even though brief had no refs, the prompt should make that explicit ("References: (none provided)") so indash's downstream code knows.

## What the strategist should have done instead
See `examples/good/product_demo_dashboard.md`. Same brief shape, fully timeline-prompted, demo-arc-correct.

---

## The lesson

A "shot list" written as bullets of intent is **not a shot list**. Seedance multi-shot wants **discrete, timestamped, single-action shots** with concrete subjects, camera moves, and light. If your output reads like a creative brief, it's wrong. If it reads like a shot sheet from a real shoot, it's right.
