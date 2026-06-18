# 02 — Discovery

Trabajo silencioso. Armás el brief interno del cliente que después volcás en el `CLAUDE.md` y en el índice de productos. **No narrás el proceso al user** — solo le mostrás resultados al final.

---

## Sub-paso 2A: Gate de autenticación del MCP de Indash (PRIMERO, no negociable)

Antes de traer nada, verificá que el MCP **`indash`** esté disponible (conectado y autenticado).

- **Si `indash` NO está disponible** → frená. No scrapees a mano, no inventes productos. Decile al user, en una sola intervención:

  > Para traer los productos de **{cliente}** necesito el conector **Indash** conectado. Conectalo desde el panel de conectores de Cowork (o configurá `INDASH_TOKEN`) y seguimos. Mientras tanto puedo armar la estructura de carpetas, pero el catálogo queda vacío hasta que esté.

  El user decide: esperar a conectar, o avanzar con la estructura y completar productos después.

- **Si `indash` está disponible** → seguí con 2B.

---

## Sub-paso 2B: Traer los productos del cliente desde Indash

Con el MCP `indash` conectado, traé el catálogo del cliente:

1. **Ubicá al cliente en Indash** — por el ID/handle que te pasaron en Intake; si no lo tenés, buscalo por nombre.
2. **Listá sus productos**. Por cada producto, capturá lo que esté disponible:
   - Nombre exacto del producto.
   - URL de la página del producto.
   - Imagen de referencia (URL o asset).
   - Categoría, precio, variantes/SKU si vienen.
3. Si el cliente no aparece en Indash o no tiene productos cargados → anotalo como pendiente; no inventes nada.

> Las herramientas exactas del MCP de Indash se autodescubren al estar conectado. Usá las que correspondan para resolver cliente → productos. No asumas nombres de tools; mirá las que estén disponibles.

Esto alimenta `templates/product_index.md`. **La URL + imagen de cada producto son justamente los dos inputs que después piden `carrusel-nano-banana` y `stories-nano-banana`** — por eso las capturás bien acá.

---

## Sub-paso 2C: Assets de marca — logos, tipografías y brand kit

El objetivo es que `brand/` quede poblado con TODO el material de marca, cada cosa en su lugar fijo:

- **Logos** → `brand/logos/`
- **Tipografías** (archivos de fuente: .otf/.ttf/.woff) → `brand/typographies/`
- **Brand kit crudo / guidelines** (PDF u otros) → `brand/assets/`

### Orden de búsqueda

1. **Primero, desde el MCP de Indash.** Si la marca del cliente está cargada en la app de Indash, descargá desde ahí los logos, las tipografías y el brand kit, y guardalos en las carpetas de `brand/` que correspondan. (Usá las herramientas del MCP que estén disponibles para resolver marca → assets; no asumas nombres de tools.)
2. **Si la marca NO está en Indash**, pedíselo al user de forma concreta:

   > La marca de **{cliente}** no está cargada en Indash. Si tenés el brand kit (un PDF), los logos o las tipografías, pasámelos y los dejo ordenados en `brand/`. Si no, dejo esos campos como pendientes.

   Cuando el user pase archivos:
   - Logos → `brand/logos/`
   - Fuentes → `brand/typographies/`
   - PDF del brand kit / guidelines → `brand/assets/`
   - De ese material extraés paleta y tipografía para el `brand-kit.md` y el `CLAUDE.md`.
3. **Si no hay ni Indash ni archivos**, dejá `brand/` con sus `.gitkeep` y marcá los campos de marca como `⚠️ PENDIENTE` — **no inventes** logos, fuentes ni paleta.

> No descargues nada que no sea de marca acá. Las imágenes de **producto** van en `productos/referencias/`, no en `brand/`.

---

## Sub-paso 2D: Análisis de marca (si tenés URL del sitio o el brand kit)

Si te pasaron la URL del sitio/tienda, extraé el brand kit implícito para el `CLAUDE.md`:

1. **Paleta dominante** — 3 a 5 colores con descripción + hex.
2. **Tipografía** — familia(s) visible(s); describí características (serif/sans, peso, contraste) en vez de afirmar un nombre exacto salvo certeza.
3. **Tono de marca** — cómo escribe la marca: técnico, emocional, minimalista, hablado, etc.
4. **Estética / mood** — editorial, lifestyle, minimal, heritage, clinical, playful, etc. (una palabra).
5. **Categoría / vertical** del cliente.

Si NO tenés URL → dejá estos campos como placeholder explícito en el `CLAUDE.md` para que un humano los complete. **No inventes paleta ni tono.**

---

## Sub-paso 2E: Síntesis del brief silencioso

Armá una nota interna con esta estructura. No se la mostrás al user todavía — la usás en Scaffold y Client Context.

```
CLIENTE: [nombre exacto]
SLUG: [kebab-case derivado]
INDASH: [ID/handle o "pendiente: linkear cliente en Indash"]
SITIO: [URL o "pendiente"]
DRIVE: [link o "pendiente"]
NOTION: [link o "pendiente"]
CATEGORIA / VERTICAL: [o "pendiente"]
TONO DE MARCA: [una palabra o "pendiente"]
ESTETICA / MOOD: [una palabra o "pendiente"]
PALETA: [colores + hex, o "pendiente"]
TIPOGRAFIA: [familia + características, o "pendiente"]
ASSETS DE MARCA:
  - LOGOS: [cantidad guardada en brand/logos/ y fuente (Indash / user) o "pendiente"]
  - TIPOGRAFIAS: [archivos en brand/typographies/ o "pendiente"]
  - BRAND KIT: [archivo en brand/assets/ o "pendiente"]
PRODUCTOS (desde Indash):
  - [nombre] — [URL] — [imagen] — [categoría/precio]
  - ...
  (o "pendiente: conectar Indash / cliente sin productos cargados")
```

Con esto avanzás a Scaffold.

---

## Reglas de Discovery

1. **Gate de Indash primero.** Sin el conector, no hay catálogo: o se conecta, o el índice queda como pendiente.
2. **Silencio total** con el user durante el discovery.
3. **No inventes.** Marca, productos y links que no consigas van como placeholder explícito.
4. **Capturá URL + imagen de cada producto con precisión** — son los inputs de las skills de contenido.
