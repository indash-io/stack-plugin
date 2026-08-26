# Template — Plan de edición por segundos

Formato exacto del plan de edición. Es el corazón del entregable: se lee en 30
segundos y le dice a cualquiera qué se ve en cada momento.

Cómo *pensarlo*: `instructions/04_edit_concept.md`. Cómo elegir duraciones:
`style/pacing.md`.

---

## Estructura

```markdown
## Plan de edición — [Nombre de la pieza]

**Formato**: 9:16 · 1080×1920 · **Duración**: 12.0s · **Destino**: Instagram Reels
**Composición**: `data-composition-id="main"` · `data-duration="12"`

### Cortes

| # | Timecode | Dur. | Material | `data-media-start` | Función | Texto on-screen | Audio |
|---|---|---|---|---|---|---|---|
| 1 | 0.0 – 2.0 | 2.0s | `shot-01.mp4` | 2.2 | **HOOK** — [qué se ve] | "[texto, ≤8 palabras]" | música 0.8 |
| 2 | 2.0 – 5.0 | 3.0s | `shot-02.mp4` | 0.0 | Desarrollo — [qué se ve] | "[texto]" | música 0.20 + VO 1.0 |
| 3 | 5.0 – 7.5 | 2.5s | `shot-03.mp4` | 1.4 | Desarrollo — [qué se ve] | — | ídem |
| 4 | 7.5 – 9.8 | 2.3s | `shot-04.mp4` | 0.0 | **PAYOFF** — [qué se ve] | "[texto]" | ídem |
| 5 | 9.8 – 12.0 | 2.2s | `packshot.png` | — | **CTA** — packshot + logo | "[verbo + acción]" | música 0.6 |

### Seams (transiciones)

| Seam | Timecode | Tipo | Duración | Rol |
|---|---|---|---|---|
| 1 → 2 | 2.0 | `transitions-push` | 0.30s | primaria |
| 2 → 3 | 5.0 | corte seco | — | el beat carga la continuidad |
| 3 → 4 | 7.5 | `transitions-push` | 0.30s | primaria |
| 4 → 5 | 9.8 | `flash-through-white` | 0.25s | **acento** — entra el payoff |

### Curva de audio

| Tramo | `music.mp3` | `vo.wav` | Nota |
|---|---|---|---|
| 0.0 – 2.0 | 0.80 | — | entra con el hook |
| 2.0 – 9.8 | 0.20 | 1.00 | la música baja bajo la voz |
| 9.8 – 12.0 | 0.60 | — | sube en el CTA |

### Movimiento interno

| Corte | Movimiento | Params |
|---|---|---|
| 5 | push-in lento sobre el packshot | `scale 1.00 → 1.06`, `ease: none`, 2.2s |

### Zona segura ([formato])

- Texto entre `y = [límite superior]px` y `y = [límite inferior]px`
- Márgenes laterales: `x = [izq]px` / `[der]px` ([razón: rail de acciones])

### Material que queda afuera

| Archivo | Por qué |
|---|---|
| `shot-05.mp4` | Repite el ángulo del corte 3 sin agregar información |
```

---

## Reglas del plan

1. **La suma de las duraciones = `data-duration` del root.** Exacto, sin
   redondeos escondidos.
2. **Ningún `data-duration` supera la duración real del archivo** (la que
   medisteis con `ffprobe` en Discovery).
3. **Los timecodes son absolutos y continuos**: el corte N+1 arranca donde
   termina el N (los overlaps de transición se declaran en la tabla de seams, no
   se descuentan de las duraciones).
4. **El corte 1 es el hook** y su texto está visible desde el frame 1.
5. **Cada corte declara su función.** Si una función es "relleno", el corte no
   va.
6. **Una transición primaria + un acento como máximo.**
7. **Los textos on-screen van entre comillas y literales**, tal como van a
   aparecer. Nada de "un texto sobre el beneficio".
8. **`data-media-start` explícito** en cada clip que no arranque en su segundo 0.
9. **La columna de audio no puede quedar vacía.** "Sin audio" es una decisión
   válida y se escribe.

---

## Variante: pieza sin voz (solo música + texto)

Sacá la columna de VO de la curva de audio y asegurate de que cada bloque tenga
su texto: **una pieza para feed se mira sin sonido**, y sin texto no comunica
nada.

## Variante: pieza en dos formatos

Un solo plan de cortes (el corte es el mismo) + una tabla por formato con lo que
cambia:

```markdown
### Deltas por formato

| Elemento | 9:16 (1080×1920) | 4:5 (1080×1350) |
|---|---|---|
| Corte 2, encuadre | `object-position: center 40%` | `object-position: center` |
| Rail de captions | `bottom: 420px` | `bottom: 200px` |
| Tamaño del hook | 110px | 78px |
```
