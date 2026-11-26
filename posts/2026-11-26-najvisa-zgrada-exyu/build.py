import sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "tools"))
from stanologija import Deck, contact_sheet, bars

EXTRA = """
.duo{display:flex;gap:28px;margin-top:50px}
.duo .c{flex:1;background:#16304A;border-top:8px solid var(--gold);padding:36px 34px}
.duo .c .n{font-family:Oswald;font-weight:600;font-size:40px;text-transform:uppercase;line-height:1.1}
.duo .c .g{font-family:Oswald;font-weight:700;font-size:120px;color:var(--gold);line-height:1.05;margin-top:14px}
.duo .c .t{font-size:30px;line-height:1.45;margin-top:10px;color:var(--cream)}
.tl{margin-top:44px}
.st{display:flex;align-items:center;margin-bottom:22px}
.st .d{font-family:Oswald;font-weight:700;font-size:58px;color:var(--gold);width:170px;flex-shrink:0;line-height:1}
.st .t{font-size:31px;line-height:1.35;border-left:4px solid #2A4562;padding-left:28px}
.st .t b{font-family:Oswald;font-weight:600;font-size:38px}
.lab{width:300px !important;font-size:32px !important}
.li{font-size:33px;line-height:1.4;padding:16px 0 16px 54px;border-bottom:1px solid #2A4562;position:relative}
.li:before{content:"•";position:absolute;left:10px;top:8px;font-family:Oswald;font-weight:700;font-size:48px;color:var(--gold)}
.li b{color:var(--gold)}
"""

N = 8
d = Deck(n=N)
add = d.add
WS = "Izvor: Wikipedia, List of tallest structures in Serbia (pristup 26.11.2026)."
WB = "Izvor: Wikipedia, List of tallest buildings in Bosnia and Herzegovina (pristup 26.11.2026)."
CT = "CTBUH Skyscraper Center"

# 1 HOOK
add("""<div style="margin-top:120px"><div class="kick">Kuriozitet · ex-YU</div>
<h1>Najviša zgrada<br><span class="gold">bivše Jugoslavije?</span></h1>
<div class="lead">Beograd kaže Kula. Sarajevo kaže Avaz. <span class="gold">U pravu su i jedni i drugi</span>, zavisi kako meriš.</div>
<div class="tag">Prevuci →</div></div>""")

# 2 DVA PRETENDENTA
add("""<div class="kick">Dva pretendenta</div><h2>168 m protiv<br><span class="gold">172 m</span></h2>
<div class="duo">
<div class="c"><div class="n">Kula Beograd</div><div class="g">168 m</div><div class="t">42 sprata<br>fasada završena 2022.<br>Beograd na vodi</div></div>
<div class="c"><div class="n">Avaz Twist Tower</div><div class="g">172 m</div><div class="t">39 spratova<br>završena 2008.<br>Sarajevo</div></div>
</div>
<div class="note">Na papiru je Avaz viši. Ali pogledaj šta se tu računa →</div>""",
    "Izvor: " + CT + " (Avaz: 172 m do vrha, 39 spratova, 2008; Kula: 168 m); Wikipedia, Belgrade Tower (42 sprata, 2022).",
    alt="Dve kartice jedna pored druge. Levo: Kula Beograd, 168 metara, 42 sprata, fasada završena 2022, Beograd na vodi. Desno: Avaz Twist Tower, 172 metra, 39 spratova, završena 2008, Sarajevo. Ispod: na papiru je Avaz viši, ali pogledaj šta se tu računa. Izvor: CTBUH Skyscraper Center i Wikipedia.")

# 3 KVAKA
add("""<div class="kick">Kvaka je u anteni</div><h2>Kako se meri<br><span class="gold">neboder</span></h2>
<div class="card"><b>142 m</b>Avaz bez antene: arhitektonska visina. Toliko ga vodi CTBUH, svetski registar nebodera.</div>
<div class="li">Antena se po CTBUH pravilima <b>ne računa</b>. Po tom merilu Kula sa <b>168 m</b> je viša za 26 m.</div>
<div class="li">Računaš li antenu, Avaz ima <b>172 m</b> i viši je od Kule za 4 m.</div>""",
    "Izvor: " + CT + ": Avaz Twist Tower, arhitektonska visina 142 m, do vrha 172 m; Kula Beograd 168 m. Razlike: obračun STANOLOGIJA (168−142; 172−168).")

# 4 PO ZEMLJAMA
R = [("Srbija", 168), ("BiH", 142), ("Hrvatska", 135), ("S. Makedonija", 130), ("Slovenija", 89)]
add(f"""<div class="kick">Najviša zgrada po zemlji</div><h2>Ko ima<br><span class="gold">najviši toranj</span></h2>
<div style="margin-top:56px">{bars(R, 168*560/430, lambda v: f"{v} m", hi=lambda v: v == 168)}</div>
<div class="note" style="font-size:27px">Kula Beograd · Avaz Twist Tower, Sarajevo · Dalmatia Tower, Split · Cevahir, Skoplje · Kristalna palata, Ljubljana. Crna Gora nema zgradu na ovoj listi.</div>""",
    "Izvor: Wikipedia, List of tallest buildings in the Balkans (arhitektonska visina, bez antena; pristup 26.11.2026); BiH: " + CT + ".",
    alt="Stubičasti grafikon najviših zgrada po zemlji, arhitektonska visina bez antena. Srbija, Kula Beograd: 168 m (najviša). BiH, Avaz Twist Tower u Sarajevu: 142 m. Hrvatska, Dalmatia Tower u Splitu: 135 m. Severna Makedonija, Cevahir u Skoplju: 130 m. Slovenija, Kristalna palata u Ljubljani: 89 m. Crna Gora nema zgradu na ovoj listi. Izvor: Wikipedia lista najviših zgrada Balkana i CTBUH.")

# 5 SRBIJA REKORDI
add("""<div class="kick">Srbija · smena rekorda</div><h2>Rekord koji je<br><span class="gold">trajao 42 godine</span></h2>
<div class="tl">
<div class="st"><div class="d">1939</div><div class="t"><b>Palata Albanija · 58 m</b><br>prva visoka zgrada na Balkanu</div></div>
<div class="st"><div class="d">1964</div><div class="t"><b>Kula Ušće · 115 m</b><br>danas, posle rekonstrukcije 2005.</div></div>
<div class="st"><div class="d">1979</div><div class="t"><b>Zapadna kapija (Geneks) · 117 m</b><br><span class="gold">najviša u Srbiji do 2021.</span></div></div>
<div class="st"><div class="d">2021</div><div class="t"><b>West 65 · 155 m</b></div></div>
<div class="st"><div class="d">2022</div><div class="t"><b>Kula Beograd · 168 m</b></div></div>
</div>""",
    WS + " Visine do krova; Zapadna kapija sa restoranom 140 m.",
    alt="Vremenska linija najviših zgrada u Srbiji. 1939: Palata Albanija, 58 m, prva visoka zgrada na Balkanu. 1964: Kula Ušće, 115 m (današnja visina, posle rekonstrukcije 2005). 1979: Zapadna kapija Beograda (Geneks), 117 m, najviša u Srbiji do 2021, rekord 42 godine. 2021: West 65, 155 m. 2022: Kula Beograd, 168 m. Izvor: Wikipedia.")

# 6 BIH REKORDI
add("""<div class="kick">BiH · smena rekorda</div><h2>Deset godina<br>vodila je <span class="gold">Zenica</span></h2>
<div class="tl">
<div class="st"><div class="d">1974</div><div class="t"><b>Zgrada prijateljstva Grčka–BiH · 83 m</b><br>Sarajevo</div></div>
<div class="st"><div class="d">1976</div><div class="t"><b>Lamela · 102 m</b><br><span class="gold">Zenica, najviša u BiH do 1986.</span></div></div>
<div class="st"><div class="d">1986</div><div class="t"><b>UNITIC · 111 m</b><br>Sarajevo, dve kule</div></div>
<div class="st"><div class="d">2006</div><div class="t"><b>Bosmal City Center · 118 m</b></div></div>
<div class="st"><div class="d">2008</div><div class="t"><b>Avaz Twist Tower · 142 / 172 m</b></div></div>
</div>""",
    WB + " Avaz: " + CT + ".",
    alt="Vremenska linija najviših zgrada u Bosni i Hercegovini. 1974: Zgrada prijateljstva Grčka–BiH u Sarajevu, 83 m. 1976: Lamela u Zenici, 102 m, najviša u BiH do 1986. 1986: UNITIC kule u Sarajevu, 111 m. 2006: Bosmal City Center, 118 m. 2008: Avaz Twist Tower, 142 m bez antene, 172 m sa antenom. Izvor: Wikipedia i CTBUH.")

# 7 STA DALJE
add("""<div class="kick">A šta dalje?</div><h2>Ni Kula nije<br><span class="gold">kraj priče</span></h2>
<div class="card"><b>202 m</b>Sky Fort u Sofiji (2023) prestigao je Kulu kao najvišu zgradu Balkana van Turske.</div>
<div class="li">U Sarajevu je 2020. odobren <b>Avaz R Tower</b>: planirano <b>181 m</b> i 40 spratova.</div>
<div class="li">Gradnja još nije počela, pa je to za sada <b>samo projekat</b>.</div>""",
    "Izvor: Wikipedia, Belgrade Tower (Sky Fort, Sofija); List of tallest buildings in Bosnia and Herzegovina (Avaz R Tower: odobren januara 2020, bez početka gradnje); pristup 26.11.2026.")

# 8 CTA
add("""<div style="margin-top:120px"><div class="kick">Spor rešen. Skoro.</div>
<h1 style="font-size:96px">Bez antene Kula,<br><span class="gold">sa antenom Avaz</span></h1>
<div class="lead">Pošalji ovo drugaru iz Sarajeva ili Beograda koji tvrdi da je „njihova” najviša.</div>
<div class="tag">Prati @stanologija · sutra: nove brojke sa tržišta stanova</div></div>""")

d.render(HERE, extra_css=EXTRA)
contact_sheet(HERE, N, "/tmp/claude-0/-home-claude-stanologija-slike/2ab3861b-c6c9-5144-80b4-d3084501f2ab/scratchpad/sheet.jpg")
