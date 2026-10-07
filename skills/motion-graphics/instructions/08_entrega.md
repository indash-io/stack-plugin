# 08 — Entrega

Objetivo: que la persona pueda ver la pieza en un clic y decidir lo pendiente sin abrir
el código.

## El mensaje, en este orden

1. **Una línea de estado**: qué es (duración, formato), dónde está y que pasa el `check`.
2. **Link de Studio**: `http://127.0.0.1:<puerto>/#project/<carpeta>`. Si se cae, se
   levanta con `npx hyperframes preview --background` desde la carpeta.
3. **Draft**: la ruta del MP4 y las alternativas (`…-voz-b.mp4`, proyectos hermanos con
   su link).
4. **Qué dice**: la UVP en una frase y la historia escena por escena, en pocas líneas.
5. **Sonido**: qué música es y por qué esa, dónde cae el golpe final, la voz elegida y
   el loudness medido.
6. **Cómo se revisó**: cuántos drafts, qué se arregló (lo más importante, no todo) y qué
   se verificó en Studio.
7. **Para decidir o confirmar**:
   - supuestos que tomaste;
   - datos de cuenta demo visibles;
   - lo que quedó como placeholder (badges, tipografías sustitutas);
   - la variante de end card elegida y cuáles quedan.
8. **Lo que no se pudo verificar**: el audio no se escuchó, solo se midió. Pedile que lo
   escuche en Studio.
9. **Render final**: el comando, y que corre cuando dé el OK.

```bash
npx hyperframes render --quality high --output renders/<slug>.mp4
```

Después del render final, corré `mix.py measure --file` sobre ese archivo y pasale el
número a la persona.
