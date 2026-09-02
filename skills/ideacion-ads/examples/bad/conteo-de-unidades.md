# ❌ Conteo de unidades equivocado en un bundle

**Caso real (anonimizado)**: pack de inicio de suplementos, estática 4:5.

## Qué pasó

El pack tiene **3 productos** (Omega 3, Magnesio, Vitamina C+Zinc). La pieza
salió con **4 frascos**, porque una imagen de referencia del catálogo tenía un
frasco duplicado y el conteo se asumió de la imagen en vez de validarse contra
la descripción del producto.

## Por qué es grave

- Cualquier persona que conozca el pack lo detecta al instante → credibilidad rota.
- Rompe la verdad del producto, que es lo único innegociable de un ad DTC.

## La lección para ideación

1. **Nunca asumir el conteo de un bundle desde una imagen.** Antes de escribir
   "pack de 3" (o dibujar el concepto con N unidades), validá contra el catálogo
   (`list_products`) o la landing oficial.
2. El conteo validado se escribe **explícito** en el bloque: en el copy si
   aplica, y siempre en el concepto visual ("EXACTAMENTE tres frascos") y en
   `notes` con su fuente — así la ejecución no re-adivina.
3. Si la referencia del catálogo contradice la realidad del producto, anotarlo
   en `notes`: es información que la ejecución necesita para elegir refs.
