# Quality Checklist (Ecom B2C)

Correr este checklist **antes de devolver el output**. Si alguna fila tiene ❌, reescribir ESE bloque.

## 1. Estrategia (las 3 variantes son A/B testables)

- [ ] Las 3 variantes tienen **ángulo distinto** (no solo copy distinto)
- [ ] Los 3 subject lines prometen cosas distintas
- [ ] El hero de cada variante es visualmente distinto
- [ ] Puedo decir en 1 línea por qué cada variante podría ganar

## 2. Variedad visual

- [ ] **Heros distintos** (no los 3 H2, no los 3 H3)
- [ ] **Body diversidad:** al menos 4 body-blocks distintos sumando entre las 3
- [ ] **Closings distintos** (no los 3 con C1)
- [ ] **Anti-defaulting:** combinaciones distintas a las del último brief

## 3. Copy

### Subject + preheader
- [ ] Subject 30–50 chars
- [ ] Preheader 80–110 chars
- [ ] Subject sin CAPS sostenidas ni 3+ emojis
- [ ] Preheader complementa, no repite

### Body
- [ ] Frases cortas (promedio <18 palabras)
- [ ] Cero fluff corporativo
- [ ] Números en cifra (`20%`, `48hs`)
- [ ] Voseo consistente si AR

### CTAs
- [ ] Cada CTA con verbo + beneficio/contexto
- [ ] CTA primario identificable (1 por mail)
- [ ] Sin "Click aquí" / "Hacé clic"

## 4. Brand (prioridad: cliente > Indash > `brands/` legacy)

- [ ] Tono match con el contexto del cliente (`CLAUDE.md` / `brand/brand.md`; fallback `brands/{marca}/brand.md`)
- [ ] Paleta match con `brand/brand-kit.md` del cliente (HEX exactos); fallback `brands/{marca}/palette.md`
- [ ] Logo del cliente (`brand/logos/`) presente en header
- [ ] Footer con unsubscribe visible
- [ ] Palabras de la marca presentes
- [ ] Palabras prohibidas ausentes (`usted`, hype vacío, corporate)

## 5. Imágenes (MCP Indash)

- [ ] Hero images generadas con `mcp__indash__generate_image`
- [ ] `reference_image_urls` incluyó URLs reales de `get_product_images` (producto fiel)
- [ ] URLs devueltas (Supabase Storage) embebidas en el HTML
- [ ] Todas con `alt=""` descriptivo
- [ ] Todas con `width=` y `height="auto"` o `max-width`

## 6. HTML técnico

- [ ] `<!DOCTYPE html>` y `<html lang="es">`
- [ ] Viewport meta presente
- [ ] Ancho máximo 600px
- [ ] Layout con tablas, no divs
- [ ] CSS inline (solo media queries + reset en `<style>`)
- [ ] CTAs bulletproof (tabla con bgcolor)
- [ ] Preheader en div invisible
- [ ] Links con `target="_blank"`
- [ ] No base64 images

## 7. Mobile

- [ ] Media query para max-width 600px
- [ ] En mobile las columnas se apilan
- [ ] Padding horizontal baja a 20px en mobile
- [ ] Headlines escalan a mobile (30px en lugar de 44px)

## 8. Render (opcional)

- [ ] `scripts/render.js` corrió sin errores
- [ ] 3 PNG generados en el folder
- [ ] Sin elementos cortados ni overflow horizontal

## 9. Entregables (guardados en disco)

- [ ] 3 archivos `.html`
- [ ] `brief.md` con decisiones + URLs de assets generados
- [ ] Todo guardado en `entregables/emails/<AAAA-MM-DD>_<campaña-slug>_v<N>/` (no solo mostrado en chat)
- [ ] Versión correcta: no se pisó un folder existente (si existía, se subió `v<N>`)
- [ ] Mensaje final al usuario con resumen + ruta del folder + A/B split + checklist pre-envío

## Regla

Si este checklist no está limpio al 100%, **el output no se entrega**.
