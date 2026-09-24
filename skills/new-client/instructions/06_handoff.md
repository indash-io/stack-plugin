# 06 — Handoff

Cerrás diciendo qué quedó, qué falta y con qué se sigue. Corto: la persona ya vio el inventario y el análisis; esto es el resumen para volver mañana.

---

## Qué mostrás

1. **Dónde quedó**: el workspace y `onboarding.url`. Es el mismo onboarding de la app: lo que falte se puede seguir acá o allá.
2. **El veredicto**, literal (`verdict_text`), y si hubo `pending[]` al cerrar, qué es. Sin porcentajes.
3. **El análisis**: qué ramas quedaron confirmadas, cuáles rechazadas y cuáles `pending` (y que las pendientes no se usan hasta que alguien las confirme). Si no se corrió, por qué: sin material suficiente, o la tool no está en el conector.
4. **La carpeta local**, solo si se armó: el árbol real (no uno de memoria) y los placeholders del `CLAUDE.md`, cada uno con dónde se completa.
5. **Pendientes accionables**, una línea cada uno: un `authorize_url` de Tiendanube sin abrir, un import de tienda que sigue corriendo, audios sin transcribir por tope diario, la lectura de Instagram sin confirmar.

---

## Con qué se sigue

```
¿Qué quiere hacer la persona ahora?
├── Planificar el período → `content-brief`: "armá el brief de octubre".
│     Lee este onboarding (y lo confirmado del análisis) desde Indash. No necesita la carpeta.
├── Producir una pieza suelta → la skill de ejecución: `carruseles`, `stories-nano-banana`,
│     `ads`, `ugc-generator` / `ugc-video-prompts`, `all-videos`, `email-marketing-ecomm`.
│     Desde la carpeta local heredan el `CLAUDE.md`; sin carpeta, piden URL + imagen del producto.
├── Seguir cargando → esta misma skill, cuando quiera. Retoma por `next[]` sin repreguntar.
└── Nada por ahora → dejale `onboarding.url` y terminá.
```

Una línea de ejemplo, no un menú de todo el stack:

> Quedó cargado en **Acme** (`{onboarding.url}`): puede arrancar, con Mecanismo pendiente. Análisis: voz, objeciones y verbatims confirmados; avatar rechazado; sistema visual pendiente. Cuando quieras, "armá el brief de octubre" y sale de acá.

---

## Reglas

1. **Nada inventado**: el árbol es el que está en disco, el veredicto es el que devolvió la tool.
2. **Sin porcentajes ni "casi listo"**: compuertas y pendientes con nombre.
3. **Handoff concreto**: una skill y un pedido de ejemplo, no la lista entera.
4. Si en la sesión hubo fricción con la skill (la persona te corrigió un paso, pidió rehacer algo), sugerí `/save-learnings` en una línea. Si salió derecho, no lo menciones.
5. Rioplatense, breve, sin relleno.
