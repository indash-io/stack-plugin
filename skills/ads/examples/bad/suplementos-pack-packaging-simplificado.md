# Suplementos — packaging simplificado / no fiel al producto real

**Marca**: marca de suplementos (anonimizada)
**Categoría**: suplementos
**Formato**: estática 4:5
**Tipo**: ❌ bad

Aplica a las 3 imágenes: `suplementos-pack-packaging-simplificado-v1.png`, `-v2.png`, `-v3.png`.

## Qué falla
El modelo (gpt-image) reprodujo los frascos con la silueta y los colores correctos, pero **simplificó el packaging real** omitiendo elementos críticos:

- ❌ Falta el conteo de cápsulas: el frasco real dice "60 Cápsulas Blandas" (Omega 3) o "120 Cápsulas" (Magnesio, Vit C+Zinc).
- ❌ Falta el subtítulo de composición: "OMEGA 3 + VITAMINA E" en Omega 3, "MÁXIMA ABSORCIÓN" en Magnesio.
- ❌ Falta la curva decorativa (la semi-esfera oscura) que cruza los labels de los frascos de esta marca — es un elemento de marca recurrente.
- ❌ Falta la fine print inferior ("Suplemento dietario a base de…").
- ❌ El pill de categoría a veces se renderiza sin acento ("RELAJACION" en vez de "RELAJACIÓN").

Resultado: parecen "frascos parecidos a los de la marca" pero no son los frascos reales. Alguien que conoce la marca lo nota al instante → pérdida de confianza + el ad se siente "fake".

## Por qué pasa
- **gpt-image** es excelente para texto on-image (headlines, badges, tablas), pero **inventa el packaging** cuando los detalles del producto son densos (texto secundario, fine print, gráficos del label).
- La imagen de referencia que se le pasa funciona como "inspiración general", no como source literal.

## Qué evitar / cómo corregir
1. **Para productos con packaging denso (suplementos, cosmética, alimentos con muchas leyendas)** → usar `nano-banana` en vez de `gpt-image`. Nano Banana preserva el producto desde la imagen de referencia con mucha más fidelidad.
2. **Compensación**: nano-banana es peor con texto on-image grande. Si el ad necesita TANTO producto fiel COMO texto grande → considerar workflow de dos pasos:
   - Paso 1: generar con nano-banana solo la escena con los frascos perfectos.
   - Paso 2: editar esa salida agregando los textos on-image (en una segunda llamada al MCP, o en Canva/Photoshop).
3. **Pasar TODAS las imágenes del producto disponibles** como referencia (no solo una). Más data = menos invención.
4. **Listar en el prompt los elementos NO NEGOCIABLES del packaging**: "must show '60 Cápsulas Blandas' subtitle, must show the decorative dark curve on the label, must include fine print at the bottom".
5. En NEGATIVE: `"simplified packaging, missing subtitle text, missing capsule count, missing decorative curve, missing fine print, made-up bottle design"`.

## Regla a partir de ahora (aplicar siempre)
**El producto en un ad tiene que ser FOTOGRÁFICAMENTE FIEL al packaging real.** No es una opción estilística — es la línea base de calidad. Si el modelo elegido no puede preservarlo, cambiar de modelo o cambiar de mecánica (ej: mostrar el producto más chico y compensar con tipografía, o usar una foto real del producto editada en el background).
