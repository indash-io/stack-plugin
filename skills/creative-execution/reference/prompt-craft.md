# Prompt Craft — cómo se escribe un prompt de imagen en Studio

Esto es **conocimiento, no workflow** (el workflow es el proceso de 8 pasos del
SKILL.md). Acá está cómo escribir prompts que funcionen para
`mcp__indash__generate_image`, en cualquier formato.

**El marco de todo:** en Studio el modelo genera SOLO la escena orgánica. El
texto, el logo, el precio y los badges son capas del manifiesto — el prompt
jamás los pide. Lo que sí pide el prompt es el **espacio negativo** donde esas
capas van a caer.

## Las 7 leyes del prompting cinematográfico

### Ley 1 — Lenguaje natural narrativo, no keywords

Los modelos modernos fueron entrenados con captions tipo descripción humana.
**Rinden mejor con prosa fluida, no con listas de keywords pegoteadas.**

- ❌ *"perfume bottle, marble, golden hour, 85mm, f/2.0, editorial, luxury, warm tones, cinematic, photorealistic, 8k, masterpiece"*
- ✅ *"Un frasco de perfume sobre un pedestal de mármol gastado, iluminado por la luz cálida del atardecer entrando por una ventana lateral. Tomado con lente de 85mm a f/2.0, mood de lujo silencioso."*

El segundo es **más corto y más efectivo**. Confiá en oraciones completas.

### Ley 2 — Anclá siempre a la imagen de referencia

Si pasás refs (producto, persona, estilo), **el producto/sujeto debe salir
idéntico** a esa referencia. La única forma de garantizarlo: mencionar
explícitamente la imagen.

Patrones que funcionan:
- *"Usá la imagen de producto provista como sujeto exacto — conservá envase, etiquetas, colores y proporciones idénticos."*
- *"El producto de la imagen de referencia, sin alteraciones, ubicado en…"*

Patrones que **fallan**:
- No mencionar la ref → el modelo "imagina" un producto similar y deriva entre piezas.
- Describir el producto con palabras además de referenciarlo → conflicto: el
  modelo prioriza tu descripción y altera el producto.

**Regla**: si hay ref, **no describas el producto**. Identificación mínima
(qué es + color base) y dirigí su contexto. Es la misma regla del paso 3 del
SKILL.md, vista desde el prompt.

### Ley 3 — Dirección cinematográfica, no adjetivos vagos

Los modelos entienden vocabulario fotográfico técnico (lente, apertura,
ángulo, calidad de luz). Es lo que más diferencia un prompt amateur de uno pro.

| Vago | Específico |
|---|---|
| *"foto bonita"* | *"tomado con 85mm a f/2.0, ángulo a la altura del producto"* |
| *"buena luz"* | *"luz de ventana lateral suave, temperatura cálida 3200K, con sutil rim light"* |
| *"fondo limpio"* | *"sobre travertino color hueso, espacio negativo generoso en el tercio superior"* |
| *"que se vea profesional"* | *"claridad de formato medio, foco nítido, mood de lujo silencioso"* |

### Ley 4 — Nada de prompts negativos

Los modelos no procesan bien frases tipo *"sin gente, sin desenfoque, sin
texto"*. Tienden a confundirse o a generar exactamente lo que pediste evitar.

**Regla**: describí siempre lo que SÍ querés ver. Si necesitás que una zona
quede libre, pedila como algo positivo: *"pared lisa fuera de foco en el
tercio superior"*, no *"sin objetos arriba"*.

### Ley 5 — El espacio negativo se pide, no se espera

La versión Studio de la vieja ley del texto on-image: como el texto va en
capas, **la escena se diseña PARA esas capas**. El prompt reserva el lugar:

- Decidí primero dónde van las capas de texto (ver
  `../style/composicion-texto.md`).
- Pedí ese espacio en el prompt como parte de la composición: *"tercio
  superior limpio y fuera de foco"*, *"mitad izquierda con pared lisa en
  sombra suave"*, *"superficie despejada en el cuarto inferior"*.
- Pensá el **contraste local** de esa zona: si el texto va blanco, la zona
  tiene que quedar oscura o poder llevar un scrim encima (capa `rect`); si va
  oscuro, clara. El scrim arregla mucho, pero una escena que ya trae la zona
  calma arregla más.

Una escena sin lugar para el texto obliga a scrims agresivos o a re-generar:
es un candidato perdido por no pedir una frase.

### Ley 6 — Personas: dirigí o salen "AI"

Sin dirección, los modelos generan el clásico "rostro IA" (piel plástica,
simetría perfecta, expresión vacía). Mitigaciones:

1. **Edad concreta**, no "joven" — *"mujer de 38 años"* ≫ *"mujer joven"*.
2. **Textura de piel natural obligatoria** — *"poros visibles, líneas finas,
   sin sobre-suavizado"*. Esta frase elimina ~60% del look IA.
3. **Expresión específica** — *"concentración serena mirándose al espejo"* ≫
   *"sonriendo"*.
4. **Pose candid, no posada** — *"momento candid, captura espontánea"*.
5. **Manos visibles → manos descriptas** — qué hace la mano, posición de los
   dedos, qué sostiene. Evita los dedos extra clásicos.
6. **Casting realista** — *"belleza realista, no de pasarela"*, *"rostro con
   carácter"*.
7. **Iluminación que muestre piel** — luz lateral suave > luz frontal plana.

### Ley 7 — Consistencia entre piezas hermanas

Si vas a generar N imágenes que viven juntas (los slides de un carrusel, una
secuencia de stories), tienen que sentirse tomadas en la misma sesión.
Comparten:

- **Las MISMAS refs de producto** (no "parecidas" — las mismas).
- **Mismo lente** (50mm en todas, o 85mm en todas — no mezcles).
- **Misma paleta** (heredada de la marca del proyecto).
- **Mismo mood** (una palabra que define la secuencia entera).
- **Mismo tratamiento general de luz.**

Lo que **debe variar**: ángulo de cámara, escena/contexto, composición (el
espacio negativo cae en distinto lugar → el placement del texto varía),
distancia (una pieza cerrada, otra abierta).

Sin variación → repetitivo. Sin consistencia → desarmado.

## EDIT vs GENERATE — la distinción clave

Editar una imagen NO es lo mismo que regenerar una. Confundirlos es el error
más caro porque deshace cambios que ya estaban bien.

### Generate (candidato nuevo)

Querés una imagen nueva. Las refs son producto/estilo. El prompt = la escena
completa (con las 7 leyes).

### Edit (corregir un candidato que casi sale)

Tenés un candidato bueno al que hay que cambiarle UNA cosa (el fondo, la luz
de una zona, un elemento). Reglas duras:

1. **El candidato base va PRIMERO en `refs`** (`creatives/.../layers/img/v2.jpg`,
   o el archivo que sea el `active`), las demás refs después.
2. **El prompt describe SOLO el delta**, no la imagen entera:
   - ❌ *"Un frasco sobre mármol con luz cálida… ahora con fondo más oscuro."*
   - ✅ *"Tomá la imagen base y oscurecé el fondo: de mármol claro a piedra
     carbón, manteniendo producto, luz y composición idénticos."*
3. **Mencioná explícitamente lo que NO debe cambiar.**
4. **Pasá el mismo `aspect_ratio`** que la pieza (parámetro de la tool, nunca
   en el texto del prompt). Sin él, el modelo cambia las dimensiones.
5. El resultado es un candidato NUEVO (`vN+1` + sidecar) — nunca pisa al base.

## Anti-patrones

1. **Keyword soup** — pegote estilo Midjourney. Degrada el resultado.
2. **Doble descripción del producto** — si referenciás la foto, no lo
   describas: compite con la referencia.
3. **Stacking de adjetivos** — *"limpio, minimalista, moderno, profesional,
   elegante"*. Una palabra precisa gana: *"travertino color hueso"*.
4. **Efectos de video en una imagen** — *"motion blur mientras rota"*. Es una
   imagen estática.
5. **Espacio negativo no pedido** — la escena sale llena y el texto no tiene
   dónde vivir (Ley 5).
6. **Asumir que el modelo "sabe" la marca** — *"estética de Aesop"* a veces
   funciona, a veces no. Describí la estética por sus elementos (paleta,
   materiales, mood, luz).
7. **Múltiples unidades con una sola ref** — *"tres frascos en línea"* con una
   ref → tres frascos distintos, ninguno fiel. Una ref = un producto en escena.
8. **Edit que se vuelve generate** — pedir un edit describiendo la imagen
   entera (ver arriba).
9. **Pedirle texto o logos al modelo** — el anti-patrón número uno de Studio.
   Eso es una capa; si lo escribiste en el prompt, borralo y armá la capa.

## Trucos por tipo de producto

- **Etiqueta tipográfica importante** (perfume, vino, skincare): anclá fuerte
  (*"conservá la tipografía de la etiqueta idéntica"*), evitá ángulos muy
  oblicuos en piezas hero, y subí a `resolution: "4K"` si el texto del label
  es chico.
- **Reflectivo / metálico / vidrio**: especificá la fuente de luz porque se va
  a reflejar (*"luz suave de softbox grande"*); pedí rim light para separar
  del fondo.
- **Textil / ropa**: cómo está dispuesta la prenda (*"plegada con dobleces
  precisos"* / *"colgada con caída natural"*) y el material (*"textura de
  lino visible"*).
- **Comida / bebida**: frescura (*"condensación visible"*, *"vapor sutil"*);
  3/4 alto vende, cenital cuenta.
- **Chico** (joyería, accesorios): macro 100mm f/2.8, fondo simple.
- **Que requiere demostración**: persona en cuadro → Ley 6, manos descriptas
  con precisión.

## Estructura mental de un prompt

En prosa fluida, cubriendo en orden:

```
[Anclaje a la ref si hay]. [Escena y contexto].
[Cámara: lente, ángulo, composición, profundidad de campo].
[Iluminación: fuente + dirección + calidad + temperatura].
[Estilo + textura + mood en una frase].
[Paleta de la marca, con hex].
[Persona — si aplica, con Ley 6].
[Espacio negativo: dónde queda libre la zona de las capas de texto].
[Calidad técnica de cierre — fotorrealismo, foco].
```

**El aspect ratio NO va en el texto**: es el parámetro `aspect_ratio` de
`generate_image` (`4:5`, `9:16`, `1:1`…), siempre el del canvas de la pieza.

## Checklist al cerrar un prompt

- [ ] ¿Anclé a la referencia en la primera oración (si hay)?
- [ ] ¿Identificación del producto mínima (qué es + color), sin describirlo?
- [ ] ¿Lente, ángulo, composición, profundidad?
- [ ] ¿Fuente, dirección, calidad y temperatura de luz?
- [ ] ¿Estilo + mood en una frase precisa? ¿Paleta con hex?
- [ ] Si hay persona: ¿edad concreta, textura de piel, expresión específica, manos descriptas?
- [ ] ¿Pedí el espacio negativo donde van las capas de texto?
- [ ] ¿CERO texto, logos, precios o badges pedidos al modelo?
- [ ] ¿Prosa fluida, sin keyword soup, sin negaciones?
- [ ] Si es parte de secuencia: ¿mismas refs, lente, mood, paleta que las hermanas?
- [ ] Si es edit: ¿candidato base primero en refs, prompt solo con el delta, mismo aspect_ratio?
