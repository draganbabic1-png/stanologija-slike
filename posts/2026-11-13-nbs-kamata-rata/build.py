import sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "tools"))
from stanologija import Deck, bars, eur, contact_sheet

def pct(v, d=2): return f"{v:.{d}f} %".replace(".", ",")
def rata(P, god_pct, n=300):
    i = god_pct / 1200
    return P * i / (1 - (1 + i) ** -n)

MARZA = 3.0
EUR6M = [("jan 2026", 2.105), ("11. sep", 2.820), ("11. nov", 3.010)]
RATE = [(lab, rata(100000, e + MARZA)) for lab, e in EUR6M]

EXTRA = """
.compact .row{margin-bottom:22px}.compact .bar{height:62px}.compact .lab{width:250px;flex-shrink:0;font-size:34px}.compact .val{font-size:42px}
.li{font-size:33px;line-height:1.4;padding:18px 0 18px 64px;border-bottom:1px solid #2A4562;position:relative}
.li:before{position:absolute;left:0;top:14px;font-family:Oswald;font-weight:700;font-size:40px;color:var(--gold)}
.num{counter-reset:k}.num .li{counter-increment:k}.num .li:before{content:counter(k)}
.li small{display:block;font-size:24px;color:var(--muted);margin-top:4px}
.two{display:flex;gap:28px;margin-top:40px}.two .card{flex:1;margin-top:0}
"""

d = Deck(n=9)
add = d.add

add("""<div style="margin-top:130px"><div class="kick">NBS · 12. novembar 2026.</div>
<h1>Kamata skočila.<br>Raste li ti <span class="gold">rata?</span></h1>
<div class="lead">Narodna banka je prvi put posle 26 meseci podigla referentnu stopu. Za većinu stambenih kredita odgovor je iznenađujući.</div>
<div class="tag">Prevuci →</div></div>""")

add("""<div class="kick">Šta se desilo</div><h2>Referentna stopa<br>5,75 → 6,00 %</h2>
<div class="card"><b>+0,25</b>procentnih poena. Prvo povećanje posle 26 meseci. Depozitna olakšica 4,75 %, kreditna 7,25 %.</div>
<div class="card"><b>4,1 %</b>međugodišnja inflacija u septembru. NBS hoće da spreči da se energetski šok prelije na ostale cene.</div>
<div class="note">Sledeća odluka: <span class="gold">10. decembra 2026.</span></div>""",
    "Izvori: NBS preko Tanjuga, 12.11.2026; Magazin Biznis, 12.11.2026.")

add("""<div class="kick">Prvo pitanje</div><h2>Kakvu kamatu<br>ti imaš?</h2>
<div class="two"><div class="card"><b>Fiksnu</b>Rata se ne menja. Ni zbog NBS, ni zbog Evrope.</div>
<div class="card"><b>Promenljivu</b>Rata prati indeks za koji je kredit vezan. Proveri koji.</div></div>
<div class="card"><b>49 %</b>stambenih kredita u Srbiji odobreno je po fiksnoj kamati (jun 2026). Udeo raste.</div>""",
    "Izvor: NBS, Trendovi u kreditnoj aktivnosti banaka, Q2 2026 (prenosi VP Law Firm, 5.11.2026).")

add("""<div class="kick">Iznenađenje</div><h2>Stambeni kredit<br>ne sluša NBS</h2>
<div class="card"><b>U evrima</b>Skoro svi stambeni krediti u Srbiji indeksirani su u evrima. Promenljiva kamata = EURIBOR + marža banke.</div>
<div class="card"><b>EURIBOR</b>određuje tržište evrozone i ECB, ne Narodna banka Srbije. Zato ti rata zbog ove odluke neće automatski porasti.</div>""",
    "Izvori: Biznis.rs, 15.9.2026; Srpske novine, 12.11.2026.")

add(f"""<div class="kick">Šta stvarno pomera ratu</div><h2>Šestomesečni<br>EURIBOR u 2026.</h2>
<div class="compact" style="margin-top:60px">{bars(EUR6M, 3.010*560/470, lambda v: pct(v, 3), hi=lambda v: v > 3)}</div>
<div class="note">Od januara <span class="gold">+0,9 poena</span>. ECB je 29. oktobra zadržala depozitnu stopu na 2,50 %.</div>""",
    "Izvori: Biznis.rs, 15.9.2026 (jan. i sep.); euribor-rates.eu (11.11.2026); CNBC, 29.10.2026.")

add(f"""<div class="kick">Koliko je to u evrima</div><h2>Rata na 100.000 €<br>za 25 godina</h2>
<div class="compact" style="margin-top:60px">{bars(RATE, 645*560/470, eur, hi=lambda v: v > 640)}</div>
<div class="card" style="font-size:32px;padding:30px 40px"><b style="font-size:56px">+54 € mesečno</b>u odnosu na januar. Oko 650 € godišnje.</div>""",
    "Obračun STANOLOGIJA: anuitet = P·i / (1−(1+i)^−300), i = (EURIBOR 6M + 3 % marža) / 12. Primer, ne ponuda banke. Jan. i sep. se poklapaju sa Biznis.rs (591 i 633 €).")

add("""<div class="kick">Kome NBS ipak menja ratu</div><h2>Dinarski krediti</h2>
<div class="two"><div class="card"><b>8,4 %</b>prosečna kamata na dinarske kredite stanovništvu</div>
<div class="card"><b>4,7 %</b>na kredite u evrima i evroindeksirane</div></div>
<div class="card"><b>3–6 meseci</b>Za toliko bi novi dinarski krediti mogli da poskupe. Postojeće kredite sa fiksnom kamatom ovo ne dira.</div>""",
    "Kamate: NBS, jun 2026 (VP Law Firm, 5.11.2026). 3–6 meseci je procena Dušana Uzelca (Kamatica) za Kurir Biznis, prenele Srpske novine 12.11.2026.")

add("""<div class="kick">Uzmi ugovor u ruke</div><h2>Proveri 4 stvari</h2>
<div class="num" style="margin-top:40px">
<div class="li">Vrsta kamate<small>fiksna ili promenljiva (ili fiksna samo prvih nekoliko godina)</small></div>
<div class="li">Indeks<small>EURIBOR 3M, EURIBOR 6M ili dinarski indeks</small></div>
<div class="li">Datum usklađivanja<small>kada banka preračunava ratu (npr. na 6 meseci)</small></div>
<div class="li">Marža banke<small>fiksni deo kamate; jedini deo o kom se pregovara</small></div></div>""",
    "Saveti STANOLOGIJA na osnovu: Srpske novine, 12.11.2026 (proveriti vrstu kamate i pokazatelj za usklađivanje).")

add("""<div style="margin-top:160px"><div class="kick">Podeli</div>
<h1 style="font-size:96px">Pošalji ovo<br>nekome ko <span class="gold">otplaćuje<br>stan</span></h1>
<div class="lead">Da zna da li treba da se brine, ili samo da proveri EURIBOR. Ti napiši: fiksna ili promenljiva?</div>
<div class="tag">Pošalji · Sačuvaj za decembar</div></div>""")

d.render(HERE, extra_css=EXTRA)
contact_sheet(HERE, 9, "/tmp/claude-0/-home-claude-stanologija-slike/f4e9461b-4915-5b41-b48d-5c9e1b1e0ad1/scratchpad/sheet.jpg")
