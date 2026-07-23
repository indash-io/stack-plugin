# Template — Índice de productos del cliente

Copiá esta plantilla a `{slug}/assets/products/index.md` y completala con los productos traídos del MCP de Indash en Discovery. Una fila por producto.

La **URL** y la **imagen de referencia** son los dos inputs que piden `carruseles` y `stories-nano-banana`. Por eso este índice es el puente entre el onboarding y la producción de contenido.

El bloque de abajo es lo que va dentro del archivo del cliente.

---8<--- copiar desde acá ---8<---

```markdown
# Productos — {Nombre del cliente}

> Catálogo traído del MCP de Indash el {fecha}. Fuente: Indash ({handle/ID}).
> Cada producto tiene URL + imagen: son los inputs de las skills de carrusel y stories.

| Producto | URL | Imagen de referencia | Categoría | Precio | Notas |
|---|---|---|---|---|---|
| {nombre} | {url} | {url o assets/products/...} | {cat} | {precio} | {variantes/SKU} |
| … | | | | | |

## Pendientes

- {Productos sin imagen / sin URL en Indash, si los hay}
- > ⚠️ Si la tabla está vacía: conectar Indash y/o linkear el cliente para traer el catálogo.
```

---8<--- hasta acá ---8<---

## Notas de uso

- Si un producto no tiene imagen en Indash, marcalo en la columna y dejalo como pendiente — la skill de contenido la va a pedir igual.
- Guardá las imágenes que uses en `assets/products/` o linkealas al Drive; no pegues binarios pesados en el índice.
- Mantené el nombre del producto **exacto** como viene de Indash (las skills no lo traducen ni lo abrevian).
