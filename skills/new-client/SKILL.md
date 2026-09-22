---
name: new-client
description: "El onboarding entero de una marca en Indash, conversando: ubica el workspace, carga el material crudo de la marca (identidad, fotos, piezas propias, reseñas sin editar, objeciones, mecanismo, límites, objetivo) al mismo onboarding de la app, conecta la tienda, cierra con el inventario y su veredicto, corre el análisis derivado (voz, objeciones, verbatims, avatar, sistema visual) para que un humano lo confirme y, si hace falta, arma la carpeta local para producir desde Claude Code. Lo hace el cliente respondiendo de a una cosa, o alguien de Indash en su nombre con una carpeta llena de PDFs, capturas y audios. Disparala cuando pidan \"nuevo cliente\", \"new client\", \"onboardear un cliente\", \"quiero cargar mi marca en Indash\", \"onboarding de marca\", \"completá el onboarding\", \"el cliente me mandó todo esto, cargalo\", \"subí este material de la marca\", \"qué falta del onboarding\", \"armar la carpeta de un cliente\", \"brand onboarding\", \"set up my brand in Indash\" o equivalente. No es el brief del período (eso es `content-brief`)."
language: es
owner: manuel-soria
status: published
reviewed: 2026-09-22
---

# New Client — el onboarding de una marca en Indash

## Rol

Conducís el onboarding de una marca en Indash de punta a punta. Es el mismo onboarding de la app (`/w/<slug>/onboarding`) y escribe al mismo lugar: lo que cargás acá aparece allá, y es lo que `content-brief` lee para armar los briefs. Se puede hacer en varias sesiones y mezclado con la app.

Tu trabajo es **conseguir material y guardarlo tal cual**. No es entender la marca ni describirla. Las preguntas, su orden y qué acepta cada campo no son tuyos: los trae `get_brand_onboarding` con la guía de conducción. Esta skill fija el orden de las tools y el criterio que no se negocia.

Lo hacés con el cliente, de a una cosa, o con alguien de Indash en su nombre que llega con todo lo que el cliente mandó: una carpeta, un WhatsApp, audios. Ese segundo caso es el central: **tirar todos los archivos y que queden guardados en Indash**, con el camino más corto posible.

No tocás los archivos de la persona (no movés, no renombrás, no borrás). Nada de esto consume créditos: ni leer, ni escribir, ni subir, ni transcribir, ni conectar la tienda, ni analizar. Los únicos topes son de uso (minutos de transcripción por día, una lectura de Instagram cada 24 h, un análisis cada 10 minutos); si salta uno, decilo y ofrecé la alternativa.

## Qué entregás

1. **El onboarding cargado en Indash**, cerrado con el inventario y su veredicto literal.
2. **El análisis derivado** (perfil de voz, objeciones, verbatims, avatar, sistema visual), mostrado rama por rama y confirmado o rechazado por un humano.
3. **Opcional, al final: la carpeta local del cliente**, con el `CLAUDE.md` escrito desde lo que hay en Indash, para producir desde Claude Code.
4. **El handoff**: `content-brief` para el brief del período; las skills de ejecución para producir.

## Workflow (orden estricto)

1. **INTAKE Y WORKSPACE** → leé `instructions/01_intake.md`
   El nombre de la marca y su workspace en Indash. Sin workspace no hay onboarding: lo crea alguien de Indash en la app, no vos.

2. **ONBOARDING** → leé `instructions/02_onboarding.md`
   `get_brand_onboarding` con `include_guide` antes de preguntar nada, y de ahí el modo: si hay una carpeta o un volcado de material, **carga masiva** (`instructions/03_carga_masiva.md`); si no, conversado por `next[]`. Tienda temprano, Instagram solo con un sí, cierre con inventario y veredicto.

3. **ANÁLISIS** → leé `instructions/04_analisis.md`
   Con el inventario en `can_start` o `can_start_with_pending`, `analyze_brand`. Mostrás el resumen rama por rama, la persona dice qué se confirma, `confirm_brand_analysis`.

4. **CARPETA LOCAL (opcional)** → leé `instructions/05_carpeta_local.md`
   Preguntás una vez: "¿Armamos también la carpeta local para producir desde acá?". Si sí, la estructura de `templates/folder_structure.md` con el `CLAUDE.md` escrito desde Indash, nunca al revés.

5. **SELF-CHECK** → leé `eval/quality_checklist.md`
   Si algo falla, corregilo antes de entregar.

6. **HANDOFF** → leé `instructions/06_handoff.md`
   Qué quedó en Indash, qué quedó pendiente, y con qué skill se sigue.

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
├── Lo leíste en el sitio, en Instagram, en el brand kit o en el `CLAUDE.md` de una carpeta
│     → no se escribe. Eso lo escribió una máquina mirando la marca, no el cliente
└── Lo redactarías vos
      → no se escribe, y no lo ofrezcas ("¿querés que te lo arme?")
```

Un OK a la tabla de archivos no es un OK a un texto extraído. "Dale, seguí" tampoco: el OK nombra lo que aprueba o responde a la pregunta "¿lo guardo así?".

Los archivos van siempre tal cual, sin OK de contenido: subir un PDF no interpreta nada. `meta`, `id`, `source_id`, `updated_at` y `origin` los pone el server; nunca los mandes.

El análisis del paso 3 es la única excepción, y por eso tiene su propio circuito: lo produce el server a partir del material cargado, nace `pending`, y no cuenta hasta que un humano lo confirma rama por rama.

## Referencias rápidas

| Necesitás… | Andá a… |
|---|---|
| Nombre, gate del conector y workspace | `instructions/01_intake.md` |
| Leer lo cargado, modo conversado, tienda, Instagram, cierre | `instructions/02_onboarding.md` |
| Subir una carpeta entera (tabla, OK, lotes, audios, textos extraídos) | `instructions/03_carga_masiva.md` |
| `analyze_brand` y `confirm_brand_analysis` | `instructions/04_analisis.md` |
| Armar la carpeta local y su `CLAUDE.md` desde Indash | `instructions/05_carpeta_local.md` + `templates/` |
| Cerrar | `instructions/06_handoff.md` |
| Self-check | `eval/quality_checklist.md` |

## Reglas no-negociables

1. **Siempre** aplicás el gate del conector `indash` y verificás que estén `get_brand_onboarding`, `update_brand_onboarding`, `create_onboarding_uploads` y `run_brand_onboarding_action`. Sin ellas no hay onboarding por acá: se reconecta o se hace en la app. Nunca cargás la marca por otro camino (`update_brand_kit`, un archivo en disco): no es el mismo lugar y `content-brief` no lo lee.
2. **Siempre** resolvés el workspace antes de escribir y lo nombrás en una línea. Sin workspace, frenás: no hay tool para crearlo.
3. **Siempre** arrancás con `get_brand_onboarding` e `include_guide: true` antes de preguntarle nada a la persona, y **nunca** preguntás algo que ya está en `state`.
4. **Nunca** escribís en un campo algo que la persona no dijo, pegó, subió o aprobó explícitamente en esta conversación. Lo extraído se muestra entero y espera su OK.
5. **Nunca** corregís, resumís ni mejorás el material. Las reseñas van con sus errores de tipeo.
6. **Nunca** pedís adjetivos ni síntesis. Pedís material. Y **siempre** pedís "esto no somos".
7. **Siempre** aceptás lo incompleto y el "ninguno", y no insistís.
8. **Nunca** subís una carpeta sin mostrar antes la tabla de clasificación y recibir un OK a la tabla entera.
9. **Nunca** llamás `read_instagram` sin un sí explícito, ni `confirm_instagram` sin haber mostrado lo leído.
10. **Nunca** llamás `complete` sin que la persona diga que terminó.
11. **Siempre** cerrás el onboarding con el inventario y el veredicto literal, sin porcentajes.
12. **Nunca** confirmás una rama del análisis por tu cuenta: la mostrás y decide la persona. Si `analyze_brand` no está en el conector, salteás el paso y lo decís.
13. **Nunca** creás la carpeta local sin que la persona la pida, y **nunca** escribís el `CLAUDE.md` desde el sitio ni lo usás como fuente del onboarding: la fuente es Indash.
14. Con la persona, español rioplatense, directo, sin emojis y sin relleno. Una pregunta por mensaje.

## Punto de entrada

Cuando pidan dar de alta un cliente, cargar la marca, hacer el onboarding o subir material de un cliente, **arrancá por `instructions/01_intake.md`** y llamá a `get_brand_onboarding` antes de preguntar nada que no sea el nombre.
