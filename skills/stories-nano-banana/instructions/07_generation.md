# 07 — Generación de imágenes (Indash MCP)

Este es el paso donde la skill **deja de entregar solo prompts y genera las imágenes reales** de la secuencia de Stories. Después del self-check (paso 6), cada story se genera con el MCP de **Indash** usando `mcp__indash__generate_image`, eligiendo el modelo correcto (`nano-banana` o `gpt-image`) según el tipo de story.

**Gate del MCP `indash` (no negociable)**: el conector `indash` es **requerido** para este paso. Antes de generar, verificá que sus herramientas estén disponibles (conectado y autenticado). Si **no** lo está, **frená**: avisale al user en una sola intervención clara que tiene que conectar `indash` desde el panel de conectores de Cowork y por qué lo necesita esta tarea. No improvises workarounds ni dispares el flujo OAuth por tu cuenta; esperá a que lo conecte y recién ahí seguí. (Este gate ya se evaluó en el paso 0; acá se reconfirma porque es el punto donde se generan las imágenes. Política completa en `hooks/context/stack-policy.md`.)

**Los stickers de engagement NO son parte de la imagen generada.** El poll, la pregunta, el countdown, el slider o el link son **sugerencias del shot list** que el user agrega en Instagram al subir cada story. La imagen que generás acá es el fondo limpio; el sticker va encima en la app. No intentes "dibujar" un sticker dentro de la imagen.

---

## Flujo de generación (orden estricto)

### 1. Resolver el `workspace_id` (una sola vez)
`generate_image` requiere `workspace_id`. Resolvelo al inicio del paso 7:

- Si el user ya te lo dio en esta sesión → usalo.
- Si no → llamá `mcp__indash__list_workspaces` (o `search_workspaces` para dashers) y:
  - Si hay **un solo** workspace → usalo.
  - Si hay **varios** → preguntá al user cuál (única pregunta permitida en este paso).

Guardá el `workspace_id` para todas las stories.

### 2. Resolver las imágenes de referencia
Las referencias garantizan consistencia (producto/logo idénticos entre stories). Tres orígenes posibles, en este orden de preferencia:

1. **Brand kit / producto del workspace Indash** — si el producto vive en Indash, traé las URLs con `mcp__indash__get_product_images`, `mcp__indash__get_brand_kit` y `mcp__indash__get_style_references`, y pasalas como `reference_image_urls`.
2. **URLs públicas** que el user haya dado → `reference_image_urls`.
3. **Archivos locales** (ej. brand kit en disco, como el de un cliente que no es e-commerce) → convertilos a base64 y pasalos como `reference_images_base64` (con su `mime_type`). Para leer y convertir un archivo local usá Bash: `base64 -i "/ruta/al/archivo.png"`.

**Orden de las referencias**: producto primero, luego brand/estilo. (Mismo criterio que la descripción del tool: *product first, then brand/style*.)

### 3. Elegir el modelo por story → ver "Selección de modelo" abajo
Por **default una secuencia = un solo modelo** (cohesión visual). Solo cambiás de modelo en una story puntual cuando su necesidad lo justifica (ej. una story CTA tipo infografía con mucho texto dentro de una secuencia fotográfica). Si mezclás, avisalo en las notas finales y cuidá que paleta/tipografía/encuadre se mantengan.

### 4. Generar story por story
Para cada story, llamá `mcp__indash__generate_image` con:
- `workspace_id`
- `prompt` → el prompt del paso 5 (ya pasó self-check)
- `model` → el elegido para esa story
- `aspect_ratio` → **`"9:16"`** (Stories). **Nunca dejes el default `1:1`.**
- `reference_image_urls` y/o `reference_images_base64` → las del paso 2
- `output_name` → nombre claro y ordenado, ej. `"solar04_story1_hook.png"`

Generá **en orden** (story 1 → N). Cada llamada devuelve una **URL pública** y guarda la imagen en la galería del workspace. Guardá las URLs para el output.

### 4b. Forzar el aspect ratio real 9:16 SIN cortar contenido (post-proceso obligatorio con gpt-image)
**`gpt-image` ignora el ratio fino y devuelve tamaños fijos**: para retrato entrega **1024×1536 (2:3)**, NO el 9:16 (1080×1920) de Instagram Stories. `nano-banana` respeta mejor el 9:16.

**NUNCA recortes (crop) para pasar de 2:3 a 9:16.** Acá la diferencia con carruseles es clave: el **9:16 es más ALTO y angosto** que el 2:3. El 2:3 que devuelve gpt-image es relativamente más bajo/cuadrado; para llegar al 9:16 hay que **agregar alto, no ancho**. Si recortás los lados para estilizar el ratio, te comés el producto y los márgenes; el crop está PROHIBIDO acá.

La forma correcta es **agregar alto (padding VERTICAL, arriba y abajo), sin perder un pixel**. Esto además **juega a favor**: el padding cae justo en las **zonas de UI de Instagram** — la franja de arriba (avatar, nombre, tiempo) y la de abajo (input "enviar mensaje", sticker, indicadores). Es exactamente donde NO querés contenido importante.

- **Piezas de fondo plano/oscuro (la mayoría):** extendé arriba y abajo replicando el borde. Es invisible en degradados/fondos lisos. Con Python/cv2:
  ```python
  import cv2
  img = cv2.imread(src); h, w = img.shape[:2]
  th = round(w * 16 / 9); pad = th - h; top = pad // 2; bottom = pad - top
  out = cv2.copyMakeBorder(img, top, bottom, 0, 0, cv2.BORDER_REPLICATE)
  out = cv2.resize(out, (1080, 1920), interpolation=cv2.INTER_AREA)
  cv2.imwrite(dst, out)
  ```
- **Piezas fotográficas (donde replicar el borde haría streaks):** rellená arriba/abajo con una **copia desenfocada y oscurecida de la misma imagen** (fondo "cover" + blur), con el poster nítido centrado encima. Se ve premium, no corta nada. (cover blureado al 55% de brillo + foreground fit-by-width centrado.)
- Componé igual los prompts con **margen de seguridad** y respetando la zona segura (no pegues copy/CTA al borde superior ni inferior), pero el padding es la garantía determinística de que nada se corta.
- **Verificá cada pieza mirándola** después del padding: producto, headline y CTA completos, y el copy dentro de la zona segura.
- **Nunca entregues una story que no sea exactamente 9:16 (1080×1920) o con cualquier elemento cortado.**

### 5. Revisar cada resultado (loop de calidad)
Después de generar, **mirá** cada imagen (leé la URL devuelta). Chequeá contra la story:
- ¿El texto on-image se renderizó **legible y sin errores de ortografía**? (el punto más frágil — ver selección de modelo).
- ¿El producto/logo quedó **fiel** a la referencia?
- ¿Respetó paleta, composición y aspect ratio 9:16 (1080×1920)?
- ¿El copy on-image quedó dentro de la **zona segura** (entre el 14% y 85% del alto vertical), sin meterse en las franjas de UI de Instagram (avatar arriba, input abajo)?
- ¿Dejaste libre la zona del sticker sugerido (típicamente tercio inferior ~70-85%) para que no lo tape el copy?

Si algo falla:
- **Texto ilegible/mal escrito** → regenerá esa story con `gpt-image` (mejor render de texto) o reforzá la instrucción de texto.
- **Producto/logo deformado** → regenerá con `nano-banana` reforzando el anclaje a la referencia.
- **Copy fuera de la zona segura** → reforzá en el prompt el placement dentro del 14%-85% vertical y regenerá.
- **Hasta 2 reintentos por story.** Si sigue fallando, entregala igual marcándola en notas y proponé el ajuste.

---

## Selección de modelo: nano-banana vs gpt-image

Ambos están disponibles en `generate_image` vía el parámetro `model`. No son intercambiables: cada uno gana en cosas distintas. (Mismo criterio que carruseles.)

### nano-banana (Gemini 2.5 Flash Image) — DEFAULT para e-commerce
**Su superpoder: fidelidad a la imagen de referencia.** Mantiene el producto/packaging/logo **idéntico** entre las N stories. También es el más fuerte en fotorrealismo de producto y de personas (piel, materiales, luz) cuando lo dirigís con las 7 leyes.

**Elegilo cuando la story es:**
- Fotográfica / fotorrealista con un **producto real** que debe verse idéntico a la referencia.
- Lifestyle con **persona** (casting realista, piel natural).
- Cualquier story donde la **consistencia del producto entre stories** es lo más importante.
- Multi-image fusion (combinar producto + escena + modelo).

**Es más débil en:**
- Renderizar **mucho texto** o **texto largo** dentro de la imagen (puede deformar letras, especialmente en español con tildes/ñ). En Stories esto pesa menos porque el copy es corto (≤6-8 palabras).
- Layouts tipográficos complejos, infografías, charts, tablas, diagramas.

**Cómo prompteárlo:** prosa narrativa cinematográfica + anclaje a la referencia + las 7 leyes de `05_prompt_engineering.md`. Sin keyword soup. Sin prompts negativos. Texto on-image: corto, entrecomillado, dentro de la zona segura.

### gpt-image (OpenAI) — para stories con peso tipográfico / gráfico
**Su fuerza: render de texto legible y seguimiento de instrucciones de layout.** Escribe títulos, badges y composiciones tipo poster/infografía mucho mejor que nano-banana, y respeta indicaciones de disposición con más precisión.

**Elegilo cuando la story es:**
- **Text-heavy** para el formato: titular fuerte con números grandes, dato, comparativa corta.
- **Infografía / data viz / diagrama / comparativa** simple.
- Diseño gráfico tipo **poster editorial** donde el texto rendereado importa más que la fidelidad fotográfica a un producto.
- Marca **sin producto físico** (agencia, SaaS, servicio) donde el "sujeto" es concepto + texto + identidad gráfica.

**Es más débil en:**
- **Consistencia exacta** de un producto/logo entre varias generaciones (menos fiel a la referencia que nano-banana; puede reinterpretar). Si la identidad visual exacta es crítica en todas las stories, esto pesa.
- A veces aplica una estilización/calidez propia.
- **Devuelve 2:3 (1024×1536), no 9:16** → siempre requiere el padding vertical del paso 4b.

**Cómo prompteárlo:** sirve la misma prosa, pero podés ser **más explícito y estructurado** con el layout y el texto: indicá jerarquía, posición exacta (dentro de la zona segura 14%-85%), y el texto literal a renderizar entre comillas con su color hex y peso. Pedí explícitamente *"texto nítido, ortografía exacta, sin errores de tipeo"*. Respeta bien colores hex y fondos limpios/transparentes. Igual: sin keyword soup, sin prompts negativos.

### Tabla de decisión rápida

| La story es… | Modelo |
|---|---|
| Producto real que debe verse idéntico entre stories | **nano-banana** |
| Persona / lifestyle fotorrealista | **nano-banana** |
| Hero shot de packaging / botella / textil | **nano-banana** |
| Titular fuerte con número/dato grande | **gpt-image** |
| Infografía, comparativa, data, diagrama | **gpt-image** |
| Poster editorial / concepto sin producto físico | **gpt-image** |
| Logo/símbolo de marca que debe quedar fiel | **nano-banana** (anclá la referencia) |

### Regla de cohesión de la secuencia
1. **Default: un modelo para toda la secuencia.** Elegí según el peso dominante (¿manda el producto/foto o manda el texto/gráfica?).
2. Secuencia **fotográfica de producto** (e-commerce clásico) → **nano-banana** en todas las stories; el CTA también, salvo que sea infografía pura.
3. Secuencia **conceptual/educativa sin producto** (servicio, agencia, mucho texto) → **gpt-image** en todas las stories; usá nano-banana solo si una story depende de fidelidad fotográfica/logo exacta.
4. Si mezclás modelos, **mantené idénticos** paleta, tipografía descripta, lente/encuadre y mood para que no se note el salto, y **declaralo en las notas finales**.

---

## Reglas no-negociables del paso 7

1. **Generás las imágenes**, no entregás solo prompts. El output final lleva las imágenes (URLs) + shot list con stickers + los prompts como registro.
2. **Siempre 9:16 real (1080×1920)** en el entregable. Pasá `aspect_ratio: "9:16"` en la llamada, y como gpt-image devuelve 2:3 (1024×1536), **agregá padding VERTICAL (arriba/abajo) y reescalá a 1080×1920** (paso 4b). Nunca crop.
3. **Siempre pasás la(s) referencia(s)** cuando existen (producto/logo), para consistencia entre stories.
4. **Elegís el modelo conscientemente** por story según la tabla; no dejás el default sin pensarlo.
5. **Revisás cada imagen generada** y regenerás (máx. 2 reintentos) si falla texto, fidelidad, marca o zona segura.
6. **Respetás la zona segura** (copy entre 14% y 85% del alto) como criterio de revisión de cada imagen, y dejás libre la franja del sticker.
7. **Los stickers de engagement no van dentro de la imagen** — son sugerencias del shot list que el user agrega en Instagram.
8. **Una secuencia = un modelo** por default; mezclar es la excepción justificada y declarada.
9. Si el MCP de Indash no está conectado o falta `workspace_id` que no podés resolver → **frená y pedilo**, no inventes.
