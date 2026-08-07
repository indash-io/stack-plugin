# Agencia ecommerce — cutaways CGI + chilango = alucinación

**Setup:**
- Brief: 2 ads × 15s cada uno para una agencia de e-commerce (México/USA/Europa), anonimizada.
- Talent: hombre mexicano 33, chilango, navy crewneck, oficina warm daylight.
- Idioma: español chilango con audio nativo Seedance ON.
- Modelo: Seedance 2.0 ambos clips.
- Resultado: usuario lo descartó — "hay tomas que no van" + "la voz tampoco tan bien".

---

## Qué falló

### 1. Cutaways CGI / motion graphics no son trabajo para Seedance

**Clip A shot 3 (11–15s):** "Cutaway to a clean dark blue background. Four white minimalist line icons appear in sequence and then move toward a central hub with a soft blue glow: a gear (strategy), a color palette (design), a megaphone (ads), and a bar chart (data). The icons converge into the hub with a subtle ripple, no brand logos, no wordmarks."

**Clip B shot 1 (0–6s):** "Cutaway to a clean stylized world map graphic over a dark blue background, glowing white nodes lighting up sequentially over Mexico, the United States and Europe, thin animated lines connecting the nodes. Small generic e-commerce icons softly appearing near the nodes."

Ambos cutaways pidieron al modelo **animar motion graphics abstractos** — algo para lo que NO está entrenado. Seedance 2.0 está entrenado mayormente en footage real (personas, objetos físicos, espacios). Cuando le pedís motion graphics genera:
- Iconos derivados / incorrectos (engranaje con dientes irregulares, megáfono raro)
- Mapa con países en lugares equivocados o distorsionados
- Animaciones sin "snap" — convergencia confusa, líneas que se cruzan mal
- Tipografía inventada en los iconos
- Color palette inconsistente con el resto del clip

**Comparación:** los talking head shots del mismo talent en los mismos clips (shots 1 y 2 del Clip A, shots 2 y 3 del Clip B) **rindieron bien** — porque son footage real. Los cutaways fueron la parte que tiró el video abajo.

### 2. Acento chilango / mexicano todavía no validado como porteño

La regla 33 del framework lista chilango como "OFF default conservador". Lo probamos en este ad con ON + receta similar a la porteña:

```
NATIVE AUDIO: ON. Male voice in DISTINCT MEXICAN Spanish (central Mexico "chilango" accent) —
fully pronounced "s", "ll"/"y" as [ʝ] (NOT porteño "sh"), "tú" never "vos",
melodic central-Mexican intonation, mid-30s confident expert tone.
```

Resultado: la voz salió **menos creíble que el porteño del caso de lip plumper**. Posibles causas:
- El descriptor fonético del chilango no es tan distintivo en el dataset como el del porteño.
- "Mid-30s confident expert tone" salió más plano / locutor genérico que natural mexicano hablando.
- Las líneas formales ("socio de crecimiento") arrastraron la voz a registro corporate, no UGC.

**Conclusión:** chilango sigue OFF hasta validación adicional con un caso más simple (1 talking head, frase corta, registro casual).

### 3. Líneas largas (>8 palabras) y registro formal-corporate

Líneas del brief:
- "No te mandamos tareas sueltas. Somos tu socio de crecimiento." (11 palabras + jerga corporate)
- "Estrategia, diseño, ads y data, todo jalando parejo." (8 palabras + "jalando parejo" suena forzado)
- "Más de trescientas marcas confían en un solo equipo." (9 palabras + claim numérico)
- "Súmate a las más de trescientas. Diagnóstico gratis." (9 palabras + claim)

Problemas:
- **Largo:** Seedance pierde sync limpio en frases >8 palabras. La cara articula bien las primeras palabras y se desfasa al final.
- **Corporate/marketing register:** "socio de crecimiento", "todo jalando parejo", "diagnóstico gratis" suenan a copy de landing, no a persona hablando en UGC. El modelo TTS interno de Seedance los pronuncia con cadencia de locutor, no de conversación natural.

---

## Reglas destiladas

### A. **Cutaways de motion graphics → NO pedírselos a Seedance.**

Si el guión necesita un cutaway gráfico (mapa con nodos, iconos animados, dashboard, ilustración con animación), el camino correcto es:

1. **Generar el frame estático** con Nano Banana (o Figma/Photoshop si tiene que respetar branding específico).
2. **Animarlo en CapCut / After Effects:** Ken Burns, fade-in secuencial de elementos, particles, masks.
3. **Pedir a Seedance SOLO los shots de footage real** (talking head, manos, producto, ambient).

**Excepción:** cutaway de objeto físico real (un celular vibrando, una mano agarrando un producto, una pantalla de laptop mostrando algo) — eso sí lo hace bien Seedance porque es footage. La línea es: **¿esto se podría filmar con una cámara real?** Si sí → Seedance. Si requiere After Effects → fuera de Seedance.

### B. **Acentos no-porteño → default OFF + lipsync hasta validación.**

Solo porteño y neutro LATAM están validados con audio nativo ON. Chilango, mexicano del norte, cubano, chileno, español de España siguen OFF. Cuando el cliente pide acento no validado:
- Hacer el video con `generate_audio: false` + `lips move in full natural articulation as if speaking, no native audio dialogue generation`.
- Generar la voz aparte con ElevenLabs (tienen voces buenas mexicanas, cubanas, españolas).
- Lipsync en post con HeyGen V4 o Sync.so.

### C. **Líneas de diálogo ≤8 palabras + registro natural.**

Si el cliente entrega un script con frases largas o muy "corporate":
- **Cortarlas** en oraciones de ≤8 palabras antes de meterlas al prompt.
- **Reescribirlas en registro conversacional UGC** (acordá esto con el cliente antes de generar — no es libertad creativa, es viabilidad técnica del medio).
  - "Somos tu socio de crecimiento" → "Te ayudamos a crecer."
  - "Todo jalando parejo" → "Todo en un solo equipo."
- Si el cliente exige las frases originales tal cual: **OFF + voz aparte + lipsync** (B arriba). El TTS pro maneja largos sin perder sync.

### D. **Validar audio nativo en variantes nuevas con un caso simple antes de meter en producción.**

Antes de aceptar un cliente con acento no-validado, ofrecer un test mínimo:
- 1 talking head 8s.
- 1 frase corta 5-6 palabras.
- Registro conversacional.

Si ese mini-test sale bien → escalar a producción. Si no → quedarse con TTS + lipsync.

---

## Cómo se hubiera hecho bien

Re-rendering del mismo brief aplicando las reglas:

- **Clip A**:
  - Shot 1 (0–5s) talking head — "Más de 300 marcas." (6 palabras, corto, claim limpio)
  - Shot 2 (5–10s) talking head — "Estrategia y diseño." (3 palabras + recurso de pausa)
  - Shot 3 (10–15s) talking head — "Ads y data en un solo equipo." (8 palabras)
- **Clip B**:
  - Shot 1 (0–5s) cutaway real-footage — mano de talent moviendo iPhone con mapa Google Maps físico en pantalla (footage real, NO motion graphics).
  - Shot 2 (5–10s) talking head — "Vendé más. Gana más." (4 palabras)
  - Shot 3 (10–15s) talking head — "Diagnóstico gratis. Link abajo." (5 palabras)

Voz: **OFF + lipsync en post** con TTS mexicano (ElevenLabs voz "Dario" o "Mateo"). Tono casual UGC editado por el cliente.

**Motion graphics en CapCut, no en Seedance:**
- Logo del cliente animado como overlay PNG.
- Texto en pantalla animado por shot.
- Mapa de servicios → ilustración estática en Nano Banana + animación de fade-in secuencial en CapCut.

---

## Casos relacionados

- `examples/bad/aerolinea_wordmark_text_rendering.md` — text rendering flojo de marcas no-dominantes (lección complementaria: si el cutaway necesita branding específico, hacerlo fuera de Seedance).
- `examples/good/lip_plumper_porteno_22s.md` — caso donde audio nativo Seedance + porteño rindió bien (el extremo opuesto).
- `examples/good/es_neutro_15s.md` (por documentar) — caso donde audio nativo Seedance + neutro LATAM rindió bien.

---

## Reglas que aplican (y/o se actualizaron por este caso)

- **Regla 33 actualizada:** chilango y mexicano siguen OFF — caso documentado en este file.
- **Regla 41 nueva:** cutaways de motion graphics fuera de Seedance, dentro de CapCut/Nano Banana.
- **Regla 42 nueva (si se documenta):** líneas de diálogo ≤8 palabras + registro conversacional. Reescribir scripts corporate antes de meterlos al prompt.