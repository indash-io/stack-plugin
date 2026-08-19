# Input Processing

Your job here: take whatever the user gives you and turn it into a clean, structured brief. Do not skip ambiguity by inventing.

## Expected input shape

The user gives you some combination of:
1. **Concept** (always present): a short description of what they want. Example: "Ad para TikTok mostrando que indash genera 100 ads en 1 hora vs 1 semana de un equipo creativo"
2. **Visual refs** (optional): URLs or local paths to images/videos/audio. Seedance 2.0 caps at **9 images + 3 video clips + 3 audio refs**.
3. **Format hints** (optional): "9:16, 8 segundos", "horizontal", "Meta ad", "brand film de 15s"
4. **Brand context** (optional): product name, USP, audience

## Parse into this structure

Extract the following fields. If absent, mark as `MISSING` and ask before continuing:

```
USE_CASE       : ad_performance | product_demo | organic_social | brand_film  [infer from concept verbs/nouns]
PRODUCT        : the thing being sold/shown                                   [REQUIRED]
AUDIENCE       : who watches it                                               [infer or ask]
INSIGHT        : the human truth the video taps into                          [infer or leave blank]
HOOK_ANGLE     : the specific opening idea (problem? contrast? reveal?)       [infer or ask]
FORMAT         : aspect_ratio + duration_seconds                              [REQUIRED — ask if missing]
LANGUAGE       : EN | ES                                                      [default EN, switch to ES if brief is in ES]
REFS           : list of {type: image|video|audio, url, role}                 [optional]
AUDIO_ON       : true | false                                                 [default true for ads, false for silent demos — ask if unclear]
TONE           : energetic | dry | premium | playful | hard-sell | docu       [infer from concept]
CONSTRAINTS    : anything the user said NOT to do                             [optional]
```

## Inference rules (use case detection)

- Words like "ad", "anuncio", "creative", "performance", "Meta", "TikTok ad", "hook", "convert" → `ad_performance`
- Words like "demo", "feature", "tutorial", "explica", "muestra cómo", "dashboard", "UI", "screen" → `product_demo`
- Words like "reel", "post", "social", "orgánico", "story" → `organic_social`
- Words like "brand", "marca", "manifesto", "founder", "story", "film" → `brand_film`

If two are plausible, ask. Do not assume.

## Aspect ratio inference (only if user is silent)

- TikTok / Reels / Shorts / Stories → `9:16`
- YouTube / web / dashboard demo → `16:9`
- Feed (IG, FB) → `1:1` or `4:5` (Seedance supports 1:1, 4:3, 3:4 — pick 1:1 for square, 3:4 for portrait-feed)
- Cinematic brand film → `21:9`
- If unclear, ASK.

## Duration inference (only if user is silent)

- Ads: 6–9s (default 8s)
- Demos: 8–12s
- Organic: 6–10s
- Brand films: 12–15s

Always clamp to Seedance 2.0 hard limits: **4s minimum, 15s maximum**.

## Refs handling

For each ref the user provides, classify its **role** in the prompt:
- `style` → defines look/grade/lighting
- `subject` → defines person/product appearance
- `motion` → defines camera or character movement
- `palette` → defines color palette only
- `audio` → defines music/sfx tone (audio refs only)

A single ref can carry multiple roles (e.g., a lifestyle photo that defines both subject AND palette → role tag: `subject + palette`).

When you write the final prompt, you must explicitly say what each ref contributes. Do not just dump URLs.

## Ref audit (MANDATORY GATE before generating)

This is a hard step. Before moving on to `analysis.md`, run this audit using `reference/refs_strategy.md`:

### Step 1 — Determine what the video visually contains
From the brief, identify whether the video must show:
- A **specific physical product** (with brand identity — color, shape, logo)
- A **specific person** (founder, recurring talent, brand face)
- A **specific environment** (a known store, office, set)
- A **specific brand element** (logo, packaging, typography)

### Step 2 — Classify each required element
Cross-reference with `reference/refs_strategy.md` decision matrix. For each element, mark it as:
- **CRITICAL** (must have ref) — without it, Seedance hallucinates and the video becomes useless for the brand
- **RECOMMENDED** (should have ref) — without it, output is generic but acceptable
- **OPTIONAL** (nice to have)

### Step 3 — Compare with what the user provided
| Required | Critical? | User provided? | Action |
|----------|-----------|----------------|--------|
| Yes      | CRITICAL  | Yes            | ✓ proceed, assign role |
| Yes      | CRITICAL  | **No**         | **STOP — ask the user** |
| Yes      | RECOMMENDED | No           | flag in strategist context, proceed |
| Yes      | OPTIONAL  | No             | ignore |

### Step 4 — If a CRITICAL ref is missing, the gate fires

Do NOT generate the prompt. Instead, return one short message in the user's language:

EN example:
> "Stopping before generating. This brief shows a specific product (a branded heating belt). Without a product reference image, Seedance will invent a generic device and the wordmark will not render. Please attach: 1 product hero photo. Optionally: 1 lifestyle photo with the talent. I'll generate as soon as you share them."

ES example:
> "Freno antes de generar. Este brief muestra un producto específico (una faja térmica de marca). Sin foto de referencia del producto, Seedance va a inventar un dispositivo genérico y el wordmark no va a renderizar. Mandame: 1 foto hero del producto. Opcional: 1 lifestyle con la modelo. Genero apenas las pases."

Do NOT proceed silently with `T2V` and a hallucinated product. The gate is non-negotiable for `ad_performance` and `brand_film` use cases when a specific product/person is in the brief.

### Step 5 — Document the audit result in the structured brief

Add to the parsed structure:

```
REFS_AUDIT     :
  required_critical    : [list of elements]
  required_recommended : [list of elements]
  user_provided        : [list of refs with assigned role(s)]
  missing_critical     : [list — must be empty before proceeding]
  missing_recommended  : [list — flag in strategist context line]
```

This audit becomes the source of truth for the "REFS A SUBIR" callout in `instructions/execution.md`.

## When to ask, when to infer

**Ask** when missing: USE_CASE (if ambiguous), PRODUCT, FORMAT, AUDIO_ON (if ambiguous), refs that user mentioned but didn't provide.

**Infer silently**: AUDIENCE (only if confident), INSIGHT, HOOK_ANGLE, TONE, LANGUAGE.

Maximum 3 questions. If you need more, you have a brief problem — ask the user to expand the brief.

## Output of this step
A filled-in structured brief + the result of the ref audit (`REFS_AUDIT` block above).

If the audit passed (no `missing_critical`), proceed to **`instructions/ref_maximization.md`** — that step walks every anticipated shot, classifies remaining ref gaps, and ASKS the user (provide / generate via Nano Banana / skip) before strategy is written.

If the audit fired (any `missing_critical`), STOP here and ask the user for the missing CRITICAL ref. Do not go to ref_maximization yet — resolve the CRITICAL first.

Do not generate the Seedance prompt at this stage — that's `execution.md`, after strategy.
