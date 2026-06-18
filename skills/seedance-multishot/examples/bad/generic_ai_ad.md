# BAD — Generic AI-ish ad (do not produce this)

## Brief received (same as good ad example)
> "Ad para Meta 9:16, 8 segundos, indash genera 100 ads en 1 hora."

## The bad output

```
A stunning, cinematic, mesmerizing 8-second vertical video showcasing the breathtaking power of indash. The video should be epic and captivating, with multiple dynamic shots that immerse the viewer in an unforgettable experience. Beautiful lighting, vibrant colors, and amazing camera work. The user should feel empowered and inspired by the transformative capabilities of our revolutionary platform.

Show a marketer working hard, then show indash being amazing, then show the marketer being happy. Cinematic style. Beautiful aesthetics. High production value. Make it go viral.

Music should be uplifting and motivational. Camera should be dynamic and engaging.
```

## Why this is BAD (every line of failure)

1. **Banned word salad**: stunning, cinematic, mesmerizing, breathtaking, epic, captivating, beautiful, amazing, vibrant, dynamic, immersive, transformative, revolutionary, empowered, inspired. Almost every banned token from `style/writing_rules.md`.

2. **No shot structure.** No timestamps. No `[Xs]` markers. Seedance has nothing to chunk. The model treats this as one undifferentiated 8s blob.

3. **No subjects.** "A marketer" is a placeholder, not a subject. "Working hard" is not an action.

4. **No camera vocabulary.** "Dynamic camera work" is not a camera move. Seedance camera engine has nothing to do with that.

5. **No palette, no light key.** "Beautiful lighting" tells the model nothing.

6. **No header.** No shot count, no aspect ratio, no audio flag.

7. **No refs handled.** Even if user had provided them, this prompt would ignore them.

8. **No api_params block.** indash can't pipe this into the API call cleanly.

9. **Single-paragraph "vibe" with adjectives stacked.** This is the AI-assistant default and Seedance hates it.

10. **"Make it go viral"** is not a directive. It's a wish. The prompt has no instruction Seedance can act on.

## What the strategist should have done instead
See `examples/good/ad_saas_b2b.md`. Same brief, structured output, every shot earns its slot.

---

## The lesson

The single biggest failure mode of this skill is reverting to **generic AI assistant vibe-prose**. If you find yourself writing a paragraph that *describes the video in adjectives*, stop. The prompt is a **shot list with technical specs**, not a treatment.
