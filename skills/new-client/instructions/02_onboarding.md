# 02 — El onboarding de marca

Acá se carga la marca en Indash. El orden es **leer → elegir el modo → cargar → cierre**. La regla de procedencia del `SKILL.md` aplica a cada escritura de este paso.

---

## 1. Leer antes de preguntar

Llamá `get_brand_onboarding` con `include_guide: true` y leé la guía entera: trae los 6 pasos con la pregunta literal de cada campo (el copy de la app), qué acepta cada uno y con qué cambio se guarda.

- **Nunca preguntes algo que ya está en `state`.** El onboarding se completa una vez; repreguntar le dice al cliente que lo que cargó no sirvió. Retomá por `next[]`.
- Un texto con `truncated: true` está cargado completo; el recorte es de la respuesta. No es un hueco.
- `onboarding.completed_at` con fecha quiere decir que ya lo cerraron. Sigue vivo: se puede sumar material. No vuelvas a llamar `complete`.
- `state.analysis` dice si ya hay un análisis y en qué status están sus ramas. Si hay uno `pending`, aparece en `next[]`: se resuelve en `04_analisis.md`, no acá.
- Contale a la persona en dos o tres líneas qué hay y qué falta, y seguí. Sin `exists`, arrancás de cero con `next[]` completo.
- Releé con `get_brand_onboarding` al retomar una sesión o cuando la persona diga que cargó algo en la app. Después de cada escritura no hace falta: `update_brand_onboarding` ya devuelve `inventory` y `next[]` al día.

---

## 2. Elegir el modo

```
¿Hay una carpeta, una lista de archivos o un volcado grande de material en la conversación?
├── Sí → carga masiva: leé `03_carga_masiva.md` y seguila entera.
│        Cuando termine, lo que quede en `next[]` sigue en modo conversado (abajo).
└── No → conversado.
```

Si la persona dice "el cliente me mandó todo" y todavía no pasó nada, pedile la carpeta o los archivos antes de arrancar a preguntar. Un archivo a la vez que llega por el chat también es material: se guarda en el momento (ver *Según dónde corras*).

---

## 3. Material, no adjetivos

Si pedís una descripción, te devuelven adjetivos ("cercano, fresco, premium"), que son los mismos para todas las marcas. Por eso:

- **Nunca** "describí tu tono" → pedí los posts y captions que ya publicaron.
- **Nunca** "¿quién es tu cliente?" ni "¿cuáles son las objeciones?" → pedí las reseñas tal cual están y las capturas de los mensajes que ya les aburre contestar.
- **El mecanismo es por qué funciona, no qué logra.** El cliente casi nunca sabe qué es "un mecanismo": no uses la palabra sola. Preguntá qué tiene adentro el producto y por qué eso hace lo que hace, y mostrá el par:
  - No sirve: "Hidrata en profundidad y repara la barrera cutánea."
  - Sirve: "Tiene ceramidas iguales a las que tu piel ya fabrica, así que la barrera las reconoce y las usa en vez de rechazarlas."

  Si contestan con un resultado, guardalo igual (es lo que dijeron) y preguntá **una vez** más. Sin mecanismo las piezas solo pueden afirmar, no explicar.
- **"Esto no somos" se pide siempre**, con el mismo peso que "esto somos": piezas propias que no los representan o de otras marcas a las que no quieren parecerse (`origin: "other_brand"`). Es lo que más pesa al generar y lo que nadie pide: el borde define tanto como el centro.
- Si quien carga es de Indash, pedile el original del cliente (el mensaje reenviado, el audio) antes que su resumen de lo que dijo el cliente. Si solo tiene el resumen, se guarda.

---

## 4. Modo conversado

Andá por `next[]` en orden, **una cosa por vez**, con la `question` literal. Cada ítem dice dónde se guarda: `field` o `list` (con `use`, la action que corresponde), o una `action` cuando lo que sigue no es una pregunta (reintentar un audio sin transcribir, confirmar lo leído de Instagram, cerrar). Es el mismo copy de la app, no lo reescribas. Sumá el `why` en una línea solo cuando el pedido es raro (pedir piezas que *no* son la marca, pedir reseñas malas).

- **Guardá en el momento** con `update_brand_onboarding`, una respuesta por llamada. Si la sesión se corta, lo dicho ya quedó.
- **Aceptá lo incompleto.** Ocho reseñas en vez de veinte se guardan; el inventario dirá `incompleto` y está bien. No retengas una respuesta esperando que se complete.
- **"Ninguno" y "no tenemos esto" son respuestas.** En identidad, assets y material escrito es `set_flag` (`brand.identity_none`, `assets.assets_none`, `voice.written_none`); en un campo de texto se guarda lo que dijeron ("Ninguno"). Vacío a propósito no es lo mismo que sin responder, y el inventario los distingue. No insistas. La única excepción es decir la consecuencia una vez cuando es una compuerta: sin fotos de producto no se puede mostrar el producto.
- **Para sumar, `mode: "append"`**. `replace` solo cuando la persona pide reemplazar: borra lo que había, que pudo cargarse desde la app.
- **Mecanismos**: uno alcanza si todos los productos funcionan igual; si hay otro que funciona distinto, otro `add_mechanism`. Mandá `product_id` solo cuando el nombre coincide sin ambigüedad con uno de `products[]`; si no, omitilo y matchea el server.
- **Qué puede tocar la IA** (`set_asset_freedom`): mostrá las seis opciones juntas con sus valores por defecto y mandá lo que la persona contestó. No lo marques como respondido por tu cuenta: viajan literales al generador como restricciones duras.
- **SKUs prioritarios: máximo 3.** Si dicen "todos", pedí tres: "todos" no es una prioridad.
- **Lanzamientos**: `add_launch` con la fecha solo si la dijeron. No se adivina.
- **Métrica de una ganadora**: opcional a propósito. Si no la tienen, se carga sin métrica. Lo que sí preguntás es si fue orgánica o paga (`winner_organic` / `winner_paid`): mezclarlas contamina el análisis.
- Links (posts de Instagram o TikTok, Drive, Figma) van con `add_file` y `source: { url }`. Se guardan como link, no se bajan.
- **Audios**: `03_carga_masiva.md`, sección Audios. En claude.ai, sin shell, un audio se graba en la app (`onboarding.url`).

---

## 5. La tienda, temprano

Con la URL, `run_brand_onboarding_action` → `connect_store`, y mirá el `status` que vuelve:

| `status` | Qué hacés |
|---|---|
| `connected` | Trajo el catálogo y las fotos de producto (`imported`, `updated`). `products[]` ya sirve para matchear mecanismos y SKUs. |
| `importing` | Catálogo grande. Seguí con otra cosa y consultá después con `get_brand_onboarding` (`state.store.import`). Más de 15 minutos sin terminar se da por caído: decilo. |
| `needs_authorization` | Tiendanube sin autorizar. Pasale la `authorize_url` para que la abra en su browser con su sesión de Indash; vos no podés. Al volver, la app importa sola. |
| `saved_unknown_platform` | La URL queda guardada sin catálogo. Decilo y pedí las fotos de producto por otro lado. |
| `failed` / `invalid_url` | Decí el error tal cual (`error_code` y el mensaje). No reintentes solo. |

La tienda **no trae reseñas**: se piden igual. `disconnect_store` solo si la persona lo pide.

---

## 6. Instagram es opt-in

Guardar el handle (`brand.instagram`) no autoriza a leer la cuenta. `read_instagram` **solo** si la persona lo pidió o aceptó explícitamente. Ofrecelo una vez, en el cierre y solo si quedan huecos: "¿Querés que además lea tu Instagram para completar huecos?". Sin un sí, no se llama. Si vuelve `blocked`, decí el `reason` (`no_handle`, o `rate_limited` con `retry_at`).

Cuando la lectura esté `ready` (se ve con `get_brand_onboarding`, `state.instagram`), mostrale la bio y los captions que trajo y preguntá si se usan; recién ahí `confirm_instagram` con `use: true` o `false`. Lo leído nunca reemplaza lo cargado: si subieron 6 piezas y el feed tiene 200, las 6 son la verdad. Hay una lectura cada 24 horas por workspace.

---

## 7. Cierre

Mostrá el inventario que vuelve en `inventory`, una línea por dimensión: `state`, qué falta (`reason`) y cómo se resuelve (`fix_hint`). Después el veredicto, con su frase literal (`verdict_text` y, si hay pendientes, `verdict_detail`). **Son compuertas, no porcentajes**: nunca digas "vas 70%". Solo Assets y Mecanismo frenan la producción; todo lo demás sale con el pendiente marcado.

`complete` **solo cuando la persona dice que terminó**. "Por ahora está", "después sigo" o un silencio no son terminar: dejale `onboarding.url` para volver cuando quiera, acá o en la app. `complete` le avisa al equipo de Indash, por eso no se dispara de más. Devuelve `pending[]` con lo obligatorio que falta: decilo en una línea.

El análisis (`04_analisis.md`) no necesita `complete`: necesita material. Si el inventario ya está en `can_start` o `can_start_with_pending`, pasá al análisis aunque la persona quiera seguir cargando después.

---

## Según dónde corras

```
¿Tenés shell y los archivos están en disco? (Claude Code, Cowork)
├── Sí → `create_onboarding_uploads` + `curl --upload-file` + `add_file` / `add_audio` (detalle en `03_carga_masiva.md`)
└── No (claude.ai)
    ├── Es un link → `add_file` con `source: { url }`
    ├── Es un archivo de hasta 3 MB cuyos bytes tenés de verdad → `source: { base64, mime_type, filename }`
    └── Todo lo demás → pasale `onboarding.url` para que lo suba en la app, y seguí con lo que sí se puede conversar
```

Una imagen adjunta al chat que solo ves no la podés codificar. No la reconstruyas ni la describas en su lugar: va por la app.
