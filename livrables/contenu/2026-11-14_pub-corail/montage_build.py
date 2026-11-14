#!/usr/bin/env python3
"""Montage publicitaire Majdi Corail, 1080x1920, 30 fps."""
import os, subprocess
from PIL import Image, ImageDraw, ImageFont, ImageFilter

S = os.path.dirname(os.path.abspath(__file__))
U = "/root/.claude/uploads/71c43adb-20f1-53bf-b0bd-bd6fa7e0564a"
OUT = os.path.join(S, "out"); os.makedirs(OUT, exist_ok=True)
FD = os.path.join(S, "fonts")
CG = FD + "/fontsource-cormorant-garamond-5.3.0/files/cormorant-garamond-latin-%s.woff"
CZ = FD + "/fontsource-cinzel-5.3.0/files/cinzel-latin-%s-normal.woff"
W, H, FPS, XF = 1080, 1920, 30, 0.6
GOLD = (217, 184, 106); CREAM = (240, 230, 210)
GRADE = ("eq=contrast=1.07:saturation=1.10:gamma=0.96,"
         "colorbalance=rs=0.03:gs=0.0:bs=-0.04:rh=0.02:bh=-0.03,"
         "vignette=angle=0.62")

def font(path, size): return ImageFont.truetype(path, size)

def spaced(draw, xy_center_y, text, f, fill, spacing, anchor_x=W // 2, shadow=True):
    widths = [draw.textlength(c, font=f) for c in text]
    total = sum(widths) + spacing * (len(text) - 1)
    x = anchor_x - total / 2
    for c, w in zip(text, widths):
        if shadow:
            draw.text((x + 2, xy_center_y + 3), c, font=f, fill=(0, 0, 0, 150), anchor="lm")
        draw.text((x, xy_center_y), c, font=f, fill=fill + (255,), anchor="lm")
        x += w + spacing

def ornament(draw, y, half=70):
    cx = W // 2
    draw.line([(cx - half - 14, y), (cx - 14, y)], fill=GOLD + (230,), width=2)
    draw.line([(cx + 14, y), (cx + half + 14, y)], fill=GOLD + (230,), width=2)
    draw.polygon([(cx, y - 7), (cx + 7, y), (cx, y + 7), (cx - 7, y)], fill=GOLD + (255,))

def soft_text(img, y, text, f, fill):
    """Texte centré avec ombre douce floutée."""
    sh = Image.new("RGBA", img.size, (0, 0, 0, 0))
    ImageDraw.Draw(sh).text((W // 2, y + 4), text, font=f, fill=(0, 0, 0, 200), anchor="mm")
    sh = sh.filter(ImageFilter.GaussianBlur(8))
    img.alpha_composite(sh)
    ImageDraw.Draw(img).text((W // 2, y), text, font=f, fill=fill + (255,), anchor="mm")

def gradient(img, y0, y1, amax, up=False):
    d = ImageDraw.Draw(img)
    for y in range(0, H):
        r = (y - y0) / (y1 - y0)
        if up: r = 1 - r
        r = min(max(r, 0), 1)
        a = int(amax * r ** 1.3)
        if a: d.line([(0, y), (W, y)], fill=(8, 4, 4, a))

def top_mark(img):
    d = ImageDraw.Draw(img)
    spaced(d, 175, "MAJDI CORAIL", font(CZ % "500", 30), GOLD, 9)

def caption_png(name, line1, line2=None, y=1330):
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    if y > 900: gradient(img, y - 480, y + 120, 200)
    else: gradient(img, y - 120, y + 420, 200, up=True)
    # haut : léger voile pour la marque
    d = ImageDraw.Draw(img)
    for yy in range(0, 300):
        d.line([(0, yy), (W, yy)], fill=(8, 4, 4, int(110 * (1 - yy / 300) ** 1.5)))
    top_mark(img)
    ornament(d, y - 95)
    soft_text(img, y, line1, font(CG % "500-italic", 84), GOLD)
    if line2:
        spaced(ImageDraw.Draw(img), y + 95, line2.upper(), font(CZ % "500", 34), CREAM, 5)
    p = os.path.join(OUT, name + ".png"); img.save(p); return p

def intro_png():
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    ornament(d, 760, 110)
    spaced(d, 870, "MAJDI", font(CZ % "500", 124), GOLD, 26)
    spaced(d, 1010, "CORAIL", font(CZ % "500", 124), GOLD, 26)
    ornament(d, 1110, 110)
    soft_text(img, 1200, "Corail rouge de Tabarka", font(CG % "500-italic", 60), CREAM)
    p = os.path.join(OUT, "intro.png"); img.save(p); return p

def outro_png():
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    spaced(d, 560, "MAJDI CORAIL", font(CZ % "500", 64), GOLD, 14)
    ornament(d, 660, 110)
    soft_text(img, 800, "L'élégance rare", font(CG % "500-italic", 104), GOLD)
    soft_text(img, 910, "de la mer", font(CG % "500-italic", 104), GOLD)
    d = ImageDraw.Draw(img)
    # bouton CTA
    bx0, bx1, by0, by1 = 200, 880, 1080, 1180
    d.rounded_rectangle([bx0, by0, bx1, by1], radius=50, outline=GOLD + (255,), width=3, fill=(20, 8, 6, 140))
    spaced(d, (by0 + by1) // 2, "COMMANDEZ EN MESSAGE PRIVÉ", font(CZ % "500", 30), CREAM, 3, shadow=False)
    soft_text(img, 1290, "Instagram  @majdicorail", font(CG % "500-normal", 52), CREAM)
    soft_text(img, 1365, "TikTok  @jewelrycoralred", font(CG % "500-normal", 52), CREAM)
    p = os.path.join(OUT, "outro.png"); img.save(p); return p

def run(args):
    r = subprocess.run(["ffmpeg", "-v", "error", "-y"] + args)
    if r.returncode: raise SystemExit("ffmpeg failed: " + " ".join(args))

ENC = ["-c:v", "libx264", "-preset", "medium", "-crf", "17", "-pix_fmt", "yuv420p", "-r", str(FPS), "-an"]

def overlay_chain(base, png_idx, dur, text_in=0.35):
    return (f"{base};[{png_idx}:v]format=rgba,fade=in:st={text_in}:d=0.7:alpha=1[t];"
            f"[bg][t]overlay=0:0:format=auto,trim=duration={dur},setsar=1[v]")

def photo_seg(out, img, dur, png, mode="fill", zoom_in=True, z=0.09, crop=None, blur_bg=False):
    n = int(dur * FPS)
    zexpr = f"1+{z}*on/{n}" if zoom_in else f"1+{z}-{z}*on/{n}"
    pre = f"crop={crop}," if crop else ""
    if blur_bg:
        comp = (f"[0:v]{pre}split[a][b];"
                f"[a]scale=2160:3840:force_original_aspect_ratio=increase,crop=2160:3840,boxblur=40:2,eq=brightness=-0.18:saturation=0.9[bgb];"
                f"[b]scale=2040:-2[fg];[bgb][fg]overlay=(W-w)/2:(H-h)/2-80[c]")
    else:
        comp = f"[0:v]{pre}scale=2160:3840:force_original_aspect_ratio=increase:flags=lanczos,crop=2160:3840[c]"
    base = (comp + f";[c]zoompan=z='{zexpr}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=1:s={W}x{H}:fps={FPS},"
            f"{GRADE}[bg]")
    run(["-loop", "1", "-t", str(dur), "-i", img, "-loop", "1", "-t", str(dur), "-i", png,
         "-filter_complex", overlay_chain(base, 1, dur), "-map", "[v]", "-t", str(dur)] + ENC + [out])

def video_seg(out, vid, start, dur, png):
    base = (f"[0:v]scale={W}:{H}:force_original_aspect_ratio=increase:flags=lanczos,crop={W}:{H},"
            f"unsharp=5:5:0.6,fps={FPS},{GRADE}[bg]")
    run(["-ss", str(start), "-t", str(dur), "-i", vid, "-loop", "1", "-t", str(dur), "-i", png,
         "-filter_complex", overlay_chain(base, 1, dur), "-map", "[v]", "-t", str(dur)] + ENC + [out])

def dark_seg(out, img, dur, png, bright=-0.32, text_in=0.4):
    n = int(dur * FPS)
    base = (f"[0:v]scale=2160:3840:force_original_aspect_ratio=increase,crop=2160:3840,boxblur=28:2,"
            f"eq=brightness={bright}:saturation=1.05:contrast=1.05[c];"
            f"[c]zoompan=z='1+0.06*on/{n}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=1:s={W}x{H}:fps={FPS},vignette=angle=0.8[bg]")
    run(["-loop", "1", "-t", str(dur), "-i", img, "-loop", "1", "-t", str(dur), "-i", png,
         "-filter_complex", overlay_chain(base, 1, dur, text_in), "-map", "[v]", "-t", str(dur)] + ENC + [out])

if __name__ == "__main__":
    f = lambda n: os.path.join(U, n)
    V_BUST = f("bab66282-9ed1598e-994d-423d-ba81-a2978ec03b85.mov")
    V_CAB = f("f7931ecd-7388d7b4-be02-4c9e-aaa0-26ee4d18dfc7.mov")
    segs = []
    def seg(name): p = os.path.join(OUT, name + ".mp4"); segs.append(p); return p

    dark_seg(seg("s00"), f("91d91c0b-image.jpg"), 3.2, intro_png(), bright=-0.36, text_in=0.2)
    photo_seg(seg("s01"), f("91d91c0b-image.jpg"), 3.2, caption_png("c01", "Trésor de la mer", "Méditerranée"), zoom_in=False, z=0.12)
    video_seg(seg("s02"), V_BUST, 0.3, 4.2, caption_png("c02", "Corail rouge véritable", "Tabarka · Tunisie"))
    photo_seg(seg("s03"), f("54eed878-image.jpg"), 3.2, caption_png("c03", "Des perles d'exception", "colliers en dégradé"))
    photo_seg(seg("s04"), f("0d2b10db-image.jpg"), 3.0, caption_png("c04", "Un éclat naturel", "sans artifice"), zoom_in=False)
    photo_seg(seg("s05"), f("bc91ee83-image.jpg"), 2.8, caption_png("c05", "Chaque perle mesurée"), z=0.10)
    photo_seg(seg("s06"), f("a4919b62-image.jpg"), 2.8, caption_png("c06", "Chaque gramme pesé", y=420), z=0.06)
    photo_seg(seg("s07"), f("1bb07b20-image.jpg"), 3.2, caption_png("c07", "Parures complètes", "collier · bracelet · boucles"), crop="498:900:0:100", z=0.07)
    video_seg(seg("s08"), V_CAB, 2.5, 3.8, caption_png("c08", "Cabochons & chapelets", "pièces uniques"))
    photo_seg(seg("s09"), f("19c4e940-image.jpg"), 3.0, caption_png("c09", "Un héritage", "méditerranéen"), zoom_in=False)
    dark_seg(seg("s10"), f("55890166-image.jpg"), 5.0, outro_png(), bright=-0.40, text_in=0.3)

    # Enchaînement en fondus
    durs = [float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration",
            "-of", "csv=p=0", p]).decode()) for p in segs]
    inputs = sum([["-i", p] for p in segs], [])
    fc, last, t = [], "[0:v]", 0.0
    for i in range(1, len(segs)):
        t += durs[i - 1] - XF
        lab = f"[x{i}]"
        fc.append(f"{last}[{i}:v]xfade=transition=fade:duration={XF}:offset={t:.3f}{lab}")
        last = lab
    total = sum(durs) - XF * (len(segs) - 1)
    fc.append(f"{last}fade=in:st=0:d=0.5,fade=out:st={total-0.8:.3f}:d=0.8,format=yuv420p[v]")
    final = os.path.join(OUT, "majdi_corail_pub.mp4")
    run(inputs + ["-filter_complex", ";".join(fc), "-map", "[v]", "-c:v", "libx264", "-preset", "slow",
                  "-crf", "18", "-pix_fmt", "yuv420p", "-r", str(FPS), "-movflags", "+faststart", final])
    print("OK", final, round(total, 2), "s")
