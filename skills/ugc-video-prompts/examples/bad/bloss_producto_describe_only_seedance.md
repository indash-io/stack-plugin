# Bad example — Packaging describe-only en Nano Banana (caso bloss.)

**Caso real ocurrido 2026-05-18.** Pedido: ad UGC 9s 9:16 del **bloss. Silicone Scar Stick** (skincare), modelo Seedance 2.0, multi-shot mixto (UGC handheld + commercial hero).

**El usuario subió 5 imágenes al chat** (4 referencias de cast/style + 1 imagen del producto bloss real). El framework **describió el producto a partir de la imagen vista** pero **no pudo pasarla como `reference_image_urls`** al MCP (las imágenes inline del chat de Claude no exponen bytestream).

Resultado: el packaging generado por Nano Banana fue **inconsistente con el producto real** en las 3 escenas. Producto inventado, no fiel.

---

## Qué se hizo (incorrecto)

Se redactó un prompt de Nano Banana describiendo el packaging del bloss con todo el detalle posible a ojo:

```
... A minimalist nude-beige cylindrical tube, matte finish, approximately
8cm tall and 2cm wide. The cream-beige plastic cap is removed and placed
standing next to the base, revealing a translucent white-clear silicone
balm cylinder at the top of the stick. The front label reads "bloss." in
bold black sans-serif lowercase letters, with a period after the word,
positioned in the upper third of the tube. Below in much smaller thin
black uppercase letters reads "SCAR SOLUTIONS · SILICONE SCAR STICK"
wrapping vertically along the side of the tube. ...
```

Tres errores en la descripción (descubiertos al comparar con la foto real del producto):

1. **Posición del lettering invertida.** El "bloss." real va **abajo** y en bold grande; "SCAR SOLUTIONS / SILICONE SCAR STICK" va **arriba** en una línea fina superior. El prompt lo describió al revés.
2. **Layout del texto secundario.** Las dos líneas "SCAR SOLUTIONS" y "SILICONE SCAR STICK" están en **horizontal apiladas en la cara frontal**, no "wrapping vertically along the side".
3. **Color del cuerpo.** No es "nude-beige" neutro. Es un **blush nude rosado pálido** (más cálido y con leve matiz rosa). El cap es del mismo color que el cuerpo, no contrastante.

Resultado: en los 3 shots el packaging derivó a **distintas variantes inventadas** (cada Nano Banana propuso un layout diferente; Seedance las mezcló).

---

## Por qué falló

Nano Banana puede leer "minimalist skincare tube with black sans-serif label" como **concepto**, pero **no reproduce fielmente tipografía, layout y matiz de color de un producto comercial específico** desde texto. El modelo va al gestalt de "producto skincare premium minimalista" y rellena los detalles a su criterio.

**Reference image > prompt descriptivo** para cualquier producto con identidad de marca real. Sin la foto, el modelo inventa.

---

## Qué hubiera funcionado

**Opción A — la correcta:** cargar el producto al workspace de Indash (con `list_products` / la UI) y traer las imágenes con `get_product_images`. Pasarlas como `reference_image_urls` a Nano Banana y Seedance.

**Opción B — workaround:** que el usuario suba la foto del producto a un host público (Drive público, Imgur, Dropbox público) y pase la URL en el chat. Pasarla como `reference_image_urls`.

**Opción C — solo si A y B son imposibles:** generar **una sola** Nano Banana del producto como packshot hero con descripción quirúrgica + iterar hasta que salga fiel + usar **esa Nano Banana** como reference image en los demás frames y en el Seedance final. Sigue siendo inferior a A/B pero al menos ancla la deriva entre frames.

---

## Lección incorporada a la skill

→ Ver `eval/quality_checklist.md` sección D, ítem "imagen real del producto".

**Regla dura:** Si el pedido involucra un producto con packaging específico (tipografía, color, layout, logo), **NO se entrega sin imagen real del producto como `reference_image_urls`**. Avisar al usuario ANTES de generar y resolver con Opción A o B. Si solo Opción C es viable, marcar el riesgo en §8 antes de generar.

---

## Bonus — fallo paralelo del mismo run: Shot 2 sin mejora real de piel

El concept pedía un "before/after" de las cicatrices entre Shot 1 (auto, con marcas visibles) y Shot 2 (espejo, glow). En el video generado **la piel no mejora visiblemente** entre los dos shots.

Causa: el frame de Nano Banana del Shot 2 fue descrito como "noticeably faded and softened (still slightly visible — keep it real, not magic)". El "keep it real" suavizó tanto la diferencia que Seedance no la registró como cambio visual entre cuts.

**Regla:** En transformaciones de antes/después que **dependen de un cambio visual sutil de skin** (acne, manchas, hinchazón, ojeras), pedir el **delta exagerado** en el frame del estado final. Si parece "demasiado", Seedance lo va a suavizar al interpolar — entonces el extremo del Nano Banana es lo que llega a "lo realista" en el render final. Sub-shoot deliberado del delta = no se ve.

→ Ver `style/writing_rules.md` regla nueva 31 (transformación visual) y `eval/quality_checklist.md` sección E.
