# Seedance 2.0 — Parameter Reference

This is the closed-set list of valid parameters and values. The skill must never invent values outside these tables.

> Source: ByteDance Seed / Seedance 2.0 release (April 2026), provider docs (fal.ai, Replicate, Atlas Cloud, Segmind, Modelslab). If ByteDance changes the API, update this file.

---

## Model

| Param  | Value          | Notes                                  |
|--------|----------------|----------------------------------------|
| model  | `seedance-2.0` | Only model this skill targets.         |

Do NOT use: `seedance-1.0-lite`, `seedance-1.0-pro`, `seedance-1.0-pro-fast`. They do not support native multi-shot or synchronized audio.

---

## Duration

| Param       | Range     | Notes                                                         |
|-------------|-----------|---------------------------------------------------------------|
| duration_s  | 4 – 15    | Hard limits. Floor 4s, ceiling 15s. Reject anything outside. |

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

| Value     | Notes                                            |
|-----------|--------------------------------------------------|
| `480p`    | Draft / cost-saving previews only.               |
| `720p`    | Acceptable for organic.                          |
| `1080p`   | Default for paid creative, demos, brand films.   |

Default for indash: `1080p` unless user explicitly requests lower.

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

| Type   | Max count | Notes                                                              |
|--------|-----------|--------------------------------------------------------------------|
| image  | 9         | Style / subject / palette refs                                     |
| video  | 3         | Motion / pacing / camera-language refs                             |
| audio  | 3         | Music tone / BPM / vocal style refs (only meaningful when audio on)|

Each ref needs an explicit ROLE in the prompt: `style`, `subject`, `motion`, `palette`, `audio`. See `instructions/execution.md` Block 4.

---

## What Seedance 2.0 does NOT support (do not request)

- Custom resolutions outside the table above
- Frame rates other than 24 or 30
- Per-shot resolution changes
- Per-shot aspect ratio changes (the entire video has one A:R)
- Reading on-screen text from prompts as exact glyphs (Seedance approximates text — use post-prod for legible copy)
- Brand-typography accuracy (use indash's editor layer for logos)
- Durations >15s (split into a sequence of clips and stitch in post)

---

## Quick parameter cheatsheet by use case

| Use case        | duration_s | aspect_ratio | fps | generate_audio | creativity_scale | temporal_smoothing |
|-----------------|------------|--------------|-----|----------------|------------------|--------------------|
| ad_performance  | 6–9        | 9:16         | 24  | true           | 0.6              | 0.4                |
| product_demo    | 8–12       | 16:9         | 24  | false          | 0.35             | 0.6                |
| organic_social  | 6–10       | 9:16         | 30  | true           | 0.7              | 0.3                |
| brand_film      | 12–15      | 21:9 / 16:9  | 24  | true           | 0.5              | 0.6                |
