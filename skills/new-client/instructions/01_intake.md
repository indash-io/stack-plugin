# 01 — Intake y workspace

Salís de acá con dos cosas: el **nombre de la marca** y su **workspace en Indash**. Nada más. Todo lo demás (tienda, Drive, Instagram, material) lo pide el onboarding en su orden, con su pregunta literal; si lo pedís acá, lo pedís dos veces.

---

## 1. El nombre

Si no lo tenés, es la única pregunta de este paso:

> ¿Cómo se llama la marca? Con eso la busco en Indash y arrancamos.

Si la persona ya arrancó con material ("acá está todo lo de Acme", una carpeta), el nombre suele estar en el mensaje o en la carpeta. No lo repreguntes.

---

## 2. Gate del conector

Aplicá el gate del conector `indash` de la política del stack. Si no está conectado, frená en una sola intervención:

> Para cargar la marca necesito el conector **Indash** conectado. Conectalo con `/mcp` (o desde el panel de conectores) y seguimos.

Con el conector, verificá que existan `get_brand_onboarding`, `update_brand_onboarding`, `create_onboarding_uploads` y `run_brand_onboarding_action`. Si falta alguna, o contestan que no están disponibles en ese transporte, el conector está desactualizado: pedile a la persona que lo reconecte, o que haga el onboarding en la app. No cargues la marca por otro camino.

`analyze_brand` y `confirm_brand_analysis` no son parte del gate: si no están, el paso 3 se saltea y se avisa (ver `04_analisis.md`).

---

## 3. El workspace

El onboarding se escribe en un workspace. Un material cargado en el equivocado contamina los briefs de otra marca, así que esto se resuelve antes de la primera escritura.

```
¿En qué workspace?
├── La carpeta actual tiene un `CLAUDE.md` de cliente con el workspace
│     → usalo, y confirmá que el nombre coincide con la marca que te nombraron
├── `list_workspaces` devuelve uno solo (el cliente, con su cuenta)
│     → ese
├── Devuelve varios, o quien carga es de Indash
│     → `search_workspaces` por el nombre
│         ├── Un resultado claro → ese
│         ├── Varios parecidos ("Acme", "Acme Test", "Acme LATAM") → preguntá cuál, mostrando los nombres
│         └── Ninguno → la marca no existe en Indash todavía (abajo)
```

Antes de la primera escritura, nombralo en una línea: "cargo en **Acme**". Si la persona corrige, cambiás y volvés a leer.

### Si la marca no existe en Indash

No hay tool para crear un workspace: lo crea alguien de Indash desde la app. Decilo tal cual y frená; sin workspace no hay onboarding, y tampoco carpeta local (no tendría de dónde salir).

> **Acme** no está en Indash todavía. El workspace lo crea el equipo de Indash desde la app; cuando exista, seguimos acá mismo y cargamos todo.

Si quien carga es de Indash, alcanza con que lo cree en la app y vuelva. Mientras tanto no juntes material "para después" en la conversación: se pierde al cerrar la sesión. Lo que sí sirve es decirle en una línea qué conviene tener a mano cuando exista: brand book y logos, fotos de producto, piezas publicadas que sí los representan y piezas que no, reseñas tal cual, capturas de las preguntas que más les hacen, y cómo funciona el producto.

---

## Lo que NO hacés acá

- No pedís URL de la tienda, Drive, Notion, Instagram ni el brand kit. El onboarding los pide en su paso.
- No pedís que describan la marca.
- No creás carpetas. La carpeta local es opcional y va al final (`05_carpeta_local.md`).

Con nombre y workspace → pasá a `02_onboarding.md`.
