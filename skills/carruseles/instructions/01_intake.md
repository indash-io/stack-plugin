# 01 — Intake

Primer paso del workflow. Acá validás que tenés todo lo necesario para empezar. **Si falta algo crítico, frenás acá y lo pedís. No avances sin input completo.**

---

## Inputs obligatorios

Para arrancar necesitás SÍ o SÍ:

1. **URL del producto** — un link a la página del producto en el e-commerce (Shopify, Tiendanube, web propia, etc.). De ahí scrapeás nombre, descripción, beneficios, target, precio.
2. **Imagen de referencia del producto** — la foto del producto que va a usarse como input en nano banana. Idealmente con la etiqueta/packaging visible, porque de ahí extraés tipografía y paleta. **Esta primera imagen suele ser la frontal**.

Si **falta cualquiera** de los dos: pedilo y frená.

### Imágenes de referencia adicionales (cuando aplica)

**Regla de oro**: **un ángulo del producto = una imagen de referencia.** Sin la referencia de un ángulo, nano banana lo inventa y sale mal (ver `examples/bad/ai_generico.md` MALO #10).

En el **paso de Discovery + Concept** (silencioso), si el carrusel va a mostrar el producto desde **vistas distintas a la frontal**, tenés que pedir las imágenes correspondientes **ANTES de generar prompts**. Vistas que típicamente requieren referencia adicional:

- **Espalda / dorso** (apparel, electrónicos, packaging con info nutricional atrás)
- **Lateral** (productos con perfil distintivo, packaging tipo doypack/bolsa)
- **Interior** (apparel con forrería, productos abiertos, contenedores)
- **Macro de un detalle específico** (costuras, texturas, tipografía pequeña, sello, certificación)
- **Vista superior / cenital** (envases con tapa, packaging con layout en la tapa)
- **Producto abierto / en uso** (envases con bomba, cajas con producto adentro, pluma destapada)
- **Lifestyle real con persona usándolo** (si tenés UGC o lookbook con la modelo, sumalo — ayuda mucho a la consistencia del casting)

**Cuándo pedir las imágenes adicionales**:
- En el **Discovery** detectás qué ángulos pueden ser útiles según el arquetipo y la categoría.
- En la **propuesta consolidada de Decisions**, mencionás explícitamente *"para los slides X y Y voy a necesitar imágenes de [espalda / interior / macro], ¿las tenés?"*
- **Antes de generar prompts** validás que tenés todo. Si falta algo, **frená y pedilo**.

**Si el user solo tiene la imagen frontal y no más**:
- No avances con slides que muestren ángulos no disponibles.
- Reformulá el concept para que todos los slides usen vistas derivables de la frontal (3/4 frontal, macro de un detalle frontal, hero shot frontal en distintas escenas).
- Decile al user qué cambiaste y por qué.

---

## Inputs opcionales

Estos son bienvenidos pero **no obligatorios**. Si el user los pasa, los respetás. Si no los pasa, vos decidís en `03_decisions.md`:

- **Cantidad de slides** (3-7, default 4)
- **Tipo de carrusel** (educativo / hot take / listicle / caso de estudio / storytelling / promo)
- **Estilo visual** (editorial / lifestyle / minimal / etc.)
- **Hook o ángulo específico** (ej: "quiero hablar de la duración del aroma")
- **Audiencia target** (si la URL no la deja clara)
- **Si va con persona o no** (default: vos decidís según el arquetipo)
- **Brand voice particular** (si la marca tiene tono establecido)

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
- ❌ No hacés preguntas de tipo de carrusel todavía (eso es Decisions, después del Discovery).
- ❌ No empezás a generar nada hasta tener URL + imagen frontal confirmadas + cualquier imagen adicional necesaria para los ángulos que el carrusel va a mostrar.

## Lo que SÍ hacés en Intake / Discovery

- ✅ **Una imagen frontal alcanza para arrancar el Discovery**, pero no necesariamente para generar.
- ✅ Si en el Concept aparecen ángulos distintos al frontal, **pedís las imágenes adicionales** antes de generar prompts.
- ✅ Mejor pedir 1 imagen extra ahora que regenerar 5 prompts después.

---

## Tono al pedir input faltante

Directo, breve, una sola pregunta a la vez. Sin AI-speak.

- ✅ *"Necesito una imagen de referencia del producto. ¿Me la compartís?"*
- ❌ *"¡Hola! Soy tu asistente de carruseles. Para poder ayudarte mejor, ¿podrías por favor compartir conmigo la imagen del producto que te gustaría utilizar? 😊"*
