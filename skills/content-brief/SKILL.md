---
name: content-brief
description: Arma el brief de contenido de un período para una marca DTC e-commerce con el mismo contexto de marca y la misma metodología que el agente de briefs de la app de Indash — dos o tres mensajes con fuente, y cada pieza (videos UGC, estáticos, carruseles, historias) con copy literal —, lo guarda en Indash para que el cliente y el equipo lo revisen, y orquesta las skills de ejecución del stack. Disparala cuando el user pida "armá el brief del mes/período", "plan de contenido", "calendario de piezas", "brief de social media" o equivalente.
language: es
owner: manuel-soria
status: published
reviewed: 2026-08-25
---

# Content Brief — el brief del período

## Rol

Armás el brief de contenido de un período para una marca. El criterio no es tuyo ni de esta skill: es el de Indash, y vive en el conector. Esta skill te dice **en qué orden llamar las tools**; cómo se decide un mensaje y cómo se escribe una pieza te lo da `get_brand_context`.

Es la misma metodología con la que corre el agente de briefs de la app (`ecom-founder` decide qué mensajes y por qué, `content-brief-builder` escribe cada pieza). Un brief armado acá y uno armado en la app tienen que salir iguales. Por eso **no la reemplaces por tu idea de qué es un brief**, ni la resumas de memoria de una sesión anterior: se edita en la app y el próximo llamado ya trae lo nuevo.

## Qué entregás

1. **El brief guardado en Indash**, con su URL. Es un borrador que la persona revisa pieza por pieza en la app, y que Indash aprueba antes de producir.
2. **Los chequeos** que devuelve `save_brief`, con lo rojo corregido o explicado.
3. **El handoff**: qué skill del stack ejecuta cada tipo de pieza.

## Workflow (orden estricto)

### 1. Gate y workspace

Aplicá el gate del conector `indash`. Resolvé el workspace con `list_workspaces` (el equipo de Indash, con `search_workspaces`). Si la carpeta del cliente tiene `CLAUDE.md` con el workspace, usá ese.

Si el conector no tiene `get_brand_context` y `save_brief`, está desactualizado: frená y pedile a la persona que lo reconecte. No armes el brief "a la vieja usanza".

### 2. Contexto y metodología

Llamá `get_brand_context` con `include_methodology: true`. Vuelve:

- **El contexto de marca**: el onboarding que cargó el cliente (mecanismo, reseñas sin editar, objeciones, corpus propio, ganadoras, límites, objetivo). `context.source` dice de dónde salió.
- **El inventario**: qué hay y qué falta. Es contexto, no un freno: armás el brief con lo que hay.
- **Las aclaraciones del cliente**: son reglas. Se aplican a todas las piezas y no se repreguntan.
- **El plan**: cadencia, cupo de videos e imágenes, y el período que viene con su fecha de entrega. El cupo no se excede.
- **El índice de material**: los archivos originales, cada uno con su id y una URL de lectura.
- **La metodología**: una nota que traduce las tools del portal a las de acá, el `AGENT.md` (el flujo, etapa por etapa) y el índice de las dos skills.

Después leé los dos `SKILL.md` que vienen en `methodology.read_first`, llamando de nuevo a `get_brand_context` con `methodology_files`. Pesan demasiado para venir en la primera respuesta. Sin leerlos no propongas mensajes.

Sumá lo que pide el `AGENT.md` en su etapa 1: `get_brand_kit`, `list_products` y `list_creatives`.

### 3. Armar el brief

Seguí el `AGENT.md` al pie: diagnóstico en una línea, dos o tres mensajes con fuente, validaciones en el momento en que aparece el pedido, intake corto, reparto dentro del cupo, escritura un mensaje por vez. Las preguntas que ahí van con `ask_user` se las hacés a la persona en el chat, con las mismas reglas: lo que ya está en el contexto no se pregunta.

- **Antes de escribir un formato, leé su reference** (`methodology_files` con el path del índice: `ugc-video.md`, `estaticos.md`, `carruseles.md`, `historias.md`, y `voz.md` para la ficha de voz).
- **Abrí el material que haga falta** con `material_ids`. Las imágenes vuelven como imágenes que podés ver; el resto, como URL firmada. Las marcadas `always` en el índice definen la voz de la marca: abrilas antes de escribir la primera pieza. "Esto NO somos" pesa tanto como "esto somos".
- **En Claude Code**, lo pesado (un brand book en PDF, un video, un Word) lo podés bajar de su URL firmada a una carpeta temporal y leerlo local. Las URLs vencen en unas dos horas: si vencieron, pedí el índice de nuevo.
- **Lo que falta no se inventa.** Ni un mecanismo, ni una reseña, ni un precio, ni un claim. Va a `ficha.pendientes` con responsable y fecha, y se lo decís a la persona en una línea.
- Si la carpeta del cliente tiene `CLAUDE.md`, suma lo que el contexto de Indash no tenga. Si se contradicen, decíselo a la persona; no elijas en silencio.

### 4. Guardar y corregir

Llamá `save_brief` con el documento **entero**. El schema de `doc` es el de la app y cada campo dice qué lleva. No mandes `n`, `status`, `note` ni `ready`.

- Si el documento no valida, no se guarda nada y vuelven los errores por path. Corregí y llamá de nuevo.
- La primera vez te devuelve un `draft_id`. **Todas las llamadas siguientes de ese brief lo llevan**; sin él creás un brief duplicado.
- Leé los chequeos. Los rojos que dependen de vos (guiones fuera de 75 a 85 palabras, hooks repetidos, oferta sin vigencia, carrusel sin continuidad, link de historia que no va último) se corrigen y se guarda de nuevo. Los que dependen del cliente (un producto sin foto, el contexto de marca vacío) se los decís en una línea.
- Cuando la persona pide cambios, mandás el documento corregido con el mismo `draft_id`. Las piezas que no tocaste conservan su OK.

### 5. Mostrar y mandar a revisión

Pasale la URL a la persona y contale en tres o cuatro líneas qué quedó armado: los mensajes, el reparto contra el cupo y lo que quedó pendiente.

`send: true` congela la versión, se la pasa a Indash y le avisa al equipo. **Solo cuando la persona leyó el brief y te dice explícitamente que lo mandes.** "Quedó bien" no es una orden de mandar.

### 6. Copia en disco y handoff

En Claude Code, guardá además una copia legible en `briefs/<AAAA-MM-DD>_<periodo-slug>_v<N>.md` de la carpeta del cliente (versiona, no pisa), con la URL del brief arriba de todo. La fuente de verdad es la de Indash: la copia es para trabajar las piezas sin salir de la carpeta.

Cerrá con el handoff de abajo y preguntá por cuál arrancar. **No produzcas piezas de un brief que Indash todavía no aprobó**, salvo que la persona te lo pida sabiéndolo.

## Si el workspace no tiene contexto

`context.source` en `none` quiere decir que no hay onboarding ni `CONTEXT.md`. La metodología vuelve igual, porque es de Indash y no de la marca; lo que falta es la materia prima.

1. Decíselo a la persona y ofrecele completar el onboarding: acá mismo, conversando, con la skill `new-client`, o en la app (`/w/<workspace>/onboarding`). Es lo que resuelve todos los briefs que vengan, no solo este.
2. Si quiere avanzar igual, pedile el mínimo que pide el `AGENT.md`: el mecanismo explicado para alguien de 12 años y cinco reseñas tal cual. Sumá el `CLAUDE.md` del cliente, el brand kit y el catálogo.
3. Todo lo demás va a `ficha.pendientes`. El chequeo de base fundacional va a salir en rojo y está bien que salga: es verdad.

`context.source` en `context_md` es el contexto cargado a mano en ajustes, de antes del onboarding. Sirve. Mirá la fecha de cada sección: una sección vacía o vieja se marca pendiente.

## Cómo orquesta las skills de ejecución

El brief planifica; la pieza la produce la skill que corresponde, con el copy literal del brief como insumo.

| Pieza del brief | Skill que la ejecuta |
|---|---|
| Video (guion UGC) | `ugc-generator` (produce los clips) o `ugc-video-prompts` (solo los prompts) |
| Estático | `ads` |
| Carrusel | `carruseles` |
| Historia | `stories-nano-banana` |
| Montaje de los clips de avatar (silencios, morphs, subtítulos, placa) | `edicion-ugc` |
| Pieza final con assets varios, captions con estilo o placa animada | `hyperframes` |
| Voz en off de una pieza (el guion ya está en el brief) | `locuciones` |

**El video suele necesitar dos pasos**: primero los clips, después la post-producción. Si el brief pide un reel terminado, nombrá a los dos en el handoff, en ese orden.

Los emails y los videos que no son UGC (`email-marketing-ecomm`, `all-videos`) no salen de este brief. Si la persona los pide, van directo a su skill.

## Reglas no-negociables

1. **Siempre** aplicás el gate del conector `indash` antes de arrancar. Sin conector no hay brief.
2. **Siempre** arrancás con `get_brand_context` e `include_methodology: true`, y leés los dos `SKILL.md` antes de proponer mensajes. Nunca escribís un brief con una metodología recordada o inventada.
3. **Nunca** inventás lo que falta. Se marca pendiente, con responsable y fecha.
4. **Nunca** excedés el cupo del plan. Si piden más, se saca de otro formato o se habla de subir el plan.
5. **Siempre** el brief termina en `save_brief`. Un brief que quedó solo en el chat no existe para el equipo.
6. **Siempre** reusás el `draft_id` en las llamadas siguientes.
7. **Nunca** mandás `send: true` sin una confirmación explícita de la persona.
8. **Siempre** cerrás con el handoff que mapea cada tipo de pieza a su skill.
9. El copy va en la voz de la marca, sin emojis ni guiones largos. Con la persona, español rioplatense, directo y sin relleno.

## Punto de entrada

Cuando el user pida armar el brief o el plan de un período, **arrancá por el paso 1** y llamá a `get_brand_context` antes de preguntarle nada.
