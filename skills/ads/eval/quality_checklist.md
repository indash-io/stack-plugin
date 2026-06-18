# Quality Checklist — Self-check antes de entregar

Correr esta lista antes de cada entrega. Si algo falla → arreglar y volver a chequear.

## Estrategia
- [ ] El ángulo está **confirmado por el usuario** (no me lo inventé en el último paso)
- [ ] Las variaciones desarrollan el ángulo confirmado, no se desvían
- [ ] Si son 3-5 variaciones, son realmente DISTINTAS entre sí (no la misma con cambios cosméticos)

## Prompt de imagen
- [ ] Cada slot del skeleton aplicable está resuelto (no hay `[STYLE]` vacío)
- [ ] Paleta de color del brandkit aplicada (HEX explícitos)
- [ ] Aspect ratio coherente con el placement objetivo
- [ ] Imagen de referencia indicada explícitamente y con su rol
- [ ] Modelo recomendado (Nano Banana / GPT Image) con criterio (no al azar)
- [ ] Si hay texto on-image → está en español y especificado dónde y con qué tipografía
- [ ] El prompt tiene menos de ~120 palabras
- [ ] Está en inglés (salvo el ON-IMAGE TEXT)

## Copy de Meta
- [ ] **Primary Text**: hook fuerte en los primeros ~50 caracteres
- [ ] **Headline**: dentro de ~27-40 caracteres y CONTADO
- [ ] **Description**: dentro de ~27-30 caracteres y CONTADO (si se usa)
- [ ] **CTA**: elegido de la lista oficial de Meta y alineado al objetivo de campaña
- [ ] Sin fluff, sin clickbait, sin "descubrí el secreto"
- [ ] Números concretos donde se puede
- [ ] Pasa el test "¿lo diría una persona real?"

## Brandkit
- [ ] Paleta del brandkit respetada en el prompt
- [ ] Tono del copy coherente con el inferido de las referencias
- [ ] No usé nada de los "don'ts" detectados (ni visual ni copy)

## Formato
- [ ] La elección estática vs carrusel está justificada en 1 línea
- [ ] Si es carrusel, hay contenido REAL para cada tarjeta (no relleno)
- [ ] Si es carrusel, todas las tarjetas usan 1:1

## Consistencia visual (solo carrusel)
- [ ] Cada tarjeta con modelo lista el outfit COMPLETO + lo que NO va (negative inventory: "no belt, no jewelry…")
- [ ] Si hay 3+ tarjetas con la misma persona, los prompts de T3 en adelante referencian la salida previa para mantener identidad/luz/fondo
- [ ] El recap/grid NO regenera los looks desde cero — exige usar las salidas previas como source y prohíbe invención de detalles
- [ ] El orden de generación está explícito en las notas finales (qué tarjeta se hace primero y qué adjuntar en cada paso)

## Fidelidad al producto (chequeo contra `examples/bad/`)
- [ ] **Conteo correcto**: si es un bundle/pack, el número de unidades en la imagen coincide con la realidad del producto (no asumir desde la ref de Indash)
- [ ] **Sin precios inventados**: no hay números de precio en la imagen salvo que el usuario los haya dado explícitamente
- [ ] **Sistema de color del packaging respetado**: si la marca usa pills/colores por categoría (ej: VITS azul=esenciales, naranja=inmunidad, celeste=relajación), los labels superiores matchean el color del frasco de abajo
- [ ] **Sin claims inventados**: cada beneficio/feature en la imagen tiene sustento en la landing o el brief del usuario
- [ ] **Wordmark/logo legible y sin distorsión**: el nombre del producto aparece como en el packaging real
- [ ] He revisado `examples/bad/` filtrando por marca/categoría y no estoy repitiendo ninguno de esos errores

## Entregable
- [ ] Sigue el template (`output_static.md` o `output_carousel.md`) sin saltarse bloques
- [ ] Las imágenes de referencia a adjuntar están claramente identificadas
- [ ] El usuario puede copiar y pegar cada bloque sin tener que reinterpretar nada

Si TODO está OK → entregar. Si algo falla → arreglar y volver a correr el checklist.
