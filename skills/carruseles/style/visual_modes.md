# Style — Visual Modes

La skill ofrece **dos modos visuales** para cada carrusel. La skill **siempre propone uno** en Decisions (paso 3) según el producto y la marca, y el user puede confirmar, cambiar al otro, o pedir A/B (ambos paralelos).

**Regla**: un carrusel = un modo. **No mezclar modos entre slides** del mismo carrusel — eso rompe la consistencia. Si querés ambos, generás dos carruseles paralelos (A/B).

---

## Modo A — MINIMALISTA

**Cuándo elegirlo (default)**:
- Producto premium / técnico / packaging fino (perfume, skincare, suplemento, joyería, electrónica)
- Marca con tono editorial, clínico, heritage o industrial honesto
- Cuando la pureza del producto es el argumento principal
- Cuando la URL/imagen muestra estética minimal/editorial

**Producto en escena**: protagonista absoluto. El producto vive solo o con elementos secundarios mínimos (una superficie, un objeto auxiliar). Sin persona, salvo en un slide de demostración puntual.

**Composición**:
- Producto centrado o en regla de tercios, ocupando 40-60% del cuadro
- Fondo neutro liso (negro, blanco, hueso, gris carbón) o superficie material (mármol, cemento, lino, madera cruda)
- Espacio negativo amplio para texto

**Lente**:
- 50mm a f/2.0–2.2 (default)
- 85mm a f/2.0 (si querés compresión y mood editorial premium)
- 100mm macro a f/2.8 (productos pequeños con detalle)

**Iluminación**:
- Softbox de estudio, neutra-fría 5000-5500K
- Suave pero direccional (lateral o cenital)
- Rim light para separar producto del fondo
- Sombras controladas, no dramáticas

**Paleta**:
- Heredada estricta del producto (3-4 colores con hex)
- No agregar colores del entorno

**Tipografía + texto on-image**:
- Heredada del packaging del producto
- **Color del texto**: hex de la paleta, sobre fondo de paleta complementario
- Tamaño moderado (1/4 a 1/5 del alto)
- Peso bold para titulares, regular para subtítulos y datos

**Persona**:
- Por default **no aparece**
- Si aparece (slide de uso), es muy controlada: solo manos o brazos, casting realista (las 7 disciplinas de prompt_engineering aplican siempre)

**Mood típico**:
- *lujo silencioso*, *autoridad técnica*, *pureza disciplinada*, *heritage cálido*, *clínico considerado*, *editorial mineral*

**Estilo visual típico**:
- editorial premium, minimal, clinical, heritage moderno, industrial honesto, escultórico

**Ejemplo en la skill**: el carrusel de una creatina que generamos previamente (4 slides técnicos sobre fondo negro / acero / Purity).

---

## Modo B — LIFESTYLE CINEMATOGRÁFICO

**Cuándo elegirlo**:
- Producto que requiere demostración o contexto de uso (electrodomésticos, ollas/utensilios, herramientas, ropa, cosmética en aplicación, suplementos en rutina, accesorios fitness)
- Marca con storytelling personal, aspiracional o de comunidad
- Cuando el cómo se usa importa más que cómo se ve el producto solo
- Cuando el feed de la marca muestra mucha persona / contexto real

**Producto en escena**: persona real protagonista; el producto puede aparecer como sujeto secundario, en uso, o no aparecer en algunos slides intermedios (slide 1 hook puede ser solo la persona; producto sí debe aparecer en al menos 2 de los N slides).

**Composición**:
- Persona ocupando 50-80% del cuadro (mitad inferior dominante en carrusel 4:5)
- Texto en la mitad superior, grande, dominante
- Fondo lifestyle real (azotea con ciudad, gym minimalista, sala con ventana grande, cocina, exterior natural)

**Lente**:
- **35mm a f/2.8** (default — capta contexto + persona)
- 50mm a f/2.2 (cuando querés persona más cerrada con menos contexto)

**Iluminación**:
- **Cálida, lateral o backlight**, temperatura 3200-3400K
- Golden hour outdoor o luz de ventana grande indoor
- Contraste medio-alto, sombras presentes
- Iluminación que muestra textura de piel (piel natural, no aplanada)

**Paleta**:
- Extendida (5-6 colores): hereda del producto + suma 1-2 del entorno (skyline azul, madera cálida del gym, etc.)
- Permite acentos del contexto sin perder coherencia con la marca

**Tipografía + texto on-image**:
- Sans-serif geométrica humanista bold (estilo Hanken Grotesk, Söhne, GT Walsheim)
- **Color del texto: blanco hueso #ECE7DC** (default) sobre áreas oscuras/medias de la imagen
- Tamaño grande dominante (titular ocupa 25-35% del alto del cuadro)
- Jerarquía clara: titular bold gigante + subtítulo regular más chico

**Elementos gráficos de marca digital** (opcionales pero característicos):
- **Pills** (cápsulas redondeadas con borde fino blanco): para CTAs secundarios, badges, items de listicle, subtítulos contenidos
- **Brand mark** (logo o símbolo) anclando arriba o abajo del cuadro como elemento de marca
- **Íconos lineales blancos** dentro de pills (en slides de listicle, para íconos de cada ítem)
- **Flechas** ("→") para indicar continuidad o CTA

**Persona**:
- **Casi siempre aparece** (en slide 1 hook, en slides de demostración, etc.)
- Casting real, las 7 disciplinas de prompt_engineering siempre obligatorias
- Edad concreta, textura de piel natural visible, expresión específica, pose candid, manos descriptas
- Looks reales: ropa deportiva auténtica, looks casuales, no de catálogo

**Mood típico**:
- *aspiracional pero cercano*, *energía cálida*, *intensidad de oficio*, *ritual matinal*, *cotidiano premium*, *humano y honesto*

**Estilo visual típico**:
- documental cinematográfico, lifestyle editorial, oficio en acción, brand digital moderno

**Ejemplo en la skill**: las refs de una marca de suplementos sobre energía/hábitos que el user pasó (mujer con pelo al viento en azotea + hombre fatigado en gym + mujer haciendo yoga junto a ventana, todas con texto blanco grande, pills, brand mark asterisco/logo).

---

## Cómo elegir el modo (lógica para Decisions)

| Si el producto / marca… | Modo sugerido |
|---|---|
| Premium con packaging fino y tipografía importante | **Minimalista** |
| Marca con storytelling fuerte, comunidad, aspiracional | **Lifestyle** |
| Categoría que se vende por demostración (cocina, fitness, beauty in-use) | **Lifestyle** |
| Categoría editorial (perfume, joyería, vino, accesorios premium) | **Minimalista** |
| Marca cuyo feed actual ya tiene mucho lifestyle | **Lifestyle** |
| Marca cuyo feed actual es minimal/editorial | **Minimalista** |
| Producto sin contexto de uso obvio | **Minimalista** |
| Producto con persona como parte del valor (cosmética aplicada, fitness wear) | **Lifestyle** |

**Si dudás → default = Minimalista** (es más controlable, más rápido de generar y casi siempre aceptable). Pero en la pregunta consolidada de Decisions, agregá: *"si querés también la versión Lifestyle para A/B, avisame"*.

---

## A/B paralelo (ambos modos)

El user puede pedir explícitamente que generes **ambos modos** para A/B testing.

**Cuándo ofrecerlo proactivamente**:
- Producto que claramente puede vivir en los dos mundos (suplemento que es premium pero también lifestyle, perfume que es editorial pero tiene momento de uso)
- Cuando el user pidió "hace dos versiones" o "no estoy seguro qué prefiere la marca"
- Cuando es el primer carrusel de una marca y vale tener ambos para testear

**Cómo se entrega A/B** (detalle completo en `instructions/06_output_format.md`):
- Dos secuencias paralelas, **mismo copy on-image, misma narrativa, mismo hook y CTA**
- Solo varían: modo visual, lente, mood, luz, persona, paleta, color del texto, escena
- Output con bloques separados claros: "Carrusel A · Minimalista" y "Carrusel B · Lifestyle"

**Regla A/B**: nunca cambies el copy entre A y B. Eso rompe la comparación. La diferencia está en lo visual, no en el mensaje.

---

## Reglas duras transversales a los dos modos

1. **Un modo por carrusel**. Sin excepción.
2. **El producto debe ser reconocible** en al menos 2 de los N slides (en Minimalista en todos, en Lifestyle en al menos los slides de hook y CTA).
3. **Las 7 disciplinas para personas** aplican siempre que haya persona, en cualquiera de los dos modos.
4. **Aspect ratio 4:5 (1080x1350)** en cualquiera de los dos modos.
5. **Paleta y tipografía heredadas del producto** — el modo Lifestyle puede sumar entorno, pero la base es del producto.
6. **Self-check** (`eval/quality_checklist.md`) corre igual en ambos modos.
7. **Variación de composición obligatoria entre slides** (ver matriz abajo). No todos los textos en la misma zona.

---

## Matriz de composición y posición del texto entre slides

**Regla crítica**: **el texto on-image NO puede estar siempre en la misma zona del cuadro entre slides**. Eso genera carruseles predecibles, planos y sin ritmo. Un creativo real **varía la posición y el tratamiento del texto** según la función del slide.

### Matriz por función de slide

| Slide | Función | Posición sugerida del texto | Tratamiento de imagen | Por qué |
|---|---|---|---|---|
| 1 | Hook | **Texto grande arriba o centro vertical**, dominante | Imagen nítida, producto/persona protagonista | Atrapa la atención inicial. El brand mark puede acompañar arriba. |
| 2 | Argumento / Diferencial | **Texto arriba alineado a la izquierda o centrado**, con bullets/pills abajo o al lado | Imagen nítida, contexto explicativo | Mantiene legibilidad sin repetir la composición del hook. |
| Intermedio (3+) | Concepto / Prueba / Detalle | **Texto al medio sobre imagen con leve blur cinematográfico** o **texto pequeño abajo** | Imagen levemente desenfocada para dar peso al texto, o macro detalle | Variación visual fuerte. Da peso al concepto. |
| Penúltimo | Bullet list / desglose | **Texto distribuido**: titular arriba + bullets en el medio o abajo | Imagen como soporte, no protagonista | Aprovecha el espacio. Cambio respecto a slides previos. |
| Último (CTA) | Acción | **CTA abajo**, producto al medio o arriba | Imagen frontal limpia para máxima legibilidad | El ojo termina la lectura abajo. El CTA queda en la zona de "siguiente paso". |

### Variaciones extra que un creativo aplicaría

Usá estas técnicas cuando aporten — no todas en cada carrusel, pero **al menos 1 o 2 en algún slide intermedio**:

- **Texto al medio sobre imagen levemente desenfocada** (blur cinematográfico sutil) → da peso a la palabra clave, perfecto para slides intermedios o de "concepto".
- **Texto en columna lateral** → cuando la imagen tiene un sujeto desplazado a un lado, dejá el espacio negativo del otro lado para texto vertical.
- **Tipografía gigante** que ocupa 50%+ del cuadro → cuando el texto es el protagonista del slide (hook contundente o slide de afirmación).
- **Texto en negativo natural** (texto blanco sobre área oscura natural de la imagen, sin pill) → más editorial.
- **Jerarquía cambiante**: un slide con texto enorme + sub pequeño, otro slide solo texto medio sin sub.
- **Asimetría intencional**: no todos centrados horizontalmente. Texto alineado a la izquierda en uno, centrado en otro, derecha en otro.
- **Tratamiento de imagen distinto entre slides**: nítido en hook, blur cinematográfico en intermedio, frontal limpio en CTA.

### Reglas duras de variación

1. **Si el carrusel tiene 4+ slides con texto, al menos 2 deben usar posiciones distintas** entre sí (no todos arriba, no todos abajo).
2. **El último slide (CTA) debe tener una composición distinta del primer slide (Hook)** — diferencia clara entre apertura y cierre.
3. **Si un slide va a llevar imagen con blur cinematográfico**, el texto vive en el centro vertical o en una zona de máximo contraste.
4. **El producto debe quedar reconocible en cualquier composición** — la variación es del texto y la composición, no del producto.

### Ejemplo de variación bien aplicada (carrusel Lifestyle de creatina, 4 slides)

> Slide 1 (Hook): titular GRANDE en tercio superior central, brand mark arriba, persona en mitad inferior. Imagen nítida.
>
> Slide 2 (Diferencial): titular en tercio superior izquierdo (alineado a la izquierda), bullets en pills horizontales en el tercio inferior. Composición asimétrica.
>
> Slide 3 (Performance): titular en CENTRO VERTICAL EXACTO sobre la imagen del atleta con leve desenfoque cinematográfico. Tipografía grande (1/3 del alto). Imagen al servicio del texto.
>
> Slide 4 (CTA): titular compacto arriba, producto en el centro, **CTA en pill grande sólida en el tercio inferior central**. Composición de cierre invertida respecto al hook.

Cada slide se siente distinto pero coherente. El ojo encuentra novedad. El carrusel respira.
