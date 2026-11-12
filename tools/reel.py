"""STANOLOGIJA - Reel (9:16 MP4) i Story (9:16 JPEG) iz gotovih carousel slajdova.
Upotreba:  python3 tools/reel.py posts/<slug> [--slides 1,3,6,9] [--hook 3.0] [--dur 3.0]
Pravi: posts/<slug>/reel.mp4 (1080x1920, 30 fps, H.264 + tiha AAC traka) i posts/<slug>/story.jpg.
Slajd se postavlja na tamnoplavu podlogu (y=200), van zona koje pokriva Instagram UI.
"""
import argparse, os, subprocess, tempfile
from PIL import Image, ImageDraw, ImageFont

NAVY, GOLD, CREAM = (14, 33, 51), (230, 178, 86), (244, 239, 230)
W, H, Y = 1080, 1920, 200
FONT_DIRS = ["/usr/share/fonts", "/usr/local/share/fonts"]

def _font(size):
    for d in FONT_DIRS:
        for root, _, files in os.walk(d):
            for f in files:
                if f.lower() in ("oswald-bold.ttf", "oswald-semibold.ttf", "dejavusans-bold.ttf"):
                    return ImageFont.truetype(os.path.join(root, f), size)
    return ImageFont.load_default()

def frame(slide_path, top_text=None):
    c = Image.new("RGB", (W, H), NAVY)
    c.paste(Image.open(slide_path).convert("RGB"), (0, Y))
    d = ImageDraw.Draw(c)
    d.rectangle([0, Y - 6, W, Y], fill=GOLD)
    if top_text:
        f = _font(54)
        tw = d.textlength(top_text, font=f)
        d.text(((W - tw) / 2, 95), top_text, font=f, fill=GOLD)
    return c

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("post"); ap.add_argument("--slides", default="")
    ap.add_argument("--hook", type=float, default=3.0); ap.add_argument("--dur", type=float, default=3.0)
    a = ap.parse_args()
    files = sorted(f for f in os.listdir(a.post) if f[:2].isdigit() and f.endswith(".jpg"))
    idx = [int(x) for x in a.slides.split(",")] if a.slides else list(range(1, len(files) + 1))
    tmp = tempfile.mkdtemp()
    inputs, durs = [], []
    for k, i in enumerate(idx):
        p = os.path.join(tmp, f"f{k:02d}.png")
        frame(os.path.join(a.post, f"{i:02d}.jpg")).save(p)
        inputs.append(p); durs.append(a.hook if k == 0 else a.dur)
    # Story: prvi slajd + natpis
    frame(os.path.join(a.post, "01.jpg"), "NOVO NA PROFILU").save(os.path.join(a.post, "story.jpg"), quality=92)
    # Reel: kratki crossfade (0,3 s) izmedju slajdova
    X = 0.3
    cmd = ["ffmpeg", "-y", "-loglevel", "error"]
    for p, t in zip(inputs, durs):
        cmd += ["-loop", "1", "-t", f"{t + X:.2f}", "-framerate", "30", "-i", p]
    total = sum(durs) + X
    cmd += ["-f", "lavfi", "-t", f"{total:.2f}", "-i", "anullsrc=r=44100:cl=stereo"]
    fc, last, off = "", "0:v", 0.0
    for k in range(1, len(inputs)):
        off += durs[k - 1]
        out = f"v{k}"
        fc += f"[{last}][{k}:v]xfade=transition=fade:duration={X}:offset={off:.2f}[{out}];"
        last = out
    fc += f"[{last}]format=yuv420p[vout]"
    cmd += ["-filter_complex", fc, "-map", "[vout]", "-map", f"{len(inputs)}:a",
            "-c:v", "libx264", "-preset", "medium", "-crf", "20", "-r", "30",
            "-c:a", "aac", "-b:a", "128k", "-shortest", "-movflags", "+faststart",
            os.path.join(a.post, "reel.mp4")]
    subprocess.run(cmd, check=True)
    print(f"reel.mp4: {len(inputs)} slajdova, ~{total:.1f} s; story.jpg")

if __name__ == "__main__":
    main()
