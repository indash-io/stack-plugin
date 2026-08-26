# 04 — Edit concept (el plan de edición por segundos)

El plan de edición es **el entregable intelectual** de esta skill. La
composición HTML es su traducción mecánica. Si el plan es flojo, ninguna
transición lo salva.

Usá `templates/edit_plan.md` como formato exacto. Este archivo te dice **cómo
pensarlo**.

---

## 1. El hook manda (primeros 1-3 segundos)

Regla no negociable 5 del `SKILL.md`. En el primer segundo alguien decide si
sigue mirando.

**El primer corte tiene que mostrar:**
- el momento de mayor contraste visual del material, o
- el producto en su plano más deseable, o
- la tensión que el resto de la pieza resuelve.

**Nunca:**
- ❌ un logo (el logo va al final, no al principio)
- ❌ un fundido desde negro
- ❌ un plano de establecimiento lento "para contextualizar"
- ❌ un caption que explica lo que todavía no se vio

**Y el texto del hook aparece en el frame 1**, no a los 0.8s. Si el texto entra
con animación, la animación arranca en `0` y dura ≤ 0.4s.

Truco de corte: si el mejor frame del clip está a los 2.5s, no esperes — usá
`data-media-start="2.2"` y entrá casi en el momento. El material crudo casi
nunca empieza en su mejor frame.

---

## 2. Estructura por bloques

| Bloque | Función | % de la duración | Regla |
|---|---|---|---|
| **Hook** | Frenar el scroll | 10–20% | 1 solo corte. Nunca dos. |
| **Desarrollo** | Mostrar el producto / el beneficio | 45–60% | 2–4 cortes, cada uno con **una** idea |
| **Payoff** | El resultado, el "ahá" | 15–20% | El plano más satisfactorio del material |
| **CTA** | Qué hacer ahora | 12–20% | Packshot + verbo + logo. Nunca poético. |

Sobre una pieza de 12s:

```
[0.0 – 2.0]  HOOK        corte 1
[2.0 – 5.0]  DESARROLLO  corte 2
[5.0 – 7.5]  DESARROLLO  corte 3
[7.5 – 9.8]  PAYOFF      corte 4
[9.8 – 12.0] CTA         corte 5
```

Si te sobran cortes para llenar el tiempo, **la pieza es demasiado larga**. Bajá
la duración antes de meter relleno.

---

## 3. Un corte = una idea

Cada corte responde a: **¿qué entiende el que mira, que no entendía antes de
este corte?** Si la respuesta es "nada nuevo", el corte no va.

Anti-patrón clásico: tres cortes seguidos del producto girando desde ángulos
distintos. Eso es un solo corte con tres variantes, no tres ideas. Ver
`examples/bad/slideshow_sin_ritmo.md`.

---

## 4. Ritmo: la duración de cada corte

Detalle completo en `style/pacing.md`. Lo mínimo:

- Ningún corte baja de **0.6s** (abajo de eso no se lee, se percibe como flash).
- Ningún corte de contenido pasa de **4s** en una pieza corta: si necesita más,
  partilo o metele movimiento interno (un push-in lento con GSAP).
- **Variá** la duración. Cinco cortes de 2.4s exactos suenan a metrónomo.
  Alterná: 2.0 / 3.0 / 2.5 / 2.3 / 2.2.
- El corte del CTA es el más largo de la cola: necesita tiempo de lectura
  (mínimo 1.5s, ideal 2.0-2.5s).

---

## 5. Texto on-screen: uno por bloque

- **Máximo un bloque de texto principal visible a la vez.** Dos textos
  compitiendo = ninguno se lee.
- Máximo **6-8 palabras** por bloque de texto.
- Cada texto entra con el corte, no a mitad de camino, y sale antes del corte
  siguiente (0.2-0.3s de aire).
- Específico o nada: *"Se absorbe en 30 segundos"* ✅ · *"Descubrí la
  diferencia"* ❌.
- Sin emojis, salvo pedido explícito del user.
- **Todo dentro de la zona segura** de la plataforma → `style/safe_zones.md`.

---

## 6. Audio: la curva, no solo los archivos

El plan declara **qué se escucha en cada tramo**, no solo qué archivos hay:

| Tramo | Música | VO / nativo | Nota |
|---|---|---|---|
| 0.0–2.0 | 0.8 | — | Entra fuerte con el hook |
| 2.0–9.8 | 0.20 | VO a 1.0 | La música baja bajo la voz |
| 9.8–12.0 | 0.6 | — | Sube de nuevo en el CTA |

En HyperFrames eso se implementa con `data-volume` estático por clip de audio, o
con `data-automation` (envolventes) si necesitás una rampa. Si vas a partir la
música en tramos con volúmenes distintos, son **varios `<audio>` con
`data-media-start`** consecutivos, no uno solo.

Regla de oro: **si hay voz, todo lo demás baja.** Una cama de música arriba de
0.3 con VO encima tapa la voz.

---

## 7. Transiciones en el plan

En el plan, cada **seam** (junta entre dos cortes) declara su transición:

```
corte 1 → corte 2 : transitions-push, 0.3s   [primaria]
corte 2 → corte 3 : corte seco
corte 3 → corte 4 : transitions-push, 0.3s   [primaria]
corte 4 → corte 5 : flash-through-white, 0.25s  [ACENTO — el payoff]
```

Una primaria + un acento. **Un corte seco es una decisión válida y elegante**
cuando hay algo que carga la continuidad (un match cut, una forma compartida, el
beat de la música).

---

## 8. Antes de pasar a la composición: la pasada de honestidad

Releé el plan y contestá:

1. ¿El primer segundo aguanta solo, sin contexto?
2. ¿Hay algún corte que no aporte una idea nueva?
3. ¿Alguna duración es igual a la de al lado (metrónomo)?
4. ¿Algún texto se solapa con otro?
5. ¿La suma de las duraciones da **exactamente** el `data-duration` del root?
6. ¿Algún `data-duration` de clip supera la duración real medida del archivo?
7. ¿El CTA dice qué hacer, con un verbo?

Si alguna da mal, corregí el plan **acá** — es infinitamente más barato que
corregirlo en el HTML.

---

## Salida de este paso

El plan de edición completo, con el formato de `templates/edit_plan.md`:
timecodes, material por corte, función, texto on-screen, transición por seam y
curva de audio.

→ Pasá a `instructions/05_composition.md`.
