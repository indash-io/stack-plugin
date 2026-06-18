# Ejemplos MALOS — Qué NO hacer

Este archivo entrena el **criterio negativo**: cómo se ve un output mal hecho y por qué falla. Si la skill se encuentra produciendo algo similar, frená y reescribí.

---

## MALO #1 — Keyword soup (estilo Midjourney)

**Prompt malo**:

```
perfume bottle, amber glass, marble pedestal, golden hour, mediterranean, 85mm, f/2.0, editorial, luxury, warm tones, cinematic, photorealistic, 8k, masterpiece, hyperdetailed, professional photography, beautiful lighting, vibrant
```

**Por qué falla**:
1. Lista de keywords pegoteada — nano banana fue entrenado con captions narrativos, no con strings de keywords. Degrada el resultado.
2. Adjetivos vagos apilados ("luxury, warm, cinematic, beautiful") — ninguno aporta dirección concreta.
3. Sin anclaje a la imagen de referencia — el modelo va a generar un perfume genérico, no el del usuario.
4. Sin texto on-image especificado — ¿qué dice el slide?
5. "8k, masterpiece" — vocabulario aprendido de Midjourney que en nano banana no aporta.
6. Sin paleta heredada con hex.
7. Sin aspect ratio.

**Cómo se hace bien**: ver `examples/good/listicle_cocina.md` — slide 1.

---

## MALO #2 — Doble descripción del producto

**Prompt malo**:

```
Usá la imagen del producto provisto. El producto es un frasco alto de vidrio ámbar con tapa dorada metalizada y etiqueta blanca con tipografía serif. Mide aproximadamente 12cm de alto. Ubicalo sobre un pedestal de mármol blanco italiano...
```

**Por qué falla**:
1. Después de referenciar la imagen, **describe el producto con palabras**. La descripción compite con la referencia y el modelo termina alterando el frasco (cambia altura, cambia matiz del ámbar, cambia tipografía).
2. Detalles del producto ("12cm de alto", "tapa metalizada") son innecesarios — la imagen los aporta.
3. Resultado: el producto sale **distinto** entre slides porque cada prompt lo redescribe levemente diferente.

**Regla rota**: B5 — Nunca describas el producto desde cero. Solo ubicalo y dirigí su contexto.

**Cómo se hace bien**:
> *"Usá la imagen de producto provista como sujeto exacto — conservá envase, etiquetas, colores y proporciones idénticos — y ubicá el frasco sobre un pedestal de mármol blanco italiano…"*

---

## MALO #3 — Copy on-image vago / marketing-speak

**Slides malos**:

| # | Copy malo |
|---|---|
| 1 | "Descubrí la diferencia" |
| 2 | "Calidad superior, ingredientes premium" |
| 3 | "Resultados que se notan" |
| 4 | "Sumate a la familia" |

**Por qué falla**:
1. Slide 1: "Descubrí la diferencia" — ¿qué diferencia? No detiene el scroll, no genera curiosidad. Genérico.
2. Slide 2: "Calidad superior, ingredientes premium" — palabras prohibidas (premium, superior). Ninguna se puede sostener con un hecho.
3. Slide 3: "Resultados que se notan" — ¿qué resultados? ¿en cuánto tiempo? ¿en qué? Cero especificidad.
4. Slide 4: "Sumate a la familia" — CTA poético, no accionable. ¿Qué hago? ¿Comprar? ¿Seguir? ¿Suscribirme? Sin verbo concreto.

**Cómo se hace bien**:

| # | Copy bueno |
|---|---|
| 1 | "Por qué dura 12+ horas" |
| 2 | "01 · Liberación gradual de moléculas" |
| 3 | "Probado en 200 personas · 89% notó cambio en 6 semanas" |
| 4 | "Probalo 30 días · garantía total" |

**Regla rota**: A2 (especificidad), A8 (sin marketing-speak), A10 (CTA accionable).

---

## MALO #4 — Persona genérica "AI face"

**Prompt malo (fragmento)**:

```
Una mujer joven y hermosa con piel perfecta sosteniendo el producto, sonriendo a la cámara, fondo borroso, look profesional.
```

**Por qué falla**:
1. **"Joven y hermosa"** → modelo genera la cara IA estándar (simétrica, sobre-suavizada, vacía).
2. **"Piel perfecta"** → activa el sobre-suavizado plástico que delata el AI face.
3. **"Sonriendo"** → expresión genérica e inespecífica → sonrisa de catálogo.
4. **"Sosteniendo el producto"** → sin describir las manos → manos deformadas, dedos extra.
5. **"Fondo borroso"** → vago. ¿Qué tipo de fondo? ¿Qué luz?
6. **"Look profesional"** → palabra vacía.

**Cómo se hace bien**:
> *"Una persona real, mujer de 38 años de fenotipo latino, con textura de piel natural visible (poros, leves líneas finas bajo los ojos, asimetrías humanas, sin sobre-suavizado), pelo castaño oscuro a la altura de los hombros recogido suelto en un rodete bajo, vistiendo una camisa de lino blanco sin estructurar. Aplicando una pequeña cantidad de crema con el dedo medio de la mano derecha sobre su pómulo derecho, dedos relajados y visibles claramente. Expresión: concentración serena, mirándose en un espejo fuera de cuadro, ojos entrecerrados naturalmente. Captura espontánea, momento candid, no posada."*

**Regla rota**: B11 (las 7 disciplinas para personas).

---

## MALO #5 — Prompt negativo embebido

**Prompt malo (fragmento)**:

```
... iluminado por luz natural, sin gente en la escena, sin desenfoque excesivo, sin texto adicional, sin marcas de agua, sin distorsión, sin manos visibles, fondo limpio sin elementos distractores...
```

**Por qué falla**:
1. Nano banana **no procesa bien prompts negativos**. Tiende a generar exactamente lo que pediste evitar (la palabra activa el concepto).
2. Resultado típico: aparece gente, aparece texto extra, aparecen elementos en el fondo.
3. Lista larga de "sin X, sin Y, sin Z" parece ordenada pero está saboteando el output.

**Cómo se hace bien**:
> *"... iluminado por luz natural difusa, escena de producto en foco único, fondo de mármol travertino limpio sin otros objetos en cuadro."*

(Describí lo que SÍ querés ver, no lo que NO.)

**Regla rota**: B6 (cero prompts negativos).

---

## MALO #6 — Workflow saltado: generar sin confirmar

**Conversación mala**:

```
User: Carrusel para [URL] con esta imagen [imagen].
Skill: ¡Genial! Acá tenés tu carrusel de 5 slides...
[entrega los prompts directo]
```

**Por qué falla**:
1. Salta el paso 3 (Decisions). El user no confirmó tipo, slides, hook, mood.
2. La skill decidió todo sola sin propuesta visible. Si algo está mal, el user tiene que pedir cambios sobre algo ya hecho — pérdida de tiempo y tokens.
3. **Regla no-negociable rota**: siempre se confirma antes de generar.

**Cómo se hace bien**:
- Recibe URL + imagen → silencio (Discovery) → pregunta consolidada con propuestas → user confirma/edita → genera.

---

## MALO #7 — Inconsistencia entre slides

**Síntoma**: el mismo carrusel tiene:
- Slide 1: lente 85mm, luz cálida, mood lujo silencioso, paleta neutros cálidos.
- Slide 2: lente 35mm, luz fría, mood enérgico, paleta saturada.
- Slide 3: vuelta a 85mm, otra paleta más.

**Por qué falla**: parece tres carruseles distintos pegados, no uno solo. El user lo posta y se ve incoherente en el feed.

**Regla rota**: B10 (consistencia entre prompts) + ley 7 de prompt_engineering.

**Cómo se hace bien**: lente, mood, paleta y luz general son **iguales** en todos los slides. Lo que cambia es ángulo + escena + composición.

---

## MALO #8 — Texto on-image sin dirección

**Prompt malo (fragmento)**:

```
... con un titular llamativo en la parte superior que diga algo sobre la duración del producto, en una tipografía moderna...
```

**Por qué falla**:
1. **"Algo sobre la duración"** → el modelo inventa el copy, sale "Long Lasting Effect" o cualquier cosa.
2. **"Tipografía moderna"** → vago, fallback random.
3. **"Llamativo"** → no es una dirección, es un adjetivo vacío.
4. Sin color, sin posición exacta, sin tamaño relativo.

**Cómo se hace bien**:
> *"Renderizá el titular "Por qué dura 12+ horas" en serif moderna de alto contraste (coincidente con la tipografía de la etiqueta), peso regular, en color ámbar profundo #6B3410, ubicado en la zona superior del cuadro, ocupando aproximadamente 1/4 del espacio vertical, con espacio negativo generoso debajo separando el titular del producto."*

**Regla rota**: B8 (texto entre comillas + dirección completa).

---

## MALO #9 — Texto siempre en la misma posición entre slides

**Síntoma**: el carrusel tiene texto on-image en los N slides, pero **todos los textos están en la misma zona del cuadro** (típicamente "tercio superior central"). Cuando ves los N slides en secuencia, se sienten predecibles, planos y sin ritmo.

**Caso real observado** (carrusel Lifestyle de Creatina VITS, primera versión):

| Slide | Posición del texto | Sensación al ver el carrusel |
|---|---|---|
| 1 (Hook) | Tercio superior central | OK individualmente |
| 2 (Diferencial) | Tercio superior central | Repite el slide 1 |
| 3 (Performance) | Tercio superior central | Predecible |
| 4 (CTA) | Tercio superior central | Sin variación, sin clímax |

**Por qué falla**:
1. **Falta de ritmo visual**: un carrusel se consume en secuencia. Si las 4 composiciones son iguales, el ojo del usuario no encuentra novedad y deja de mirar.
2. **No usa la función del slide**: cada slide tiene una función distinta (hook, desarrollo, CTA). La composición debe acompañar la función. Un CTA con texto arriba es contraintuitivo — el ojo termina abajo, no arriba.
3. **Predecibilidad**: la tipografía + posición igual en cada slide se siente templete, no diseño curado.
4. **No aprovecha el medio**: un carrusel permite movimiento, contraste, tratamiento de imagen distinto entre slides. Un creativo real cambia el peso visual entre slides.

**Cómo se hace bien — variación de posición del texto por función**:

| Slide | Función | Posición sugerida del texto | Por qué |
|---|---|---|---|
| 1 | Hook | **Texto grande arriba o centro vertical**, dominante | Atrapa la atención inicial. Puede llevar brand mark arriba. |
| 2 | Desarrollo / Argumento | **Texto arriba** o **lateral con espacio** | Mantiene legibilidad sin repetir el hook. |
| Intermedios | Detalle / prueba | **Texto al medio sobre imagen con leve blur** o **texto pequeño abajo** | Da peso al concepto. Imagen menos protagonista. Variación visual fuerte. |
| Penúltimo | Bullet list / desglose | **Texto distribuido**: titular arriba + bullets en el medio o abajo | Aprovecha el espacio. Cambio respecto a slides previos. |
| Último (CTA) | Acción | **CTA abajo**, producto al medio o arriba | El ojo termina la lectura abajo. El CTA queda en la zona de "siguiente paso". |

**Variaciones extra que un creativo aplicaría** (úsalas cuando aporten):
- **Texto al medio sobre imagen levemente desenfocada** (blur sutil) → da peso a la palabra, perfecto para slides de "concepto" o intermedios.
- **Texto en columna lateral** → cuando la imagen tiene un sujeto desplazado a un lado.
- **Tipografía gigante** que ocupa 50%+ del cuadro → cuando el texto es el protagonista del slide (hook contundente).
- **Texto en negativo** (texto blanco sobre área oscura natural de la imagen) en lugar de pill → más editorial.
- **Jerarquía cambiante**: un slide texto enorme + sub pequeño, otro slide solo texto medio sin sub.
- **Asimetría intencional**: no todos centrados horizontalmente. Texto alineado a la izquierda en uno, centrado en otro, derecha en otro.

**Cómo aplicarlo en el prompt** (ejemplo de variación entre los 4 slides de un carrusel):

> Slide 1: *"...titular 'Rendimiento sin margen de error' en peso bold, blanco hueso #F5F1E9, ubicado en el **tercio superior central**, ocupando 1/4 del alto..."*
>
> Slide 2: *"...titular 'Pureza comprobada por terceros' alineado a la izquierda en el **tercio superior izquierdo**, con las pills en el tercio inferior izquierdo..."*
>
> Slide 3: *"...titular 'Energía y desempeño' centrado en el **centro vertical exacto** del cuadro, sobre la imagen del atleta con leve desenfoque cinematográfico que da peso al texto, en tipografía grande ocupando 1/3 del alto..."*
>
> Slide 4: *"...titular 'Suplementación inteligente para atletas conscientes' compacto en el **tercio superior derecho**, y la pill de CTA con 'vitsnutricion.com →' en el **tercio inferior central** ocupando una zona de máxima legibilidad..."*

**Regla rota**: principio de **variación creativa entre slides** (matriz nueva en `style/visual_modes.md`).

---

## MALO #10 — Mostrar un ángulo del producto sin tener imagen de referencia de ese ángulo

**Síntoma**: el concept propone un slide que muestra el producto desde una vista distinta (espalda, lateral, interior, detalle específico), pero la skill **NO le pidió al user la imagen de referencia de esa vista**. El prompt referencia "la imagen del producto" genérica, nano banana usa la frontal y **inventa** la espalda/lateral/interior. Resultado: el detalle sale incorrecto o ausente, el carrusel pierde credibilidad.

**Caso real observado** (carrusel del Chaleco Baccaris Vesna):

| Slide | Vista propuesta | Referencia disponible | Resultado |
|---|---|---|---|
| 1 (Hook) | Frente, modelo cuerpo entero | ✅ Imagen frontal | OK |
| 2 (Detalle tachas) | Frente macro pecho | ✅ Imagen frontal con tachas | OK |
| 3 (Detalle corte) | Frente plano medio 3/4 | ✅ Imagen frontal | OK |
| 4 (Detalle calidad) | Chaleco colgado mostrando interior | ⚠️ Sin referencia explícita | Riesgoso |
| 5 (CTA) | **Espalda con detalle de tachas en cuello posterior** | ❌ **No pedida** | **Salió mal** — nano banana inventó el detalle posterior |

**Por qué falla**:
1. Nano banana es **excelente respetando la imagen de referencia** que le pasás. Es su superpoder. Pero **solo respeta lo que ve** — si le pedís un ángulo que no está en la imagen, lo inventa.
2. En apparel especialmente: la espalda, el lateral, el interior y los detalles macro son **tan distintos como un producto diferente**. Una marca puede tener un patrón de tachas en el cuello posterior que es la mitad o un cuarto del frontal. Sin referencia, nano banana asume "más de lo mismo".
3. En suplementos/packaging: la información nutricional del dorso, el cierre lateral, los ingredientes interiores — son zonas con tipografía y diseño propios. Inventarlos quema la confianza del consumidor.
4. La skill prometió "el producto es reconocible y consistente" — eso solo se cumple si la skill tiene referencia de cada ángulo que muestra.

**Cómo se hace bien — protocolo de validación de referencias**:

En el **paso de Concept (paso 4)**, la skill debe armar una matriz como esta antes de generar prompts:

| Slide | Vista del producto | ¿Tengo imagen de referencia de esa vista? |
|---|---|---|
| 1 | Frente | ✅ Sí |
| 2 | Frente macro | ✅ Sí (zoom de la misma) |
| 3 | Frente 3/4 | ⚠️ Aproximada (puedo derivar del frente) |
| 4 | Interior / forrería | ❌ No → **PEDIR** |
| 5 | Espalda | ❌ No → **PEDIR** |

**Si hay cualquier ❌ → la skill debe parar, pedir las imágenes faltantes al user, y solo avanzar cuando estén todas.** No avanzar y "que el modelo se las arregle".

**Mensaje sugerido al user cuando faltan referencias**:

> Para el slide N (vista de espalda) y slide M (interior con forrería) necesito imágenes de referencia adicionales — sin esas, nano banana va a inventar esos ángulos y van a salir mal. ¿Me las podés compartir? Si solo tenés la frontal, lo replanteamos: o cambiamos el ángulo de esos slides a algo que sí tengamos en la imagen frontal, o reducimos el carrusel a N-2 slides.

**Reglas duras**:

1. **Un ángulo del producto = una imagen de referencia.** Sin excepción.
2. La skill **NO genera prompts de un slide sin tener la referencia del ángulo que muestra**.
3. Si el user solo tiene la frontal y el concept propone mostrar otros ángulos, la skill **propone alternativas** (cambiar de ángulo, sacar el slide, cerrar con macro de un detalle frontal en lugar de espalda).
4. Detalles ambiguos (forrería interior, costuras internas, tipografía en el dorso, detalle del lateral, vista superior/cenital del envase) **siempre** requieren referencia explícita.
5. Si la skill propone un slide con un ángulo nuevo, **lo señala explícitamente en la pregunta consolidada de Decisions** y pide las imágenes ahí, no después de generar.

**Regla rota**: principio de **anclaje a referencia real** + nuevo protocolo de validación de imágenes.

---

## Resumen de errores recurrentes

1. ❌ Keyword soup en lugar de prosa.
2. ❌ Doble descripción del producto (referencia + texto).
3. ❌ Copy genérico, marketing-speak, CTAs poéticos.
4. ❌ Personas sin las 7 disciplinas.
5. ❌ Prompts negativos.
6. ❌ Saltarse el paso de confirmación.
7. ❌ Inconsistencia entre slides.
8. ❌ Texto on-image sin dirección quirúrgica.
9. ❌ Texto siempre en la misma posición entre slides — falta de ritmo visual.
10. ❌ **Mostrar un ángulo del producto sin tener imagen de referencia de ese ángulo** — nano banana inventa y sale mal.

Si tu output cae en cualquiera de estos → frená y reescribí esa parte. No entregues.
