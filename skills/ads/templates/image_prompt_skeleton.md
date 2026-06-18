# Image Prompt Skeleton

Estructura base. Adaptar el orden si el caso lo pide, pero **todos los slots aplicables deben estar resueltos**. Si un slot no aplica (ej: no hay texto on-image), omitirlo entero — no dejarlo vacío.

```
[SHOT TYPE]: product photography / lifestyle scene / studio packshot / UGC-style smartphone shot / flat lay top-down

[SUBJECT]: [qué se ve exactamente, en qué pose, qué hace, en qué contexto / escena]

[COMPOSITION]: [framing — close-up / medium / wide], [rule of thirds / centered / off-center], [negative space yes/no, dónde]

[LIGHTING]: [natural soft window light / studio rim light / golden hour warm / dramatic side light / bright overcast / etc.]

[STYLE & MOOD]: [del brandkit — minimal editorial / warm lifestyle / bold pop / clean clinical / cozy home / luxury aspirational / etc.]

[COLOR PALETTE]: dominant colors #XXXXXX, #XXXXXX, accent #XXXXXX

[ON-IMAGE TEXT]: "[texto en español]" — placement: [top-left / bottom-center / etc.], font style: [bold sans-serif / elegant serif / handwritten script / etc.], size: [large headline / medium subheadline / small caption]

[ASPECT RATIO]: 1:1 / 4:5 / 9:16

[QUALITY]: sharp focus, high detail, photorealistic, commercial-grade

[NEGATIVE]: no cartoon, no distortion, no extra limbs, no blurry text, no watermark, no oversaturation
```

## Bloque OBLIGATORIO fuera del prompt
```
REFERENCE IMAGE TO ATTACH:
- [Image N from input] — purpose: product fidelity (preserve exact product appearance)
- [Image M from input] — purpose: style / palette reference (mood and visual language)
```

## Reglas
- Todo el prompt en **inglés** salvo el `ON-IMAGE TEXT` (que va en español porque es lo que verá el usuario final)
- Si NO hay texto on-image → omitir ese slot, no dejarlo vacío
- Si el brandkit no permite inferir tipografía → default seguro: `modern bold sans-serif`
- Máximo ~120 palabras totales en el prompt. Denso, no narrativo.
