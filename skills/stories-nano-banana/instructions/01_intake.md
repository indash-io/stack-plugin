# 01 — Intake

Primer paso del workflow. Acá validás que tenés todo lo necesario para empezar. **Si falta algo crítico, frenás acá y lo pedís. No avances sin input completo.**

---

## Inputs obligatorios

Para arrancar necesitás SÍ o SÍ:

1. **URL del producto** — un link a la página del producto en el e-commerce (Shopify, Tiendanube, web propia, etc.). De ahí scrapeás nombre, descripción, beneficios, target, precio.
2. **Imagen de referencia del producto** — la foto del producto que va a usarse como input en nano banana. Idealmente con la etiqueta/packaging visible, porque de ahí extraés tipografía y paleta.

Si **falta cualquiera** de los dos: pedilo y frená.

---

## Inputs opcionales

Estos son bienvenidos pero **no obligatorios**. Si el user los pasa, los respetás. Si no los pasa, vos decidís en `03_decisions.md`:

- **Cantidad de stories** (3-6, default 4)
- **Tipo de secuencia** (educativo / hot take / listicle / caso de estudio / storytelling / promo)
- **Estilo visual** (editorial / lifestyle / minimal / etc.)
- **Hook o ángulo específico** (ej: "quiero hablar de la duración del aroma")
- **Audiencia target** (si la URL no la deja clara)
- **Si va con persona o no** (default: vos decidís según el arquetipo)
- **Brand voice particular** (si la marca tiene tono establecido)
- **Stickers preferidos / vetados** (ej: "no usar polls, prefiero countdown")

---

## Cómo manejar entrada incompleta

### Caso 1: el user solo pasa una URL
Respondé con:

> Para arrancar necesito una imagen de referencia del producto (la foto que vas a pasar como input a nano banana). Idealmente con el packaging y la etiqueta visibles, porque de ahí saco la paleta y la tipografía. ¿Me la podés compartir?

Frená. No empieces el discovery.

### Caso 2: el user solo pasa una imagen
Respondé con:

> Necesito también la URL del producto. De ahí saco el nombre exacto, los beneficios y el target. ¿Me la pasás?

### Caso 3: el user pasa todo y aclara cosas opcionales (slides, tipo, etc.)
Avanzá directo al paso 2 (Discovery). Guardá los opcionales para usarlos en Decisions.

### Caso 4: la URL no carga / la imagen no es clara
- URL rota o sin acceso → pedí descripción manual del producto al user (qué es, beneficios, target, precio).
- Imagen borrosa / sin packaging → pedí una foto mejor antes de seguir. La paleta y tipografía dependen de eso.

---

## Cómo confirmar que entendiste el input

Antes de avanzar al Discovery, hacé un **acuse de recibo silencioso interno** (no se lo digas al user todavía). Verificá:

- [ ] Tengo URL accesible
- [ ] Tengo imagen de referencia clara
- [ ] Si el user pasó opcionales, los anoté
- [ ] No tengo dudas críticas que resolver antes de scrapear

Si todo OK → pasá a `02_discovery.md`. **Trabajás en silencio**, sin contarle al user los detalles del scrapeo. Solo le mostrás resultados cuando llegues a Decisions.

---

## Lo que NO hacés en Intake

- ❌ No pedís brand kit completo (eso lo extraés vos de la imagen).
- ❌ No pedís copy del cliente (eso lo escribís vos en Concept).
- ❌ No pedís múltiples imágenes (una sola alcanza).
- ❌ No hacés preguntas de tipo de carrusel todavía (eso es Decisions, después del Discovery).
- ❌ No empezás a generar nada hasta tener URL + imagen confirmadas.

---

## Tono al pedir input faltante

Directo, breve, una sola pregunta a la vez. Sin AI-speak.

- ✅ *"Necesito una imagen de referencia del producto. ¿Me la compartís?"*
- ❌ *"¡Hola! Soy tu asistente de carruseles. Para poder ayudarte mejor, ¿podrías por favor compartir conmigo la imagen del producto que te gustaría utilizar? 😊"*
