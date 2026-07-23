# 03 — Scaffold

Creás la estructura de carpetas estándar del cliente en el **directorio de trabajo actual**. La estructura exacta está en `templates/folder_structure.md` — seguila tal cual.

---

## Antes de crear

1. **Derivá el slug** del nombre del cliente en kebab-case (minúsculas, sin acentos, espacios → guiones). Ej: "Acme Foods" → `acme-foods`, "Café del Sur" → `cafe-del-sur`.
2. **Chequeá si la carpeta del cliente ya existe** en el directorio actual.
   - Si **ya existe** → frená y preguntá:
     > Ya hay una carpeta `{slug}`. ¿La actualizo (completo lo que falte sin pisar lo existente) o creás otra con otro nombre?
   - Si **no existe** → seguí.

---

## Qué crear

Creá las carpetas y los archivos base según `templates/folder_structure.md`. En concreto:

- La carpeta raíz del cliente (`{slug}/`).
- Las subcarpetas estándar:
  - `brand/` con `logos/`, `typographies/` y `assets/` (acá aterrizan los assets de marca de Discovery).
  - `assets/products/` con `referencias/`.
  - `exports/` con `carruseles/` y `stories/`.
  - `briefs/`.
- Los archivos base vacíos o con su plantilla:
  - El `CLAUDE.md` del cliente → lo escribís en el paso 4 (Client Context), pero podés crear el archivo acá.
  - `assets/brand-kit/brand.md` (narrativa de marca) y `assets/brand-kit/brand-kit.md` (resumen estructurado) → los completás en el paso 4 con lo que extrajiste.
  - El índice de productos (`assets/products/index.md`) → lo completás en el paso 5.
  - Un `.gitkeep` en las carpetas que arrancan vacías (incluidas `assets/logos/`, `assets/fonts/`, `assets/brand-kit/`), para que la estructura quede versionable.

---

## Cómo crearla

Usá las herramientas de filesystem disponibles (crear directorios y archivos). Creá todo de una y después verificá que el árbol quedó completo mostrándolo.

No descargues binarios pesados ni copies imágenes grandes acá: las imágenes de referencia se linkean (Drive) o se guardan a demanda cuando se produce contenido.

---

## Reglas de Scaffold

1. **No pises** archivos existentes sin avisar (regla 5 del SKILL.md).
2. **Estructura fiel** a `templates/folder_structure.md` — ni de más ni de menos.
3. **Slug consistente** entre la carpeta y el `CLAUDE.md`.
4. Dejá la estructura **versionable** (carpetas vacías con `.gitkeep`).

Con la estructura creada → pasá a `04_client_context.md`.
