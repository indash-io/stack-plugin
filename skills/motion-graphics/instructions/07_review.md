# 07 — Revisión

Objetivo: un draft que aguanta una pasada completa sin fixes nuevos. Revisás mirando
renders, no leyendo código (regla 6).

## El loop

1. `npx hyperframes render --quality draft --output renders/draft-<letra>.mp4`.
   Cada draft lleva una letra nueva: nunca pises uno que la persona vio.
2. `contact_sheet.py renders/draft-<letra>.mp4 --fps 6` para la pieza entera, y
   `--fps 10 --from … --to …` alrededor de cada corte y cada escena 3D.
3. Mirá cada hoja y escribí la lista: `t · qué está mal · fix`.
4. Arreglá, corré `snapshot --at` en esos tiempos para verificar, y volvé a 1.

Cortás cuando una pasada completa no agrega nada a la lista.

## Qué buscar (lo que apareció en las piezas de referencia)

- **Choques**: texto contra otro elemento o contra el borde, palabras huérfanas,
  cortes de línea feos, layouts descentrados.
- **Restos**: elementos que se quedan después de su beat; el primer o último frame de
  una escena con un estado que no corresponde (un `fromTo` filtrándose).
- **Vacíos**: media pantalla vacía más de medio segundo, o un plano quieto más de 1.5 s.
- **Legibilidad**: texto sobre fondos cargados (si pasa, oscurecé o desenfocá el fondo
  detrás del texto); flash frames que lavan el color de marca.
- **3D**: logo espejado o deformado; objetos que atraviesan el título; el punto de
  grabación asomando.
- **CSS**: imágenes con un tamaño que no corresponde porque una regla genérica le ganó
  a la específica.

## Sync y audio

- Cada cue de SFX cae en el frame de su evento: compará los tiempos del `cues.json`
  con los snapshots.
- Transcribí el audio del draft y confirmá que no falta ninguna palabra.
- `mix.py measure --file renders/draft-<letra>.mp4` tiene que decir OK.

## El gap contra el pedido

Antes de cerrar, releé el pedido original palabra por palabra ("exciting", "100% del
material real", "fiel a la marca") y poné una nota a cada una contra el draft. Si alguna
no llega, es un fix, no una salvedad de la entrega. Pasá `eval/quality_checklist.md`.

Siguiente: `08_entrega.md`.
