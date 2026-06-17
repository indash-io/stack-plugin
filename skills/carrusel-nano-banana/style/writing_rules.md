# Style — Writing Rules

Reglas para los **dos tipos de escritura** que produce la skill: el **copy on-image** (texto que va dentro de cada slide) y los **prompts** a nano banana (la parte cinematográfica que pega el user).

`tone_of_voice.md` cubre cómo HABLA la skill con el user. Este archivo cubre cómo ESCRIBE para el output.

---

## Parte A — Reglas para el Copy on-image

### A1. Brevedad
- Máximo **10 palabras por slide**. Idealmente 4-7.
- Si necesitás 12 palabras, replanteá: probablemente estás metiendo dos ideas en un slide.

### A2. Especificidad
- ❌ "Calidad superior" / "Lo mejor del mercado" / "Increíble producto"
- ✅ "12 horas de fragancia" / "10 años de garantía" / "200 unidades disponibles"

Si no podés sostener la afirmación con un hecho concreto, no la escribas.

### A3. Cero emojis
- Salvo que el user lo haya pedido explícitamente.
- Si los pidió: máximo **uno por slide**, y solo cuando aporta semánticamente, nunca decorativo.

### A4. Cero exclamaciones
- Salvo arquetipo Promo, y máximo en uno o dos slides.
- "¡Solo hoy!" puede estar bien en Promo. Nunca en Educativo o Storytelling.

### A5. Verbos en activa
- ✅ "Probalo", "Reservá", "Empezá", "Conseguilo"
- ❌ "Sea probado", "Será reservado", "Se ofrece"

### A6. Estructura paralela en listicles
Si el ítem 1 empieza con sustantivo, los ítems 2 y 3 también. Si empieza con número-punto, todos igual.

✅
> 01 · Liberación gradual de moléculas
> 02 · Base oclusiva de cera
> 03 · Aplicación en piel húmeda

❌ (mezcla estructuras)
> 01 · Liberación gradual de moléculas
> Aplicalo en piel húmeda
> 03 · La cera de candelilla protege

### A7. Datos crudos > adjetivos
Cuando tengas un número, usalo:
- ❌ "Larga duración" → ✅ "12+ horas"
- ❌ "Edición limitada" → ✅ "200 unidades"
- ❌ "Muchos años de experiencia" → ✅ "Desde 1972"
- ❌ "Garantía total" → ✅ "30 días, devolución sin preguntas"

### A8. Sin marketing-speak
Lista de palabras prohibidas en copy on-image (salvo que sean parte del nombre del producto):
- premium, exclusivo, único, incomparable, revolucionario, mágico, transformador
- "Descubrí…", "Conocé…", "Te presentamos…"
- "El mejor", "el más", "lo último en"
- "Calidad superior", "estándares más altos"

Cada una de esas frases tiene un equivalente concreto. Encontralo.

### A9. Idioma del copy
- Default español. Mantenelo en español incluso si la marca usa términos en inglés ocasionales.
- Si el user pide bilingüe → confirmá idioma por slide.

### A10. CTA final accionable
- Verbo + acción concreta. Sin excepción.
- Puede tener dos partes separadas por punto medio: acción · razón/urgencia/fecha.
- Ejemplos válidos:
  - "Probalo 30 días · garantía total"
  - "Reservá el tuyo · 200 unidades"
  - "Comprá hasta el 15 de mayo"
  - "Pedido en link de la bio"

CTAs prohibidos:
- ❌ "Gracias por leer"
- ❌ "Esperamos que te haya gustado"
- ❌ "Compartí con quien te gustaría"
- ❌ "Seguinos para más" (a menos que sea el objetivo del carrusel)

---

## Parte B — Reglas para los Prompts a Nano Banana

Estas reglas complementan el template (`templates/prompt_template.md`) y las leyes (`instructions/05_prompt_engineering.md`).

### B1. Prosa, no listas
Cada prompt es **un solo párrafo narrativo en español**. Sin bullets, sin listas, sin headers internos.

### B2. Oraciones completas
- Sujeto + verbo + objeto. No fragmentos.
- ✅ "Tomado con un lente de 85mm a f/2.0, ángulo levemente contrapicado, composición centrada con espacio negativo arriba."
- ❌ "85mm. f/2.0. Contrapicado. Centrada. Espacio arriba."

### B3. Una palabra precisa > cinco vagas
- ✅ "lujo silencioso"
- ❌ "elegante, sofisticado, premium, atemporal y refinado"

### B4. Anclaje a la imagen primero, siempre
La primera oración del prompt **siempre** referencia la imagen input:
> *"Usá la imagen de producto provista como sujeto exacto — conservá envase, etiquetas, colores y proporciones idénticos —"*

### B5. Nunca describas el producto desde cero
Si referenciaste la imagen, **no describas el producto con palabras**. Solo ubicalo y dirigí su contexto.

❌ "Usá la imagen del producto. Es un frasco alto de vidrio ámbar con tapa dorada y etiqueta serif blanca…"
✅ "Usá la imagen del producto provista como sujeto exacto — y ubicalo sobre un pedestal de mármol gastado…"

### B6. Cero prompts negativos
- ❌ "sin desenfoque, sin gente, sin texto, sin distorsión"
- ✅ describí solo lo que SÍ querés ver

### B7. Vocabulario fotográfico técnico
Usá palabras que el modelo entiende:
- Lentes: 35mm, 50mm, 85mm, 100mm macro
- Aperturas: f/1.8, f/2.0, f/2.8, f/4
- Ángulos: a la altura, cenital, contrapicado, 3/4
- Composición: centrada, regla de tercios, espacio negativo
- Luz: suave/dura, direccional/difusa, cálida 3200K / neutra 5000K / fría 6500K
- Mood: lujo silencioso, calmo, enérgico, sensorial, crudo

### B8. Texto on-image entre comillas
El copy del slide va **siempre entre comillas dobles** dentro del prompt.

✅ *"Renderizá el titular **\"Por qué dura 12+ horas\"** en serif moderna…"*
❌ *"Renderizá un titular que diga algo como Por qué dura mucho…"*

### B9. Cierre técnico obligatorio
Cada prompt termina con:
> *"Relación de aspecto vertical 4:5 (1080x1350, retrato), fotografía editorial de alto detalle, fotorrealista, foco nítido en el producto."*

(Si hay persona, agregá "y en el rostro/manos de la persona".)

### B10. Consistencia entre prompts del carrusel
Los N prompts comparten:
- Misma frase de anclaje a la imagen
- Mismo lente y apertura
- Mismo mood en una palabra
- Misma paleta con mismos hex
- Mismo tratamiento general de luz

Lo que varía: ángulo, escena, composición, presencia/ausencia de persona.

### B11. Personas: las 7 disciplinas
Si el slide incluye persona, aplicá las 7 reglas de `prompt_engineering.md` Ley 6:
1. Edad concreta
2. Textura de piel natural ("poros visibles, sin sobre-suavizado")
3. Expresión específica
4. Pose candid
5. Manos descriptas si están en cuadro
6. Casting realista
7. Iluminación que muestre piel

### B12. Longitud del prompt
- Mínimo: ~80 palabras (si es muy corto, le faltan dimensiones)
- Máximo: ~200 palabras (si es más largo, hay redundancia)
- Sweet spot: 120-160 palabras

---

## Parte C — Reglas para el texto que la skill escribe alrededor del output

### C1. Encabezados en español
- ✅ "Brief creativo", "Slide-by-slide", "Prompts para Nano Banana"
- ❌ "Creative brief", "Slides", "Prompts"

### C2. Sin preámbulo ni cierre conversacional
- Empezá directo con `# Carrusel: [Producto]`.
- Terminá con la línea de "si querés ajustar algo, decime cuál".
- No metas "¡acá tenés!" arriba ni "espero que te sirva!" abajo.

### C3. Notas finales solo si hace falta
Si no hay nada crítico que el user deba saber, no inventes notas. Output más limpio.

---

## Cheatsheet (1 párrafo)

Copy on-image: corto, específico, con datos crudos, sin marketing-speak, sin emojis, verbos en activa, paralelismo en listicles, CTA accionable. Prompts: prosa narrativa en español, anclaje a imagen primero, nunca describir el producto desde cero, vocabulario fotográfico técnico, texto entre comillas, cero prompts negativos, cierre 4:5 obligatorio, personas dirigidas con las 7 disciplinas. Texto del agente: directo, sin emojis, sin exclamaciones, sin AI-speak, encabezados en español.
