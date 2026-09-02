# MALO — El slideshow con música

El anti-patrón más común de esta skill: el material está bien, la composición es
válida, `lint` y `check` pasan… y la pieza es una presentación con música.

Marca anonimizada. Categoría: apparel DTC.

---

## Lo que se entregó

```
[0.0 – 2.5]  shot-01.mp4   producto de frente
[2.5 – 5.0]  shot-02.mp4   producto de perfil
[5.0 – 7.5]  shot-03.mp4   producto de espaldas
[7.5 – 10.0] shot-04.mp4   producto en detalle
[10.0 – 12.5] shot-05.mp4  producto sobre mesa
[12.5 – 15.0] logo.png     logo centrado
```

Transición `transitions-dissolve` de 0.4s en **cada** seam. Música a `0.8` de
punta a punta. Cero texto on-screen.

---

## MALO #1 — Metrónomo: seis cortes de 2.5s exactos

Todos iguales. La pieza tiene el pulso de un reloj y se siente automatizada
desde el segundo 5.

**Fix**: ninguna duración igual a la de su vecina, diferencia mínima de 0.2s. Y
aceleración hacia el payoff: `2.4 / 2.0 / 1.6 / 2.8 [payoff] / 2.4 [CTA]`.

Ver `style/pacing.md` §3.

---

## MALO #2 — No hay hook, hay un catálogo

El corte 1 es "el producto de frente". No hay tensión, no hay número, no hay
nada que frenar el scroll. El primer segundo se puede resumir en "hay una
prenda".

**Fix**: el hook es el plano **más deseable o más raro** del material, con texto
específico visible desde el frame 1. Si el material no tiene un plano así, el
brief necesita otro plano — se frena y se pide, no se disimula.

Ver `instructions/04_edit_concept.md` §1.

---

## MALO #3 — Cinco variantes del mismo plano son un corte, no cinco

Frente, perfil, espalda, detalle, sobre la mesa: es **la misma idea** ("así es
la prenda") repetida cinco veces. Nadie entiende nada nuevo en el corte 4 que no
supiera en el 1.

**Fix**: un corte = una idea. Si hay cinco ángulos y una sola idea, entran dos
ángulos como máximo y la pieza dura 8 segundos, no 15.

---

## MALO #4 — La misma transición en todos los seams, y encima larga

`transitions-dissolve` de 0.4s × 5 seams = **2 segundos** de los 15 son fundido.
Un octavo de la pieza es transición. Y como todas son iguales, ninguna significa
nada.

**Fix**: una primaria (0.2–0.3s) en dos o tres seams, cortes secos en el resto,
y **un** acento donde algo cambia de verdad. Un corte seco es una decisión, no
una omisión.

Ver `reference/hyperframes.md` §1.4 — la doc lo dice textual: una transición
distinta en cada seam se lee como caos; la misma en todos, como plantilla.

---

## MALO #5 — El logo abre… perdón, cierra 2.5 segundos vacíos

El corte final es el logo solo, centrado, 2.5s. No dice qué hacer. No hay verbo,
no hay oferta, no hay dónde.

**Fix**: el CTA es packshot + **verbo + acción concreta** + logo chico. *"Pedilo
en el link"*, no un logo respirando.

---

## MALO #6 — Cero texto en una pieza para feed

El feed se mira **sin sonido**. Sin texto, esta pieza comunica exactamente
nada a la mayoría de quienes la ven.

**Fix**: 2-4 textos on-screen, uno por bloque, ≤8 palabras, dentro de zona
segura. Aunque no haya voz.

Ver `style/captions_typography.md` §5.

---

## MALO #7 — Todo el material adentro

Los cinco clips entraron porque existían. Nadie decidió qué **no** entra.

**Fix**: la tabla de material de Decisions tiene una columna "Entra" y una
sección "Queda afuera" con la razón. Editar es sacar.

---

## MALO #8 — Planos fijos sin movimiento interno

Tres de los cinco clips son casi estáticos. Son fotos con duración.

**Fix**: push-in lento con GSAP (`scale 1.00 → 1.05`, `ease: none`) sobre los
planos quietos. Un movimiento por corte, imperceptible pero vivo.

Ver `style/pacing.md` §6.

---

## MALO #9 — La música a 0.8 todo el tiempo

Sin curva. Sin que baje en ningún momento, sin que suba en el cierre. La pieza
suena plana aunque los cortes cambien.

**Fix**: curva de audio declarada en el plan. Aunque no haya voz: entrar fuerte
en el hook, bajar un poco en el desarrollo, subir en el payoff y el CTA.

---

## MALO #10 — Pasó `lint` y `check`, así que "está bien"

Los gates técnicos no evalúan si la pieza retiene. `lint` chequea el contrato,
`check` chequea layout y contraste. **Ninguno de los dos mira el ritmo.**

**Fix**: el `draft` existe para eso, y se mira con `eval/quality_checklist.md`
sección "Sobre el render" en la mano. Un render que pasa los gates y aburre es
un render que hay que rehacer.

---

## La versión arreglada, en una línea

De 15s con 6 cortes a **9s con 4 cortes**: hook con el detalle del tejido y el
texto "Tres capas, 340 gramos", dos ángulos (no cinco), push-in en el estático,
`transitions-push` en dos seams y corte seco en el otro, CTA de 2.3s con verbo.
Menos material, más pieza.
