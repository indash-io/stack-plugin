# Template — bloque de email

Sub-formato del bloque de email dentro del contrato general
(`../../content-brief/templates/bloque_por_pieza.md`). Este bloque **no genera
piezas en el Studio**: viaja en el brief y se entrega a quien ejecute el mail.

```markdown
### Email: <id>                       ← kebab-case, ej. email-20off-borrador
- **promo**: <20% off | 3x2 | restock | lanzamiento | BFCM | fecha especial>
- **producto hero**: <product_id> (+ secundarios si hay)
- **segmento**: <toda la base | VIP | nuevos | dormant | carrito abandonado>
- **deadline**: <fecha + hora reales — o "48-72hs, asumido, no pedido">
- **código**: <código — o "link directo">
- **recomendación de split**: <qué variante mandarías al mayor % y por qué>
- **defaults asumidos (no pedidos)**: <lista — o "ninguno">
- **notes**: <no-negociables de la marca, claims prohibidos>

#### V1 — Emocional
- **hipótesis**: <por qué esta variante podría ganar, en una línea>
- **subject** (<n> chars): "<…>"
- **preheader** (<n> chars): "<…>"
- **headline**: "<3-6 palabras>"
- **body** (máx. 3 párrafos cortos): "<…>"
- **CTA primario**: "<verbo + beneficio>"
- **concepto visual del hero**: <2 líneas — momento/lifestyle, sin precio>

#### V2 — Racional
- (mismos campos; subject CON precio/%, urgencia arriba, hero de producto limpio)

#### V3 — Aspiracional
- (mismos campos; el ángulo es el resultado/futuro-yo, sin precio en el subject)
```

## Reglas del template

1. Las 3 hipótesis tienen que ser distinguibles en una línea cada una.
2. Conteos de caracteres junto a subject y preheader, siempre.
3. Ningún dato duro inventado: si el pedido no lo trae, no existe.
