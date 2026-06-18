# Ejemplo BAD — Multi-instance packshot en un solo shot (NO hacer esto)

Caso real reportado por el usuario: ad de butaca de auto Baby Trend Hybrid 3 en 1, donde se intentó mostrar **el mismo producto en sus 3 configuraciones (arnés bebé / booster con respaldar / booster sin respaldar) alineadas en un único packshot top-down de 5 segundos**, generado por Kling/Seedance.

El resto del paquete estaba bien: identidad de la mamá clara, framing y lighting específicos, audio desglosado, prompt bajo el cap de 2500 chars. **El error era arquitectónico, no de redacción.**

---

## El intento (Shot 2 del prompt original)

```
Shot 2 (5-10s): Cut to overhead packshot — same Midnight Grey Baby Trend Hybrid booster on a soft beige flat-weave rug, but now in three configurations side by side: left = same booster with the 5-point harness installed (infant-toddler mode); center = high-back booster with harness removed, headrest attached (matches first frame configuration); right = low-back booster with the headrest detached, only the bottom seat cushion remaining. Same charcoal gray fabric on all three units. Locked top-down camera, slight 2cm push-in over the 5 seconds.
```

> ❌ El prompt es claro y específico, pero le pide al modelo algo que **no puede entregar consistente**: tres instancias del MISMO producto, simultáneamente en frame, con tela y geometría idénticas pero con configuraciones distintas.

## Qué salió en el video real

Las 3 unidades **no eran el mismo producto en 3 estados** — eran **3 butacas de modelos distintos**:
- Izquierda: butaca genérica con soporte ISOFIX, otro fabricante.
- Centro: la Baby Trend Hybrid real (con quilted fabric, logo "babytrend" visible, color correcto).
- Derecha: booster sin respaldar de otro modelo, otra textura, otro color.

Resultado: el packshot **no comunica "3 en 1"**. Comunica "3 butacas de marcas distintas". Destruye el ángulo creativo del ad.

## Por qué falla — explicación técnica

1. **Element Consistency en Kling 3.0 / Seedance / Veo 3.1 está pensada para UN sujeto principal** (una persona, un producto). No para N instancias del mismo objeto.
2. **Los modelos generativos de video no "copian" un objeto** — cada región de píxeles se sintetiza desde cero según el prompt y el ruido inicial. Sin un anclaje visual por instancia, cada copia se interpreta de forma independiente y deriva.
3. **Una sola imagen de referencia (first frame) no alcanza** porque el first frame muestra UNA configuración, no las tres. Cuando el modelo cortea al packshot (Shot 2), no tiene anclaje visual de las otras 2 configuraciones — las inventa.
4. **Pedirle a Nano Banana las 3 configs en una sola imagen tiene el mismo problema.** Los modelos de imagen tampoco mantienen consistencia de N instancias del mismo objeto en una sola generación.

## Approach correcto — 3 patrones que sí funcionan

### Patrón A — 3 mini-clips de Kling, uno por configuración (recomendado para ads)
- Generar **3 imágenes de Nano Banana**, una por configuración (cada una con su own setting top-down, mismo lighting y misma alfombra para coherencia visual).
- Generar **3 mini-clips de Kling de ~1.5s cada uno** (push-in suave, single-shot), uno por imagen.
- Pegar los 3 clips en edición con corte seco o quick-wipe (~4.5s totales + 0.5s de transiciones = 5s).
- **Ventaja:** consistencia perfecta de cada config; cada clip ancla su producto específico.
- **Costo extra:** 2 generaciones más de Nano Banana + 2 mini-clips Kling. Pero es la única vía con resultado predecible.

### Patrón B — 3 imágenes Nano Banana montadas en CapCut como secuencia
- Generar las mismas 3 imágenes top-down (sin clips de video).
- Montaje en CapCut/Premiere como sucesión de imágenes con micro-zoom (Ken Burns) y cortes de 1.5s cada una.
- **Ventaja:** más barato (sin generación de video para Shot 2); funciona si el ritmo del ad permite estética de "carrusel".
- **Desventaja:** se pierde el feeling de "video continuo"; lee más a "presentación" que a UGC.

### Patrón C — collage físico-real en Nano Banana (avanzado)
- Generar UNA imagen de Nano Banana de un **collage** o **lineup posado** donde el prompt describa explícitamente "three different units" (no "same booster in three configurations") y se asuma que serán visualmente distintos. Tratarlo como packshot publicitario, no como "3 estados del mismo producto".
- **Cuándo usarlo:** si el cliente acepta que las 3 unidades se vean parecidas pero no idénticas (ej: catálogo de variantes de color).
- **Cuándo NO usarlo:** cuando el ángulo creativo depende de "es la misma butaca, mirá cómo se transforma" — falla por definición.

---

## Resumen — por qué este output es malo

1. **Pidió consistencia inter-instancia que el modelo no puede entregar.** El prompt era específico y bien escrito, pero la tarea era estructuralmente imposible para un solo shot.
2. **El "case imposible" no se anticipó.** El skill tiene una sección para esto en `analysis.md` (kling vs veo, "caso imposible"), pero no cubría multi-instance packshots. Ahora sí.
3. **Las "notas de riesgo" mencionaban el problema, pero como riesgo, no como bloqueo.** Cuando un riesgo es ~100% certero, no es riesgo — es decisión arquitectónica fallada. El skill ahora exige flag explícito al usuario antes de generar.

**Regla derivada (en `instructions/analysis.md` y `eval/quality_checklist.md`):**
> Si el plan requiere mostrar el mismo producto en N estados/configuraciones simultáneamente en un mismo shot, partir el shot en N inserts separados. Cada uno con su propio first frame (Nano Banana) y su propio mini-clip. Avisar al usuario de este plan ANTES de generar.
