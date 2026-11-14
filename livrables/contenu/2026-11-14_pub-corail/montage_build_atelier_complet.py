#!/usr/bin/env python3
"""Montage v3 : version atelier + toutes les photos et vidéos."""
import os, sys, subprocess
S = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, S)
import build as b
import build2 as b2

A = os.path.join(S, "atelier")
b.OUT = os.path.join(S, "out3"); os.makedirs(b.OUT, exist_ok=True)
U, FPS = b.U, b.FPS

if __name__ == "__main__":
    f = lambda n: os.path.join(U, n)
    PILE, DBL, PAR = (os.path.join(A, x + "_clean.png") for x in ("pile", "double", "parure"))
    V_CAB = f("f7931ecd-7388d7b4-be02-4c9e-aaa0-26ee4d18dfc7.mov")
    V_BUST = f("bab66282-9ed1598e-994d-423d-ba81-a2978ec03b85.mov")
    V_CAL = f("6c4b63cb-61d86e0a-f273-4f8e-9b30-b1eb54366039.mov")
    V_DBL = f("26ccb1dd-cb99e4b8-9fb7-4916-8073-480709c941c6.mov")
    cap = b.caption_png
    fr = lambda *a, **k: b2.framed_seg(*a, **k)
    Y = 1450
    segs = []
    def seg(name): p = os.path.join(b.OUT, name + ".mp4"); segs.append(p); return p

    b.dark_seg(seg("s00"), PILE, 3.2, b.intro_png(), bright=-0.30, text_in=0.2)
    b.photo_seg(seg("s01"), PILE, 3.2, cap("c01", "Trésor de la mer", "Méditerranée"), zoom_in=False, z=0.10)
    b.photo_seg(seg("s02"), DBL, 3.2, cap("c02", "Corail rouge véritable", "Tabarka · Tunisie"), z=0.08)
    fr(seg("s03"), DBL, V_DBL, 4.0, cap("c03", "Double rang d'exception", "corail rouge naturel", y=Y), 600, video_start=0.5)
    b.photo_seg(seg("s04"), PAR, 3.2, cap("c04", "Parures complètes", "collier · bracelet · boucles"), zoom_in=False, z=0.08)
    fr(seg("s05"), PILE, V_BUST, 3.6, cap("c05", "Un héritage", "méditerranéen", y=Y), 600, video_start=7.8)
    fr(seg("s06"), DBL, f("0d2b10db-image.jpg"), 3.0, cap("c06", "Un éclat naturel", "sans artifice", y=Y), 760)
    fr(seg("s07"), PAR, V_CAL, 4.5, cap("c07", "Chaque perle mesurée", y=Y), 600, video_start=0.0)
    fr(seg("s08"), PILE, f("fefac000-image.jpg"), 2.6, cap("c08", "Au millimètre près", y=Y), 760)
    fr(seg("s09"), DBL, f("a4919b62-image.jpg"), 2.8, cap("c09", "Chaque gramme pesé", y=Y), 760)
    fr(seg("s10"), PAR, f("8518bfd5-image.jpg"), 2.8, cap("c10", "Cabochons & chapelets", "pièces uniques", y=Y), 760)
    fr(seg("s11"), PILE, V_CAB, 3.4, cap("c11", "Des formes rares", "ovales · gouttes · carrés", y=Y), 600, video_start=2.5)
    fr(seg("s12"), DBL, f("c690d19c-image.jpg"), 2.8, cap("c12", "Le rouge profond", "de la Méditerranée", y=Y), 760)
    fr(seg("s13"), PAR, f("55890166-image.jpg"), 3.0, cap("c13", "Des perles d'exception", "colliers en dégradé", y=Y), 760)
    b.dark_seg(seg("s14"), DBL, 5.0, b.outro_png(), bright=-0.36, text_in=0.3)

    durs = [float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration",
            "-of", "csv=p=0", p]).decode()) for p in segs]
    inputs = sum([["-i", p] for p in segs], [])
    fc, last, t, XF = [], "[0:v]", 0.0, b.XF
    for i in range(1, len(segs)):
        t += durs[i - 1] - XF
        fc.append(f"{last}[{i}:v]xfade=transition=fade:duration={XF}:offset={t:.3f}[x{i}]"); last = f"[x{i}]"
    total = sum(durs) - XF * (len(segs) - 1)
    fc.append(f"{last}fade=in:st=0:d=0.5,fade=out:st={total-0.8:.3f}:d=0.8,format=yuv420p[v]")
    final = os.path.join(b.OUT, "majdi_corail_pub_atelier_complete.mp4")
    b.run(inputs + ["-filter_complex", ";".join(fc), "-map", "[v]", "-c:v", "libx264", "-preset", "slow",
                    "-crf", "18", "-pix_fmt", "yuv420p", "-r", str(FPS), "-movflags", "+faststart", final])
    print("OK", final, round(total, 2), "s")
