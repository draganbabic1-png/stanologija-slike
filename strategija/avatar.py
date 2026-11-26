import sys, os, asyncio
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "tools"))
from stanologija import FONTS
from playwright.async_api import async_playwright
A = """<div class="w"><div class="m">S</div><div class="u"></div></div>"""
B = """<div class="w"><div class="t">STANO<br>LOGIJA</div><div class="u2"></div></div>"""
CSS = FONTS + """*{margin:0;padding:0}body{width:1080px;height:1080px;background:#0E2133}
.w{width:1080px;height:1080px;display:flex;flex-direction:column;align-items:center;justify-content:center}
.m{font-family:Oswald;font-weight:700;font-size:620px;line-height:.9;color:#E6B256}
.u{width:300px;height:34px;background:#F4EFE6;margin-top:30px}
.t{font-family:Oswald;font-weight:700;font-size:250px;line-height:.92;color:#F4EFE6;text-align:center;letter-spacing:4px}
.u2{width:520px;height:26px;background:#E6B256;margin-top:40px}"""
async def go():
    async with async_playwright() as p:
        b = await p.chromium.launch(); pg = await b.new_page(viewport={"width":1080,"height":1080})
        for n, h in (("A", A), ("B", B)):
            await pg.set_content(f"<style>{CSS}</style>{h}"); await pg.wait_for_timeout(300)
            await pg.screenshot(path=os.path.join(HERE, f"avatar_{n}.jpg"), type="jpeg", quality=95)
        await b.close()
asyncio.run(go())
