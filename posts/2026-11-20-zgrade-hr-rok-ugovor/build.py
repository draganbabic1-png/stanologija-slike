import sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "tools"))
from stanologija import Deck, contact_sheet

# Izvori:
# - MPGI, "Zakon o upravljanju i održavanju zgrada - Vodič za upravitelje" (mpgi.gov.hr): rok 1.1.2027, natpolovična većina, 15 dana, prinudni upravitelj (gradonačelnik, 6 meseci, javni poziv), godišnji program do 15.11.
# - ZUOZ NN 152/2024 (na snazi od 1.1.2025), čl. 1, 4, 61 (sažetak: Unitify, provereno 27.10.2026).
# - Čl. 29 ZUOZ, minimalna pričuva 0,54% etalonske cene godišnje i 5x pričuva bez godišnjeg programa (citat zakona preneli Index.hr i DuList, 30.3.2025); etalon 796,34 €/m² za primenu u drugim propisima (MPGI preko Index.hr; ZGRADOnačelnik 25.7.2025: ostaje).
# - HRT Vijesti 15.11.2026 (T. Jukić, MPGI; nema službenih podataka o broju potpisanih ugovora); tportal 16.11.2026.
# - Procena OIB: ZGRADOnačelnik / T. Bašić za N1, preneo tportal 20.5.2026.

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

SRC_MIN = "MPGI, Vodič za upravitelje (ZUOZ, NN 152/2024)"
d = Deck(n=9)
add = d.add

add("""<div style="margin-top:120px"><div class="kick">Hrvatska · zgrade · rok 31.12.2026.</div>
<h1>Tvojoj zgradi<br>ističe <span class="gold">ugovor</span></h1>
<div class="lead">Za <span class="gold">41 dan</span> stari ugovori o zgradi prestaju da važe. Ako komšije ne potpišu novi, pričuva može da skoči <span class="gold">5 puta</span>.</div>
<div class="tag">Prevuci →</div></div>""",
    "Rok: MPGI, Vodič za upravitelje; HRT, 15.11.2026. 41 dan = od 20.11. do 31.12.2026.")

add("""<div class="kick">Šta se menja</div><h2>Novi zakon,<br>novi ugovori</h2>
<table class="tbl">
<tr><td>Zakon o upravljanju i održavanju zgrada<small>NN 152/2024</small></td><td class="r">1.1.2025.</td></tr>
<tr><td>Stari ugovori važe<small>najduže 2 godine od stupanja na snagu</small></td><td class="r">31.12.2026.</td></tr>
<tr><td>Novi ugovori obavezni<small>međuvlasnički + ugovor s upraviteljem</small></td><td class="r">1.1.2027.</td></tr>
</table>
<div class="note" style="margin-top:30px">Međuvlasnički ugovor = pravila zgrade: ko predstavlja suvlasnike, kako se troši pričuva, kako se odlučuje.</div>""",
    SRC_MIN + "; ZUOZ čl. 61 (sažetak Unitify, 27.10.2026).")

add("""<div class="kick">Na koga se odnosi</div><h2>Da li je i<br>tvoja zgrada?</h2>
<table class="tbl">
<tr><td>Stambena zgrada</td><td class="r">4+ stana</td></tr>
<tr><td>Stambeno-poslovna</td><td class="r">3+ stana i lokal</td></tr>
<tr><td>Poslovne zgrade i blokovske garaže</td><td class="r">sve</td></tr>
</table>
<div class="note" style="margin-top:30px">Kuće i manje zgrade nisu obuhvaćene ovim rokom.</div>""",
    "ZUOZ NN 152/2024, čl. 1 i čl. 4 (sažetak: Unitify, provereno 27.10.2026).")

add("""<div class="kick">Kako se potpisuje</div><h2>Tri koraka<br>do novog ugovora</h2>
<div class="steps">
<div class="st"><span class="n">1</span><div>Suvlasnici potpišu <span class="gold">međuvlasnički ugovor</span>. Važi kad potpiše <b>više od polovine</b> (po suvlasničkim udelima, ne po glavi).</div></div>
<div class="st"><span class="n">2</span><div>Predstavnik suvlasnika ga u roku od <b>15 dana</b> dostavi upravitelju.</div></div>
<div class="st"><span class="n">3</span><div>Potpisuje se novi <span class="gold">ugovor o upravljanju</span> sa izabranim upraviteljem.</div></div>
</div>""",
    SRC_MIN + ". Većina po udelima: ZUOZ čl. 4 (sažetak Unitify).")

add("""<div class="kick">Pričuva = fond za održavanje</div><h2>Koliki je<br>zakonski minimum?</h2>
<div class="big" style="margin-top:36px;font-size:170px">0,36 €</div>
<div class="lead" style="margin-top:10px">po m² mesečno. To je <span class="gold">0,54%</span> etalonske cene gradnje (796,34 €/m²) godišnje.</div>
<div class="card"><b>≈ 21,50 €</b>mesečno za stan od 60 m² na minimumu.</div>""",
    "ZUOZ čl. 29 (citat preneli Index.hr i DuList, 30.3.2025); etalon 796,34 €/m²: MPGI preko Index.hr. Obračun STANOLOGIJA: 796,34 × 0,54% ÷ 12 = 0,358 €/m²; × 60 m² ≈ 21,50 €.")

add("""<div class="kick">Kazna za neslogu</div><h2>Nema godišnjeg plana?<br>Pričuva × 5</h2>
<div class="cc"><div class="card"><b>≈ 21,50 €</b>stan 60 m², pričuva na minimumu</div>
<div class="card"><b>≈ 107,50 €</b>isti stan, ako zgrada ne usvoji godišnji program održavanja</div></div>
<div class="note" style="margin-top:30px">Zakon: plaća se <b>peterostruki</b> iznos zadnje usvojene pričuve, dok se program ne usvoji. Bez međuvlasničkog ugovora nema ko da ga usvoji (MPGI, HRT 15.11.2026).</div>""",
    "ZUOZ čl. 29 (preneli Index.hr/DuList, 30.3.2025); T. Jukić, MPGI, HRT 15.11.2026. Obračun STANOLOGIJA: 21,50 € × 5. Ako je vaša pričuva viša od minimuma, i ×5 je viši.")

add("""<div class="kick">Ako niko ne potpiše</div><h2>Prinudni<br>upravitelj</h2>
<div class="lead" style="margin-top:30px">Gradonačelnik (načelnik opštine) imenuje <span class="gold">prinudnog upravitelja</span> u roku od 6 meseci, preko javnog poziva. On upravlja zgradom i novcem dok suvlasnici ne izaberu svog.</div>
<div class="card"><b>0</b>službenih podataka o tome koliko je zgrada već potpisalo nove ugovore (HRT, 15.11.2026).</div>""",
    SRC_MIN + "; HRT, 15.11.2026; tportal, 16.11.2026 (nije automatski od 1.1.).")

add("""<div class="kick">Uradi ove nedelje</div><h2>Ček-lista<br>za tvoju zgradu</h2>
<div class="steps">
<div class="st"><span class="n">✓</span><div>Pitaj predstavnika suvlasnika: <b>da li je novi međuvlasnički ugovor potpisan?</b></div></div>
<div class="st"><span class="n">✓</span><div>Proveri da li zgrada ima <span class="gold">OIB</span>: bez njega nema prijave na javne pozive.</div></div>
<div class="st"><span class="n">✓</span><div>Traži <b>godišnji program održavanja</b>: upravitelj ga predlaže do 15. novembra.</div></div>
</div>
<div class="note">Procena: ~17.000 zgrada ima OIB, od oko 60.000 (ZGRADOnačelnik, maj 2026).</div>""",
    SRC_MIN + "; procena OIB: T. Bašić (ZGRADOnačelnik) za N1, preneo tportal 20.5.2026.")

add("""<div style="margin-top:160px"><div class="kick">Tvoj red</div>
<h1 style="font-size:92px">Pošalji<br><span class="gold">komšiji</span><br>iz zgrade</h1>
<div class="lead">Pošalji ovo nekome ko ima stan u Hrvatskoj, pre nego što mu pričuva skoči. U komentaru: da li je vaša zgrada već potpisala?</div>
<div class="tag">Pošalji · Sačuvaj</div></div>""")

d.render(HERE, extra_css=EXTRA)
contact_sheet(HERE, 9, "/tmp/claude-0/-home-claude-stanologija-slike/b1d62a6c-ffdd-5a9c-b43e-3097b66b7ac5/scratchpad/sheet.jpg")
