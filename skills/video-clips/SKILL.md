---
name: video-clips
description: "Cómo se producen los CLIPS UGC de un video en un proyecto de Indash Studio (cwd con .indash/) — guion primero, still después, clip al final, todo en la carpeta del Workbench del creativo de video (workbench/<brief>/<carpeta>/{scripts,stills,clips}/). Un video es UN creativo del plan (`kind: video` + `seconds`); esta skill produce los clips de ~10s que después pega `video-composition`. Usala SIEMPRE que haya que escribir guiones, generar stills o renderizar clips de avatar para un video del Studio. Para piezas estáticas por capas es creative-execution; para montar y renderizar el video, video-composition."
language: es
tags: execution
owner: lburgwardtr
status: draft
reviewed: 2026-09-02
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
workbench/<brief>/<carpeta>/          ← una por creativo de video, LAZY
  .folder.json                        ← { "creative": "<brief>/<grupo>/<id>" }
  scripts/                            ← guiones, uno por clip, en .md
    clip-01.md  clip-02.md  clip-03.md
  stills/                             ← still de cada clip, versionado
    clip-01-v1.jpg  clip-01-v2.jpg  clip-02-v1.jpg
  clips/                              ← el mp4 de cada clip, versionado
    clip-01-v1.mp4  clip-01-v2.mp4
  musica.mp3 / referencias…           ← lo que el humano soltó desde Finder
```

- **La carpeta la resuelve la app.** Las tools de generación reciben
  `creative: "<brief>/<grupo>/<id>"` y escriben en la carpeta del Workbench
  vinculada a ese creativo (la crean, con su `.folder.json`, si no existe).
  Para los guiones `.md` que escribís vos, buscala escaneando
  `workbench/<brief>/*/.folder.json`; si todavía no existe, crela con el
  título o el id del creativo + el sidecar. No espejes el board: solo el
  creativo que estás trabajando.
- **Versión en el nombre**, no en carpetas: `clip-01-v2.mp4` es la segunda
  toma del clip 1. La ponen las tools (`name: "clip-01"` → `clip-01-v1`,
  `clip-01-v2`…): nunca pisan, y vos tampoco — el humano navega esto como
  Finder y compara versiones a ojo.
- Dónde cae cada cosa lo decís con `folder`: `"stills"` para `generate_image`,
  `"clips"` para `generate_video` (es su default). Nada de esto se promueve:
  los clips son insumo de `video-composition`, no candidatos.
- No tocás el manifiesto del creativo en este proceso (salvo `meta.generating`
  si el humano quiere ver la tarjeta pulsar): no hay bloque de clip en el
  manifiesto, no hay `clips/` en el creativo, no hay `active` que mover. El
  commit del video es el render, y eso es `video-composition`.

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

**No hay aprobación formal de guion.** Escribís los `.md`, **parás**, y el
humano los lee en el Workbench (o en el chat) y te dice que sigas. Eso es todo.
El resto corre de corrido — el humano eligió este proceso justamente para no
ser consultado a cada paso.

## Paso 0 — El producto, con sus fotos reales

Igual que en `creative-execution`, y por las mismas razones. `list_products`
para ver qué hay, `pull_product_images` para bajar las fotos reales, y
`library/products/<producto>/product.json` para saber qué es cada foto.

**Mirá la foto ANTES de escribir el guion.** Las descripciones mienten: qué
packaging tiene, qué textos lleva impresos, qué proporciones tiene. No
escribas "este:" ni "mirá esto" si el still no va a tener el producto en mano.

Leé también las `notes` del creativo en `plan.json`: ahí está escrito qué
cuenta el video, qué producto, y si lleva packshot o música (la trae el
humano — nunca generes música ni TTS).

## Paso 1 — Los guiones (los N a la vez)

**Antes de escribir una sola palabra, leé `reference/guiones.md`**: los dos
registros, el catálogo de hooks y CTAs con ejemplos reales entregados, y las
reglas de lenguaje.

- **Hook en los primeros 2 segundos** del clip 1, **CTA imperativo** al final
  del último. Si el video es de un solo clip, los dos conviven adentro.
- **Palabras: ~3 por segundo.** Un clip de 10s son 28-32 palabras; apuntá a
  32, el techo es ~34. Más que eso suena apurado y el lip-sync se degrada
  antes que la comprensión. Anotá el conteo en el `.md`.
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
- En una tanda de varios videos del mismo producto, **alterná registros**: dos
  videos que arrancan parecido se leen como campaña fabricada.

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
`workbench/<brief>/<carpeta>/scripts/`.** Pegá los N de corrido en el chat
también: la pregunta que tiene que poder contestar no es "¿este guion está
bien?" sino "¿estos clips cuentan una historia y no repiten el hook?", y eso
solo se ve leyendo seguido. Seguís cuando te diga.

## Paso 2 — Los stills (uno por clip)

Un still por clip, **misma escena, distinto ángulo de cámara**. Van a
`stills/clip-NN-vK.<ext>` (`generate_image { creative, folder: "stills",
name: "clip-01" }`; la versión y el formato los pone la tool).

- **Racord:** todo objeto visible existe en los clips vecinos en la misma
  posición. Si en el clip 2 el producto está en la mano, en el clip 1 ya está
  sobre la mesa. **Nada aparece de la nada.** Generá cada still usando el
  anterior como referencia (misma ropa, misma luz, mismo set): si solo cambia
  la boca, el corte parece glitch; si cambia el punto de vista, parece edición.
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
- **Prohibí texto en fondos**: bolsas, packaging y carteles de fondo van
  "plain, NO lettering" explícito, o aparecen marcas mal escritas.
- **Mirada a la lente** y **"solo sus dos manos en cuadro"** — sin eso
  aparecen miradas perdidas y manos fantasma entrando por los bordes.
- Casting **"real pero aspiracional"**: linda natural, maquillaje mínimo,
  contexto prolijo. El realismo extremo (ojeras marcadas, cocina desordenada)
  rebota con los clientes.
- Formato del still = formato del creativo (`canvas` del manifiesto, p. ej.
  9:16 → `aspect_ratio: "9:16"`). El clip hereda el encuadre del still.

### QA de producto, antes de renderizar

Comparar el still contra la foto real y decir el veredicto con evidencia:
**identidad** (¿es ESTE producto o uno inventado parecido?), **texto** (¿marca
y etiquetas letra por letra?), **proporción** (¿tamaño creíble respecto a
manos y mesa?). Si falla, regenerá como `-vK+1`. Si después de 2-3 pases queda
un defecto menor, presentá el trade-off (con `show_media`) y que decida el
humano. **Nunca presentes un still con defecto como "perfecto"** — la
confianza del humano en tu QA vale más que un still.

## Paso 3 — Los clips

Un `generate_video { creative, folder: "clips", name: "clip-01" }` por clip,
con el still elegido como `start_image`. Modelo por defecto
**omni** (audio nativo, tope 10s, es sobre lo que está calibrado todo esto).
**Si el humano pide otro modelo (seedance / veo / kling), leé
`reference/modelos.md` PRIMERO**: cambian las duraciones, el audio por acento
y las reglas de fidelidad — y hay clips que en otro modelo hay que replantear.

En el prompt de animación, SIEMPRE:

- el guion textual, idioma y tono;
- qué hace el que NO habla (boca cerrada, escucha, asiente);
- protección del producto: "sus letras no cambian ni se deforman";
- **negá los movimientos indeseados** ("sin zoom, sin alejamiento, la cámara
  no se mueve"). Omitir no alcanza: si no se lo prohibís, el modelo lo inventa;
- **"el producto queda EN MANO desde el primer frame hasta el último"** — sin
  esa línea el modelo lo hace desaparecer a mitad de clip;
- **el idioma escrito literal**: "Argentine Rioplatense Spanish". Solo
  "Spanish" produce acento neutro o mexicano.

### Pronunciación: escalera de 3 pasos, sin saltear

1. Guion con grafía real + nota fonética en el prompt (`"Lyanna" is pronounced
   "li-ÁH-na" — Spanish, three syllables, stress on the A`).
2. Nombre dudoso → producí UN clip y que el humano lo escuche antes de quemar
   la tanda. **La pronunciación no se puede verificar sola: la valida un oído
   humano, siempre.**
3. Solo si (1) falla: reescribí la palabra EN el guion como suena, minúscula y
   con tilde ("smúd") — avisando que es grafía fonética solo para el motor. La
   grafía real va en el `.md`, en los captions y en todo registro.

### Verificar el clip

Medilo y miralo: `ffprobe` para duración/resolución/audio, y frames a 1/5/9s
(`ffmpeg -ss <s> -i clip.mp4 -frames:v 1 frame.png`, o `show_media` para
que lo vea el humano) buscando deriva de cara, deformación del producto y
elementos aparecidos. **Si no lo verificaste, no está entregado.** Los
problemas conocidos van al humano con opciones, no maquillados. Cosmético ≠
fallo: el criterio es si se lee real en el feed.

**Si el motor rechaza, cambiá la IMAGEN, no el motor.** Los filtros rebotan
por lo que se ve, no por lo que se dice: mostrar la caja del producto en vez
del producto a la vista resuelve la mayoría. Cambiar de modelo solo si el
humano lo pide.

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
es conocimiento del cliente y va al workspace, no a un archivo suelto. Lo que
aprendas sobre el PROCESO (un modelo que degrada texto, un prompt que evita un
movimiento) vale para todos los clientes y va acá.

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

## Punto de entrada

Arrancá por el **Paso 0**: ningún guion se escribe sobre un producto cuyas
fotos reales no miraste. Después guiones → parás hasta que el humano diga →
stills → clips → la posta a `video-composition`.
