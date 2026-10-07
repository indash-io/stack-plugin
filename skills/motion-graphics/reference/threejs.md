# Three.js dentro de HyperFrames

Usalo donde suma algo que el CSS no da: el logo en volumen, un mundo persistente, una
lluvia de objetos, una tarjeta con brillo. Para todo lo demás alcanza el DOM.

## Carga

r147, el build global (sin módulos). Va en `assets/vendor/` y se carga en el `<head>` del
`index.html`, después de GSAP:

```html
<script src="assets/vendor/three.min.js"></script>
<script src="assets/vendor/SVGLoader.js"></script>       <!-- logo e íconos extruidos -->
<script src="assets/vendor/RoomEnvironment.js"></script> <!-- reflejos PBR -->
<!-- bloom, en este orden: CopyShader, LuminosityHighPassShader, EffectComposer, ShaderPass, MaskPass, RenderPass, UnrealBloomPass -->
<!-- (los shaders antes del composer, el composer antes de los passes: si no, el global no existe todavía) -->
```

## Renderer

```js
const renderer = new THREE.WebGLRenderer({ canvas, antialias: true, alpha: true, preserveDrawingBuffer: true });
renderer.setPixelRatio(1);
renderer.setSize(W, H, false);
renderer.outputEncoding = THREE.LinearEncoding;  // los hex de la marca salen exactos
renderer.toneMapping = THREE.NoToneMapping;      // sin esto, la paleta se lava
```

## Que lo maneje el timeline

Al hacer seek, HyperFrames no dispara los `onUpdate`. Por eso la escena se dibuja desde
un setter que GSAP tweenea:

```js
const driver = { _t: 0 };
Object.defineProperty(driver, "t", { get() { return this._t; }, set(v) { this._t = v; draw(v); } });
tl.fromTo(driver, { t: 0 }, { t: D, duration: D, ease: "none" }, 0);
```

`draw(t)` es una función pura del tiempo: posiciona todo a partir de `t` y renderiza.
No guarda estado entre frames: nada de `+= velocidad`.

El mismo patrón sirve para los contadores y cualquier número que cambie.

## El WebGL1 de Studio

El render headless tiene WebGL2. **El preview de Studio puede dar un contexto WebGL1
pelado.** Lo que en el render anda, en Studio puede tirar cientos de errores o no dibujar
nada:

| En WebGL1 sin extensiones | Qué hacés |
|---|---|
| `InstancedMesh` → "ANGLE_instanced_arrays" en cada frame | Meshes comunes que comparten geometría y material (150 sobres andan bien) |
| `MeshStandardMaterial` no compila (falta `OES_standard_derivatives`) y solo se ven las sombras | `const pbr = renderer.capabilities.isWebGL2 \|\| renderer.extensions.has("OES_standard_derivatives")`. Con `pbr`, Standard + `RoomEnvironment`; sin `pbr`, Phong |
| Mipmaps en texturas que no son potencia de 2 | `generateMipmaps = false` y `minFilter = THREE.LinearFilter` |

Verificalo con la consola de Studio abierta en cada escena 3D (`instructions/06_build.md`).

## Logo extruido desde el SVG real

```js
const g = new THREE.Group();
g.scale.set(1 / W_SVG, -1 / W_SVG, 1 / W_SVG); // 1 unidad = ancho del logo; el SVG tiene y hacia abajo
paths.forEach((d) => {
  const data = svgl.parse(`<svg xmlns="http://www.w3.org/2000/svg"><path d="${d}"/></svg>`);
  const geo = new THREE.ExtrudeGeometry(THREE.SVGLoader.createShapes(data.paths[0]),
    { depth: 26, bevelEnabled: true, bevelThickness: 4, bevelSize: 2.5, bevelSegments: 3, curveSegments: 24 });
  geo.translate(-W_SVG / 2, -H_SVG / 2, -13);
  g.add(new THREE.Mesh(geo, [capMat, sideMat]));  // [tapas, costados]
});
```

- **Tapas** con `MeshBasicMaterial` del color exacto del logo: así se lee igual que el plano.
  **Costados** en Standard/Phong, un tono más oscuro.
- La escala negativa va en el **grupo**, nunca en la geometría: si no, las normales se invierten.
- **El giro de entrada nunca pasa de ~75° (≈ 1.3 rad)**: más allá se ve el dorso y el
  logo queda espejado. Ejemplo: `ry = -1.3 * (1 - easeOut(p))`.
- Las letras salen de los paths del logo real (el SVG del sitio o `pdf_paths.py`), nunca
  de una tipografía parecida.

## Handoff 3D → DOM

Cuando el logo 3D tiene que aterrizar en un elemento HTML (el logo de una pantalla real,
el lockup final):

```
px por unidad, en un plano a distancia d de la cámara = H / (2 · d · tan(fov / 2))
```

1. Calculá la posición y la escala en mundo que dan exactamente la caja en px del
   elemento DOM.
2. Llevá el 3D ahí con rotación 0.
3. En ese frame, cortá: el DOM aparece y el 3D desaparece en el mismo `t`.

Si las cajas coinciden al píxel, el corte no se ve.

## Texturas en algunas caras

Para un objeto con una imagen solo en el frente (un sobre con el sello de la marca),
remapeá las UVs para que solo la cara +z use la textura y el resto un color plano. Es una
geometría compartida, no un material por cara.
