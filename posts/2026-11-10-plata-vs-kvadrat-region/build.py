import sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "tools"))
from stanologija import Deck, bars, eur, contact_sheet

KURS_RSD = 117.3611   # NBS srednji kurs, 18.8.2026.
KM = 1.95583          # fiksni kurs KM/EUR
# cena m2 novogradnje (EUR) i prosecna neto plata (EUR)
CENA = {"Hrvatska": 2994, "Crna Gora": 2557, "BiH": 3311 / KM, "Srbija": 1872}
PLATA = {"Hrvatska": 1543, "Crna Gora": 1043, "BiH": 1701 / KM, "Srbija": 117282 / KURS_RSD}
ODNOS = {k: CENA[k] / PLATA[k] for k in CENA}

def dec(v, n=2): return f"{v:.{n}f}".replace(".", ",")

EXTRA = """
.compact .lab{width:250px;flex-shrink:0}.row .bar{flex-shrink:0}
.tbl{margin-top:40px;width:100%;border-collapse:collapse;font-size:31px}
.tbl td{padding:15px 0;border-bottom:1px solid #2A4562;vertical-align:top}
.tbl td:last-child{text-align:right;font-family:Oswald;font-weight:600;font-size:40px;color:var(--gold);white-space:nowrap;padding-left:20px}
.tbl small{display:block;font-size:22px;color:var(--muted);font-weight:500;margin-top:4px}
"""

d = Deck(n=9)
add = d.add

add("""<div style="margin-top:130px"><div class="kick">Region · novembar 2026</div>
<h1>Koliko<br>plata košta<br><span class="gold">stan od<br>60 m²?</span></h1>
<div class="lead">Srbija, Hrvatska, Crna Gora i BiH. Zvanični podaci, ista računica.</div>
<div class="tag">Prevuci →</div></div>""")

r = sorted(CENA.items(), key=lambda x: -x[1])
add(f"""<div class="kick">Korak 1</div><h2>Cena m²<br>novogradnje</h2>
<div class="compact" style="margin-top:70px">{bars(r, 2994*560/470, eur)}</div>
<div class="note">BiH: 3.311 KM/m². Srbija je najjeftinija po kvadratu. Ali to je tek pola priče.</div>""",
    "Izvori: RGZ, I polugodište 2026 (SR); DZS, I polugodište 2026 (HR); Monstat, II kvartal 2026 (CG); Agencija za statistiku BiH, II kvartal 2026.")

r = sorted(PLATA.items(), key=lambda x: -x[1])
add(f"""<div class="kick">Korak 2</div><h2>Prosečna<br>neto plata</h2>
<div class="compact" style="margin-top:70px">{bars(r, 1543*560/470, eur)}</div>
<div class="note">Srbija: 117.282 din. BiH: 1.701 KM. Hrvatska plaća najviše, BiH najmanje.</div>""",
    "Izvori: RZS, avgust 2026 (SR); DZS, kolovoz 2026 (HR); Monstat, septembar 2026 (CG); Agencija za statistiku BiH, avgust 2026. Kurs NBS 117,36 din/€; 1 € = 1,95583 KM.")

r = sorted(ODNOS.items(), key=lambda x: -x[1])
add(f"""<div class="kick">Rezultat</div><h2>Koliko plata<br>za jedan m²</h2>
<div class="compact" style="margin-top:70px">{bars(r, 2.45*560/500, dec, hi=lambda v: v > 2.2)}</div>
<div class="note">Srbija, Hrvatska i BiH su skoro izjednačene: oko <span class="gold">1,9 plata</span> po kvadratu. Crna Gora iskače.</div>""",
    "Obračun STANOLOGIJA: cena m² novogradnje ÷ prosečna neto plata (u istoj valuti).")

r = sorted(((k, v * 60) for k, v in ODNOS.items()), key=lambda x: -x[1])
add(f"""<div class="kick">Stan od 60 m²</div><h2>Broj prosečnih<br>plata</h2>
<div class="compact" style="margin-top:60px">{bars(r, 147*560/480, lambda v: f"{v:.0f}")}</div>
<div class="card" style="margin-top:20px"><b>12,3 godine</b>rada u Crnoj Gori, bez trošenja ijednog evra. U ostale tri zemlje: 9,4 do 9,7 godina.</div>""",
    "Obračun STANOLOGIJA: 60 m² × cena m² ÷ prosečna neto plata; godine = broj plata ÷ 12. CG: 60 × 2.557 € ÷ 1.043 € = 147.")

add("""<div class="kick">Za godinu dana</div><h2>Koliko je<br>poskupela novogradnja</h2>
<table class="tbl">
<tr><td>Crna Gora<small>II kv. 2026. vs II kv. 2025.</small></td><td>+16,2%</td></tr>
<tr><td>Srbija<small>I pol. 2026. vs I pol. 2025.</small></td><td>+12,7%</td></tr>
<tr><td>Hrvatska<small>I pol. 2026. vs I pol. 2025.</small></td><td>+8,7%</td></tr>
<tr><td>BiH<small>II kv. 2026. vs II kv. 2025.</small></td><td>+5,2%</td></tr>
</table>
<div class="note">Glavni gradovi brže: Podgorica <span class="gold">+19,1%</span> (2.510 €/m²), Zagreb <span class="gold">+18,9%</span> (3.518 €/m²).</div>""",
    "Izvori: Monstat (20.8.2026), RGZ preko Srpske novine (7.9.2026), DZS (7.9.2026), Agencija za statistiku BiH (20.8.2026).")

add("""<div class="kick">Test kredita · Crna Gora</div><h2>Rata za stan<br>od 60 m²</h2>
<table class="tbl" style="margin-top:36px">
<tr><td>Cena stana (60 × 2.557 €)</td><td>153.420 €</td></tr>
<tr><td>Učešće 20%</td><td>30.684 €</td></tr>
<tr><td>Kredit, 25 godina, 5% kamata</td><td>122.736 €</td></tr>
<tr><td>Mesečna rata</td><td>≈ 718 €</td></tr>
</table>
<div class="card" style="font-size:32px;padding:30px 40px"><b style="font-size:56px">69% plate</b>ode na ratu ako je plata jedna. Sa dve plate: 34%.</div>""",
    "Izvor: Investitor.me, 4.11.2026. Kamata od 5% je pretpostavka analize, ne ponuda banke. Bez troškova obrade, osiguranja i opremanja.")

add("""<div class="kick">Sitna slova</div><h2>Šta ova računica<br>ne kaže</h2>
<div class="card" style="font-size:31px;padding:28px 40px"><b style="font-size:46px">Prosek ≠ tvoja plata</b>U Hrvatskoj je medijalna plata 1.336 €. Sa njom stan od 60 m² košta 134 plate, ne 116.</div>
<div class="card" style="font-size:31px;padding:28px 40px"><b style="font-size:46px">Različite metodologije</b>Svaki zavod meri drugačije (ugovori, ankete firmi, kvartal ili polugodište). Poređenje je orijentaciono.</div>
<div class="card" style="font-size:31px;padding:28px 40px"><b style="font-size:46px">Samo novogradnja</b>Starogradnja, kuće i placevi nisu uračunati.</div>""",
    "Izvor: DZS, medijalna neto plaća kolovoz 2026. Obračun STANOLOGIJA: 60 × 2.994 € ÷ 1.336 € ≈ 134.")

add("""<div style="margin-top:160px"><div class="kick">Tvoj red</div>
<h1 style="font-size:96px">Koliko bi<br>tebi <span class="gold">trebalo?</span></h1>
<div class="lead">Napiši u komentaru grad i koliko plata bi ti trebalo za 60 m². Najzanimljivije računice ulaze u sledeću analizu.</div>
<div class="tag">Sačuvaj · Pošalji nekom ko kupuje stan</div></div>""")

d.render(HERE, extra_css=EXTRA)
contact_sheet(HERE, 9, "/tmp/claude-0/-home-claude-stanologija-slike/f285df2a-47cf-5545-94a6-1f8c7ef5199d/scratchpad/sheet.jpg")
