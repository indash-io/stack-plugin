# BUENO — UGC con captions, entregado en 4:5 y 9:16

Marca anonimizada. Categoría: suplementos DTC. Material: 1 clip UGC de
`video-clips` (persona hablando a cámara, audio nativo) + 2 inserts de
producto + packshot, todo en la carpeta del Workbench. Dos creativos del plan:
`stories/testimonio` (9:16) y `feed/testimonio-4x5` (4:5).

**Por qué es bueno**: los captions siguen el modelo rail + embed, el audio
nativo manda, el corte se autora primero en el formato más restrictivo, y el
segundo formato se deriva sin re-planificar.

---

## Brief de entrada

> "El video de la chica quedó bárbaro pero no se entiende nada sin sonido.
> Ponele subtítulos y armá la versión para feed y para reels."

## Discovery (silencioso)

| # | Archivo | Dur. real | Res. | Audio | Qué muestra |
|---|---|---|---|---|---|
| 1 | `ugc-01.mp4` | 18.0s | 1080×1920 | **sí** | Persona hablando a cámara, un solo sujeto |
| 2 | `insert-01.mp4` | 5.0s | 1080×1920 | no | Mano abriendo el frasco |
| 3 | `insert-02.mp4` | 4.0s | 1080×1920 | no | Cápsulas cayendo en la palma |
| 4 | `packshot.png` | — | 1080×1350 | — | Frasco frontal |

El clip 1 es de **un solo sujeto** y sin cortes duros: cumple el requisito
documentado para el flujo de captions embebidos de HyperFrames.

## Decisiones clave

1. **El audio nativo manda.** El VO ya está en el clip: `data-has-audio="true"`,
   sin `muted`, `data-volume="1"`. La música va a `0.12` — apenas presente.
2. **Transcripción local**, no a mano:
   ```bash
   npx hyperframes transcribe ./assets/ugc-01.mp4 --language es --to srt --output ./assets/ugc-01.srt
   ```
3. **Rail + un embed.** El rail lleva todo lo que se dice; una sola palabra —
   *"dos semanas"* — se promueve a embed en el clímax.
4. **9:16 primero.** Es el formato con la zona segura más chica; el 4:5 es
   otro creativo: se copia `composition/` a su carpeta y se deriva bajando el
   rail y achicando la escala tipográfica.

---

## Plan de edición

**Formato base**: 9:16 · 1080×1920 · **Duración**: 16.0s · **Destino**: Reels + feed 4:5

| # | Timecode | Dur. | Material | `data-media-start` | Función | Audio |
|---|---|---|---|---|---|---|
| 1 | 0.0 – 4.2 | 4.2s | `ugc-01.mp4` | 3.8 | **HOOK** — arranca en la frase fuerte | nativo 1.0 + música 0.12 |
| 2 | 4.2 – 6.0 | 1.8s | `insert-01.mp4` | 0.8 | Insert — abre el frasco | ídem (la voz sigue por debajo) |
| 3 | 6.0 – 11.4 | 5.4s | `ugc-01.mp4` | 9.2 | Desarrollo — el testimonio | ídem |
| 4 | 11.4 – 13.2 | 1.8s | `insert-02.mp4` | 0.5 | Insert — cápsulas en la palma | ídem |
| 5 | 13.2 – 16.0 | 2.8s | `packshot.png` | — | **CTA** — packshot + logo | música 0.5 |

**Captions**

| Bloque | Timecode | Tipo | Texto |
|---|---|---|---|
| rail-01 | 0.1 – 4.0 | rail | "Lo probé porque no me creía nada" |
| rail-02 | 4.3 – 5.9 | rail | "Una cápsula con el desayuno" |
| rail-03 | 6.1 – 9.8 | rail | "A los cuatro días ya dormía distinto" |
| **embed** | 9.9 – 11.3 | **embed** | **"DOS SEMANAS"** |
| rail-04 | 11.5 – 13.1 | rail | "Y ahí sí, el cambio se notaba" |
| cta | 13.4 – 16.0 | CTA | "Probalo 30 días" |

**Seams**: `transitions-dissolve` 0.2s en los cuatro (energía media, testimonio
continuo). Sin acento: el embed **es** el acento de esta pieza.

**Zona segura 9:16**: rail entre `y = 1180px` y `y = 1440px`; embed centrado
vertical en `y = 700–1000px`; nada en el 15% derecho.

---

## Qué hace bien, punto por punto

### 1. Un solo embed, y se lo gana
16 segundos de testimonio y **una** palabra promovida a gráfica: la que carga la
promesa. El resto vive en el rail. Es exactamente lo que la doc de HyperFrames
señala como el error más común evitado: embeber todo.

### 2. La voz manda y todo lo demás baja
Música a `0.12` bajo la voz. Con el VO nativo del clip, cualquier cama por
encima de `0.3` lo tapa.

### 3. Los inserts entran *sobre* la voz
Los cortes 2 y 4 son inserts mudos, pero el `<audio>` nativo del clip 1 sigue
corriendo por debajo en su propia pista. El testimonio no se interrumpe: solo
cambia lo que se ve. Eso es edición, no armado.

### 4. Entra en la frase fuerte
`data-media-start="3.8"` en el corte 1. Los primeros 3.8s del clip crudo eran
carraspeo y "hola chicos". El hook arranca en *"Lo probé porque no me creía
nada"*.

### 5. El rail parte por sentido
`"A los cuatro días" / "ya dormía distinto"`, nunca por ancho de caja. Máximo
dos líneas.

### 6. El formato restrictivo primero
El 9:16 fija dónde puede vivir el rail. El 4:5 se deriva cambiando cuatro
variables CSS y la escala tipográfica (×0.70). Al revés, el rail del 4:5 habría
quedado bajo la UI de Reels.

### 7. Contraste verificado, no supuesto
`check --snapshots` marcó contraste bajo en `rail-03` (la persona estaba contra
una ventana). Se resolvió con scrim, no subiendo el tamaño.

### 8. Nada inventado
El copy de los captions es **verbatim del transcript**. El CTA ("Probalo 30
días") sale de la política de devolución que está escrita en las `notes` del plan.
Ningún claim de salud agregado por el editor.

---

## Deltas 9:16 → 4:5

| Elemento | 9:16 (1080×1920) | 4:5 (1080×1350) |
|---|---|---|
| `data-width` / `data-height` | 1080 / 1920 | 1080 / 1350 |
| `--safe-bottom` | 420px | 200px |
| `--safe-right` | 162px | 60px |
| Rail, `font-size` | 64px | 45px |
| Embed, `font-size` | 210px | 148px |
| Encuadre `ugc-01` | `object-position: center 35%` | `object-position: center 30%` |

Todo lo demás — cortes, timecodes, texto, audio, transiciones — **idéntico**. El
corte no se re-planificó: se reencuadró, y cada creativo tuvo su propio
`render_video`.
