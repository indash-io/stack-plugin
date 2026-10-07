# Energía — el piso, el gap y la caja de herramientas

## El piso (se mide en la contact sheet)

| Medida | Piso |
|---|---|
| Evento nuevo en pantalla | cada 0.25–0.5 s (beat o corchea) |
| Plano sin evento | nunca más de 1.5 s |
| Escena | 1.5–4 s |
| Pieza | 30–40 s; si sobra, se corta |
| Momentos "wow" | uno por tramo de la forma (hook, problema, giro, producto, CTA) |
| Transiciones | ninguna se repite dos veces seguidas |
| SFX | uno por evento visible |

## El gap que hubo que cerrar (indash v1 → v2)

| v1 ("lenta, aburrida") | v2 (la vara) |
|---|---|
| Planos de 4–12 s, pausas muertas de 1–2 s | Un evento cada 0.23–0.47 s |
| Cards chicas y oscuras, sin profundidad | Mundo 3D persistente que late con el kick |
| Dos momentos "wow" | Uno por escena |
| Siempre el mismo blur-fade | Slam, glitch, zoom-through, iris, chupar a un punto |
| El contenido real casi no se ve | El contenido real a pantalla completa, repartido como cartas |
| El problema, explicado | El problema, actuado como comedia con un remate por compás |
| 43 s | 35.5 s |

## La caja de herramientas

Los valores son los de las piezas aprobadas. Elegí por escena, no todo junto.

**Tipografía**
- **Slam**: la palabra entra en 0.2 s (`expo.out`) desde escala 1.4–1.8 con blur 16 → 0,
  y un split cromático en el acento de la marca (`text-shadow` 16 → 0 px en 0.32 s). Una
  palabra o frase corta por beat, a pantalla completa.
- **Shake del escenario** en el slam: 12–26 px, cuatro keyframes de 35 ms que decaen.
  Usá más amplitud cuanto más importante es el golpe.
- **Tachado en el beat** para lo que la marca no es ("Ni agencia. Ni software.").
- **Palabra clave** con subrayado o cursiva del acento, dibujado de izquierda a derecha.

**Objetos**
- **Repartir como cartas**: piezas reales que entran desde los bordes en corcheas, con
  rotación propia, y explotan hacia afuera (`power3.in`, 0.4 s) en el downbeat siguiente.
- **Contadores que corren** hasta el número del ledger, y aterrizan en un beat.
- **Pop-out de UI**: la pieza real sale del teléfono hacia la cámara y vuelve o se va.
- **Squash and stretch** en lo que aterriza: aplastarlo un 10–15% al tocar y que rebote.

**Cámara y transiciones**
- **Zoom-through**: la cámara atraviesa un objeto (la O del logo, una pantalla) hacia
  la escena siguiente.
- **Chupar a un punto**: todo converge a un punto, flash, y aparece la marca. Es el giro.
- **Iris**: un círculo que abre desde el último tap. Es la entrada al end card.
- **Signal glitch**: barras y desplazamiento de 2–3 frames en los cortes de sección.
  Solo si la marca es tech.
- **Flash frame** en un drop: 0.02 s de subida y 0.22 s de bajada. Uno o dos por pieza:
  más que eso lava el color de marca.

**Mundo**
- **Mundo 3D persistente** debajo de las escenas, que reacciona al kick (un piso de
  puntos, partículas en la paleta). Ver `reference/threejs.md`.
- **Capa de terminación**: grano sutil y viñeta. Scanlines solo si la marca es tech.

## Marca calma no es marca lenta

En la pieza de referencia (salud, público mayor) se mantuvo la cadencia y cambió el carácter:
- easings más redondos (`power3`, `back.out(1.4)`) en vez de `expo`;
- sin glitch ni flash;
- `air_swell` en vez de `whoosh`;
- un tema cálido en vez de uno de club.

La energía sale de cuántas cosas pasan, no de lo agresivo de cada una.

## El humor

El problema es donde la pieza se gana al que no sabe qué se vende:
- exageralo con objetos de la vida real (el cable, el pin, el inbox, la música de espera);
- un remate por compás, y el SFX como parte del chiste.

El producto, en cambio, se muestra en serio: pantalla real y dato concreto.
