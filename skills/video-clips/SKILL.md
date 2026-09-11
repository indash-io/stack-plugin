---
name: video-clips
description: "Cómo se producen los CLIPS UGC de un video en un proyecto de Indash Studio (cwd con .indash/) — guion primero, still después, clip al final, todo en la carpeta del Workbench del creativo de video (workbench/<brief>/<Título del plan>/{scripts,stills,clips}/). Un video es UN creativo del plan (`kind: video` + `seconds`); esta skill produce los clips de ~10s que después pega `video-composition`. Usala SIEMPRE que haya que escribir guiones, generar stills o renderizar clips de avatar para un video del Studio. Para piezas estáticas por capas es creative-execution; para montar y renderizar el video, video-composition."
language: es
tags: execution
owner: lburgwardtr
status: draft
reviewed: 2026-09-11
---

# Video Clips — los clips UGC de un video, en el Workbench

Sos el que produce los **clips** de UN video. El video es un creativo del board
(`kind: "video"`, `seconds`, un formato); lo que hacés acá es el material
intermedio que después se monta: guiones, stills y clips de ~10s. **Nada de
esto va a `creatives/`**: va a la carpeta del **Workbench** del creativo, y
recién `video-composition` escribe en el creativo (`composition/` +
`renders/`).

El contrato de disco (manifiesto, Workbench, `.folder.json`, orden de
escritura) está en el CLAUDE.md del proyecto. Acá está el OFICIO.

## Dónde escribís: la carpeta del Workbench del video

```
workbench/<brief>/<Título del plan>/  ← UNA por creativo, nombrada como el `title` del plan
  .folder.json                        ← { "creative": "<brief>/<grupo>/<id>" }
  scripts/                            ← guiones, uno por clip, en .md
    clip-01.md  clip-02.md  clip-03.md
  stills/                             ← still de cada clip, versionado
    clip-01-v1.jpg  clip-01-v2.jpg  clip-02-v1.jpg
  clips/                              ← el mp4 de cada clip, versionado
    clip-01-v1.mp4  clip-01-v2.mp4
  musica.mp3 / referencias…           ← lo que el humano soltó desde Finder
```

- **La carpeta la elegís vos, y es UNA por creativo.** Se llama como el
  **`title` del plan, tal cual** (`UGC creatina`, no `ugc-creatina-01` ni el
  id). **Antes de generar, buscala** escaneando
  `workbench/<brief>/*/.folder.json` (el sidecar apunta a
  `"<brief>/<grupo>/<id>"`): el humano puede haberla renombrado desde el
  Finder — **nunca asumas el nombre**. Si no existe, creala con el título +
  el sidecar `{ "creative": "<brief>/<grupo>/<id>" }`. Dos carpetas para el
  mismo creativo = error. No espejes el board: solo el creativo que estás
  trabajando.
- **Las tools escriben donde les decís.** `generate_image` / `generate_video`
  reciben `creative: "<brief>/<grupo>/<id>"` y `folder` = la ruta completa
  dentro del Workbench (`"workbench/<brief>/UGC creatina/stills"`). La app
  solo garantiza que sea dentro de `workbench/<brief>/` (afuera, error), crea
  la subcarpeta si falta y vincula la de primer nivel si no lo estaba. Sin
  `folder`, usa la carpeta vinculada al `creative` (o la crea con el título).
- **Versión en el nombre**, no en carpetas: `clip-01-v2.mp4` es la segunda
  toma del clip 1. La ponen las tools (`name: "clip-01"` → `clip-01-v1`,
  `clip-01-v2`…): nunca pisan, y vos tampoco — el humano navega esto como
  Finder y compara versiones a ojo.
- **Misma estructura en todos los videos**: `scripts/`, `stills/`, `clips/` (y
  `fondos/` si hace falta).
  `folder: ".../stills"` para `generate_image`, `folder: ".../clips"` para
  `generate_video`. Nada de esto se promueve: los clips son insumo de
  `video-composition`, no candidatos.
- No tocás el manifiesto del creativo en este proceso (salvo `meta.generating`
  si el humano quiere ver la tarjeta pulsar): no hay bloque de clip en el manifiesto, no hay
  `clips/` en el creativo, no hay `active` que mover. El commit del video es el
  render, y eso es `video-composition`.

## Por qué N clips y no uno largo

`ceil(segundos / 10)` orienta cuántos clips hacen falta: 30s son 3, 21s son 3,
10s es 1. No es una regla de estilo: es el techo del modelo. Los clips no son
"partes de una campaña", son un plano cada uno, y el corte entre ellos tiene
que leerse como edición multicámara — no como una costura. Si el video lleva
además packshot, placa o b-roll, esos segundos no son clips: descontalos.

## El orden: guion → still → clip

**El guion va primero, siempre.** Cambiar una palabra es gratis; regenerar un
still cuesta una espera y un clip cuesta plata que no vuelve. Y hay una razón
de oficio más fuerte que el costo: **el gesto del still actúa el hook del
guion**. Mano al pecho para la confesión, dedo en alto para la advertencia,
caja abierta al lado para "me llegaron". Si generás el still primero, terminás
escribiendo el texto contra una pose que salió por azar.

**Dos paradas, y solo dos.** Los guiones: escribís los `.md`, **parás**, el
humano los lee en el Workbench (o en el chat) y te dice que sigas. Los stills:
generás uno por clip, **parás**, el humano los revisa en la vista **Clips**
del Workbench (elige la versión de cada toma, fija comentarios sobre la
imagen) y te dice con qué still seguir. Recién ahí van los clips. Entre esas
dos paradas corrés de corrido — el humano eligió este proceso justamente para
no ser consultado a cada paso — pero un clip cuesta plata que no vuelve y se
rinde SOBRE un still: mandarlo sin que el still esté validado es tirar esa
plata.

## Paso 0 — El producto, con sus fotos reales

Igual que en `creative-execution`, y por las mismas razones. `list_products`
para ver qué hay, `pull_product_images` para bajar las fotos reales, y
`library/products/<producto>/product.json` para saber qué es cada foto.

**Mirá la foto ANTES de escribir el guion.** Las descripciones mienten: qué
packaging tiene, qué textos lleva impresos, qué proporciones tiene. No
escribas "este:" ni "mirá esto" si el still no va a tener el producto en mano.

Leé también las `notes` del creativo en `plan.json`: ahí está escrito qué
cuenta el video, qué producto, y si lleva packshot o música (lo trae el
humano — nunca generes música ni TTS).

## Paso 1 — Los guiones (los N a la vez)

**Antes de escribir una sola palabra, leé `reference/guiones.md`**: los dos
registros, el catálogo de hooks y CTAs con ejemplos reales entregados, y las
reglas de lenguaje.

- **Hook en los primeros 2 segundos** del clip 1, **CTA imperativo** al final
  del último. Si el video es de un solo clip, los dos conviven adentro.
- **La costura entre clips se escribe:** el clip N deja algo pendiente y el
  N+1 lo resuelve. La promesa que cruza el corte («te cuento por qué») es lo
  que hace que el siguiente se vea; si un clip cierra del todo, el corte se
  siente arbitrario. Los conceptos con giro («no gastás, ganás jugando») no
  entran en 10 segundos: por eso son dos clips, no uno.
- **Palabras: 32-34 por clip de 10s, medido, no estimado.** Con 29-31 el
  avatar habla lento y termina acelerado en post (una pieza entregada quedó a
  1.15×); con más de 34 suena apurado y el lip-sync se degrada antes que la
  comprensión. **El arreglo va en el guion, nunca en post.** Frases cortas y
  cortadas. Anotá el conteo en el `.md`.
- **Si el guion habla de plata** (ahorro, finanzas, cripto, apuestas, «no
  pagás»), **el CTA no se dice: se escribe en la placa final** que arma
  `video-composition`. El filtro del modelo bloquea la combinación «poné
  plata» + pedido de salir del video («sumate a la lista», «dejá tu mail»,
  una URL dictada) — aislado con A/B de una variable, tres imágenes
  distintas — y no es determinístico: a veces pasa, así que no se depende de
  él nunca. Una acción *dentro* del producto («armá tu mazo», «jugá una
  partida») es liviana; una *fuera* («dejá tu mail», «entrá a tal
  dirección») dispara. **Y en ese contexto una URL nunca se habla**: dictarla
  en el prompt cuelga el render sin error. Para el resto de rubros vale el
  catálogo de CTAs de `reference/guiones.md` tal cual.
- **Un hablante por clip.** Dos personas alternando diálogo en el mismo clip
  rompe el lip-sync: el modelo les mueve la boca a los dos. El que escucha va
  con boca cerrada, explícito en el prompt. El corte entre clips es el cambio
  de turno, como un podcast real editado.
- **Claims verificables solamente.** Nada de superlativos sin chequear contra
  fotos o ficha, ni promesas de durabilidad. Urgencia blanda sí ("antes de que
  vuelen"), stock u ofertas inventadas no.
- **Nombres de marca dudosos: detectalos ACÁ.** El guion se escribe y se
  presenta SIEMPRE con la grafía real. Si el nombre es inventado, extranjero o
  ambiguo, anotalo como "pronunciación a validar" y aplicá la escalera del
  Paso 3.
- En una tanda de varios videos del mismo producto, **otra persona y otro
  registro por pieza**: si comparten cara o arrancan parecido, el feed las lee
  como campaña fabricada y baja el alcance.
- **Se nombra el producto, no la plataforma** («TCG Battle», no «el juego de
  cartas de OLA»): la marca que tiene que quedar es la del producto.

Escribí cada guion en `scripts/clip-NN.md` con este formato — es lo que el
humano lee en el Workbench, así que tiene que leerse solo:

```markdown
# Clip 01 — Hook: confesión de compra

**Palabras:** 31 · **Registro:** orgánico · **Hablante:** ella, a cámara

> Bueno, listo, me las compré. Sí, ya sé, dije que no me compraba nada más…

**Gesto / escena:** mano al pecho, caja abierta sobre la mesa a la izquierda.
**Pronunciación a validar:** "Lyanna" → li-ÁH-na.
```

**Pará acá y avisale al humano que los guiones están en
`workbench/<brief>/<Título del plan>/scripts/`.** Pegá los N de corrido en el chat
también: la pregunta que tiene que poder contestar no es "¿este guion está
bien?" sino "¿estos clips cuentan una historia y no repiten el hook?", y eso
solo se ve leyendo seguido. Seguís cuando te diga.

## Paso 2 — Los stills (uno por clip)

Un still por clip, **misma escena, distinto ángulo de cámara**. Van a
`stills/clip-NN-vK.<ext>` (`generate_image { creative: "<brief>/<grupo>/<id>",
folder: "workbench/<brief>/<Título del plan>/stills", name: "clip-01" }` — la
versión la pone la tool; el formato es el que devuelve el modelo).

- **En 1K, siempre** — no mandes `resolution`. El clip sale a 720×1280:
  un still en 4K son 20× los píxeles y varias veces el costo para el mismo
  video. `2K`/`4K` solo si el humano lo pide explícitamente para ese still.
  Modelo `nano-banana-2`; `nano-banana-pro` solo si el humano lo pide o si
  UN still puntual falló en gpt-image por fidelidad del producto, nunca
  para la tanda entera.
- **Racord:** todo objeto visible existe en los clips vecinos en la misma
  posición. Si en el clip 2 el producto está en la mano, en el clip 1 ya está
  sobre la mesa. **Nada aparece de la nada.** Generá cada still usando el
  anterior como referencia (misma ropa, misma luz, mismo set): si solo cambia
  la boca, el corte parece glitch; si cambia el punto de vista, parece edición.
  La receta que cierra a la primera: el still anterior en `refs`, y el prompt
  describe **solo lo que cambia** — «Use the reference image as the exact
  source of truth for the person and the room. Same person, IDENTICAL face,
  IDENTICAL hair, same clothes. IDENTICAL room with IDENTICAL objects in
  IDENTICAL positions: <los objetos, uno por uno>. Only TWO things change, as
  if three seconds passed: the CAMERA <más frontal / tres cuartos, un poco más
  cerca> and their GESTURE and EXPRESSION <gesto concreto, mid-sentence>».
  **Listar los objetos del cuarto uno por uno** funciona mucho mejor que «la
  misma habitación»: el modelo reinventa lo que no le nombrás (con palabras
  solas cambió la cara, el peinado y medio cuarto).
- **El still contiene lo que el clip va a mostrar.** El render no inventa bien:
  el frame 0 tiene que traer ~el 70% de los elementos que aparecen en el clip,
  aunque sea insinuados (silueta, borde del objeto, parcial). Si el clip
  "abre" la escena, el still es la composición más cerrada con el resto
  sugerido. Lo que no entra en el still es señal de que va en OTRO clip.
- **El producto va SIEMPRE con su foto real en `refs`.** Describirlo de
  memoria genera un producto parecido pero falso, y un producto falso invalida
  la producción completa — es el error más caro de todo el proceso. Describir
  en texto es último recurso, solo si la foto real dispara el filtro, y en ese
  caso avisale al humano ANTES de generar que el producto va a ser aproximado.
- **Packaging con texto:** además de la referencia, dictá el texto letra por
  letra y prohibí inventar etiquetas. Los generadores degradan tipografía
  chica; el dictado la sostiene. Si la tipografía es muy chica, el producto va
  APOYADO y quieto: la mano lo señala, no lo levanta.
- **Escala dictada SIEMPRE** ("talle 37, largo de antebrazo, NO oversized").
  Obligatorio en productos de silueta voluminosa: el generador los agranda
  hasta lo absurdo. Y si salió gigante, **editar sobre esa imagen NO lo
  achica** — el modelo ancla la composición. Regenerá DE CERO, con el producto
  bajo (a la cintura, contra el cuerpo) y el tamaño descrito relativo a la mano.
- **Un solo producto en escena.** Si el avatar además lo tiene puesto, hay dos
  unidades en cuadro y delata IA.
- **Producto digital (app, juego, plataforma): nada en las manos.** El
  producto no puede estar «en mano»: entra después como insert de pantalla en
  `video-composition`. Un celular en la mano queda raro y ocupa las manos, que
  es lo que le da vida al plano. Pedilo explícito y en mayúsculas: `HER/HIS
  HANDS ARE EMPTY — there is NO phone, NO smartphone, NO tablet, NO laptop, NO
  headphones, NO controller and NO television anywhere in the image`. Y **sin
  marcas de terceros**, también en mayúsculas (`NO brand logos of any kind, NO
  console logos, NO collectible figures`): ya rebotaron una notebook con logo
  de Apple, un mando de PlayStation, auriculares de marca y cajas de
  coleccionables. Para producto digital el Paso 0 es mirar el **material real
  del cliente** (videos, capturas, el sitio): una producción entera se tiró
  por generar a alguien con cartas de cartón en la mesa cuando el juego era
  digital y se jugaba en el celular.
- **Prohibí texto en fondos**: bolsas, packaging y carteles de fondo van
  "plain, NO lettering" explícito, o aparecen marcas mal escritas.
- **Mirada a la lente** y **"solo sus dos manos en cuadro"** — sin eso
  aparecen miradas perdidas y manos fantasma entrando por los bordes.
- Casting **"real pero aspiracional"**: linda natural, maquillaje mínimo,
  contexto prolijo. El realismo extremo (ojeras marcadas, cocina desordenada)
  rebota con los clientes.
- **Skin UGC del still**, para que se lea como video de celular y no como
  render (compatible con lo anterior: piel real sí, ojeras y desorden no):
  foto candid de smartphone; **plano medio, del pecho para arriba — nunca
  primer plano**: una cara fotorrealista muy cerca sube el riesgo de que el
  filtro la lea como parecido con una persona real; **luz motivada** por algo
  que está en cuadro (una tira LED, un ring light, el monitor), nada de luz de
  ningún lado; piel real (poros visibles, brillo en la frente, pelos sueltos,
  cero retoque); profundidad de campo corta, leve inclinación de cámara, algo
  de ruido de sensor. Los colores del set salen de la paleta del producto: los
  inserts después cortan sin salto de color. Y **ropa que no se funda con el
  fondo**: un buzo negro en un cuarto apagado hace desaparecer el cuerpo.
- Formato del still = formato del creativo (`canvas` del manifiesto, p. ej.
  9:16 → `aspect_ratio: "9:16"`). El clip hereda el encuadre del still.

### QA de producto, antes de renderizar

Comparar el still contra la foto real y decir el veredicto con evidencia:
**identidad** (¿es ESTE producto o uno inventado parecido?), **marca** (¿el
logo y el nombre están enteros, no rotos ni inventados?), **proporción**
(¿tamaño creíble respecto a manos y mesa?), **anatomía** (¿dos manos, cinco
dedos, una cara normal?).

**Regenerás (`-vK+1`) SOLO por defecto flagrante**: tres brazos o manos de
más, producto distinto al real (otro envase, otro color, dos unidades),
logo/marca rotos o inventados, texto en el fondo, el producto que no está.
Cada still cuesta créditos y el clip sale a 720p: **la letra chica del label
NO es motivo** — una palabra borrosa o un carácter cambiado en el renglón
pequeño no se lee en el feed, se anota en el reporte y sigue. Máximo un
reintento por tu cuenta; si sigue mal, `show_media` con las opciones y que
decida el humano (con el trade-off dicho). **Nunca presentes un still con
defecto como "perfecto"** — decí qué tiene y seguí; la confianza del humano
en tu QA vale más que un still. Si el humano quiere el label impecable, lo
pide él, y ahí sí: producto apoyado, más grande en cuadro, dictado letra por
letra, más refs — no más resolución.

### Pará: los stills los valida el humano

Los stills son el último punto barato y el clip se rinde sobre ellos. Si el
humano quiere otro casting, otra luz u otro vestuario, se cambia acá, no con
clips ya rendidos colgando de esa cara. **Acá parás, siempre.** Mostrá los
stills con `show_media` (por clip, las versiones que valgan la pena) y avisá
que están en `stills/`. El humano los revisa en la vista **Clips** del
Workbench: elige el still de cada toma y puede fijar comentarios sobre la
imagen; eso te llega al chat como una ronda de texto («clip-01: use
stills/clip-01-v4.jpg · (top-left): más luz en la cara»). Con esa ronda:
regenerás lo que tenga comentarios (`-vK+1`, una versión por comentario, no
diez) y volvés a parar; arrancás los clips SOLO desde los stills elegidos y
SOLO cuando el humano te dijo que sigas. Si dice «dale» sin elegir, usá la
última versión de cada toma y decilo. En una tanda de varios videos, parás
por video, no por still.

## Paso 3 — Los clips

Un `generate_video` por clip, con el still elegido como `start_image`,
`creative: "<brief>/<grupo>/<id>"`,
`folder: "workbench/<brief>/<Título del plan>/clips"` y `name: "clip-01"` →
`clips/clip-01-vN.mp4`. Modelo por defecto **omni** (audio nativo, tope 10s,
es sobre lo que está calibrado todo esto). **Si el humano pide otro modelo
(seedance / veo / kling), leé `reference/modelos.md` PRIMERO**: cambian las
duraciones, el audio por acento y las reglas de fidelidad — y hay clips que en
otro modelo hay que replantear.

En el prompt de animación, SIEMPRE:

- el guion textual, idioma y tono;
- **`FAST, urgent, high-energy delivery`** (matizado por el registro del guion,
  pero siempre con energía): sin eso queda lento aunque el guion tenga las
  palabras justas;
- qué hace el que NO habla (boca cerrada, escucha, asiente);
- protección del producto: "sus letras no cambian ni se deforman";
- **negá los movimientos indeseados** («sin zoom, sin alejamiento»). Omitir no
  alcanza: si no se lo prohibís, el modelo lo inventa. La cámara quieta es el
  default; para look de celular en mano vale `handheld camera with subtle
  drift`, que no es zoom ni alejamiento;
- **"el producto queda EN MANO desde el primer frame hasta el último"** — sin
  esa línea el modelo lo hace desaparecer a mitad de clip;
- **el idioma escrito literal**: "Argentine Rioplatense Spanish". Solo
  "Spanish" produce acento neutro o mexicano;
- **y al final, siempre**: `Clean image with NO burned-in subtitles, NO
  captions, NO text overlay, NO writing of any kind on screen`. Sin esa línea
  el modelo quema subtítulos inventados con texto roto («tu dinera anoa pn
  son tues somehir» apareció grabado en un clip).

### Pronunciación: escalera de 3 pasos, sin saltear

1. Guion con grafía real + nota fonética en el prompt (`"Lyanna" is pronounced
   "li-ÁH-na" — Spanish, three syllables, stress on the A`).
2. Nombre dudoso → producí UN clip y que el humano lo escuche antes de quemar
   la tanda. **La pronunciación no se puede verificar sola: la valida un oído
   humano, siempre.**
3. Solo si (1) falla: reescribí la palabra EN el guion como suena, minúscula y
   con tilde ("smúd") — avisando que es grafía fonética solo para el motor. La
   grafía real va en el `.md`, en los captions y en todo registro.

Las siglas son el caso típico: el modelo leyó «TCG» como «TSG», deletreando
en inglés. Salidas: decir solo una parte del nombre o reformular, y dejar la
sigla completa en tipografía (los captions los corrige `video-composition`, y
la corrección se declara).

### Verificar el clip

Medilo y miralo: `ffprobe` para duración/resolución/audio, y frames a 1/5/9s
(`ffmpeg -ss <s> -i clip.mp4 -frames:v 1 frame.png`, o `show_media` para
que lo vea el humano) buscando deriva de cara, deformación del producto y
elementos aparecidos. **Si no lo verificaste, no está entregado.** Los
problemas conocidos van al humano con opciones, no maquillados. Cosmético ≠
fallo: el criterio es si se lee real en el feed.

La app verifica que el mp4 haya bajado entero (contra el tamaño que reporta
el server): una descarga truncada no se ve como archivo roto, se ve como que
el modelo «se comió la última frase» o como un render que aborta después. Si
la tool falla con «llegó truncada», volvé a pedirlo tal cual.

### Cuando el motor falla

**Primero: ¿es el filtro de contenido o es la plataforma?** Tienen firmas
distintas. El filtro **rechaza o cuelga siempre con el mismo guion e imagen**;
la plataforma degradada devuelve errores explícitos y variados (`HTTP 500`,
`failed while processing file`, timeouts) y **hace fallar también lo que
antes salía**. El diagnóstico correcto es **re-tirar una combinación que YA
funcionó**: si esa también falla, no es tu guion ni tu imagen, es la
plataforma, y hay que esperar. Siete fallos seguidos parecieron el filtro
porque el guion hablaba de plata; dos horas después salió todo a la primera
sin tocar una coma — sin ese control se reescribe un guion sano y no se
arregla nada. En Studio la generación corre server-side y el error te llega
por la tool: leelo antes de reescribir.

**Si es el filtro, cambiá la IMAGEN antes que el motor.** Los filtros rebotan
por lo que se ve más que por lo que se dice: mostrar la caja del producto en
vez del producto a la vista resuelve la mayoría; en guiones de plata, el
sospechoso número uno es un CTA que pide salir del video (Paso 1). **Y al
aislar, cambiá UNA sola variable**: dos cierres distintos sobre el mismo
still antes de tocar la imagen. Cambiar guion + duración + resolución a la
vez son tres variables, cero información y dos renders tirados. Cambiar de
modelo solo si el humano lo pide.

## Al terminar: pasarle la posta a `video-composition`

Cuando los N clips están verificados, resumile al humano qué hay en la
carpeta (clips vigentes por nombre, `-vK` elegida de cada uno, qué falta) y
ofrecé montar: **`video-composition`** lee esa carpeta, copia lo que entra a
`composition/assets/` del creativo y renderiza con `render_video`. Los
guiones `.md` son además la fuente de los captions verbatim.

## Créditos

El clip se cobra **por segundo de output**, con cargo por adelantado del lado
del server. Un video de 30s son ~3000 créditos. Si una tanda se corta por
saldo, decí exactamente qué salió y qué falta, con sus prompts, y disparás el
resto apenas el humano recargue — sin volver a preguntar nada.

## Lo que aprendas, guardalo

Un rechazo de filtro, una regla que dio el humano, un avatar que funcionó: eso
es conocimiento del cliente y va al workspace (`save_learnings`), no a un
archivo suelto. Lo que aprendas sobre el PROCESO (un modelo que degrada
texto, un prompt que evita un movimiento) vale para todos los clientes y va acá.

El canal para guardarlo es la skill **save-learnings** (la invoca el humano con
`/save-learnings`, nunca vos solo): usa la tool `mcp__indash__save_learnings`
para mandar los learnings del cliente al `LEARNINGS.md` de su workspace y los de
proceso, anonimizados, al equipo. Si la sesión dejó algo de esto, sugerila en
una línea al cerrar.

## Errores que ya pagamos

- Guion escrito después del still → el hook no pega con el gesto y hay que
  regenerar los dos.
- Producto descrito de memoria en vez de con su foto → producción entera
  inválida, y no se nota hasta que el cliente lo ve.
- Producto que se esfuma a los 9 segundos por no escribir la línea de "en mano
  hasta el último frame".
- Bolsa de fondo con la marca mal escrita por no prohibir texto en fondos.
- Clips escritos dentro de `creatives/` → el board mostraba tarjetas de clip
  que nadie pegaba. El video es UN creativo; los clips son Workbench.
- Subtítulos inventados quemados en el clip por no escribir la línea de «NO
  burned-in subtitles».
- Siete clips «bloqueados por el filtro» que eran la plataforma caída: se
  reescribió un guion sano y no se arregló nada.
- Una URL dictada en el guion de un producto de plata → el render colgó sin
  error, tres veces.
- Cuatro stills de una persona con cartas de cartón para un juego que era
  digital: no se miró el material real del cliente antes de escribir.
- Un still B descrito con palabras («la misma persona en la misma habitación»)
  en vez de con el A como referencia → otra cara, otro peinado, medio cuarto
  nuevo.

## Punto de entrada

Arrancá por el **Paso 0**: ningún guion se escribe sobre un producto cuyas
fotos reales no miraste (para producto digital, su material real). Después
guiones → parás hasta que el humano diga → stills (avisás y seguís) → clips →
la posta a `video-composition`.
