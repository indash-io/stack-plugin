# 02 — Discovery

Trabajo silencioso. Armás el contexto del período: marca, reglas, productos. No hablás con el user hasta el Plan.

## Sub-paso 2A: Gate del MCP de Indash (primero)

Verificá que el MCP `indash` esté disponible. Si no lo está, frená y pedí que lo conecten — no inventes productos ni datos de marca. (Podés avanzar con lo que haya en la carpeta del cliente, pero avisá qué falta.)

## Sub-paso 2B: Heredar la marca del cliente

La marca es la **fuente de verdad** y sale del contexto del cliente:

- `CLAUDE.md` del cliente → identidad, voz, reglas, claims prohibidos.
- `assets/brand-kit/brand.md` → narrativa y posicionamiento.
- `assets/brand-kit/brand-kit.md` → paleta (hex), tipografía, do's & don'ts.

El MCP de Indash (`get_brand_kit`) complementa lo que falte; nunca pisa al `CLAUDE.md` del cliente. Si no hay carpeta de cliente, sugerí correr `new-client` y trabajá con lo que el user provea.

## Sub-paso 2C: Productos en juego

Traé del MCP de Indash los productos del cliente (nombre, URL, imagen, precio). Identificá cuáles entran en el período según el objetivo. **No inventes productos, precios ni features.**

## Sub-paso 2D: Reglas del período

Anotá las reglas duras de la marca que el brief tiene que respetar (ej: "cuotas sin precio", "sin preventa", "humor suave", "cero invención de claims", voseo). Estas reglas gobiernan todo el copy del brief.

## Síntesis interna

```
CLIENTE: [nombre]
PERIODO: [mes / campaña]
OBJETIVO: [vender / lanzar / promo / fecha / awareness]
VOZ: [una línea]
REGLAS DURAS: [lista]
PALETA: [hex del brand-kit]
PRODUCTOS FOCO:
  - [nombre] — [URL] — [imagen] — [precio]
```

Con esto avanzás al Plan.
