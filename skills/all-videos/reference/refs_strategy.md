# Reference Strategy — When to Use Refs, Which Ones, and Why

The single most common failure mode of a B2B Seedance prompt is **assuming text alone will render the brand correctly**. It will not. Seedance hallucinates products, logos, faces, and UI elements when refs are missing. This file is the gate.

---

## The 3 Seedance 2.0 modes (recap)

| Mode | What you send | What the prompt's `References:` block does |
|------|---------------|---------------------------------------------|
| **Text-to-video (T2V)** | Just the prompt text | Block omitted entirely. |
| **Image-to-video (I2V)** | Prompt + 1 image (typically first-frame) | Block lists 1 image with role. |
| **Multi-reference (2.0)** | Prompt + up to 9 img + 3 vid + 3 audio, each role-tagged | Block lists every ref with its role. |

The `References:` block in the prompt is **documentation for the model** of what each attached ref means. It does NOT upload the file. The actual upload happens via the API call (separate parameter). Both must agree.

---

## Decision matrix — by use case

### `ad_performance`

| Element in the ad | Refs status | What happens if missing |
|---|---|---|
| Specific physical product (cosmetic, gadget, garment, food, device) | **CRITICAL** — ref of product hero required | Seedance invents a generic product. Brand identity broken. |
| Specific logo/wordmark/typography | **CRITICAL** — ref of logo OR product with logo visible | Wordmark renders as garbled text. |
| Specific human (founder, recurring talent, brand face) | **CRITICAL** — ref of that person's face | Random face. Brand consistency broken across ads. |
| Specific environment (a known store, an office, a product setting) | RECOMMENDED — ref of environment | Generic location. May not match brand world. |
| Generic stock-style ad (no specific product visible) | OPTIONAL — refs can guide style/palette only | T2V is fine. |

**Rule for ads**: if the product is the protagonist of the ad, you MUST have a product ref. No exceptions. Generic "an ad for a productivity app" with no visible product → T2V is fine.

### `product_demo`

| Element | Refs status | What happens if missing |
|---|---|---|
| Real UI/dashboard pixel-accurate | NOT POSSIBLE — Seedance can't render real UI even with refs | Use indash's editor layer to composite UI on top of the generated footage. |
| Person using the product | RECOMMENDED — ref of the user persona | Generic user. May not match brand persona. |
| Physical product in workspace | CRITICAL — ref of product | Hallucinated device. |
| Workspace setting | OPTIONAL — ref helps consistency | Generic but acceptable. |

**Rule for demos**: refs are about the human + workspace, NOT about UI. The UI is always abstract/implied in Seedance and replaced/composited later.

### `organic_social`

| Element | Refs status | What happens if missing |
|---|---|---|
| Talent (creator face, founder, etc.) | RECOMMENDED if recurring — CRITICAL if it's the brand's known face | Random face. Loses recognition. |
| Specific product visible | CRITICAL if shown — OPTIONAL if implied | Hallucinated product. |
| Native platform aesthetic | OPTIONAL — text describes it well enough | T2V works for native energy. |

**Rule for organic**: if the brand has a known talent or known product, refs are required. Pure trend-based content (no product hero) can run on T2V.

### `brand_film`

| Element | Refs status | What happens if missing |
|---|---|---|
| Founder / specific people | CRITICAL — ref of each person | Wrong faces. Manifesto loses authenticity. |
| Brand-owned spaces (HQ, factory, store) | RECOMMENDED | Generic locations. |
| Product (if shown — often implied in brand films) | CRITICAL when visible | Hallucinated product. |
| Mood/grade/look | RECOMMENDED — 1 style ref helps consistency | Drift across shots more likely. |

**Rule for brand films**: people refs are non-negotiable when faces appear. Brand films live or die on authenticity, and a hallucinated CEO face kills it.

---

## Ref roles (closed list — use these in the `References:` block)

| Role | What this ref provides | Typical input |
|------|------------------------|---------------|
| `subject` | The exact person, product, or object that must appear in-frame | Product hero photo, person headshot, logo file |
| `style` | Visual register: grade, contrast, texture, era | A reference still from a film/photo whose look you want |
| `palette` | Color palette only | A swatch or any image whose colors you want extracted |
| `motion` | How camera or character moves | A short video clip showing the desired energy |
| `audio` | Sonic register: tone, BPM, instrumentation | A short audio clip with the desired feel |

A single ref can serve multiple roles. Tag accordingly: `(subject + palette)`, `(style + motion)`.

---

## How to recommend refs to the user (the gate)

Before generating the prompt, the skill must perform this audit:

1. **Detect the use case** (from `instructions/input_processing.md`).
2. **Detect what the ad/demo/film visually requires** (specific product? specific person? specific space?).
3. **Cross-reference with the matrix above** to determine `CRITICAL` / `RECOMMENDED` / `OPTIONAL` refs for this brief.
4. **Compare against what the user provided.**
5. **Decide:**
   - All CRITICAL refs present → proceed.
   - Any CRITICAL ref missing → **STOP. Ask the user to provide it before generating.** Explain WHY (one line: "sin esta ref Seedance va a inventar el producto").
   - RECOMMENDED missing → flag as a soft warning in the strategist context line, but proceed.
   - OPTIONAL missing → ignore.

**Never** generate a prompt that depends on a CRITICAL ref the user did not provide. That's worse than no prompt — it's a prompt that produces a video looking like a competitor's product or a fake brand.

---

## Cap reminder (Seedance 2.0 hard limits)

- Images: 9 max
- Video clips: 3 max
- Audio refs: 3 max

In practice for B2B work, useful ref count per use case:
- ad_performance: 2–4 images (product + person + maybe style/palette)
- product_demo: 1–3 images (product + user + workspace)
- organic_social: 1–2 images (talent + product)
- brand_film: 3–6 images + 1 motion video (people + spaces + style + a motion clip for camera energy)

More refs ≠ better. Each ref must have a clear role. Two refs fighting for the same role (e.g., two style refs with different palettes) confuse the model.

---

## What to put in the output ("Refs to attach" block)

When delivering the prompt to the user, ALWAYS include a callout BEFORE the prompt that says:

```
▸ REFS A SUBIR A LA API ANTES DE EJECUTAR (n total)
1. <descripción concreta del archivo que el user tiene> → role: <role(s)>
   Por qué: <one line explaining why this ref matters>
2. ...
```

Format the callout in the user's `LANGUAGE` (ES / EN). The callout sits between the strategist context line and the prompt itself. See `instructions/execution.md` and `templates/output_template.md` for exact placement.

---

## After the gate — ref maximization (step 3.5)

This file defines the **CRITICAL gate** only. After the gate passes, the skill goes further via `instructions/ref_maximization.md` — which walks every anticipated shot, identifies RECOMMENDED / OPTIONAL gaps, and ASKS the user per gap:
- **A** — provide a photo,
- **B** — let the skill write a Nano Banana prompt the user runs (using `reference/nano_banana_prompts.md`),
- **C** — skip.

The CRITICAL matrix in this file determines if a video can be generated at all. The ASK in step 3.5 determines how *good* it will be. Both are mandatory unless the user explicitly says "T2V only" or "skip todo".
