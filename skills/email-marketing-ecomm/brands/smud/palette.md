---
name: smud-palette
note: paleta extraída de packaging, producto y assets editoriales de Smud
---

# Smud — Paleta visual y tipografía

## Colores (HEX)

### Primarios — lila / lavanda
| Token | HEX | Uso |
|---|---|---|
| `lila` | `#A78BFA` | acento principal, texto destacado, botones secundarios |
| `lila-mid` | `#8B5CF6` | botones, CTAs primarios sobre cream |
| `lila-dark` | `#4C2C8C` | footer, fondos premium, headlines sobre cream |
| `lila-deep` | `#2E1A5C` | footer profundo, fondos hero dark |
| `lila-soft` | `#D7C9F5` | badges, pills, fondos suaves |
| `lila-bg` | `#EFE9FB` | fondo alternativo para secciones |

### Cream / neutros cálidos
| Token | HEX | Uso |
|---|---|---|
| `cream` | `#F5F0EA` | fondo principal default |
| `cream-warm` | `#EFE6D8` | fondo alternativo más cálido |
| `cream-deep` | `#E5DAC5` | borders suaves, separadores |
| `off-white` | `#FAF7F2` | fondo de cards sobre cream |

### Acento — verde lima
| Token | HEX | Uso |
|---|---|---|
| `lime` | `#D4F564` | accent decorativo, badges, ribbons, redes en footer |
| `lime-mid` | `#B8E040` | hover, énfasis |
| `lime-dark` | `#7BA01F` | texto lime sobre cream (contraste AA) |

### Texto
| Token | HEX | Uso |
|---|---|---|
| `text-primary` | `#1A1130` | headlines y body sobre cream |
| `text-secondary` | `#4C3F66` | subtítulos sobre cream |
| `text-muted` | `#807299` | captions, fine print sobre cream |
| `text-on-dark` | `#FFFFFF` | sobre fondos lila-dark / lila-deep |
| `text-on-dark-muted` | `#D7C9F5` | subtitle sobre dark |

### Bordes
| Token | HEX | Uso |
|---|---|---|
| `border-soft` | `#E5DAC5` | divisores sobre cream |
| `border-lila` | `#D7C9F5` | bordes lila soft |

## Tipografía

### Stack
- **Headlines:** `'Inter', 'Helvetica Neue', Arial, sans-serif` weight 700-800, letter-spacing -0.5px a -1px
- **Body:** `'Inter', 'Helvetica Neue', Helvetica, Arial, sans-serif` weight 400
- (Si Smud tiene custom font tipo Söhne / Cabinet Grotesk, agregar acá; fallback queda Inter)

### Escala

| Elemento | Desktop | Mobile | Weight |
|---|---|---|---|
| H1 / Hero | 40-48px | 28-34px | 800 |
| H2 / Section | 28-32px | 22-26px | 700 |
| H3 | 20-22px | 18-20px | 700 |
| Body | 15-16px | 15px | 400 |
| Body lead | 17-18px | 16px | 400 |
| Eyebrow | 12px | 12px | 600 uppercase |
| CTA | 14-15px | 14px | 600 |
| Footer | 11-12px | 11px | 400 |

## Componentes reutilizables

### Botón primario (sobre cream)
- background: `#4C2C8C` (lila-dark) o `#8B5CF6` (lila-mid)
- color: `#FFFFFF`
- border-radius: `999px` (pill) o `8px` (suave editorial)
- padding: `14px 28px`
- font-weight: `600`

### Botón primario (sobre lila-dark)
- background: `#D4F564` (lime accent)
- color: `#1A1130`
- mismo padding y peso

### Eyebrow / label
- font-size: `12px`
- letter-spacing: `2px`
- text-transform: uppercase
- color: `#8B5CF6` (lila-mid) o `#7BA01F` (lime-dark) según contraste
- font-weight: `600`

### Badge / pill (lime accent)
- background: `#D4F564`
- color: `#1A1130`
- border-radius: `999px`
- padding: `5px 14px`
- font-weight: `600`
- font-size: `12px`

### Card de producto
- background: `#FFFFFF` o `#FAF7F2`
- border: `1px solid #E5DAC5`
- border-radius: `12px`
- padding: `20px`

### Footer Smud (signature)
- background: `#2E1A5C` (lila-deep) o `#4C2C8C` (lila-dark)
- logo `smud` grande en cream / blanco
- redes IG/TT en pill `#D4F564` (lime)
- texto pie en cream / lila-soft

## Reglas de uso

1. **Lila siempre presente.** Aunque sea en accent. Fondo cream + lila es el combo signature.
2. **Verde lima con moderación.** Solo en CTAs sobre dark, badges, ribbons. NO como background grande.
3. **Cream como fondo principal default.** Blanco puro queda frío para Smud.
4. **Border-radius:** `8-12px` editorial / `999px` para CTAs pill.
5. **Sin sombras pesadas.** Si hay sombra, muy sutil (`box-shadow: 0 1px 3px rgba(76,44,140,0.08)`).
6. **Header del mail:** wordmark `smud` lowercase en lila-dark o lila-mid sobre cream.

## Logo

Wordmark `smud` lowercase, peso 800, letter-spacing -0.5px. Usar:
- Lila-dark (`#4C2C8C`) sobre cream
- Cream/blanco sobre lila-dark / lila-deep
- Nunca multicolor, nunca rotado

## Placeholders mientras no haya assets generados

```
Producto cream:    https://placehold.co/800x1000/F5F0EA/4C2C8C?text=Smud&font=raleway
Lifestyle:         https://placehold.co/1200x1500/EFE9FB/4C2C8C?text=Ritual&font=raleway
Hero dark:         https://placehold.co/1200x1500/2E1A5C/D4F564?text=smud&font=raleway
```

Reemplazar SIEMPRE con assets generados via `mcp__indash__generate_image` antes de enviar.
