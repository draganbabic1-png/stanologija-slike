import sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "tools"))
from stanologija import Deck, bars, contact_sheet

SRC = "Izvor: Pravilnik o uslovima i normativima za projektovanje stambenih zgrada i stanova, „Sl. glasnik RS“ 58/2012, 74/2015, 82/2015"

STANOVI = [("Garsonjera", 26), ("Jednosoban", 30), ("Jednoiposoban", 40), ("Dvosoban", 48), ("Dvoiposoban", 56),
           ("Trosoban", 64), ("Troiposoban", 77), ("Četvorosoban", 86), ("Četvoroiposoban", 97)]
SOBE = [("Dnevna soba", "16"), ("Soba za dvoje", "11"), ("Soba za jednog", "7"), ("Kuhinja", "4"),
        ("Trpezarijski deo", "4"), ("Kupatilo", "3"), ("Odvojen WC", "1,3"), ("Plakar", "0,5")]

def m2(v): return f"{v} m²".replace(".", ",")

EXTRA = """
.compact .row{margin-bottom:16px}.compact .bar{height:50px}.compact .lab{width:330px;font-size:31px}.compact .val{font-size:38px}
.grid{display:grid;grid-template-columns:1fr 1fr;gap:22px;margin-top:50px}
.cell{background:#16304A;border-left:6px solid var(--gold);padding:22px 28px}
.cell b{display:block;font-family:Oswald;font-weight:600;font-size:58px;color:var(--gold);line-height:1.05}
.cell span{font-size:28px;font-weight:600}
.tbl{margin-top:44px;width:100%;border-collapse:collapse;font-size:32px}
.tbl td{padding:15px 0;border-bottom:1px solid #2A4562}
.tbl td:last-child{text-align:right;font-family:Oswald;font-weight:600;font-size:42px;color:var(--gold);white-space:nowrap}
"""

d = Deck(n=8)
add = d.add

add("""<div style="margin-top:150px"><div class="kick">Standardi · Srbija</div>
<h1>Koliko<br>najmanje<br><span class="gold">sme da bude<br>stan?</span></h1>
<div class="lead">Pravilnik to propisuje do kvadrata i do centimetra.</div>
<div class="tag">Prevuci →</div></div>""")

add(f"""<div class="kick">Minimum po strukturi</div><h2>Neto površina stana</h2>
<div class="compact" style="margin-top:44px">{bars(STANOVI, 97*560/400, m2)}</div>
<div class="note" style="font-size:27px;margin-top:10px">Važi za projektovanje novih zgrada. Stanovi građeni pre 2012. nisu morali da ga ispune.</div>""",
    "Izvor: Pravilnik o uslovima i normativima za projektovanje stambenih zgrada i stanova, čl. 20 („Sl. glasnik RS“ 58/2012, 74/2015, 82/2015).")

cells = "".join(f'<div class="cell"><b>{v} m²</b><span>{n}</span></div>' for n, v in SOBE)
add(f"""<div class="kick">Minimum po prostoriji</div><h2>Najmanje<br>prostorije</h2>
<div class="grid">{cells}</div>""",
    "Izvor: isti pravilnik, čl. 19. Neto površina, bez zidova.")

add("""<div class="kick">Uža ne sme</div><h2>Minimalne širine</h2>
<table class="tbl">
<tr><td>Dnevna soba (zavisi od strukture)</td><td>3,20–3,80 m</td></tr>
<tr><td>Soba za dvoje</td><td>2,40 m</td></tr>
<tr><td>Bar jedna soba u dvosobnom i većem</td><td>2,80 m</td></tr>
<tr><td>Soba za jednog</td><td>2,10 m</td></tr>
<tr><td>Kuhinja</td><td>1,70 m</td></tr>
<tr><td>Kupatilo</td><td>1,60 m</td></tr>
<tr><td>Ulazni prostor / hodnik</td><td>1,20 / 0,90 m</td></tr>
</table>
<div class="note">Plus pravilo: soba ne sme biti uža od polovine svoje dužine. Bez „hodnik-soba“ rešenja.</div>""",
    "Izvor: isti pravilnik, čl. 17.")

add("""<div class="kick">Visina i svetlo</div><h2>Plafon ne niži od</h2>
<div class="big" style="margin-top:20px;font-size:180px">2,60 m</div>
<div class="lead" style="margin-top:28px;font-size:32px">svetle visine u svim stambenim prostorijama (osim potkrovlja)</div>
<div class="card" style="font-size:31px;padding:30px 40px"><b style="font-size:52px">≥ 15% stakla</b>u odnosu na površinu poda. Soba od 11 m² → bar 1,65 m² prozora.</div>
<div class="card" style="font-size:31px;padding:30px 40px"><b style="font-size:52px">max 7,80 m</b>dubina sobe sa prozorom na jednoj strani (3 × svetla visina).</div>""",
    "Izvor: isti pravilnik, čl. 13 i 18. Obračun STANOLOGIJA: 11 m² × 15% = 1,65 m²; 3 × 2,60 m = 7,80 m.")

add("""<div class="kick">Proveri metrom</div><h2>Vrata: svetla<br>širina najmanje</h2>
<table class="tbl" style="margin-top:60px">
<tr><td>Ulazna vrata stana</td><td>90 cm</td></tr>
<tr><td>Vrata sobe</td><td>80 cm</td></tr>
<tr><td>Vrata kuhinje</td><td>70 cm</td></tr>
<tr><td>Vrata kupatila i WC-a</td><td>70 cm</td></tr>
<tr><td>Visina svih unutrašnjih vrata</td><td>200 cm</td></tr>
</table>
<div class="note">Svetla širina = otvor kroz koji se zaista prolazi, ne mera krila sa štokom. Bitno kad unosiš frižider ili kauč.</div>""",
    "Izvor: isti pravilnik, čl. 26.")

add("""<div class="kick">Kuriozitet</div><h2>Parking mesto ≈<br><span class="gold">soba za dvoje</span></h2>
<div class="card"><b>11,04 m²</b>parking mesto po pravilniku (2,30 × 4,80 m). Minimalna soba za dvoje: 11 m².</div>
<div class="card"><b>14,85 m²</b>garažni boks (2,70 × 5,50 m). To je 57% minimalne garsonjere.</div>
<div class="note">Auto i dvoje ljudi dobijaju isto mesta. Samo auto nema prozor.</div>""",
    "Izvor: isti pravilnik, čl. 3, 19, 20. Obračun STANOLOGIJA: 2,30 × 4,80; 2,70 × 5,50; 14,85 ÷ 26.")

add("""<div style="margin-top:160px"><div class="kick">Tvoj red</div>
<h1 style="font-size:96px">Da li tvoj<br>stan <span class="gold">prolazi?</span></h1>
<div class="lead">Napiši u komentaru: struktura i kvadratura. Ili najmanju sobu koju si ikad video.</div>
<div class="tag">Sačuvaj pre kupovine stana</div></div>""")

d.render(HERE, extra_css=EXTRA)
contact_sheet(HERE, 8, "/tmp/claude-0/-home-claude-stanologija-slike/c99f868f-a48b-5396-93c8-d7a9e002ace0/scratchpad/sheet.jpg")
