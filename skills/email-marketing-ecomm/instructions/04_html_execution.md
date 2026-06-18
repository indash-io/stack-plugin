# 04 — HTML Execution

## Regla 0: email HTML es HTML de 2005

Gmail, Outlook, Yahoo y Apple Mail tienen engines limitados.

## Reglas no negociables

### Layout
- **Tablas para layout.** `<table>` + `<tr>` + `<td>`. Nada de flexbox/grid.
- **Ancho máximo:** 600px. Contenedor centrado con `align="center"`.
- **Mobile:** `<meta name="viewport">` + media queries. Columnas que apilan con `display:block` + `width:100%`.

### CSS
- **Inline CSS** en cada elemento. Solo media queries + reset en `<style>` del head.
- **Sin CSS variables** (no andan en Outlook).
- **Sin `background-image` en elementos críticos** (Outlook los ignora). Colores HEX sólidos.

### Tipografía
- **Font stack safe:** `'Inter', 'Helvetica Neue', Helvetica, Arial, sans-serif`.
- Inter via `<link>` en head. Outlook Windows cae al fallback Helvetica Neue.
- **Tamaños:** H1 36–48px desktop / 28–34px mobile, H2 24–30px, body 15–16px, CTA 14–16px, footer 11–12px.
- **Line-height:** 1.3–1.5.

### Imágenes
- **Siempre `alt="..."`** descriptivo.
- **Siempre `width=` y `height="auto"`** o `style="width:100%; max-width:600px; height:auto;"`.
- **Retina:** servir a 2x.
- **Formato:** JPG para fotos, PNG para producto con fondo liso, WebP solo con fallback.
- **Hospedar en CDN** (Indash storage, Shopify Files, Klaviyo CDN). NUNCA base64.

### Botones (bulletproof)

```html
<table role="presentation" cellspacing="0" cellpadding="0" border="0">
  <tr>
    <td align="center" bgcolor="#4C2C8C" style="border-radius: 999px;">
      <a href="https://..." target="_blank"
         style="display:inline-block; padding:14px 32px; font-family:'Inter','Helvetica Neue',Arial,sans-serif; font-size:15px; color:#FFFFFF; text-decoration:none; font-weight:600;">
        Llevátelo con 20% off →
      </a>
    </td>
  </tr>
</table>
```

- **Padding mínimo:** `14px 28px`.
- **Border-radius:** `999px` (pill) o `8px` (suave editorial) según marca.

### Dark mode
- **Apple Mail / iOS** invierten colores. Incluir `<meta name="color-scheme">` y `<meta name="supported-color-schemes">`.

### Accesibilidad
- `role="presentation"` en tablas de layout.
- `lang="es"` en `<html>`.
- Contraste AA mínimo (ratio 4.5:1).

## Estructura mínima

```html
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="color-scheme" content="light">
  <meta name="supported-color-schemes" content="light">
  <title>{{SUBJECT}}</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800&display=swap" rel="stylesheet">
  <style>
    body { margin:0; padding:0; width:100% !important; -webkit-text-size-adjust:100%; }
    img { border:0; line-height:100%; outline:none; text-decoration:none; display:block; }
    table { border-collapse:collapse; }
    @media only screen and (max-width:600px) {
      .col-mobile { display:block !important; width:100% !important; }
      .px-mobile { padding-left:20px !important; padding-right:20px !important; }
      .h1-mobile { font-size:30px !important; line-height:1.2 !important; }
    }
  </style>
</head>
<body style="margin:0; padding:0; background-color:{{BG}};">
  <div style="display:none; max-height:0; overflow:hidden; mso-hide:all;">{{PREHEADER}}</div>
  <table role="presentation" width="100%" cellspacing="0" cellpadding="0" border="0" bgcolor="{{BG}}">
    <tr><td align="center">
      <table role="presentation" width="600" class="col-mobile" cellspacing="0" cellpadding="0" border="0" style="max-width:600px;">
        <!-- bloques -->
      </table>
    </td></tr>
  </table>
</body>
</html>
```

## Imágenes generadas con MCP

Cuando uses `mcp__indash__generate_image`:
1. Pasar **URLs reales del producto** como `reference_image_urls` (de `get_product_images`) — para que el output mantenga el producto real, no uno inventado.
2. Modelo: `nano-banana` (default, mejor para lifestyle); `gpt-image` (mejor para text rendering en imagen).
3. Aspect ratio: `4:5` (heroes verticales), `1:1` (producto clean), `16:9` (banners horizontales), `9:16` (stories).
4. La URL devuelta se embebe directo en el `<img src="...">` del HTML — Indash hostea en Supabase Storage.

## Checklist antes de entregar

- [ ] Abre bien en Gmail web
- [ ] 600px, se centra en desktop
- [ ] Mobile: bloques apilan, no se cortan
- [ ] Todas las imágenes con `alt`
- [ ] CTAs bulletproof (tabla con bgcolor)
- [ ] Preheader en div invisible
- [ ] Links con `target="_blank"`
- [ ] Sin clases dependientes de CSS externo
- [ ] HEX sólidos
