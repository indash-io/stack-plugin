# 01 — Intake

Primer paso. Validás que tenés lo mínimo para dar de alta al cliente. **Si falta el nombre, frenás acá.**

---

## Input obligatorio

1. **Nombre del cliente** — tal como lo vas a usar para nombrar la carpeta y el contexto. De acá derivás el slug en kebab-case (ej: "Acme Foods" → `acme-foods`).

Si no lo tenés, pedilo y frená:

> ¿Cómo se llama el cliente? Con eso armo la carpeta y todo el contexto.

---

## Inputs recomendados (pedilos en UNA sola pregunta consolidada)

No son obligatorios para arrancar, pero si los tenés el onboarding queda completo en una pasada. Pedilos juntos, no de a uno:

- **Identificador del cliente en Indash** — el ID, slug o handle con el que el cliente existe en el MCP de Indash. Es lo que te deja traer sus productos en Discovery. Si no lo sabés, en Discovery probás buscar por nombre.
- **URL del sitio / tienda** — para analizar marca (paleta, tipografía, tono) y como fallback de productos.
- **Link a su Google Drive** — carpeta del cliente donde viven assets y entregables.
- **Link a su Notion** — brief, base de conocimiento o board del cliente.
- **Logo / imágenes de marca** — si los tenés a mano, mejor; si no, quedan como placeholder.

### Pregunta consolidada sugerida

> Dale, doy de alta a **{cliente}**. Para dejarlo completo, si los tenés a mano pasame (lo que falte lo dejo como pendiente):
> - ID o handle del cliente en Indash (para traer sus productos)
> - URL de su tienda/sitio
> - Link a su Drive y/o Notion
>
> Con el nombre solo ya puedo arrancar igual.

---

## Cómo manejar entrada incompleta

- **Solo el nombre** → avanzá. En Discovery intentás encontrar el cliente en Indash por nombre; lo que no consigas queda como placeholder en el `CLAUDE.md`.
- **Nombre + ID de Indash** → ideal. Avanzás directo a Discovery con todo para traer productos.
- **Sin ID pero con URL** → usás la URL para marca y como fallback de catálogo, y dejás anotado que falta linkear el cliente en Indash.

---

## Lo que NO hacés en Intake

- ❌ No pedís el brand kit completo (paleta, tipografía) — eso lo extraés vos en Discovery de la URL/imágenes.
- ❌ No pedís todo de a una pregunta por vez. Una sola consolidada.
- ❌ No empezás a crear carpetas todavía. Eso es Scaffold, después del Discovery.

---

## Tono al pedir input

Directo, breve, rioplatense. Sin AI-speak ni saludos largos.

- ✅ *"¿Cómo se llama el cliente? Con eso arranco."*
- ❌ *"¡Hola! Estoy aquí para ayudarte con el onboarding. ¿Podrías por favor proporcionarme el nombre del cliente? 😊"*

Si tenés todo lo necesario → pasá a `02_discovery.md`.
