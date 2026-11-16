import sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "tools"))
from stanologija import Deck, bars, eur, contact_sheet

BUDZET = 100_000
# Prosečne realizovane cene stanova, €/m², 1. polugodište 2026. (RZS/RGZ, preneli Mondo/Nova ekonomija 8.9.2026. i Novosti 29.10.2026.)
GRADOVI = [("Kikinda", 957), ("Novi Pazar", 1047), ("Kragujevac", 1575), ("Užice", 1634),
           ("Niš", 1765), ("Srbija prosek", 1918), ("Novi Sad", 2359), ("Beograd", 3219)]
BG = [("Rakovica", 2600), ("Zemun", 2822), ("Čukarica", 2852), ("Vračar", 3639),
      ("Stari grad", 4030), ("Savski venac", 4210), ("Beograd na vodi", 5821)]
NOVI_M2 = 65.5   # prosečna površina stana u zgradama sa 3+ stanova, dozvole sept. 2026 (RZS)

def m2(c): return BUDZET / c
def fm(v): return f"{v:.1f}".replace(".", ",") + " m²"

EXTRA = """
.compact .row{margin-bottom:16px}.compact .bar{height:54px}.compact .lab{width:270px;flex-shrink:0;font-size:32px}.compact .val{font-size:40px}
.tbl{margin-top:36px;width:100%;border-collapse:collapse;font-size:33px}
.tbl td{padding:15px 0;border-bottom:1px solid #2A4562;vertical-align:middle}
.tbl td.r{text-align:right;font-family:Oswald;font-weight:600;font-size:42px;white-space:nowrap;padding-left:20px;color:var(--gold)}
.tbl td.m{text-align:right;color:var(--muted);font-size:28px;white-space:nowrap}
.tbl th{font-size:22px;color:var(--muted);font-weight:600;text-align:right;letter-spacing:2px;padding-bottom:6px}
.tbl th:first-child{text-align:left}
"""

d = Deck(n=8)
add = d.add

add("""<div style="margin-top:130px"><div class="kick">Srbija · realne cene iz ugovora</div>
<h1>Šta dobiješ<br>za <span class="gold">100.000 €?</span></h1>
<div class="lead">Isti novac: od <span class="gold">17</span> do <span class="gold">104</span> kvadrata. Zavisi samo od toga gde kupuješ.</div>
<div class="tag">Prevuci →</div></div>""")

add("""<div class="kick">Polazna tačka</div><h2>Prosečan stan<br>u Srbiji košta</h2>
<div class="big" style="margin-top:40px;font-size:170px">100.157 €</div>
<div class="card"><b>+15,81%</b>za godinu dana (1. polugodište 2026. prema istom periodu 2025).</div>
<div class="card"><b>197.689 €</b>prosečan stan u Beogradu. Skoro duplo više.</div>""",
    "Izvor: RZS/RGZ, 1. polugodište 2026 (Danas, 4.9.2026; Mondo/Nova ekonomija, 8.9.2026).")

add(f"""<div class="kick">Gradovi</div><h2>Kvadrata za<br>100.000 €</h2>
<div class="compact" style="margin-top:50px">{bars([(g, m2(c)) for g, c in GRADOVI], m2(957)*560/500, fm, hi=lambda v: v >= 90 or v < 35)}</div>""",
    "Obračun STANOLOGIJA: 100.000 € ÷ prosečna realizovana cena €/m² (RZS/RGZ, 1. pol. 2026; za Niš Novosti navode 1.756 €/m², Mondo 1.765). Bez troškova kupovine.")

rows = "".join(f'<tr><td>{g}</td><td class="m">{c:,} €/m²</td><td class="r">{fm(m2(c))}</td></tr>'.replace(",", ".", 1) if False else
               f'<tr><td>{g}</td><td class="m">{eur(c)}/m²</td><td class="r">{fm(m2(c))}</td></tr>' for g, c in BG)
add(f"""<div class="kick">Beograd po opštinama</div><h2>Ista suma,<br>drugi kraj grada</h2>
<table class="tbl"><tr><th></th><th>KVADRAT</th><th>ZA 100.000 €</th></tr>{rows}</table>""",
    "Obračun STANOLOGIJA: 100.000 € ÷ prosečna cena €/m². Izvor cena: RZS/RGZ, 1. pol. 2026 (Mondo/Nova ekonomija, 8.9.2026). Beograd na vodi: 55 prodatih stanova.")

add(f"""<div class="kick">Najveći raspon</div><h2>Za jedan stan<br>u Beogradu</h2>
<div class="big" style="margin-top:40px">3,4×</div>
<div class="lead" style="margin-top:10px">toliko kvadrata više dobiješ u <span class="gold">Kikindi</span> nego u proseku Beograda.</div>
<div class="card"><b>3.219 vs 957 €</b>prosečan kvadrat: Beograd naspram Kikinde.</div>""",
    "Obračun STANOLOGIJA: 3.219 ÷ 957 ≈ 3,4. Izvor: RZS/RGZ, 1. pol. 2026 (Novosti, 29.10.2026).")

NOVI = [("Beograd", 3219), ("Novi Sad", 2359), ("Niš", 1765), ("Kikinda", 957)]
rows2 = "".join(f'<tr><td>{g}</td><td class="r">≈ {eur(round(NOVI_M2*c, -2))}</td></tr>' for g, c in NOVI)
add(f"""<div class="kick">Sveže · RZS, 16.11.</div><h2>Stan u novoj zgradi:<br><span class="gold">65,5 kvadrata</span></h2>
<div class="note" style="margin-top:20px">U septembru prijavljena gradnja 3.284 stana. Prosek u zgradama sa 3+ stanova: 65,5 m². Koliko bi koštao:</div>
<table class="tbl" style="margin-top:20px">{rows2}</table>""",
    "Obračun STANOLOGIJA (procena): 65,5 m² × prosečna cena €/m² svih stanova, 1. pol. 2026, zaokruženo na 100 €. Novogradnja u centru može biti skuplja. Izvor: RZS, građevinske dozvole sept. 2026 (B92, 16.11.2026).")

add("""<div class="kick">Kako se kupuje</div><h2>Svaki treći stan<br>ide na kredit</h2>
<div class="big" style="margin-top:40px">33%</div>
<div class="lead" style="margin-top:10px">kupoprodaja stanova u Srbiji uz stambeni kredit (+3 p.p. za godinu).</div>
<div class="card"><b>40%</b>u Beogradu. Pre tri godine 23%.</div>""",
    "Izvori: RGZ, 1. pol. 2026 (Danas, 4.9.2026); Beograd: Coreside/Marera, 1. pol. 2026 vs 2023 (Kurir, 21.10.2026). Proseci kriju velike razlike između stanova.")

add("""<div style="margin-top:160px"><div class="kick">Tvoj red</div>
<h1 style="font-size:92px">Gde bi ti<br>uložio <span class="gold">100.000 €?</span></h1>
<div class="lead">Pošalji ovo nekome ko kaže „kupiću stan kad uštedim". Ti napiši u komentaru: koliko je kvadrat u tvom gradu?</div>
<div class="tag">Pošalji · Sačuvaj</div></div>""")

d.render(HERE, extra_css=EXTRA)
contact_sheet(HERE, 8, "/tmp/claude-0/-home-claude-stanologija-slike/ae1d0c2d-03e4-5d90-b7bf-dde4db15c028/scratchpad/sheet.jpg")
