# Style — Ritmo

El ritmo es lo que separa una pieza editada de un slideshow. No sale de una
fórmula, pero tiene reglas que casi nunca conviene romper.

---

## 1. El hook: primeros 1-3 segundos

Es la regla más importante de esta skill y no es negociable.

| Plataforma | Ventana real de decisión |
|---|---|
| TikTok / Reels / Shorts | ~1.0-1.5s |
| Feed de Instagram (4:5) | ~1.5-2.0s (el scroll es más lento) |
| Meta ads | ~1.5s, y compite con todo el feed |
| YouTube pre-roll | ~3s (hasta el botón de skip) |

Qué tiene que pasar en esa ventana:

- **Algo se mueve o cambia.** Un plano estático de 1.5s es una foto.
- **El sujeto ya está en cuadro.** No hay tiempo de "llegar" a él.
- **El texto del hook está visible desde el frame 1** (si entra animado, la
  animación arranca en `0` y dura ≤ 0.4s).

Qué **no** puede pasar:

- ❌ fundido desde negro
- ❌ logo de apertura
- ❌ plano de establecimiento "para contextualizar"
- ❌ el mejor frame del clip llegando a los 2.5s — entrá con
  `data-media-start` casi encima de él

---

## 2. Duración de corte

| | Mínimo | Sweet spot | Máximo |
|---|---|---|---|
| Corte de contenido, pieza ≤15s | 0.6s | **1.8–3.0s** | 4.0s |
| Corte de contenido, pieza 20-45s | 0.8s | **2.5–4.0s** | 6.0s |
| Corte de CTA (cierre) | 1.5s | **2.0–2.5s** | 3.5s |
| Flash / insert de acento | 0.3s | 0.4s | 0.6s |

- **Abajo de 0.6s** el ojo no lee el contenido, solo percibe un destello. Es
  válido como acento deliberado, nunca como corte de información.
- **Arriba de 4s** en pieza corta hay que justificarlo con movimiento interno
  (un push-in lento, un caption que evoluciona). Si el plano no cambia en 4
  segundos, el plano terminó a los 2.

---

## 3. Variá las duraciones

Cinco cortes de 2.4s exactos suenan a metrónomo y se sienten robóticos.

- ❌ `2.4 / 2.4 / 2.4 / 2.4 / 2.4`
- ✅ `2.0 / 3.0 / 2.5 / 2.3 / 2.2`

Una regla práctica: **ningún corte dura exactamente lo mismo que su vecino.**
Diferencia mínima de 0.2s.

**La aceleración funciona.** Cortes que se acortan progresivamente hacia el
payoff generan tensión:

```
3.0 → 2.6 → 2.0 → 1.4 → [PAYOFF 2.5] → [CTA 2.5]
```

---

## 4. Reparto por bloques

| Duración total | Hook | Desarrollo | Payoff | CTA | Cortes totales |
|---|---|---|---|---|---|
| 6s (ad corto) | 1.2s | 2.5s | 1.0s | 1.3s | 3–4 |
| 10s (ad estándar) | 1.8s | 4.5s | 1.7s | 2.0s | 4–5 |
| 12s (reel) | 2.0s | 5.5s | 2.2s | 2.3s | 5 |
| 20s | 2.5s | 10.5s | 3.5s | 3.5s | 6–8 |
| 30s (brand film corto) | 3.0s | 17.0s | 5.0s | 5.0s | 8–11 |

**Si te sobran cortes para llenar el tiempo, la pieza es demasiado larga.** Bajá
la duración antes de meter relleno. Un ad de 8s impecable rinde más que uno de
15s con tres cortes de más.

---

## 5. El ritmo lo manda la música (cuando hay)

Si hay una cama musical con pulso claro, **cortá en el beat**. Un corte a
contratiempo se siente mal aunque nadie sepa explicar por qué.

```bash
npx hyperframes beats --json    # { ok, file, count, bpm }
```

Con el BPM sacás la grilla: a 120 BPM el beat cae cada 0.5s, el compás cada 2.0s.
Cortes cada 2 o 4 beats leen como intencionales. Si el material no da para caer
justo, es preferible **estirar o achicar 0.1-0.2s** un corte que quedar a
contratiempo.

Si no hay música con pulso, el ritmo lo manda el contenido y esta sección no
aplica.

---

## 6. Movimiento dentro del corte

Un clip generado suele tener su propio movimiento de cámara. Cuando **no** lo
tiene (una imagen fija, un packshot), metele movimiento con GSAP:

- **Push-in lento**: `scale` de 1.0 → 1.06 durante todo el corte, `ease:
  "none"`. Casi imperceptible y evita que la imagen se sienta muerta.
- **Pan lateral**: `x` de 0 → -40px en un plano más ancho que el cuadro.
- **Parallax**: producto y fondo a velocidades distintas, si están separados.

Regla: **un movimiento por corte**. Un push-in + un pan + una rotación al mismo
tiempo se lee como plantilla de banco de imágenes.

Y ojo: el movimiento tiene que ser **seekable** (una tween de GSAP en el
timeline registrado), nunca una animación de reloj de pared. Ver
`instructions/05_composition.md` §5.

---

## 7. Aire

- Entre que un texto sale y entra el siguiente: **0.2-0.3s** de aire. Sin eso
  parece un teleprompter.
- El último corte no termina en el frame exacto en que muere el audio: dejá
  0.2-0.4s de cola para que el cierre respire.
- Un corte seco después de una transición marcada da descanso. **No todos los
  seams necesitan efecto.**

---

## 8. Anti-patrones de ritmo

| Anti-patrón | Por qué falla | Fix |
|---|---|---|
| Metrónomo (todos los cortes iguales) | Se siente automatizado | Variá ≥0.2s entre vecinos |
| Slideshow (planos fijos consecutivos) | No es video, son fotos con música | Movimiento interno o cortes más cortos |
| Hook lento | Se pierde antes de empezar | El mejor frame en el segundo 1 |
| CTA de 0.8s | Nadie llega a leerlo | Mínimo 1.5s, ideal 2.0-2.5s |
| Tres variantes del mismo plano seguidas | Es un corte, no tres | Fusionalos o sacá dos |
| Transición distinta en cada seam | Caos, no diseño | Una primaria + un acento |
| Todo el material adentro | La pieza se estira sin razón | Lo que no aporta, afuera |

Casos desarrollados en `examples/bad/slideshow_sin_ritmo.md`.
