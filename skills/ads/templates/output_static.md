# Output Template — Imagen Estática (con generación directa vía Indash MCP)

Formato de entrega para CADA variación:

---

## Variación [N] — [Nombre corto del ángulo]

**Ángulo**: [1 línea]
**Formato**: Imagen estática · [aspect ratio: 1:1 / 4:5 / 9:16]

### 🖼 Imagen generada

[ Imagen renderizada inline vía `Read` sobre el archivo local descargado a `/tmp/ads/<slug>-<vN>.png` ]

🔗 Link de descarga (Indash): `[URL del MCP]`

### 📝 Copy de Meta

**Primary Text**:
> [texto completo]
> *— [125 char visibles ↑] —*

**Headline**: [texto] · `[N] caracteres`

**Description**: [texto] · `[N] caracteres`

**CTA**: `[Botón de la lista oficial de Meta]` — [por qué este CTA, 1 línea]

<details>
<summary>Ver prompt usado</summary>

```
[prompt completo que se mandó al MCP, en inglés]
```

**Referencias adjuntadas al MCP**:
- [Imagen N del input] → rol: [producto / estilo / paleta]

</details>

---

(repetir bloque por cada variación)

## Notas finales del entregable
- 1 línea sobre el formato elegido y por qué
- 1 línea sobre el ángulo común si las variaciones lo comparten
- Sugerencia de testing si aplica

## Cómo pedir ajustes
> *Para editar una imagen: decime el número de variación + qué cambiar (ej: "V2 más oscura, sacá el texto del medio").*
> *Para ver el prompt usado: "mostrame el prompt de V3".*
> *Para regenerar igual con otra semilla: "reroll V1".*
