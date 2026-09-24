# Self-check — New Client

Corré este checklist antes del handoff. Si algo falla, corregilo. No entregues con ítems en rojo sin decírselo a la persona.

## Workspace y gate

- [ ] El conector `indash` estaba conectado y tenía las cuatro tools de onboarding. No cargué la marca por otro camino.
- [ ] Nombré el workspace en una línea antes de la primera escritura, y es el de esta marca.
- [ ] Si la marca no existía en Indash, frené y dije que el workspace lo crea Indash en la app. No inventé uno ni cargué en otro.

## Procedencia

- [ ] Arranqué con `get_brand_onboarding` e `include_guide: true`, y no pregunté nada que ya estaba en `state`.
- [ ] Cada texto que escribí lo dijo, pegó, subió o aprobó la persona en esta conversación. Lo extraído de un material largo se mostró entero y esperó un OK que lo nombraba.
- [ ] No corregí, resumí ni mejoré nada. Las reseñas fueron con sus errores.
- [ ] No pedí adjetivos ni descripciones: pedí piezas, reseñas y capturas. Pedí "esto no somos".
- [ ] Acepté lo incompleto y el "ninguno" sin insistir (`set_flag` donde corresponde).
- [ ] No mandé `meta`, `id`, `source_id`, `updated_at` ni `origin`.

## Carga masiva (si hubo carpeta)

- [ ] Inventarié por contenido y tipo real, no por nombre de archivo.
- [ ] Mostré una sola tabla archivo → lista → por qué, con las dudas como pregunta, y recibí un OK a la tabla entera antes de subir.
- [ ] Subí en lotes de hasta 20 con `create_onboarding_uploads` + `curl --fail`, y registré con `add_file` (`source: { upload_id, filename }`) solo los que subieron bien.
- [ ] Leí `results[]` uno por uno; reintenté solo los que fallaron.
- [ ] Los audios fueron con `add_audio` y un `save_to` que la persona me dijo, no que adiviné.
- [ ] Los textos extraídos (capturas, PDFs, transcripciones) fueron aparte, enteros, y cada uno con su OK.

## Tienda, Instagram, cierre

- [ ] Pedí la tienda temprano y actué según el `status` que volvió (`authorize_url` a la persona si fue `needs_authorization`).
- [ ] `read_instagram` solo con un sí explícito; `confirm_instagram` solo después de mostrar lo leído.
- [ ] Mostré el inventario por dimensión y el veredicto literal, sin porcentajes.
- [ ] `complete` solo si la persona dijo que terminó.

## Análisis

- [ ] Ofrecí `analyze_brand` solo con `inventory.verdict` en `can_start` o `can_start_with_pending`, explicando que nace pendiente y que el agente de briefs no lo ve sin confirmación.
- [ ] Si la tool no estaba en el conector, salteé el paso y lo dije. Si fue `not_enough_material`, dije qué falta y no insistí.
- [ ] Mostré `summary_markdown` tal cual y pregunté rama por rama. No confirmé ni rechacé nada por mi cuenta, ni edité lo derivado.
- [ ] `confirm_brand_analysis` con las decisiones de la persona, en una sola llamada; las ramas sin decisión quedaron `pending` y lo dije.

## Carpeta local (solo si la pidieron)

- [ ] La pregunté una vez y la creé solo con un sí.
- [ ] Slug en kebab-case; no pisé una carpeta existente sin avisar; estructura igual a `templates/folder_structure.md`, con `.gitkeep`.
- [ ] `CLAUDE.md`, `brand.md`, `brand-kit.md` e `index.md` salen de `get_brand_context` + `get_brand_kit` + `list_products`. Nada del sitio, nada inferido, nada del análisis que siga `pending` o `rejected`.
- [ ] Cada placeholder dice qué falta y que se carga en el onboarding.
- [ ] Logos y fuentes en `assets/logos/` y `assets/fonts/`; brand book en `assets/brand-kit/`. Nada mezclado, nada inventado.
- [ ] No cargué nada del `CLAUDE.md` al onboarding.

## Handoff

- [ ] Dije dónde quedó (`onboarding.url`), el veredicto literal, el estado de cada rama del análisis y los pendientes con nombre.
- [ ] Un handoff concreto: `content-brief` con un pedido de ejemplo, o la skill de ejecución que corresponda.
- [ ] Rioplatense, sin emojis, sin relleno. Una pregunta por mensaje.

Si todo está en verde (o los rojos están explicados como pendientes para la persona) → entregá.
