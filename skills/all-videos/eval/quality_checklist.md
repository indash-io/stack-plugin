# Quality Checklist — Self-Eval

Run this on **every** prompt before delivering. Any FAIL = rewrite that block silently and re-check. Do not deliver a prompt that fails any of these.

---

## A. Structural integrity (must all PASS)

- [ ] **A1** Header is exactly one line in the format `[N shots, Ts, A:R, audio: on/off] — Master line.`
- [ ] **A2** Master atmosphere line names a palette (≥2 colors) AND a light key.
- [ ] **A3** Every shot has a `[Xs]` timestamp.
- [ ] **A4** Timestamps are monotonically increasing and cumulative.
- [ ] **A5** Shot durations sum to total declared duration (within ±0.2s).
- [ ] **A6** Total duration is in `[4, 15]` (Seedance 2.0 limits).
- [ ] **A7** Aspect ratio is one of: `16:9 | 9:16 | 1:1 | 4:3 | 3:4 | 21:9 | adaptive`.
- [ ] **A8** `References:` block exists if and only if user provided refs.
- [ ] **A9** `Audio:` block exists, either with content (if on) or `off (...)` line.
- [ ] **A10** `api_params:` block exists with at minimum: model, duration_s, aspect_ratio, resolution, fps, generate_audio.

## B. Per-shot discipline (each shot must PASS all)

- [ ] **B1** ONE subject (one concrete noun phrase).
- [ ] **B2** ONE action (one verb, present tense, active voice).
- [ ] **B3** ONE camera move (single verb from the allowed vocabulary).
- [ ] **B4** Camera block names a SIZE (`ECU/close-up/medium/medium-wide/wide/extreme-wide`).
- [ ] **B5** Light/atmosphere fragment present, names a specific source or descriptor.
- [ ] **B6** ≤30 words per shot.
- [ ] **B7** ≤2 adjectives per noun, both observable.
- [ ] **B8** No banned words: stunning, breathtaking, mesmerizing, captivating, epic, awesome, amazing, incredible, cinematic (alone), masterpiece, perfect (alone), beautiful (alone), vibrant (alone), dynamic (alone), immersive (alone), showcase, leverage, unleash, empower, transformative, revolutionary, game-changing.

## C. Strategic integrity (must all PASS)

- [ ] **C1** Shot 1 is a hook appropriate for the use case (not a logo, not a slow establishing for ads).
- [ ] **C2** Brand/logo does NOT appear in shot 1 (unless brief explicitly demanded it).
- [ ] **C3** For ads: at least one product/outcome shot exists.
- [ ] **C4** For demos: ONE feature shown, not multiple. UI implied, not pixel-rendered.
- [ ] **C5** For organic: at least one shot has handheld energy or native framing.
- [ ] **C6** For brand films: cuts are slower (≥1.5s avg), at least one held shot ≥2.0s.
- [ ] **C7** Pattern interrupt between consecutive shots: subject OR scale OR movement OR light changes.
- [ ] **C8** Audio is specific (instruments + sync points) OR explicitly off.
- [ ] **C9** If refs were provided, each is referenced with a role assignment.
- [ ] **C10** Output language matches `LANGUAGE` field (camera terms in EN regardless).

## D. Anti-AI-ish (must all PASS)

- [ ] **D1** No paragraph-style vibe-prose ("a stunning, captivating video that...").
- [ ] **D2** No bullet lists inside the prompt.
- [ ] **D3** No markdown headers (`#`, `##`) inside the prompt body.
- [ ] **D4** No phrases that describe *the video as a video* ("the viewer experiences", "the audience feels"). Describe the shot, not its effect.
- [ ] **D5** No "make it go viral", "high production value", "modern and clean", "professional-grade" — non-directives.
- [ ] **D6** No hedging in the strategist context line ("might", "could", "perhaps", "I think").

## E. API readiness (must all PASS)

- [ ] **E1** `creativity_scale` ∈ `[0.0, 1.0]`.
- [ ] **E2** `temporal_smoothing` ∈ `[0.0, 1.0]`.
- [ ] **E3** `resolution` ∈ `{480p, 720p, 1080p}`.
- [ ] **E4** `fps` ∈ `{24, 30}`.
- [ ] **E5** `generate_audio` boolean matches the audio block.
- [ ] **E6** Model is `seedance-2.0`.
- [ ] **E7** Total ref count: images ≤9, videos ≤3, audio ≤3.

## F. Ref gate (must all PASS — see `reference/refs_strategy.md`)

- [ ] **F1** Ref audit was performed (CRITICAL / RECOMMENDED / OPTIONAL classified for this brief).
- [ ] **F2** No CRITICAL ref is missing. (If one is, the skill stopped and asked — no prompt was generated.)
- [ ] **F3** RECOMMENDED refs that are missing are flagged in the strategist context line (not silently ignored).
- [ ] **F4** Output contains a `▸ REFS A SUBIR ANTES DE EJECUTAR` block (or `▸ No refs required (text-to-video).` if pure T2V).
- [ ] **F5** Each entry in the REFS A SUBIR block has a concrete asset description (not abstract `ref_image_n`).
- [ ] **F6** Each entry in the REFS A SUBIR block has a `Por qué:` / `Why:` line ≤ 25 words.
- [ ] **F7** The order of refs in REFS A SUBIR matches the numeric order of `ref_image_n` / `ref_video_n` / `ref_audio_n` in the in-prompt `References:` block.
- [ ] **F8** A `---` divider sits between the operator-facing layer (context + REFS A SUBIR) and the prompt itself.
- [ ] **F9** REFS A SUBIR callout is in the user's `LANGUAGE`. (Operator-facing copy follows the user; in-prompt camera vocabulary stays in EN regardless.)
- [ ] **F10** Ref maximization step ran (or was deliberately skipped because user said "skip todo" / "T2V only").
- [ ] **F11** Every anticipated shot was classified for ref need; gaps were presented to the user as an A/B/C ASK before strategy was written.
- [ ] **F12** For shots where the user picked B (generate), a Nano Banana prompt was delivered as a paste-ready code block following `reference/nano_banana_prompts.md`.
- [ ] **F13** No Nano Banana prompt invents brand identity (no logos, founder faces, owned spaces). USER_ONLY gaps stayed USER_ONLY.

## G. MCP execution (solo si MODE = single_shot_premium o stitched_multishot)

- [ ] **G1** Mode fue anunciado al user en la primera línea (`Modo: single_shot_premium` o similar) ANTES de ejecutar.
- [ ] **G2** Las URLs de producto / imagen ref vienen del brief del user (no se corre discovery automático del workspace).
- [ ] **G4** Frame 0 se generó con `mcp__indash__generate_image` siguiendo la gramática de `reference/nano_banana_prompts.md` (variante frame 0 protagonista).
- [ ] **G5** Motion prompt para `generate_video` cumple `reference/motion_prompts.md`: ≤60 palabras, un solo movimiento de cámara, sin timestamps, sin banned words.
- [ ] **G6** Aspect ratio del frame 0 coincide con el aspect ratio del `generate_video`.
- [ ] **G7** `generate_video` se llamó UNA sola vez para este pedido — no hay retries activos.
- [ ] **G8** Polling con `get_video_result` cada ~30s, idempotente.
- [ ] **G9** Si llegó `status: "error"`, se reportó al user con el mensaje del error. NO se reintentó silenciosamente.
- [ ] **G10** El output entregado al user es la URL pública del video + 1 línea de contexto. Nada de shot list textual (eso es modo `prompt_only`).
- [ ] **G11** Si modo `stitched_multishot`, se confirmó el costo con el user ANTES de disparar las N llamadas.
- [ ] **G12** No se prometieron features que el MCP no soporta (multi-reference de 9 imgs, `creativity_scale`, 21:9, 4:5, audio direction custom). Si el brief los pedía, se le avisó al user al elegir el modo.

---

## How to run the check

After writing the prompt, mentally walk through A → B → C → D → E → F. If anything fails:

1. **A or E failure** → structural fix (almost always 1 line).
2. **B failure** → rewrite that one shot.
3. **C failure** → reconsider the strategy. May need to revisit `instructions/strategy.md` step.
4. **D failure** → ruthless edit. Rewrite the offending sentences with concrete visuals.
5. **F failure** → check `instructions/input_processing.md` ref audit step. If F2 fails, do NOT silently fix — stop and ask the user for the missing CRITICAL ref. F4–F9 failures are formatting and can be fixed silently.

After the fix, re-run the affected section. **Deliver only when all sections pass.** Do not surface the checklist to the user. Just deliver the corrected prompt.

---

## When to break a rule

The only legitimate reason to break a B or C rule is if the user's brief **explicitly demands** it. Example: "I want a 12-shot ad in 6 seconds — chaotic on purpose." In that case, note the deviation in the strategist context line ("12 shots in 6s as requested — chaotic by design") and proceed.

Do not break A, D, or E rules. Ever.
