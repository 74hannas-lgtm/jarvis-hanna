#!/usr/bin/env python3
"""Montage v2 : version atelier de haute joaillerie."""
import os, sys, subprocess
S = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, S)
import build as b
from PIL import Image, ImageDraw, ImageFilter

A = os.path.join(S, "atelier")
b.OUT = os.path.join(S, "out2"); os.makedirs(b.OUT, exist_ok=True)
U, W, H, FPS = b.U, b.W, b.H, b.FPS

def frame_png(name, w, h, top):
    """Cadre doré + ombre portée autour de la zone photo."""
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    left = (W - w) // 2
    sh = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    ImageDraw.Draw(sh).rectangle([left - 6, top + 14, left + w + 6, top + h + 30], fill=(0, 0, 0, 190))
    img.alpha_composite(sh.filter(ImageFilter.GaussianBlur(26)))
    d = ImageDraw.Draw(img)
    d.rectangle([left - 14, top - 14, left + w + 13, top + h + 13], outline=b.GOLD + (255,), width=3)
    d.rectangle([left - 5, top - 5, left + w + 4, top + h + 4], outline=b.GOLD + (140,), width=1)
    # le centre doit rester transparent (on y pose la photo)
    p = os.path.join(b.OUT, name + ".png"); img.save(p); return p

def framed_seg(out, bg_img, src, dur, caption, w, video_start=None):
    n = int(dur * FPS)
    sw, shh = (478, 850) if video_start is not None else Image.open(src).size
    h = int(round(w * shh / sw / 2) * 2); top = 210
    fr = frame_png(os.path.basename(out)[:-4] + "_fr", w, h, top)
    left = (W - w) // 2
    if video_start is not None:
        src_in = ["-ss", str(video_start), "-t", str(dur), "-i", src]
        fg = f"[1:v]fps={FPS},scale={w}:{h}:flags=lanczos,unsharp=5:5:0.5,{b.GRADE.split(',vignette')[0]}[fg]"
    else:
        src_in = ["-loop", "1", "-t", str(dur), "-i", src]
        fg = (f"[1:v]scale={w*2}:{h*2}:flags=lanczos,zoompan=z='1+0.05*on/{n}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)'"
              f":d=1:s={w}x{h}:fps={FPS},{b.GRADE.split(',vignette')[0]}[fg]")
    fc = (f"[0:v]scale=2160:3840,boxblur=22:2,eq=brightness=-0.22[c];"
          f"[c]zoompan=z='1+0.05*on/{n}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=1:s={W}x{H}:fps={FPS},vignette=angle=0.7[bgb];"
          f"{fg};[2:v]format=rgba[fr];[bgb][fr]overlay=0:0[b1];[b1][fg]overlay={left}:{top}[b2];"
          f"[3:v]format=rgba,fade=in:st=0.35:d=0.7:alpha=1[t];[b2][t]overlay=0:0,trim=duration={dur},setsar=1[v]")
    b.run(["-loop", "1", "-t", str(dur), "-i", bg_img] + src_in +
          ["-loop", "1", "-t", str(dur), "-i", fr, "-loop", "1", "-t", str(dur), "-i", caption,
           "-filter_complex", fc, "-map", "[v]", "-t", str(dur)] + b.ENC + [out])

if __name__ == "__main__":
    f = lambda n: os.path.join(U, n)
    PILE, DBL, PAR = (os.path.join(A, x + "_clean.png") for x in ("pile", "double", "parure"))
    V_CAB = f("f7931ecd-7388d7b4-be02-4c9e-aaa0-26ee4d18dfc7.mov")
    cap = b.caption_png
    segs = []
    def seg(name): p = os.path.join(b.OUT, name + ".mp4"); segs.append(p); return p

    b.dark_seg(seg("s00"), PILE, 3.2, b.intro_png(), bright=-0.30, text_in=0.2)
    b.photo_seg(seg("s01"), PILE, 3.4, cap("c01", "Trésor de la mer", "Méditerranée"), zoom_in=False, z=0.10)
    b.photo_seg(seg("s02"), DBL, 3.4, cap("c02", "Corail rouge véritable", "Tabarka · Tunisie"), z=0.08)
    b.photo_seg(seg("s03"), PAR, 3.4, cap("c03", "Parures complètes", "collier · bracelet · boucles"), zoom_in=False, z=0.08)
    framed_seg(seg("s04"), DBL, f("0d2b10db-image.jpg"), 3.0, cap("c04", "Un éclat naturel", "sans artifice", y=1450), 760)
    framed_seg(seg("s05"), PAR, f("bc91ee83-image.jpg"), 2.8, cap("c05", "Chaque perle mesurée", y=1450), 760)
    framed_seg(seg("s06"), PILE, f("a4919b62-image.jpg"), 2.8, cap("c06", "Chaque gramme pesé", y=1450), 760)
    framed_seg(seg("s07"), PAR, V_CAB, 3.8, cap("c07", "Cabochons & chapelets", "pièces uniques", y=1450), 600, video_start=2.5)
    framed_seg(seg("s08"), DBL, f("55890166-image.jpg"), 3.0, cap("c08", "Des perles d'exception", "colliers en dégradé", y=1450), 760)
    b.dark_seg(seg("s09"), DBL, 5.0, b.outro_png(), bright=-0.36, text_in=0.3)

    durs = [float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration",
            "-of", "csv=p=0", p]).decode()) for p in segs]
    inputs = sum([["-i", p] for p in segs], [])
    fc, last, t, XF = [], "[0:v]", 0.0, b.XF
    for i in range(1, len(segs)):
        t += durs[i - 1] - XF
        fc.append(f"{last}[{i}:v]xfade=transition=fade:duration={XF}:offset={t:.3f}[x{i}]"); last = f"[x{i}]"
    total = sum(durs) - XF * (len(segs) - 1)
    fc.append(f"{last}fade=in:st=0:d=0.5,fade=out:st={total-0.8:.3f}:d=0.8,format=yuv420p[v]")
    final = os.path.join(b.OUT, "majdi_corail_pub_atelier.mp4")
    b.run(inputs + ["-filter_complex", ";".join(fc), "-map", "[v]", "-c:v", "libx264", "-preset", "slow",
                    "-crf", "18", "-pix_fmt", "yuv420p", "-r", str(FPS), "-movflags", "+faststart", final])
    print("OK", final, round(total, 2), "s")
