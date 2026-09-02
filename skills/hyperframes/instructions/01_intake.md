# 01 — Intake

Acá validás que haya con qué editar. **Esta skill no genera material: lo
ensambla.** Si no hay material, no hay pieza.

---

## Lo que necesitás sí o sí

| Input | Por qué | Si falta |
|---|---|---|
| **Material** — un grupo video del board, rutas de clips/imágenes/audio, o adjuntos del chat | Es lo que vas a editar | **Frená y derivá.** No inventes planos. |
| **Plataforma de destino** — IG Reels, Stories, feed 4:5, Meta ads, YouTube | Define aspect ratio, zona segura y duración | Proponé el default y confirmalo en Decisions |
| **Duración objetivo** | Define cuántos cortes entran | Proponé según plataforma (`style/pacing.md`) |

## Lo que proponés vos (no lo preguntes suelto)

Todo esto va junto en la **única pregunta consolidada** del paso 3, con un
default ya elegido y su razón en una línea:

- estructura del corte (cuántos segmentos y qué hace cada uno)
- transición primaria
- estilo de captions (o si no lleva)
- audio: música, voiceover, audio nativo de los clips, o silencio
- qué material entra y qué queda afuera

---

## Cómo llega el material (tres casos)

### Caso A — "armá el reel final del grupo \<grupo\>" (el caso normal)

El material es un **grupo video** del board. No preguntes qué hay: **andá a
mirar** (paso 2, Discovery):

- El orden de los clips: el array `creatives` del grupo en
  `briefs/<brief>/plan.json`.
- El MP4 vigente de cada clip: `meta.video.render.version` de su manifiesto →
  `creatives/<brief>/<grupo>/<id>/clips/<vN>.mp4`.
- Lo que dice cada clip: `meta.video.script`.

Si el humano nombra el grupo a medias ("el video de la confesión"), resolvelo
contra los `title` del plan; si hay más de un candidato, preguntá cuál.

### Caso B — el humano pasa rutas o adjuntos sueltos

Aceptalos. Los adjuntos del chat quedan en `.indash/chat-files/` (solo lectura
para vos — perfecto para leer y copiar). Cualquier archivo del material se
**copia al proyecto de entrega** antes de componer: la composición referencia
solo rutas relativas propias.

### Caso C — el material todavía no existe

El humano pide "editame un reel de X" y no hay clips renderizados. **No es esta
skill.** Decilo en una línea y derivá:

> Todavía no hay clips renderizados para editar. Generarlos es
> `video-execution` (o `creative-execution` si son imágenes). Cuando estén,
> vuelvo y armo el corte.

**No** empieces a escribir una composición con placeholders que el humano va a
tener que rellenar. Eso no es un entregable.

---

## Preguntas que SÍ hacés en Intake (máximo 2, y solo si falta lo crítico)

- *"¿Qué edito? ¿El grupo \<grupo\> del board o me pasás rutas?"*
- *"¿Para qué plataforma? (Reels 9:16, Stories, feed 4:5, Meta ads, YouTube 16:9)"*

Nada más. El resto se consolida en el paso 3.

## Preguntas que NO hacés acá

- ❌ "¿Qué transición querés?" → va en Decisions, con default.
- ❌ "¿Querés captions?" → va en Decisions, con default.
- ❌ "¿Qué música?" → va en Decisions, con default.
- ❌ "¿Cuántos cortes?" → lo decidís vos en el plan de edición.

---

## Señales de que el pedido está incompleto de verdad

Frená y pedí si pasa alguna:

1. No hay ni un grupo video, ni una ruta, ni un adjunto de material.
2. Hay más de un grupo video que matchea el pedido y no está claro cuál.
3. El humano pide captions de un voiceover que no existe como archivo ni como
   guion en los manifiestos.
4. El humano pide una duración imposible para el material que hay (30s de pieza
   con 12s de clips y sin stills para estirar).
5. Un clip del grupo tiene el render **desactualizado** (`fromStill` ≠ el
   `active` del still) o directamente no tiene render — ¿se edita con lo que
   hay, o se re-renderiza primero con `video-execution`?

En todos los casos: **una sola intervención**, concreta, con la opción más
razonable propuesta.

---

## Salida de este paso

Tenés identificado:
- qué material se edita (el grupo, o las rutas concretas),
- la plataforma de destino (aunque sea la propuesta por default),
- el modo (`full_render` / `plan_only`) ya resuelto en el paso 0.

→ Pasá a `instructions/02_discovery.md`. **En silencio.**
