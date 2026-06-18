# VITS Pack Starter — pills de color no alineados al producto

**Marca**: VITS Nutrición
**Categoría**: suplementos
**Formato**: estática 4:5
**Tipo**: ❌ bad

## Qué falla
- Cada frasco VITS tiene un pill de color en la etiqueta que codifica su categoría:
  - **Omega 3** → pill AZUL "Esenciales"
  - **Citrato de Magnesio** → pill CELESTE "Relajación"
  - **Vitamina C + Zinc** → pill NARANJA "Inmunidad"
- En este ad, los pills sobre cada frasco (en el bloque de beneficios superior) **no respetan el color del frasco de abajo**: aparece naranja sobre Omega 3, azul sobre Magnesio, etc. Eso rompe el código visual de la marca y confunde la asociación beneficio↔producto.
- También aparecen labels incorrectos pegados a los frascos (ej: "ESENCIALES" sobre Magnesio).

## Qué evitar
- Cuando hay sistema de color por categoría en el packaging del cliente → **listarlo explícitamente en el prompt** y enlazarlo al producto correspondiente, no dejarlo librado a interpretación del modelo.
- Definir el orden de los frascos en el prompt (left/center/right) y asignar a cada posición su color de pill correcto.
- Repetir la regla en el bloque CRITICAL del prompt: *"the colored pill above each bottle MUST be the same color as the pill printed on that bottle"*.
- En NEGATIVE: `"mismatched pill colors, swapped labels, wrong bottle order"`.

## Notas adicionales
- Aplica a cualquier marca con sistema de color por línea de producto (suplementos, skincare con tipos de piel, alimentos con sabores). Hacer un mini inventario antes de promptear.
