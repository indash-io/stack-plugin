# Voces: estudio, biblioteca y diseñadas

Tres fuentes, y las tres se pasan igual: el `voice_id` tal cual en `voice` o en
`speakers[].voice` de `generate_speech`.

| Fuente | Qué es | Cuándo |
|---|---|---|
| **Estudio** (30) | Las fijas de Google, con un carácter de una palabra. Hablan cualquier idioma; el acento sale "neutro-ish" | Cuando el acento no es el punto, o para draftear |
| **Biblioteca** (`list_voices`) | Cientos de voces prebuilt afinadas por idioma, acento, género, pitch, persona | Cuando el brief pide un idioma/acento concreto que una prebuilt ya trae (`language_codes: ["es-AR"]`) |
| **Diseñada** (`design_voice`) | Una voz nueva desde una descripción de rasgos permanentes: edad, género, timbre, acento, forma base de hablar. Queda guardada para el workspace, con sample | Cuando la persona es específica ("una argentina de veinte años, voz clara, porteña") o cuando la marca quiere **su** voz y reusarla en todas las piezas |

**La regla que ordena todo:** edad, género, timbre y acento son **de la voz**;
el `style` de `generate_speech` es **de la lectura** (tono, ritmo, energía, a
quién le habla). Pedirle al `style` "que suene a un argentino de 20" no
funciona de forma confiable; diseñar esa voz, sí.

## Las 30 de estudio

Nombre y **carácter según Google** (es la única descripción oficial; el resto
lo pone la dirección).

Google **no publica género ni edad** de cada voz, y las dos cosas se mueven
bastante con el `style`. Regla: **si la voz no está decidida, hacé audición**
— una línea del guion en 2-3 candidatas como items `short` (10 créditos cada
una), y que la persona elija escuchando. No la elijas vos por el nombre.

| Voz | Carácter (Google) | Suele servir para |
|---|---|---|
| **Kore** | Firm | **Default.** Anuncio claro, marca que afirma, instrucción |
| Zephyr | Bright | Lifestyle luminoso, belleza, bienestar |
| Puck | Upbeat | UGC entusiasta, promo, unboxing |
| Charon | Informative | Explainer, demo de producto, "cómo funciona" |
| Fenrir | Excitable | Lanzamiento, gaming, "no lo puedo creer" |
| Leda | Youthful | Gen Z, TikTok, moda joven |
| Orus | Firm | Autoridad, B2B, finanzas |
| Aoede | Breezy | Viajes, verano, bebidas |
| Callirrhoe | Easy-going | Conversación relajada, testimonial |
| Autonoe | Bright | Retail, ofertas alegres |
| Enceladus | Breathy | Íntimo, ASMR, cosmética premium |
| Iapetus | Clear | Narración neutra, institucional |
| Umbriel | Easy-going | Podcast, charla entre amigos |
| Algieba | Smooth | Premium, perfumes, autos |
| Despina | Smooth | Lujo accesible, hogar, deco |
| Erinome | Clear | Salud, farmacia, instrucciones |
| Algenib | Gravelly | Rock, café, cerveza artesanal, "voz con historia" |
| Rasalgethi | Informative | Noticias, educación, tutoriales |
| Laomedeia | Upbeat | Promo con ritmo, fitness |
| Achernar | Soft | Bebés, sueño, cuidado |
| Alnilam | Firm | Deporte, rendimiento, CTA fuerte |
| Schedar | Even | Locución corporativa, IVR, narración larga |
| Gacrux | Mature | Voz "de experiencia", vinos, herencia |
| Pulcherrima | Forward | Directo a cámara, hook agresivo |
| Achird | Friendly | Atención al cliente, onboarding, "hola, soy…" |
| Zubenelgenubi | Casual | UGC natural, "te cuento", reseña |
| Vindemiatrix | Gentle | Mindfulness, maternidad, mascotas |
| Sadachbia | Lively | Kids, juguetes, eventos |
| Sadaltager | Knowledgeable | Experto que explica, tech, finanzas personales |
| Sulafat | Warm | Comida, familia, hogar, "volvé a casa" |

## La biblioteca extendida

`list_voices` con filtros. Lo útil: `language_codes` (BCP-47: `es-AR`, `es-MX`,
`es-419` para neutro latino, `es-ES`, `en-US`, `pt-BR`), `genders`
(`female` / `male` / `neutral`), `accents` (como los etiqueta Google:
"Argentine", "Mexican"…), `personas` ("Narrator", "Warm, Friendly"), `search`.
Devuelve `voice_id`, nombre, descripción, idioma, acento, género, pitch. **No
trae sample**: la audición es una línea del guion con `generate_speech`.

Con `include_library: false` solo devuelve las de estudio y las diseñadas del
workspace (útil para ver qué voces ya tiene el cliente).

## Voz diseñada

`design_voice` → `voice_…` + sample. Cómo se escribe la descripción, en este
orden y en una o dos frases: **edad, género, timbre/textura, acento regional,
forma base de hablar**. Ejemplos que funcionan:

- *"Una mujer argentina de veintipocos, voz clara con un poco de aire, acento
  porteño marcado, habla rápido y con seguridad, como recomendándole algo a
  una amiga."*
- *"Un hombre mexicano de unos cuarenta, voz grave y aterciopelada, acento de
  Ciudad de México suave, habla pausado y con autoridad tranquila."*
- *"Una voz neutra latinoamericana, mujer de treinta y tantos, media, limpia,
  sin regionalismo marcado, cadencia de narradora de documental."*

Lo que **no** va ahí: la emoción de una lectura concreta ("entusiasmada por la
promo") — eso es `style` en `generate_speech`, por pieza y por línea. Poné
`language_code` (`es-AR`) siempre: ancla el acento.

Cada diseño es **una voz nueva guardada** (200 por proyecto para todo Indash,
un año). Iterá con cabeza: cambiá un rasgo por vez, escuchá el sample, quedate
con una, `delete_voice` al resto. Y anotá el `voice_id` en el `CLAUDE.md` del
cliente bajo "Voz de marca", para que la próxima sesión no la vuelva a diseñar.

## Cómo se elige

1. **Del pedido y del `CLAUDE.md` del cliente** sacá tres adjetivos del tono
   (ej: *cálida, directa, joven*) y si hay un **acento/edad/género** que
   importe. Mirá si el `CLAUDE.md` ya tiene un `voice_id` de marca.
2. **Fuente**: sin acento específico → estudio. Con idioma/acento concreto →
   biblioteca (`list_voices` por `language_codes`). Con persona específica o
   voz de marca a reusar → diseñada.
3. **Shortlist de 2-3.** Una "segura" y una o dos con más carácter.
4. **Audición**: la línea más representativa del guion (el hook), misma
   dirección, en las 2-3 voces, en **una sola llamada** de items `short`. Si una
   es diseñada, su sample ya sirve de primera escucha.
5. La persona **escucha y elige**. Recién ahí generás el guion completo.

La misma voz con otro `style` es otra lectura: antes de descartar una, probá
cambiarle la dirección ("más lento, sonriendo, más íntimo"). Pero si lo que
falla es la edad, el género o el acento, cambiá de **voz**, no de `style`.

## Dos voces

Para una escena, combiná **contraste**: una Firm/Clear con una Upbeat/Casual,
una Warm con una Excitable. Dos voces del mismo carácter se confunden en el
oído. Y nombralas en el guion como personas (`Ana:`, `Tomi:`), no como
`Speaker 1:` — el modelo actúa mejor con nombres.
