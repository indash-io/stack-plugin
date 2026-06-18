# Snowball — TACoS vs Revenue (charts vacíos)

**Marca**: Snowball Partners (agencia / growth partner ecommerce — NO ecommerce, sin producto físico)
**Categoría**: servicio / agencia (carrusel y estáticos conceptuales)
**Formato**: estática 4:5 (1080×1350)
**Tipo**: ❌ bad
**Modelo**: gpt-image

## Qué falla (concreto)
- **Los "charts" son flechas de clip-art, no data-viz.** Cada gráfico es una sola flecha (roja subiendo / azul plana) dentro de una caja con grid casi vacío. Lee a PowerPoint 2010, no a dashboard premium. La marca es tech/SaaS: los datos tienen que verse como datos (línea con varios nodos, ejes, valores, glow neón fino), no como una flecha decorativa.
- **Demasiado aire muerto.** Dos cajas enormes con grid vacío ocupan media pieza sin información. El vacío no es "minimal premium", es desbalance: ni dato, ni texto, ni gráfica que llene.
- **Las dos cajas compiten y aplanan la jerarquía.** Al ser dos recuadros gemelos del mismo peso, el ojo no sabe qué mirar; el contraste del concepto (sube vs. no sube) se diluye en vez de golpear.
- **El símbolo de marca está mal.** Es un círculo azul con un punto blanco, no las dos circunferencias superpuestas con la lente blanca en la intersección. (Problema general de estas piezas: el logo es interpretado por el modelo, no el asset real — ver abajo.)
- **El botón dibujado dentro de la imagen** ("Quiero mi diagnóstico") en un ad de Meta es redundante con el CTA nativo y ocupa espacio que podría llevar el dato.

## Qué evitar / qué hacer en su lugar
- **Nunca representes una métrica con una sola flecha.** Si el concepto es "TACoS sube, Revenue no", dibujá **un solo gráfico combinado** con dos líneas (TACoS rojo subiendo, Revenue azul plano) sobre los mismos ejes → el contraste se ve en un golpe, sin duplicar cajas ni dejar grids vacíos. O reemplazá las flechas por líneas neón con 5–7 nodos, valores y eje.
- **Llená el cuadro con densidad de diseño** (ver `style/` y la guía de design-richness del carrusel): números grandes, delta %, etiquetas, glow fino. Si sobra espacio, falta diseño.
- **Logo real en post, no generado.** gpt-image reinterpreta el símbolo. Para la versión final, componé el PNG del brand kit por encima (overlay con margen), no se lo pidas al modelo.
- **En ads de Meta, omití el botón dentro de la imagen** (o hacelo muy secundario): el CTA real es el nativo de la plataforma.

## Por qué quedó así
Generada con gpt-image describiendo "dos line charts lado a lado". El modelo resolvió cada chart con una flecha sola sobre grid vacío → look pobre. El prompt pedía data-viz pero no exigía nodos/ejes/valores ni prohibía representar la serie con una sola flecha. Lección para el prompt: especificar **línea con N nodos + ejes + valores**, idealmente **un gráfico combinado** en vez de dos cajas, y reservar el espacio para densidad, no para grid vacío.
