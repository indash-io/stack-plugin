# 05 — Entrega y guardado

## Qué se muestra en el chat

1. **Una línea honesta**: *"No puedo escuchar el audio: chequeé duración,
   tier y guion. Escuchá y decime."*
2. **Tabla de resultados**, un item por fila:

   | # | Voz / speakers | Dirección (resumen) | Duración real | Objetivo | Tier | Escuchar |
   |---|---|---|---|---|---|---|
   | A | Zubenelgenubi | UGC natural, voseo | 10.4s | 10s | short | `<url>` |
   | B | Puck | ídem, más energía | 9.8s | 10s | short | `<url>` |

3. **El guion dirigido** que se generó (con `style`, acotaciones y tags), para
   que la persona vea qué cambiar.
4. **Qué cambiaría vos** si algo no cierra en lo medible (duración fuera de
   rango, un nombre que puede sonar raro).
5. **Handoff**: a qué skill va (`hyperframes` para la pieza final,
   `edicion-ugc` si es la voz de un clip de avatar), o cómo convertir:
   `ffmpeg -i <archivo>.wav -b:a 192k <archivo>.mp3`.
6. **Dónde lo guardaste** (ruta).

## Qué se guarda en disco

**Locución suelta** → `exports/audio/<AAAA-MM-DD>_<slug>_v<N>.md` con el
template de `templates/guion.md` completo (intake, `style`, guion dirigido,
voces, tabla de resultados con `url` y `creative_id`). Los WAV, en la
subcarpeta `exports/audio/<AAAA-MM-DD>_<slug>_v<N>/` si tenés shell (`curl -L
<url> -o <output_name>`); si no, quedan en la galería y lo decís.

**Voz de una pieza de video** → adentro de la carpeta de ese set en
`exports/videos/<set>/`: el `.md` como `vo.md` (o la sección "Locución" del
`.md` del set, si el set lo tiene) y los WAV al lado de los clips, con el
nombre del shot (`shot-02_vo.wav`). Así `hyperframes` los encuentra.

Nunca pises: si el nombre existe, subí la versión.

**Si diseñaste una voz que quedó**, anotala en el `CLAUDE.md` del cliente:

```
## Voz de marca
- `voice_abc123` — "Juli — porteña 25": una mujer argentina de veintipocos,
  voz clara con un poco de aire, acento porteño. Diseñada 2026-09-24, vence
  2027-09-24. Sample: <url>
```

Así la próxima sesión la reusa en vez de diseñarla otra vez (y de gastar
cuota).

## Qué queda en Indash

Cada item es un creative **`audio`** en la galería del workspace, en estado
**draft** (privado). Si la persona elige uno como final, `promote_creative`
lo hace visible para el equipo. Los descartados se pueden dejar en draft.

## Cierre

Si en la sesión hubo fricción con esta skill (la persona te corrigió una
regla, pidió rehacer por algo que la skill debería haber sabido), sugerí en
una línea `/save-learnings`. Si salió derecho, no lo menciones.
