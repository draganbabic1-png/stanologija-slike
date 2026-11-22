import sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "tools"))
from stanologija import Deck, contact_sheet

# Izvori:
# - MPGI, "Novi Zakon o najmu stanova donosi veću sigurnost i za najmoprimce i za najmodavce", 31.7.2026 (HINA/MPGI):
#   kirija najviše 1x godišnje, 30 dana najave, najviše % rasta cena stambenih objekata u prethodnoj godini (DZS), veće povećanje ništavno;
#   polog 1 kirija; pregled 2x godišnje uz najavu; podstanar otkaz bez razloga 60 dana; opomena + 15 dana + još min. 30 dana;
#   bez krivice podstanara: min 6 meseci, 1 godina ako najam > 5 god, +6 meseci ako živi dete, ugovorom najmanje 3 meseca;
#   solemnizacija kod javnog beležnika; Agencija za osiguranje radničkih tražbina: članarina max 2% godišnje kirije (~40-150 €), bianco zadužnica do 10.000 €.
# - ZGRADOnačelnik, 31.7.2026 (početna kirija nije ograničena; povećanje = osnov za otkaz podstanara) i 3.8.2026 (e-savjetovanje 3.8.-2.9.2026).
# - najam.hr, 10.11.2026: zakon još nije na snazi, važi zakon iz 1996.
# - DZS preko RBA Research (8.4.2026) i Lider/Hina (3.4.2026): cene stambenih objekata 2025. u proseku +14,1% u odnosu na 2024.

EXTRA = """
.steps{margin-top:44px}
.st{display:flex;align-items:flex-start;margin-bottom:34px;font-size:36px;line-height:1.4}
.st .n{font-family:Oswald;font-weight:700;font-size:64px;color:var(--gold);width:80px;flex:none;line-height:1}
.tbl{margin-top:40px;width:100%;border-collapse:collapse;font-size:36px}
.tbl td{padding:22px 0;border-bottom:1px solid #2A4562;vertical-align:middle}
.tbl td.r{text-align:right;font-family:Oswald;font-weight:600;font-size:52px;white-space:nowrap;padding-left:20px;color:var(--gold)}
.tbl small{display:block;font-size:26px;color:var(--muted);margin-top:4px}
.cc .card{padding:28px 40px;margin-top:24px;font-size:32px}.cc .card b{font-size:54px}
"""

MPGI = "MPGI, predstavljanje nacrta Zakona o najmu stanova, 31.7.2026."
d = Deck(n=8)
add = d.add

add("""<div style="margin-top:120px"><div class="kick">Hrvatska · nacrt Zakona o najmu stanova</div>
<h1>Podstanar si?<br>Ovo se <span class="gold">menja</span></h1>
<div class="lead">Kirija bi smela da raste <span class="gold">najviše jednom godišnje</span>, i ne više od rasta cena stanova. Ako vlasnik otkaže bez tvoje krivice, zakonski rok za iseljenje je <span class="gold">6 meseci</span>.</div>
<div class="tag">Prevuci →</div></div>""",
    MPGI)

add("""<div class="kick">Gde smo sada</div><h2>Zakon još<br>nije na snazi</h2>
<table class="tbl">
<tr><td>Važeći zakon o najmu<small>i dalje se primenjuje</small></td><td class="r">1996.</td></tr>
<tr><td>Ministarstvo predstavilo nacrt<small>ministar Branko Bačić</small></td><td class="r">31.7.2026.</td></tr>
<tr><td>Javno savetovanje<small>e-Savjetovanja</small></td><td class="r">3.8.–2.9.</td></tr>
</table>
<div class="note" style="margin-top:30px">Detalji se još mogu menjati pre usvajanja. Stanje na dan 10.11.2026: zakon nije na snazi.</div>""",
    "MPGI, 31.7.2026; ZGRADOnačelnik, 3.8.2026; najam.hr, 10.11.2026.")

add("""<div class="kick">Kirija</div><h2>Koliko sme<br>da poskupi?</h2>
<div class="steps">
<div class="st"><span class="n">1×</span><div>Najviše <b>jednom godišnje</b> dok traje ugovor.</div></div>
<div class="st"><span class="n">30</span><div>Dana ranije podstanar mora da dobije <b>najavu</b> nove cene.</div></div>
<div class="st"><span class="n">%</span><div>Ne više od <span class="gold">rasta cena stanova</span> u prethodnoj godini (DZS). Ugovor koji dozvoljava više je u tom delu <b>ništavan</b>.</div></div>
</div>
<div class="note">Početna kirija nije ograničena: vlasnik je slobodno određuje.</div>""",
    MPGI + " Početna kirija: ZGRADOnačelnik, 31.7.2026.")

add("""<div class="kick">Primer: da je pravilo važilo za 2025.</div><h2>Plafon bi bio<br><span class="gold">14,1%</span></h2>
<div class="lead" style="margin-top:20px">Toliko su u proseku porasle cene stambenih objekata u Hrvatskoj 2025. u odnosu na 2024.</div>
<div class="cc"><div class="card"><b>600 €</b>kirija danas</div>
<div class="card"><b>najviše 684,60 €</b>posle godinu dana (+84,60 €)</div></div>""",
    "DZS (preko RBA Research, 8.4.2026 i Lider/Hina, 3.4.2026). Obračun STANOLOGIJA: 600 × 14,1% = 84,60 €. Ilustracija; zakon još ne važi.",
    alt="Slajd 4/8, STANOLOGIJA. Primer: da je pravilo važilo za 2025, plafon povećanja kirije bio bi 14,1 posto, koliko su u proseku porasle cene stambenih objekata u Hrvatskoj 2025. u odnosu na 2024. prema DZS. Kartica 1: kirija danas 600 evra. Kartica 2: najviše 684,60 evra posle godinu dana, odnosno plus 84,60 evra. Obračun STANOLOGIJA: 600 puta 14,1 posto. Ilustracija, zakon još ne važi. Izvor: DZS preko RBA Research (8.4.2026) i Lider/Hina (3.4.2026).")

add("""<div class="kick">Otkaz</div><h2>Koliko vremena<br>imaš da se iseliš?</h2>
<table class="tbl">
<tr><td>Podstanar otkazuje<small>bez navođenja razloga</small></td><td class="r">60 dana</td></tr>
<tr><td>Vlasnik otkazuje bez tvoje krivice<small>zakonski minimum</small></td><td class="r">6 mes.</td></tr>
<tr><td>Ako najam traje duže od 5 godina</td><td class="r">1 godina</td></tr>
<tr><td>Ako u stanu živi dete</td><td class="r">+6 mes.</td></tr>
<tr><td>Najkraće što se sme ugovoriti</td><td class="r">3 mes.</td></tr>
</table>""",
    MPGI)

add("""<div class="kick">Ako podstanar krši ugovor</div><h2>Prvo opomena,<br>pa otkaz</h2>
<div class="steps">
<div class="st"><span class="n">1</span><div>Vlasnik šalje <b>pisanu opomenu</b> (neplaćena kirija ili režije, šteta, kršenje kućnog reda).</div></div>
<div class="st"><span class="n">2</span><div>Podstanar ima <span class="gold">15 dana</span> da ispravi propust.</div></div>
<div class="st"><span class="n">3</span><div>Ako ne ispravi: rok za iseljenje je još <span class="gold">najmanje 30 dana</span>.</div></div>
</div>""",
    MPGI + " Razlozi: ZGRADOnačelnik, 31.7.2026.")

add("""<div class="kick">Novac i papiri</div><h2>Šta još<br>donosi nacrt</h2>
<div class="steps">
<div class="st"><span class="n">1</span><div>Depozit: <span class="gold">jedna mesečna kirija</span>, ako ugovorom nije drugačije.</div></div>
<div class="st"><span class="n">2</span><div>Svaki novi ugovor <b>overava javni beležnik</b> (solemnizacija), pa se iseljenje rešava bez dugog spora.</div></div>
<div class="st"><span class="n">3</span><div>Vlasnik sme da pregleda stan <b>2× godišnje</b>, uz najavu.</div></div>
<div class="st"><span class="n">4</span><div>Garancija za vlasnika preko državne agencije: članarina do <span class="gold">2% godišnje kirije</span> (ministar: oko 40–150 €).</div></div>
</div>""",
    MPGI + " Agencija za osiguranje radničkih tražbina; podstanar daje bianco zadužnicu do 10.000 €.")

add("""<div style="margin-top:160px"><div class="kick">Tvoj red</div>
<h1 style="font-size:92px">Pošalji<br><span class="gold">podstanaru</span></h1>
<div class="lead">Pošalji ovo nekome ko živi pod kiriju u Hrvatskoj, ili ko izdaje stan. U komentaru: da li i Srbiji treba ovakav zakon?</div>
<div class="tag">Pošalji · Sačuvaj</div></div>""")

d.render(HERE, extra_css=EXTRA)
contact_sheet(HERE, 8, "/tmp/claude-0/-home-claude-stanologija-slike/0b39cd3a-8722-5894-a9ac-1721d0555a94/scratchpad/sheet.jpg")
