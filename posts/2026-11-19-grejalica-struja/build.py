import sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "tools"))
from stanologija import Deck, contact_sheet, bars

# Cene: EPS cenovnik za garantovano snabdevanje domaćinstava, važi od 1.10.2025 (AERS saglasnost 28.8.2025),
# preneto iz Nedeljnik, 1.10.2025. Cene bez akcize i PDV-a. Do 19.11.2026 nije bilo novog poskupljenja
# (Danas, 31.8.2026: EPS nije podneo zahtev; Srbija Danas/Beta, 7.11.2026: poskupljenje se očekuje 2027).
SRC_C = "Izvor: EPS cenovnik garantovanog snabdevanja domaćinstava, važi od 1.10.2025 (Nedeljnik, 1.10.2025). Cene bez akcize i PDV-a."
OBR = "Obračun STANOLOGIJA: snaga (kW) × sati = kWh; kWh × cena zone. Bez obračunske snage, akcize, PDV-a i naknada."

EXTRA = """
.tbl{margin-top:40px;width:100%;border-collapse:collapse;font-size:36px}
.tbl td{padding:22px 0;border-bottom:1px solid #2A4562;vertical-align:middle}
.tbl td.r{text-align:right;font-family:Oswald;font-weight:600;font-size:56px;white-space:nowrap;padding-left:20px;color:var(--gold)}
.tbl td.r.dim{color:var(--muted)}
.tbl small{display:block;font-size:26px;color:var(--muted);margin-top:4px}
.zone{display:inline-block;width:26px;height:26px;border-radius:50%;margin-right:16px;vertical-align:middle}
.cc .card{padding:28px 40px;margin-top:26px;font-size:33px}.cc .card b{font-size:56px}
"""

d = Deck(n=8)
add = d.add

add("""<div style="margin-top:130px"><div class="kick">Srbija · struja · zima</div>
<h1>Koliko ti<br>grejalica pojede<br><span class="gold">struje?</span></h1>
<div class="lead">Uključiš je „samo na par sati”. Evo računa po <span class="gold">EPS ceni</span>, i zašto zima gura račun u skuplju zonu.</div>
<div class="tag">Prevuci →</div></div>""")

add("""<div class="kick">Osnovni račun</div><h2>2 kW grejalica<br>= 2 kWh svaki sat</h2>
<table class="tbl">
<tr><td>1 sat</td><td class="r">2 kWh</td></tr>
<tr><td>4 sata dnevno</td><td class="r">8 kWh</td></tr>
<tr><td>4 sata × 30 dana</td><td class="r">240 kWh</td></tr>
</table>
<div class="note" style="margin-top:30px">Grejalica pretvara struju u toplotu 1 : 1. Koliko kW piše na njoj, toliko kWh troši na sat punom snagom.</div>""",
    "Obračun STANOLOGIJA: 2 kW × 4 h × 30 dana = 240 kWh. Pretpostavka: rad punom snagom (bez termostata).")

add("""<div class="kick">Cena kWh po zoni</div><h2>Isti kilovat,<br>tri cene</h2>
<table class="tbl">
<tr><td><span class="zone" style="background:#5BB974"></span>Zelena<small>do 350 kWh mesečno</small></td><td class="r">8,41 din</td></tr>
<tr><td><span class="zone" style="background:#4A90D9"></span>Plava<small>351 – 1.200 kWh</small></td><td class="r">12,62 din</td></tr>
<tr><td><span class="zone" style="background:#D9534F"></span>Crvena<small>preko 1.200 kWh</small></td><td class="r">25,24 din</td></tr>
</table>
<div class="note" style="margin-top:30px">Plava je <b>1,5×</b>, crvena <b>3×</b> skuplja od zelene. Jednotarifno brojilo.</div>""", SRC_C)

add("""<div class="kick">Zamka</div><h2>Grejalica te gura<br>u plavu zonu</h2>
<div class="cc"><div class="card"><b>210 kWh</b>primer: tročlano domaćinstvo, stan od 60 m² = <span class="gold">1.766 din</span></div>
<div class="card"><b>+240 kWh</b>grejalica = 450 kWh. Prvih 350 u zelenoj, 100 u plavoj = <span class="gold">4.206 din</span></div></div>
<div class="lead" style="margin-top:34px">Grejalica: <span class="gold">+2.439 din</span> mesečno, samo za kWh.</div>""",
    "Primer potrošnje 210 kWh: Nedeljnik, 1.10.2025. Obračun STANOLOGIJA: 350 × 8,4119 + 100 × 12,6178 = 4.205,95 din; 210 × 8,4119 = 1.766,50 din. Bez akcize, PDV-a i naknada.")

add("""<div class="kick">Jedan sat grejalice</div><h2>Koliko košta sat<br>u svakoj zoni</h2>
<table class="tbl">
<tr><td><span class="zone" style="background:#5BB974"></span>Zelena</td><td class="r">16,82 din</td></tr>
<tr><td><span class="zone" style="background:#4A90D9"></span>Plava</td><td class="r">25,24 din</td></tr>
<tr><td><span class="zone" style="background:#D9534F"></span>Crvena</td><td class="r">50,47 din</td></tr>
</table>
<div class="card"><b>~7%</b>potrošača u decembru i januaru pređe 1.200 kWh i plaća crvenu zonu (EPS).</div>""",
    SRC_C + " Udeo potrošača iznad 1.200 kWh: EPS, 2025. " + "Obračun STANOLOGIJA: 2 kWh × cena zone.")

add("""<div class="kick">Jeftina struja</div><h2>Noćna tarifa je<br>4× jeftinija</h2>
<table class="tbl">
<tr><td>Zelena, viša tarifa (VT)</td><td class="r dim">9,61 din</td></tr>
<tr><td>Zelena, niža tarifa (NT)</td><td class="r">2,40 din</td></tr>
</table>
<div class="lead" style="margin-top:34px">Isti 240 kWh: <span class="gold">2.307 din</span> danju, <span class="gold">577 din</span> noću.</div>
<div class="note">NT traje 8 h: Beograd 00–08, Vojvodina 23–07, centralna Srbija 22–06. Važi uz dvotarifno brojilo.</div>""",
    SRC_C + " Termini NT: Espreso/Mondo, 30.9.2026. Obračun STANOLOGIJA: 240 × 9,6136 i 240 × 2,4034.")

add("""<div class="kick">Isto grejanje, manje struje</div><h2>Klima A+ greje<br>4× jeftinije</h2>
<div class="big" style="margin-top:40px;font-size:170px">SCOP ≥ 4</div>
<div class="lead" style="margin-top:10px">Inverter klima klase <span class="gold">A+</span> daje najmanje 4 kWh toplote po 1 kWh struje (sezonski prosek).</div>
<div class="card"><b>≈ 505 din</b>ista toplota kao 240 kWh grejalice: oko 60 kWh struje u zelenoj zoni (procena).</div>""",
    "Izvor: Delegirana uredba (EU) 626/2011, Prilog II, Tabela 1 (A+: 4,00 ≤ SCOP < 4,60). Procena STANOLOGIJA: 240 kWh / 4 = 60 kWh × 8,4119 din. Po jakom mrazu klima je manje efikasna.")

add("""<div style="margin-top:160px"><div class="kick">Tvoj red</div>
<h1 style="font-size:92px">Pošalji pre<br><span class="gold">decembarskog</span><br>računa</h1>
<div class="lead">Pošalji ovo nekome ko greje stan grejalicom i čudi se računu. U komentaru napiši: koliko kWh ti je bilo prošlog januara?</div>
<div class="tag">Pošalji · Sačuvaj</div></div>""")

d.render(HERE, extra_css=EXTRA)
contact_sheet(HERE, 8, "/tmp/claude-0/-home-claude-stanologija-slike/2d09cfa8-4c2d-5954-a9f2-35632413031b/scratchpad/sheet.jpg")
