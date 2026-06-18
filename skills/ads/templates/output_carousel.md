# Output Template — Carrusel (con generación directa vía Indash MCP)

Formato de entrega para CADA variación:

---

## Variación [N] — [Nombre corto del ángulo]

**Ángulo**: [1 línea]
**Formato**: Carrusel · [N tarjetas] · 1:1

### 📝 Primary Text general (común a todo el carrusel)
> [texto completo]
> *— [125 char visibles ↑] —*

### 🃏 Tarjetas

#### Tarjeta 1 — [rol narrativo: hook / problema / solución / prueba / CTA]

[ Imagen renderizada inline vía `Read` sobre archivo local `/tmp/ads/<slug>-<vN>-tN.png` ]

🔗 Link de descarga (Indash): `[URL del MCP]`

**Headline**: [texto] · `[N] char`
**Description**: [texto] · `[N] char`

<details>
<summary>Ver prompt de T1</summary>

```
[prompt]
```
**Referencias adjuntadas**: [Imagen N] → rol: [...]
</details>

---

#### Tarjeta 2 — [rol narrativo]

[idem estructura — imagen + headline + description + prompt colapsado]

---

(... hasta tarjeta N)

### 🎯 CTA general del carrusel
`[Botón de la lista oficial de Meta]` — [por qué]

---

## Notas finales
- Por qué carrusel y no estática
- Lógica narrativa entre tarjetas (problema → solución → prueba → CTA, o lo que aplique)
- **Orden de generación obligatorio si hay modelo/persona o look repetido**:
  1. Generar primero las tarjetas de "ejecución" (las que muestran el look completo, ej: T2)
  2. Pasar la salida buena de T2 como referencia adicional al MCP para T3, T4 → mantiene modelo, fondo, luz, peinado
  3. Hook (T1) y Recap (T5/última) se generan AL FINAL, ya con las salidas previas como source
- **Para el Recap/Grid**: NO regenerar los looks desde cero. Pasar al MCP las salidas finales de las tarjetas anteriores como source. Si el modelo igual inventa detalles → armar el grid manualmente en Canva/Photoshop.

## Checklist de consistencia (antes de entregar)
- [ ] Cada prompt de tarjeta lista TODOS los ítems del outfit Y los que NO van (no belt, no jewelry, etc.)
- [ ] Las tarjetas con modelo recurrente recibieron la salida previa como ref de identidad
- [ ] El prompt del Recap incluyó la directiva "do not modify, do not add elements, treat previous outputs as locked source"
- [ ] Las imágenes generadas mantienen la paleta del brandkit (chequeo visual rápido)

## Cómo pedir ajustes
> *Para editar una tarjeta: decime variación + nº de tarjeta + qué cambiar (ej: "V1-T3 cambiá el fondo a beige").*
> *Para ver el prompt usado: "mostrame el prompt de V2-T1".*
> *Para regenerar una tarjeta igual con otra semilla: "reroll V1-T2".*
