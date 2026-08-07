# Nano Banana inventando variantes cuando se rearreglan frascos

**Marca**: marca de suplementos (anonimizada)
**Categoría**: suplementos
**Formato**: estática 4:5
**Tipo**: ❌ bad
**Modelo usado**: nano-banana

Aplica a: `suplementos-pack-nano-banana-invento-variantes.png` y `-v3.png`.

## Qué falla
Pasé la imagen del pack de inicio (4 frascos juntos: 2 Omega 3 + Magnesio + Vit C+Zinc) como referencia y le pedí a nano-banana que **rearreglara los frascos** en una nueva composición:
- En V2: 3 frascos en fila lower-right
- En V3: 3 frascos en fila, en orden específico left-to-right

Nano-banana respetó el packaging (curvas, fine print, conteos) pero **inventó variantes que no están en el pack de inicio**:
- ❌ Vitamina C+Zinc se convirtió en un **pote de polvo "200g" "Puro Ácido Ascórbico"** (que es otro SKU del catálogo, NO el del pack de inicio)
- ❌ Citrato de Magnesio se convirtió en un frasco **"Magnesio Complex"** (otra variante del catálogo, NO la del pack de inicio)
- ❌ Bonus: en V3 apareció un wordmark mal escrito "OMSGA 3"

## Por qué pasa
Nano-banana es excelente **editando** una imagen de referencia (la trata como source casi inviolable), pero cuando le pedís **re-componer / re-arreglar** frascos individualmente, deja de "editar" y empieza a "generar inspirado en". En ese modo tira de su training data: si la marca tiene otras variantes conocidas (acá: Vitamina C en polvo y un Magnesio Complex como SKUs separados), las inserta como si fueran lo mismo.

## Qué evitar / cómo corregir
1. **Si la composición deseada es CASI IGUAL a la de la ref** (mismo agrupamiento, mismo plano) → nano-banana funciona perfecto (ver V1 del mismo set, que sí salió bien).
2. **Si la composición deseada es muy distinta** (separar frascos, reordenarlos, cambiar el plano radicalmente) → nano-banana va a alucinar variantes.

Workarounds:
- **Reforzar en el prompt**: *"DO NOT use any other product variant from this brand. Only use the EXACT three bottles shown in the reference: Omega 3 + Citrato de Magnesio + Vitamina C+Zinc. No powder pots, no Magnesio Complex, no alternate SKUs."*
- **Componer la nueva escena manualmente**: tomar el ref original con los frascos juntos, recortarlos individualmente en Photoshop/Canva, armar la composición ahí y solo usar el MCP para el texto on-image encima.
- **Workflow de 2 pasos**: paso 1 con nano-banana respetando el plano del ref para preservar packaging; paso 2 editar agregando texto.

## Regla a partir de ahora
**Antes de pedirle a nano-banana una re-composición radical, listar explícitamente las variantes de la marca que NO deben aparecer** y forzar que solo use las que están en el ref. Si la marca tiene un catálogo amplio y similar, considerar armado manual de la composición.
