# Composición de texto y gráfica — por CAPAS

Texto + imagen son **una sola composición**, no dos capas que se ignoran. En
Studio la posición del texto no se le pide al modelo: se decide en el
manifiesto (`anchor` + márgenes + `below`/`gap`) y la escena se genera PARA
esa decisión (Ley 5 de `../reference/prompt-craft.md`).

La pregunta que separa una pieza diseñada de una perezosa: **¿esta pieza sería
distinta si moviera el texto, lo cambiara de tamaño o le diera otro
tratamiento al fondo?** Si la respuesta es "no", la composición es un template.

## 6 placements (elegí uno por pieza, variá entre piezas hermanas)

Cada placement es una combinación de `anchor` + márgenes. Los márgenes
respetan SIEMPRE las safe zones del formato (`../data/safe-zones.json`).

1. **Cabezal** — `anchor: "top"` + `marginTop` ≥ safe zone superior. Cuando el
   producto domina la mitad inferior y hay aire arriba para anunciar. Tamaño:
   1/4 a 1/3 del alto.
2. **Pie** — `anchor: "bottom"` + `marginBottom` ≥ safe zone inferior. Cuando
   la imagen tiene vacío natural abajo (mesa limpia, fondo desenfocado) y
   querés cerrar. Tamaño: 1/5 a 1/4 del alto.
3. **Centro sobre escena** — `anchor: "center"`. La imagen es fondo escénico y
   el texto es el sujeto (hooks fuertes, números crudos). Peso bold dominante,
   1/3 del alto. **Requisito**: la zona detrás necesita tratamiento (scrim o
   escena calma pedida en el prompt).
4. **Desplazado** — anchor lateral (`left`/`right`) o esquina. Texto
   "anotación" que no compite con un sujeto fuerte centrado. Peso regular,
   chico. En 9:16 hay poco ancho: preferí desplazamiento vertical antes que
   lateral.
5. **Profundidad con cutout** — el truco de tres capas: escena ai-gen abajo,
   capa `text` en el medio, **cutout del producto** (`remove_background`)
   arriba. El producto se superpone parcialmente al texto y la pieza gana
   profundidad real, con el texto igual de nítido. Funciona con productos de
   silueta sólida.
6. **Doble peso** — dos capas `text` alineadas (la segunda con `below` + `gap`):
   la palabra clave grande y bold, el descriptor a ~60% del tamaño en peso
   regular. Para copy con golpe + complemento (*"Hierro fundido." / "Sin
   curado."*). Si igualás los pesos, el efecto se cae.

### Variación entre piezas hermanas (secuencias y carruseles)

1. **No repitas el mismo placement en piezas consecutivas.**
2. 3 piezas → 3 placements distintos. 4-6 piezas → podés repetir uno, nunca
   más de 2 iguales y nunca consecutivas.
3. **La pieza de CTA lleva el texto arriba/centro** dejando el pie libre (en
   story, para el sticker de link). Esta es la única regla rígida.
4. La familia tipográfica y el color se mantienen — la variación va en
   posición y tamaño, no en estilo.

## Contraste: 5 tratamientos (en orden de preferencia)

El contraste se resuelve mirando **la zona específica** donde vive el texto,
no el promedio de la imagen.

- **A. Escena calma pedida en el prompt** — la mejor: la zona del texto ya
  sale lisa/desenfocada/oscura porque la pediste (Ley 5). Gratis y natural.
- **B. Scrim degradé** — capa `rect` con `gradient` de transparente a color
  (negro para texto claro), en la zona del texto:
  ```json
  { "id": "scrim", "type": "rect", "anchor": "bottom", "height": "45%",
    "gradient": { "direction": "vertical", "stops": [
      { "offset": 0, "color": "#00000000" }, { "offset": 1, "color": "#000000cc" } ] } }
  ```
  Sutil: si el scrim se nota como overlay, está fuerte. Ajustar el alpha del
  stop final es gratis (no gasta candidato).
- **C. Bloque / letterbox** — `rect` sólido del color de marca detrás del
  texto (con `cornerRadius` para pill, o de borde a borde para letterbox
  editorial). Fuerte y gráfico; no lo uses en todas las piezas de una
  secuencia o parece template.
- **D. Grade/vignette pedidos en el prompt** — *"zona superior en sombra
  natural suave"*, *"vignette sutil que oscurece los bordes"*. Más orgánico
  que un scrim, pero cuesta un candidato si no salió de entrada.
- **E. Sin tratamiento** — cuando el fondo de esa zona ya es ≥80%
  monocromático y contrasta. No agregues scrims por reflejo.

## Densidad de diseño (que la pieza no quede "virgen de diseño")

Una pieza "objeto flotando + título" repetida N veces se ve sin diseñar. Cada
pieza de desarrollo lleva al menos **un dispositivo** que explique el mensaje
sin leer — y en Studio, casi todos son CAPAS:

| Dispositivo | Cómo se arma |
|---|---|
| Dato destacado | Número grande como capa `text` bold + descriptor con `below` |
| Pill / badge | `rect` con `cornerRadius` + capa `text` encima |
| Comparación lado a lado | Dos mitades: `rect` de fondo por lado + textos; o dos zonas pedidas en la escena |
| Indicador de progreso (carrusel) | Capa `text` chica (`2/5`) o `rect`s finitos, mismo lugar en todos los slides |
| Zoom de detalle del producto | Candidato aparte de la capa ai-gen (crop/detalle) o segunda capa `image` |
| Diagrama / iconografía | Lo ÚNICO que puede justificar generarlo: gráfica orgánica dentro de la imagen, SIN labels legibles (los labels van como capas `text` encima) |

Sistema gráfico recurrente entre piezas hermanas (da cohesión): headline
bicolor en dos capas o dos pesos (el grueso en neutro + la palabra clave en el
color de acento de la marca), brand mark chico y consistente (capa `image`
SVG, `recolor` si hay que invertirlo), mismo tratamiento de fondo. **Una
secuencia = un template (claro U oscuro)** — no alternes mundo claro y oscuro
entre piezas.

## Anti-patrones

1. **Placement clonado** — N piezas con el texto en el mismo lugar, tamaño y
   color. Template de Canva.
2. **Texto flotando random** — sin relación con la composición de la escena
   (titular arriba a la derecha, producto abajo a la izquierda).
3. **Contraste inexistente** — blanco hueso sobre fondo hueso. El color del
   texto se decide mirando la zona real, y se corrige con capas (gratis).
4. **Texto tapando el producto** — el titular sobre la etiqueta o el detalle
   distintivo. La capa se mueve; el detalle no.
5. **Todo al mismo tamaño y peso** — sin jerarquía entre golpe y descriptor.
6. **Texto en safe zone** — tapado por la UI al publicar. Bloquea (paso 7).
7. **Tratamiento exagerado** — scrim al 70% que mata la imagen, bloque que
   aplasta. El tratamiento empuja el texto, no aplasta la escena.
8. **Pieza sin dispositivo** — solo texto sobre fondo liso, repetido.

## Checklist al componer las capas de texto

- [ ] ¿Qué placement elegí y por qué encaja con ESTA pieza?
- [ ] ¿Es distinto del placement de la pieza hermana anterior?
- [ ] ¿Hay contraste real en esa zona específica? Si no, ¿qué tratamiento (A-E)?
- [ ] ¿La jerarquía está en las capas (tamaños/pesos distintos)?
- [ ] ¿Todo dentro de las safe zones del formato?
- [ ] ¿El texto no tapa marca, etiqueta ni detalle clave del producto?
- [ ] ¿La pieza tiene al menos un dispositivo de diseño (si es de desarrollo)?
- [ ] ¿El sistema gráfico es consistente con las piezas hermanas?
