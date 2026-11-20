# -*- coding: utf-8 -*-
"""Mapy „Embargo” rysowane od nowa w SVG (siatka 70 px = 1 m) i renderowane do WebP."""
import sys, random, math, os, subprocess
sys.path.insert(0, "/home/claude/build")
from maps import DEFS, svg, R, wall_room, door, gap, crate, barrel, table, chair, label, grid_overlay, rubble, finish, G

EXTRA = """
<defs>
 <pattern id="concrete" width="140" height="140" patternUnits="userSpaceOnUse">
  <rect width="140" height="140" fill="#5d5b56"/><path d="M0 139.5h140M139.5 0v140" stroke="#47453f" stroke-width="3"/>
  <circle cx="30" cy="40" r="2" fill="#4a4843"/><circle cx="100" cy="90" r="3" fill="#4a4843"/></pattern>
 <pattern id="grating" width="28" height="28" patternUnits="userSpaceOnUse">
  <rect width="28" height="28" fill="#1d1c1a"/><path d="M0 2h28M0 16h28M2 0v28M16 0v28" stroke="#4f4a43" stroke-width="4"/></pattern>
 <pattern id="tin" width="24" height="70" patternUnits="userSpaceOnUse">
  <rect width="24" height="70" fill="#6d6f6c"/><path d="M12 0v70" stroke="#4d4f4c" stroke-width="5"/></pattern>
 <pattern id="sand" width="200" height="200" patternUnits="userSpaceOnUse">
  <rect width="200" height="200" fill="#8a7a5c"/><rect width="200" height="200" filter="url(#stain)"/></pattern>
 <radialGradient id="fire" r="50%"><stop offset="0" stop-color="#fff2b0"/><stop offset=".35" stop-color="#ffb030"/><stop offset=".7" stop-color="#c2400f" stop-opacity=".8"/><stop offset="1" stop-color="#5a1405" stop-opacity="0"/></radialGradient>
 <radialGradient id="redglow" r="50%"><stop offset="0" stop-color="#ff3b2a" stop-opacity=".55"/><stop offset="1" stop-color="#ff3b2a" stop-opacity="0"/></radialGradient>
 <radialGradient id="screen" r="70%"><stop offset="0" stop-color="#bfe8ff"/><stop offset="1" stop-color="#3a6f8f"/></radialGradient>
</defs>"""

INK = "#1d1a16"
CCOL = ["#3e5d6b", "#5c6e3a", "#7a3a2c", "#3b4f7a", "#6b5a2a", "#2f5a4f", "#6a3d5c"]

def M(v): return v * G

def container(x, y, w=6, h=2.4, color=None, rng=None, cut=False, text=None, rot=0):
    rng = rng or random.Random(int(x * 7 + y * 13))
    c = color or rng.choice(CCOL)
    X, Y, W, H = M(x), M(y), M(w), M(h)
    ribs = "".join(f'<path d="M{X + i * 18:.0f} {Y}v{H}" stroke="#000" stroke-opacity=".25" stroke-width="4"/>' for i in range(1, int(W / 18)))
    s = f'<g transform="rotate({rot} {X + W / 2:.0f} {Y + H / 2:.0f})" filter="url(#shadow)">{R(X, Y, W, H, c, "#111", 4)}{ribs}'
    if cut:
        s += R(X + W * 0.3, Y + H * 0.25, W * 0.4, H * 0.5, "#0b0b0a", "#222", 3)
    if text:
        s += f'<text x="{X + W / 2:.0f}" y="{Y + H / 2 + 12:.0f}" font-family="DejaVu Sans" font-weight="bold" font-size="34" fill="#e8e4d8" text-anchor="middle">{text}</text>'
    return s + "</g>"

def tree(x, y, r=1.4, rng=None):
    rng = rng or random.Random(int(x * 31 + y))
    X, Y = M(x), M(y)
    blobs = "".join(f'<circle cx="{X + rng.uniform(-r, r) * 30:.0f}" cy="{Y + rng.uniform(-r, r) * 30:.0f}" r="{rng.uniform(.5, .9) * r * G:.0f}" fill="#3d4a2a" opacity=".85"/>' for _ in range(5))
    return f'<g filter="url(#shadow)">{blobs}</g>'

def hatch(x, y, s=1):
    return R(M(x), M(y), M(s), M(s), "#0d0c0b", "#9a8a5a", 4) + f'<path d="M{M(x)} {M(y)}l{M(s)} {M(s)}M{M(x + s)} {M(y)}l-{M(s)} {M(s)}" stroke="#9a8a5a" stroke-width="3"/>'

def screen(x, y, w=2, h=0.4):
    return R(M(x), M(y), M(w), M(h), "url(#screen)", "#0c1820", 4) + R(M(x), M(y), M(w), M(h), "#000", extra='opacity=".25"')

def full(body, w, h, vign=True):
    s = finish(body, w, h, vign)
    return s.replace("<defs>", EXTRA.replace("<defs>", "<defs>").replace("</defs>", "") + "", 1) if False else s.replace(DEFS, DEFS + EXTRA, 1)

# ---------------------------------------------------------------- 1. Osada
def map_osada():
    rng = random.Random(21); w, h = 30, 20
    b = R(0, 0, M(w), M(h), "url(#sand)") + R(0, 0, M(w), M(h), "url(#dirt)", extra='opacity=".45"')
    # wydmy pyłu
    for _ in range(14):
        x, y = rng.uniform(0, M(w)), rng.uniform(0, M(h))
        b += f'<ellipse cx="{x:.0f}" cy="{y:.0f}" rx="{rng.uniform(120, 300):.0f}" ry="{rng.uniform(40, 90):.0f}" fill="#a28f68" opacity=".35" transform="rotate({rng.uniform(-20, 20):.0f} {x:.0f} {y:.0f})"/>'
    # ruiny na północy
    for i in range(9):
        x = 1 + i * 3.3 + rng.uniform(-.4, .4)
        b += f'<g filter="url(#shadow)">{R(M(x), M(rng.uniform(-.5, .6)), M(rng.uniform(2, 3)), M(rng.uniform(1, 1.8)), "#4a4741", "#25221e", 4)}</g>'
    b += rubble(rng, 120, M(w), M(2.6))
    # droga
    b += f'<path d="M0 {M(17.5)} C{M(8)} {M(16.5)} {M(14)} {M(15)} {M(30)} {M(14.2)}" fill="none" stroke="#6b5a40" stroke-width="{M(2.2)}" opacity=".85"/>'
    b += f'<path d="M0 {M(17.5)} C{M(8)} {M(16.5)} {M(14)} {M(15)} {M(30)} {M(14.2)}" fill="none" stroke="#584a35" stroke-width="6" stroke-dasharray="30 40" opacity=".6"/>'
    # tablica
    b += R(M(4.8), M(15.2), 12, M(1.6), "#3a2a1c") + f'<g transform="rotate(-8 {M(5)} {M(15)})">{R(M(3.6), M(14.6), M(2.6), M(0.8), "#6e5236", INK, 3)}{label(M(4.9), M(15.15), "TUMBLER", 30, "#efe3c7")}</g>'
    # karczma
    b += f'<g filter="url(#shadow)">{R(M(8), M(6.5), M(14), M(5.5), "url(#roof)", "#1d1813", 8)}</g>'
    b += R(M(8.3), M(9.1), M(13.4), 8, "#2c241e", extra='opacity=".7"')
    b += R(M(18.5), M(6.0), M(1), M(1.2), "#3a3430", INK, 3) + f'<circle cx="{M(19)}" cy="{M(5.6)}" r="30" fill="#b8b0a0" opacity=".35"/>'
    b += door(14.5, 12, True, 1.5)
    b += label(M(15), M(9.4), "TUMBLER", 46, "#efe3c7", stroke="#1d1813")
    # zagroda Gendo i drewno
    b += f'<rect x="{M(10)}" y="{M(3)}" width="{M(5)}" height="{M(2.6)}" fill="none" stroke="#5b4430" stroke-width="10" stroke-dasharray="26 10"/>' + label(M(12.5), M(4.6), "zagroda", 26, INK, weight="normal")
    for i in range(4): b += R(M(16 + i * .5), M(3.3), 30, M(1.6), "#6e5236", INK, 2)
    # Alkowa
    b += f'<g filter="url(#shadow)">{R(M(24), M(7), M(3.6), M(3.2), "url(#tin)", INK, 6)}</g>'
    b += f'<path d="M{M(25.8)} {M(7)}V{M(4.6)}M{M(25.8)} {M(5)}l-50 -40M{M(25.8)} {M(5.4)}l55 -35M{M(25)} {M(7)}V{M(5.6)}" stroke="#2a2a2a" stroke-width="6"/>'
    b += f'<circle cx="{M(25.8)}" cy="{M(4.6)}" r="10" fill="#e33"/>' + label(M(25.8), M(11), "Alkowa Tokena", 30, INK, stroke="#d8c8a4")
    b += door(25, 10.2, True, 1)
    # wieża strażnicza
    X, Y = M(4), M(6)
    b += f'<g filter="url(#shadow)">{R(X, Y, M(2.4), M(2.4), "url(#planks)", INK, 6)}<path d="M{X} {Y}l{M(2.4)} {M(2.4)}M{X + M(2.4)} {Y}l-{M(2.4)} {M(2.4)}" stroke="#2c2016" stroke-width="5"/></g>'
    b += R(X + M(2.4), Y + M(.9), M(.5), M(.6), "#5b4430", INK, 2) + label(M(5.2), M(9.3), "wieża", 30, INK, stroke="#d8c8a4")
    # beczki, studnia
    for i in range(5): b += barrel(22.4 + (i % 2) * .8, 9 + i * .5)
    b += f'<circle cx="{M(6.5)}" cy="{M(12)}" r="{M(.8)}" fill="#3b3f40" stroke="{INK}" stroke-width="6"/>' + label(M(6.5), M(13.4), "studnia", 26, INK, weight="normal")
    b += label(M(15), M(1.9), "ruiny magazynów → Wektor", 34, "#efe3c7", stroke="#1d1813")
    b += label(M(28.5), M(19.3), "TUMBLER — OSADA", 44, "#efe3c7", anchor="end", stroke="#1d1813")
    return full(b, w, h)

# ---------------------------------------------------------------- 2. Izba
def map_izba():
    w, h = 24, 16
    b = R(0, 0, M(w), M(h), "#15120f")
    b += wall_room(1, 1, 22, 14, "planks")
    b += wall_room(17, 1, 6, 6, "tiles")  # kuchnia
    b += gap(17, 3, False, 1.2, "tiles")
    # lada w kształcie L
    b += R(M(12.5), M(2), M(1), M(7.5), "#4a3422", INK, 5) + R(M(12.5), M(8.5), M(4.5), M(1), "#4a3422", INK, 5)
    # półki z butelkami za ladą
    b += R(M(14.7), M(2), M(.5), M(6), "#3a2a1c", INK, 3)
    rng = random.Random(4)
    for i in range(24):
        b += f'<circle cx="{M(14.95):.0f}" cy="{M(2.2) + i * 17:.0f}" r="7" fill="{rng.choice(["#3f6b3a", "#7a5a2a", "#9fb4b8", "#5a2a2a"])}"/>'
    # stoły
    for (x, y) in [(3, 3), (3, 8), (7, 5), (7, 11), (3, 12)]:
        b += table(x, y, 2, 1.4)
        for dx, dy in [(-.6, .2), (2.1, .2), (-.6, .9), (2.1, .9)]: b += chair(x + dx, y + dy)
    b += f'<circle cx="{M(4)}" cy="{M(3.7)}" r="22" fill="#5b3a22" stroke="{INK}" stroke-width="3"/>'
    b += label(M(4), M(2.6), "Shutterzy", 26, "#f0e0c0", stroke=INK)
    # kominek / piec
    b += R(M(20), M(1.2), M(2.6), M(1.2), "#2a2622", INK, 4) + f'<circle cx="{M(21.3)}" cy="{M(1.9)}" r="34" fill="url(#lamp)"/>'
    b += label(M(20), M(5.4), "kuchnia", 28, INK, weight="normal")
    # schody do piwnicy
    for i in range(6): b += R(M(19) + i * 14, M(10), 12, M(2), "#3a2a1c", INK, 2)
    b += label(M(20.5), M(12.8), "piwnica ↓", 26, "#e8d9b8", stroke=INK)
    # drzwi
    b += door(9, 15, True, 1.5) + door(23, 9, False, 1)
    b += label(M(9.8), M(15.8), "wejście", 24, "#e8d9b8", stroke=INK)
    for (x, y) in [(5, 6), (10, 3), (10, 12)]: b += f'<circle cx="{M(x)}" cy="{M(y)}" r="110" fill="url(#lamp)"/>'
    b += label(M(1.4), M(15.7), "TUMBLER — IZBA", 36, "#e8d9b8", anchor="start", stroke=INK)
    return full(b, w, h)

# ---------------------------------------------------------------- 3. Ruiny i Wektor (bez siatki)
def map_ruiny():
    rng = random.Random(33); W, H = 2400, 1600; ink = "#2a241c"
    b = R(0, 0, W, H, "#cbbd98") + R(0, 0, W, H, "url(#dirt)", extra='opacity=".25"')
    # hale magazynów
    halls = []
    for row in range(4):
        for col in range(6):
            x, y = 120 + col * 300 + rng.uniform(-20, 20), 140 + row * 330 + rng.uniform(-20, 20)
            if 1200 < x < 2000 and 450 < y < 1150: continue
            hw, hh = rng.uniform(190, 240), rng.uniform(200, 250)
            halls.append((x, y, hw, hh))
            b += f'<rect x="{x:.0f}" y="{y:.0f}" width="{hw:.0f}" height="{hh:.0f}" fill="#8a8172" stroke="{ink}" stroke-width="4" opacity=".9"/>'
            for _ in range(2):
                b += f'<circle cx="{x + rng.uniform(30, hw - 30):.0f}" cy="{y + rng.uniform(30, hh - 30):.0f}" r="{rng.uniform(22, 40):.0f}" fill="#4f5f37" opacity=".75"/>'
            # runy
            b += f'<text x="{x + hw / 2:.0f}" y="{y + hh / 2 + 10:.0f}" font-family="DejaVu Sans" font-size="30" fill="#5a2a1a" text-anchor="middle" opacity=".7">{rng.choice(["ᛉ", "ᛟ", "ᚦ", "ᛞ", "ᛝ", "ᛜ"])}</text>'
    # pnie łączące dachy
    for _ in range(8):
        (x1, y1, w1, h1), (x2, y2, w2, h2) = rng.sample(halls, 2)
        if abs(x1 - x2) < 400 and abs(y1 - y2) < 400:
            b += f'<path d="M{x1 + w1 / 2:.0f} {y1 + h1 / 2:.0f}L{x2 + w2 / 2:.0f} {y2 + h2 / 2:.0f}" stroke="#5b4430" stroke-width="12" opacity=".7"/>'
    # Wektor
    vx, vy, vw, vh = 1320, 560, 600, 460
    b += f'<g filter="url(#shadow)"><rect x="{vx}" y="{vy}" width="{vw}" height="{vh}" fill="#d9d4c8" stroke="{ink}" stroke-width="8"/></g>'
    for i in range(7): b += R(vx - 22, vy + 20 + i * 64, 22, 40, "#efebe2", ink, 3) + R(vx + vw, vy + 20 + i * 64, 22, 40, "#efebe2", ink, 3)
    for i in range(14):
        ax, ay = vx + 60 + i * 38, vy + 40 + (i % 3) * 30
        b += f'<path d="M{ax} {ay}v-30m-10 10l10 -10l10 10" stroke="#333" stroke-width="3" fill="none"/>'
    b += R(vx + 200, vy + vh - 10, 200, 26, "#111") + label(vx + 300, vy + vh + 60, "brama", 30, ink)
    b += R(vx + vw + 18, vy + 300, 14, 60, "#555", ink, 3) + label(vx + vw + 40, vy + 420, "drzwi bez klamki", 26, ink, anchor="start")
    b += label(vx + vw / 2, vy + 190, "WEKTOR", 70, "#2a241c")
    # plac z wirami pyłu
    for i in range(6):
        cx, cy = vx + 120 + i * 70, vy + vh + 150 + (i % 2) * 40
        b += f'<path d="M{cx} {cy} m-30 0 a30 30 0 1 1 30 30 a20 20 0 1 1 -20 -20" fill="none" stroke="#8a7a5a" stroke-width="4" opacity=".7"/>'
    # ścieżka od Tumblera
    b += f'<path d="M60 1560 C400 1450 700 1400 900 1250 S1250 1150 1500 1100" fill="none" stroke="#6b4a2a" stroke-width="8" stroke-dasharray="20 18"/>'
    b += label(80, 1530, "← do Tumblera", 34, ink, anchor="start")
    locs = [("A", 760, 1180, "Grób Draffa"), ("B", 1040, 330, "Punkt widokowy (dachy)"), ("C", 1620, 1240, "Plac z wirami pyłu"), ("D", 1480, 920, "Fałszywa Alkowa (szyb)")]
    for k, x, y, n in locs:
        b += f'<circle cx="{x}" cy="{y}" r="32" fill="#7a1a14" stroke="{ink}" stroke-width="4"/>' + label(x, y + 12, k, 34, "#f3ead6")
        b += label(x, y + 70, n, 30, ink, stroke="#d9ccae")
    b += f'<g transform="translate(2200 1420)"><circle r="80" fill="none" stroke="{ink}" stroke-width="4"/><path d="M0 -100 L16 0 L0 100 L-16 0Z" fill="{ink}"/>{label(0, -110, "N", 32, ink)}</g>'
    b += label(120, 80, "RUINY MAGAZYNÓW I WEKTOR", 50, ink, anchor="start")
    return svg(W, H, b + R(0, 0, W, H, "#000", extra='filter="url(#grain)" opacity=".6"') + R(0, 0, W, H, "url(#vign)", extra='opacity=".6"')).replace(DEFS, DEFS + EXTRA, 1)

# ---------------------------------------------------------------- 4. Hala (Dzicz)
def map_hala():
    rng = random.Random(44); w, h = 32, 22
    b = R(0, 0, M(w), M(h), "url(#concrete)")
    b += R(0, 0, M(w), M(h), "url(#dirt)", extra='opacity=".25"')
    # filary
    for x in range(4, 32, 7):
        for y in range(4, 22, 7):
            b += R(M(x), M(y), M(1), M(1), "#7d7a72", "#2f2d29", 5) + label(M(x + .5), M(y + .65), f"{x}{y}", 22, "#b3261e")
    # winda (lądowisko) po lewej
    b += f'<circle cx="{M(3)}" cy="{M(11)}" r="{M(3)}" fill="url(#redglow)"/>'
    b += R(M(1.5), M(9.5), M(3), M(3), "#2b3a40", "#111", 6) + f'<path d="M{M(4.5)} {M(9.5)}v{M(3)}" stroke="#999" stroke-width="10" stroke-dasharray="6 10"/>'
    b += label(M(3), M(13.4), "winda", 26, "#e8e4d8", stroke="#000")
    # klatki Gendo
    for i in range(3):
        b += f'<rect x="{M(1.5 + i * 2)}" y="{M(17.5)}" width="{M(1.6)}" height="{M(1.6)}" fill="none" stroke="#999" stroke-width="5" stroke-dasharray="8 8"/>'
    b += label(M(3.8), M(20.2), "klatki Gendo (otwarte)", 24, "#e8e4d8", stroke="#000")
    # labirynt kontenerów
    spots = [(6, 2, 0), (6, 5, 0), (13, 2.5, 90), (8, 8, 0), (8, 14, 0), (12, 16.5, 0), (6, 19, 0), (15, 8, 90), (17, 13, 0), (11, 11, 0),
             (19, 3, 0), (22, 16.5, 0), (14, 19, 0), (20, 9, 90), (25, 2, 0)]
    for (x, y, r) in spots:
        b += container(x, y, 6, 2.4, rng=rng, rot=r, cut=rng.random() < .3)
    b += container(8, 11.2, 4, 2.4, text="TĘDY →", color="#3e5d6b")
    b += container(17, 16, 6, 2.4, text="TU, GÓRĄ ↑", color="#7a3a2c")
    # góra złomu (lawina)
    for _ in range(40):
        x, y = rng.uniform(M(12), M(16)), rng.uniform(M(13.5), M(15.5))
        b += f'<rect x="{x:.0f}" y="{y:.0f}" width="{rng.uniform(20, 60):.0f}" height="{rng.uniform(10, 40):.0f}" fill="{rng.choice(["#6a5a4a", "#4a4a4a", "#7a6a3a"])}" transform="rotate({rng.uniform(0, 90):.0f} {x:.0f} {y:.0f})"/>'
    b += label(M(14), M(16.2), "złom (pułapka)", 22, "#e8e4d8", stroke="#000")
    # beczki
    for _ in range(14): b += barrel(rng.uniform(5, 26), rng.uniform(1, 21), mark=rng.random() < .2)
    # most suwnicy
    b += f'<path d="M{M(17)} 0V{M(22)}" stroke="#c9a23a" stroke-width="22" stroke-dasharray="40 14" opacity=".85"/>'
    for i, y in enumerate([4, 7.5, 11]):
        b += container(17.6 if i else 16, y, 3, 2.2, color="#6b5a2a", rot=8 * (i - 1))
    b += label(M(18.8), M(14.2), "most suwnicy (wiszące kontenery)", 24, "#f0e0a0", stroke="#000")
    # ściana kontenerów po prawej
    for y in range(0, 22, 3):
        b += container(26, y, 6, 2.6, rng=rng)
    b += label(M(29), M(21.6), "ściana kontenerów → jaskinia", 24, "#e8e4d8", stroke="#000")
    # schody do wyjścia
    for i in range(10): b += R(M(8 + i * 1.8), M(.2), M(1.6), M(.6), "#8a8a80", "#222", 3)
    b += R(M(26.5), M(.1), M(1.4), M(.9), "#222", "#c9a23a", 5) + label(M(27.2), M(1.6), "wyjście", 24, "#f0e0a0", stroke="#000")
    b += label(M(1), M(21.7), "WEKTOR — HALA (DZICZ KOWALA)", 34, "#e8e4d8", anchor="start", stroke="#000")
    return full(b, w, h)

# ---------------------------------------------------------------- 5. Wnętrze i spalarnia
def map_wnetrze():
    rng = random.Random(55); w, h = 30, 20
    b = R(0, 0, M(w), M(h), "url(#grating)")
    # pomieszczenia z wyciętymi ścianami
    rooms = [(1, 1, 7, 5), (9, 1, 6, 5), (16, 1, 6, 5), (1, 8, 6, 5), (8, 8, 7, 4), (1, 14, 8, 5), (10, 14, 6, 5)]
    for (x, y, rw, rh) in rooms:
        b += R(M(x), M(y), M(rw), M(rh), "url(#concrete)", "#1a1a18", 12)
        b += R(M(x + rw * .4), M(y + rh) - 8, M(rw * .25), 16, "url(#grating)")
    # ekrany
    for (x, y) in [(1.5, 1.3), (5.2, 1.3), (9.5, 1.3), (16.5, 1.3), (1.5, 8.3), (10.5, 14.3)]:
        b += screen(x, y)
    b += label(M(4.5), M(4.2), "ekrany: EMBARGO", 24, "#e8f4ff", stroke="#000")
    # drukarka
    b += R(M(10.5), M(2.6), M(3), M(1.6), "#d9d4c8", "#111", 5) + f'<circle cx="{M(12)}" cy="{M(3.4)}" r="70" fill="url(#lamp)"/>'
    for i in range(6): b += R(M(9.2) + i * 34, M(5.2), 26, 36, "#e8e0c8", "#555", 1, f'transform="rotate({rng.uniform(-20, 20):.0f} {M(9.2) + i * 34} {M(5.2)})"')
    b += label(M(12), M(6.6), "drukarka Draftów", 26, "#f0e0a0", stroke="#000")
    # kamery
    for (x, y) in [(1.2, 1.2), (8.6, 1.2), (21.6, 1.2), (1.2, 7.8), (14.6, 7.8), (1.2, 13.6), (15.6, 13.6), (28.6, 10)]:
        b += f'<circle cx="{M(x)}" cy="{M(y)}" r="16" fill="#111" stroke="#e33" stroke-width="5"/>'
    # włazy
    for (x, y) in [(6.2, 6.4), (16.3, 6.5), (8.3, 12.6), (12.3, 12.6), (17.5, 10.5), (6.5, 18.6)]:
        b += hatch(x, y, .9)
    # rampy
    b += f'<path d="M{M(16)} {M(9)}h{M(5)}l{M(1)} {M(2)}h-{M(5)}z" fill="#6a665e" stroke="#111" stroke-width="5"/>' + label(M(18.5), M(12.4), "rampa ↓", 24, "#e8e4d8", stroke="#000")
    # spalarnia
    b += R(M(21), M(8), M(8), M(11), "#2a1a12", "#111", 14)
    b += f'<circle cx="{M(25)}" cy="{M(13)}" r="{M(4)}" fill="url(#fire)"/>'
    for i in range(5): b += R(M(22) + i * 90, M(9), 70, 70, "#c9c0b0", "#333", 3, 'opacity=".8"')
    b += R(M(28.3), M(8.4), M(.6), M(10.2), "#3a3a3a", "#111", 4)
    for i in range(12): b += R(M(28.35), M(8.7) + i * 58, 30, 18, rng.choice(["#e33", "#ddd", "#36c"]), "#000", 2)
    b += label(M(25), M(18.2), "SPALARNIA · pulpit sterowania →", 26, "#ffe0a0", stroke="#000")
    # podest i drzwi awaryjne
    b += R(M(23), M(1), M(6), M(2), "#5b5850", "#111", 5) + R(M(27.6), M(1.2), M(1.2), M(1.6), "#111", "#c9a23a", 5)
    b += label(M(25.5), M(4), "podest · drzwi awaryjne", 24, "#f0e0a0", stroke="#000")
    b += label(M(1), M(19.7), "WEKTOR — WNĘTRZE I SPALARNIA", 34, "#e8e4d8", anchor="start", stroke="#000")
    return full(b, w, h)

MAPS = {
    "tumbler-osada": (map_osada, (30, 20), "Tumbler — osada"),
    "tumbler-izba": (map_izba, (24, 16), "Tumbler — izba"),
    "ruiny-wektor": (map_ruiny, None, "Ruiny magazynów i Wektor"),
    "wektor-hala": (map_hala, (32, 22), "Wektor — hala (Dzicz Kowala)"),
    "wektor-wnetrze": (map_wnetrze, (30, 20), "Wektor — wnętrze i spalarnia"),
}

if __name__ == "__main__":
    out = "/home/claude/embargo/assets/maps"; os.makedirs(out, exist_ok=True)
    from PIL import Image
    for k, (fn, _, _) in MAPS.items():
        open(f"/tmp/{k}.svg", "w").write(fn())
        subprocess.run(["rsvg-convert", f"/tmp/{k}.svg", "-o", f"/tmp/{k}.png"], check=True)
        Image.open(f"/tmp/{k}.png").convert("RGB").save(f"{out}/{k}.webp", quality=82)
        print(k)
