# 04 — El análisis de la marca

Con el material cargado, el server produce lo **derivado** que el onboarding deja afuera a propósito: el perfil de voz, las objeciones priorizadas, los verbatims, el avatar y el sistema visual. Lo hace `analyze_brand`, con el material del cliente y nada más. Vos no lo escribís, no lo editás y no lo confirmás: lo mostrás, y decide la persona.

Por qué existe este circuito: es la única vez que algo que no dijo el cliente entra al onboarding. Por eso cada rama nace `pending`, y **el agente de briefs no la ve hasta que un humano la confirme**. Sin confirmación, los briefs se arman solo con la materia prima, como si el análisis no existiera.

---

## 1. Cuándo se ofrece

```
¿`analyze_brand` está en el conector?
├── No → salteá el paso. Decilo en una línea: "El análisis de la marca todavía no está
│        en este conector; se corre después, desde acá o desde la app." Seguí a la carpeta local.
└── Sí
    ¿`inventory.verdict` es `can_start` o `can_start_with_pending`?
    ├── No → no se ofrece. Lo que frena está en el inventario (Assets o Mecanismo);
    │        ya se lo dijiste en el cierre. No insistas.
    └── Sí → ofrecelo, con el porqué en dos líneas:
             "Con esto puedo correr el análisis: saca de tus reseñas y tus piezas cómo
              habla la marca, qué objeciones se repiten, frases textuales, un avatar y
              el sistema visual. Nace pendiente y no se usa en ningún brief hasta que
              vos lo confirmes. ¿Lo corro?"
```

No necesita `complete`. Si `state.analysis` ya tiene ramas `pending` de una corrida anterior (aparece en `next[]`), no ofrezcas correrlo de nuevo: `state.analysis` no trae el resumen, así que llamá `analyze_brand` sin `force` (no cambió nada, devuelve lo que ya está sin correr) y andá a la sección 3.

---

## 2. Correr

`analyze_brand` con `workspace_id`, sin `force`. Mirá el `status`:

| Vuelve | Qué hacés |
|---|---|
| `summary_markdown` y `derived` | Sección 3. |
| `running` | Tarda más de un minuto. Decilo, seguí con lo que quede (o la carpeta local) y consultá `get_brand_onboarding` → `state.analysis`. Cuando deje de estar corriendo, volvé a llamar `analyze_brand` sin `force`: no cambió nada, así que devuelve el resultado que ya está en vez de correr de nuevo. |
| `not_enough_material` | Sin reseñas y sin corpus no hay de dónde sacar nada. Decí qué falta con las palabras de la respuesta y no insistas: si la persona quiere cargarlo, vuelve a `02_onboarding.md`; si no, se sigue sin análisis. |
| Un error por tope (un análisis cada 10 minutos por workspace) | Decí cuánto falta y seguí. No mandes `force`. |

`force: true` solo cuando la persona pide rehacerlo sabiendo que el anterior se pisa. Después de cargar material nuevo no hace falta: el server detecta que cambió algo y corre solo.

---

## 3. Mostrar rama por rama

Mostrá `summary_markdown` tal cual, no tu resumen del resumen. Después, una rama por vez y una pregunta por rama, en este orden:

| Rama | `decisions` | Qué mirar con la persona |
|---|---|---|
| Perfil de voz | `voice_profile` | Persona (vos / tú / usted), largo de frase, emojis, cómo nombran el producto, claims y CTAs que repiten, estructura del caption. ¿Así escriben? |
| Objeciones | `objections` | Cada objeción con su frecuencia, categoría y los ejemplos que la sostienen. ¿Son las preguntas que les hacen de verdad? |
| Verbatims | `verbatim` | Frases exactas de las reseñas, sin editar. Una frase que la persona no reconoce como de sus reseñas es motivo para rechazar la rama. |
| Avatar | `audience_profile` | Cinco a ocho líneas escritas solo con lo que dicen las reseñas. ¿Describe a quien les compra, o a quien les gustaría que les compre? |
| Sistema visual | `visual_system` | Paleta en hex, tipografías con su rol, reglas del logo. Si salió de las piezas y no de un brand book, lo dice: ¿coincide con el brand book que tienen? |

Cada rama se confirma o se rechaza **entera** (`"confirm"` | `"reject"`). No hay edición campo por campo, y vos no corregís el texto derivado:

```
La persona dice…
├── "Sí" / "así es" → `confirm`
├── "No" / "eso no es así" → `reject`. Preguntá qué falló solo si sirve para el material:
│     una objeción que no existe suele ser una reseña que no era suya;
│     un avatar equivocado suele ser reseñas de un solo producto.
│     Lo que se corrige es el material (más reseñas, otro corpus), y se vuelve a correr.
├── "Cambiá esto y confirmá" → no se puede editar lo derivado. Dos salidas, que las elija:
│     rechazar la rama, o confirmarla sabiendo que queda así.
└── "Después lo veo" → la rama queda `pending`. No la decidas vos.
```

Cuando la persona terminó de decidir, **una sola llamada** a `confirm_brand_analysis` con las decisiones que tomó. Las ramas sin decisión se omiten del objeto y quedan `pending`; decí cuáles, y que se pueden confirmar después desde acá o desde la app.

---

## 4. Lo que el análisis no es

- No reemplaza lo cargado. Va por debajo de la materia prima: si el perfil de voz dice "vos" y las 6 piezas que subieron dicen "tú", las piezas mandan y la rama se rechaza.
- No es un campo del onboarding. Nada de `summary_markdown` se copia con `set_text` a ningún campo, ni aunque la persona lo pida: para eso está la confirmación.
- No es fuente del `CLAUDE.md` de la carpeta local salvo lo confirmado, y eso llega solo por `get_brand_context` (`05_carpeta_local.md`).

Con las decisiones guardadas → preguntá por la carpeta local (`05_carpeta_local.md`).
