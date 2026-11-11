import sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "tools"))
from stanologija import Deck, bars, eur, contact_sheet

STARA, NOVA = 5.0, 8.0          # €/m² godišnje, Zagreb (do 2026 / od 1.1.2027)
POVRSINE = [30, 50, 60, 85]
GRADOVI = [("Zagreb '27", 8.0), ("Split", 5.0), ("Rijeka", 5.0), ("Osijek", 0.6)]

def dec(v): return (f"{v:.2f}" if v < 1 else f"{v:.0f}").replace(".", ",") + " €"

EXTRA = """
.compact .row{margin-bottom:22px}.compact .bar{height:62px}.compact .lab{width:250px;flex-shrink:0;font-size:34px}.compact .val{font-size:42px}
.tbl{margin-top:40px;width:100%;border-collapse:collapse;font-size:32px}
.tbl td{padding:16px 0;border-bottom:1px solid #2A4562;vertical-align:middle}
.tbl td.r{text-align:right;font-family:Oswald;font-weight:600;font-size:42px;white-space:nowrap;padding-left:20px}
.tbl td.o{color:var(--muted);text-decoration:line-through;text-decoration-thickness:2px}
.tbl td.n{color:var(--gold)}
.tbl th{font-size:22px;color:var(--muted);font-weight:600;text-align:right;letter-spacing:2px;padding-bottom:6px}
.tbl th:first-child{text-align:left}
.li{font-size:33px;line-height:1.4;padding:18px 0 18px 54px;border-bottom:1px solid #2A4562;position:relative}
.li:before{position:absolute;left:0;top:14px;font-family:Oswald;font-weight:700;font-size:40px}
.yes .li:before{content:"✕";color:#E07A5F}.no .li:before{content:"✓";color:var(--gold)}
.li small{display:block;font-size:24px;color:var(--muted);margin-top:4px}
"""

d = Deck(n=9)
add = d.add

add("""<div style="margin-top:130px"><div class="kick">Zagreb · od 1. januara 2027.</div>
<h1>Prazan stan<br>košta <span class="gold">60%<br>više</span></h1>
<div class="lead">Porez na nekretnine skače sa 5 na 8 € po kvadratu godišnje. Ko plaća, koliko, i kako se legalno izbegava.</div>
<div class="tag">Prevuci →</div></div>""")

add(f"""<div class="kick">Šta je izglasano</div><h2>Sa 5 na 8 €<br>po m² godišnje</h2>
<div class="card"><b>8 € / m²</b>Zakonski maksimum u Hrvatskoj. Raspon koji gradovi smeju da biraju: 0,60 do 8 €.</div>
<div class="card"><b>24 : 7</b>Gradska skupština Zagreba usvojila je predlog 16. oktobra 2026. Važi od 1. januara 2027.</div>""",
    "Izvori: Porezna uprava RH (Zakon o lokalnim porezima); HRT i Index.hr, 16.10.2026.")

rows = "".join(f'<tr><td>Stan od {m} m²</td><td class="r o">{eur(m*STARA)}</td><td class="r n">{eur(m*NOVA)}</td></tr>' for m in POVRSINE)
add(f"""<div class="kick">Koliko košta</div><h2>Godišnji porez<br>za prazan stan</h2>
<table class="tbl" style="margin-top:50px"><tr><th></th><th>DO 2026.</th><th>OD 2027.</th></tr>{rows}</table>
<div class="card" style="font-size:32px;padding:30px 40px"><b style="font-size:56px">40 € mesečno</b>za prazan stan od 60 m². Do sada 25 €.</div>""",
    "Obračun STANOLOGIJA: površina × stopa (5 ili 8 €/m²); mesečno = godišnje ÷ 12. Primeri se poklapaju sa onima iz Gradske skupštine (50 m²: 250 → 400 €).")

add("""<div class="kick">Ko plaća</div><h2>Na udaru su</h2>
<div class="yes" style="margin-top:40px">
<div class="li">Stan koji stoji prazan<small>čuva se kao investicija, van tržišta najma</small></div>
<div class="li">Kratkoročni najam<small>Airbnb, Booking i slično</small></div>
<div class="li">Stan za vikend i povremeno<small>niko u njemu ne živi stalno</small></div>
<div class="li">Najam kraći od 10 meseci<small>u kalendarskoj godini</small></div>
<div class="li">Investitorski stan<small>u poslovnim knjigama 6 meseci ili duže</small></div></div>""",
    "Obveznik je vlasnik, ne podstanar. Gleda se ko je vlasnik na dan 31. marta. Izvor: Index.hr, 13.10.2026; Porezna uprava RH.")

add("""<div class="kick">Ko ne plaća</div><h2>Oslobođeni su</h2>
<div class="no" style="margin-top:40px">
<div class="li">Stan u kome neko stalno živi</div>
<div class="li">Dugoročni najam 10+ meseci<small>ugovor prijavljen Poreznoj upravi, podstanar stvarno živi u stanu</small></div>
<div class="li">Stan neuslovan za život<small>bez osnovne infrastrukture ili posle elementarne nepogode</small></div>
<div class="li">Novi investitorski stan<small>u knjigama kraće od 6 meseci (na dan 31. marta)</small></div></div>
<div class="note">Podaci koje Porezna uprava nema prijavljuju se <span class="gold">do 31. marta</span>.</div>""",
    "Izvori: Porezna uprava RH, Porez na nekretnine; Index.hr, 13.10.2026.")

add("""<div class="kick">Zašto baš sada</div><h2>Svaki šesti stan<br>u Zagrebu je prazan</h2>
<div class="big" style="margin-top:50px">55.000</div>
<div class="lead" style="margin-top:10px">praznih stanova od oko <span class="gold">350.000</span> stambenih jedinica</div>
<div class="card"><b>5 : 1</b>Na jedan stan u dugoročnom najmu dolazi pet u kratkoročnom.</div>""",
    "Izvor: izjava zamenika gradonačelnika Luke Korlaeta na sednici Skupštine (HRT, 16.10.2026). Procena grada, ne popis.")

add(f"""<div class="kick">Hrvatska</div><h2>Koliko je kvadrat<br>u drugim gradovima</h2>
<div class="compact" style="margin-top:60px">{bars(GRADOVI, 8.0*560/470, dec, hi=lambda v: v >= 8)}</div>
<div class="note">Split je stopu podigao sa 1,99 na 5 € od 2026. Osijek je na zakonskom minimumu. Najviših 8 € naplaćuju i Umag, Vis i Baška Voda.</div>""",
    "Stope u €/m² godišnje. Izvori: SveHrNekretnine (okt. 2026), Dalmacija Danas (12.11.2025), Croatia Week (14.3.2025, podaci Porezne uprave).")

add("""<div class="kick">Dve strane</div><h2>Hoće li ovo<br>vratiti stanove?</h2>
<div class="card" style="font-size:31px;padding:28px 40px"><b style="font-size:46px">Za</b>Vlast: cilj je da prazni stanovi odu u dugoročni najam. Ministar Bačić: mera je u skladu sa Nacionalnim planom stambene politike.</div>
<div class="card" style="font-size:31px;padding:28px 40px"><b style="font-size:46px">Protiv</b>Opozicija: povećanje bez konkretne analize, neće izbaciti stanove na tržište. Vlasnicima Airbnb-a 150 € više godišnje možda nije dovoljan razlog.</div>""",
    "Izvori: Financije.hr, 14.10.2026; Index.hr, 16.10.2026. Poslednja rečenica je mišljenje STANOLOGIJA (primer: 50 m², +150 €/god).")

add("""<div style="margin-top:160px"><div class="kick">Tvoj red</div>
<h1 style="font-size:96px">Da li bi ovo<br>radilo <span class="gold">kod tebe?</span></h1>
<div class="lead">Beograd, Sarajevo, Podgorica, Novi Sad... Napiši grad i da li si za porez na prazne stanove ili protiv.</div>
<div class="tag">Sačuvaj · Pošalji nekom ko ima prazan stan</div></div>""")

d.render(HERE, extra_css=EXTRA)
contact_sheet(HERE, 9, "/tmp/claude-0/-home-claude-stanologija-slike/75688a35-073b-58c3-b8ee-df39a761bda6/scratchpad/sheet.jpg")
