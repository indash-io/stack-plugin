# 05 — Música, locución y SFX

Objetivo: tres stems en `assets/audio/` (`music.wav`, `vo.wav`, `sfx.wav`) calzados a la
grilla. El código que los genera va en `audio-src/`, así se pueden rehacer.

## 1. Música

```
¿Hay temas del cliente o licenciados?
├─ sí → beat_phase.py en cada uno
│       ├─ BPM = grilla (±0.5%)        → usalo tal cual, calzá la fase
│       ├─ BPM a ≤ 2% de la grilla     → --atempo en music_conform.py
│       └─ más lejos                   → descartalo, o reconstruí la grilla sobre su BPM
└─ no → score provisorio en la grilla, marcado como provisorio en la entrega
```

- **Elegir el tema**: mirá el mapa de compases. Las filas con ◀ son cambios de sección.
  El drop o estribillo tiene que poder caer en el giro, y el golpe final en el CTA. Entre
  varios candidatos, preferí un edit corto del compositor que ya termine solo.
- **Calzar**: offset = `t_golpe_final_en_el_tema − t_CTA_en_el_video`. Comprobá que con
  ese offset los beats del tema caigan en la grilla: `(fase + k·beat − offset)` tiene que
  ser múltiplo del beat del video.
- **Conformar**: `music_conform.py --seg v0:v1:t0`. Los empalmes se cortan en compás, con
  crossfade antes del downbeat. Los 30 ms de fade-in del frame 0 los pone el script
  (`reference/gotchas.md`).
- **El gag de espera**: si el problema es esperar, `--hold 0:<giro>` hace que el mismo
  tema suene por teléfono, se acelere con la tensión y frene en seco (tape-stop) en el
  giro. Ahí entra a rango completo.
- **Pieza calma** (salud, seguros, finanzas): bajá la agresividad (otro tema, `air_swell` en
  vez de `whoosh`) y mantené la cadencia.

## 2. Locución (si hay)

1. **Voces**: con la skill `locuciones`. Para acento mexicano, buscá "Mexican" o es-419:
   el filtro es-MX devuelve vacío. Generá 2–3 voces distintas del guion completo y en el
   workspace que se acordó en el intake.
2. **Una lectura continua por toma**: el guion entero de una vez. La prosodia sale mejor
   que línea por línea.
3. **Tramos**: corré `vo_fit.py segments TOMA.wav`, y transcribí con
   `npx hyperframes transcribe TOMA.wav -l es` para saber qué tramos forman cada línea.
4. **`lines.json`**: `{start, end}` de cada línea en la toma, y `target` = el corte de
   su escena.
5. **Calce**: `vo_fit.py fit --take … --lines … --duration … --out assets/audio/vo.wav`.
   Si alguna línea llega más de 0.35 s tarde, subí `--tempo` (máx 1.08), o recortá el
   guion o mové el corte.
6. **Verificación**: transcribí el `vo.wav` final y compará palabra por palabra con el guion.

La voz que no queda en Studio se entrega como alternativa: el mismo proyecto renderizado
con la otra toma (`draft-<x>-voz-b.mp4`).

## 3. SFX

- Un cue por evento visible, en el frame exacto del movimiento: la lista de tiempos del
  storyboard.
- `sfx.py list` muestra el catálogo con el uso de cada efecto. `impact` va una o dos
  veces por pieza; `boing`, como mucho dos.
- `sfx.py render cues.json --duration <D> --out assets/audio/sfx.wav`.

## 4. Mezcla

1. `mix.py duck --music … --vo assets/audio/vo.wav --db 8 --out assets/audio/music.wav`
   (9 dB si el tema es denso). Va después del calce de la voz.
2. En `index.html`, tres `<audio>` con `data-volume`. Para arrancar: voz 0.9, música
   0.75, SFX 0.55.
3. `mix.py measure --stem vo.wav:0.9 --stem music.wav:0.75 --stem sfx.wav:0.55` y ajustá
   los volúmenes hasta que diga OK, antes de renderizar.

Siguiente: `06_build.md`.
