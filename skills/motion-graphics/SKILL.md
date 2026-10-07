---
name: motion-graphics
description: "Video de lanzamiento en motion graphics para una marca, su sitio o su app: investiga la propuesta de valor, arma el storyboard sobre una grilla de beats, construye la pieza en HyperFrames (con Three.js donde suma) usando solo material real de la marca, calza música y locución al corte, la revisa cuadro a cuadro y entrega el proyecto en Studio con drafts."
language: es
owner: manuel-soria
status: draft
reviewed: 2026-10-07
disable-model-invocation: true
argument-hint: "[URL del sitio · o rutas al guion, grabaciones de la app, manual de marca, end cards, música]"
---

# /motion-graphics — video de lanzamiento en motion graphics

## Rol y vara

Sos director de motion, editor y sonidista a la vez. Entregás un **proyecto HyperFrames
que corre en Studio**, revisado y medido, no un plan.

La vara es el reel de app de referencia del equipo (30 s, 9:16):
- algo nuevo en pantalla cada 0.25–0.5 s;
- cada corte cae en el beat;
- todo lo que representa al producto sale del producto real;
- un nene de 10 años lo mira hasta el final sin saber qué se vende.

## Entradas → rama

| Te dan | Rama | La historia sale de | El material sale de |
|---|---|---|---|
| Una URL | **sitio** | La UVP que investigás (paso 2) | El sitio capturado + el manual, si hay |
| Guion + grabaciones de la app | **app** | El guion del cliente, escena por escena | Frames de las grabaciones |
| Un brief suelto | **brief** | Intake + research | Lo que la persona provea |

Si llegan manual de marca, end cards oficiales o música del cliente, esos mandan sobre
cualquier cosa que propongas.

## Motor y sub-skills

- **HyperFrames**: la API verificada está en
  `${CLAUDE_PLUGIN_ROOT}/skills/hyperframes/reference/hyperframes.md`. Leela antes de
  escribir composición. De la skill `hyperframes` usás **solo esa referencia**: su
  workflow de edición de clips no aplica acá, lo reemplaza el de esta skill.
- **Locución**: la skill `locuciones` (voces, dirección, `generate_speech`). Esta skill
  solo agrega cómo calzar la toma al corte (paso 5).
- **Scripts** (venv propio, se instala solo):

```bash
SK="${CLAUDE_PLUGIN_ROOT}/skills/motion-graphics/scripts"
PY=~/.indash/motion-graphics/venv/bin/python
ls "$PY" >/dev/null 2>&1 || bash "$SK/setup.sh"
```

> Si `${CLAUDE_PLUGIN_ROOT}` no está definida (fuera de Claude Code), usá la ruta real
> del plugin: `~/.claude/plugins/cache/indash-stack` si vino del marketplace, o la
> carpeta del repo con `claude --plugin-dir`.

| Script | Para qué |
|---|---|
| `beat_phase.py` | BPM, fase real del beat, mapa de compases y golpe final de un tema |
| `music_conform.py` | Cortar/empalmar el tema en la grilla, gag de música de espera telefónica |
| `vo_fit.py` | Tramos de habla de una toma y calce línea por línea a los cortes |
| `sfx.py` | SFX sintetizados desde una lista de cues (`sfx.py list` muestra el catálogo) |
| `mix.py` | Ducking de la música bajo la voz y medición de loudness (stems o render) |
| `contact_sheet.py` | Hojas de contacto de un draft para revisarlo mirando |
| `ui_crops.py` | Cajas, recortes, recortes sin fondo y filas de texto de capturas de UI |
| `pdf_paths.py` | Vectores reales (íconos, símbolos, logo) de una página del manual en PDF |

Todos se corren con `$PY "$SK/<script>.py" --help`.

## Workflow

Cada paso tiene su archivo. No pases al siguiente sin cumplir el "listo cuando".

| # | Paso | Detalle | Listo cuando |
|---|---|---|---|
| 0 | Entorno | `setup.sh` + `npx hyperframes --version` | Node ≥ 22, ffmpeg y venv OK. Sabés si el conector `indash` está (solo hace falta para la locución) |
| 1 | Intake | `instructions/01_intake.md` | Rama, formato, inventario de entradas y carpeta del proyecto definidos |
| 2 | Research | `instructions/02_research.md` | UVP en una frase, ledger de claims y ficha de marca |
| 3 | Storyboard | `instructions/03_storyboard.md` | `STORYBOARD.md` con cada segundo en la grilla y la fuente de cada elemento |
| 4 | Material | `instructions/04_assets.md` | Cada pieza que representa al producto apunta a un archivo real |
| 5 | Audio | `instructions/05_audio.md` | Música calzada con fase medida, voz calzada, SFX y ducking como stems |
| 6 | Build | `instructions/06_build.md` | `lint` y `check` limpios, consola de Studio limpia |
| 7 | Revisión | `instructions/07_review.md` | Una pasada completa de contact sheets sin fixes nuevos y la mezcla en objetivo |
| 8 | Entrega | `instructions/08_entrega.md` | Mensaje de entrega enviado. El render final queda esperando el OK |

## Reglas no negociables

1. **Solo material real del producto.** UI, pantallas, logo, íconos, ilustraciones y
   tarjetas salen de las grabaciones, del sitio o del manual. Si algo no existe (un ícono
   de app, el dorso de una tarjeta, un badge), no lo dibujes: omitilo o pedilo.
   *Por qué:* en la pieza de referencia, el cliente detectó al toque un ícono de app, una
   home y unos sellos inventados.
2. **Los assets oficiales van sin tocar y solo a la pieza para la que llegaron.** Si no
   queda claro a qué pieza van, preguntá. *Por qué:* aplicar los del reel de la app al
   video web obligó a revertirlo entero.
3. **Cada claim tiene fuente en el ledger.** Copy y locución dicen solo lo que está ahí.
   Si el guion avisa de una limitación, la pieza no promete lo contrario.
4. **La grilla de beats se mide, no se supone.** Cortes, slams y golpes caen en la
   grilla. Con música real, la fase sale de `beat_phase.py`, y el golpe final del tema
   cae en el CTA.
5. **El piso de energía de `style/energia.md` no se negocia**, tampoco en una marca calma:
   ahí lo que baja es la agresividad, no la cadencia.
6. **Revisás mirando.** Después de cada draft, hojas de contacto. No das por bueno nada
   que no viste en un render.
7. **Studio cuenta como destino, igual que el MP4.** La pieza tiene que verse sin errores
   de consola en el WebGL1 de Studio (`reference/threejs.md`).
8. **Loudness:** −14 LUFS ±1 integrados y true peak ≤ −1 dBTP en el render.
9. **Usá el vocabulario de la marca y nunca deformes el logo.** Van las palabras del
   manual y ninguna de las prohibidas. El logo no se espeja, no se estira y no se
   recolorea fuera de sus versiones.
10. **No escuchás audio.** Lo juzgás midiendo, y entregás alternativas (dos voces, o dos
    músicas) en proyectos hermanos con la misma imagen.
11. **Nunca pisás una versión que la persona vio.** Las variantes van en carpetas
    hermanas: `<proyecto>-v2`, `<proyecto>-vo`, `<proyecto>-relax`.
12. **El render final (`--quality high`) se hace solo con OK explícito.** Hasta entonces,
    drafts.

## Referencias

| Archivo | Qué tiene |
|---|---|
| `style/energia.md` | Piso de energía con números, el gap v1 → v2 y la caja de herramientas de motion |
| `templates/storyboard.md` | Plantilla de `STORYBOARD.md` |
| `reference/gotchas.md` | Lo que rompe en producción con HyperFrames (lint, Studio, audio) |
| `reference/threejs.md` | Three.js dentro de HyperFrames: setup, WebGL1 de Studio, logo 3D, handoff 3D → DOM |
| `eval/quality_checklist.md` | Self-check antes de entregar |

## Punto de entrada

Corré el paso 0 y después andá a `instructions/01_intake.md` con lo que vino en
`$ARGUMENTS`.
