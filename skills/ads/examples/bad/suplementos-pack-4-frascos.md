# Suplementos — pack de inicio con 4 frascos en vez de 3

**Marca**: marca de suplementos (anonimizada)
**Categoría**: suplementos
**Formato**: estática 4:5
**Tipo**: ❌ bad

## Qué falla
- El pack de inicio contiene **3 productos** (Omega 3, Citrato de Magnesio, Vitamina C+Zinc). El modelo generó **4 frascos** porque la imagen de referencia de Indash tenía un Omega 3 duplicado en la composición original y lo repliqué literal sin filtrar.
- Esto rompe la verdad del producto: cualquier persona que conozca el pack lo detecta al instante y pierde credibilidad.
- También desbalancea la composición — el cuarto frasco no aporta nada visual ni informativo.

## Qué evitar
- **Nunca asumir el conteo de un bundle desde la imagen de referencia.** Antes de promptear, validar contra la descripción del producto en Indash o la landing oficial cuántas unidades tiene.
- En el prompt, escribir el conteo en mayúsculas + reforzar en NEGATIVE: `"EXACTLY THREE bottles. NO fourth bottle."`
- Si la ref de Indash muestra una cantidad distinta a la real → aclarar explícitamente que se ignore esa cantidad y se respete el conteo correcto.

## Notas adicionales
- Modelo: gpt-image. Ref: imagen de otro pack del mismo catálogo en el workspace.
- Corrección aplicada en regeneración: agregar "EXACTLY THREE" + "NO fourth bottle, NO duplicate bottles" en NEGATIVE.
