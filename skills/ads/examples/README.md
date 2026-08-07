# Examples — Good & Bad

Banco de referencias para que la skill calibre qué entregar y qué evitar.

## Cómo se usa (en el workflow de la skill)

Antes de proponer conceptos (paso 3 STRATEGY), la skill escanea esta carpeta:
- `good/` → ads que rindieron / estéticamente correctos / fieles al producto → **inspiración**
- `bad/` → ads con errores concretos (producto distorsionado, claim falso, paleta off-brand, conteos errados) → **línea roja**

Filtra por **categoría** (suplementos, mobiliario, comida, electrónica, etc.), que es lo que va al principio del nombre del archivo.

## Estructura por ejemplo

Cada imagen va acompañada de un `.md` con el MISMO nombre. Ejemplo:

```
good/
├── suplementos-omega3-comparativa.png
└── suplementos-omega3-comparativa.md
```

El `.md` usa el template de `_TEMPLATE.md`.

## Cómo agregar un ejemplo nuevo

1. Pegá la imagen en `good/` o `bad/` con un nombre tipo `<categoria>-<producto>-<mecanica>.png` (ej: `suplementos-pack-4-frascos.png`).
2. Duplicá `_TEMPLATE.md`, renombralo igual que la imagen pero con `.md`, y completalo.
3. Listo. La próxima corrida ya lo tiene en cuenta.

## Naming sugerido

- `suplementos-omega3-sello-autoridad.png`
- `bebidas-electrolitos-ugc-deportista.png`
- `mobiliario-sillon-nube-aspiracional.png`

Categoría al principio = fácil filtrar por workspace de Indash. (Los ejemplos de este
banco van anonimizados: se nombra la **categoría**, nunca al cliente.)
