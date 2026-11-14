#!/usr/bin/env python3
"""5 propositions de logo HafsiCoral (fond sombre, or, corail, serif)."""
import os, math, random
from PIL import Image, ImageDraw, ImageFont, ImageFilter

S = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(S, "logos"); os.makedirs(OUT, exist_ok=True)
FD = os.path.join(S, "fonts")
CG = FD + "/fontsource-cormorant-garamond-5.3.0/files/cormorant-garamond-latin-%s.woff"
CZ = FD + "/fontsource-cinzel-5.3.0/files/cinzel-latin-%s-normal.woff"
SZ = 1600
BG = (14, 10, 9, 255)
GOLD_T, GOLD_B = (246, 226, 166), (176, 128, 46)
CORAL, CORAL_D = (205, 58, 44), (150, 30, 24)
F = lambda p, s: ImageFont.truetype(p, s)

def gold_fill(mask, top=None, bot=None):
    """Remplit un masque avec un dégradé or vertical."""
    w, h = mask.size
    bbox = mask.getbbox() or (0, 0, w, h)
    t0, t1 = top if top is not None else bbox[1], bot if bot is not None else bbox[3]
    grad = Image.new("RGBA", (w, h))
    gd = ImageDraw.Draw(grad)
    for y in range(h):
        r = min(max((y - t0) / max(t1 - t0, 1), 0), 1)
        r = 0.5 - 0.5 * math.cos(r * math.pi * 1.6)  # léger reflet
        c = tuple(int(GOLD_T[i] * (1 - r) + GOLD_B[i] * r) for i in range(3))
        gd.line([(0, y), (w, y)], fill=c + (255,))
    out = Image.new("RGBA", (w, h), (0, 0, 0, 0)); out.paste(grad, (0, 0), mask); return out

def text_mask(text, font, spacing=0, center=(SZ // 2, SZ // 2)):
    m = Image.new("L", (SZ, SZ), 0); d = ImageDraw.Draw(m)
    widths = [d.textlength(c, font=font) for c in text]
    total = sum(widths) + spacing * (len(text) - 1)
    x = center[0] - total / 2
    for c, w in zip(text, widths):
        d.text((x, center[1]), c, font=font, fill=255, anchor="lm"); x += w + spacing
    return m

def gold_text(img, text, font, y, spacing=0, x=SZ // 2):
    m = text_mask(text, font, spacing, (x, y)); img.alpha_composite(gold_fill(m))

def gold_draw(img, fn):
    m = Image.new("L", (SZ, SZ), 0); fn(ImageDraw.Draw(m)); img.alpha_composite(gold_fill(m))

def ornament(d, y, half, cx=SZ // 2, w=3):
    d.line([(cx - half - 24, y), (cx - 24, y)], fill=255, width=w)
    d.line([(cx + 24, y), (cx + half + 24, y)], fill=255, width=w)
    d.polygon([(cx, y - 11), (cx + 11, y), (cx, y + 11), (cx - 11, y)], fill=255)

def coral_bead(img, cx, cy, r):
    """Perle de corail avec reflet."""
    b = Image.new("RGBA", (SZ, SZ), (0, 0, 0, 0)); d = ImageDraw.Draw(b)
    for k in range(r, 0, -1):
        t = k / r
        c = tuple(int(CORAL[i] * (1 - t * 0.35) + CORAL_D[i] * t * 0.35) for i in range(3))
        d.ellipse([cx - k, cy - k, cx + k, cy + k], fill=c + (255,))
    hl = Image.new("RGBA", (SZ, SZ), (0, 0, 0, 0))
    ImageDraw.Draw(hl).ellipse([cx - r * 0.55, cy - r * 0.6, cx - r * 0.1, cy - r * 0.2], fill=(255, 225, 210, 150))
    b.alpha_composite(hl.filter(ImageFilter.GaussianBlur(max(r * 0.12, 1))))
    img.alpha_composite(b)

def coral_branch(img, x, y, length, angle, width, depth, rnd, color=CORAL):
    d = ImageDraw.Draw(img)
    x2 = x + length * math.cos(angle); y2 = y - length * math.sin(angle)
    d.line([(x, y), (x2, y2)], fill=color + (255,), width=int(width))
    r = width / 2; d.ellipse([x2 - r, y2 - r, x2 + r, y2 + r], fill=color + (255,))
    d.ellipse([x - r, y - r, x + r, y + r], fill=color + (255,))
    if depth == 0: return
    for sgn in (-1, 1):
        a = angle + sgn * rnd.uniform(0.32, 0.55)
        coral_branch(img, x2, y2, length * rnd.uniform(0.66, 0.8), a, max(width * 0.7, 6), depth - 1, rnd, color)

def coral_organic(img, x, y, angle, length, width, depth, rnd, color):
    d = ImageDraw.Draw(img); steps = 7; seg = length / steps
    for i in range(steps):
        angle += rnd.uniform(-0.16, 0.16)
        w = width * (1 - 0.45 * i / steps)
        x2 = x + seg * math.cos(angle); y2 = y - seg * math.sin(angle)
        d.line([(x, y), (x2, y2)], fill=color + (255,), width=max(int(w), 4))
        r = w / 2; d.ellipse([x2 - r, y2 - r, x2 + r, y2 + r], fill=color + (255,))
        if depth > 0 and i in (2, 4) and rnd.random() < 0.95:
            sgn = 1 if (i == 2) ^ (rnd.random() < 0.5) else -1
            coral_organic(img, x2, y2, angle + sgn * rnd.uniform(0.45, 0.8), length * rnd.uniform(0.5, 0.65),
                          w * 0.75, depth - 1, rnd, color)
        x, y = x2, y2
    r = width * 0.3; d.ellipse([x - r, y - r, x + r, y + r], fill=color + (255,))

def coral_fan(img, x, y, angle, length, width, depth, rnd, color):
    d = ImageDraw.Draw(img); steps = 4; seg = length / steps
    for i in range(steps):
        angle += rnd.uniform(-0.12, 0.12)
        w = width * (1 - 0.18 * i / steps)
        x2 = x + seg * math.cos(angle); y2 = y - seg * math.sin(angle)
        d.line([(x, y), (x2, y2)], fill=color + (255,), width=int(w))
        r = w / 2; d.ellipse([x2 - r, y2 - r, x2 + r, y2 + r], fill=color + (255,))
        x, y = x2, y2
    if depth == 0:
        r = width * 0.62; d.ellipse([x - r, y - r, x + r, y + r], fill=color + (255,)); return
    spread = rnd.uniform(0.38, 0.55)
    for sgn in (-1, 1):
        a = angle + sgn * spread
        a = a + (math.pi / 2 - a) * 0.15   # tend vers le haut, en éventail
        coral_fan(img, x, y, a, length * rnd.uniform(0.72, 0.85), max(width * 0.74, 11), depth - 1, rnd, color)

def circle_text(img, text, font, cx, cy, radius, start_deg=-90, spacing_deg=None):
    n = len(text); step = spacing_deg or 360 / n
    m = Image.new("L", (SZ, SZ), 0)
    for i, ch in enumerate(text):
        a = math.radians(start_deg + i * step)
        g = Image.new("L", (160, 160), 0); ImageDraw.Draw(g).text((80, 80), ch, font=font, fill=255, anchor="mm")
        g = g.rotate(-(start_deg + i * step + 90), resample=Image.BICUBIC)
        px, py = cx + radius * math.cos(a), cy + radius * math.sin(a)
        m.paste(255, (int(px - 80), int(py - 80)), g)
    img.alpha_composite(gold_fill(m))

def canvas(): return Image.new("RGBA", (SZ, SZ), (0, 0, 0, 0))

# 1. Classique : Cinzel espacé + filets et losange
def logo1():
    im = canvas()
    gold_draw(im, lambda d: ornament(d, 560, 230))
    gold_text(im, "HAFSI", F(CZ % "500", 190), 700, 46)
    gold_text(im, "CORAL", F(CZ % "500", 190), 900, 46)
    gold_draw(im, lambda d: ornament(d, 1040, 230))
    gold_text(im, "L'ÉLÉGANCE RARE DE LA MER", F(CZ % "400", 40), 1130, 9)
    return im

# 2. Monogramme HC dans un double anneau
def logo2():
    im = canvas(); cx, cy = SZ // 2, 640
    gold_draw(im, lambda d: (d.ellipse([cx - 330, cy - 330, cx + 330, cy + 330], outline=255, width=6),
                             d.ellipse([cx - 300, cy - 300, cx + 300, cy + 300], outline=255, width=2)))
    gold_text(im, "H", F(CG % "500-normal", 440), cy + 10, 0, cx - 85)
    gold_text(im, "C", F(CG % "500-italic", 440), cy + 30, 0, cx + 95)
    coral_bead(im, cx, cy - 300, 26)
    gold_text(im, "HAFSI CORAL", F(CZ % "500", 92), 1130, 22)
    gold_text(im, "CORAIL ROUGE · TABARKA", F(CZ % "400", 38), 1230, 10)
    return im

# 3. Branche de corail + nom en italique
def logo3():
    im = canvas(); rnd = random.Random(7)
    SEED = 5
    br = canvas(); coral_fan(br, SZ // 2, 845, math.pi / 2, 130, 44, 4, random.Random(SEED), CORAL)
    shade = canvas(); coral_fan(shade, SZ // 2 + 6, 852, math.pi / 2, 130, 44, 4, random.Random(SEED), CORAL_D)
    im.alpha_composite(shade.filter(ImageFilter.GaussianBlur(3))); im.alpha_composite(br)
    gold_draw(im, lambda d: d.line([(SZ // 2 - 260, 860), (SZ // 2 + 260, 860)], fill=255, width=3))
    gold_text(im, "Hafsi Coral", F(CG % "500-italic", 200), 1000)
    gold_text(im, "HAUTE JOAILLERIE DE CORAIL", F(CZ % "400", 40), 1175, 9)
    return im

# 4. Romantique : grand italique + perles de corail
def logo4():
    im = canvas()
    gold_text(im, "Hafsi", F(CG % "600-italic", 330), 700)
    gold_text(im, "C O R A L", F(CZ % "500", 96), 965, 14)
    for k, r in enumerate([12, 16, 21, 27, 21, 16, 12]):
        coral_bead(im, SZ // 2 + (k - 3) * 62, 1090, r)
    gold_text(im, "L'élégance rare de la mer", F(CG % "500-italic", 56), 1200)
    return im

# 5. Sceau / médaillon circulaire
def logo5():
    im = canvas(); cx, cy = SZ // 2, SZ // 2
    gold_draw(im, lambda d: (d.ellipse([cx - 560, cy - 560, cx + 560, cy + 560], outline=255, width=8),
                             d.ellipse([cx - 420, cy - 420, cx + 420, cy + 420], outline=255, width=3)))
    top = "HAFSI CORAL"; st = 11
    circle_text(im, top, F(CZ % "500", 76), cx, cy, 490, -90 - st * (len(top) - 1) / 2, st)
    bot = "CORAIL ROUGE · TABARKA"; sb = 7.2
    fnt = F(CZ % "500", 56); m = Image.new("L", (SZ, SZ), 0)
    for i, ch in enumerate(bot):
        deg = 90 + sb * (len(bot) - 1) / 2 - i * sb; a = math.radians(deg)
        g = Image.new("L", (160, 160), 0); ImageDraw.Draw(g).text((80, 80), ch, font=fnt, fill=255, anchor="mm")
        g = g.rotate(-(deg - 90), resample=Image.BICUBIC)
        px, py = cx + 485 * math.cos(a), cy + 485 * math.sin(a)
        m.paste(255, (int(px - 80), int(py - 80)), g)
    im.alpha_composite(gold_fill(m))
    for k in (-1, 1):
        coral_bead(im, int(cx + k * 490), cy, 18)
    for k, r in enumerate([10, 14, 19, 24, 19, 14, 10]):
        coral_bead(im, cx + (k - 3) * 52, cy + 215, r)
    gold_text(im, "HC", F(CG % "500-normal", 300), cy - 40, 10)
    gold_draw(im, lambda d: ornament(d, cy + 120, 110))
    return im

logos = [("1_classique", logo1), ("2_monogramme", logo2), ("3_branche_corail", logo3),
         ("4_romantique", logo4), ("5_sceau", logo5)]
names = ["1. Classique", "2. Monogramme HC", "3. Branche de corail", "4. Romantique", "5. Sceau"]
thumbs = []
for (n, fn), label in zip(logos, names):
    lg = fn()
    lg.save(os.path.join(OUT, f"hafsicoral_logo_{n}_transparent.png"))
    dark = Image.new("RGBA", (SZ, SZ), BG); dark.alpha_composite(lg)
    dark.convert("RGB").save(os.path.join(OUT, f"hafsicoral_logo_{n}.png"))
    th = dark.resize((600, 600), Image.LANCZOS)
    ImageDraw.Draw(th).text((300, 570), label, font=F(CG % "500-italic", 34), fill=(200, 190, 170), anchor="mm")
    thumbs.append(th)
board = Image.new("RGBA", (1830, 1230), (8, 6, 5, 255))
for i, th in enumerate(thumbs):
    x = 15 + (i % 3) * 605 + (302 if i >= 3 else 0); y = 15 + (i // 3) * 605
    board.alpha_composite(th, (x, y))
board.convert("RGB").save(os.path.join(OUT, "hafsicoral_logos_planche.jpg"), quality=92)
print("OK")
