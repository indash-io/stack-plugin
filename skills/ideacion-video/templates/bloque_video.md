# Template — bloque de video

Sub-formato del bloque de video dentro del contrato general
(`../../content-brief/templates/bloque_por_pieza.md`). El bloque es **un creativo**
(un video = UNA tarjeta del board: `kind: video` + `seconds`, dentro del grupo
de su formato); los clips van adentro, en orden, como material de producción.
La cantidad de clips se **deriva** de `seconds` (`ceil(seconds/10)`) — nunca se
escribe.

```markdown
### Video: <id-del-creativo>         ← kebab-case, ej. video-confesion
- **grupo**: <grupo del formato, ej. stories>   ← un video = un formato
- **kind**: video
- **seconds**: <10 | 20 | …>
- **formato**: 9:16 (1080×1920)
- **funnel**: frío | tibio | caliente
- **rama**: UGC | marca              ← marca → agregar `ejecución a validar`
- **producto**: <product_id> — vista pedida: <frente|perfil|detalle|en-uso|packshot>
- **escenario**: <dónde pasa — un solo setting en UGC>
- **avatar / sujeto**: <descripción corta; si es no-humano, justificar el desvío>
- **registro**: orgánico | descriptivo   ← en tandas, alternar entre videos
- **riesgos declarados**: <desvíos del default y por qué — o "ninguno">
- **defaults asumidos (no pedidos)**: <lista — o "ninguno">
- **notes**: <no-negociables del cliente, claims prohibidos>

#### Clip 1
- **guion** (<N> palabras): "<texto exacto, grafía real>"
- **gesto del still**: <qué actúa el hook — ej. caja abierta al lado, mano al pecho>
- **pronunciación a validar**: <palabra dudosa — u omitir la línea>

#### Clip 2  (solo si seconds > 10)
- **guion** (<N> palabras): "<abre donde terminó el 1; cierra con el CTA imperativo>"
- **gesto del still**: <…>
```

## Reglas del template

1. Hook en los primeros 2 segundos del clip 1; CTA imperativo al final del
   último clip. En formato corto conviven en el clip único.
2. Conteo de palabras junto a cada guion: 10s → 28-32 (techo ~34) · 8s → ~27 ·
   7s → ~24.
3. Un hablante por clip. Si hay dos personas, el corte entre clips es el cambio
   de turno.
4. Para la rama **marca**, reemplazá los clips por el shot list del arco elegido
   (shot + job + duración + sujeto + acción), manteniendo los campos del bloque —
   y la marca `ejecución a validar`.
```
