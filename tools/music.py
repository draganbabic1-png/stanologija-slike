"""STANOLOGIJA - originalna instrumentalna podloga za reel (lo-fi / ambijent), generisana u kodu.
Bez tuđih snimaka i semplova -> bez autorskih prava i bez rizika da Instagram utiša zvuk.
Upotreba:  python3 tools/music.py izlaz.wav --dur 15.3 [--seed 20261122] [--bpm 88]
Seed menja tonalitet, progresiju i ritam, pa svaki dan zvuči malo drugačije.
"""
import argparse, wave
import numpy as np

SR = 44100
PROGS = [  # stupnjevi (polustepeni od tonike) za 4 akorda, mol/dur sedmice
    [(0, "m7"), (8, "M7"), (3, "M7"), (10, "7")],   # i - VI - III - VII
    [(0, "M7"), (9, "m7"), (5, "M7"), (7, "7")],    # I - vi - IV - V
    [(0, "m7"), (5, "m7"), (10, "7"), (3, "M7")],   # i - iv - VII - III
    [(5, "M7"), (7, "7"), (4, "m7"), (9, "m7")],    # IV - V - iii - vi
]
SHAPES = {"m7": [0, 3, 7, 10], "M7": [0, 4, 7, 11], "7": [0, 4, 7, 10]}

def hz(midi): return 440.0 * 2 ** ((midi - 69) / 12)

def env(n, a, r):
    e = np.ones(n)
    na, nr = min(int(a * SR), n // 2), min(int(r * SR), n // 2)
    if na: e[:na] = np.linspace(0, 1, na)
    if nr: e[-nr:] *= np.linspace(1, 0, nr)
    return e

def lowpass(x, cutoff):
    a = np.exp(-2 * np.pi * cutoff / SR)
    y = np.empty_like(x); s = 0.0
    for i in range(len(x)):  # jednopolni filter, dovoljno brz za ~20 s
        s = (1 - a) * x[i] + a * s; y[i] = s
    return y

def pad(freq, n, rng):
    t = np.arange(n) / SR
    x = np.zeros(n)
    for det in (-0.12, 0.0, 0.12):
        f = freq * 2 ** (det / 12)
        ph = rng.uniform(0, 2 * np.pi)
        x += np.sin(2 * np.pi * f * t + ph) + 0.35 * np.sin(4 * np.pi * f * t + ph) + 0.12 * np.sin(6 * np.pi * f * t)
    return x / 3

def kick(n):
    t = np.arange(n) / SR
    f = 50 + 70 * np.exp(-t * 30)
    return np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t * 9)

def hat(n, rng):
    t = np.arange(n) / SR
    x = rng.standard_normal(n)
    x = x - lowpass(x, 6000)
    return x * np.exp(-t * 60)

def make(dur, seed, bpm=None):
    rng = np.random.default_rng(seed)
    bpm = bpm or int(rng.choice([82, 86, 90, 94]))
    root = 45 + int(rng.integers(0, 7))          # A2..D#3
    prog = PROGS[int(rng.integers(0, len(PROGS)))]
    beat = 60 / bpm
    bar = 4 * beat
    N = int(dur * SR)
    L = np.zeros(N); R = np.zeros(N)

    # Akordi (pad) - jedan akord po taktu
    k, t0 = 0, 0.0
    while t0 < dur:
        deg, shape = prog[k % 4]
        n = min(int(bar * SR) + int(0.4 * SR), N - int(t0 * SR))
        s = int(t0 * SR)
        chord = np.zeros(n)
        for iv in SHAPES[shape]:
            chord += pad(hz(root + 12 + deg + iv), n, rng)
        chord *= env(n, 0.25, 0.5) * 0.11
        bass = np.sin(2 * np.pi * hz(root + deg) * np.arange(n) / SR) * env(n, 0.02, 0.4) * 0.22
        L[s:s + n] += chord * 0.9 + bass; R[s:s + n] += chord * 1.1 + bass
        k += 1; t0 += bar

    # Ritam: kick na 1 i 3 (+ ponekad "i" posle 3), hi-hat na osminama
    swing = 0.06 * beat
    kn, hn = int(0.45 * SR), int(0.08 * SR)
    K, Hh = kick(kn) * 0.55, None
    step, i = beat / 2, 0
    while i * step < dur:
        t = i * step + (swing if i % 2 else 0)
        s = int(t * SR)
        pos = i % 8
        if pos in (0, 4) or (pos == 5 and rng.random() < 0.4):
            n = min(kn, N - s)
            if n > 0: L[s:s + n] += K[:n]; R[s:s + n] += K[:n]
        n = min(hn, N - s)
        if n > 0:
            h = hat(hn, rng)[:n] * (0.05 if pos % 2 else 0.08)
            L[s:s + n] += h * 0.8; R[s:s + n] += h * 1.2
        i += 1

    # Topla boja, blagi "vinyl" šum, fade in/out, normalizacija
    L = lowpass(L, 5200); R = lowpass(R, 5200)
    noise = lowpass(rng.standard_normal(N), 3000) * 0.004
    L += noise; R += noise
    e = env(N, 0.6, 1.2)
    L *= e; R *= e
    peak = max(np.abs(L).max(), np.abs(R).max())
    g = 0.7 / peak
    return np.stack([L * g, R * g], axis=1), bpm

def save(path, data):
    pcm = (np.clip(data, -1, 1) * 32767).astype("<i2")
    with wave.open(path, "wb") as w:
        w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR)
        w.writeframes(pcm.tobytes())

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("out"); ap.add_argument("--dur", type=float, required=True)
    ap.add_argument("--seed", type=int, default=0); ap.add_argument("--bpm", type=int, default=None)
    a = ap.parse_args()
    data, bpm = make(a.dur, a.seed, a.bpm)
    save(a.out, data)
    print(f"{a.out}: {a.dur:.1f} s, {bpm} BPM, seed {a.seed}")
