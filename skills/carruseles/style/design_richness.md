# Style — Riqueza visual (design density)

Un carrusel **no es un objeto flotante con un título encima**. Eso se ve "virgen de diseño" y plano. Cada slide debe tener **densidad de diseño**: un sistema visual reconocible + un elemento gráfico que *explique* el mensaje, no que solo lo decore.

Esta guía complementa `visual_modes.md` (Minimalista vs Lifestyle). Aplica a **ambos modos**, pero pesa más en carruseles **conceptuales / educativos / de servicio** (sin un producto físico hero), donde el diseño gráfico ES el contenido.

---

## El principio

> Cada slide responde: **¿qué elemento visual hace que entienda el mensaje sin leer?**

Si la respuesta es "ninguno, solo hay texto sobre un fondo", falta diseño. Sumá uno de los **dispositivos de diseño** de abajo.

---

## Dispositivos de diseño (elegí al menos 1 por slide)

1. **Mockup de dispositivo** — un teléfono / pantalla / tarjeta mostrando una UI real del contexto (un listing de marketplace, un post de IG, un dashboard, una galería de producto). Es lo que más "aterriza" el mensaje en e-commerce.
2. **Diagrama con conectores** — cajas/nodos unidos por líneas con glow (hub-and-spoke, flujo, jerarquía, "antes → después"). Ideal para explicar relaciones o sistemas (ver ref "Inventario + Listings + Precios").
3. **Hub central + ramas** — un sujeto central (producto, ícono, símbolo) conectado por líneas de neón a varios elementos satélite con label (ver ref favorita "Mismo producto en 3 canales").
4. **Line-icons con label** — íconos lineales (neón sobre oscuro / negros finos en círculo sobre claro), cada uno rotulado. Para listas de features, canales, pasos.
5. **Render 3D / isométrico** — escena tridimensional con profundidad y glow (hub tech, pods de plataforma). El más "premium", úsalo en hooks de impacto.
6. **Data viz** — gráfico de línea/barra, medidor, contador, rating de estrellas. Para datos, métricas, prueba social.
7. **Comparación lado a lado** — "esto sí / esto no", "antes / después", débil vs fuerte.

---

## Sistema gráfico recurrente (lo que da cohesión de marca)

Aplicá estos elementos de forma consistente entre slides para que el carrusel se sienta diseñado y on-brand:

- **Headline bicolor en 2 líneas**: el grueso en blanco (mundo oscuro) o negro (mundo claro) + **la palabra clave en color de acento** (cian #00FFE5 en oscuro, azul Tech #022AFD en claro). Tipografía de marca, bold, grande (25-35% del alto).
- **Subhead corto** debajo, en peso regular, con 1-2 palabras en color de acento.
- **Indicador de progreso**: barra numerada arriba (`1/7`, `4/7`) en el template claro, o **dots** centrados abajo en el template oscuro.
- **Brand mark** (símbolo) chico anclado en una esquina en slides internos; lockup completo en el CTA.
- **Acento gráfico**: subrayado/ístick de color bajo el headline, o una línea fina divisoria.
- **Textura de fondo** sutil en el mundo oscuro: globo de partículas / patrón de puntos en una esquina, glow radial detrás del sujeto.
- **Cápsulas / pills y tarjetas con borde fino** para labels, métricas y nodos de diagrama.

---

## Dos templates (derivados de las refs de marca)

### Template OSCURO / Tech (default para conceptual/tech/dolor→solución)
- Fondo `#001137` → negro, con globo de partículas sutil en una esquina y glow radial.
- Line-icons y diagramas en **neón cian/azul** con glow.
- Headline blanco + acento cian. Dots de progreso abajo.
- Mockups con marco de neón.

### Template CLARO / Editorial (para educativo "x/7", listicles limpios)
- Fondo Nieve `#F6F7F8`.
- Headline negro bold + palabra clave en azul Tech, con subrayado azul.
- **Line-icons negros finos dentro de círculos** delgados; ilustración line-art (estilo calculadora con íconos orbitando).
- Barra de progreso `x/7` arriba con tramo en azul Tech.

**Un carrusel = un template.** No mezclar claro y oscuro entre slides (igual que un modo visual).

---

## Reglas de densidad

1. **Ningún slide es solo texto sobre fondo liso.** Siempre hay un dispositivo de diseño que explica el mensaje.
2. **Los mockups muestran UI del contexto real** (listing, post, dashboard), no cuadros vacíos. Para texto interno de los mockups, usá **líneas placeholder** (no intentes texto legible diminuto: sale gibberish). El texto legible se reserva para headline, labels y números.
3. **Consistencia del sistema gráfico** entre slides: mismo template, misma familia de íconos, mismo tratamiento de headline bicolor, mismo indicador de progreso.
4. **Variación del dispositivo** entre slides: no repitas el mismo mockup 5 veces; alterná mockup / diagrama / data viz / line-icons.
5. **El acento de color marca jerarquía**, no decora: resaltá la palabra que carga el significado.
6. Para estos carruseles ricos en gráfica y texto, **gpt-image** suele rendir mejor (íconos, diagramas, labels legibles). Ver `instructions/07_generation.md`.

---

## Anti-patrones (lo que se ve "virgen de diseño")

- ❌ Un ícono/objeto centrado flotando + título arriba, repetido en los 5 slides.
- ❌ Headline monocromo sin palabra de acento.
- ❌ Cero mockups, cero diagramas, cero line-icons.
- ❌ Sin indicador de progreso.
- ❌ Fondo liso sin textura ni glow ni profundidad.
- ❌ Mismo layout exacto en todos los slides (sin variación de dispositivo ni de posición).
