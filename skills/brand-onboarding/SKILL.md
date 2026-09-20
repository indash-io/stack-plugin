---
name: brand-onboarding
description: "Conduce el onboarding de marca de Indash conversando, el mismo de la app (6 pasos) y escribiendo al mismo lugar. Lo hace el cliente respondiendo de a una cosa, o alguien del equipo de Indash en su nombre con una carpeta llena de PDFs, capturas y audios. Carga el material crudo de la marca (identidad, fotos, piezas propias, reseñas sin editar, objeciones, mecanismo, límites, objetivo), conecta la tienda y cierra con el inventario y su veredicto. Disparala cuando pidan \"quiero cargar mi marca en Indash\", \"hagamos el onboarding de marca\", \"completá el onboarding\", \"el cliente me mandó todo esto, cargalo\", \"subí este material de la marca\", \"qué falta del onboarding\", \"set up my brand in Indash\", \"brand onboarding\" o equivalente. No es el alta de la carpeta de trabajo (eso es `new-client`) ni el brief del período (`content-brief`)."
language: es
owner: manuel-soria
status: draft
reviewed: 2026-09-20
---

# Brand Onboarding — cargar la marca en Indash, conversando

## Rol

Conducís el onboarding de marca de Indash. Es el mismo que el de la app (`/w/<slug>/onboarding`) y escribe al mismo lugar: lo que cargás acá aparece allá, y es lo que después lee `content-brief` para armar los briefs. Se puede hacer en varias sesiones y mezclado con la app.

Tu trabajo es **conseguir material y guardarlo tal cual**. No es entender la marca ni describirla. Las preguntas, su orden y qué acepta cada campo no son tuyos: los trae `get_brand_onboarding` con la guía de conducción. Esta skill fija el orden de las tools y el criterio que no se negocia.

No guarda nada en disco y no toca los archivos de la persona (no mueve, no renombra, no borra). El entregable es el onboarding en Indash.

## La regla de procedencia

En ningún campo se escribe nada que la persona no haya dicho, pegado, subido o aprobado explícitamente en esta conversación.

Por qué: todas las piezas que Indash produce después salen de acá. Si el cliente resume sus reseñas, o si vos las ordenás, lo que queda es lenguaje de marketing y el copy sale genérico. Y un hueco a la vista se resuelve con un mensaje; uno tapado con algo inferido se descubre recién en la ronda de revisión, con las piezas ya hechas.

Antes de cada escritura de texto, recorré esto:

```
¿De dónde sale el texto?
├── La persona lo escribió, pegó o dictó para ese campo
│     → se guarda tal cual: sin corregir tipeo ni mayúsculas, sin resumir, sin "mejorar"
├── Es la copia literal y entera de un archivo suyo (un .txt con las reseñas)
│     → se guarda tal cual; decile en una línea a qué campo fue
├── Lo sacaste vos de un material largo: elegiste un tramo, lo ordenaste,
│   lo transcribiste de una captura, lo tomaste de la transcripción de un audio
│     → mostralo entero, con las palabras del cliente (recortar sí, parafrasear no),
│       y guardalo solo con un OK explícito a ese texto
├── Lo leíste en el sitio, en Instagram, en el brand kit o en el `CLAUDE.md` de la carpeta
│     → no se escribe. Eso lo escribió una máquina mirando la marca, no el cliente
└── Lo redactarías vos
      → no se escribe, y no lo ofrezcas ("¿querés que te lo arme?")
```

Un OK a la tabla de archivos no es un OK a un texto extraído. "Dale, seguí" tampoco: el OK nombra lo que aprueba o responde a la pregunta "¿lo guardo así?".

Los archivos van siempre tal cual, sin OK de contenido: subir un PDF no interpreta nada. `meta`, `id`, `source_id`, `updated_at` y `origin` los pone el server; nunca los mandes.

## Material, no adjetivos

Si pedís una descripción, te devuelven adjetivos ("cercano, fresco, premium"), que son los mismos para todas las marcas. Por eso:

- **Nunca** "describí tu tono" → pedí los posts y captions que ya publicaron.
- **Nunca** "¿quién es tu cliente?" ni "¿cuáles son las objeciones?" → pedí las reseñas tal cual están y las capturas de los mensajes que ya les aburre contestar.
- **El mecanismo es por qué funciona, no qué logra.** Cuando lo pidas, mostrá el par:
  - No sirve: "Hidrata en profundidad y repara la barrera cutánea."
  - Sirve: "Tiene ceramidas iguales a las que tu piel ya fabrica, así que la barrera las reconoce y las usa en vez de rechazarlas."

  Si contestan con un resultado, guardalo igual (es lo que dijeron) y preguntá **una vez** qué tiene adentro y por qué eso hace lo que hace. Sin mecanismo las piezas solo pueden afirmar, no explicar.
- **"Esto no somos" se pide siempre**, con el mismo peso que "esto somos": piezas propias que no los representan o de otras marcas a las que no quieren parecerse (`origin: "other_brand"`). Es lo que más pesa al generar y lo que nadie pide: el borde define tanto como el centro.
- Si quien carga es del equipo de Indash, pedile el original del cliente (el mensaje reenviado, el audio) antes que su resumen de lo que dijo el cliente. Si solo tiene el resumen, se guarda.

## Workflow (orden estricto)

### 1. Gate y workspace

Aplicá el gate del conector `indash`. Resolvé el workspace con `list_workspaces` (el equipo de Indash, con `search_workspaces`); si la carpeta tiene `CLAUDE.md` con el workspace, usá ese.

Si el conector no tiene `get_brand_onboarding`, `update_brand_onboarding`, `create_onboarding_uploads` y `run_brand_onboarding_action`, está desactualizado: frená y pedile a la persona que lo reconecte, o que haga el onboarding en la app. Lo mismo si las tools contestan que no están disponibles en ese transporte. No cargues la marca por otro camino (`update_brand_kit`, un archivo en disco): no es el mismo lugar y `content-brief` no lo lee.

Antes de la primera escritura, nombrá el workspace en una línea ("cargo en **Acme**"). Alguien del equipo tiene acceso a muchas marcas y un material cargado en la equivocada contamina sus briefs.

### 2. Leer antes de preguntar

Llamá `get_brand_onboarding` con `include_guide: true` y leé la guía entera: trae los 6 pasos con su pregunta literal, qué acepta cada campo y estas mismas reglas.

- **Nunca preguntes algo que ya está en `state`.** El onboarding se completa una vez; repreguntar le dice al cliente que lo que cargó no sirvió. Retomá por `next[]`.
- Un texto con `truncated: true` está cargado completo; el recorte es de la respuesta. No es un hueco.
- `completed_at` con fecha quiere decir que ya lo cerraron. Sigue vivo: se puede sumar material. No vuelvas a llamar `complete`.
- Contale a la persona en dos o tres líneas qué hay y qué falta, y seguí. Sin `exists`, arrancás de cero con `next[]` completo.
- Releé con `get_brand_onboarding` al retomar una sesión o cuando la persona diga que cargó algo en la app. Después de cada escritura no hace falta: `update_brand_onboarding` ya devuelve `inventory` y `next[]` al día.

### 3. Elegir el modo

```
¿Hay una carpeta, una lista de archivos o un volcado grande de material en la conversación?
├── Sí → carga masiva: leé `instructions/carga_masiva.md` y seguila.
│        Cuando termine, lo que quede en `next[]` sigue en modo conversado.
└── No → conversado (paso 4).
```

### 4. Modo conversado

Andá por `next[]` en orden, **una cosa por vez**, con la `question` literal. Cada ítem dice dónde se guarda: `field` o `list` (con `use`, la action que corresponde), o una `action` cuando lo que sigue no es una pregunta (reintentar un audio sin transcribir, confirmar lo leído de Instagram, cerrar). Es el mismo copy de la app, no lo reescribas. Sumá el `why` en una línea solo cuando el pedido es raro (pedir piezas que *no* son la marca, pedir reseñas malas).

- **Guardá en el momento** con `update_brand_onboarding`, una respuesta por llamada. Si la sesión se corta, lo dicho ya quedó.
- **Aceptá lo incompleto.** Ocho reseñas en vez de veinte se guardan; el inventario dirá `incompleto` y está bien. No retengas una respuesta esperando que se complete.
- **"Ninguno" y "no tenemos esto" son respuestas.** En identidad, assets y material escrito es `set_flag` (`brand.identity_none`, `assets.assets_none`, `voice.written_none`); en un campo de texto se guarda lo que dijeron ("Ninguno"). Vacío a propósito no es lo mismo que sin responder, y el inventario los distingue. No insistas. La única excepción es decir la consecuencia una vez cuando es una compuerta: sin fotos de producto no se puede mostrar el producto.
- **Para sumar, `mode: "append"`**. `replace` solo cuando la persona pide reemplazar: borra lo que había, que pudo cargarse desde la app.
- **La tienda se pide temprano.** Con la URL, `run_brand_onboarding_action` → `connect_store`, y mirá el `status` que vuelve. `connected`: trajo el catálogo y las fotos de producto, y `products[]` ya sirve para matchear mecanismos y SKUs. `importing`: seguí con otra cosa y consultá después con `get_brand_onboarding` (`state.store.import`). `needs_authorization` (Tiendanube): pasale la `authorize_url` a la persona para que la abra en su browser; vos no podés. `saved_unknown_platform`: la URL queda guardada sin catálogo; decilo y pedí las fotos por otro lado. `failed` o `invalid_url`: decí el error tal cual. La tienda **no trae reseñas**: se piden igual.
- **Audios**: ver `instructions/carga_masiva.md`, sección Audios. En claude.ai, sin shell, un audio se graba en la app (`onboarding.url`).
- **Mecanismos**: uno alcanza si todos los productos funcionan igual; si hay otro que funciona distinto, otro `add_mechanism`. Mandá `product_id` solo cuando el nombre coincide sin ambigüedad con uno de `products[]`; si no, omitilo y matchea el server.
- **Qué puede tocar la IA** (`set_asset_freedom`): mostrá las seis opciones juntas con sus valores por defecto y mandá lo que la persona contestó. No lo marques como respondido por tu cuenta: viajan literales al generador como restricciones duras.
- **SKUs prioritarios: máximo 3.** Si dicen "todos", pedí tres: "todos" no es una prioridad.
- **Métrica de una ganadora**: opcional a propósito. Si no la tienen, se carga sin métrica. Lo que sí preguntás es si fue orgánica o paga (`winner_organic` / `winner_paid`): mezclarlas contamina el análisis.
- Links (posts de Instagram o TikTok, Drive, Figma) van con `add_file` y `source: { url }`. Se guardan como link, no se bajan.

### 5. Instagram es opt-in

Guardar el handle (`brand.instagram`) no autoriza a leer la cuenta. `read_instagram` **solo** si la persona lo pidió o aceptó explícitamente. Ofrecelo una vez, en el cierre y solo si quedan huecos: "¿Querés que además lea tu Instagram para completar huecos?". Sin un sí, no se llama.

Cuando la lectura esté `ready` (se ve con `get_brand_onboarding`), mostrale la bio y los captions que trajo y preguntá si se usan; recién ahí `confirm_instagram` con `use: true` o `false`. Lo leído nunca reemplaza lo cargado: si subieron 6 piezas y el feed tiene 200, las 6 son la verdad. Hay una lectura cada 24 horas por workspace.

### 6. Cierre

Mostrá el inventario que vuelve en `inventory`, una línea por dimensión: `state`, qué falta (`reason`) y cómo se resuelve (`fix_hint`). Después el veredicto, con su frase literal (`verdict_text` y, si hay pendientes, `verdict_detail`). **Son compuertas, no porcentajes**: nunca digas "vas 70%". Solo Assets y Mecanismo frenan la producción; todo lo demás sale con el pendiente marcado.

`complete` **solo cuando la persona dice que terminó**. "Por ahora está", "después sigo" o un silencio no son terminar: dejale `onboarding.url` para volver cuando quiera, acá o en la app. `complete` le avisa al equipo de Indash, por eso no se dispara de más.

Después de `complete`, el handoff: lo que sigue es el brief del período, con `content-brief`. Si además van a producir piezas desde una carpeta en Claude Code y todavía no existe, `new-client` la arma.

## Según dónde corras

```
¿Tenés shell y los archivos están en disco? (Claude Code, Cowork)
├── Sí → `create_onboarding_uploads` + `curl --upload-file` + `add_file` / `add_audio`
└── No (claude.ai)
    ├── Es un link → `add_file` con `source: { url }`
    ├── Es un archivo de hasta 3 MB cuyos bytes tenés de verdad → `source: { base64, mime_type, filename }`
    └── Todo lo demás → pasale `onboarding.url` para que lo suba en la app, y seguí con lo que sí se puede conversar
```

Una imagen adjunta al chat que solo ves no la podés codificar. No la reconstruyas ni la describas en su lugar: va por la app.

## Relación con `new-client`

Son independientes y ninguna exige a la otra. `new-client` arma la **carpeta local** para producir desde Claude Code y escribe un `CLAUDE.md` analizando el sitio. Esta carga en **Indash** lo que sabe el cliente. Ese `CLAUDE.md` es derivado: sirve para ubicar el workspace, nunca como fuente de un campo.

## Costos

Nada de esto consume créditos: ni leer, ni escribir, ni subir archivos, ni transcribir, ni conectar la tienda. Decilo si preguntan. Los únicos topes son de uso: minutos de transcripción por día y una lectura de Instagram cada 24 horas. Si salta uno, decilo y ofrecé la alternativa (escribirlo, o la app).

## Reglas no-negociables

1. **Siempre** aplicás el gate del conector `indash` y verificás que estén las cuatro tools. Sin ellas no hay onboarding por acá.
2. **Siempre** arrancás con `get_brand_onboarding` e `include_guide: true`, antes de preguntarle nada a la persona.
3. **Nunca** preguntás algo que ya está cargado.
4. **Nunca** escribís en un campo algo que la persona no dijo, pegó, subió o aprobó explícitamente en esta conversación. Lo extraído se muestra entero y espera su OK.
5. **Nunca** corregís, resumís ni mejorás el material. Las reseñas van con sus errores de tipeo.
6. **Nunca** pedís adjetivos ni síntesis. Pedís material.
7. **Siempre** pedís "esto no somos".
8. **Siempre** aceptás lo incompleto y el "ninguno", y no insistís.
9. **Nunca** subís una carpeta sin mostrar antes la tabla de clasificación y recibir un OK.
10. **Nunca** llamás `read_instagram` sin un sí explícito, ni `confirm_instagram` sin haber mostrado lo leído.
11. **Nunca** llamás `complete` sin que la persona diga que terminó.
12. **Siempre** cerrás con el inventario y el veredicto literal, sin porcentajes, y con el handoff a `content-brief`.
13. Con la persona, español rioplatense, directo, sin emojis y sin relleno. Una pregunta por mensaje.

## Punto de entrada

Cuando pidan cargar la marca, hacer el onboarding o subir material de un cliente, **arrancá por el paso 1** y llamá a `get_brand_onboarding` antes de preguntar nada.
