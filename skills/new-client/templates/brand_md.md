# Template — brand.md (la marca, en palabras del cliente)

Copiá esta plantilla a `{slug}/assets/brand-kit/brand.md`. Es la lectura larga de la marca para quien abre la carpeta por primera vez: qué vende, cómo funciona, quién le compra y cómo habla. Todo sale del onboarding en Indash (`get_brand_context`) y de lo confirmado del análisis. **Sin adjetivos tuyos**: si una sección pide algo que el cliente no dijo, va `> PENDIENTE: …` con dónde se carga. No reemplaza al `CLAUDE.md` (operativo) ni al `brand-kit.md` (ficha técnica).

El bloque de abajo es lo que va dentro del archivo del cliente.

---8<--- copiar desde acá ---8<---

```markdown
# {Nombre del cliente} — Marca

Escrito desde el onboarding en Indash el {fecha}. Lo que está entre comillas es literal del cliente.

## Qué vende
{Tienda, catálogo y SKUs prioritarios (`priority_skus`), en una línea o dos. — o PENDIENTE: sin tienda ni productos en Indash}

## Cómo funciona
{Mecanismo por producto, literal. — o PENDIENTE: cargar el mecanismo en el onboarding}

## Quién le compra
{El avatar confirmado del análisis (5 a 8 líneas, sale solo de las reseñas). — o PENDIENTE: análisis sin confirmar / sin reseñas cargadas}

## Qué le preguntan antes de comprar
{Las objeciones confirmadas del análisis, una por línea con su frecuencia y un ejemplo literal. — o PENDIENTE: análisis sin confirmar / sin objeciones cargadas}

## Cómo habla
{El perfil de voz confirmado: persona, largo de frase, emojis, nombres del producto, claims y CTAs que repiten, estructura del caption. — o PENDIENTE: análisis de voz sin confirmar}
- **Frases textuales que se pueden usar (verbatims confirmados):** {una por línea, entre comillas — o "ninguna confirmada"}
- **Qué no decir:** {`rules.forbidden_claims` literal — o "ninguno cargado"}

## Esto somos / esto no somos
- Piezas que sí los representan (`corpus_on_brand`): {N}, en Indash.
- Piezas que no (`corpus_off_brand`): {N}, en Indash. Pesan tanto como las otras.
- Ganadoras: {N pagas, N orgánicas}.

## Qué usaban antes y qué no funcionó
{`product.prior_failures` literal — o "no cargado"}

## Material de marca (en esta carpeta)
- **Logos:** `assets/logos/` — {qué hay, o PENDIENTE}
- **Tipografías:** `assets/fonts/` — {qué hay, o PENDIENTE}
- **Brand book / guidelines:** `assets/brand-kit/` — {archivo, o "no hay"}
- **Ficha técnica (paleta + tipografía + reglas):** `assets/brand-kit/brand-kit.md`
```

---8<--- hasta acá ---8<---
