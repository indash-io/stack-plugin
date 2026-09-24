# Template — Índice de productos del cliente

Copiá esta plantilla a `{slug}/assets/products/index.md` y completala con lo que devuelve `list_products` (`instructions/05_carpeta_local.md`). Una fila por producto. Si la tienda se conectó en el onboarding, el catálogo ya está en Indash; si no, el índice queda vacío y lo dice.

La **URL** y la **imagen de referencia** son los dos inputs que piden las skills de ejecución. Por eso este índice es el puente entre el onboarding y la producción de contenido.

El bloque de abajo es lo que va dentro del archivo del cliente.

---8<--- copiar desde acá ---8<---

```markdown
# Productos — {Nombre del cliente}

> Catálogo traído de Indash el {fecha} (workspace {slug}).
> Cada producto tiene URL + imagen: son los inputs de las skills de ejecución. SKUs prioritarios del onboarding marcados en Notas.

| Producto | URL | Imagen de referencia | Categoría | Precio | Notas |
|---|---|---|---|---|---|
| {nombre} | {url} | {url o assets/products/...} | {cat} | {precio} | {variantes/SKU, "prioritario" si está en `priority_skus`} |
| … | | | | | |

## Pendientes

- {Productos sin imagen / sin URL en Indash, si los hay}
- > PENDIENTE si la tabla está vacía: conectar la tienda en el onboarding (`connect_store`) o cargar los productos en la app.
```

---8<--- hasta acá ---8<---

## Notas de uso

- Si un producto no tiene imagen en Indash, marcalo en la columna y dejalo como pendiente: la skill de ejecución la va a pedir igual.
- Las imágenes no se bajan en el onboarding. Cuando una skill las use, van a `assets/products/`; no pegues binarios en el índice.
- Mantené el nombre del producto **exacto** como viene de Indash (las skills no lo traducen ni lo abrevian).
