---
name: ugc-generator
description: Proceso estándar end-to-end para producir videos UGC para un cliente — desde el pedido hasta los clips verificados en carpeta, generando con el MCP de Indash. Usá esta skill SIEMPRE que haya que producir contenido de video para un cliente, sin importar cómo llegue el pedido — una frase por chat ("hacele un UGC a <cliente> con este producto"), un sheet/template de pedidos, un brief, un audio transcripto, o "seguí con los videos de X". También para onboardear un cliente nuevo de UGC, cargar sus productos al workspace, o crear/actualizar su ficha de marca. Si el usuario menciona avatares, clips, guiones de video, videos de 10 o 20 segundos, o un cliente + producto + video en la misma frase, es esta skill. Para la redacción fina de prompts de modelos (Kling/Veo/Seedance/Nano Banana) usa ugc-video-prompts; esta skill es el proceso que la contiene.
language: es
---

# UGC Generator — Estándar de producción

Sos el productor responsable de que cada video salga igual de bien sin importar
quién lo produce ni cómo llegó el pedido. El proceso: toma de contexto, 7 pasos,
2 gates de aprobación, 1 QA bloqueante. Si un paso falla, se dice y se resuelve
antes de seguir — nunca se maquilla.

## Toma de contexto (SIEMPRE primero, antes de responder nada)

El valor de esta skill es que "ya entiende" cuando el usuario tira una frase.
Eso se logra leyendo, en este orden, lo que ya existe:

1. **Ficha de marca** → `ficha-marca.md` en la carpeta local del cliente. Tiene
   workspace_id, tono, tope de contenido, avatares aprobados, qué modelo
   funciona y qué rebota en filtros. Si no existe, crearla desde
   `templates/ficha-marca-template.md` es parte del primer pedido (los datos
   salen del sitio del cliente + 2-3 preguntas al usuario).
2. **Carpeta local del cliente** (default `~/Desktop/Clientes/<Cliente>/`; si
   no existe en esta máquina, preguntar UNA vez dónde guarda el trabajo el que
   produce y usar esa): los SCRIPTS.md
   de videos anteriores son la memoria de qué se decidió y por qué. Leer el más
   reciente alcanza para agarrar el estilo. Si la carpeta la creó la skill
   `new-client`, su `CLAUDE.md` de marca también es contexto — no lo repitas
   en la ficha, referencialo.
3. **Productos del workspace** (`list_products` con el workspace_id de la ficha):
   qué ya está cargado, con qué fotos.

Con esas tres lecturas, un pedido de una línea alcanza para producir. No le
pidas al usuario contexto que ya está escrito en alguno de esos tres lugares.

## El pedido puede llegar en cualquier formato

Una fila de sheet, una frase por chat, un audio, un brief pegado. Da igual: de
cualquier entrada se extraen los mismos campos, y lo que falte lo tapan los
defaults. El template (`templates/template-pedidos.md`) es una forma cómoda de
pedir en tandas — no un requisito. Nunca le digas al usuario "llename el
template" si ya te dio la información hablando.

Campos a extraer de cualquier entrada, con su default si no vienen:

| Campo | Default si falta |
|---|---|
| Producto | — (único obligatorio; si viene el nombre, buscar la URL real) |
| Ángulo / tema | proponerlo desde los beneficios del producto |
| No negociables | ninguno |
| Duración/formato | **corto: 2 videos de 10s por producto** (ver Formatos) |
| Formato | 9:16 |
| Escenario | el de la ficha de marca; si no hay, estudio de podcast |
| Tono | el de la ficha de marca |
| Cómo mostrar el producto | visible + mencionado |
| Avatar | el aprobado en la ficha para ese tipo de video |
| Idioma | español rioplatense |
| Modelo de video | el de la ficha; si no hay, Omni |

Todo default aplicado se registra en el SCRIPTS.md como "asumido, no pedido" —
así, si el cliente esperaba otra cosa, se sabe qué fue supuesto y qué fue pedido.
Si falta algo que ningún default resuelve, preguntá UNA vez, todo junto.

---

## Los dos formatos

**Formato corto (default): por producto se arman 2 VIDEOS de 10 segundos, un
solo clip cada uno.** Cada video es autocontenido: abre con hook (primeros 2
segundos) y cierra con CTA imperativo, todo adentro del mismo clip.
**28-32 palabras por video** — ese es el rango bueno; ~34 es el techo absoluto.
Sin frame B, sin racord entre clips: un frame → un clip → un video. Mitad de
costo y de puntos de falla que el formato largo. Los 2 videos del producto
llevan avatar y escena DISTINTOS y hooks bien diferentes entre sí (si arrancan
parecido, el feed los lee como serie fabricada).

**Formato largo (a pedido): 1 video de 20s = 2 clips de 10s** (clip A hook,
clip B CTA), misma escena con cambio de ángulo entre frames (multicámara) y
racord estricto. Usarlo cuando el pedido lo pide explícito o el guion no entra
en 10s. Todo lo del proceso aplica igual; los pasos de frame B y racord solo
existen en este formato.

## Vale para cualquier categoría de producto

El proceso es agnóstico: ya corrió con calzado, juguetes íntimos, bazar, comida
y cosmética. Lo específico de cada rubro vive en la ficha de marca, no acá. Lo
que cambia por categoría es qué regla pesa más:

- **Producto con marca/etiqueta impresa** (termos, packaging, cosmética): el
  dictado letra por letra + QA de texto con zoom pasan a ser la regla #1, y si
  la tipografía es chica el producto va APOYADO y quieto — la mano lo señala,
  no lo levanta (el texto se degrada en movimiento).
- **Producto voluminoso** (plataformas, botellones, cajas): la escala dictada
  es la regla #1.
- **Categoría sensible** (íntimo, bebidas, salud): los filtros del generador
  rebotan por la IMAGEN, no por el guion — mostrar la caja resuelve; el tope
  de contenido lo fija la ficha de marca.
- Los hooks y CTAs de `style/guiones.md` son fórmulas de personas, no de rubro:
  funcionan igual para un termo que para una sandalia.

## El proceso

### Paso 0 — Producto cargado en Indash

Todo producto que aparezca en un video existe primero en el workspace con nombre
real, URL, precio, descripción con beneficios y **fotos reales**. ¿Por qué
primero? Porque la foto real es la referencia obligatoria para generar, la
fuente de los beneficios para el guion, y el contra qué se hace el QA. Sin esto
cargado, todo lo demás se hace peor.

- Validar contra el sitio real del cliente, no contra nombres del workspace.
- Mirar la foto ANTES de generar: qué packaging tiene, qué textos lleva
  impresos, qué proporciones tiene. (Las descripciones de los sitios mienten:
  hubo una ficha que decía "paleta" y la foto mostraba un látigo.)
- **Cliente sin sitio web** (vende por Instagram/WhatsApp/ML): el paso no se
  saltea, cambia la fuente — pedir fotos reales al usuario o bajarlas del IG
  del cliente y subirlas (`add_product_images` acepta base64). Lo innegociable
  es que exista una foto real en el workspace.

### Paso 1 — Entender el pedido

Releer la entrada textual (no de memoria — las palabras exactas del cliente
importan: "que se presente como alternativa a X" es un posicionamiento, no una
sugerencia). Extraer los campos de la tabla y listar los no negociables.

### Paso 2 — Checkpoint

Aplicar defaults a lo que falte. Preguntar solo lo que ningún default resuelve,
una vez, todo junto.

### Paso 3 — Scripts → GATE 1

- **Formato corto: un video = UN clip** (hook y CTA adentro del mismo).
  **Formato largo: un video = exactamente 2 clips.** Nunca 3: el tercer corte
  rompe el formato UGC y suma una costura que el feed nota. Si el pedido tiene más momentos
  (travelling, plano producto, remate), van adentro de uno de los dos clips.
- Duración partida en 2, tope 10s por clip (límite de Omni): 20s → 10+10 ·
  15s → 8+7 · 12s → 6+6.
- **Más de 20s no entra en 2 clips.** Opciones a plantear en este gate:
  (a) recortar a 20s — casi siempre el guion mejora; (b) partir en DOS videos
  de 2 clips, cada uno con su hook y CTA; (c) modelo de clip largo
  (kling/seedance, 15s/clip) solo si la ficha de marca lo permite.
- **Palabras por clip: 10s → 28-32 (apuntar a 32) · 8s → ~27 · 7s → ~24.**
  Techo absoluto ~34: más que eso suena apurado y el lip-sync se degrada.
  Escribir el conteo junto a cada script, siempre.
- Hook y CTA son innegociables en TODOS los formatos: en corto conviven en el
  clip único (hook primeros 2s, CTA imperativo al final); en largo, clip A abre
  con el **hook** y clip B cierra con el **CTA** (+precio si aplica).
- **Antes de escribir un solo guion, leer `style/guiones.md`**: los
  dos registros (orgánico/genuino vs descriptivo/beneficios), el catálogo de
  12 hooks y 7 CTAs con ejemplos reales entregados, y las reglas de lenguaje.
  En tandas, alternar registros — nunca dos hooks parecidos al mismo cliente.
- Claims verificables solamente: nada de "la más alta", "te duran años" ni
  colores/variantes sin confirmar contra fotos o ficha. Urgencia blanda sí
  ("antes de que vuelen"), stock/ofertas inventadas no.
- **Pareja = un hablante por clip.** Dos personas alternando diálogo en un
  mismo clip rompe el lip-sync (el modelo les mueve la boca a los dos). El que
  escucha va con boca cerrada, explícito en el prompt. El corte entre clips es
  el cambio de turno, como un podcast real editado.
- Guion y frame se diseñan juntos: no escribir "este:" o "mirá esto" si el
  frame no va a tener el producto en mano.
- **Nombres de marca/producto: detectar el riesgo de pronunciación ACÁ.**
  El guion SIEMPRE se escribe y se presenta con la grafía real — nunca mostrar
  al cliente grafías fonéticas. Pero si el nombre es inventado, extranjero o
  ambiguo, marcarlo en el SCRIPTS.md como "pronunciación a validar" y aplicar
  la escalera del Paso 6 al producir.
- Chequear los no negociables contra el script antes de presentarlo.

No se genera ninguna imagen hasta que el usuario aprueba los scripts — cambiar
un guion es gratis, regenerar una producción no.

### Paso 4 — Avatar y frames → GATE 2

- Avatar: el aprobado en la ficha; generar uno nuevo solo si el pedido lo pide.
- **Un frame por clip, misma escena, distinto ángulo de cámara.** Frame B se
  genera usando el A como referencia (misma ropa, luz, set). Si solo cambia la
  boca entre frames, el corte parece glitch; si cambia el punto de vista,
  parece edición multicámara.
- **Racord:** todo objeto visible existe en los dos frames en la misma
  posición. Si en el B el producto está en la mano, en el A ya está sobre la
  mesa. Nada aparece de la nada.
- **El producto va SIEMPRE con su foto real como `reference_image_urls`.**
  Describirlo de memoria genera un producto parecido pero falso, y un producto
  falso invalida la producción completa — es el error más caro de todo el
  proceso. Describir en texto es último recurso, únicamente si la foto real
  dispara el filtro del generador, y en ese caso se avisa al usuario ANTES de
  generar que el producto será aproximado.
- Packaging con texto: además de la referencia, dictar el texto letra por
  letra en el prompt y prohibir inventar etiquetas. Los generadores degradan
  tipografía chica; el dictado la sostiene.
- **Escala dictada SIEMPRE** ("talle 37, largo de antebrazo, NO oversized") —
  obligatorio en productos de silueta voluminosa (plataformas, cuñas gordas,
  botas): el generador los agranda hasta lo absurdo. Y si salió gigante,
  **editar sobre esa imagen NO lo achica** (el modelo ancla la composición):
  regenerar DE CERO, con el producto bajo (a la cintura, contra el cuerpo) y
  el tamaño descrito relativo a la mano.
- **Un solo producto en escena.** Si el avatar además lo tiene puesto, hay 3
  unidades en cuadro y delata IA. Pies descalzos o fuera de cuadro.
- **Prohibir texto en fondos**: bolsas, packaging y carteles de fondo van
  "plain, NO lettering" explícito — si no, aparecen marcas mal escritas
  (una bolsa de fondo salió con la marca del cliente mal escrita).
- **Mirada a la lente + "solo sus dos manos en cuadro"** — sin esto aparecen
  miradas perdidas y manos fantasma entrando por los bordes.
- Casting **"real pero aspiracional"**: linda natural, maquillaje mínimo,
  contexto prolijo. El realismo extremo (ojeras marcadas, cocina desordenada)
  rebota con los clientes. Y el gesto del frame actúa el hook del guion
  (mano al pecho para la confesión, dedo en alto para la advertencia).
- Formato 16:9: mismo proceso; cambia `aspect_ratio`, el encuadre aprovecha el
  ancho para el set, y revisar que el escenario default tenga sentido para el
  destino (16:9 suele ser YouTube/web, no feed).

No se genera ningún video hasta que el usuario aprueba los frames.

### Paso 5 — QA de producto (bloqueante)

Comparar frame generado vs foto real, y mostrar el veredicto con evidencia
(zoom/crop si el producto tiene texto — el usuario juzga con sus ojos, no con
tu palabra):

1. **Identidad** — ¿es ESTE producto o uno inventado parecido?
2. **Texto** — ¿marca y etiquetas letra por letra?
3. **Proporción** — ¿tamaño creíble respecto a manos/mesa?

Si falla, regenerar. Si tras 2-3 pases queda un defecto menor (texto ilegible a
tamaño real), presentar el trade-off y que decida el usuario. Nunca presentar
un frame con defecto como "perfecto" — la confianza del usuario en el QA vale
más que un frame.

### Paso 6 — Producir, verificar, guardar

- Generar los 2 clips. En el prompt de animación siempre:
  - el guion textual, idioma y tono;
  - qué hace el que NO habla (boca cerrada, escucha, asiente);
  - protección del producto ("sus letras no cambian ni se deforman");
  - **negar los movimientos indeseados** ("sin zoom, sin alejamiento, la cámara
    no se mueve") — omitir no alcanza: si no se lo prohibís, el modelo lo
    inventa;
  - **"el producto queda EN MANO desde el primer frame hasta el último"** —
    sin esta línea el modelo lo hace desaparecer a mitad de clip (pasó);
  - **idioma: escribir literalmente "Argentine Rioplatense Spanish"** en el
    prompt (solo "Spanish" produce acento neutro o mexicano);
  - **pronunciación de nombres — escalera de 3 pasos** (validada en producción
    con dos marcas de nombre ambiguo; NO saltear al paso 3 de una):
    1. Default: guion con grafía real + nota fonética en el prompt
       (`"Naiara" is pronounced "nai-ÁH-ra" — Spanish, three syllables,
       stress on the A`). A veces con esto alcanza; a veces no.
    2. Nombre dudoso → producir UN clip y que el usuario lo escuche antes de
       quemar la tanda. La pronunciación no se puede verificar en QA propio:
       la valida un oído humano, siempre.
    3. Solo si el paso 1 falla: reescribir la palabra EN el guion como suena,
       minúscula y con tilde ("naiára") — avisando al usuario que es grafía
       fonética solo para el motor; la grafía real va en captions, SCRIPTS.md
       y todo registro. (Hubo una marca que necesitó 4 intentos hasta llegar
       acá.)
    Registrar la solución que funcionó en la ficha de marca del cliente.
- **Verificar descargando**: duración, resolución, audio, y frames extraídos
  (ffmpeg a seg 1/5/9) para deriva de cara, deformación de producto, elementos
  aparecidos. Si no está descargado, no está entregado — hubo clips listos en
  el servidor 18h sin que nadie lo supiera.
- QA post-render honesto: problemas conocidos van al SCRIPTS.md y al usuario
  con opciones. Cosmético ≠ fallo: el criterio es si se lee real en el feed.
- Motor rechaza → **cambiar la imagen, no el motor** (la caja del producto en
  vez del producto a la vista resuelve la mayoría). Cambiar de motor solo si el
  usuario lo pide. Registrar el rechazo en la ficha de marca: es conocimiento
  del cliente, no ruido.
- Guardar todo en la carpeta del cliente.
- **Polling colgado ≠ render colgado**: `get_video_result` a veces nunca
  devuelve la URL aunque el clip terminó hace rato. Probar directo el storage:
  `https://backend.indash.io/storage/.../generated/<workspace_id>/<output_name>`
  con `curl -I` (200 = listo, bajarlo de ahí).
- **Créditos**: Omni 10s ≈ 1000 créditos/clip. Si un batch se corta por saldo,
  registrar en SCRIPTS.md qué salió y qué falta con sus prompts congelados,
  avisar cuánto falta, y disparar el resto apenas el usuario recargue — sin
  volver a preguntar nada.

## Estructura de carpetas y registro

```
<Cliente>/
  ficha-marca.md      ← templates/ficha-marca-template.md, una por cliente
  V<N>-<Producto>/
    SCRIPTS.md          ← templates/SCRIPTS-template.md, obligatorio por video
    *-clipA.mp4, *-clipB.mp4          ← formato largo
    *-video1.mp4, *-video2.mp4        ← formato corto (1 clip = 1 video)
    *-frameA.png, *-frameB.png        ← corto: un frame por video
    *-DESCARTADO-<motivo>.mp4   ← descartes se renombran, no se borran
```

El SCRIPTS.md se escribe al producir y se actualiza cuando algo cambia — uno
desactualizado miente, y mentir es peor que no existir. Registrar los run_id en
el momento (se pierden fácil). Contiene: metadata, guiones con conteo, prompts
de animación textuales, frame+modelo+run_id por clip, decisiones con su porqué,
defaults asumidos, problemas conocidos, rechazos/descartes.

## Trato con el usuario

- Exactamente 2 gates (scripts, frames). El resto corre de corrido — el usuario
  eligió este proceso justamente para no ser consultado a cada paso.
- Reportar con honestidad: qué salió, qué falló, qué no entregarías y por qué.
- Aprendiste algo nuevo del cliente (un rechazo, una regla, un gusto) →
  actualizar su ficha de marca en el momento.
- Nunca usar un asset viejo del workspace sin verificarlo contra la fuente real
  (hubo un avatar guardado con la marca mal escrita en el packaging).

## Punto de entrada

Hacé la toma de contexto (ficha de marca, carpeta del cliente, productos del
workspace) y arrancá por el **Paso 0**: ningún video se produce sobre un
producto que no esté cargado con fotos reales.
