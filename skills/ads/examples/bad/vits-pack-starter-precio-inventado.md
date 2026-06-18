# VITS Pack Starter — precio inventado en el ad

**Marca**: VITS Nutrición
**Categoría**: suplementos
**Formato**: estática 4:5
**Tipo**: ❌ bad

## Qué falla
- El ad muestra "Antes $14.990" como precio tachado, pero **ese número es inventado por el modelo de imagen** — no fue provisto por el usuario ni viene de la landing.
- Mostrar un precio falso en un ad de Meta es un riesgo legal (publicidad engañosa) y operativo (la landing tiene otro precio → conversión cae por mismatch).
- Regla dura violada: *"NUNCA inventar features, claims o precios del producto"* (SKILL.md).

## Qué evitar
- **Nunca incluir precios numéricos en el prompt de imagen** salvo que el usuario los haya provisto explícitamente.
- Si la mecánica del ad requiere price anchor (precio tachado + nuevo precio) → preguntar al usuario el monto exacto ANTES de generar.
- Si se quiere comunicar la oferta sin número → usar "% off", "oferta por tiempo limitado", "envío gratis" — claims que no dependen de un valor inventado.
- En NEGATIVE del prompt incluir: `"NO price numbers, NO currency symbols, NO $, NO strikethrough prices, no 'antes' or 'ahora' prices"` cuando no hay precio confirmado.

## Notas adicionales
- Modelo: gpt-image. El modelo "completa" los espacios vacíos de la composición — si pedís un bloque de precio, lo va a llenar con algo aunque no le des el número.
