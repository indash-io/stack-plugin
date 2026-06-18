# Ejemplo GOOD — Product reveal multi-shot 12s (Kling 3.0)

**Input del usuario:**
> "Necesito un video para Reels mostrando unas zapatillas nuevas, ángulos distintos, con un poco de narrativa, 12 segundos."

---

# Paquete de video — Zapatillas hero multi-shot

## 1. Análisis de escena
- **Tipo de contenido:** product demo / narrative corto
- **Sujeto principal:** producto (zapatillas) + persona (pies y manos de un joven)
- **Plataforma:** Reels
- **Aspect ratio:** 9:16
- **Mood:** urbano-clean, ritmo medio, luz tarde
- **Asumidos:** zapatilla blanca con detalles verde oliva (ajustar al modelo real que estés promocionando); locación skate-park/calle urbana

## 2. Recomendación de modelo
**Elegido: Kling 3.0**

Razón: 12s + 3 shots narrativamente conectados + consistencia de producto (misma zapatilla idéntica entre tomas) = Kling 3.0 Element Consistency + Multi-Shot Storytelling. Veo 3.1 queda afuera por cap de 8s.

## 3. Estructura
- **Shots:** multi-shot, 3 tomas
  - Shot 1 (0-4s): close-up producto en caja, mano entra, levanta zapatilla
  - Shot 2 (4-8s): orbit lento alrededor de la zapatilla suspendida en altura de cintura
  - Shot 3 (8-12s): zapatillas puestas, caminando sobre asfalto húmedo, pull-out lento
- **Frames de referencia:** first frame (Shot 1) + last frame (Shot 3 final)
- **Razón first/last:** el arco narrativo tiene un estado inicial claro (zapatilla en caja, contexto indoor) y uno final claro (zapatilla puesta, calle) que queremos anclar para que el modelo no derive
- **Duración total:** 12s — 3 beats de 4s cada uno, cómodo para Kling
- **Aspect ratio:** 9:16

## 4. Prompts de Nano Banana

### First frame
```
Overhead close-up of an open shoe box on a concrete floor in warm late afternoon indoor light spilling from a window out of frame on camera-left. Inside the box: a single fresh white leather-and-mesh sneaker with olive green accents on the tongue and heel tab, black rubber outsole, white laces loosely tied. The box is matte black with minimal white sans-serif branding printed on the inner lid. A young man's tanned right hand with short clean nails enters from the top of the frame, fingers just grazing the tongue of the sneaker. 9:16 vertical, overhead angle tilted 10 degrees from true top-down. Shot on Sony a7siii with 35mm lens, photorealistic, shallow depth of field with the sneaker in perfect focus, subtle film grain, matte color grade with slight green-teal push in the shadows.
```

### Last frame
```
Low-angle ground-level shot, camera on wet asphalt pointing upward at a 20-degree tilt. Same young man (tanned skin, short dark hair barely visible at top of frame) wearing the same sneakers from the first frame — fresh white leather-and-mesh with olive green accents, black rubber outsole. He is mid-stride, right foot planted on wet asphalt with a shallow reflection of the sole, left foot lifted in motion blur. Dark slim cropped jeans ending above the ankle. Urban background out of focus: blurred outlines of a graffitied concrete wall and a yellow street light just coming on. Late afternoon turning dusk, moody blue-grey ambient with warm sodium streetlight rim on camera-right. 9:16 vertical, low-angle. Shot on Sony a7siii with 35mm lens, photorealistic, shallow depth of field, subtle film grain, matte color grade with slight green-teal push.
```
**Qué cambia respecto al first frame:**
- Ubicación: interior → exterior urbano
- Ángulo: overhead → low-angle
- Iluminación: warm indoor → dusk blue + sodium rim
- Estado de la zapatilla: en caja → puesta en pie del usuario
- Lo que se mantiene: identidad del producto, color grade, aspecto cinematográfico, 9:16, lens

## 5. Prompt de video

**Modelo:** Kling 3.0
**Audio nativo:** on — SFX diegéticos + ambiente urbano agregan autenticidad
**Frames de referencia:** first + last

```
Three-shot sequence, 12 seconds total, 9:16 vertical. The same white sneaker with olive green accents (as shown in first-frame reference) and the same young man appear across all shots — maintain identity.

Shot 1 (0-4s): Opens on the overhead close-up of the sneaker in the open black shoe box (as first-frame reference). At 1s, the young man's right hand lifts the sneaker slowly out of the box over 2 seconds, fingers pinching the tongue near the laces. Camera holds steady overhead. Soft cardboard rustle, faint leather creak. Quiet interior room tone.

Shot 2 (4-8s): Cut to the same sneaker suspended at waist height against a blurred indoor wall, held from behind by the man's hand out of focus. Camera does a slow 90-degree orbit around the sneaker over 4 seconds, revealing the side profile, then the heel tab with olive accent, then the outsole tread. Warm late afternoon indoor light from camera-left, rim light from a window behind. Diegetic: very faint ambient hum, shoe material subtle creak. No music yet.

Shot 3 (8-12s): Cut to low-angle ground-level shot on wet asphalt (as last-frame reference). The man walks toward camera wearing the same sneakers. Three full strides visible, right-left-right, each step creating a subtle splash on the wet asphalt. Camera pulls out slowly by 40cm over 4 seconds, maintaining low angle. Dusk blue ambient with a warm sodium streetlight rim from camera-right. Diegetic: wet-asphalt footstep splashes (three clear beats), distant muffled traffic, a single car horn far away at 10s. A low-bpm lo-fi bassline fades in from 8s to 12s (non-diegetic underscore, subtle).

Closing state (as last-frame reference): mid-stride, right foot planted on wet asphalt with reflection, left foot lifted in motion blur, streetlight rim warming the scene.

Duration: 12 seconds. 9:16 vertical.
```

## 6. Parámetros técnicos
- **Duración:** 12s
- **Aspect ratio:** 9:16
- **Resolución sugerida:** 1080p
- **Audio nativo:** on
- **Frames de referencia:** first + last
- **Modo (Kling):** Master (prompts largos con múltiples beats requieren más capacidad de adherencia)

## 7. Diálogo
N/A — sin diálogo. Audio: SFX de cardboard, leather creak, footstep splashes + ambiente urbano dusk + underscore lo-fi tenue desde Shot 3.

## 8. Notas de riesgo
- **Qué puede salir mal en el primer intento:**
  1. La consistencia del modelo de zapatilla entre shots puede derivar (color, forma de accent).
  2. Los pasos en wet asphalt pueden salir con cadencia irregular o sin splash visible.
  3. El orbit de Shot 2 puede acelerarse o cortar ángulo.
- **Cómo mitigarlo si pasa:**
  1. Reforzar "identical sneaker to Shot 1" + regenerar. Si persiste, generar un frame intermedio con Nano Banana y usarlo como tercer anclaje.
  2. Agregar "three distinct footstep beats, each creating a visible water splash on wet asphalt" al Shot 3.
  3. Explicitar "camera performs a smooth 90-degree orbit, constant speed, taking the full 4 seconds" en Shot 2.
