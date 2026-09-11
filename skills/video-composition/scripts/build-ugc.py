#!/usr/bin/env python3
"""Arma la composición HyperFrames de un UGC de 2 clips + inserts + placa.

Uso (cwd libre):
    python3 build-ugc.py <creatives/<brief>/<grupo>/<id>/composition>

Lee en esa carpeta:
    ugc.json   el spec de la pieza (ver formats/ugc-2clips.md)
    t1.json    transcripción del clip A (array de words con text/start/end)
    t2.json    transcripción del clip B
y escribe <composition>/index.html a partir de templates/ugc-2clips.html.

Los subtítulos salen SIEMPRE de la transcripción real, nunca del guion
tipeado. El index.html generado no se edita a mano: el próximo build lo pisa.
Cambiar cómo se ve = tocar el template; cambiar qué aparece y cuándo = tocar
el spec.
"""
import html
import json
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
TEMPLATE = os.path.join(HERE, "..", "templates", "ugc-2clips.html")

# El template está dibujado sobre un lienzo de 720x1280; otros tamaños se
# resuelven escalando el escenario entero (transform: scale), no reposicionando.
BASE_W, BASE_H = 720, 1280
MAXW = 4          # palabras por cue de subtítulo
CLEAN_HEAD = 2.0  # segundos iniciales sin insert (la cara y la frase)

DEFAULT_FONTS = {
    "disp": {"family": "", "stack": '"Arial Rounded MT Bold", "Helvetica Neue", Arial, sans-serif'},
    "body": {"family": "", "stack": '"Arial Narrow", "Helvetica Neue", Arial, sans-serif'},
    "mono": {"family": "", "stack": 'Menlo, "Courier New", monospace'},
}


def die(msg):
    print(f"build-ugc: {msg}", file=sys.stderr)
    sys.exit(1)


def warn(msg):
    print(f"build-ugc: aviso — {msg}", file=sys.stderr)


# ── transcripción → palabras ────────────────────────────────────────────────

def load_words(path, offset, speed, splits, fixes):
    if not os.path.exists(path):
        die(f"falta {path} (transcribí el clip con `npx hyperframes@0.8.33 transcribe … --json`)")
    raw = json.load(open(path, encoding="utf-8"))
    words = raw["words"] if isinstance(raw, dict) and "words" in raw else raw
    out = []
    for w in words:
        txt = w["text"].strip()
        txt = fixes.get(txt.strip(" ,.¿?¡!"), txt)
        start = float(w["start"]) / speed + offset
        end = float(w["end"]) / speed + offset
        parts = splits.get(txt.rstrip(".,?!")) or splits.get(txt)
        if parts:
            step = (end - start) / len(parts)
            for i, p in enumerate(parts):
                out.append({"t": start + i * step, "text": p, "end": start + (i + 1) * step})
        else:
            out.append({"t": start, "text": txt, "end": end})
    return out


def clean(tok):
    return tok.strip(" ,.¿?¡!").upper()


def group(words, breaks_after=".?!"):
    cues, cur = [], []
    for w in words:
        cur.append(w)
        hard = any(w["text"].rstrip().endswith(c) for c in breaks_after)
        if hard or len(cur) >= MAXW:
            cues.append(cur)
            cur = []
    if cur:
        cues.append(cur)
    return cues


def caption_html(cues, keywords):
    kw = {k.upper() for k in keywords}
    rows = []
    for i, cue in enumerate(cues, 1):
        start = cue[0]["t"]
        end = max(w["end"] for w in cue)
        spans = []
        for w in cue:
            t = clean(w["text"])
            if not t:
                continue
            cls = "w kw" if t in kw else "w"
            spans.append(f'<span class="{cls}" data-t="{w["t"]:.2f}">{html.escape(t)}</span>')
        if not spans:
            continue
        rows.append(
            f'    <div id="cap-{i:02d}" class="cap clip" data-start="{start:.2f}" '
            f'data-duration="{max(end - start, 0.35):.2f}" data-track-index="7">' + " ".join(spans) + "</div>"
        )
    return "\n".join(rows)


# ── chequeos baratos que el lint no hace ───────────────────────────────────

def probe_duration(path):
    try:
        r = subprocess.run(
            ["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", path],
            capture_output=True, text=True, timeout=20,
        )
        return float(r.stdout.strip()) if r.returncode == 0 and r.stdout.strip() else None
    except (OSError, ValueError, subprocess.TimeoutExpired):
        return None


def check_spec(s, root):
    o = s["outro"]
    if o["start"] + o["dur"] > s["total"] + 0.01:
        die(f"la placa termina en {o['start'] + o['dur']:.2f}s pero total={s['total']}")
    gap = o["start"] - s["cut"] - s.get("avatar_dur", 10.0)
    if gap > 0.5:
        warn(f"hay {gap:.2f}s de aire entre el fin del clip B y la placa (¿la placa arranca tarde?)")
    for ov in s["overlays"]:
        if ov["start"] < CLEAN_HEAD and ov["kind"] in ("cutaway", "card", "cardtall"):
            warn(f"overlay {ov['kind']} a {ov['start']}s: los primeros {CLEAN_HEAD:.0f}s van limpios (la cara y la frase)")
    for ov in s["overlays"]:
        src = ov.get("src")
        if not src:
            continue
        p = os.path.join(root, src)
        if not os.path.exists(p):
            die(f"no existe {src} (todo asset va copiado a composition/assets/)")
        d = probe_duration(p)
        if d is not None and ov.get("mstart", 0) + ov["dur"] > d + 0.01:
            die(f"{src}: mstart {ov.get('mstart', 0)} + dur {ov['dur']} pasa la duración real {d:.2f}s")
    band = os.path.join(root, o["band"])
    if not os.path.exists(band):
        die(f"no existe el fondo de la placa {o['band']}")
    d = probe_duration(band)
    if d is not None and o["bandstart"] + o["dur"] > d + 0.01:
        die(f"la placa no tiene runway: bandstart {o['bandstart']} + dur {o['dur']} > {d:.2f}s del asset. Loopealo con ffmpeg -stream_loop")
    for av in (s.get("av1", "assets/clip-01.mp4"), s.get("av2", "assets/clip-02.mp4")):
        if not os.path.exists(os.path.join(root, av)):
            die(f"no existe el clip de avatar {av}")


# ── fuentes ────────────────────────────────────────────────────────────────

def fonts_css(spec_fonts):
    """@font-face por rol desde archivos en assets/ (la fuente REAL de la
    marca); sin archivo, el stack del sistema. Nunca un <link> remoto: el
    render tiene que dar igual sin red."""
    faces, families = [], {}
    for role in ("disp", "body", "mono"):
        f = (spec_fonts or {}).get(role)
        if f and f.get("file"):
            fam = f.get("family") or f"Ugc{role.capitalize()}"
            weight = f.get("weight", 700)
            faces.append(
                f'  @font-face {{ font-family: "{fam}"; src: url("{f["file"]}"); '
                f'font-weight: {weight}; font-display: block; }}'
            )
            families[role] = f'"{fam}", ' + DEFAULT_FONTS[role]["stack"]
        else:
            families[role] = DEFAULT_FONTS[role]["stack"]
    return "\n".join(faces), families


# ── build ──────────────────────────────────────────────────────────────────

def build(root):
    root = os.path.abspath(root)
    spec_path = os.path.join(root, "ugc.json")
    if not os.path.exists(spec_path):
        die(f"falta {spec_path}")
    s = json.load(open(spec_path, encoding="utf-8"))
    for k in ("total", "cut", "palette", "overlays", "outro"):
        if k not in s:
            die(f"el spec no tiene `{k}`")
    check_spec(s, root)

    splits, fixes = s.get("splits", {}), s.get("fixes", {})
    words = load_words(os.path.join(root, "t1.json"), 0.0, s.get("speed1", 1.0), splits, fixes) + \
            load_words(os.path.join(root, "t2.json"), s["cut"], 1.0, splits, fixes)
    cues = group(words)
    caps = caption_html(cues, s.get("keywords", []))

    p, total, cut = s["palette"], float(s["total"]), float(s["cut"])
    avdur = float(s.get("avatar_dur", 10.0))
    sfx_files = s.get("sfx") or {}
    ov, tl, sfx = [], [], []

    def add_sfx(t, key, dur, vol):
        if sfx_files.get(key):
            sfx.append((t, sfx_files[key], dur, vol))

    for i, o in enumerate(s["overlays"], 1):
        st, du = float(o["start"]), float(o["dur"])
        kind = o["kind"]
        if kind in ("card", "cardtall"):
            tall = " tall" if kind == "cardtall" else ""
            ms = f' data-media-start="{o["mstart"]}"' if "mstart" in o else ""
            ov.append(f'    <video id="ov{i}" class="clip cardvid{tall}" src="{o["src"]}" data-start="{st:.2f}" data-duration="{du:.2f}"{ms} data-track-index="2" muted playsinline></video>')
            ov.append(f'    <div id="ov{i}f" class="clip cardframe{tall}" data-start="{st:.2f}" data-duration="{du:.2f}" data-track-index="3"><div class="label">{html.escape(o.get("label", ""))}</div></div>')
            ov.append(f'    <div id="ov{i}g" class="clip cardglow{tall}" data-start="{st:.2f}" data-duration="{du:.2f}" data-track-index="8"></div>')
            tl.append(f'    tl.fromTo("#ov{i}f", {{ y:-34, scale:.94, opacity:0 }}, {{ y:0, scale:1, opacity:1, duration:.34, ease:"back.out(1.9)" }}, {st:.2f});')
            tl.append(f'    tl.fromTo("#ov{i}g", {{ opacity:.15 }}, {{ opacity:.8, duration:1.1, ease:"sine.inOut", repeat:3, yoyo:true }}, {st + .1:.2f});')
            tl.append(f'    tl.fromTo("#ov{i}", {{ scale:1 }}, {{ scale:1.06, duration:{du:.2f}, ease:"none" }}, {st:.2f});')
            add_sfx(st - .07, "pill", .36, .45)
        elif kind == "cutaway":
            ms = f' data-media-start="{o["mstart"]}"' if "mstart" in o else ""
            ov.append(f'    <video id="ov{i}" class="clip cutaway" src="{o["src"]}" data-start="{st:.2f}" data-duration="{du:.2f}"{ms} data-track-index="2" muted playsinline></video>')
            # scrim localizado: banda de 200px centrada en esa y, solo para tapar
            # texto quemado del cliente que NO cae bajo nuestro bloque de captions
            if o.get("scrim"):
                top = int(o["scrim"]) - 100
                ov.append(f'    <div id="ov{i}s" class="clip cutscrim" style="top:{top}px" data-start="{st:.2f}" data-duration="{du:.2f}" data-track-index="6"></div>')
            if o.get("label"):
                ov.append(f'    <div id="ov{i}l" class="clip cutlabel" data-start="{st + .12:.2f}" data-duration="{du - .2:.2f}" data-track-index="4">{html.escape(o["label"])}</div>')
                tl.append(f'    tl.fromTo("#ov{i}l", {{ y:-20, opacity:0 }}, {{ y:0, opacity:1, duration:.3, ease:"back.out(2)" }}, {st + .12:.2f});')
            # zoom: False es obligatorio si hay algo que leer (interfaz, tabla)
            if o.get("zoom", True):
                tl.append(f'    tl.fromTo("#ov{i}", {{ scale:1.1 }}, {{ scale:1, duration:{du:.2f}, ease:"power2.out" }}, {st:.2f});')
            add_sfx(st - .07, "cut", .57, .5)
        elif kind == "pill":
            ov.append(f'    <div id="ov{i}" class="clip pill" data-start="{st:.2f}" data-duration="{du:.2f}" data-track-index="4">{html.escape(o["text"])}</div>')
            tl.append(f'    tl.fromTo("#ov{i}", {{ y:26, scale:.92, opacity:0 }}, {{ y:0, scale:1, opacity:1, duration:.28, ease:"back.out(2.2)" }}, {st:.2f});')
            add_sfx(st, "pill", .36, .45)
        elif kind == "chip":
            ov.append(f'    <div id="ov{i}" class="clip chip" data-start="{st:.2f}" data-duration="{du:.2f}" data-track-index="4">{html.escape(o["text"])}</div>')
            tl.append(f'    tl.fromTo("#ov{i}", {{ y:-20, opacity:0 }}, {{ y:0, opacity:1, duration:.3, ease:"back.out(2)" }}, {st:.2f});')
        elif kind == "stamp":
            text = html.escape(o["text"]).replace("\\n", "<br/>").replace("\n", "<br/>")
            ov.append(f'    <div id="ov{i}" class="clip stamp" data-start="{st:.2f}" data-duration="{du:.2f}" data-track-index="4">{text}</div>')
            tl.append(f'    tl.fromTo("#ov{i}", {{ scale:2.1, rotation:-14, opacity:0 }}, {{ scale:1, rotation:-7, opacity:1, duration:.22, ease:"power4.in" }}, {st:.2f});')
            add_sfx(st - .03, "stamp", 1.6, .55)
        elif kind == "danger":
            ov.append(f'    <div id="ov{i}" class="clip danger" data-start="{st:.2f}" data-duration="{du:.2f}" data-track-index="8"></div>')
            tl.append(f'    tl.fromTo("#ov{i}", {{ opacity:0 }}, {{ opacity:1, duration:.22, ease:"sine.inOut", repeat:3, yoyo:true }}, {st + .02:.2f});')
        else:
            die(f"overlay desconocido: {kind}")

    o = s["outro"]
    ostart, odur = float(o["start"]), float(o["dur"])
    ov.append(f'''    <div id="outro" class="clip outro" data-start="{ostart:.2f}" data-duration="{odur:.2f}" data-track-index="5">
      <div class="top">{html.escape(o.get("top", ""))}</div>
      <div class="bottom"><div class="url">{html.escape(o.get("url", ""))}</div>
      <div class="wl"><span class="arrow">→</span> {html.escape(o.get("cta", ""))}</div></div>
    </div>
    <video id="outro-v" class="clip bandvid outroband" src="{o["band"]}" data-start="{ostart:.2f}" data-duration="{odur:.2f}" data-media-start="{o["bandstart"]}" data-track-index="6" muted playsinline></video>''')
    tl.append(f'    tl.fromTo("#outro", {{ opacity:0 }}, {{ opacity:1, duration:.25, ease:"power2.out" }}, {ostart:.2f});')
    tl.append(f'    tl.fromTo("#outro-v", {{ scale:1.15 }}, {{ scale:1, duration:.5, ease:"power3.out" }}, {ostart:.2f});')
    tl.append(f'    tl.fromTo("#outro .bottom", {{ y:40, autoAlpha:0 }}, {{ y:0, autoAlpha:1, duration:.35, ease:"back.out(1.8)" }}, {ostart + .35:.2f});')
    tl.append(f'    tl.fromTo("#outro .top", {{ y:-20, opacity:0 }}, {{ y:0, opacity:1, duration:.3, ease:"power2.out" }}, {ostart + .25:.2f});')
    tl.append(f'    tl.fromTo("#outro .arrow", {{ x:0 }}, {{ x:9, duration:.28, ease:"sine.inOut", repeat:5, yoyo:true }}, {ostart + .7:.2f});')
    add_sfx(ostart - .08, "cut", .57, .5)
    add_sfx(ostart + .05, "close", 2.4, .5)

    # flash del color de acento en el corte entre clips y en la placa
    for t in (cut, ostart):
        tl.append(f'    tl.fromTo("#flash", {{ opacity:0 }}, {{ opacity:.7, duration:.11, ease:"power1.in", immediateRender:false }}, {t - .1:.2f});')
        tl.append(f'    tl.to("#flash", {{ opacity:0, duration:.18, ease:"power2.out" }}, {t + .01:.2f});')
        tl.append(f'    tl.set("#flash", {{ opacity:0 }}, {t + .21:.2f});')
    add_sfx(cut - .1, "cut", .57, .5)
    # hard-kill del flash en TODO borde de clip que caiga dentro del fade,
    # subtítulos incluidos: el seek no lineal puede caer después del fade y
    # dejar el flash prendido; el linter marca el borde exacto
    # (gsap_exit_missing_hard_kill), no el tl.set que quedó cerca.
    cue_starts = [c[0]["t"] for c in cues]
    edges = {float(x["start"]) for x in s["overlays"]} | {ostart}
    for f in (cut, ostart):
        edges |= {round(c, 2) for c in cue_starts if f - 0.15 <= c <= f + 0.4}
    for b in sorted(edges):
        tl.append(f'    tl.set("#flash", {{ opacity:0 }}, {b:.2f});')

    sfx_html = "\n".join(
        f'    <audio id="sfx-{i}" src="{n}" data-start="{max(t, 0):.2f}" data-duration="{d}" data-track-index="{20 + i}" data-volume="{v}"></audio>'
        for i, (t, n, d, v) in enumerate(sfx, 1))

    W, H = int(s.get("width", BASE_W)), int(s.get("height", BASE_H))
    if abs(W / H - BASE_W / BASE_H) > 0.01:
        die(f"{W}x{H} no es 9:16: este formato es vertical (720x1280 o 1080x1920)")
    scale = W / BASE_W
    faces, fam = fonts_css(s.get("fonts"))
    cid = s.get("cid", "main")

    tpl = open(TEMPLATE, encoding="utf-8").read()
    out = (tpl.replace("{{TITLE}}", html.escape(s.get("title", cid))).replace("{{CID}}", cid)
              .replace("{{W}}", str(W)).replace("{{H}}", str(H)).replace("{{SCALE}}", f"{scale:.4f}")
              .replace("{{FPS}}", str(s.get("fps", 30)))
              .replace("{{TOTAL}}", f"{total:.2f}").replace("{{CUT}}", f"{cut:.2f}").replace("{{AVDUR}}", f"{avdur:.2f}")
              .replace("{{AV1SRC}}", s.get("av1", "assets/clip-01.mp4")).replace("{{AV1DUR}}", f'{float(s.get("av1_dur", avdur)):.2f}')
              .replace("{{AV2SRC}}", s.get("av2", "assets/clip-02.mp4"))
              .replace("{{ACCENT}}", p["accent"]).replace("{{KW}}", p.get("kw", p["accent"]))
              .replace("{{DARK}}", p["dark"]).replace("{{DARK2}}", p.get("dark2", p["dark"])).replace("{{CREAM}}", p.get("cream", "#F5F0E8"))
              .replace("{{FONTS_CSS}}", faces)
              .replace("{{FONT_DISP}}", fam["disp"]).replace("{{FONT_BODY}}", fam["body"]).replace("{{FONT_MONO}}", fam["mono"])
              .replace("{{WATERMARK}}", html.escape(s.get("watermark", "")))
              .replace("{{WM_DUR}}", f"{max(ostart - 1.2 - 0.6, 1):.2f}")
              .replace("{{OVERLAYS}}", "\n".join(ov)).replace("{{CAPTIONS}}", caps)
              .replace("{{SFX}}", sfx_html).replace("{{TIMELINE}}", "\n".join(tl)))
    with open(os.path.join(root, "index.html"), "w", encoding="utf-8") as fh:
        fh.write(out)
    print(f"{os.path.basename(root)}: {len(cues)} cues, {len(s['overlays'])} overlays, {total}s → index.html")
    if fixes or splits:
        print("correcciones de ASR aplicadas (declaralas al humano): "
              + ", ".join([f"{k}→{v}" for k, v in fixes.items()] + [f"{k}→{' '.join(v)}" for k, v in splits.items()]))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        die("uso: build-ugc.py <carpeta composition/>")
    build(sys.argv[1])
