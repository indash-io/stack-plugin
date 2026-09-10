# 01 — Intake

Acá validás que haya con qué editar. **Esta skill no genera material: lo
ensambla.** Si no hay material, no hay pieza.

---

## Lo que necesitás sí o sí

| Input | Por qué | Si falta |
|---|---|---|
| **El creativo de video** — `creatives/<brief>/<grupo>/<id>` con `kind: "video"` | Fija formato (`canvas`), duración (`video.seconds`) y dónde se escribe | Si no existe en el plan, es `new-brief` (scaffold). No lo crees vos de la nada sin avisar |
| **Material** — la carpeta del Workbench vinculada (`workbench/<brief>/<carpeta>/` con `.folder.json` → tu creativo), o rutas concretas | Es lo que vas a editar | **Frená y derivá.** No inventes planos. |
| **Plataforma de destino** — IG Reels, Stories, feed 4:5, Meta ads, YouTube | Define zona segura y ritmo (el formato ya lo fija el canvas) | Proponé el default según el formato y confirmalo en Decisions |

## Lo que proponés vos (no lo preguntes suelto)

Todo esto va junto en la **única pregunta consolidada** del paso 3, con un
default ya elegido y su razón en una línea:

- duración final (el default es `video.seconds`; si el material no la aguanta,
  proponés otra y la anotás para actualizar el manifiesto)
- estructura del corte (cuántos segmentos y qué hace cada uno)
- transición primaria
- estilo de captions (o si no lleva)
- audio: música que trajo el humano, audio nativo de los clips, o silencio
- qué material entra y qué queda afuera

---

## Cómo llega el material (tres casos)

### Caso A — "montá el video <id>" (el caso normal)

El material está en la carpeta del Workbench del creativo. No preguntes qué
hay: **andá a mirar** (paso 2, Discovery):

- La carpeta: escaneá `workbench/<brief>/*/.folder.json` y quedate con la que
  apunta a `"<brief>/<grupo>/<id>"`. Si hay varias, la que tenga `clips/`.
- Los clips: `clips/clip-NN-vK.mp4` — el orden lo dan los números; la versión
  vigente es la que dijo el humano o `video-clips`, si no la `-vK` más alta.
- Lo que dice cada clip: `scripts/clip-NN.md`.
- Lo demás de la carpeta: música, b-roll, logos que el humano soltó.

Si el humano nombra el video a medias ("el de la confesión"), resolvelo contra
los `title` del plan; si hay más de un candidato, preguntá cuál.

### Caso B — el humano pasa rutas o adjuntos sueltos

Aceptalos. Los adjuntos del chat quedan en `.indash/chat-files/` (solo lectura
para vos — perfecto para leer y copiar). Cualquier archivo del material se
**copia a `composition/assets/`** antes de componer: la composición referencia
solo rutas relativas propias. Si conviene que quede a mano para próximas
vueltas, copialo también a la carpeta del Workbench.

### Caso C — el material todavía no existe

El humano pide "montame un reel de X" y no hay clips ni stills. **No es esta
skill.** Decilo en una línea y derivá:

> Todavía no hay clips para montar. Generarlos es `video-clips` (o
> `creative-execution` si son imágenes). Cuando estén en el Workbench, vuelvo
> y armo el corte.

**No** empieces a escribir una composición con placeholders que el humano va a
tener que rellenar. Eso no es un entregable.

---

## Preguntas que SÍ hacés en Intake (máximo 2, y solo si falta lo crítico)

- *"¿Qué video monto? ¿`<id>` del board o me pasás rutas?"*
- *"¿Para qué plataforma? (Reels, Stories, feed, Meta ads, YouTube)"*

Nada más. El resto se consolida en el paso 3.

## Preguntas que NO hacés acá

- ❌ "¿Qué transición querés?" → va en Decisions, con default.
- ❌ "¿Querés captions?" → va en Decisions, con default.
- ❌ "¿Qué música?" → la que haya en la carpeta; si no hay, sin música (Decisions).
- ❌ "¿Cuántos cortes?" → lo decidís vos en el plan de edición.

---

## Señales de que el pedido está incompleto de verdad

Frená y pedí si pasa alguna:

1. No hay carpeta del Workbench vinculada, ni una ruta, ni un adjunto.
2. Hay más de un creativo de video que matchea el pedido y no está claro cuál.
3. El humano pide captions de un voiceover que no existe como archivo ni como
   guion en `scripts/`.
4. El humano pide una duración imposible para el material que hay (30s de
   pieza con 12s de clips y sin stills para estirar).
5. Un clip tiene varias versiones (`-v1`, `-v2`, `-v3`) y nadie dijo cuál va.
6. El creativo está `approved` (congelado): no se toca; que el humano lo
   des-apruebe desde la app si quiere otra versión.

En todos los casos: **una sola intervención**, concreta, con la opción más
razonable propuesta.

---

## Salida de este paso

Tenés identificado:
- el creativo (carpeta, `canvas`, `video.seconds`, `notes`),
- la carpeta del Workbench con el material (o las rutas concretas),
- la plataforma de destino (aunque sea la propuesta por default),
- el modo (`full_render` / `plan_only`) ya resuelto en el paso 0.

→ Pasá a `instructions/02_discovery.md`. **En silencio.**
