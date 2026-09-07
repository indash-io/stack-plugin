# Seedance — Parameter Reference (2.0 y 2.5)

This is the closed-set list of valid parameters and values. The skill must never invent values outside these tables.

> Source: ByteDance Seed / Seedance 2.0 (April 2026) and 2.5 (August 2026), verified against fal's live input schemas on 2026-09-07. If ByteDance changes the API, update this file.

> **Not every param here is sendable through `generate_video`.** The MCP exposes `prompt`, references, `aspect_ratio`, `duration_seconds`, `resolution` and `generate_audio`. `fps`, `creativity_scale` and `temporal_smoothing` are model-level knobs with no field on our tool — express that intent in the prompt instead of asking for a parameter that will not travel.

---

## Model

| `model` value      | Version | Route | Notes |
|--------------------|---------|-------|-------|
| `seedance`         | 2.0 | fal | The workhorse. 4-15s. |
| `seedance-2.5`     | 2.5 | fal | 4-30s in ONE render, 10 refs of each kind, last frame, text-to-video. ~1.55x the cost per second. |
| `seedance-ark`     | 2.0 | ByteDance ModelArk | Same model as `seedance` at HALF the credits. Moderation allows AI-generated people. 4-12s, no video/audio refs, slow (~40s render per second of clip). |
| `seedance-2.5-ark` | 2.5 | ByteDance ModelArk | Same trade as above, on 2.5. 4-12s. |

**Pick the ark route by default for anything cost-sensitive or people-heavy.** It is the same model at half the price; what you give up is the long durations, the video/audio references and the auto-retry.

Do NOT use: `seedance-1.0-lite`, `seedance-1.0-pro`, `seedance-1.0-pro-fast`. They do not support native multi-shot or synchronized audio.

---

## Duration

| Model              | Range    | Notes |
|--------------------|----------|-------|
| `seedance`         | 4 – 15   | Hard limits. |
| `seedance-2.5`     | 4 – 30   | The headline of 2.5: a 30s single take, no stitching. |
| `seedance-ark` / `seedance-2.5-ark` | 4 – 12 | Capped by our gateway budget, not by the model. |

Off-menu values snap DOWN and you are charged for the snapped value.

---

## Aspect ratio

| Value       | Use case                            |
|-------------|-------------------------------------|
| `16:9`      | Web, YouTube, dashboard demos       |
| `9:16`      | TikTok, Reels, Shorts, Stories      |
| `1:1`       | IG feed square                      |
| `4:3`       | Legacy / retro register             |
| `3:4`       | IG portrait feed                    |
| `21:9`      | Cinematic / brand films             |
| `adaptive`  | Lets Seedance choose. Avoid for B2B output — always specify. |

---

## Resolution

**Resolution is a PRICE knob.** Seedance bills on output video tokens, and tokens scale with pixels: the cost per second is a direct function of the tier.

| Value   | Cost vs 720p | Use |
|---------|--------------|-----|
| `480p`  | ~0.45x | Drafts, choreography checks, anything the client will not see. On 2.5 it costs less per second than 2.0 does at 720p. |
| `720p`  | 1x     | **Default.** Fine for organic and for most paid social. |
| `1080p` | ~2.25x | Only when the deliverable genuinely needs it — a brand film, a hero spot, something going to a big screen. |

Default for indash: **`720p`**. Ask for `1080p` deliberately and say why; on `seedance-2.5` a 30s 1080p render is the single most expensive thing the stack can produce.

---

## Frame rate

| Value | Use case                           |
|-------|------------------------------------|
| `24`  | Cinematic — ads, brand films, demos |
| `30`  | Native social (TikTok/Reels)        |

---

## generate_audio

| Value   | Notes                                                                         |
|---------|-------------------------------------------------------------------------------|
| `true`  | Seedance 2.0 produces synchronized audio from prompt context.                 |
| `false` | Silent video. Required for sound-off feed playback when audio is added later. |

When `true`, the prompt MUST include an `Audio:` paragraph naming instruments + sync points. Otherwise audio will be generic.

---

## creativity_scale (0.0 – 1.0)

How much the model can deviate from the prompt.

| Range     | Meaning                          | When to use                                |
|-----------|----------------------------------|--------------------------------------------|
| 0.0–0.3   | Strict adherence                 | Brand-critical demos, exact UI fidelity    |
| 0.3–0.5   | Slight interpretive freedom      | Most B2B demos, brand films                |
| 0.5–0.7   | Balanced                         | Ads, hybrid creative                       |
| 0.7–1.0   | High creative deviation          | Organic / experimental / TikTok native     |

Default by use case: see `instructions/execution.md`.

---

## temporal_smoothing (0.0 – 1.0)

Reduces flicker in long shots; trades motion energy for stability.

| Range     | Meaning                        | When to use                                       |
|-----------|--------------------------------|---------------------------------------------------|
| 0.0–0.3   | Maximum motion energy          | Handheld, organic, ads with kinetic intent        |
| 0.3–0.5   | Balanced                       | Most general use                                  |
| 0.5–0.8   | Smooth, less micro-motion      | Demos with screen content, brand films            |
| 0.8–1.0   | Maximum smoothness             | Pristine product hero shots, slow brand intros    |

---

## Multimodal references

| Type   | `seedance` (2.0) | `seedance-2.5` | Notes |
|--------|------------------|----------------|-------|
| image  | 9  | 10 | Style / subject / palette refs |
| video  | 3  | 10 | Motion / pacing / camera-language refs |
| audio  | 3  | 10 | Music tone / BPM / vocal style refs (only meaningful when audio on) |

The ark routes take **images only** — no video or audio references. That is a limit of the surface we call, not of the model.

Each ref needs an explicit ROLE in the prompt: `style`, `subject`, `motion`, `palette`, `audio`. See `instructions/execution.md` Block 4.

---

## What Seedance 2.0 does NOT support (do not request)

- Custom resolutions outside the table above
- Frame rates other than 24 or 30
- Per-shot resolution changes
- Per-shot aspect ratio changes (the entire video has one A:R)
- Reading on-screen text from prompts as exact glyphs (Seedance approximates text — use post-prod for legible copy)
- Brand-typography accuracy (use indash's editor layer for logos)
- Durations >15s on `seedance` and >30s on `seedance-2.5` (split into a sequence of clips and stitch in post)
- Video or audio references on the `-ark` routes (image refs only)
- A last frame on 2.0 — `seedance-2.5` added it, `seedance` never had it

---

## Quick parameter cheatsheet by use case

| Use case        | duration_s | aspect_ratio | fps | generate_audio | creativity_scale | temporal_smoothing |
|-----------------|------------|--------------|-----|----------------|------------------|--------------------|
| ad_performance  | 6–9        | 9:16         | 24  | true           | 0.6              | 0.4                |
| product_demo    | 8–12       | 16:9         | 24  | false          | 0.35             | 0.6                |
| organic_social  | 6–10       | 9:16         | 30  | true           | 0.7              | 0.3                |
| brand_film      | 12–15      | 21:9 / 16:9  | 24  | true           | 0.5              | 0.6                |

For a single take longer than 15s, the use case is `seedance-2.5` and nothing else in the roster can do it.
