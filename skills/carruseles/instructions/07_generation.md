# 07 — Generación de imágenes (Indash MCP)

Este es el paso donde la skill **deja de entregar solo prompts y genera las imágenes reales**. Después del self-check (paso 6), cada slide se genera con el MCP de **Indash** usando `mcp__indash__generate_image`, eligiendo el modelo correcto (`nano-banana` o `gpt-image`) según el tipo de slide.

**Gate del MCP `indash` (no negociable)**: el conector `indash` es **requerido** para este paso. Antes de generar, verificá que sus herramientas estén disponibles (conectado y autenticado). Si **no** lo está, **frená**: avisale al user en una sola intervención clara que tiene que conectar `indash` desde el panel de conectores de Cowork y por qué lo necesita esta tarea. No improvises workarounds ni dispares el flujo OAuth por tu cuenta; esperá a que lo conecte y recién ahí seguí. (Este gate ya se evaluó en el paso 0; acá se reconfirma porque es el punto donde se generan las imágenes. Política completa en `hooks/context/stack-policy.md`.)

---

## Flujo de generación (orden estricto)

### 1. Resolver el `workspace_id` (una sola vez)
`generate_image` requiere `workspace_id`. Resolvelo al inicio del paso 7:

- Si el user ya te lo dio en esta sesión → usalo.
- Si no → llamá `mcp__indash__list_workspaces` (o `search_workspaces` para dashers) y:
  - Si hay **un solo** workspace → usalo.
  - Si hay **varios** → preguntá al user cuál (única pregunta permitida en este paso).

Guardá el `workspace_id` para todos los slides.

### 2. Resolver las imágenes de referencia
Las referencias garantizan consistencia (producto/logo idénticos entre slides). Tres orígenes posibles, en este orden de preferencia:

1. **Brand kit / producto del workspace Indash** — si el producto vive en Indash, traé las URLs con `mcp__indash__get_product_images`, `mcp__indash__get_brand_kit` y `mcp__indash__get_style_references`, y pasalas como `reference_image_urls`.
2. **URLs públicas** que el user haya dado → `reference_image_urls`.
3. **Archivos locales** (ej. brand kit en disco, como el de un cliente que no es e-commerce) → convertilos a base64 y pasalos como `reference_images_base64` (con su `mime_type`). Para leer y convertir un archivo local usá Bash: `base64 -i "/ruta/al/archivo.png"`.

**Orden de las referencias**: producto primero, luego brand/estilo. (Mismo criterio que la descripción del tool: *product first, then brand/style*.)

### 3. Elegir el modelo por slide → ver "Selección de modelo" abajo
Por **default un carrusel = un solo modelo** (cohesión visual). Solo cambiás de modelo en un slide puntual cuando su necesidad lo justifica (ej. un slide CTA tipo infografía con mucho texto dentro de un carrusel fotográfico). Si mezclás, avisalo en las notas finales y cuidá que paleta/tipografía/encuadre se mantengan.

### 4. Generar slide por slide
Para cada slide, llamá `mcp__indash__generate_image` con:
- `workspace_id`
- `prompt` → el prompt del paso 5 (ya pasó self-check)
- `model` → el elegido para ese slide
- `aspect_ratio` → **`"4:5"`** (carrusel). Nunca dejes el default `1:1`.
- `reference_image_urls` y/o `reference_images_base64` → las del paso 2
- `output_name` → nombre claro y ordenado, ej. `"snowball_listing_slide1_hook.png"`

Generá **en orden** (slide 1 → N). Cada llamada devuelve una **URL pública** y guarda la imagen en la galería del workspace. Guardá las URLs para el output.

### 4b. Forzar el aspect ratio real 4:5 SIN cortar contenido (post-proceso obligatorio con gpt-image)
**`gpt-image` ignora el ratio fino y devuelve tamaños fijos**: para retrato entrega **1024×1536 (2:3)**, NO el 4:5 de Instagram. `nano-banana` respeta mejor el 4:5.

**NUNCA recortes (crop) para pasar de 2:3 a 4:5.** El 4:5 es más ANCHO que el 2:3, así que recortar alto se come arriba/abajo y **corta logos, headline y CTA** (error real cometido: el wordmark "Snowball partners" quedó cortado). El crop está PROHIBIDO acá.

La forma correcta es **agregar ancho (padding), sin perder un pixel**:

- **Piezas de fondo plano/oscuro (la mayoría tech/neón):** extendé los laterales replicando el borde. Es invisible en degradados oscuros. Con Python/cv2:
  ```python
  import cv2
  img=cv2.imread(src); h,w=img.shape[:2]
  tw=round(h*0.8); pad=tw-w; l=pad//2; r=pad-l
  out=cv2.copyMakeBorder(img,0,0,l,r,cv2.BORDER_REPLICATE)
  out=cv2.resize(out,(1080,1350),interpolation=cv2.INTER_AREA)
  cv2.imwrite(dst,out)
  ```
- **Piezas fotográficas (donde replicar el borde haría streaks):** rellená los laterales con una **copia desenfocada y oscurecida de la misma imagen** (fondo "cover" + blur), con el poster nítido centrado encima. Se ve premium, no corta nada. (cover blureado al 55% de brillo + foreground fit-by-height centrado.)
- Componé igual los prompts con **margen de seguridad** (no pegues logo/CTA/dots al borde), pero el padding es la garantía determinística de que nada se corta.
- **Verificá cada pieza mirándola** después del padding: logo, wordmark, headline y CTA completos.
- **Nunca entregues un slide que no sea exactamente 4:5 (1080×1350) o con cualquier elemento cortado.**

### 5. Revisar cada resultado (loop de calidad)
Después de generar, **mirá** cada imagen (leé la URL devuelta). Chequeá contra el slide:
- ¿El texto on-image se renderizó **legible y sin errores de ortografía**? (el punto más frágil — ver selección de modelo).
- ¿El producto/logo quedó **fiel** a la referencia?
- ¿Respetó paleta, composición y aspect ratio 4:5?
- ¿La marca cumple sus reglas (en Snowball: sin sombras/contorno/distorsión del logo, intersección blanca visible)?

Si algo falla:
- **Texto ilegible/mal escrito** → regenerá ese slide con `gpt-image` (mejor render de texto) o reforzá la instrucción de texto.
- **Producto/logo deformado** → regenerá con `nano-banana` reforzando el anclaje a la referencia.
- **Hasta 2 reintentos por slide.** Si sigue fallando, entregalo igual marcándolo en notas y proponé el ajuste.

---

## Selección de modelo: nano-banana vs gpt-image

Ambos están disponibles en `generate_image` vía el parámetro `model`. No son intercambiables: cada uno gana en cosas distintas.

### nano-banana (Gemini 2.5 Flash Image) — DEFAULT para e-commerce
**Su superpoder: fidelidad a la imagen de referencia.** Mantiene el producto/packaging/logo **idéntico** entre los N slides. También es el más fuerte en fotorrealismo de producto y de personas (piel, materiales, luz) cuando lo dirigís con las 7 leyes.

**Elegilo cuando el slide es:**
- Fotográfico / fotorrealista con un **producto real** que debe verse idéntico a la referencia.
- Lifestyle con **persona** (casting realista, piel natural).
- Cualquier slide donde la **consistencia del producto entre slides** es lo más importante.
- Multi-image fusion (combinar producto + escena + modelo).

**Es más débil en:**
- Renderizar **mucho texto** o **texto largo** dentro de la imagen (puede deformar letras, especialmente en español con tildes/ñ).
- Layouts tipográficos complejos, infografías, charts, tablas, diagramas.

**Cómo prompteárlo:** prosa narrativa cinematográfica + anclaje a la referencia + las 7 leyes de `05_prompt_engineering.md`. Sin keyword soup. Sin prompts negativos. Texto on-image: corto y entre comillas.

### gpt-image (OpenAI) — para slides con peso tipográfico / gráfico
**Su fuerza: render de texto legible y seguimiento de instrucciones de layout.** Escribe títulos, párrafos cortos, bullets, badges y composiciones tipo poster/infografía mucho mejor que nano-banana, y respeta indicaciones de disposición con más precisión.

**Elegilo cuando el slide es:**
- **Text-heavy**: titular largo, varios bloques de texto, listas, números grandes, datos.
- **Infografía / data viz / diagrama / comparativa / tabla**.
- Diseño gráfico tipo **poster editorial** donde el texto rendereado importa más que la fidelidad fotográfica a un producto.
- Marca **sin producto físico** (agencia, SaaS, servicio) donde el "sujeto" es concepto + texto + identidad gráfica (caso típico: carruseles educativos/dolor→solución).

**Es más débil en:**
- **Consistencia exacta** de un producto/logo entre varias generaciones (menos fiel a la referencia que nano-banana; puede reinterpretar). Si la identidad visual exacta es crítica en todos los slides, esto pesa.
- A veces aplica una estilización/calidez propia.

**Cómo prompteárlo:** sirve la misma prosa, pero podés ser **más explícito y estructurado** con el layout y el texto: indicá jerarquía, posición exacta, y el texto literal a renderizar entre comillas con su color hex y peso. Pedí explícitamente *"texto nítido, ortografía exacta, sin errores de tipeo"*. Respeta bien colores hex y fondos limpios/transparentes. Igual: sin keyword soup, sin prompts negativos.

### Tabla de decisión rápida

| El slide es… | Modelo |
|---|---|
| Producto real que debe verse idéntico entre slides | **nano-banana** |
| Persona / lifestyle fotorrealista | **nano-banana** |
| Hero shot de packaging / botella / textil | **nano-banana** |
| Titular largo, bullets, varios bloques de texto | **gpt-image** |
| Infografía, comparativa, data, diagrama, tabla | **gpt-image** |
| Poster editorial / concepto sin producto físico | **gpt-image** |
| Logo/símbolo de marca que debe quedar fiel | **nano-banana** (anclá la referencia) |

### Regla de cohesión del carrusel
1. **Default: un modelo para todo el carrusel.** Elegí según el peso dominante (¿manda el producto/foto o manda el texto/gráfica?).
2. Carrusel **fotográfico de producto** (e-commerce clásico) → **nano-banana** en todos los slides; el CTA también, salvo que sea infografía pura.
3. Carrusel **conceptual/educativo sin producto** (servicio, agencia, mucho texto) → **gpt-image** en todos los slides; usá nano-banana solo si un slide depende de fidelidad fotográfica/logo exacta.
4. Si mezclás modelos, **mantené idénticos** paleta, tipografía descripta, lente/encuadre y mood para que no se note el salto, y **declaralo en las notas finales**.

---

## Reglas no-negociables del paso 7

1. **Generás las imágenes**, no entregás solo prompts. El output final lleva las imágenes (URLs) + los prompts como registro.
2. **Siempre 4:5 real (1080×1350)** en el entregable. Pasá `aspect_ratio: "4:5"` en la llamada, y como gpt-image devuelve 2:3 (1024×1536), **recortá/reescalá a 1080×1350** (paso 4b). Para Stories sería 9:16, pero esta skill es 4:5.
3. **Siempre pasás la(s) referencia(s)** cuando existen (producto/logo), para consistencia entre slides.
4. **Elegís el modelo conscientemente** por slide según la tabla; no dejás el default sin pensarlo.
5. **Revisás cada imagen generada** y regenerás (máx. 2 reintentos) si falla texto, fidelidad o marca.
6. **Un carrusel = un modelo** por default; mezclar es la excepción justificada y declarada.
7. Si el MCP de Indash no está conectado o falta `workspace_id` que no podés resolver → **frená y pedilo**, no inventes.
