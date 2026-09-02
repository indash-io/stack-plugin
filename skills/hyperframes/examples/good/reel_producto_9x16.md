# BUENO — Reel 9:16 de producto a partir de clips generados

Marca anonimizada. Categoría: skincare DTC. Material: 4 clips renderizados con
`video-execution` + 1 packshot de `library/products/`.

**Por qué es bueno**: el hook aguanta solo, cada corte aporta una idea, el ritmo
acelera hacia el payoff, hay una sola transición primaria con un acento, y el
texto vive entero en zona segura.

---

## Brief de entrada

> "Ya están renderizados los 4 clips del grupo `serum-noche` del board.
> Armame el reel final."

## Discovery (silencioso)

| # | Archivo | Dur. real | Res. | Audio | Qué muestra |
|---|---|---|---|---|---|
| 1 | `shot-01.mp4` | 6.0s | 1080×1920 | no | Gotero cayendo sobre la palma, macro |
| 2 | `shot-02.mp4` | 8.0s | 1080×1920 | no | Aplicación en el pómulo, luz de ventana |
| 3 | `shot-03.mp4` | 5.0s | 1080×1920 | no | Textura absorbiéndose, macro extremo |
| 4 | `shot-04.mp4` | 6.0s | 1080×1920 | no | Plano medio, piel a contraluz |
| 5 | `packshot.png` | — | 1080×1350 | — | Frasco frontal sobre fondo hueso |

Marca de `library/brand/brand.md`: papel `#F2EBDD`, tinta `#1B1A17`, acento
`#8FA086`, tipografía sans geométrica (`library/fonts/`). Tono: técnico y
sobrio, voseo, sin exclamaciones.

Entorno: Node 22.11, FFmpeg presente → **`full_render`**.

## Decisión clave

El mejor frame del clip 1 (la gota tocando la piel) está a los **2.4s**. En vez
de esperarlo, se entra con `data-media-start="2.15"`: el reel arranca 0.25s
antes del impacto.

---

## Plan de edición

**Formato**: 9:16 · 1080×1920 · **Duración**: 11.4s · **Destino**: Instagram Reels

| # | Timecode | Dur. | Material | `data-media-start` | Función | Texto | Audio |
|---|---|---|---|---|---|---|---|
| 1 | 0.0 – 2.1 | 2.1s | `shot-01.mp4` | 2.15 | **HOOK** — la gota toca la piel | "Se absorbe en 30 segundos" | música 0.80 |
| 2 | 2.1 – 5.0 | 2.9s | `shot-02.mp4` | 0.6 | Desarrollo — aplicación | "Una capa fina alcanza" | música 0.75 |
| 3 | 5.0 – 7.2 | 2.2s | `shot-03.mp4` | 1.4 | Desarrollo — textura absorbiéndose | — | música 0.75 |
| 4 | 7.2 – 9.0 | 1.8s | `shot-04.mp4` | 2.0 | **PAYOFF** — piel a contraluz | "Sin residuo graso" | música 0.85 |
| 5 | 9.0 – 11.4 | 2.4s | `packshot.png` | — | **CTA** — packshot + logo | "Pedilo en el link" | música 0.60 |

**Seams**

| Seam | Timecode | Tipo | Dur. | Rol |
|---|---|---|---|---|
| 1 → 2 | 2.1 | `transitions-blur` | 0.28s | primaria |
| 2 → 3 | 5.0 | corte seco | — | el match cut de la mano carga la continuidad |
| 3 → 4 | 7.2 | `transitions-blur` | 0.28s | primaria |
| 4 → 5 | 9.0 | `flash-through-white` | 0.22s | **acento** — entra el packshot |

**Movimiento interno**: push-in `scale 1.00 → 1.05`, `ease: none`, sobre el
packshot del corte 5.

**Zona segura**: texto entre `y = 330px` y `y = 1500px`; márgenes `x = 60px` /
`162px` (rail de acciones a la derecha).

**Afuera**: nada — los 4 clips entraron, recortados.

---

## Qué hace bien, punto por punto

### 1. El hook aguanta solo
No hay logo, no hay fundido, no hay plano de establecimiento. En el frame 1 hay
una gota a punto de tocar la piel y un texto con un número. Alguien que scrollea
entiende de qué se trata sin contexto.

### 2. Entra tarde en el material
`data-media-start="2.15"` en el corte 1 y `2.0` en el corte 4. El material
generado casi nunca empieza en su mejor frame; el editor lo sabe y no regala
segundos.

### 3. Los cortes aceleran
`2.1 → 2.9 → 2.2 → 1.8 → 2.4`. Ninguno igual a su vecino, y la caída de 2.2 a
1.8 antes del payoff genera tensión. El CTA es el más largo de la cola: 2.4s
para leer y reaccionar.

### 4. Una primaria, un acento
`transitions-blur` en dos seams (coherente con la energía calma del skincare),
un `flash-through-white` en el único momento que lo merece. El tercer seam es
corte seco: hay un match cut de la mano que carga la continuidad sola.

### 5. Cada corte aporta una idea
gota → aplicación → absorción → resultado → dónde comprarlo. Ningún corte repite
lo que ya se vio.

### 6. Texto: tres bloques, ninguno compite
Tres textos en 11.4s, uno por bloque narrativo, nunca dos a la vez. El corte 3
va sin texto **a propósito**: la textura habla sola y el descanso hace que el
"Sin residuo graso" del payoff pegue más.

### 7. Copy específico
"Se absorbe en 30 segundos" (número crudo del brief), no "Descubrí la nueva
generación de sérums". El CTA tiene verbo: "Pedilo en el link".

### 8. Marca real
La fuente sale de `library/fonts/`, copiada al proyecto y declarada con
`font-display: block`. La paleta sale de `library/brand/brand.md`, no de la impresión que dio
el clip.

### 9. Zona segura respetada y verificada
`check --snapshots --at 0.4,1.2,3.5,6,8,10.5` y los PNG se miraron. El caption
del corte 2 estaba a 1520px (dentro de la franja de UI) y se subió a 1460px
antes del draft.

### 10. Gates en orden
`lint` limpio → `check` con dos hallazgos de contraste (corregidos con scrim) →
`draft` → OK del user → un solo `high`.

---

## El detalle que casi lo arruina

En la primera pasada, los cortes 2 y 3 duraban 2.5s cada uno. En el draft se
sentía a metrónomo. El fix fue de dos atributos: `2.9` y `2.2`. Nada más cambió.

Es exactamente la disciplina de iteración: **un cambio por render, objetivo
absoluto** ("corte 2 = 2.9s"), y freeze explícito de todo lo demás.
