# Volaris — wordmark "volants" en vez de "volaris" (text rendering fail)

**Setup:**
- Brief: Video aerolínea Volaris honeymoon Riviera Maya, 15s.
- Producto/marca: Volaris (Airbus A319/A320 livery con wordmark lowercase "volaris" magenta en fuselaje blanco).
- Modelo: Seedance 2.0.
- Resultado v1: fuselaje del avión decía **"volants"** en vez de **"volaris"**.

---

## Qué falló

V1 del prompt tenía descripción textual detallada de la livery:
> "white fuselage; on the forward fuselage near the cockpit the lowercase wordmark reads V-O-L-A-R-I-S spelled 'volaris' in a MAGENTA-PINK color"

Sin embargo Seedance interpoló el wordmark como `volants`. Razón: **Volaris es una marca regional latinoamericana sin presencia dominante en el dataset de Seedance**. Para marcas dominantes (Coca-Cola, Apple, Boeing) el wordmark sale bien por presencia. Para regionales, el modelo **inventa** algo que "parece" un wordmark de aerolínea pero deriva al deletreo.

Razones adicionales:
- Sin imagen real del avión como reference, el modelo solo tiene la descripción de texto.
- El wordmark Volaris no tiene una tipografía que el modelo conozca por nombre.

---

## Solución que funcionó

**Workflow corregido en v3:**

1. **WebSearch + WebFetch** para encontrar imagen real del Volaris en Wikimedia Commons:
   ```
   File:XA-VOP_Volaris_Airbus_A319-133LR_"Fernando"_(9617326955).jpg
   ```

2. **Descarga directa con curl** desde la URL de upload.wikimedia.org.

3. **Generar stills intermedios** con Nano Banana usando la foto real como reference (estos stills tuvieron wordmark "volaris" perfectamente legible).

4. **Lanzar render Seedance v3** con 4 references:
   - `@Image1` = anchor pareja cast.
   - `@Image2` = foto real del Volaris desde Wikimedia.
   - `@Image3` = still BOARDING generado en paso 3 (wordmark crisp).
   - `@Image4` = still RAMP generado en paso 3 (wordmark crisp).

5. **Cláusula anti-derivación explícita** en el prompt:
   ```
   BRAND LOCK: aircraft must match @Image2/@Image3/@Image4.
   Wordmark spelled v-o-l-a-r-i-s.
   DO NOT spell "volants" / "valaris" / "volair".
   Magenta + white only.
   ```

Las 3 variantes erradas (`volants`, `valaris`, `volair`) las saqué de los intentos previos donde el modelo ya las había generado. Listarlas en negativo le da al modelo señales muy específicas de qué evitar.

---

## Plan B documentado

Mientras esperaba el v3 (que se atascó >1h en cola), generé los **2 shots críticos del avión (boarding + ramp) como stills aparte** con Nano Banana usando la foto real de Wikimedia como reference. Esos stills:
- Tienen wordmark "volaris" 100% legible.
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