# Writing Rules — Non-negotiable

These rules apply to **the Seedance prompt output**. They are not stylistic suggestions — failing any of them means rewriting.

## The 12 rules

### 1. One subject per shot
A shot describes one thing. If you have two subjects, you have two shots.

### 2. One action per shot
One verb, present tense, active voice. "Types", "tilts", "walks", "cuts to". Not "is typing while looking at".

### 3. One camera move per shot
A shot has a single camera direction. No "pans then dollies" inside one shot — that's two shots.

### 4. Camera vocabulary is closed
Only use terms from `reference/camera_vocabulary.md`. No inventing ("cinematic swoop", "epic flyover" — banned).

### 5. Two adjectives per noun, max
And both must be **observable** (visual / physical). "Cool, dim" yes. "Beautiful, magical" no.

### 6. No banned words
Banned in the prompt: stunning, breathtaking, mesmerizing, captivating, epic, awesome, amazing, incredible, cinematic (alone), masterpiece, perfect, beautiful (alone), vibrant (alone), dynamic (alone), immersive (alone), showcase, leverage, unleash, empower, transformative, revolutionary, game-changing.

### 7. Specific palette, not "warm" or "moody"
Always name 2–3 colors. "Amber + cool blue + matte black" not "warm tones with cool accents".

### 8. Specific light, not "good lighting"
Name the source: practical, motivated, key, fill, rim, ambient, soft box, hard window light, neon, fluorescent, candle, golden hour, blue hour, overcast, moonlight, monitor glow.

### 9. Timestamps on every shot
Every shot starts with `[Xs]`. Sum equals total duration. No exceptions.

### 10. Header is ONE line
`[N shots, Ts, A:R, audio: on/off] — Master atmosphere line.` If header spans 2+ lines, cut.

### 11. Audio is specific or "off"
If audio is on, name instruments, dynamics, sync points. "Soft synth pad swelling under shot 3" beats "uplifting music". If audio is off, write `Audio: off (designed for sound-off playback).`

### 12. Refs are addressed by role
Every ref the user provided gets a one-line role assignment. Refs the user did NOT provide do not appear in the prompt — never invent refs.

---

## Verbs preferred over verbs avoided

**Prefer (concrete motion)**: types, tilts, glances, lifts, sets, snaps, drags, drops, taps, slides, traces, points, leans, pulls, pushes, walks, stops, turns, opens, closes, hovers, scrolls, clicks, signs, draws, writes, reads, smiles (briefly), nods.

**Avoid (vague)**: experiences, enjoys, navigates (use "scrolls" or "clicks"), interacts (use the actual action), engages, embraces, celebrates, transforms.

---

## Sentence shape per shot

```
[Ts] Shot N — [Subject (concrete noun)]. [Action verb] [object/where]. Camera: [size], [movement]. [Light/atmosphere fragment].
```

Punctuation matters. Periods between subject/action/camera/light help Seedance segment the instructions.

**Good**:
```
[1.5s] Shot 2 — Founder at glass desk. Types one keystroke. Camera: tight close-up on hands, slow dolly-in. Cool monitor glow on knuckles, room otherwise dark.
```

**Bad**:
```
[1.5s] Shot 2 — A beautiful founder dressed elegantly is shown at her stunning glass desk while she dynamically and energetically types at her keyboard with the camera capturing the epic moment from multiple cinematic angles.
```

---

## Length budget

- Header: ≤ 25 words
- Per shot: ≤ 30 words
- Audio paragraph: ≤ 40 words
- References list: 1 line per ref
- Total prompt: ≤ ~250 words for ≤8s, ≤ ~400 words for 9–15s

If you're over budget, you have decoration — cut.

---

## Spanish output exception

If `LANGUAGE = ES`:
- Translate subject, action, atmosphere, audio direction.
- Keep these in English: camera terms (dolly-in, close-up, etc.), parameter keys, the literal word "Audio:" or "References:" can be translated to "Audio:" / "Referencias:".
- All 12 rules above still apply.
