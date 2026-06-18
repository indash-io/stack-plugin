# UGC Stitched — Consistency playbook (character + product)

Cuando un brief pide **multi-shot UGC con la misma persona y el mismo producto repartidos en N tomas stitched**, el riesgo #1 no es el motion — es el **drift de identidad y de escala** entre frame 0s. Esta nota es la checklist obligatoria antes de generar cualquier frame 0 #2 en adelante.

Aplica para: `stitched_multishot` con persona on-screen + producto on-screen en 2+ shots.

---

## Las 3 reglas no negociables

### 1. Identity lock sentence — una sola, copiada verbatim
Escribir UNA frase de identidad de la persona y pegarla **idéntica** en los N prompts de frame 0. No reescribirla, no parafrasearla, no "mejorarla" entre shots.

Plantilla:
```
[Nationality/ethnicity] [gender], age [N], [skin tone + texture detail],
[hair: length, color, style + accessory if any], [makeup state],
[wardrobe: garment, color, fit]. Keep the EXACT same face, skin, hair
and wardrobe as @Image1 reference — do not reinterpret features.
```

Ejemplo (Bloss UGC):
```
Mexican woman, 26, warm undertone skin with faint visible acne scars
on cheeks, dark wavy hair half-up in claw clip with pink headband,
no makeup, oversized white cotton t-shirt. Keep the EXACT same face,
skin, hair and wardrobe as @Image1 reference — do not reinterpret
features.
```

Esta frase va **al principio** del prompt de cada frame 0 ≥ shot 2. Antes de cualquier descripción de escena, acción o cámara.

### 2. Multi-ref identity stack (mín. 2 refs de la persona desde el shot 2)
Pasar el frame 0 del shot 1 como ref **no alcanza**. Hacer esto:

- **Antes de generar shot 2**: pedirle a Nano Banana un **portrait-only crop** del shot 1 (solo cara + cuello, fondo neutro). Subirlo como asset independiente.
- **Para frame 0 de shots 2..N**: pasar como `reference_image_urls` en este orden exacto:
  1. `portrait_crop_shot1.png` → identity lock
  2. `frame0_shot1.png` → wardrobe + lighting lock
  3. `product_image.png` → product fidelity lock
- En el prompt referenciarlas como `@Image1 (identity)`, `@Image2 (wardrobe/light)`, `@Image3 (product)`.

El portrait sin contexto fuerza al modelo a tratarlo como **identity reference**, no como "escena que reinterpretar".

> Excepción: si el MCP de generate_image limita a N refs, priorizar `portrait_crop` + `product_image` (sacar el wardrobe lock — la frase de identity lo cubre).

### 3. Product scale anchor — numérico, en cada frame 0
El producto cambia de tamaño en el cuadro entre shots. Nano Banana lo escala "para que el label se lea" si no se ancla. Resultado: bottle gigante irreal.

En cada frame 0 declarar:
- **Tamaño real del producto**: `"bottle ~12cm tall"` (o lo que sea)
- **Proporción del cuadro**: `"occupying roughly X% of frame height"`
- **Anchor de escala humano**: `"label height equal to [referencia anatómica visible en el cuadro]"`

Ejemplos por framing:
| Framing | Anchor sugerido |
|---|---|
| Producto en mano, medium shot | `"occupying ~15% of frame height, bottle height matches woman's palm length"` |
| Producto en encimera primer plano | `"occupying ~25% of frame height, label height equals half the woman's chin-to-forehead distance"` |
| Producto macro hero | `"fills 60-70% of frame height, label perfectly legible, no distortion"` |

---

## Trampas comunes (evitar by default)

### Espejos con identidad doble
Pedir "ella + su reflejo" en un mismo frame = 2 caras que tienen que matchear entre sí Y con la ref previa. Casi siempre falla.

**Reglas:**
- Si necesitás espejo → mostrar **solo el reflejo** (ella de espaldas) O **solo a ella de frente** con el espejo desenfocado/insinuado.
- Nunca pedir ambas caras nítidas en el mismo frame.

### Saltos grandes de pose/framing entre shots consecutivos
De "frente a cámara MS" a "perfil lateral MS con mirror" es un salto donde Nano Banana reinterpreta identidad.

**Regla:** entre shots consecutivos, mantener al menos 2 de estas 3 variables iguales:
- Framing (MS / MCU / CU)
- Ángulo (frontal / 3/4 / perfil)
- Pose general (mano arriba / aplicación / espejo / etc.)

Si el brief exige cambiar las 3, agregar un **shot puente** o aceptar el riesgo de drift y avisar al user antes de gastar.

### Wardrobe drift silencioso
El t-shirt cambia de cuello, el headband cambia de color, el clip aparece/desaparece. Nano Banana micro-edita sin avisar.

**Regla:** la identity lock sentence incluye wardrobe **explícito y detallado**. Repetir verbatim. Si algo no se ve en un shot, igual mencionarlo ("headband visible at top of frame" o "headband off-frame but worn").

### Pasar el frame 0 anterior crudo sin portrait crop
El frame 0 entero incluye fondo + acción + producto + cara. El modelo distribuye atención. La cara compite con el resto.

**Regla:** desde shot 2, el portrait crop dedicado va **antes** que el frame 0 completo en el array de refs.

---

## Checklist operativa (correr antes de cada frame 0 ≥ shot 2)

- [ ] ¿Tengo la identity lock sentence escrita y voy a pegarla verbatim?
- [ ] ¿Generé y tengo a mano el portrait crop del shot 1?
- [ ] ¿Los refs van en orden: identity → wardrobe → product?
- [ ] ¿Referencié cada ref como `@ImageN` en el prompt con su rol?
- [ ] ¿Declaré el tamaño del producto con anchor numérico + anatómico?
- [ ] ¿Mantengo ≥ 2 de las 3 variables (framing/ángulo/pose) iguales al shot anterior?
- [ ] ¿Si hay espejo, evité doble cara nítida?
- [ ] ¿Wardrobe descripto en la identity lock matchea el shot 1 al pie de la letra?

Si alguna falla → arreglar antes de gastar el render.

---

## Cuándo cortar y proponer alternativa al user

Si después de la checklist seguís viendo riesgo alto (ej. brief pide 4 cambios bruscos en 15s con producto + persona + locación nueva por shot), **frenar y proponer**:

- "El brief tal cual tiene riesgo alto de drift de identidad entre los shots X e Y. Propongo: A) suavizar el shot Y para mantener framing similar, o B) aceptar el riesgo y regenerar si sale mal (costo adicional)."

Mejor pedir antes que entregar un shot 3 con cara distinta.
