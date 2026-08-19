# Camera Vocabulary — Closed Set

The skill must use only terms from this file when describing camera in shot blocks. Inventing terms (e.g., "epic flyover", "cinematic swoop") is a hard fail.

---

## Shot sizes (always FIRST in the camera block)

| Term            | Abbrev | What it shows                                          |
|-----------------|--------|--------------------------------------------------------|
| extreme close-up| ECU    | Detail of one element (eye, finger, button)            |
| close-up        | CU     | Face / object filling frame                            |
| medium close-up | MCU    | Head + shoulders                                       |
| medium          | MS     | Subject from waist up                                  |
| medium-wide     | MWS    | Full body in environment                               |
| wide            | WS     | Subject + significant environment                      |
| extreme-wide    | EWS    | Landscape / vast space, subject small                  |

Use the longest form ("extreme close-up") in the prompt. Abbreviations are for internal scratchpad only.

---

## Camera movements (closed list)

| Term         | What it does                                                         |
|--------------|----------------------------------------------------------------------|
| fixed        | Camera does not move                                                 |
| locked       | Synonym of fixed (often paired with subject motion)                  |
| dolly-in     | Camera moves forward toward subject                                  |
| dolly-out    | Camera moves back away from subject                                  |
| pan-left     | Camera rotates horizontally to the left                              |
| pan-right    | Camera rotates horizontally to the right                             |
| tilt-up      | Camera rotates vertically upward                                     |
| tilt-down    | Camera rotates vertically downward                                   |
| tracking     | Camera moves alongside subject (parallel)                            |
| arc          | Camera curves around subject                                         |
| orbit        | Full circular motion around subject                                  |
| crane-up     | Camera rises vertically                                              |
| crane-down   | Camera descends vertically                                           |
| handheld     | Operator-style micro-shake (specify "with micro-shake" if subtle)    |
| dolly-zoom   | Dolly + zoom in opposite directions (Vertigo effect)                 |
| rack-focus   | Focus shifts between near and far subject (no camera body movement)  |
| push-in      | Synonym of dolly-in (often shorter and faster)                       |
| pull-out     | Synonym of dolly-out                                                 |
| whip-pan     | Very fast pan, motion blur — use sparingly                           |
| static       | Synonym of fixed                                                     |

### Movement modifiers (allowed)

- `slow` (e.g., "slow dolly-in")
- `fast` (e.g., "fast push-in")
- `micro-drift` (almost-imperceptible movement, useful for "locked-but-alive" shots)
- `with micro-shake` (subtle handheld feel without full handheld)

---

## Angles (optional — add after movement when relevant)

| Term         | What it conveys                                       |
|--------------|-------------------------------------------------------|
| eye-level    | Neutral                                               |
| low-angle    | Subject feels powerful / dominant                     |
| high-angle   | Subject feels small / vulnerable                      |
| top-down     | Overhead — flatlay or surveillance feel               |
| dutch / canted| Tilted frame — tension, unease                       |
| 3/4 profile  | Partial profile, common for portraits                 |
| over-the-shoulder | Behind one subject's shoulder framing another    |

---

## Lensing cues (optional — add at end of camera block when relevant)

| Term                  | What it does                                  |
|-----------------------|-----------------------------------------------|
| shallow depth of field| Blurred background, subject sharp             |
| deep depth of field   | Everything sharp, no separation               |
| anamorphic flare      | Horizontal lens flare streaks                 |
| 35mm look             | Classic mid-tele cinema feel                  |
| wide lens             | Distortion, expansiveness                     |

---

## How to write the camera block

Pattern (in order):
```
Camera: <size>, <movement>[, <angle if non-default>][, <lens cue if intentional>].
```

Examples:
- `Camera: close-up, slow dolly-in.`
- `Camera: medium-wide, tracking, low-angle.`
- `Camera: extreme close-up, locked, shallow depth of field.`
- `Camera: medium, handheld with micro-shake.`
- `Camera: wide, slow crane-up, anamorphic flare.`

Never:
- `Camera: dynamic, cinematic, multi-angle.`  ← not from the closed set
- `Camera: epic flyover with smooth movement.` ← not from the closed set
- `Camera: drone-like aerial swoop.`  ← invented term

---

## Pairing rules of thumb

- **Wide shots** pair with `slow dolly`, `crane`, or `locked`.
- **Medium shots** pair with `handheld` (intimate) or `tracking` (polished).
- **Close-ups / ECU** pair with `slow dolly-in`, `locked`, or `rack-focus`. Pans on close-ups feel jarring — avoid.
- **Static subjects + handheld** = nervous energy.
- **Moving subjects + locked camera** = composed, observational.
- **Dolly-zoom** is a strong choice — use it once at most per video.
- **Whip-pan** as a transition cut is fine; mid-shot is usually too aggressive.
