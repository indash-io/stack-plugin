# Nano Banana Prompts — Reference Image Generation

Used by `instructions/ref_maximization.md` when the skill offers to generate a ref image via Gemini 2.5 Flash Image (a.k.a. "Nano Banana"). The output of this file is a prompt the user will paste into their image-gen tool — not a Seedance prompt.

The grammar is close to Seedance's director voice (concrete + sensory + technical), with one key difference: **Nano Banana renders a still, not a sequence**, so there are no timestamps, no cuts, no audio. Just the frame.

---

## Anatomy of a Nano Banana ref prompt

Six elements, in order:

1. **Subject** — concrete noun phrase, what the frame contains.
2. **Composition** — framing, position in frame, depth of layers.
3. **Lighting** — named source, direction, color temperature.
4. **Palette + materials** — 2–3 colors max, surface textures.
5. **Camera/lens** — focal length feel, depth of field, angle.
6. **Aspect ratio + technical** — final ratio, photographic register.

Pattern:
```
<Subject + composition>. <Lighting>. <Palette + materials>. <Camera/lens>. <Aspect ratio + register>.
```

---

## Rules

### Inherits from the Seedance writing rules
- ≤2 adjectives per noun, both observable.
- No banned words (stunning, cinematic alone, epic, captivating, etc. — see `style/writing_rules.md`).
- Specific palette (named colors), specific light (named source).
- Concrete nouns over abstractions.

### Specific to Nano Banana
- **Match the final video's aspect ratio**. If Seedance is 9:16, generate the ref at 9:16 unless the ref will only be used for color/style (then square is fine). This avoids reframing artifacts.
- **State the photographic register explicitly**: `editorial product still`, `documentary lifestyle photo`, `food photography overhead`, `portrait, 35mm`, `studio still life`.
- **Lighting must be one named setup**, not a vibe: `single soft key from camera-left, no fill`, `north-window daylight, 5500K, soft from camera-right`, `single warm tungsten practical, deep falloff`.
- **Background is part of the subject**: name it. `Matte black acrylic surface, no seams, no reflections.` Not "dark background".
- **No people-shaped strangers when avoidable**: prefer body parts (hand, silhouette, profile from behind) over full identifiable faces, unless the user is providing a face ref.

---

## Templates by ref type

### Generic hand close-up (T-anything that needs a hand)

```
Adult hand, palm-down, holding <object> between thumb and index finger, no other fingers visible. Tight close-up framing, subject 70% of frame, dark negative space top and bottom. Single warm tungsten key from camera-left at 45°, no fill, deep shadows on the back of the hand. Matte black surface below. Skin: neutral mid-tone, faint cool rim from a low blue practical at frame-right. Camera: 50mm equivalent, shallow depth of field, eye-level. <aspect ratio> editorial still, photographic, no people-shaped strangers in background.
```

### Generic prop / object scene (plate, desk, still life)

```
<Object: e.g., dark ceramic plate with fish bones and a lemon wedge>, centered in frame, viewed from <angle: top-down / 30° high>. Surface: <matte black / oak / linen>. Single soft window key from camera-left, no fill, soft falloff into shadow. Palette: <2–3 named colors>. Camera: <35mm equivalent>, <shallow / deep> depth of field. <aspect ratio> editorial still, food/object photography register, no text, no logos.
```

### Generic person-in-environment (silhouette, profile, shoulder-level)

```
Adult, mid-30s, in 3/4 profile from behind-left, only shoulders and side of head visible, holding <prop>. Standing at a window, soft north-light daylight, no direct sun. Background: out-of-focus interior, neutral. Palette: blue-grey + warm skin tones. Camera: 50mm equivalent, shallow depth of field, eye-level. <aspect ratio>, documentary lifestyle photo, no face details required.
```

### Style / palette / grade anchor

```
Empty <surface: matte black acrylic / oak desk>, single <object: golden capsule / ceramic mug / leaf> at lower-third position. <Lighting: single warm tungsten practical from camera-left, deep low-key falloff, faint cool blue rim from camera-right>. Palette: <named 2–3 colors>. Camera: 50mm equivalent, deep negative space, eye-level. <aspect ratio>, editorial still life. Output is a grade and palette reference — clean, no text, no logos.
```

### Product hero (only when user owns the product but doesn't have a clean photo)

⚠️ Only use this when the product is generic enough that hallucinated shape is acceptable (e.g., "a generic black supplement bottle" for a stock-style ad). If the bottle/product has specific brand identity, this template is forbidden — go back to USER_ONLY.

```
<Product: e.g., matte black supplement bottle, no labels, no logos>, centered in frame, vertical orientation. Surface: matte black, faint reflection. Single warm tungsten key from camera-left, deep shadow side, faint cool rim from camera-right. Palette: black + warm amber. Camera: 85mm equivalent, deep depth of field, eye-level. <aspect ratio>, editorial product still, no text on the product, no brand identity.
```

---

## What to deliver to the user

When the user picks option B for a shot, write a clean code block with **just the Nano Banana prompt** — nothing else. Format:

````
**T<n> — <subject>** (Nano Banana prompt, paste into Gemini 2.5 Flash Image):

```
<the prompt>
```
````

If the user picked B for multiple shots, deliver one code block per shot, in shot order.

After delivery, end with one short instruction: `Generá las N, pasámelas, y reescribo el prompt de Seedance con References: actualizado.`

---

## Banned in Nano Banana prompts (same list as Seedance)

stunning, breathtaking, mesmerizing, captivating, epic, awesome, amazing, incredible, cinematic (alone), masterpiece, perfect (alone), beautiful (alone), vibrant (alone), dynamic (alone), immersive (alone), showcase, leverage, unleash, empower, transformative, revolutionary, game-changing.

If you reach for one, replace with a specific visual fact (named light, named color, named material).

---

## Sanity checklist before delivering Nano Banana prompts

- [ ] Each prompt names a subject, lighting, palette, camera, aspect ratio.
- [ ] Aspect ratio matches the Seedance final video.
- [ ] No banned words.
- [ ] No brand identity invented (no logos, no specific founder faces, no owned spaces).
- [ ] Each prompt corresponds to exactly one shot in the upcoming Seedance prompt.
- [ ] Output format: one code block per ref, ready to paste.
