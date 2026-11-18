import sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "tools"))
from stanologija import Deck, contact_sheet

# Izvor pravila: JKP "Beogradske elektrane", Česta pitanja (beoelektrane.co.rs), prema Odluci o snabdevanju
# toplotnom energijom u gradu Beogradu. Provereno 18.11.2026.
SRC = "Izvor: JKP Beogradske elektrane, Česta pitanja (Odluka o snabdevanju toplotnom energijom u gradu Beogradu), pristupljeno 18.11.2026."

EXTRA = """
.tbl{margin-top:40px;width:100%;border-collapse:collapse;font-size:36px}
.tbl td{padding:20px 0;border-bottom:1px solid #2A4562;vertical-align:middle}
.tbl td.r{text-align:right;font-family:Oswald;font-weight:600;font-size:56px;white-space:nowrap;padding-left:20px;color:var(--gold)}
.tbl td.r.dim{color:var(--muted)}
.cc .card{padding:28px 40px;margin-top:26px;font-size:33px}.cc .card b{font-size:56px}
.step{display:flex;gap:28px;align-items:flex-start;margin-top:34px}
.step .n{font-family:Oswald;font-weight:700;font-size:64px;color:var(--gold);line-height:1;width:56px;flex-shrink:0}
.step .t{font-size:34px;line-height:1.4}
.step .t b{font-weight:700}
"""

d = Deck(n=8)
add = d.add

add("""<div style="margin-top:130px"><div class="kick">Beograd · daljinsko grejanje</div>
<h1>Hladno ti je?<br>Toplana ti duguje<br><span class="gold">20°C.</span></h1>
<div class="lead">Ako je u stanu hladnije, imaš pravo na <span class="gold">manji račun</span>. Evo pravila, brojeva i kako da prijaviš.</div>
<div class="tag">Prevuci →</div></div>""")

add("""<div class="kick">Propisana temperatura</div><h2>Koliko stepeni<br>po prostoriji</h2>
<table class="tbl">
<tr><td>Sobe, kuhinja, predsoblje, hodnik u stanu</td><td class="r">20°C</td></tr>
<tr><td>Kupatilo</td><td class="r">22°C</td></tr>
<tr><td>Odvojeni WC</td><td class="r">15°C</td></tr>
<tr><td>Stepenište i hodnici zgrade</td><td class="r dim">ne greje se</td></tr>
</table>
<div class="note" style="margin-top:30px">Dozvoljeno odstupanje: <b>±1°C</b>.</div>""", SRC)

add("""<div class="kick">Kako se meri</div><h2>Termometar ide<br>na pravo mesto</h2>
<div class="big" style="margin-top:50px">1 m</div>
<div class="lead" style="margin-top:10px">iznad poda, u <span class="gold">središnjem delu sobe</span>.</div>
<div class="card"><b>Ne uz prozor</b>i ne uz radijator: meri se u sredini sobe.</div>""",
    SRC + " Napomena o prozoru i radijatoru: tumačenje STANOLOGIJA pravila „središnji deo prostorije”.")

add("""<div class="kick">Kad mora da greje</div><h2>Grejni dan<br>i grejna sezona</h2>
<div class="cc"><div class="card"><b>06–22&nbsp;h</b>radnim danima. Nedeljom i praznikom 07–22&nbsp;h.</div>
<div class="card"><b>Non-stop 24 h</b>ako je u 18 h napolju ispod +1°C, a prognoza za noć ispod 0°C.</div>
<div class="card"><b>15.10. – 15.4.</b>sezona. Od 1. do 14.10. i od 16.4. do 3.5. greje se kad je prognoza srednje dnevne temperature 12°C ili niže.</div></div>""", SRC)

add("""<div class="kick">Tvoje pravo</div><h2>Hladnije od propisa<br>= manji račun</h2>
<div class="big" style="margin-top:40px">−5%</div>
<div class="lead" style="margin-top:10px">cene grejnog dana za <span class="gold">svaki stepen</span> ispod propisane temperature.</div>
<div class="card"><b>12°C ili manje</b>tog dana grejanje ne plaćaš uopšte.</div>""",
    SRC + " Primer (Obračun STANOLOGIJA): 2 stepena ispod propisa = 2 × 5% = 10% manja cena tog dana.")

add("""<div class="kick">Kako da prijaviš</div><h2>Bez zapisnika<br>nema umanjenja</h2>
<div class="step"><div class="n">1</div><div class="t">Proveri sa komšijama: ako je hladno svima, neka prijavi <b>upravnik zgrade</b>.</div></div>
<div class="step"><div class="n">2</div><div class="t">Pozovi <b class="gold">11-0-11</b> (Servisni centar Grada) ili pošalji pisanu prijavu: Savski nasip 11, Novi Beograd.</div></div>
<div class="step"><div class="n">3</div><div class="t">Ekipa mora da izađe i zapisnički utvrdi stanje <b>u roku od 24 h</b>, najkasnije za 2 dana.</div></div>
<div class="step"><div class="n">4</div><div class="t">Sačuvaj zapisnik i uporedi ga sa računom.</div></div>""",
    SRC + " Rokovi: Nova.rs, 2.12.2025. Zapisnik kao osnov reklamacije: preporuka STANOLOGIJA.")

add("""<div class="kick">Novo od ove sezone</div><h2>Isti kvadrati,<br>različit račun</h2>
<div class="lead" style="margin-top:36px">U Beogradu se grejanje sve više naplaćuje <span class="gold">po izmerenoj potrošnji</span> (kalorimetri), a manje po kvadratu.</div>
<div class="card"><b>Prozori i fasada</b>sada direktno utiču na račun: stari drveni prozori i loša izolacija = veća potrošnja.</div>
<div class="note">Cena nije menjana: predlog od +9% Grad nije usvojio.</div>""",
    "Izvor: Republika, 8.10.2026 (izjava Ljubiše Banovačkog, Beogradske elektrane). Važi za zgrade sa uređajima za merenje.")

add("""<div style="margin-top:160px"><div class="kick">Tvoj red</div>
<h1 style="font-size:92px">Koliko je<br>kod tebe <span class="gold">sada?</span></h1>
<div class="lead">Pošalji ovo komšiji ili upravniku zgrade kome je hladno. Ti napiši u komentaru koliko stepeni pokazuje tvoj termometar.</div>
<div class="tag">Pošalji · Sačuvaj</div></div>""")

d.render(HERE, extra_css=EXTRA)
contact_sheet(HERE, 8, "/tmp/claude-0/-home-claude-stanologija-slike/43e7f9d1-e34d-5583-879b-ac36ee95174e/scratchpad/sheet.jpg")
