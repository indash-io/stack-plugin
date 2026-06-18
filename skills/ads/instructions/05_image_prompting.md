# Image Prompting — Best Practices

> **Nuevo workflow**: el prompt se construye **internamente** y se manda al MCP de Indash, que devuelve la imagen final. El usuario NO ve el prompt salvo que lo pida explícitamente. Toda la rigurosidad de esta guía sigue aplicando — porque la calidad del prompt define la calidad de la imagen que vas a entregar.

## Estructura del prompt (orden importa)

1. **SHOT TYPE** — product photography / lifestyle scene / studio packshot / UGC-style / flat lay
2. **SUBJECT** — qué se ve, en qué pose/ángulo, en qué contexto
3. **COMPOSITION** — framing (close-up / medium / wide), regla de tercios, espacio negativo
4. **LIGHTING** — natural soft / studio rim / golden hour / dramatic side / overcast
5. **STYLE & MOOD** — del brandkit extraído
6. **COLOR PALETTE** — HEX dominantes del brandkit
7. **ON-IMAGE TEXT** (si aplica) — qué texto en español, dónde, qué tipografía aprox
8. **ASPECT RATIO** — según placement
9. **QUALITY** — sharp focus, high detail, photorealistic, commercial-grade
10. **NEGATIVE** — qué evitar (cartoon, blurry text, distorted, extra fingers, watermark)

Ver template en `templates/image_prompt_skeleton.md`.

## Aspect ratios por placement de Meta
- Feed cuadrado: **1:1** (1080×1080)
- Feed vertical: **4:5** (1080×1350) — recomendado para máxima superficie en feed mobile
- Stories / Reels: **9:16** (1080×1920)
- **Default si no hay info: 4:5**

Para CARRUSEL: 1:1 obligatorio (todas las tarjetas mismo ratio).

## Imagen de referencia — pasarla al MCP
En cada llamada al MCP de Indash, adjuntar las imágenes del input que correspondan:

- Imagen del **producto** (packshot o lifestyle) → siempre que el producto aparezca en el ad
- Imagen de **estilo/brandkit** (ad anterior, foto del sitio) → cuando el mood/paleta tiene que ser coherente con material existente
- Si hay 2 referencias distintas (producto + estilo) → pasar ambas y aclarar el rol en metadata si el MCP lo soporta

En el bloque `<details>` colapsado del output, anotar qué imagen se mandó y con qué rol, para que el usuario pueda auditarlo si quiere.

## Modelo de imagen — selección experta (CRÍTICO)

Elegir entre los dos modelos NO es opcional. Hacerlo mal te cuesta una corrida entera. Decidí **antes de armar el prompt** y declará el modelo en el plan interno.

### Capacidades reales de cada modelo

| | **nano-banana** (Gemini 2.5 Flash Image) | **gpt-image** (gpt-image-1) |
|---|---|---|
| Fidelidad del producto desde packshot | ⭐⭐⭐⭐⭐ excelente | ⭐⭐ inventa detalles del label |
| Texto on-image (1-3 palabras grandes) | ⭐⭐⭐ aceptable | ⭐⭐⭐⭐⭐ excelente |
| Texto on-image (frases largas, multi-línea, cuerpo) | ⭐⭐ alucina, espejea, rota | ⭐⭐⭐⭐⭐ legible y prolijo |
| Replica de UI (search bar, chips, badges, iconos con texto) | ⭐⭐ se confunde | ⭐⭐⭐⭐⭐ nativo |
| Layouts editoriales (revista, periódico, magazine) | ⭐⭐ rompe jerarquía | ⭐⭐⭐⭐⭐ entiende grid |
| Fotografía lifestyle / escena real con personas | ⭐⭐⭐⭐⭐ fotorrealista | ⭐⭐⭐ se siente "renderizado" |
| Recoloreo de producto desde ref | ⭐⭐⭐⭐ bueno (cuidado con wordmark rotado) | ⭐⭐ reinventa el shape |
| Composiciones tipográficas puras | ⭐⭐⭐ ok | ⭐⭐⭐⭐⭐ ideal |
| Velocidad / costo | Más rápido / barato | Más lento / caro |

### Decisión por tipo de ad (matriz)

| Tipo de pieza | Modelo | Por qué |
|---|---|---|
| Hero conversion con producto + hook tipográfico simple | **nano-banana** | Producto fiel manda |
| Benefits con chips, badges, íconos circulares + texto | **gpt-image** | Chips son UI, nano alucina |
| Antes/Después con foto real (skincare, fitness) | **nano-banana** | Necesita realismo |
| Problem/Solution con search-bar mockup o screenshot | **gpt-image** | Replica de UI |
| Alert / Tipográfico denso con producto chico | **gpt-image** | El texto manda |
| Editorial estilo revista / periódico / blog | **gpt-image** | Layout y tipografía |
| UGC / smartphone-like / lifestyle | **nano-banana** | Fotorrealismo |
| Carrusel beneficio paso-a-paso (icono + texto) | **gpt-image** | Layout limpio |
| Flatlay producto + accesorios | **nano-banana** | Fidelidad producto |
| Pure poster tipográfico (sin producto o producto silueta) | **gpt-image** | Composición tipo |
| Recoloreo de producto a otro color | **nano-banana** | Edit del shape |
| Imagen con cita / testimonio / texto largo on-image | **gpt-image** | Texto largo legible |

### Workflow híbrido (cuando ningún modelo solo alcanza)

Cuando necesitás **producto 100% fiel + texto on-image complejo**, hacer 2 pasos:

1. **Paso 1 — nano-banana**: generar la escena con el producto perfecto, dejando espacio limpio para el texto. No incluir texto on-image complejo en este paso.
2. **Paso 2 — gpt-image**: pasar la salida del paso 1 como referencia y pedir solo el agregado de texto/UI. Especificar "do not modify the product or scene, only add the typography layer described".

Casos donde el híbrido es la respuesta correcta:
- Producto con packaging denso + headline grande + cuerpo de texto largo
- Recoloreo de producto (nano) + chips de beneficios (gpt)
- Foto lifestyle (nano) + magazine-style overlay (gpt)

### Bandera roja — síntomas que indican que elegiste mal

Si después de generar ves alguno de estos, **regenerá con el otro modelo, no insistas**:
- Wordmark del producto sale espejado/rotado/inventado → era gpt-image (o híbrido)
- Headline sale alucinado tipo "FOR PRET FAFT" → era gpt-image
- Producto pierde subtítulos, conteos, claims del label → era nano-banana
- Chips/badges/iconos salen torcidos o con texto roto → era gpt-image
- La persona sale con cara plástica de stock → era nano-banana
- UI mockup (search bar, screenshot) sale "dibujado" → era gpt-image

### Sin defaults perezosos

NO existe "si dudo, nano-banana". Si dudás, **decidí explícitamente**: ¿domina el producto o domina el texto/UI? Si domina el producto y el texto es 1-3 palabras grandes → nano. Si domina cualquier cosa tipográfica o de UI → gpt. Si dominan los dos → híbrido en 2 pasos.

La elección NO se muestra al usuario en el output normal. Solo si pide ver el prompt → ahí aparece junto al resto del detalle técnico.

## Reglas duras
- Prompts en **inglés** (los modelos performan mejor)
- Texto on-image dentro del prompt va en **español** (es lo que verá el usuario final)
- Nada de prompts vagos tipo "a nice product photo". Cada slot, específico.
- Máximo **120 palabras** por prompt. Denso, no narrativo.
- Si no hay texto on-image → omitir ese slot, no dejarlo vacío.

## Consistencia entre tarjetas (CRÍTICO en carrusel)

Los modelos de imagen **inventan detalles** cuando regeneran un look "ya visto" desde cero (cinturones, accesorios, calzado, peinado, fondo). Si la T5 muestra el look de la T4 con cinturón pero la T4 no lo tenía, el carrusel queda quebrado.

### Regla 1 — Inventario de outfit explícito
Cada prompt de tarjeta con modelo debe **listar TODOS los ítems del outfit y los que NO van**, sin asumir que el modelo "completa" lógicamente. Ejemplo:

> *"...wearing the studded denim vest over a black silk camisole, sleek black tailored trousers, pointed black heels. **No belt, no jewelry, no bag, no scarf, hair down loose.**"*

Si una tarjeta NO lleva cinturón → escribirlo. Si NO lleva accesorios → escribirlo. El "negative inventory" es tan importante como el positivo.

### Regla 2 — Recap / grid (la última tarjeta del carrusel)
**NUNCA regenerar los looks desde cero en la T5.** El prompt del recap debe forzar uso literal de las salidas previas como referencia y prohibir invención:

> *"Composite three-panel grid using the EXACT outputs from cards 2, 3, and 4 as references. Do not modify, recompose or add any element. No new accessories, no belt changes, no shoe changes, no pose changes. Treat the three previous outputs as locked source images."*

Y en el bloque de referencias del recap, indicar SIEMPRE:
- *"Adjuntar las salidas finales de T2, T3 y T4 como referencias source. NO usar las imágenes originales del input."*

### Regla 3 — Workaround de seguridad
Si el modelo igual inventa detalles en el grid → recomendar al usuario armarlo manualmente en Canva/Photoshop con las 3 salidas individuales. Es más prolijo que pelearse con el modelo.

### Regla 4 — Consistencia de modelo y fondo
Cuando hay 3+ tarjetas con la misma persona, indicar en cada prompt (de T3 en adelante):
> *"Use the output of the previous card as additional reference for model identity, hair, lighting and background. Same face, same hair length and style, same studio backdrop, same lighting setup."*

Esto se le aclara al usuario en las **Notas finales** del entregable: el orden de generación y qué ref sumar en cada paso.
