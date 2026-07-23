# Output Structure

Cómo se entrega el output final al usuario.

## Estructura de carpeta

Se guarda en `exports/emails/` de la carpeta del cliente, en un subfolder versionado con el nombre canónico:

```
exports/emails/<AAAA-MM-DD>_<campaña-slug>_v<N>/
```

Ejemplos:
- `exports/emails/2026-06-02_20off-smud-borrador-vello_v1/`
- `exports/emails/2026-04-23_3x2-ice-roller_v1/`
- `exports/emails/2026-11-28_bfcm-smud_v2/`

**Versiona, no pisa:** si el folder `..._v1` ya existe, subí a `v2`, `v3`… Nunca sobreescribas un entregable existente. Si no hay estructura de cliente en el directorio actual, guardá en `./exports/emails/` del CWD y avisá que conviene onboardear con `new-client`.

## Archivos dentro

```
exports/emails/<AAAA-MM-DD>_<campaña-slug>_v<N>/
├── brief.md                      # brief interpretado + decisiones + URLs de imágenes generadas
├── variant_1_emotional.html      # HTML listo para Klaviyo/Mailchimp/Customer.io
├── variant_1_emotional.png       # preview renderizado (opcional, render con Puppeteer)
├── variant_2_rational.html
├── variant_2_rational.png
├── variant_3_aspirational.html
└── variant_3_aspirational.png
```

## brief.md — campos obligatorios

```markdown
# Brief — {Marca} · {promo name}

**Fecha:** {YYYY-MM-DD}
**Marca:** {marca}
**Promo:** {tipo + valor}
**Producto destacado:** {nombre + URL}
**Deadline:** {fecha + hora}
**Segmento:** {audiencia}
**Idioma:** {es-AR / es / en}
**Indash product ID:** {product_id de list_products}

## Decisiones tomadas
- (lista de defaults asumidos, placeholders, supuestos)

## Assets generados (vía MCP Indash)
| Variante | Asset | URL |

## Variantes
| # | Ángulo | Subject | Preheader |

## Layouts elegidos (test de variedad ✓)
| Variante | Hero | Body | Closing |

## Hipótesis por variante

## Recomendación de A/B split

## Antes de enviar — checklist
```

## Mensaje final al usuario (en chat)

Resumen compacto:
- Tabla con 3 subject + preheader
- Ángulo + hipótesis en 1 línea cada uno
- Path a los archivos
- Recomendación de split
- Próximo paso (cargar en Klaviyo / previewar / etc.)
