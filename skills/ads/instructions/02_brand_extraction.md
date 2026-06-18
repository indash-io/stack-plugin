# Brand Extraction (silencioso)

Este paso es **interno**. NO mostrar el resumen al usuario. Usar los hallazgos para informar todas las decisiones siguientes (paleta del prompt de imagen, tono del copy, estilo visual, etc.).

## Qué extraer de las imágenes de referencia

### Paleta de color
- 2-3 colores dominantes en HEX aproximado
- Color de acento si existe
- Si la marca usa fondos neutros (blanco, beige, negro), anotarlo

### Tipografía
- Si hay texto legible: serif vs sans-serif, peso, estilo (geométrica, humanista, display, handwritten)
- Jerarquía: ¿usan titulares grandes o todo medido?
- Si no hay texto legible → no inventar, default seguro: "modern bold sans-serif"

### Mood visual
- Iluminación: natural soft / studio rim / golden hour / dramatic side / overcast
- Composición: minimalista / saturada / centrada / con espacio negativo
- Props recurrentes (ingredientes, manos, escenarios)
- Estilo fotográfico: editorial / UGC / packshot puro / flat lay / lifestyle

### Tono inferido (para el copy)
- Aspiracional / cercano / técnico / divertido / lujo / accesible / clínico
- Tuteo o usted (rioplatense suele ser voseo)

### Do's y Don'ts
- **Do's**: lo que aparece consistente en la marca
- **Don'ts**: lo que claramente NO usa (si todo es minimalista, no proponer ads saturados; si nunca hay texto on-image, considerar si conviene meterlo)

## Cómo aplicar lo extraído
- **Paleta** → al prompt de imagen como `dominant colors: #XXX, #XXX`
- **Tipografía** → al prompt si hay texto on-image
- **Mood** → define el bloque STYLE & MOOD del prompt
- **Tono inferido** → define cómo se escribe el copy de Meta
- **Don'ts** → filtro antes de entregar (si lo violé, rehacer)

## Si las referencias son contradictorias entre sí
Priorizar la imagen que parezca más reciente o más "ad" (producción más cuidada). No promediar estilos contradictorios — eso da resultado genérico.
