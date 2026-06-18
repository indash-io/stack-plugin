# Input Processing

Parsear el pedido del usuario antes de cualquier otra cosa. Si falta algún campo crítico, no inventes — proponé default con justificación y marcalo como "asumido" en el output.

---

## Contexto de cliente (antes de parsear el pedido)

Si la carpeta de trabajo actual es la de un cliente del stack (tiene un `CLAUDE.md` de marca y/o una carpeta `brand/`), **ese es el contexto canónico**:

- Heredá marca, tono de voz, paleta (hex) y tipografía de su `CLAUDE.md` y de `brand/brand-kit.md` / `brand/brand.md`. Eso **gana** sobre los defaults genéricos de esta skill — incluido el **acento argentino default**: si el `CLAUDE.md` del cliente define un acento/mercado (ej: mexicano, español de España), ese manda.
- Usá los assets reales del cliente cuando existan: logos en `brand/logos/`, foto de producto en `productos/referencias/` o el `productos/index.md` traído de Indash. No inventes assets que no existen.
- **Un entregable = un cliente.** No mezcles contexto entre clientes.
- Si **no** hay `CLAUDE.md` de cliente, la estética sale del discovery (URL + referencias adjuntas), nunca de prejuicios sobre la categoría.

## Gate del MCP `indash`

Esta skill tiene dos modos:

- **Modo full (genera assets):** si vas a producir los frames de Nano Banana o los clips de video (Kling / Veo / Seedance) vía el MCP de Indash, **el conector `indash` es requerido**. Antes de generar, verificá que sus herramientas estén disponibles (MCP conectado y autenticado).
  - Si `indash` **no está disponible**, frená la generación. No improvises workarounds ni inventes assets.
  - En **una sola intervención clara**, decile al usuario que conecte `indash` desde el panel de conectores de Cowork y por qué lo necesita esta tarea. No dispares el flujo OAuth por tu cuenta.
  - Mientras tanto, podés **igual entregar el paquete de prompts en modo prompt-only** (ver abajo).
- **Modo prompt-only (default si no hay generación):** si la tarea es solo armar el paquete de prompts (lo que esta skill produce siempre), el gate **no bloquea**. Entregá el paquete completo y, si el usuario después quiere que generes los assets, ahí aplicás el gate. Avisá en una línea que estás entregando en modo prompt-only y qué hace falta conectar para que vos generes los frames/clips.

## Dimensiones a extraer

### 1. Tipo de contenido
- **ad** (hook + producto + CTA implícito)
- **testimonial** (persona hablando a cámara)
- **product demo** (manos + producto + uso)
- **transformation** (antes/después)
- **b-roll** (supporting footage sin diálogo)
- **narrative** (micro-historia de varios beats)

### 2. Sujeto
- **persona** → edad estimada, género, origen/etnia, 2 rasgos físicos distintivos, wardrobe, estado emocional base
- **producto** → nombre, categoría, tamaño real, material, color, packaging
- **ambos** → especificar relación entre persona y producto (hands-on, holding, applying, wearing, reacting)

### 3. Plataforma + aspect ratio
- TikTok / Reels / Shorts → **9:16**
- YouTube / LinkedIn landscape → **16:9**
- Feed Instagram → **1:1** o **4:5**
- Cinematic / letterbox (solo Seedance 2.0) → **21:9**
- Si no se especifica → default **9:16** (UGC por default es vertical)

### 4. Mood / tono
Una frase concreta. Evitar "cool", "moderno". Usar: "íntimo y confesional", "energético y rápido", "aspiracional y luminoso", "crudo y honesto", "ASMR-calmo".

### 5. Duración
- Si el usuario la da → usar esa.
- Si no → default por tipo (ver `instructions/analysis.md`).

### 6. Acento regional (solo si hay diálogo)
- Default: **argentino**.
- Si el producto/marca es mexicano, español, etc., usar el match cultural.

### 7. Audio
- **diálogo** (qué línea, quién)
- **SFX diegéticos** (fricción, líquido, pasos, etc.)
- **ambiente** (cuarto, calle, café)
- **música** (sí/no; si sí, género + intensidad)
- **silencio** (válido — declararlo explícito)

### 8. Número de shots
- **single-shot** — una toma continua
- **multi-shot** — varias tomas narrativamente conectadas (Kling 3.0 o Seedance 2.0)

### 9. Referencias multimodales (si el usuario adjunta archivos)
Si el usuario sube imágenes, videos o audios como referencia, listar **qué subió** y **qué rol cumple cada una**:
- **Imagen del producto** → packshot real → `@image as product reference`
- **Foto del cast / persona** → identidad facial → `@image as cast reference (front-face / side-profile / outfit)`
- **Clip de video** → cámara, mood o acción → `@video as camera / grading / action reference`
- **Audio** → música, voiceover tone o ambient → `@audio as music / voice tone / ambient reference`

Si hay >12 archivos, aplicar priorización (cámara > consistencia de sujeto > mood/audio) — ver `instructions/analysis.md` §1.5.

Tener referencias multimodales **empuja la decisión hacia Seedance 2.0** (es el único modelo que las usa nativamente con sintaxis `@asset`). Kling y Veo solo aceptan first/last frame.

---

## Qué hacer si falta info

| Falta | Default | Marcar |
|-------|---------|--------|
| Plataforma | 9:16 TikTok | "Asumido: TikTok/Reels 9:16 — decime si es otra cosa" |
| Duración | por tipo (ver analysis.md) | "Asumido: Xs — decime si querés más/menos" |
| Acento | argentino | "Asumido: acento argentino" |
| Audio | depende del tipo (testimonial = diálogo, demo = SFX+ambiente) | explícito en output |
| Sujeto específico (edad, origen) | proponé una caracterización realista y genérica | "Asumido: mujer 25-30, argentina — ajustá si necesitás otro cast" |
| Referencias multimodales | ninguna — proceder con frames Nano Banana | "No subiste referencias; si tenés foto del producto o clip de cámara mandala para usar Seedance 2.0 con `@asset`" |

No dejes campos "por definir" en el output final. O se resuelve con dato del usuario o con default marcado.
