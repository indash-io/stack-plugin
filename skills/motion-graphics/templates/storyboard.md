# <Marca> — <pieza> (<duración> s, <ancho>×<alto>)

**Pedido:** <una línea con las palabras de la persona> · **Rama:** sitio | app | brief
**Grilla:** <BPM> BPM · beat <s> · compás <s> · primer downbeat en <s>
**Música:** <tema, versión, offset, dónde cae el drop y el golpe final> | provisoria
**Voz:** <voz A (en Studio)> · <voz B (alternativa)> | sin voz

## Research

**UVP:** <una frase>

| Claim | Fuente | Literal en pantalla |
|---|---|---|

**No-claims:** <limitaciones que la pieza no puede contradecir>

**Marca:**
- paleta: <hex → rol>;
- tipos: <familia → archivo>;
- logo: <archivo y versiones>;
- vocabulario: <sí / nunca>;
- símbolos: <símbolo → pilar>.

## Concepto

<3–4 líneas: el problema como comedia, el giro, cómo se muestra el producto, el cierre>

## Escenas

| t | Escena | En pantalla | Voz | Movimiento (eventos con su tiempo) | SFX | Fuente del material |
|---|---|---|---|---|---|---|
| 0.0–3.0 | Hook | | | | | |

## Captions

<dónde aparecen y por qué (solo donde la voz difiere del título)>

## Audio

- Stems: `assets/audio/{music,vo,sfx}.wav`, generados con `audio-src/`.
- `data-volume`: voz <v> · música <v> · SFX <v>.
- Loudness medido: <LUFS · dBTP>.

## Comandos

```bash
npx hyperframes preview --background
npx hyperframes check
npx hyperframes render --quality draft --output renders/draft-a.mp4
npx hyperframes render --quality high --output renders/<slug>.mp4   # solo con OK
```
