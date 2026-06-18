# ugc-video-prompts

Skill de Claude Code para generar paquetes completos de prompts de video UGC con **Kling 3.0**, **Veo 3.1**, **Seedance 2.0**, **Nano Banana** (first/last frame) y **lipsync en post** (Enhancor V4 / Sync.so / HeyGen).

## Output

Dada una idea o pedido, devuelve:
1. Análisis de escena
2. Recomendación de modelo con razón
3. Estructura (shots, frames, duración, ¿split en N clips si supera cap?)
4. Prompts de Nano Banana (first + last si aplica, por cada clip si multi-clip)
5. Prompt(s) de video — con conteo exacto de chars (`wc -c`), cap 2500
6. Parámetros técnicos
7. Diálogo — modo de generación (native audio o voz aparte + lipsync), script con timing, dirección de actuación
8. Notas de riesgo + mitigación
9. Flujo de producción (si audio off / multi-clip / sujeto no-humano)

Todo listo para copiar-pegar.

## Capacidades cubiertas

- **Sujetos:** persona, producto, ambos, sujetos no-humanos (dummies, robots, mascotes).
- **Idiomas:** inglés (native audio en cualquier modelo), español regional con voz aparte + lipsync (argentino, mexicano, cubano, colombiano, español ES, chileno, neutro LATAM). Veo 3.1 acepta español native con acentos decentes.
- **Duración:** hasta 15s en un solo clip Kling o Seedance. >15s → split en N clips pegados en CapCut con continuidad inter-clip. Seedance también soporta video extension nativa.
- **Referencias multimodales (solo Seedance 2.0):** hasta 9 imágenes + 3 videos + 3 audios con sintaxis `@asset as [rol]`.
- **Multi-instance packshot:** flagueado como caso imposible y resuelto con N inserts separados.
- **Caps duros:** prompt de video ≤2500 chars (verificado siempre con `wc -c`, nunca a ojo).

## Estructura

```
ugc-video-prompts/
├── skill.md                              # orchestrator — define rol, workflow, caps, audio strategy
├── instructions/
│   ├── input_processing.md               # parseo del pedido
│   ├── analysis.md                       # decisión de modelo, audio strategy, casos imposibles
│   ├── strategy.md                       # UGC authenticity, hook, sujetos no-humanos, articulación
│   └── execution.md                      # cómo redactar Nano Banana / Kling / Veo / multi-clip
├── style/
│   ├── tone_of_voice.md                  # estilo director (no asistente)
│   └── writing_rules.md                  # reglas duras de escritura (cap chars, textura realista, etc.)
├── templates/
│   └── output_template.md                # template del paquete final (con §9 flujo de producción)
├── examples/
│   ├── good/
│   │   ├── testimonial_skincare_8s.md           # Veo 3.1 single-shot, inglés-native
│   │   ├── product_reveal_12s.md                # Kling multi-shot
│   │   ├── testimonial_smartwatch_kids_15s.md   # Kling + voz aparte + lipsync (argentino)
│   │   ├── ad_robot_selfie_cubano_15s.md        # sujeto no-humano + español cubano + lipsync
│   │   ├── testimonial_mia_15s.md               # producto íntimo + voz aparte + lipsync
│   │   └── pov_novio_mia_30s.md                 # split en 2 clips Kling + continuidad inter-clip
│   └── bad/
│       ├── testimonial_skincare_generico.md     # AI-slop genérico
│       └── multi_instance_packshot.md           # caso imposible: N copias del producto en un shot
└── eval/
    └── quality_checklist.md              # checklist pre-entrega obligatorio (incluye §L lipsync)
```

## Cómo lo usa Claude

1. Lee `skill.md` (orchestrator).
2. Sigue el workflow: input_processing → analysis → strategy → execution → style → examples → template → **count chars con `wc -c`** → eval.
3. Nunca entrega sin pasar `eval/quality_checklist.md`.

## Aprendizajes incorporados al skill (changelog interno)

- Kling 3.0 aluciona diálogo en español regional → audio nativo off + voz aparte + lipsync por default.
- Seedance 2.0 no garantiza acentos LATAM + audio distortion ocasional → mismo tratamiento conservador que Kling para español regional.
- Lipsync en post (Enhancor V4 / Sync.so / HeyGen) reemplaza dependencia de lip-sync nativo.
- Conteo exacto de caracteres del prompt (`wc -c`), nunca estimación a ojo.
- Multi-instance packshot (N copias del mismo producto en un shot) es caso imposible — resolverlo con N inserts separados.
- Sujetos no-humanos: adaptar reglas de textura, performance gestual, articulación puppet-style.
- Videos >15s: split en N clips Kling/Seedance con continuidad de wardrobe + setting + lighting. Seedance también soporta video extension nativa.
- Seedance 2.0 + referencias multimodales (`@image`, `@video`, `@audio`) > Kling/Veo cuando hay assets reales del producto/cast/mood.
- Seedance 2.0 default-ea a look commercial/premium → para UGC sobre-dirigir handheld + natural light + no studio.
- Seedance 2.0 tiene text rendering flojo → evitar carteles legibles en el frame, agregar en post si son no-negociables.
- **Audio nativo en español regional = OFF sin excepciones (Kling y Seedance).** El trade-off "audio ON para que el video se vea vivo" es falso — la articulación expresiva se pide con `natural full conversational articulation as if speaking` en el prompt y se obtiene sin generar audio. Audio nativo en español aluciña siempre y se descarta entero en post. Codificado en `style/writing_rules.md` regla 33.
- **Minimalismo de props en multi-subject Seedance.** Cada prop específico (color exacto, marca visible, micro-detalle) que tiene que mantenerse consistente entre cuts es punto de falla. Antes de incluir un prop, preguntarse: ¿la narrativa se lee sin él? Si sí → sacarlo. Caso: el clip-on mic rosa del street vox-pop bloss costó 3 iteraciones. Codificado en `style/writing_rules.md` regla 34 y `instructions/strategy.md`.
- **Cambiar un elemento del concept visual requiere re-validar la narrativa.** Sacar el mic resolvió la derivación pero rompió la lectura de "vox-pop". Regla nueva: antes de regenerar con un cambio, preguntarse si la escena se sigue leyendo como lo que es. Codificado en `style/writing_rules.md` regla 35.
- **Anchor frame propagation.** Si regenero un frame anchor (cast / producto / setting), regenero TODOS los frames dependientes. Saltarse el paso = inconsistencia visible entre cuts. Codificado en `style/writing_rules.md` regla 36 y `eval/quality_checklist.md` sección M.
- **Self-validation antes del usuario.** Corro el checklist A→N internamente sobre cualquier output antes de mostrarlo. Si falla, lo declaro yo + propongo fix. No delego validación crítica al usuario. Codificado en `skill.md` workflow paso 8.5 y `eval/quality_checklist.md` sección N.

## Instalación

Requisito: tener [Claude Code](https://docs.claude.com/en/docs/claude-code) instalado.

### Opción A — symlink (recomendada, soporta `git pull` para updates)

```bash
git clone <URL_DEL_REPO> ~/projects/ugc-video-prompts
cd ~/projects/ugc-video-prompts
./install.sh
```

El script crea un symlink en `~/.claude/skills/ugc-video-prompts`. Cualquier `git pull` en la carpeta del clone propaga cambios al instante.

### Opción B — clonar directo en la carpeta de skills

```bash
mkdir -p ~/.claude/skills
git clone <URL_DEL_REPO> ~/.claude/skills/ugc-video-prompts
```

### Verificar

Abrí Claude Code en cualquier carpeta y pedí:
> armá un UGC de 10 segundos de un producto cualquiera

Si la skill está bien instalada, Claude la detecta por el `description` del frontmatter de `skill.md`.

### Actualizar

```bash
cd <carpeta del clone>
git pull
```

### Desinstalar

```bash
rm ~/.claude/skills/ugc-video-prompts
```
(Solo borra el symlink / clone — el repo original queda intacto.)

## Contribuir

Cambios propuestos: branch + PR. Si tocás reglas de escritura o template, corré un pedido de prueba antes de mergear y pegá el output en la PR.

## Iteración

Para mejorar la skill, tocar **UN archivo por vez**:
- ¿Output inconsistente? → `templates/output_template.md`
- ¿Prompts genéricos? → `style/writing_rules.md` o `instructions/execution.md`
- ¿Elige mal modelo (Kling vs Veo vs Seedance)? → `instructions/analysis.md`
- ¿Mal uso de referencias multimodales `@asset`? → `instructions/execution.md` sección Seedance + `instructions/analysis.md` §1.5
- ¿Tono raro? → `style/tone_of_voice.md`

Correr un pedido de prueba, ver qué falla, ajustar el archivo que corresponde, repetir.
