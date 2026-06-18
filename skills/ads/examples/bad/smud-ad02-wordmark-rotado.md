---
brand: smud
category: belleza / depilación
fecha: 2026-06-30
modelo_usado: nano-banana
modelo_correcto: gpt-image (chips + UI) + nano-banana solo para el packshot
---

# Smud AD 02 — Wordmark del producto sale rotado / espejado

## Qué salió mal

1. **Wordmark "smud" rotado 90° o espejado** sobre el pebble: en Pink salió girado, en Teal salió "pnus" (espejo), en AD 03 igual, en AD 05 también ("pnus").
2. **Forma del pebble inconsistente**: el Pink salió rectangular redondeado (mismo error de shape que AD 01), el Teal salió oval pero distinto.
3. **Chips de beneficios renderizados por nano-banana**: pasable pero no excelente. Iconos genéricos, jerarquía visual sin la limpieza de un layout dirigido.

## Causa raíz

- **Elegí el modelo equivocado**: usé `nano-banana` cuando el ad es 80% UI tipográfica (chips, badges, ícono+texto en círculos). Ese es territorio de `gpt-image`.
- **Recoloreo agresivo**: pedirle a nano-banana que "recolore" un packshot Black a Pink o Teal hace que pierda la grilla del wordmark cuando rota el producto.
- **Sin restricción explícita de orientación**: el prompt no decía "wordmark must read left-to-right, do not rotate or mirror the product".

## Cómo evitarlo

### Decisión de modelo correcta para este tipo de ad

| Componente | Modelo |
|---|---|
| Chips circulares con icono + texto | **gpt-image** (nativo en UI) |
| Hero del pebble centrado fiel | **nano-banana** (con ref del packshot del color real) |
| Tipografía del headline "SMUD PINK" | **gpt-image** |

→ Workflow correcto: **híbrido en 2 pasos**.
1. Paso 1 — nano-banana: generar el pebble en el color correcto, sin texto on-image, sin chips. Solo el producto sobre fondo limpio, wordmark legible.
2. Paso 2 — gpt-image: tomar la salida del paso 1 como ref + pedir el layout completo (chips, headline, jerarquía).

### Si lo hacés en un solo paso (no recomendado)

- Usar `gpt-image` directamente y aceptar que el producto va a ser menos fiel.
- Pasar el packshot real como ref + instrucción explícita: "wordmark 'smud' must appear correctly oriented, lowercase, left-to-right, never rotated or mirrored. If you cannot render the wordmark correctly, leave the product surface clean without text."

## Síntomas que indican el error a tiempo

- Wordmark del producto sale como "pnus", "snud", invertido, rotado, o emborronado → mal modelo. Regenerar con el otro, no insistir.
- Chips o badges con texto roto o iconos torcidos → era gpt-image.
- Producto cambia de forma entre slides → faltó pasar el packshot del color correcto + instrucción de "preserve shape".

## Línea roja

> Si el producto tiene un wordmark visible y el ad necesita texto on-image complejo (chips, headlines, layout editorial), NO usar nano-banana solo. O híbrido o gpt-image directo.
