# Aerolínea — el wordmark sale mal deletreado (text rendering fail)

**Setup:**
- Brief: video de aerolínea honeymoon Riviera Maya, 15s.
- Producto/marca: aerolínea regional latinoamericana (anonimizada) — Airbus A319/A320 con livery de wordmark lowercase magenta sobre fuselaje blanco.
- Modelo: Seedance 2.0.
- Resultado v1: el fuselaje del avión mostraba una **variante mal deletreada** del wordmark (letras cambiadas, palabra que "parece" pero no es).

---

## Qué falló

V1 del prompt tenía descripción textual detallada de la livery:
> "white fuselage; on the forward fuselage near the cockpit the lowercase wordmark reads `<B-R-A-N-D>` spelled '`<brand>`' in a MAGENTA-PINK color"

Sin embargo Seedance interpoló el wordmark a otra palabra. Razón: **es una marca regional latinoamericana sin presencia dominante en el dataset de Seedance**. Para marcas dominantes (Coca-Cola, Apple, Boeing) el wordmark sale bien por presencia. Para regionales, el modelo **inventa** algo que "parece" un wordmark de aerolínea pero deriva al deletreo.

Razones adicionales:
- Sin imagen real del avión como reference, el modelo solo tiene la descripción de texto.
- El wordmark de la marca no tiene una tipografía que el modelo conozca por nombre.

---

## Solución que funcionó

**Workflow corregido en v3:**

1. **WebSearch + WebFetch** para encontrar una foto real de un avión de esa aerolínea en Wikimedia Commons (buscar por modelo de avión + nombre de la aerolínea; las fotos de spotters están bajo licencia libre).

2. **Descarga directa con curl** desde la URL de upload.wikimedia.org.

3. **Generar stills intermedios** con Nano Banana usando la foto real como reference (estos stills tuvieron el wordmark perfectamente legible).

4. **Lanzar render Seedance v3** con 4 references:
   - `@Image1` = anchor pareja cast.
   - `@Image2` = foto real del avión desde Wikimedia.
   - `@Image3` = still BOARDING generado en paso 3 (wordmark crisp).
   - `@Image4` = still RAMP generado en paso 3 (wordmark crisp).

5. **Cláusula anti-derivación explícita** en el prompt:
   ```
   BRAND LOCK: aircraft must match @Image2/@Image3/@Image4.
   Wordmark spelled <l-e-t-r-a-p-o-r-l-e-t-r-a>.
   DO NOT spell "<variante errada 1>" / "<variante errada 2>" / "<variante errada 3>".
   Magenta + white only.
   ```

Las variantes erradas que van en el negativo **se sacan de los intentos previos**, donde el modelo ya las había generado. Listar literalmente los deletreos equivocados que ya viste le da al modelo señales muy específicas de qué evitar.

---

## Plan B documentado

Mientras esperaba el v3 (que se atascó >1h en cola), generé los **2 shots críticos del avión (boarding + ramp) como stills aparte** con Nano Banana usando la foto real de Wikimedia como reference. Esos stills:
- Tienen el wordmark 100% legible.
- Se pueden pegar en CapCut como freeze frames de 1.5-2s reemplazando los shots problemáticos del v1.
- Garantizan entrega HOY sin depender de que la cola se libere.

---

## Reglas que aplican (y/o se actualizaron por este caso)

- **Regla 39:** marcas no-dominantes + text rendering = imagen real como reference obligatoria. Si no hay producto cargado en Indash, buscar en Wikimedia Commons.
- **Regla 40:** Plan B Ken Burns / stills + freeze frame para shots problemáticos cuando la cola Seedance se atasca.
- **Regla 32:** producto con packaging específico = imagen real obligatoria como reference (extendido a marcas en general).

---

## Lección destilada

Para cualquier marca que no sea top-tier global, **asumir** que Seedance va a inventar el wordmark si no le pasás foto real. Buscar la foto **antes** de redactar el prompt, no después de ver el render fallar.
