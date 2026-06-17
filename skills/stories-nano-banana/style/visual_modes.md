# Visual Modes — Minimalista vs Lifestyle cinematográfico

Esta skill admite dos **modos visuales canónicos** para la secuencia de stories. El modo se elige en Decisions (paso 3) y define varios parámetros del prompt: mood, lente, luz, presencia de persona, paleta y color del texto on-image.

Los dos modos no son excepciones — son los **defaults** que cubren la mayoría de los productos. Si el user no especifica, **default = Minimalista**. Si el user pide "más onda", "lifestyle", "cinematográfico", "con persona", "con contexto", "real" → cambiá a Lifestyle. Si pide A/B o "ambos" → generá las dos secuencias paralelas (ver Modo C abajo).

**Una secuencia = un modo.** No mezclar modos dentro de la misma secuencia (si story 1 es minimalista y story 2 es lifestyle, la secuencia se siente desarmada).

---

## Modo A — Minimalista

### Cuándo usarlo
- Default si no hay señal en otro sentido.
- Producto que se vende por su forma/objeto en sí (joyería, frasco, cerámica, electrónico, decoración, packaging premium).
- Marca con tono editorial/contemporáneo/premium.
- Feed del cliente ya saturado de lifestyle → necesita corte limpio.
- Cuando el producto **es la atención** (no el contexto).

### Parámetros canónicos

| Parámetro | Valor |
|---|---|
| **Mood** | una palabra precisa heredada del producto (*"sólido y silencioso"*, *"lujo silencioso"*, *"calmo y considerado"*) |
| **Lente** | 50mm a f/2.0–f/2.2 (default). 85mm para premium. 100mm macro para joyería/detalle. |
| **Luz** | softbox controlado, suave envolvente, neutra 5000K o cálida 4500K. Sin contraste extremo. |
| **Fondo** | superficie + pared monocromática neutra de alto valor (blanco roto, hueso, cemento claro, travertino). El fondo desaparece. |
| **Persona** | NO. El producto es único sujeto. |
| **Paleta** | acotada a 3-4 colores heredados del producto. |
| **Color del texto on-image** | un hex de la paleta (típicamente el de mayor contraste sobre el fondo). **Casi nunca blanco.** |
| **Estilo descripto** | *"editorial-industrial / minimal / escultórico / heritage moderno"* |
| **Textura** | claridad digital limpia, sin grano. |

### Frases tipo en el prompt
- *"sobre una superficie de cemento alisado tono hueso, fondo de pared lisa blanco roto que se diluye sin transición"*
- *"luz suave de softbox frontal-lateral, calidad envolvente, temperatura neutra 5000K"*
- *"mood sólido y silencioso, casi escultórico"*
- *"texto en negro carbón #1A1A1A sobre fondo blanco roto"*

---

## Modo B — Lifestyle cinematográfico

### Cuándo usarlo
- User pide "más onda", "real", "con vida", "con personas", "lifestyle", "cinematográfico", "documental".
- Producto cuyo valor está en el **uso** (electrodoméstico, herramienta, ropa, comida/bebida, cosmético en aplicación, ollas/utensilios).
- Marca con tono storytelling, oficio, comunidad, autenticidad.
- Feed ya tiene mucho minimalista y necesita un golpe vivo.
- Cuando el contexto **agrega valor narrativo** al producto.

### Parámetros canónicos

| Parámetro | Valor |
|---|---|
| **Mood** | dos palabras que mezclan acción + temperatura emocional (*"oficio caliente"*, *"ritual matinal calmo"*, *"fin de semana lento"*, *"taller en marcha"*) |
| **Lente** | 35mm a f/2.8 (default — captura contexto). 50mm a f/2.0 para acercar. |
| **Luz** | natural cálida (sol bajo, ventana al atardecer) o tungsteno/mixta de interior real. Lateral, contraste alto, fondo en sombra. Temperatura 3200K–4000K. |
| **Fondo** | escena de uso real (cocina profesional, baño con luz de mañana, taller, mesa servida, exterior natural). El fondo cuenta narrativamente. |
| **Persona** | SÍ — al menos en hook o desarrollo. Manos / torso / a veces rostro. Aplicar **Ley 6** de `instructions/05_prompt_engineering.md` sin excepción. |
| **Paleta** | 5-6 colores: 3-4 heredados del producto + 2 sumados del entorno (madera cálida, acero, plantas, piedra, luz ámbar). |
| **Color del texto on-image** | **blanco hueso #ECE7DC** con jerarquía bold/regular sobre fondo cálido oscuro. Garantiza contraste cinematográfico. |
| **Estilo descripto** | *"documental cinematográfico / lifestyle editorial / oficio"* |
| **Textura** | grano sutil tipo 35mm, claridad digital con personalidad fotográfica. |

### Frases tipo en el prompt
- *"sobre una mesada de acero inoxidable cepillado de cocina profesional, hornalla con llama azul-naranja desenfocada al fondo"*
- *"luz cálida lateral tipo tungsteno mixto, dura y direccional con leve rebote ámbar, temperatura 3200K, contraste alto cinematográfico"*
- *"mood oficio caliente, cocina real"*
- *"texto en blanco hueso #ECE7DC con jerarquía bold/regular, contraste pleno contra fondo oscuro"*

### Reglas duras del modo B
1. **Persona descripta con Ley 6**: edad concreta, textura de piel real, expresión específica, manos descriptas. Sin excepción.
2. **Contexto justificado por la categoría**: no metas baño si vendés ollas. Inferir contexto natural de uso desde el discovery.
3. **El producto sigue siendo el sujeto principal**: si la persona u objeto secundario tapan al producto, la story pierde.
4. **Texto blanco solo si el fondo es oscuro/cálido-oscuro**. Si la escena queda muy clara, ajustá el color del texto a un hex de la paleta con contraste.

---

## Modo C — A/B paralelo (opcional)

Si el user pide explícitamente A/B testing, "las dos versiones" o "minimalista + lifestyle":

- Generás **dos secuencias completas** (mismo N de stories cada una).
- Las dos **comparten**: producto, copy on-image story por story, sticker sugerido por story, lógica narrativa, hook, CTA.
- Las dos **varían**: lente, mood, luz, presencia de persona, paleta extendida, color del texto, fondo/escena.
- En el output van en **bloques separados** con encabezados claros: `## Secuencia A · Minimalista` y `## Secuencia B · Lifestyle cinematográfico`. Ver `instructions/06_output_format.md`.
- Notas finales sugieren cómo testear (ej: *"subí A en historia destacada permanente y B en stories del día, medí completion rate y respuestas al poll"*).

---

## Cómo elegir el modo en Decisions

En `instructions/03_decisions.md`, la pregunta consolidada incluye el campo **"Modo visual"**:

- **Default**: Minimalista (con razón en una línea).
- Si el discovery sugiere lifestyle (producto de uso, marca con storytelling, feed pide variedad) → propuesta default = Lifestyle.
- Si dudás → ofrecé **A/B** explícitamente: *"También puedo armarte ambas versiones para A/B testing — decime."*

El user confirma o cambia. **Una sola pregunta**, igual que el resto de Decisions.

---

## Anti-patrones

1. **Mezclar modos dentro de una misma secuencia**. Una secuencia = un modo.
2. **Lifestyle sin contexto justificado** ("una persona joven" porque "queda con onda") → AI face garantizado, narrativa débil.
3. **Minimalista con paleta amplia** (5+ hex). Contradice el modo.
4. **Texto blanco en minimalista con fondo claro** → ilegible. Blanco es del modo B.
5. **Modo B sin persona ni contexto** → dejaste de ser B y volviste a A. Sé honesto con el modo.
6. **Forzar modo B en producto de pura forma** (joyería fina, perfume premium, packaging) cuando el cliente no lo pidió. Default minimalista existe por algo.
