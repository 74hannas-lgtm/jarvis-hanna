#!/usr/bin/env python3
"""Musique originale « Corail » : piano, cordes, violoncelle, harpe. Ré majeur, 69 BPM, 12 mesures (~42 s)."""
import os, sys, subprocess
import mido

S = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(S, "music"); os.makedirs(OUT, exist_ok=True)
BPM, TPB = 69, 480
N = {n: i for i, n in enumerate(["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"])}
def p(s):  # "F#5" -> numéro MIDI
    return 12 * (int(s[-1]) + 1) + N[s[:-1]]

events = []  # (beat, channel, note, velocity, duration_beats)
def note(beat, ch, n, vel, dur): events.append((beat, ch, p(n), vel, dur))

# Accords (beat de départ, durée, voicing cordes, basse)
chords = []
prog = ["D", "Bm", "G", "A"] * 2 + ["D", "Bm", "G/A", "D9"]
VOIC = {"D": ["D4", "F#4", "A4", "C#5"], "Bm": ["D4", "F#4", "A4", "B4"], "G": ["D4", "F#4", "G4", "B4"],
        "A": ["C#4", "E4", "A4"], "D9": ["D4", "F#4", "A4", "E5"]}
BASS = {"D": "D2", "Bm": "B1", "G": "G1", "A": "A1", "D9": "D2"}
ARP = {"D": ["D3", "A3", "E4", "F#4", "A4", "F#4", "E4", "A3"], "Bm": ["B2", "F#3", "C#4", "D4", "F#4", "D4", "C#4", "F#3"],
       "G": ["G2", "D3", "A3", "B3", "D4", "B3", "A3", "D3"], "A": ["A2", "E3", "B3", "C#4", "E4", "C#4", "B3", "E3"],
       "D9": ["D3", "A3", "E4", "F#4", "A4", "F#4", "E4", "A3"]}
for bar, c in enumerate(prog):
    b0 = bar * 4
    parts = [("G", b0, 2), ("A", b0 + 2, 2)] if c == "G/A" else [(c, b0, 4)]
    for ch, st, du in parts:
        last = bar == 11
        vel = 44 if bar < 2 else (52 if bar < 8 else 56)
        dur = du + (2.5 if last else 0.15)
        for v in VOIC[ch]: note(st, 1, v, vel, dur)                       # cordes
        if bar >= 1: note(st, 2, BASS[ch], 50 if bar < 8 else 58, dur)    # violoncelle
        if 2 <= bar <= 10:                                                # arpèges piano
            arp = ARP[ch][: int(du * 2)]
            for k, a in enumerate(arp):
                note(st + k * 0.5, 0, a, 34 + (6 if k == 0 else 0) + (4 if bar >= 4 else 0), 1.2)

# Mélodie piano (à partir de la mesure 5)
mel = [  # (mesure, beat dans la mesure, note, durée)
    (4, 0, "A5", 2), (4, 2, "F#5", 1), (4, 3, "E5", 1),
    (5, 0, "F#5", 3), (5, 3, "D5", 1),
    (6, 0, "B4", 1), (6, 1, "D5", 1), (6, 2, "G5", 1), (6, 3, "F#5", 1),
    (7, 0, "E5", 3), (7, 3, "C#5", 1),
    (8, 0, "A5", 2), (8, 2, "B5", 1), (8, 3, "A5", 1),
    (9, 0, "F#5", 2), (9, 2, "E5", 1), (9, 3, "D5", 1),
    (10, 0, "E5", 1), (10, 1, "G5", 1), (10, 2, "F#5", 1), (10, 3, "E5", 1),
    (11, 0, "F#5", 4.5),
]
for bar, bt, n, d in mel:
    note(bar * 4 + bt, 0, n, 62 if bar < 8 else 68, d + 0.1)
note(11 * 4, 0, "D5", 52, 4.5); note(11 * 4, 0, "A4", 48, 4.5)

# Harpe : glissando d'ouverture et de fin (comme une vague)
scale = ["D4", "E4", "F#4", "A4", "B4", "D5", "E5", "F#5", "A5", "B5", "D6"]
for k, n in enumerate(scale): note(0.25 + k * 0.17, 3, n, 40 + k * 2, 3)
for k, n in enumerate(scale[::-1][:8][::-1]): note(11 * 4 + 1 + k * 0.2, 3, n, 34 + k * 2, 3)

mid = mido.MidiFile(ticks_per_beat=TPB)
tr = mido.MidiTrack(); mid.tracks.append(tr)
msgs = [(0, mido.MetaMessage("set_tempo", tempo=mido.bpm2tempo(BPM)))]
for ch, prog_no, vol, pan in [(0, 0, 100, 60), (1, 49, 88, 64), (2, 42, 80, 70), (3, 46, 70, 50)]:
    msgs += [(0, mido.Message("program_change", channel=ch, program=prog_no)),
             (0, mido.Message("control_change", channel=ch, control=7, value=vol)),
             (0, mido.Message("control_change", channel=ch, control=10, value=pan)),
             (0, mido.Message("control_change", channel=ch, control=91, value=110)),
             (0, mido.Message("control_change", channel=ch, control=93, value=25))]
for beat, ch, n, vel, dur in events:
    on = int(beat * TPB); off = int((beat + dur) * TPB)
    msgs.append((on, mido.Message("note_on", channel=ch, note=n, velocity=vel)))
    msgs.append((off, mido.Message("note_off", channel=ch, note=n, velocity=0)))
msgs.sort(key=lambda m: (m[0], m[1].type == "note_on"))
t = 0
for tick, m in msgs: tr.append(m.copy(time=tick - t)); t = tick
mp = os.path.join(OUT, "corail.mid"); mid.save(mp)
wav = os.path.join(OUT, "corail_raw.wav")
subprocess.run(["fluidsynth", "-ni", "-q", "-g", "0.7", "-r", "48000", "-R", "1", "-C", "1",
                "-o", "synth.reverb.room-size=0.8", "-o", "synth.reverb.width=1.0", "-o", "synth.reverb.level=0.75",
                "-F", wav, "/usr/share/sounds/sf2/FluidR3_GM.sf2", mp], check=True)
print("OK", wav, 12 * 4 * 60 / BPM, "s")
