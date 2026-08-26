#!/usr/bin/env python3
"""Edicion de videos UGC generados con IA — Indash Stack.

Dos modos:
    editar.py revisar <carpeta|clip...>      mide y reporta, no renderiza
    editar.py montar  <config.json>          hace la edicion completa

Las constantes de estilo salen de medir 21 ediciones manuales reales de un
editor del equipo (marca A n=10, marca B n=11), validadas despues en 4 marcas.
Ver SKILL.md para la procedencia de cada numero.

Corre con el python del venv que instala setup.sh (~/.indash/edicion-ugc/venv).
"""
import datetime, glob, json, os, re, shutil, subprocess, sys, unicodedata

# ---- reglas universales (medidas, no inventadas) ---------------------------
MAX_PAUSA    = 0.50   # decision del equipo (ago 2026): ritmo mas dinamico.
                      # Medido daba 0.76 (techo de 21 ediciones), pero a 0.50
                      # el video respira mejor. Cortar mas = mas saltos en plano.
TOLERANCIA   = 1.15   # solo se comprime si lo pasa con margen
TARGET_PAUSA = 0.45   # a cuanto se comprime
PLACA_DUR    = 1.50   # decision del equipo (ago 2026). Lo medido en 21
                      # ediciones daba 1.25-1.34 (la constante mas fuerte del
                      # corpus); se subio a 1.50 para que la placa respire un
                      # poco mas.
                      # Aplica SOLO a placas fijas: si es video manda su duracion.
UMBRAL_SIL   = "-25dB"
W, H, FPS    = 720, 1280, 24
BITRATE      = "6300k"  # con maxrate holgado; ver nota en el export

# subtitulos
SUB_SIZE     = 32     # calibrado: ancho de string real contra la referencia
SUB_PESO     = 600    # SemiBold. El editor pidio Regular, pero sus 21 videos
                      # son SemiBold: manda lo medido.
SUB_Y        = 1027   # centro vertical, promedio de ambas marcas
SUB_MAX_PAL  = 4      # 24/24 muestras caen entre 2 y 4 palabras
SUB_MAX_CHAR = 26
SUB_ANCHO_MAX = 640

# Frames de silencio que se dejan antes de que arranque la voz en cada clip.
# Los clips se generan desde el mismo still, asi que todos abren en la misma
# pose. Si se concatenan enteros, esa pose se repite en el empalme y se nota.
# Entrando justo antes de la voz, el clip 2 ya esta en movimiento al cortar.
LEAD_FRAMES = 3

# morph
MORPH_SOLAPE_OK = 0.15  # cuanto habla se puede comer para tapar un morph

# B-roll. Va SIEMPRE sobre el momento mas feo del dialogo, sea morph o no: un
# movimiento brusco da score alto sin llegar al umbral de morph y igual se nota.
# Posicion del bloque, medida en las 4 ediciones manuales con B-roll, como
# fraccion del dialogo:
#                    entra    sale
#   edicion 1         25.0%   70.4%
#   edicion 2         34.8%   75.3%
#   edicion 3         32.3%   69.8%
#   edicion 4         47.3%   73.2%
# El FINAL es el ancla: 70-75% en los cuatro. El inicio varia mucho (25-47%),
# asi que se deriva del final y del largo, no al reves.
# En los cuatro el bloque cae sobre la parte de beneficios/ingredientes, que es
# lo que se quiere ilustrar con producto.
BROLL_FIN  = 0.72   # donde TERMINA el bloque, como fraccion del dialogo
BROLL_LARGO = 0.40  # largo del bloque como fraccion del dialogo
                    # (medido: 26%, 37.5%, 40.5%, 45.4% — n=4, disperso)
BROLL_MIN_S = 2.50  # piso y techo absolutos, para que no se desmadre en
BROLL_MAX_S = 6.50  # videos muy cortos o muy largos
BROLL_SEP  = 2.00   # separacion minima entre dos tapones
BROLL_SNAP = 0.60   # Si un corte ya existente cae a menos de esto de un borde del
                    # B-roll, el borde se pega a ese corte. Si no, quedan dos
                    # cortes separados por unos pocos frames y el video trastabilla:
                    # se ve un corte, 3 frames de dialogo, y otro corte al B-roll.
                    # Los cortes que caen ADENTRO del bloque no molestan: los tapa.

# ---- entorno ---------------------------------------------------------------
# El script vive dentro del plugin (skills/edicion-ugc/scripts/), que es una
# cache que se pisa entera en cada auto-update. Por eso NADA mutable vive aca:
# el venv va a ~/.indash/ y el modelo de whisper a ~/.cache/.
AQUI     = os.path.dirname(os.path.abspath(__file__))
SETUP    = os.path.join(AQUI, "setup.sh")
VENV     = os.path.expanduser("~/.indash/edicion-ugc/venv")
MODELO_WHISPER = os.path.expanduser("~/.cache/whisper-cpp/ggml-large-v3-turbo.bin")
FUENTE_PREF = os.path.expanduser("~/Library/Fonts/Montserrat[wght].ttf")


def _buscar_fuente():
    """Montserrat: primero la variable que instala el cask, si no cualquier
    Montserrat instalada. Devuelve None si no hay ninguna."""
    if os.path.exists(FUENTE_PREF):
        return FUENTE_PREF
    for raiz in (os.path.expanduser("~/Library/Fonts"), "/Library/Fonts"):
        hits = sorted(glob.glob(os.path.join(raiz, "Montserrat*.ttf")) +
                      glob.glob(os.path.join(raiz, "Montserrat*.otf")))
        if hits:
            return hits[0]
    return None


FUENTE = _buscar_fuente() or FUENTE_PREF


def verificar_entorno(whisper=True, pillow=True, fuente=True):
    """Chequea las dependencias ANTES de tocar nada y falla con un mensaje
    accionable. Sin esto el error aparece 40 segundos despues, como traceback
    de PIL o como un mp4 de 0 bytes."""
    faltan = []
    for binario in ("ffmpeg", "ffprobe"):
        if not shutil.which(binario):
            faltan.append(f"{binario} (brew install ffmpeg)")
    if whisper:
        if not shutil.which("whisper-cli"):
            faltan.append("whisper-cli (brew install whisper-cpp)")
        if not os.path.exists(MODELO_WHISPER):
            faltan.append(f"el modelo de whisper en {MODELO_WHISPER} (1.5 GB)")
    if fuente and not _buscar_fuente():
        faltan.append("la fuente Montserrat (brew install --cask font-montserrat)")
    if pillow:
        try:
            import PIL  # noqa: F401
        except ImportError:
            faltan.append(f"Pillow — estas corriendo {sys.executable}; usa el "
                          f"python del venv: {VENV}/bin/python")
    if faltan:
        print("Falta parte del entorno de la skill edicion-ugc:\n")
        for f in faltan:
            print(f"  - {f}")
        print(f"\nCorrelo de una: bash {SETUP}")
        print("(es idempotente: si ya esta todo, no hace nada)")
        sys.exit(1)


# ---- convencion de carpetas del stack --------------------------------------
NOMBRE_CFG_MARCA = "edicion-ugc.json"
# Donde busca la config y la placa de la marca, en orden. `brand/` es la carpeta
# de config por cliente; `assets/` es donde `new-client` deja los assets de marca.
SUBCARPETAS_CFG   = ("brand", os.path.join("assets", "brand-kit"))
SUBCARPETAS_PLACA = ("brand", os.path.join("assets", "logos"))


def slugify(texto):
    texto = unicodedata.normalize("NFKD", texto).encode("ascii", "ignore").decode()
    texto = re.sub(r"[^A-Za-z0-9]+", "-", texto).strip("-").lower()
    return texto or "ugc"


def raiz_cliente(base):
    """La carpeta del cliente: la primera hacia arriba con `exports/` o un
    `CLAUDE.md` de marca. Los crudos suelen vivir en <cliente>/Crudo/."""
    d = os.path.abspath(base)
    for _ in range(5):
        if (os.path.isdir(os.path.join(d, "exports")) or
                os.path.isfile(os.path.join(d, "CLAUDE.md"))):
            return d
        padre = os.path.dirname(d)
        if padre == d:
            break
        d = padre
    return None


def _raices(base):
    """Carpetas donde se busca config y placa de marca, sin repetir."""
    cands = [os.path.abspath(base),
             os.path.dirname(os.path.abspath(base)),
             raiz_cliente(base),
             os.path.abspath(os.getcwd())]
    vistas, out = set(), []
    for c in cands:
        if c and os.path.isdir(c) and c not in vistas:
            vistas.add(c)
            out.append(c)
    return out


def buscar_config_marca(base, explicita=None):
    """Config por cliente: `brand/edicion-ugc.json` en la carpeta del cliente.

    Campos: marca, placa, marcas_whisper, producto, nota. Vive en la carpeta
    del CLIENTE, no en el plugin: el plugin es publico y no lleva datos de
    nadie. Formato documentado en templates/brand-edicion-ugc.example.json.
    """
    if explicita:
        p = os.path.abspath(os.path.expanduser(explicita))
        if not os.path.exists(p):
            print(f"   !! no existe la config de marca declarada: {p}")
            return {}, None
        return json.load(open(p)), p
    for raiz in _raices(base):
        for sub in SUBCARPETAS_CFG:
            p = os.path.join(raiz, sub, NOMBRE_CFG_MARCA)
            if os.path.exists(p):
                return json.load(open(p)), p
    return {}, None


def buscar_placa_marca(base):
    """`brand/placa.*` (o `assets/logos/placa.*`) de la carpeta del cliente."""
    for raiz in _raices(base):
        for sub in SUBCARPETAS_PLACA:
            for ext in EXT_IMG + EXT_VID:
                p = os.path.join(raiz, sub, "placa" + ext)
                if os.path.exists(p):
                    return p
    return None


def salida_por_defecto(base, slug):
    """`exports/videos/<AAAA-MM-DD>_<slug>_v<N>.mp4` de la carpeta del cliente.

    Convencion global del stack (hooks/context/stack-policy.md). Nunca pisa:
    si el nombre existe, sube la version.
    """
    raiz = raiz_cliente(base) or os.path.abspath(base)
    carpeta = os.path.join(raiz, "exports", "videos")
    os.makedirs(carpeta, exist_ok=True)
    hoy = datetime.date.today().isoformat()
    n = 1
    while os.path.exists(os.path.join(carpeta, f"{hoy}_{slug}_v{n}.mp4")):
        n += 1
    return os.path.join(carpeta, f"{hoy}_{slug}_v{n}.mp4")


def sh(cmd, binario=False):
    return subprocess.run(cmd, capture_output=True, text=not binario)


def dur(path):
    r = sh(["ffprobe", "-v", "error", "-show_entries", "format=duration",
            "-of", "csv=p=0", path])
    return float(r.stdout.strip())


def silencios(path):
    out = sh(["ffmpeg", "-i", path, "-af",
              f"silencedetect=n={UMBRAL_SIL}:d=0.15", "-f", "null", "-"]).stderr
    ini = [float(x) for x in re.findall(r"silence_start: ([\d.-]+)", out)]
    fin = [float(x) for x in re.findall(r"silence_end: ([\d.]+)", out)]
    return [(max(a, 0.0), b) for a, b in zip(ini, fin)]


def picos_scene(path, desde=0.0, hasta=None):
    cmd = ["ffmpeg", "-v", "error"]
    if desde:
        cmd += ["-ss", str(desde)]
    if hasta:
        cmd += ["-t", str(hasta - desde)]
    cmd += ["-i", path, "-filter_complex",
            "select='gt(scene,0.0001)',metadata=print:file=-", "-f", "null", "-"]
    r = sh(cmd)
    return [(round(float(t) + desde, 3), float(s)) for t, s in re.findall(
        r"pts_time:([\d.]+)[\s\S]{0,40}?scene_score=([\d.]+)", r.stderr + r.stdout)]


def morphs(path, ventana=None):
    """Devuelve (fin_morph_cabeza, [morphs sobre voz]).

    Calibra el umbral contra el ruido propio del clip: un clip con mucho
    movimiento tiene el piso mas alto. Ciego a las derivas graduales.

    Descarta los ultimos 0.3s: el ultimo frame de un clip generado casi siempre
    da pico, pero es artefacto de borde y cae en el empalme — no es un morph
    sobre voz que haya que tapar con B-roll.
    """
    p = picos_scene(path, 0.0, ventana)
    if not p:
        return 0.0, []
    total = ventana or dur(path)
    sc = sorted(s for _, s in p)
    umbral = max(sc[len(sc) // 2] * 20, 0.15)
    cabeza, medio = 0.0, []
    for t, s in p:
        if s <= umbral:
            continue
        if t <= 1.5:
            cabeza = max(cabeza, round(t + 1 / FPS, 3))
        elif t < total - 0.3:
            medio.append((t, round(s, 3)))
    return cabeza, medio


# ---- paso 1: recorte de silencio -------------------------------------------
def tramos_a_conservar(path):
    total, sil = dur(path), silencios(path)
    keep, cursor = [], 0.0
    for a, b in sil:
        a, b = max(a, 0.0), min(b, total)
        # cabeza y cola se van SIEMPRE: el video arranca y corta sobre la voz
        if a <= 0.05:
            cursor = max(cursor, b - 0.10)
            continue
        if b >= total - 0.05:
            keep.append((cursor, a + 0.15))
            cursor = total
            break
        if b - a <= MAX_PAUSA * TOLERANCIA:
            continue
        corte_ini = a + TARGET_PAUSA / 2
        keep.append((cursor, corte_ini))
        cursor = corte_ini + (b - a) - TARGET_PAUSA
    if cursor < total:
        keep.append((cursor, total))
    return [(round(a, 3), round(b, 3)) for a, b in keep if b - a > 0.05]


def aplicar_tramos(entrada, keep, salida, crf="16"):
    sel = "+".join(f"between(t,{a},{b})" for a, b in keep)
    sh(["ffmpeg", "-v", "error", "-i", entrada, "-filter_complex",
        f"[0:v]select='{sel}',setpts=N/{FPS}/TB[v];"
        f"[0:a]aselect='{sel}',asetpts=N/SR/TB[a]",
        "-map", "[v]", "-map", "[a]", "-c:v", "libx264", "-crf", crf,
        "-preset", "medium", "-c:a", "aac", "-b:a", "192k", salida, "-y"])


def peores_momentos(path, n, sep=BROLL_SEP):
    """Los n instantes mas feos del video, separados entre si.

    NO filtra por umbral de morph: el objetivo es tapar lo peor que haya, sea un
    morph, un movimiento brusco o un empalme raro. Descarta los bordes, donde el
    primer y el ultimo frame casi siempre dan pico por artefacto de encoding.
    """
    total = dur(path)
    picos = [(t, s) for t, s in picos_scene(path) if 0.3 < t < total - 0.3]
    elegidos = []
    for t, s in sorted(picos, key=lambda x: -x[1]):
        if len(elegidos) >= n:
            break
        if all(abs(t - t2) >= sep for t2, _ in elegidos):
            elegidos.append((round(t, 2), round(s, 4)))
    return elegidos


def mejor_tramo(path, largo):
    """Ventana mas estable de un B-roll: la de menor pico de movimiento.

    Los B-roll tambien se generan con IA y traen sus propios defectos, casi
    siempre al arranque o al final. En las ediciones manuales no se usan enteros
    justamente por eso: se agarra el pedazo que se ve bien. Esto automatiza esa
    eleccion.
    """
    total = dur(path)
    if largo >= total - 0.4:
        return 0.0
    picos = picos_scene(path)
    mejor, mejor_ini = None, 0.0
    ini = 0.2                                   # saltear el asentamiento inicial
    while ini + largo <= total - 0.2:
        dentro = [s for t, s in picos if ini <= t <= ini + largo]
        if dentro:
            # primero el pico mas bajo; a igualdad, el promedio mas bajo
            puntaje = (max(dentro), sum(dentro) / len(dentro))
            if mejor is None or puntaje < mejor:
                mejor, mejor_ini = puntaje, ini
        ini += 0.25
    return round(mejor_ini, 2)


def inicio_voz(path):
    """Segundo en que arranca la voz (fin del silencio de cabeza)."""
    for a, b in silencios(path):
        if a <= 0.05:
            return b
    return 0.0


def entrada_de_clip(path, morph_hasta=0.0):
    """Desde donde entrar al clip: LEAD_FRAMES antes de la voz, y siempre
    despues del morph de cabeza si lo hay."""
    voz = inicio_voz(path)
    corte = max(0.0, voz - LEAD_FRAMES / FPS)
    return round(max(corte, morph_hasta), 3)


def concat(clips, salida, desde=None):
    desde = desde or [0.0] * len(clips)
    if len(clips) == 1:
        cmd = ["ffmpeg", "-v", "error"]
        if desde[0]:
            cmd += ["-ss", str(desde[0])]
        cmd += ["-i", clips[0], "-vf",
                f"fps={FPS},scale={W}:{H},setsar=1", "-af", "aresample=48000",
                "-c:v", "libx264", "-crf", "16", "-preset", "medium",
                "-c:a", "aac", "-b:a", "192k", salida, "-y"]
        sh(cmd)
        return
    cmd, fc = ["ffmpeg", "-v", "error"], []
    for i, c in enumerate(clips):
        if desde[i]:
            cmd += ["-ss", str(desde[i])]
        cmd += ["-i", c]
        fc.append(f"[{i}:v]fps={FPS},scale={W}:{H},setsar=1[v{i}]")
        fc.append(f"[{i}:a]aresample=48000[a{i}]")
    enc = "".join(f"[v{i}][a{i}]" for i in range(len(clips)))
    fc.append(f"{enc}concat=n={len(clips)}:v=1:a=1[v][a]")
    cmd += ["-filter_complex", ";".join(fc), "-map", "[v]", "-map", "[a]",
            "-c:v", "libx264", "-crf", "16", "-preset", "medium",
            "-c:a", "aac", "-b:a", "192k", salida, "-y"]
    sh(cmd)


# ---- paso 5: placa ---------------------------------------------------------
EXT_IMG = (".png", ".jpg", ".jpeg", ".webp")
EXT_VID = (".mp4", ".mov", ".m4v", ".webm")
# La placa puede ser un video (outro animado). Se reconoce por el nombre para no
# confundirla con los clips de dialogo, que viven en la misma carpeta.
NOMBRES_PLACA = ("placa", "outro", "cierre", "endcard")


def _carpeta_logos(carpeta):
    """Busca una subcarpeta 'logo'/'placa' en la carpeta y en su padre.

    Los clips suelen vivir en <cliente>/Crudo/ y los logos en <cliente>/Logos/,
    o sea que hay que mirar un nivel para arriba.
    """
    for raiz in (carpeta, os.path.dirname(os.path.abspath(carpeta))):
        if not os.path.isdir(raiz):
            continue
        for sub in sorted(os.listdir(raiz)):
            d = os.path.join(raiz, sub)
            if os.path.isdir(d) and sub.lower().rstrip("s") in ("logo", "placa"):
                return d
    return None


def encontrar_placa(carpeta):
    """Encuentra la placa. Ante cualquier ambiguedad avisa fuerte en vez de
    elegir en silencio: quien usa esta skill puede no saber que salio mal."""
    d = _carpeta_logos(carpeta)
    if d:
        arch = [f for f in sorted(os.listdir(d))
                if f.lower().endswith(EXT_IMG + EXT_VID)]
        if len(arch) == 1:
            return os.path.join(d, arch[0])
        if len(arch) > 1:
            print(f"   !! hay {len(arch)} archivos en '{os.path.basename(d)}': "
                  f"{arch}")
            print("   !! NO se cual usar. Agrega \"placa\": \"<nombre>\" al config.")
            return None

    # por nombre: sirve para placas en video, que no se pueden distinguir de los
    # clips de dialogo por extension
    porn = [f for f in sorted(os.listdir(carpeta))
            if f.lower().endswith(EXT_IMG + EXT_VID)
            and any(k in f.lower() for k in NOMBRES_PLACA)]
    if len(porn) == 1:
        print(f"   (placa deducida por el nombre: '{porn[0]}')")
        return os.path.join(carpeta, porn[0])
    if len(porn) > 1:
        print(f"   !! varios archivos parecen placa: {porn}. Declarar \"placa\".")
        return None

    # Unica imagen suelta: primero en la carpeta de trabajo, si no en la de
    # arriba. Es comun tener el logo del cliente una vez y una subcarpeta por
    # pieza colgando de ahi.
    for raiz, donde in ((carpeta, "la carpeta"),
                        (os.path.dirname(os.path.abspath(carpeta)),
                         "la carpeta de arriba")):
        if not os.path.isdir(raiz):
            continue
        imgs = [f for f in sorted(os.listdir(raiz)) if f.lower().endswith(EXT_IMG)]
        if len(imgs) == 1:
            print(f"   (placa deducida: unica imagen de {donde}, '{imgs[0]}' — "
                  f"verificar que sea la placa y no una foto de producto)")
            return os.path.join(raiz, imgs[0])
        if len(imgs) > 1:
            print(f"   !! hay {len(imgs)} imagenes en {donde}: {imgs}. "
                  f"Poner una sola, meterlas en 'Placa/', o declarar \"placa\".")
            return None
    return None


def a_srgb(imagen, tmp):
    """Convierte la imagen a sRGB si trae ICC embebido, y devuelve la ruta a usar.

    Los logos exportados desde Mac suelen venir en Display P3. Si se usan los
    numeros crudos, el color sale apagado respecto de como lo ve el disenador
    (medido: (229,84,98) crudo vs (248,69,94) convertido — el segundo es el que
    coincide con la edicion manual). Hay que convertir la imagen ENTERA, no solo
    el color muestreado: si se corrige el fondo pero no el logo, vuelve a
    aparecer el borde de la imagen.
    """
    from PIL import Image
    im = Image.open(imagen)
    icc = im.info.get("icc_profile")
    if not icc:
        return imagen
    try:
        import io
        from PIL import ImageCms
        origen = ImageCms.ImageCmsProfile(io.BytesIO(icc))
        alpha = im.convert("RGBA").getchannel("A")
        conv = ImageCms.profileToProfile(
            im.convert("RGB"), origen, ImageCms.createProfile("sRGB"),
            outputMode="RGB").convert("RGBA")
        conv.putalpha(alpha)
        salida = os.path.join(tmp, "placa_srgb.png")
        conv.save(salida)
        print(f"   perfil ICC '{ImageCms.getProfileDescription(origen).strip()}'"
              f" -> convertido a sRGB")
        return salida
    except Exception as e:
        print(f"   !! no se pudo convertir el perfil ICC ({e}); se usan los "
              f"numeros crudos y el color puede salir apagado")
        return imagen


ESCALA_PLACA = ("scale={W}:{H}:force_original_aspect_ratio=increase,"
                "crop={W}:{H},fps={FPS},setsar=1")


def hacer_placa(placa, salida):
    """La placa se usa TAL CUAL. Acepta imagen fija o video (outro animado).

    Antes esto componia un logo suelto sobre un fondo del color muestreado de la
    imagen. Funcionaba, pero obligaba a deducir el color, y deducir deja residuo:
    contra la edicion manual quedaba a ~12 unidades por la conversion de espacio.
    Con la placa ya armada no se interpreta nada y el color es exacto.
    """
    vf = ESCALA_PLACA.format(W=W, H=H, FPS=FPS)

    if placa.lower().endswith(EXT_VID):
        d = dur(placa)
        # PLACA_DUR (1.3s) se midio sobre placas FIJAS. Una placa animada tiene
        # su propia duracion de diseno; truncarla cortaria la animacion.
        print(f"   placa en VIDEO, {d:.2f}s — se respeta su duracion "
              f"(la regla de {PLACA_DUR}s aplica solo a placas fijas)")
        tiene_audio = bool(sh(["ffprobe", "-v", "error", "-select_streams", "a:0",
                               "-show_entries", "stream=codec_name",
                               "-of", "csv=p=0", placa]).stdout.strip())
        cmd = ["ffmpeg", "-v", "error", "-i", placa]
        if tiene_audio:
            cmd += ["-vf", vf, "-af", "aresample=48000"]
        else:
            print("   (la placa no trae audio: se le agrega silencio)")
            cmd += ["-f", "lavfi", "-i", "anullsrc=r=48000:cl=stereo",
                    "-vf", vf, "-shortest"]
        cmd += ["-c:v", "libx264", "-crf", "16", "-preset", "medium",
                "-c:a", "aac", "-b:a", "192k", "-pix_fmt", "yuv420p", salida, "-y"]
        sh(cmd)
        return

    from PIL import Image
    placa = a_srgb(placa, os.path.dirname(salida))
    w, h = Image.open(placa).size
    if abs(w / h - W / H) > 0.08:
        print(f"   !! la placa mide {w}x{h} (aspecto {w/h:.2f}) y no es 9:16 "
              f"({W/H:.2f}). Se recorta para llenar la pantalla y puede perder "
              f"parte del diseno. Exportala a {W}x{H}.")
    else:
        print(f"   placa {w}x{h} — se usa tal cual, {PLACA_DUR}s")
    sh(["ffmpeg", "-v", "error", "-loop", "1", "-i", placa,
        "-f", "lavfi", "-i", "anullsrc=r=48000:cl=stereo", "-t", str(PLACA_DUR),
        "-vf", vf, "-c:v", "libx264", "-crf", "16", "-preset", "medium",
        "-c:a", "aac", "-b:a", "192k", "-pix_fmt", "yuv420p", salida, "-y"])


# ---- modo revisar ----------------------------------------------------------
def revisar(paths):
    print("=" * 74)
    print("REVISION PREVIA — no se renderiza nada")
    print("=" * 74)
    hay_morph_voz = False
    for p in paths:
        d = dur(p)
        cab, medio = morphs(p)
        sil = silencios(p)
        cab_sil = next((b - a for a, b in sil if a <= 0.05), 0.0)
        internas = [b - a for a, b in sil if a > 0.05 and b < d - 0.05]
        largas = [round(x, 2) for x in internas if x > MAX_PAUSA * TOLERANCIA]
        print(f"\n{os.path.basename(p)[:60]}")
        print(f"   duracion            {d:.2f}s")
        print(f"   silencio de cabeza  {cab_sil:.2f}s")
        print(f"   pausas a comprimir  {largas if largas else 'ninguna'}")
        if cab:
            print(f"   MORPH DE CABEZA     hasta {cab:.3f}s")
            if cab_sil >= cab:
                print(f"      -> el recorte de silencio ({cab_sil:.2f}s) ya lo tapa")
            else:
                print(f"      -> ATENCION: el silencio ({cab_sil:.2f}s) es MAS CORTO "
                      f"que el morph; el corte se va a ajustar")
        else:
            print("   morph de cabeza     ninguno (sin saltos secos)")
        if medio:
            hay_morph_voz = True
            print(f"   MORPH SOBRE VOZ     {[t for t, _ in medio]}")
            print("      -> conviene generar un clip de producto para taparlo")
    print("\n" + "=" * 74)
    if hay_morph_voz:
        print("HAY MORPH SOBRE VOZ. Genera un clip de producto y pasalo como")
        print("'broll' en el config para que el montaje lo tape.")
    else:
        print("Sin morphs sobre voz. Se puede montar directo.")
    print("Recorda: 'morph 0.000' significa SIN SALTOS SECOS, no 'clip limpio'.")
    print("Las derivas graduales no las detecta — revisalas a ojo.")
    print("=" * 74)


# ---- modo montar -----------------------------------------------------------
def montar(cfg_path):
    cfg = json.load(open(cfg_path))
    base = cfg.get("carpeta", os.path.dirname(os.path.abspath(cfg_path)))
    P = lambda n: n if os.path.isabs(n) else os.path.join(base, n)
    tmp = cfg.get("tmp", os.path.join(base, "_build"))
    os.makedirs(tmp, exist_ok=True)
    T = lambda n: os.path.join(tmp, n)

    # Config de marca del CLIENTE (brand/edicion-ugc.json). Lo que venga en el
    # config del trabajo pisa a lo de la marca.
    marca, marca_path = buscar_config_marca(base, cfg.get("config_marca"))
    if marca_path:
        print(f"== config de marca: {marca_path} "
              f"({marca.get('marca', 'sin nombre')}) ==")
    clips = [P(c) for c in cfg["clips"]]

    print("== 0. medicion ==")
    morph_cabeza = []
    for c in clips:
        cab, medio = morphs(c)
        morph_cabeza.append(cab)
        print(f"   {os.path.basename(c)[:44]:44} morph_cabeza={cab:.3f} "
              f"morph_voz={[t for t, _ in medio] if medio else 'no'}")

    print("\n== 1. entrada de cada clip ==")
    entradas = []
    for i, c in enumerate(clips):
        e = entrada_de_clip(c, morph_cabeza[i])
        entradas.append(e)
        v = inicio_voz(c)
        extra = "" if i == 0 else "   <- evita repetir la pose del still"
        print(f"   {os.path.basename(c)[:40]:40} voz en {v:.3f}s -> entra en "
              f"{e:.3f}s ({(v-e)*FPS:.0f} frames antes){extra}")

    print("\n== 2. recorte de silencios ==")
    concat(clips, T("crudo.mp4"), entradas)
    empalme_crudo = (dur(clips[0]) - entradas[0]) if len(clips) > 1 else None
    keep = tramos_a_conservar(T("crudo.mp4"))
    print(f"   tramos conservados: {keep}")
    aplicar_tramos(T("crudo.mp4"), keep, T("dialogo.mp4"))

    # El empalme entre clips es donde viven los morphs. Hay que reproyectarlo
    # al timeline ya recortado, porque los tramos borrados corren todo hacia atras.
    def a_timeline_final(t):
        acum = 0.0
        for a, b in keep:
            if t < a:
                return acum
            if t <= b:
                return acum + (t - a)
            acum += b - a
        return acum

    empalme = a_timeline_final(empalme_crudo) if empalme_crudo else None

    print("\n== 3. re-chequeo de morph sobre el resultado ==")
    cab, medio = morphs(T("dialogo.mp4"), ventana=2.0)
    if cab:
        # cuanto habla nos comeriamos al correr el corte hasta pasar el morph
        sil = silencios(T("dialogo.mp4"))
        libre = next((b for a, b in sil if a <= 0.05), 0.0)
        solape = max(0.0, cab - libre)
        if solape <= MORPH_SOLAPE_OK:
            print(f"   quedo morph hasta {cab:.3f}s -> se corre el corte "
                  f"(se come {solape:.3f}s de voz, dentro de lo tolerable)")
            aplicar_tramos(T("dialogo.mp4"), [(cab, dur(T("dialogo.mp4")))],
                           T("dialogo2.mp4"))
            os.replace(T("dialogo2.mp4"), T("dialogo.mp4"))
        else:
            print(f"   !! quedo morph hasta {cab:.3f}s y taparlo se comeria "
                  f"{solape:.3f}s de voz. NO se ajusta — revisar a mano.")
    else:
        print("   sin morph residual")

    print("\n== 4. transcripcion ==")
    correcciones = dict(marca.get("marcas_whisper", {}))
    correcciones.update(cfg.get("marcas_whisper", {}))
    segs = []
    if cfg.get("subtitulos", True) or cfg.get("broll"):
        segs = transcribir(T("dialogo.mp4"), tmp, correcciones,
                           cfg.get("idioma", "es"))
        print(f"   {len(segs)} frases")

    print("\n== 5. B-roll ==")
    cuerpo = T("dialogo.mp4")
    brolls = cfg.get("broll")
    if isinstance(brolls, str):
        brolls = [brolls]
    if brolls:
        brolls = [P(b) for b in brolls]
        d_dial = dur(T("dialogo.mp4"))
        bloque = cfg.get("broll_dur", round(
            max(BROLL_MIN_S, min(BROLL_MAX_S, d_dial * BROLL_LARGO)), 2))

        # DONDE va el bloque.
        # Por defecto, posicion proporcional: termina en BROLL_FIN del dialogo.
        # Es lo unico que se sostiene en las 4 ediciones manuales (70-75% en las
        # cuatro). El inicio se deriva del final y del largo.
        # La mencion del producto NO sirve como ancla: en una de las ediciones
        # medidas la persona dice "proba el producto" y sigue en camara — el
        # B-roll entra despues, sobre los beneficios. Se reporta como
        # referencia, nada mas.
        fin_sug = d_dial * BROLL_FIN
        ini = round(fin_sug - bloque, 2)
        motivo = f"posicion estandar: termina en {BROLL_FIN:.0%} del dialogo"

        # Correccion: si hay un morph fuerte y queda FUERA del bloque, se corre
        # el bloque para taparlo. Adentro no hace falta mover nada.
        peor = peores_momentos(T("dialogo.mp4"), 1)
        if peor and peor[0][1] >= 0.15 and not (ini <= peor[0][0] <= ini + bloque):
            ini = round(peor[0][0] - bloque / 2, 2)
            motivo = (f"corrido para tapar el morph de {peor[0][1]:.3f} en "
                      f"{peor[0][0]:.2f}s (caia fuera de la posicion estandar)")
        elif peor and peor[0][1] >= 0.15:
            motivo += f" (y de paso tapa el morph de {peor[0][1]:.3f})"

        t_prod, frase = momento_producto(segs, cfg.get("producto") or
                                         marca.get("producto") or
                                         list(correcciones.values()))
        if t_prod is not None:
            print(f'   (el producto se nombra en {t_prod:.2f}s: "{frase}")')
        ini = round(max(0.0, min(ini, d_dial - bloque)), 2)

        # Alinear los bordes con los cortes que ya existen (los del recorte de
        # aire muerto y el empalme entre clips). Un corte a pocos frames del
        # borde del B-roll se lee como un tropiezo, no como un corte.
        cortes_duros, acum = [], 0.0
        for a, b in keep[:-1]:
            acum += b - a
            cortes_duros.append(round(acum, 3))
        if empalme:
            cortes_duros.append(round(empalme, 3))
        for c in sorted(cortes_duros):
            if 0 < abs(c - ini) <= BROLL_SNAP:
                print(f"   borde de entrada {ini:.2f}s -> {c:.2f}s "
                      f"(habia un corte a {abs(c-ini):.2f}s: se alinean)")
                ini = round(max(0.0, min(c, d_dial - bloque)), 2)
                break
        fin = ini + bloque
        for c in sorted(cortes_duros):
            if 0 < abs(c - fin) <= BROLL_SNAP and c > ini + BROLL_SNAP:
                print(f"   borde de salida {fin:.2f}s -> {c:.2f}s "
                      f"(habia un corte a {abs(c-fin):.2f}s: se alinean)")
                bloque = round(c - ini, 2)
                break

        # UN solo bloque, armado con todos los clips disponibles pegados.
        # Asi salen las ediciones manuales: en una de ellas son dos clips
        # seguidos formando un solo bloque de 4.54s.
        n = len(brolls)
        cada = round(bloque / n, 2)
        origen = "declarado en el config" if cfg.get("broll_dur") else \
                 (f"{BROLL_LARGO:.0%} del dialogo — medido 26/37/40/45% en 4 "
                  f'ediciones, ajustable con "broll_dur"')
        print(f"   bloque de {bloque:.2f}s en {ini:.2f}-{ini+bloque:.2f}s "
              f"-> {motivo}")
        print(f"   largo {origen}")
        planos, cursor = [], ini
        for br in brolls:
            desde = mejor_tramo(br, cada)
            planos.append((round(cursor, 2), cada, br, desde))
            print(f"      {os.path.basename(br)[:38]:38} {cursor:.2f}-"
                  f"{cursor+cada:.2f}s (tramo desde {desde:.2f}s del clip)")
            cursor += cada

        cmd, fc, prev = ["ffmpeg", "-v", "error", "-i", T("dialogo.mp4")], [], "[0:v]"
        for i, (a, dd, br, desde) in enumerate(planos):
            cmd += ["-ss", str(desde), "-i", br]
            fc.append(f"[{i+1}:v]fps={FPS},scale={W}:{H},setsar=1,trim=0:{dd},"
                      f"setpts=PTS-STARTPTS+{a}/TB[ov{i}]")
            fc.append(f"{prev}[ov{i}]overlay=enable='between(t,{a},{a+dd})'[b{i}]")
            prev = f"[b{i}]"
        cmd += ["-filter_complex", ";".join(fc), "-map", prev, "-map", "0:a",
                "-c:v", "libx264", "-crf", "16", "-preset", "medium",
                "-c:a", "copy", T("cuerpo.mp4"), "-y"]
        sh(cmd)
        cuerpo = T("cuerpo.mp4")
    else:
        print("   sin clip de B-roll: no se tapa nada")

    print("\n== 6. subtitulos ==")
    if cfg.get("subtitulos", True):
        quemar_subs(cuerpo, T("consubs.mp4"), tmp, segs)
        cuerpo = T("consubs.mp4")
    else:
        print("   desactivados")

    print("\n== 7. placa ==")
    # Prioridad: config del trabajo > config de marca (brand/edicion-ugc.json)
    # > brand/placa.* del cliente > deteccion en la carpeta de crudos.
    placa = cfg.get("placa")
    base_placa = base
    if not placa and marca.get("placa"):
        placa = marca["placa"]
        base_placa = os.path.dirname(marca_path) if marca_path else base
    placa = placa or buscar_placa_marca(base) or encontrar_placa(base)
    if placa:
        placa = os.path.expanduser(placa)
        if not os.path.isabs(placa):
            placa = os.path.join(base_placa, placa)
        if not os.path.exists(placa):
            print(f"   !! la placa declarada no existe: {placa}")
            sys.exit(1)
        hacer_placa(placa, T("placa.mp4"))
        print(f"   {os.path.basename(placa)} — {dur(T('placa.mp4')):.2f}s")
        final_in = T("conplaca.mp4")
        sh(["ffmpeg", "-v", "error", "-i", cuerpo, "-i", T("placa.mp4"),
            "-filter_complex", "[0:v][0:a][1:v][1:a]concat=n=2:v=1:a=1[v][a]",
            "-map", "[v]", "-map", "[a]", "-c:v", "libx264", "-crf", "16",
            "-preset", "medium", "-c:a", "aac", "-b:a", "192k", final_in, "-y"])
        cuerpo = final_in
    else:
        print("   !! sin placa definida: poné la placa en brand/placa.png del "
              "cliente, en una subcarpeta Placa/, o declará \"placa\" en el config")

    print("\n== 8. export ==")
    # Sin "salida" explicita se aplica la convencion del stack:
    # exports/videos/<AAAA-MM-DD>_<slug>_v<N>.mp4 de la carpeta del cliente.
    if cfg.get("salida"):
        salida = P(cfg["salida"])
        os.makedirs(os.path.dirname(os.path.abspath(salida)), exist_ok=True)
    else:
        slug = slugify(cfg.get("slug") or marca.get("marca") or
                       os.path.basename(os.path.abspath(base)))
        salida = salida_por_defecto(base, slug)
        print(f"   sin 'salida' en el config -> convencion del stack, slug '{slug}'")
    # maxrate NO puede ser igual a -b:v: el VBV se queda corto y el archivo sale
    # muy por debajo del target (medido: pedia 6000k y entregaba 4957k).
    sh(["ffmpeg", "-v", "error", "-i", cuerpo, "-c:v", "libx264",
        "-b:v", BITRATE, "-maxrate", "9500k", "-bufsize", "19000k",
        "-preset", "slow", "-c:a", "aac", "-b:a", "192k",
        "-pix_fmt", "yuv420p", salida, "-y"])
    print(f"   {salida}  ({dur(salida):.2f}s)")


# ---- subtitulos ------------------------------------------------------------
def transcribir(entrada, tmp, marcas, idioma):
    """Whisper -> lista de (inicio, fin, texto) en frases de 2-4 palabras.

    Se corre ANTES de ubicar el B-roll: sin el texto no se puede saber en que
    momento se menciona el producto, que es donde va el B-roll cuando no hay
    ningun morph que tapar.
    """
    wav = os.path.join(tmp, "audio.wav")
    sh(["ffmpeg", "-v", "error", "-i", entrada, "-ac", "1", "-ar", "16000",
        wav, "-y"])
    modelo = os.path.expanduser("~/.cache/whisper-cpp/ggml-large-v3-turbo.bin")
    sh(["whisper-cli", "-m", modelo, "-f", wav, "-l", idioma,
        "-ojf", "-ml", "1", "-sow", "-of", os.path.join(tmp, "tr")])
    js = os.path.join(tmp, "tr.json")
    if not os.path.exists(js):
        print("   !! whisper no devolvio transcripcion")
        return []

    def corregir(t):
        """Reemplazo a nivel FRASE, no palabra.

        Whisper a veces parte un nombre propio en dos ("Marcalinda" -> "marca
        Linda"); un diccionario palabra-por-palabra no puede recomponer eso.
        Las claves de varias palabras se aplican primero, para que la mas
        especifica gane.
        """
        for mal in sorted(marcas, key=lambda k: -len(k.split())):
            t = re.sub(r"(?<!\w)" + re.escape(mal) + r"(?!\w)", marcas[mal], t,
                       flags=re.IGNORECASE)
        return t

    palabras = [(s["offsets"]["from"] / 1000, s["offsets"]["to"] / 1000,
                 s["text"].strip())
                for s in json.load(open(js))["transcription"] if s["text"].strip()]

    segs, buf = [], []

    def cerrar():
        if buf:
            txt = corregir(" ".join(w for _, _, w in buf)).rstrip(".,;:")
            segs.append((buf[0][0], buf[-1][1], txt))
            buf.clear()

    for i, (a, b, w) in enumerate(palabras):
        buf.append((a, b, w))
        if w[-1] in ".,;:!?" and len(palabras) - i - 1 != 1:
            cerrar()
        elif len(buf) >= SUB_MAX_PAL or len(" ".join(x[2] for x in buf)) >= SUB_MAX_CHAR:
            cerrar()
    cerrar()

    # Whisper cierra la palabra ANTES de que la persona termine de articularla,
    # asi que el subtitulo desaparecia temprano y quedaban huecos entre frases.
    # Cada frase se estira hasta que arranca la siguiente; si el hueco es largo
    # (silencio real) se corta a los 0.6s para no dejar texto viejo colgado.
    HUECO_MAX = 0.6
    for i in range(len(segs) - 1):
        a, b, t = segs[i]
        segs[i] = (a, min(segs[i + 1][0], b + HUECO_MAX), t)
    if segs:
        a, b, t = segs[-1]
        segs[-1] = (a, b + 0.25, t)
    return segs


def momento_producto(segs, claves):
    """Cuando se menciona el producto. Devuelve el inicio de esa frase.

    Es donde va el B-roll si no hay morph que tapar: el plano de producto entra
    justo cuando la persona lo nombra. Sale de medir una edicion manual donde el
    bloque de B-roll arranca en 2.50s y la frase que nombra al producto arranca
    en 2.39s.
    """
    claves = [c.lower() for c in claves if c]
    for a, b, t in segs:
        low = t.lower()
        if any(c in low for c in claves):
            return a, t
    return None, None


def quemar_subs(entrada, salida, tmp, segs):
    from PIL import Image, ImageDraw, ImageFont
    if not segs:
        sh(["ffmpeg", "-v", "error", "-i", entrada, "-c", "copy", salida, "-y"])
        return
    png = os.path.join(tmp, "subs_png")
    os.makedirs(png, exist_ok=True)
    print(f"   {len(segs)} frases")
    for i, (a, b, t) in enumerate(segs):
        im = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        d = ImageDraw.Draw(im)
        size = SUB_SIZE
        while size > 18:
            f = ImageFont.truetype(FUENTE, size)
            try:
                f.set_variation_by_axes([SUB_PESO])
            except Exception:
                pass
            if d.textlength(t, font=f) <= SUB_ANCHO_MAX:
                break
            size -= 1
        w_ = d.textlength(t, font=f)
        x = (W - w_) / 2
        # contorno + sombra caida. Mas marcado que la version anterior:
        # sobre fondos claros el texto se perdia.
        for dx, dy in ((-2, 0), (2, 0), (0, -2), (0, 2),
                       (-2, -2), (2, -2), (-2, 2), (2, 2)):
            d.text((x + dx, SUB_Y + dy), t, font=f, fill=(0, 0, 0, 200), anchor="lm")
        d.text((x + 1, SUB_Y + 3), t, font=f, fill=(0, 0, 0, 120), anchor="lm")
        d.text((x, SUB_Y), t, font=f, fill=(255, 255, 255, 255), anchor="lm")
        im.save(os.path.join(png, f"{i:03d}.png"))
        print(f"      {a:6.2f} -> {b:6.2f}  {t}")

    cmd = ["ffmpeg", "-v", "error", "-i", entrada]
    for i in range(len(segs)):
        cmd += ["-i", os.path.join(png, f"{i:03d}.png")]
    fc, prev = [], "[0:v]"
    for i, (a, b, _) in enumerate(segs):
        fc.append(f"{prev}[{i+1}:v]overlay=0:0:enable='between(t,{a},{b})'[s{i}]")
        prev = f"[s{i}]"
    cmd += ["-filter_complex", ";".join(fc), "-map", prev, "-map", "0:a",
            "-c:v", "libx264", "-crf", "16", "-preset", "medium",
            "-c:a", "copy", "-pix_fmt", "yuv420p", salida, "-y"]
    r = sh(cmd)
    if r.returncode:
        print(r.stderr[-1500:])
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(1)
    modo = sys.argv[1]
    if modo == "revisar":
        # Revisar solo mide: no transcribe, no compone, no necesita fuente.
        verificar_entorno(whisper=False, pillow=False, fuente=False)
        objetivos = []
        for a in sys.argv[2:]:
            if os.path.isdir(a):
                objetivos += [os.path.join(a, f) for f in sorted(os.listdir(a))
                              if f.lower().endswith((".mp4", ".mov"))]
            else:
                objetivos.append(a)
        if not objetivos:
            print("No hay ningun .mp4 ni .mov en lo que pasaste.")
            sys.exit(1)
        revisar(objetivos)
    elif modo == "montar":
        verificar_entorno()
        if not os.path.exists(sys.argv[2]):
            print(f"No existe el config: {sys.argv[2]}")
            sys.exit(1)
        montar(sys.argv[2])
    else:
        print(__doc__)
        sys.exit(1)
