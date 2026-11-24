import sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "tools"))
from stanologija import Deck, bars, eur, contact_sheet

def rata(L, r, god):
    i = r / 12; n = god * 12
    return L * i / (1 - (1 + i) ** -n)

STAN = 100_000; PRINOS = 0.043; KREDIT = 90_000; KAM = 0.05; GOD = 25
KIRIJA = STAN * PRINOS / 12                  # 358,33
RATA = rata(KREDIT, KAM, GOD)                # 526,13
DOPLATA = RATA - KIRIJA                      # 167,80
POKRIVA = KIRIJA / RATA                      # 68,1%
MAX_KREDIT = KIRIJA / rata(1, KAM, GOD)      # 61.297

def pct(x, d=1): return f"{x:.{d}f}".replace(".", ",") + "%"
def e0(x): return eur(round(x))

EXTRA = """
.compact .row{margin-bottom:26px}.compact .lab{width:250px;flex-shrink:0;font-size:36px}
.tbl{margin-top:40px;width:100%;border-collapse:collapse;font-size:32px}
.tbl td{padding:18px 0;border-bottom:1px solid #2A4562;vertical-align:middle}
.tbl td.r{text-align:right;font-family:Oswald;font-weight:600;font-size:42px;white-space:nowrap;padding-left:18px}
.tbl td.o{color:var(--muted)}
.tbl td.n{color:var(--gold)}
.tbl td.up{color:#E07A5F}.tbl td.dn{color:#7FC8A9}
.tbl th{font-size:22px;color:var(--muted);font-weight:600;text-align:right;letter-spacing:2px;padding-bottom:6px}
.tbl th:first-child{text-align:left}
.li{font-size:33px;line-height:1.4;padding:16px 0 16px 54px;border-bottom:1px solid #2A4562;position:relative}
.li:before{content:"•";position:absolute;left:10px;top:8px;font-family:Oswald;font-weight:700;font-size:48px;color:var(--gold)}
.split{display:flex;height:90px;margin-top:50px;border-radius:4px;overflow:hidden}
.split div{display:flex;align-items:center;justify-content:center;font-family:Oswald;font-weight:600;font-size:34px;color:var(--navy)}
"""

N = 8
d = Deck(n=N)
add = d.add
SRC_E = "Izvor: Estitor, izveštaj o tržištu Crne Gore, 3. kv. 2026 (oglasne cene, bruto prinos bez rasta vrednosti)."

# 1 HOOK
add(f"""<div style="margin-top:120px"><div class="kick">Crna Gora · novembar 2026.</div>
<h1>Kirija otplaćuje<br>kredit? <span class="gold">Ne baš.</span></h1>
<div class="lead">Stan od 100.000 € na kredit: kirija <span class="gold">{e0(KIRIJA)}</span>, rata <span class="gold">{e0(RATA)}</span>. Razliku plaćaš ti.</div>
<div class="tag">Prevuci →</div></div>""",
    alt="Slajd 1/8, STANOLOGIJA. Naslov: Kirija otplaćuje kredit? Ne baš. Crna Gora, novembar 2026. Stan od 100.000 € kupljen na kredit: kirija oko 358 €, rata 526 € mesečno. Razliku plaća vlasnik. Prevuci.")

# 2 PRINOS
add(f"""<div class="kick">Koliko stan donosi</div><h2>4,3% godišnje<br>pre troškova</h2>
<div class="card"><b>3.073 €/m²</b>prosečna oglasna cena stana u CG, +3,5% za tri meseca.</div>
<div class="card"><b>715 €</b>prosečna oglasna kirija mesečno.</div>
<div class="note"><span class="gold">Bruto prinos</span> = godišnja kirija ÷ cena stana. Pre poreza, održavanja i meseci bez stanara.</div>""",
    SRC_E)

# 3 GRADOVI
G = [("Budva", 5.0), ("Tivat", 4.6), ("Podgorica", 4.5), ("Bar", 4.4), ("Kotor", 4.3), ("Herceg Novi", 4.0)]
add(f"""<div class="kick">Bruto prinos po gradu</div><h2>Nigde ne<br>prelazi 5%</h2>
<div class="compact" style="margin-top:56px">{bars(G, 5.0, lambda v: pct(v), hi=lambda v: v >= 4.5)}</div>
<div class="note">Za poređenje: fiksna kamata na stambeni kredit u CG je <span class="gold">oko 5%</span>.</div>""",
    SRC_E + " Kamata: Investitor.me, 24.11.2026.",
    alt="Slajd 3/8, STANOLOGIJA. Grafikon: bruto prinos od izdavanja stana po gradovima Crne Gore, 3. kvartal 2026: Budva 5,0%, Tivat 4,6%, Podgorica 4,5%, Bar 4,4%, Kotor 4,3%, Herceg Novi 4,0%. Najviši je u Budvi, najniži u Herceg Novom. Nigde ne prelazi 5%. Za poređenje, fiksna kamata na stambeni kredit u Crnoj Gori je oko 5%. Izvor: Estitor; kamata: Investitor.me 24.11.2026.")

# 4 OBRACUN
rows = (f'<tr><td>Kirija (4,3% od 100.000 €)</td><td class="r dn">+{e0(KIRIJA)}</td></tr>'
        f'<tr><td>Rata (90.000 €, 5%, 25 god.)</td><td class="r up">−{e0(RATA)}</td></tr>'
        f'<tr><td><b>Svakog meseca</b></td><td class="r up">−{e0(DOPLATA)}</td></tr>')
add(f"""<div class="kick">Primer · stan 100.000 €</div><h2>Mesečni<br>račun</h2>
<table class="tbl" style="margin-top:44px">{rows}</table>
<div class="card" style="font-size:32px;padding:30px 40px"><b style="font-size:56px">≈ 2.014 €</b>godišnje doplaćuješ iz plate. I to pre poreza i održavanja.</div>""",
    "Obračun STANOLOGIJA: kirija = 100.000 × 4,3% ÷ 12; rata = anuitet, 90.000 €, 5% fiksno, 300 meseci; doplata = rata − kirija. Pretpostavke prema Investitor.me, 24.11.2026.")

# 5 68%
add(f"""<div class="kick">Zašto ne ide</div><h2>Kirija pokriva<br><span class="gold">68%</span> rate</h2>
<div class="split"><div style="width:68.1%;background:#E6B256">kirija 68%</div><div style="width:31.9%;background:#E07A5F">ti 32%</div></div>
<div class="note" style="margin-top:50px">Rata = <span class="gold">kamata + glavnica</span>. Kirija od 4,3% ne pokriva ni kamatu od 5%, a kamoli i otplatu glavnice.</div>""",
    "Obračun STANOLOGIJA: 358,33 ÷ 526,13 = 68,1%.",
    alt="Slajd 5/8, STANOLOGIJA. Naslov: Kirija pokriva 68% rate. Traka podeljena na dva dela: kirija pokriva 68% mesečne rate, vlasnik doplaćuje 32%. Rata se sastoji od kamate i glavnice. Kirija od 4,3% godišnje ne pokriva ni kamatu od 5%, a kamoli i otplatu glavnice. Obračun STANOLOGIJA: 358,33 € podeljeno sa 526,13 € je 68,1%.")

# 6 KAMATE
K = [(0.03, rata(KREDIT, .03, GOD)), (0.04, rata(KREDIT, .04, GOD)), (0.05, RATA), (0.06, rata(KREDIT, .06, GOD))]
rows = "".join(f'<tr><td>Kamata {pct(r*100,0)}</td><td class="r n">{e0(v)}</td><td class="r {"dn" if KIRIJA>=v else "up"}">{"+" if KIRIJA>=v else "−"}{e0(abs(KIRIJA-v))}</td></tr>' for r, v in K)
add(f"""<div class="kick">Ista kirija, druga kamata</div><h2>Ni na 3%<br>ne ide</h2>
<table class="tbl" style="margin-top:44px"><tr><th></th><th>RATA</th><th>KIRIJA − RATA</th></tr>{rows}</table>
<div class="note" style="margin-top:36px">Kredit 90.000 €, 25 godina, kirija {e0(KIRIJA)}. Svaki procenat kamate = oko 50 € rate više.</div>""",
    "Obračun STANOLOGIJA: anuitetna rata za 90.000 € na 300 meseci pri kamati 3–6%.",
    alt="Slajd 6/8, STANOLOGIJA. Tabela, kredit 90.000 € na 25 godina, kirija 358 €: kamata 3% rata 427 €, razlika −68 €; kamata 4% rata 475 €, razlika −117 €; kamata 5% rata 526 €, razlika −168 €; kamata 6% rata 580 €, razlika −222 €. Ni na 3% kirija ne pokriva ratu. Svaki procenat kamate je oko 50 € rate više. Obračun STANOLOGIJA, anuitetna rata.")

# 7 KAD IDE
add(f"""<div class="kick">Kad bi kirija pokrila ratu?</div><h2>Tek sa ~40%<br>svog novca</h2>
<div class="card" style="padding:30px 40px"><b>{e0(round(MAX_KREDIT, -2))}</b>najveći kredit (5%, 25 god.) koji kirija od {e0(KIRIJA)} može da otplaćuje.</div>
<div class="card" style="padding:30px 40px"><b>≈ 39.000 €</b>učešće na stan od 100.000 €, umesto 10.000 €.</div>
<div class="note">Tada stanar otplaćuje kredit, ali porez, održavanje i prazni meseci i dalje idu iz tvog džepa.</div>""",
    "Obračun STANOLOGIJA: kredit = 358,33 ÷ anuitetni faktor (5%, 300 mes.) ≈ 61.300 €; učešće = 100.000 − 61.300.")

# 8 CTA
add("""<div style="margin-top:130px"><div class="kick">Pre nego što kupiš „za izdavanje”</div>
<h1 style="font-size:92px">Kirija ÷ rata<br>= <span class="gold">istina</span></h1>
<div class="lead">Pošalji ovo nekome ko misli da će mu stanar otplatiti kredit.</div>
<div class="note">Primer je ilustracija na oglasnim cenama, nije investicioni savet. Ista računica važi i za Beograd, Zagreb, Sarajevo.</div>
<div class="tag">Prati @stanologija · sutra: kuriozitet iz gradnje</div></div>""")

d.render(HERE, extra_css=EXTRA)
contact_sheet(HERE, N, "/tmp/claude-0/-home-claude-stanologija-slike/b5384e01-2f77-5223-9c98-254399679e9c/scratchpad/sheet.jpg")
