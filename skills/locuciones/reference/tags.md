# Formato del guion: acotaciones, tags y dos voces

Todo lo que dirige la lectura va **adentro del `script`** (más el `style` de la
pieza). La tool lo parsea así — exacto, sin variantes:

## 1. Líneas

- El guion se divide por **líneas**. Las vacías se ignoran.
- Una línea sin nada especial **continúa la anterior** (misma voz, misma
  dirección). Cortar en líneas no mete pausas: para eso está la puntuación o
  `<short pause>`.

## 2. Acotación por línea — `(así) texto`

- Un paréntesis **al inicio** de una línea es dirección para **esa línea**:

  ```
  (bajando la voz, cómplice) Esto no se lo cuentes a nadie.
  (volviendo a la energía normal) Pero a vos sí.
  ```

- Se suma al `style` de la pieza, no lo reemplaza.
- Un paréntesis **a mitad de frase se habla**: `Envío gratis (a todo el país)`
  → el modelo dice "a todo el país". Si querés dirección, va al inicio.
- Una acotación **sola en su línea** se aplica a la siguiente hablada:

  ```
  (pausa larga, cansado)
  Bueno. Ya está.
  ```

## 3. Tags de vocalización — `<tag>` en el punto exacto

Ocurren donde los ponés, no se hablan y no cuentan para el costo.

| Tag | Qué hace |
|---|---|
| `<short pause>` / `<long pause>` | Silencio corto / largo. Mejor que `...` cuando querés controlarlo |
| `<breath>` | Toma aire. Antes de un CTA o de una frase larga |
| `<laugh>` / `<chuckle>` | Risa / risita. Uno por línea como máximo |
| `<sigh>` | Suspiro. Cansancio, alivio, "por fin" |
| `<gasp>` | Sorpresa |
| `<cough>` / `<throat-clearing>` | Carraspeo. Para "atención" o humor |
| `<groan>` | Queja. Humor de "otra vez lo mismo" |

Interjecciones de escucha (en diálogos, la voz que no habla): `|mhm|`, `|yeah|`.

Regla: **un tag por emoción real**. Si una persona no lo haría en esa frase,
no va.

## 4. Puntuación = ritmo

- `.` corta. `,` respira. `…` deja colgado. `!` sube. `?` sube al final.
- MAYÚSCULAS no gritan de forma confiable: pedí "gritando" en la acotación.
- Números y siglas se leen **literal**: escribí `veinte por ciento`, `dos por
  uno`, `Instagram`, `ce-be-de` si querés que deletree.

## 5. Dos voces — `speakers` + `Nombre:`

- Declarás `speakers` (exactamente 2): `{ name, voice, style? }` cada uno.
- Cada línea empieza con **el nombre y dos puntos**:

  ```
  Ana: ¿Lo probaste?
  Tomi: (dudando) Todavía no…
  Es que no sabía si era para mí.
  Ana: (riéndose) <chuckle> Es para todos. Probalo.
  ```

- El nombre se compara sin distinguir mayúsculas. La línea sin nombre sigue
  con el último que habló.
- **La primera línea tiene que nombrar a alguien** — si no, la tool rechaza el
  item (sin cobrar).
- Un `Palabra:` que **no** es speaker declarado se habla como texto
  (`Nota: el envío es gratis.` la dice el speaker actual).
- El `style` de cada speaker es su forma de hablar en toda la escena; la
  acotación por línea es el momento.

## 6. El `style` de la pieza (fuera del guion)

Una o dos frases, lenguaje natural, en este orden: **tono, ritmo, energía,
registro, a quién le habla, dónde se escucha**.

```
Lectura de anuncio de Instagram, sonriendo, rápida pero clara, registro
cercano con voseo, le habla a una mujer de 30 que scrollea de noche.
```

Con eso el modelo ya está en escena; las acotaciones solo marcan los cambios.

**Lo que NO va en el `style`** (Google lo dice explícito): edad, género,
nombre, ni un cambio permanente de acento. Eso es **de la voz** — se elige en
`list_voices` o se diseña en `design_voice`. Un `style` que diga "un argentino
de 20 años" no lo va a hacer de forma confiable; una voz diseñada con esa
descripción, sí.
