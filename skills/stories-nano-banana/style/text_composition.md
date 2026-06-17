# Text Composition — Composición creativa del texto on-image

## Principio

Texto + imagen son **una sola composición**, no dos capas separadas. La posición del texto, su tamaño, la profundidad del fondo y el contraste se diseñan **juntos**. Un texto bien escrito en una posición floja vale lo mismo que un texto débil — el resultado es ilegible o aburrido.

Tu trabajo en el prompt no termina cuando ponés "tercio superior central". Empezás ahí. La pregunta real es: **¿esta story sería distinta si moviera el texto, lo cambiara de tamaño, o blureara el fondo?** Si la respuesta es "no", la composición es perezosa.

Esto es lo que hace que las stories no se sientan a "template de Canva". Variá placement, jugá con tamaños, dirigí tratamientos de imagen para que el texto siempre tenga lugar.

---

## 6 estrategias de placement (elegí una por story, variá entre stories)

### 1. Cabezal — tercio superior central
- **Cuándo**: el producto domina la mitad inferior y necesitás aire arriba para anunciar.
- **Tamaño**: 1/4 a 1/3 del alto del cuadro.
- **Riesgo**: si el avatar de Instagram (0%-14%) tapa el inicio, perdés la primera línea. Línea superior arranca en ~18% mínimo.

### 2. Pie — tercio inferior central
- **Cuándo**: la imagen tiene vacío natural en la parte inferior (mesa limpia, fondo desenfocado) y querés cerrar.
- **Tamaño**: 1/5 a 1/4 del alto.
- **Riesgo**: el input de respuesta (85%-100%) y el sticker de Link chocan acá. Cerrá tu texto antes del 80% como margen.

### 3. Centro vertical sobre producto
- **Cuándo**: la imagen es fondo escénico y el texto es el sujeto principal (hooks fuertes, frases contraintuitivas, números crudos).
- **Tamaño**: 1/3 del alto, peso bold dominante.
- **Requisito**: la imagen detrás necesita **tratamiento** (blur, scrim, grade — ver sección abajo) para que el texto no compita con detalles.

### 4. Desplazado — tercio lateral o esquina
- **Cuándo**: la composición tiene un sujeto fuerte centrado y querés un texto "anotación" que no compita.
- **Tamaño**: 1/6 a 1/5 del alto, peso regular o light.
- **Riesgo**: en 9:16 hay poco ancho — desplazamientos laterales se ven incómodos. Mejor jugar con desplazamiento vertical antes que lateral.

### 5. Wrap / interacción con producto
- **Cuándo**: querés que el texto rodee, "abrace" o se corte detrás del producto. Genera profundidad real (texto entre fondo y producto).
- **Cómo se instruye**: *"texto ubicado de modo que la silueta del producto se superponga parcialmente a la palabra X, dando profundidad de capas"*.
- **Riesgo**: nano banana lo logra cuando el producto es claramente sólido — falla con productos transparentes o con bordes finos.

### 6. Doble peso — palabra clave grande + descriptor chico
- **Cuándo**: el copy tiene un golpe + un complemento (ej: *"Hierro fundido. Sin curado."*, *"Estuvimos en cocinas de **grandes restaurantes**"*).
- **Cómo se instruye**: peso bold + tamaño grande para la palabra clave, peso regular + tamaño 60% para el descriptor, alineados en grilla común (mismo eje x).
- **Riesgo**: si el modelo iguala los pesos, el efecto se cae. Especificá pesos + tamaños relativos explícitos.

---

## 6 tratamientos de imagen para resaltar el texto

Si el fondo natural de la story compite con el texto, **dirigí explícitamente uno de estos tratamientos** en la dimensión 8 del prompt:

### A. Blur de fondo / depth shift
- *"profundidad de campo extrema (f/1.4) con el fondo desenfocado a bokeh suave para abrir respiro detrás del titular"*
- Útil cuando el entorno es rico (cocina llena, escena con muchos elementos).

### B. Scrim / gradiente sutil
- *"un gradiente vertical sutil de transparente a negro 30% en la mitad superior del cuadro, integrado en la luz natural, para asegurar legibilidad del titular blanco"*
- Útil cuando la luz no controla el contraste por sí sola.
- **Cuidado**: si es muy fuerte, parece overlay barato. Mantené 20-35% de opacidad.

### C. Grade que aplana zona del texto
- *"zona donde vive el texto con sombra natural ligeramente oscurecida y reducción de saturación local del 15% para empujar el texto hacia adelante"*
- Más sutil que el scrim. Funciona muy bien en Lifestyle.

### D. Vignette cinematográfico
- *"vignette suave que oscurece bordes superior e inferior un 10%, concentrando atención en el centro del cuadro"*
- Alineado al modo Lifestyle por default.

### E. Letterbox / barra de color sólida
- *"barra de color sólido [hex de la paleta] cubriendo el tercio superior del cuadro, con el titular en el color complementario"*
- Útil en hooks editoriales fuertes. **No abusar** — si lo usás en todas las stories, parece template.

### F. Sin tratamiento — texto pelado sobre imagen
- Cuando la imagen ya tiene suficiente contraste y respiro natural (escena minimalista con pared blanca, cielo plano).
- **Test mental**: si el fondo tiene 80%+ de área monocromática, no necesitás tratamiento.

---

## Reglas de variación entre stories de la misma secuencia

Una secuencia con placement repetido aburre. Una secuencia caótica desarma. El balance:

1. **No repitas el mismo placement en stories consecutivas.** Si story 1 tiene texto en tercio superior, story 2 idealmente lo lleva en tercio inferior o centro.
2. **Si la secuencia tiene 3 stories**: usá 3 placements distintos.
3. **Si tiene 4-6 stories**: podés repetir un placement, pero nunca más de 2 stories iguales y nunca consecutivas.
4. **El CTA (última story) suele ir con texto en tercio superior** dejando el inferior libre para el sticker de Link. **Esta es la única regla rígida.**
5. **Mantené coherente la familia tipográfica + color** entre stories — la variación va en posición y tamaño, no en estilo. (Excepción: en A/B paralelo el color cambia entre Modo A y Modo B según `style/visual_modes.md`.)
6. **Mezclá tratamientos**: si tres stories llevan blur, la cuarta gana variando a scrim o sin tratamiento.

---

## 8 bad examples — anti-patrones a no generar

### ❌ Bad 1 — Placement clonado
Las N stories con texto en tercio superior central, mismo tamaño, mismo color. Parece template de Canva.

### ❌ Bad 2 — Texto flotando random
Texto puesto en una zona arbitraria sin relación con la composición de la imagen. Ejemplo: titular en esquina superior derecha mientras el producto vive abajo a la izquierda. Sin lectura clara.

### ❌ Bad 3 — Contraste inexistente
Texto blanco hueso sobre fondo blanco hueso. Texto negro sobre olla negra sin tratamiento. La regla del modo (color del texto) se aplica **mirando el fondo real de esa zona específica**, no automáticamente.

### ❌ Bad 4 — Texto encima de detalle del producto
Titular cubriendo la marca grabada, la etiqueta o un detalle distintivo. Borra justo lo que lo hace reconocible.

### ❌ Bad 5 — Tamaño sin jerarquía
Todo el copy al mismo tamaño y peso, sin distinción entre golpe y descriptor. Plano y lento de leer. Las stories ganan con jerarquía (Estrategia 6).

### ❌ Bad 6 — Texto en zona tapada por UI
Texto vivo en 0%-14% (avatar, nombre, tiempo) o 85%-100% (input de respuesta, ícono de envío) → tapado en Instagram al subir.

### ❌ Bad 7 — Tratamiento exagerado
Scrim al 70% que mata la imagen. Blur tan fuerte que el producto deja de ser reconocible. El tratamiento **empuja** el texto, no aplasta la imagen. Si tenés que dudar entre fuerte y sutil, sutil siempre.

### ❌ Bad 8 — Texto que rebotó del prompt
El modelo renderizó un texto distinto al pedido. Pasa cuando:
- No entrecomillaste el copy exacto entre comillas dobles.
- Pediste tipografías raras sin describir características.
- Pediste 2+ bloques de texto en la misma story.

Solución: regenerá con copy entre comillas dobles + descripción de fuente por características (no por nombre) + un solo bloque de texto principal por story.

---

## Checklist mental al definir el texto on-image en cada story

Antes de escribir la dimensión 8 del prompt:

- [ ] ¿Qué placement (1-6) elegí y por qué encaja con esta story específica?
- [ ] ¿Es distinto del placement de la story anterior?
- [ ] ¿Hay contraste real entre el texto y el fondo **en esa zona específica del cuadro** (no en promedio)?
- [ ] Si no hay contraste, ¿qué tratamiento (A-F) aplico?
- [ ] ¿El tamaño (fracción del alto) está alineado con la jerarquía (hook = grande, descriptor = chico)?
- [ ] ¿La línea superior arranca después del 18%? ¿La inferior cierra antes del 80%?
- [ ] ¿El sticker de engagement no choca con el texto?
- [ ] ¿La palabra clave queda **fuera del producto** (no tapa marca, etiqueta o detalle clave)?

Si alguna falla, reescribí la dimensión 8 antes de pasar a la siguiente story.
