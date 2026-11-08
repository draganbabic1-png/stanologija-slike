"""STANOLOGIJA - zajednički alat za carousel slajdove 1080x1350.
Upotreba u posts/<slug>/build.py:
    import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "tools"))
    from stanologija import Deck, bars, eur
    d = Deck(n=8); d.add(body_html, src="Izvor: ..."); ...; d.render(os.path.dirname(__file__))
Klase: .kick .gold .lead .note .tag .card(+<b>) .big h1 h2 ; bars(rows, maxv, fmt, hi=None).
"""
import asyncio, base64, os
from playwright.async_api import async_playwright

FD = os.path.join(os.path.dirname(os.path.abspath(__file__)), "fonts")

def _b64(f): return base64.b64encode(open(f, "rb").read()).decode()
def _ff(fam, pkg, w):
    return "".join(
        f"@font-face{{font-family:'{fam}';font-weight:{w};src:url(data:font/woff2;base64,{_b64(os.path.join(FD, f'{pkg}-{sub}-{w}-normal.woff2'))}) format('woff2');}}"
        for sub in ("latin", "latin-ext"))

FONTS = "".join(_ff("Oswald", "oswald", w) for w in (400, 500, 600, 700)) + \
        "".join(_ff("Montserrat", "montserrat", w) for w in (400, 500, 600, 700))

CSS = FONTS + """
:root{--navy:#0E2133;--gold:#E6B256;--cream:#F4EFE6;--muted:#9FB0C2;}
*{margin:0;padding:0;box-sizing:border-box}
body{width:1080px;height:1350px;background:var(--navy);color:var(--cream);font-family:Montserrat;overflow:hidden}
.s{position:relative;width:1080px;height:1350px;padding:96px 88px}
.brand{position:absolute;left:88px;bottom:64px;font-family:Oswald;font-weight:600;letter-spacing:6px;font-size:26px;color:var(--gold)}
.pg{position:absolute;right:88px;bottom:64px;font-size:24px;color:var(--muted);font-weight:500}
.src{position:absolute;left:88px;right:88px;bottom:118px;font-size:22px;line-height:1.45;color:var(--muted)}
.kick{font-family:Oswald;font-weight:500;font-size:30px;letter-spacing:4px;color:var(--gold);text-transform:uppercase}
h1{font-family:Oswald;font-weight:700;font-size:112px;line-height:1.02;text-transform:uppercase;margin-top:28px}
h2{font-family:Oswald;font-weight:600;font-size:68px;line-height:1.08;text-transform:uppercase;margin-top:20px}
.lead{font-size:40px;line-height:1.45;margin-top:40px;font-weight:500}
.gold{color:var(--gold)}
.row{display:flex;align-items:center;margin:0 0 34px}
.lab{width:270px;font-size:36px;font-weight:600}
.bar{height:72px;background:var(--gold);border-radius:4px}
.bar.dim{background:#3A5470}
.val{font-family:Oswald;font-size:46px;font-weight:600;margin-left:20px;white-space:nowrap}
.big{font-family:Oswald;font-weight:700;font-size:200px;line-height:1;color:var(--gold)}
.card{background:#16304A;border-left:8px solid var(--gold);padding:40px 44px;margin-top:36px;font-size:36px;line-height:1.45}
.card b{font-family:Oswald;font-weight:600;font-size:64px;color:var(--gold);display:block;margin-bottom:6px}
.line{position:absolute;left:0;top:0;width:1080px;height:14px;background:var(--gold)}
.note{font-size:30px;color:var(--muted);margin-top:24px;line-height:1.45}
.tag{display:inline-block;border:2px solid var(--gold);color:var(--gold);font-weight:700;font-size:22px;letter-spacing:3px;padding:8px 16px;margin-top:34px;text-transform:uppercase}
"""

def bars(rows, maxv, fmt, hi=None):
    out = ""
    for lab, v in rows:
        w = int(560 * v / maxv)
        cls = "bar" if (hi is None or hi(v)) else "bar dim"
        out += f'<div class="row"><div class="lab">{lab}</div><div class="{cls}" style="width:{w}px"></div><div class="val">{fmt(v)}</div></div>'
    return out

def eur(x): return f"{x:,.0f} €".replace(",", ".")

class Deck:
    def __init__(self, n):
        self.n, self.slides = n, []
    def add(self, body, src=""):
        i = len(self.slides) + 1
        s = f'<div class="s"><div class="line"></div>{body}'
        if src: s += f'<div class="src">{src}</div>'
        s += f'<div class="brand">STANOLOGIJA</div><div class="pg">{i}/{self.n}</div></div>'
        self.slides.append(s)
    def render(self, out, extra_css=""):
        assert len(self.slides) == self.n, f"{len(self.slides)} != {self.n}"
        os.makedirs(out, exist_ok=True)
        async def go():
            async with async_playwright() as p:
                b = await p.chromium.launch()
                pg = await b.new_page(viewport={"width": 1080, "height": 1350}, device_scale_factor=1)
                for i, s in enumerate(self.slides, 1):
                    await pg.set_content(f"<html><head><meta charset='utf-8'><style>{CSS}{extra_css}</style></head><body>{s}</body></html>")
                    await pg.evaluate("document.fonts.ready")
                    await pg.wait_for_timeout(300)
                    await pg.screenshot(path=f"{out}/{i:02d}.jpg", type="jpeg", quality=92)
                await b.close()
        asyncio.run(go())

def contact_sheet(out, n, path):
    """Pregledna mreža svih slajdova (za proveru preklapanja)."""
    from PIL import Image
    cols = 4; rows = (n + cols - 1) // cols
    c = Image.new("RGB", (540 * cols, 675 * rows), "white")
    for k in range(n):
        im = Image.open(f"{out}/{k+1:02d}.jpg").resize((540, 675))
        c.paste(im, ((k % cols) * 540, (k // cols) * 675))
    c.save(path, quality=85)
