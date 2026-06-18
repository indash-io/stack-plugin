# Ref Maximization

Runs as **step 3.5** in the skill workflow — between the ref audit gate (step 3) and strategy (step 4).

The audit gate only stops if a CRITICAL ref is missing. This step goes further: it walks the (anticipated) shot list, asks per-shot "would a ref make this shot more faithful?", and for every gap proposes an action — **ask the user** or **generate via Nano Banana**.

This is the difference between a Seedance video that *might* render the brand right and one that *will*.

---

## When to run this step

Always — unless the brief explicitly says "T2V only, no refs". The CRITICAL gate is necessary but not sufficient; this step is where fidelity is won.

If the ref audit gate fired and STOPPED (a CRITICAL is missing), do NOT run this step yet — first resolve the CRITICAL with the user, then come back here.

---

## What to do, in order

### 1. Anticipate the shot list

You do not have a final shot scratchpad yet (that's step 4). But after analysis you know:
- The use case
- Total duration + shot count band
- The arc
- The key subjects (product, talent, environments)

Build a tentative shot map (subject + role per shot) — enough to identify which shots have specific subjects that need refs.

### 2. Classify per-shot ref need

For every anticipated shot, decide:

| Subject in shot | Ref need | Default action |
|---|---|---|
| The brand product (specific bottle/device/garment) | **CRITICAL** — already resolved by gate | use existing product ref |
| The brand's known talent / founder face | **CRITICAL** — already resolved by gate | use existing talent ref |
| Generic human body part (hand, arm, silhouette) | **OPTIONAL→helpful** | offer: user photo OR Nano Banana |
| Generic object scene (a plate, a desk setup, a B-roll prop) | **OPTIONAL→helpful** | offer: user photo OR Nano Banana |
| Generic environment (studio backdrop, window light, kitchen) | **RECOMMENDED if recurring across shots** | offer: user photo OR Nano Banana |
| Brand-owned space (their HQ, their store) | **CRITICAL if shown** | must come from user |
| Style/grade/palette anchor across all shots | **RECOMMENDED** | offer: user reference still OR Nano Banana |
| Motion/camera energy reference | **OPTIONAL** | only ask if user has a clip in mind |

### 3. Decide who can fulfill each gap

For each gap, mark it as one of:

- **`USER_ONLY`** — must come from the user (real-world specific: their face, their store, their owned product variant, their team).
- **`GENERATABLE`** — can be created with Nano Banana (Gemini 2.5 Flash Image) because it is a generic subject that doesn't carry brand-specific identity (a plate, a hand, a generic adult silhouette, a palette anchor still).
- **`SKIPPABLE`** — Seedance can hallucinate this acceptably; only worth a ref if the user wants extra control.

### 4. Build the ASK block — present to user, stop, wait

Present the gaps as a structured question. Format (in user's `LANGUAGE`):

ES:
```
▸ ANTES DE GENERAR — decisiones sobre refs (n faltantes)

<Shot id> — <Subject>  (<priority: RECOMMENDED | OPTIONAL>, role: <role>)
  A. Pasame una foto que tengas
  B. Te armo el prompt de Nano Banana y la generás vos
  C. Skip — Seedance la inventa (queda genérica pero aceptable)

<Shot id> — ...

¿Qué hacemos con cada una? Respondé "T1: B, T3: A, T5: C" o similar.
```

EN:
```
▸ BEFORE GENERATING — ref decisions needed (n gaps)

<Shot id> — <Subject>  (<priority>, role: <role>)
  A. Send me a photo you have
  B. I'll write a Nano Banana prompt for you to run
  C. Skip — Seedance hallucinates (generic but acceptable)

...

How do we handle each? Reply with "T1: B, T3: A, T5: C" or similar.
```

Rules for the ASK block:
- One block per missing ref. Don't lump.
- USER_ONLY gaps don't show option B (can't generate a brand-specific space).
- SKIPPABLE-only gaps may show A and C only (no B) if generation adds nothing.
- Order: RECOMMENDED first, then OPTIONAL.
- Cap at the most useful 6 gaps. Beyond that you're over-engineering — Seedance bank is 9 images max, leave headroom.
- Always leave the user a clean "skip everything, just generate" exit: end the ask with `Si querés saltear todo y generar con lo que hay, decime "skip todo".`

### 5. Wait for the user response, then route

Three response patterns:

**Pattern X — user provides photo(s) directly**
- Assign each photo to its shot, classify role, slot into the upcoming `References:` block.
- Confirm: "Tomo T1 como subject de la Toma 1. ¿Sigo?"

**Pattern Y — user picks B (generate) for one or more shots**
- Pull from `reference/nano_banana_prompts.md` to write the generation prompt(s).
- Deliver them as a code block the user can paste into their image-gen tool.
- WAIT for the user to come back with the generated images before proceeding.

**Pattern Z — user picks C (skip) or "skip todo"**
- Mark those shots as `T2V-fallback`.
- Add a one-line caveat to the strategist context: "(refs faltantes en T1/T3 — Seedance va a aproximar, brand quedaa salvo en T4/T6)."
- Proceed to strategy.

### 6. Update the operator-facing REFS A SUBIR block

After the user resolved the asks, the final REFS A SUBIR list is the union of:
- The original CRITICAL refs (user-provided),
- The new RECOMMENDED/OPTIONAL refs (user-provided OR generated),
- In numeric order matching the in-prompt `References:` block.

If a ref was generated by the user via Nano Banana, mark it: `1. Plato cerámico oscuro con espinas — generada por vos con Nano Banana → role: subject`. The model doesn't care about provenance, but the operator might re-run.

---

## What this step is NOT

- **Not a license to spam refs.** Each ref must do work. Two refs fighting for the same role still confuses Seedance. The cap remains: practical max around 6 well-roled refs for a 6-shot video.
- **Not a way to bypass the CRITICAL gate.** If a CRITICAL is missing, the audit gate stopped you earlier — fix that first.
- **Not a replacement for the user's brand.** USER_ONLY gaps stay USER_ONLY. Don't try to "Nano Banana the founder's face" — that's hallucinating brand identity by another name.

---

## Decision matrix — quick reference

| Ref subject | USER_ONLY | GENERATABLE | SKIPPABLE |
|---|---|---|---|
| Brand product (specific) | yes (already CRITICAL) | no | no |
| Brand talent / founder face | yes (already CRITICAL) | no | no |
| Brand-owned space | yes | no | no |
| Generic adult hand / arm / silhouette | optional | **yes** | yes |
| Generic prop / object / plate / desk | optional | **yes** | yes |
| Window light / backdrop / studio surface | optional | **yes** | yes |
| Style grade / palette anchor still | optional | **yes** | yes |
| Generic crowd / blurred bg humans | no | **yes** | yes |

When in doubt, **offer all three options** (A user, B generate, C skip) and let the user choose.
