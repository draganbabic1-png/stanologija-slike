import sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "tools"))
from stanologija import Deck, bars, eur, contact_sheet

P, N = 80000, 360                     # primer: 80.000 €, 30 godina
def ann(p, r, n): i = r / 1200; return p * i / (1 - (1 + i) ** -n)
RATE = [("Uz subvenciju<br><small>1,5 %</small>", ann(P, 1.5, N)),
        ("Bez subvencije<br><small>3,5 %</small>", ann(P, 3.5, N)),
        ("Komercijalni<br><small>primer 6 %</small>", ann(P, 6.01, N))]
# posle 6 godina: ostatak duga po EURIBOR 6M (3,01 %) + 2 %
i = 1.5 / 1200; R = ann(P, 1.5, N)
B72 = P * (1 + i) ** 72 - R * ((1 + i) ** 72 - 1) / i
POSLE6 = ann(B72, 5.01, N - 72)

EXTRA = """
.compact .row{margin-bottom:26px}.compact .bar{height:70px}.compact .lab{width:300px;flex-shrink:0;font-size:32px;line-height:1.1}
.compact .lab small{font-size:24px;color:var(--muted);font-weight:500}.compact .val{font-size:44px}
.li{font-size:33px;line-height:1.4;padding:18px 0 18px 64px;border-bottom:1px solid #2A4562;position:relative}
.li b{position:absolute;left:0;top:14px;font-family:Oswald;font-weight:700;font-size:40px;color:var(--gold)}
.li small{display:block;font-size:24px;color:var(--muted);margin-top:4px}
.w .li{padding-left:150px}
.two{display:flex;gap:28px}.two .card{flex:1;font-size:30px;padding:30px 32px}.two .card b{font-size:58px}
"""

d = Deck(n=8)
add = d.add

add("""<div style="margin-top:130px"><div class="kick">Srbija · novembar 2026.</div>
<h1>Kredit za mlade:<br><span class="gold">kraj ili<br>pauza?</span></h1>
<div class="lead">Najveća banka u programu prestala je da prima nove zahteve. Šta to znači ako planiraš prvi stan.</div>
<div class="tag">Prevuci →</div></div>""")

add("""<div class="kick">Šta se desilo</div><h2>Poštanska štedionica<br>stala sa prijemom</h2>
<div class="card"><b>440 mil. €</b>Kvota banke je popunjena: odobreni krediti plus zahtevi u obradi. Banka kaže da je mera privremena.</div>
<div class="card"><b>≈ 5.300</b>mladih je konkurisalo preko ove banke. Već primljeni zahtevi se obrađuju. Banka je tražila dodatna sredstva od Ministarstva finansija.</div>""",
    "Izvori: Banka Poštanska štedionica preko Insajder.net i Forbes Srbija (N1), 10.11.2026. Odgovor Ministarstva do tada nije stigao.")

add("""<div class="kick">A druge banke?</div><h2>Gde se još<br>može predati zahtev</h2>
<div class="two" style="margin-top:44px"><div class="card"><b>UniCredit</b>prima i obrađuje zahteve. Iskorišćeno oko 85 % limita iz tranše.</div>
<div class="card"><b>Erste</b>nastavlja sa prijemom zahteva.</div></div>
<div class="card" style="font-size:32px"><b style="font-size:52px">Bez odgovora</b>NLB, Banca Intesa i OTP nisu odgovorile novinarima. Nekim klijentima je rečeno da je kvota popunjena.</div>""",
    "Izvor: Forbes Srbija (N1), 10.11.2026. Stanje se menja iz dana u dan: proveri direktno u banci.")

add(f"""<div class="kick">Program u brojevima</div><h2>Od marta 2025.<br>do danas</h2>
<div class="big" style="font-size:180px;margin-top:40px">8.400+</div>
<div class="lead" style="margin-top:6px">odobrenih kredita, ukupno preko <span class="gold">670 mil. €</span> (kraj avgusta 2026)</div>
<div class="card" style="font-size:32px;padding:30px 40px"><b style="font-size:56px">≈ 80.000 €</b>prosečan kredit. Garantni okvir države podignut je na 900 mil. € u junu 2026.</div>""",
    "Izvori: NBS preko Insajder.net, 10.11.2026; Forbes Srbija, 10.11.2026. Obračun STANOLOGIJA: prosek = 670 mil. € ÷ 8.400 kredita (zaokruženo).")

add("""<div class="kick">Zašto su svi hteli ovaj kredit</div><h2>Uslovi programa</h2>
<div class="w" style="margin-top:34px">
<div class="li"><b>1 %</b>učešće<small>minimum od vrednosti nekretnine</small></div>
<div class="li"><b>1,5 %</b>kamata prvih 6 godina<small>fiksna 3,5 %, država plaća 2 procentna poena</small></div>
<div class="li"><b>40 g.</b>najduži rok otplate<small>otplata do 70. godine života</small></div>
<div class="li"><b>100k €</b>najviše po kreditu (100.000 €)<small>od 20. do dana pre 36. rođendana, prva nekretnina</small></div>
<div class="li"><b>6 g.</b>ne smeš da prodaš ni izdaš stan</div></div>""",
    "Izvori: Ministarstvo finansija preko Novosti (6.3.2025); Forbes Srbija, 10.11.2026. Država garantuje 40 % kredita prvih 10 godina.")

rows = bars(RATE, RATE[2][1] * 560 / 470, eur, hi=lambda v: v < 300)
add(f"""<div class="kick">Koliko vredi subvencija</div><h2>Rata na 80.000 €<br>za 30 godina</h2>
<div class="compact" style="margin-top:56px">{rows}</div>
<div class="card" style="font-size:31px;padding:28px 40px;margin-top:20px"><b style="font-size:52px">+{eur(RATE[1][1]-RATE[0][1])} mesečno</b>bez subvencije države. Posle 6 godina i u programu kamata postaje EURIBOR + 2 %: po današnjem EURIBOR-u rata bi bila oko {eur(POSLE6)}.</div>""",
    "Obračun STANOLOGIJA: anuitet = P·i / (1−(1+i)^−360), i = godišnja stopa / 12. Komercijalni primer: EURIBOR 6M 3,01 % (11.11.2026) + 3 % marže. Primer, ne ponuda banke.")

add("""<div class="kick">Ako planiraš prvi stan</div><h2>Šta da uradiš<br>ove nedelje</h2>
<div style="margin-top:34px">
<div class="li"><b>1</b>Pitaj više banaka, ne samo jednu<small>kvote su po bankama, neke i dalje primaju zahteve</small></div>
<div class="li"><b>2</b>Proveri datum rođenja<small>gleda se starost na dan predaje zahteva</small></div>
<div class="li"><b>3</b>Izračunaj ratu i bez subvencije<small>ako program stane, ostaju komercijalni uslovi</small></div>
<div class="li"><b>4</b>Ne potpisuj predugovor sa kaparom<small>dok banka pismeno ne potvrdi kredit</small></div></div>""",
    "Saveti 3 i 4 su mišljenje STANOLOGIJA, ne finansijski savet. Uslovi: Ministarstvo finansija (Novosti, 6.3.2025).")

add("""<div style="margin-top:160px"><div class="kick">Tvoj red</div>
<h1 style="font-size:92px">Znaš nekog ko<br><span class="gold">traži prvi stan?</span></h1>
<div class="lead">Pošalji mu ovo pre nego što preda zahtev. A ti napiši: da li bi uzeo kredit i bez subvencije?</div>
<div class="tag">Pošalji · Sačuvaj</div></div>""")

d.render(HERE, extra_css=EXTRA)
contact_sheet(HERE, 8, sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "..", "..", "sheet.jpg"))
print(round(RATE[0][1]), round(RATE[1][1]), round(RATE[2][1]), round(POSLE6))
