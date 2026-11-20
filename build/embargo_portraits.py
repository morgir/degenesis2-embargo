# -*- coding: utf-8 -*-
"""Portrety-sylwetki i żetony NPC „Embargo” (ten sam styl co system)."""
import sys, os, subprocess
sys.path.insert(0, "/home/claude/build"); sys.path.insert(0, os.path.dirname(__file__))
from portraits import portrait_svg
from embargo_npcs import NPCS
from PIL import Image, ImageDraw

OUT = "/home/claude/embargo/assets"

def token(src, dst, color):
    im = Image.open(src).convert("RGBA")
    w, h = im.size
    box = (w // 2 - 210, 220, w // 2 + 210, 640)
    face = im.crop(box).resize((400, 400))
    mask = Image.new("L", (400, 400), 0); ImageDraw.Draw(mask).ellipse((6, 6, 394, 394), fill=255)
    out = Image.new("RGBA", (400, 400), (0, 0, 0, 0)); out.paste(face, (0, 0), mask)
    d = ImageDraw.Draw(out); d.ellipse((4, 4, 396, 396), outline=color, width=12); d.ellipse((16, 16, 384, 384), outline=(0, 0, 0, 160), width=4)
    out.save(dst, quality=88)

if __name__ == "__main__":
    os.makedirs(f"{OUT}/portraits", exist_ok=True); os.makedirs(f"{OUT}/tokens", exist_ok=True)
    for n in NPCS:
        key, name, por, sub = n[0], n[1], n[-2], n[-1]
        if not por: continue
        gear, col, acc, sym, eyes = por
        svg = portrait_svg(name, sub, gear, col, acc, sym, eyes)
        open(f"/tmp/p-{key}.svg", "w").write(svg)
        subprocess.run(["rsvg-convert", f"/tmp/p-{key}.svg", "-o", f"/tmp/p-{key}.png"], check=True)
        Image.open(f"/tmp/p-{key}.png").convert("RGB").save(f"{OUT}/portraits/{key}.webp", quality=85)
        token(f"/tmp/p-{key}.png", f"{OUT}/tokens/{key}.webp", col)
        print(key)
