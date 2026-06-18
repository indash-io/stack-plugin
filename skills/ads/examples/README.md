# Examples — Good & Bad

Banco de referencias para que la skill calibre qué entregar y qué evitar.

## Cómo se usa (en el workflow de la skill)

Antes de proponer conceptos (paso 3 STRATEGY), la skill escanea esta carpeta:
- `good/` → ads que rindieron / estéticamente correctos / fieles al producto → **inspiración**
- `bad/` → ads con errores concretos (producto distorsionado, claim falso, paleta off-brand, conteos errados) → **línea roja**

Filtra por **marca** (si está en el nombre del archivo) y por **categoría** (suplementos, mobiliario, comida, electrónica, etc.).

## Estructura por ejemplo

Cada imagen va acompañada de un `.md` con el MISMO nombre. Ejemplo:

```
good/
├── vits-omega3-comparativa.png
└── vits-omega3-comparativa.md
```

El `.md` usa el template de `_TEMPLATE.md`.

## Cómo agregar un ejemplo nuevo

1. Pegá la imagen en `good/` o `bad/` con un nombre tipo `<marca>-<producto>-<mecanica>.png` (ej: `vits-pack-starter-4-frascos.png`).
2. Duplicá `_TEMPLATE.md`, renombralo igual que la imagen pero con `.md`, y completalo.
3. Listo. La próxima corrida ya lo tiene en cuenta.

## Naming sugerido

- `vits-omega3-sello-autoridad.png`
- `suma-electrolitos-ugc-deportista.png`
- `hongo-sillon-nube-aspiracional.png`

Marca al principio = fácil filtrar por workspace de Indash.
