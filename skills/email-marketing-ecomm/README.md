# Email Marketing Ecomm — Skill para Claude Code

Skill de generación de mails promocionales para e-commerce DTC.
Genera 3 variantes A/B testables (Emocional / Racional / Aspiracional) con HTML listo para Klaviyo/Mailchimp + PNG renderizado + hero images generadas con AI.

---

## Qué hace

Pasás un brief (promo + producto + deadline; la marca sale del contexto del cliente) y devuelve, guardado en disco en la carpeta del cliente:

```
entregables/emails/<AAAA-MM-DD>_<campaña-slug>_v<N>/
├── brief.md                          ← decisiones + A/B split + checklist
├── variant_1_emotional.html          ← listo para Klaviyo
├── variant_1_emotional.png           ← preview full email
├── variant_2_rational.html / .png
├── variant_3_aspirational.html / .png
└── assets/                           ← hero images generadas con AI
```

Versiona, no pisa: si el folder `..._v1` existe, sube a `v2`.

Cubre: descuentos, restock, 2x1/3x2, BFCM/Cyber, lanzamientos, fechas especiales, bundles.

---

## Setup (una vez por máquina)

### 1. Requisitos
- **Claude Code** instalado y autenticado
- **Node.js 18+** (para el render de PNG)
- **MCP de Indash** conectado en Claude Code

### 2. Instalar el skill
Copiá la carpeta `email-marketing-ecomm/` a la ubicación de skills que use tu equipo (típicamente `~/.claude/skills/` o el repo compartido).

### 3. Instalar Puppeteer (para render PNG)
```bash
cd email-marketing-ecomm/scripts
npm install
```
~200MB, una sola vez.

### 4. Conectar MCP de Indash
```bash
claude mcp add --transport http indash https://www.indash.ai/api/mcp \
  --header "Authorization: Bearer <TU_TOKEN>"
```
Pedí el token al admin del workspace de Indash.

---

## Cómo se usa

### Brief mínimo
- **Marca** (sale del contexto del cliente: `CLAUDE.md` + `brand/` de la carpeta de trabajo; se complementa con el MCP de Indash; fallback `brands/{slug}/`)
- **Promo** (20% off, 3x2, restock, lanzamiento…)
- **Producto/s destacado/s** (hero + secundarios opcionales)
- **Deadline** (fecha + hora real)

### Triggers para invocarlo
- "Armá un mail promo para [marca] con [promo]"
- "Necesito un mail de [%] off en [producto]"
- "Hacé una campaña de lanzamiento para [producto]"
- "Mail de restock de [producto]"
- "Campaña BFCM para [marca]"

### Ejemplo
> "Armá un mail de 20% off en el Borrador de Vello Smud. Termina el domingo 23:59. Audiencia: todos los suscriptores."

El skill va a:
1. Resolver la marca por prioridad: contexto del cliente (`CLAUDE.md` + `brand/`) primero, `get_brand_kit` del MCP como complemento, `brands/{slug}/` como fallback legacy
2. Levantar las imágenes reales del producto (`get_product_images`)
3. Generar heros adicionales con AI si hacen falta (`generate_image` con nano-banana / gpt-image)
4. Componer 3 variantes con layouts distintos
5. Validar contra el quality checklist
6. Renderizar los 3 PNG

---

## Arquitectura

```
email-marketing-ecomm/
├── skill.md                      ← entry point del skill
├── README.md                     ← este archivo
├── instructions/
│   ├── 01_input_processing.md    ← parseo del brief
│   ├── 02_variant_strategy.md    ← las 3 variantes A/B
│   ├── 03_copywriting.md         ← reglas de copy
│   ├── 04_html_execution.md      ← HTML email-safe
│   └── 05_layout_library.md      ← biblioteca de layouts modulares
├── style/
│   ├── tone_of_voice.md          ← tono base (transversal)
│   └── writing_rules.md          ← reglas operativas
├── templates/
│   ├── email_base.html           ← template HTML email-safe
│   └── output_structure.md       ← formato del brief.md final
├── eval/
│   └── quality_checklist.md      ← checklist anti-output-genérico
├── brands/                       ← marcas semilla / FALLBACK legacy (no es la fuente primaria)
│   └── smud/
│       ├── brand.md
│       └── palette.md
└── scripts/
    ├── render.js                 ← Puppeteer → PNG
    ├── package.json
    └── README.md
```

> La marca primaria **no** vive acá: vive en el contexto del cliente (`CLAUDE.md` + `brand/` de la carpeta de trabajo). `brands/` es solo fallback. Los entregables se guardan en `entregables/emails/` de la carpeta del cliente, no en una carpeta `output/` interna.

---

## Extensibilidad

### Agregar una marca nueva
Lo normal es **onboardear el cliente con `new-client`**: eso arma su `CLAUDE.md` + `brand/` (la fuente de verdad que esta skill hereda) y trae sus productos del MCP de Indash. No hace falta tocar `brands/`.

`brands/{slug}/` es solo el banco de marcas semilla / fallback (ej: `smud`), que se usa cuando no hay contexto de cliente ni datos en Indash. Para sumar una al fallback legacy:
1. Crear `brands/{nueva-marca}/brand.md` (perfil de tono, productos, do/don'ts)
2. Crear `brands/{nueva-marca}/palette.md` (HEX, tipografía, componentes)
3. (opcional) `brands/{nueva-marca}/tone_override.md` para overrides del tono base

### Modificar layouts
Editá `instructions/05_layout_library.md`. La biblioteca tiene 7 heros + 12 body blocks + 4 closings. Cada variante usa combinaciones distintas.

### Cambiar reglas de copy
Editá `style/writing_rules.md` (reglas duras) o `style/tone_of_voice.md` (tono base). El override de tono por marca lo da el contexto del cliente (`CLAUDE.md` + `brand/brand.md`); en modo fallback legacy va en `brands/{marca}/tone_override.md`.

---

## Reglas duras del skill

- **3 variantes siempre** (Emocional / Racional / Aspiracional) — A/B testables, no cosméticas
- **Cero fluff corporativo** ("nos complace anunciar…" → ❌)
- **CTAs con verbo + beneficio** ("Comprá en 3x2" ✅ / "Click aquí" ❌)
- **No inventa stats ni testimonios** — si no están en el brand kit, lenguaje cualitativo
- **HTML email-safe** (tablas, inline CSS, 600px max, bulletproof buttons)
- **Mobile responsive** con media queries
- **Tildes y voseo** consistentes en marcas AR

---

## Qué NO hace

- ❌ No cubre B2B SaaS (para eso está el otro skill, `indash-b2b-mail`)
- ❌ No manda los mails — solo genera HTML + PNG
- ❌ No carga a Klaviyo / Mailchimp automáticamente
- ❌ No genera video (solo imágenes estáticas con AI)
- ❌ No inventa cupones / códigos
- ❌ No promete deadlines falsos
- ❌ No usa countdowns dinámicos (los pone estáticos + nota para reemplazar por GIF de Klaviyo)

---

## Output

Los entregables se guardan en `entregables/emails/<AAAA-MM-DD>_<campaña-slug>_v<N>/` de la carpeta del cliente (3 HTML + 3 PNG + `brief.md`), versionando sin pisar. La estructura completa está en `templates/output_structure.md`.

---

## Troubleshooting

| Problema | Solución |
|---|---|
| "Brand kit no encontrado" | Verificar que la marca exista en el workspace de Indash conectado al MCP |
| Render PNG falla | Correr `cd scripts && npm install`. Si persiste: `npx puppeteer browsers install chrome` |
| Imágenes en blanco en el PNG | Verificar que las URLs de hero images sean públicas |
| Outlook rompe el layout | Revisar que CTAs sean bulletproof buttons y no usar flexbox |
| Mail cae en spam | Revisar checklist de deliverability en `eval/quality_checklist.md` |

---

## Contacto

Skill mantenido por el equipo de growth de Indash. Sugerencias / bugs / mejoras → equipo interno.
