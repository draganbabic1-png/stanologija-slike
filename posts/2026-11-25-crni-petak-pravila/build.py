import sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "tools"))
from stanologija import Deck, contact_sheet

EXTRA = """
.li{font-size:33px;line-height:1.4;padding:16px 0 16px 54px;border-bottom:1px solid #2A4562;position:relative}
.li:before{content:"•";position:absolute;left:10px;top:8px;font-family:Oswald;font-weight:700;font-size:48px;color:var(--gold)}
.li b{color:var(--gold)}
.tl{margin-top:56px}
.st{display:flex;align-items:center;margin-bottom:30px}
.st .d{font-family:Oswald;font-weight:700;font-size:78px;color:var(--gold);width:290px;flex-shrink:0;line-height:1;white-space:nowrap}
.st .t{font-size:33px;line-height:1.4;border-left:4px solid #2A4562;padding-left:30px}
.x{color:#E07A5F}
"""

N = 8
d = Deck(n=N)
add = d.add
ZOT = "Izvor: Zakon o trgovini, čl. 37 (izmene, „Sl. glasnik RS” 35/2026, primena od 1.5.2026); čl. 67."
ZZP = "Izvor: Zakon o zaštiti potrošača („Sl. glasnik RS” 35/2026)"

# 1 HOOK
add("""<div style="margin-top:110px"><div class="kick">Srbija · Crni petak 27.11.</div>
<h1>Kupuješ frižider<br>na <span class="gold">Crni petak?</span></h1>
<div class="lead">Bela tehnika, nameštaj, TV: <span class="gold">4 pravila iz zakona</span> koja trgovac mora da poštuje. I jedno što ne mora.</div>
<div class="tag">Prevuci →</div></div>""")

# 2 PRETHODNA CENA
add("""<div class="kick">Pravilo 1 · Lažni popust</div><h2>„Stara cena” =<br><span class="gold">najniža u 30 dana</span></h2>
<div class="card"><b>30 dana</b>Prethodna cena je najniža cena po kojoj je trgovac nudio robu u 30 dana pre početka sniženja.</div>
<div class="li">Moraju jasno da istaknu <b>i sniženu i prethodnu cenu</b>.</div>
<div class="li">Proizvod u ponudi kraće od 30 dana: najniža cena u bar <b>15 dana</b>.</div>""",
    ZOT)

# 3 IZUZECI + KAZNA
add("""<div class="kick">Pravilo 1 · Sitna slova</div><h2>Gde pravilo<br>ne važi</h2>
<div class="li">Akcija <b>do 3 dana</b>: dovoljno je da istaknu samo procenat popusta.</div>
<div class="li">Lako kvarljiva roba i roba kratkog roka trajanja.</div>
<div class="card"><b>100.000 din</b>kazna za pravno lice koje prodaje „na popust” suprotno ovim pravilima.</div>
<div class="note"><span class="gold">Savet:</span> uslikaj cenu proizvoda danas. Ako se u petak pojavi „stara cena” viša od one koju si video, imaš dokaz.</div>""",
    ZOT + " Savet je preporuka STANOLOGIJA.")

# 4 ONLINE
add("""<div class="kick">Pravilo 2 · Kupovina preko sajta</div><h2><span class="gold">14 dana</span> da<br>se predomisliš</h2>
<div class="li">Odustaješ <b>bez navođenja razloga</b>, u roku od 14 dana od isporuke.</div>
<div class="li">Trgovac vraća novac (cenu i dostavu) najkasnije <b>14 dana</b> od tvog obrasca za odustanak.</div>
<div class="li">Robu vraćaš u 14 dana; trošak povrata je tvoj, ako ti je to rečeno pre kupovine.</div>
<div class="li"><span class="x">Ne važi</span> za robu po meri, npr. nameštaj rađen po tvojim dimenzijama.</div>""",
    ZZP + ", čl. 29, 35, 36; izuzeci i početak roka: Paragraf/Bizportal, 16.11.2026.")

# 5 PRODAVNICA
add("""<div class="kick">Ono što trgovac ne mora</div><h2>U radnji <span class="x">nema</span><br>„predomislio sam se”</h2>
<div class="card"><b>0 dana</b>zakonskog roka za vraćanje <i>ispravne</i> robe kupljene u prodavnici.</div>
<div class="note" style="font-size:34px;color:var(--cream)">Trgovac nije automatski dužan da je primi nazad i vrati novac. Zavisi od njegove poslovne politike.</div>
<div class="note"><span class="gold">Pre plaćanja pitaj:</span> da li mogu da vratim ili zamenim i do kada? Traži da piše na računu.</div>""",
    "Izvor: Paragraf/Bizportal, 16.11.2026; 14 dana važi samo za kupovinu na daljinu i van poslovnih prostorija (ZZP, čl. 29).")

# 6 REKLAMACIJA
add("""<div class="kick">Pravilo 3 · Kvar posle kupovine</div><h2><span class="gold">2 godine</span><br>odgovara trgovac</h2>
<div class="li">Trgovac odgovara za nesaobraznost koja se pojavi <b>u 2 godine</b> od isporuke. Popust to ne menja.</div>
<div class="li">Kvar u <b>prvih godinu dana</b>: smatra se da je postojao pri isporuci. Suprotno dokazuje trgovac.</div>
<div class="li">Javi trgovcu u roku od <b>2 meseca</b> od kad si primetio kvar.</div>""",
    ZZP + ", čl. 59.")

# 7 ROKOVI
add("""<div class="kick">Pravilo 4 · Rokovi za reklamaciju</div><h2>Trgovac ima<br>tačne rokove</h2>
<div class="tl">
<div class="st"><div class="d">8 dana</div><div class="t">da ti pisano ili elektronski odgovori na reklamaciju</div></div>
<div class="st"><div class="d">15 dana</div><div class="t">da reši reklamaciju, od dana kad si je podneo</div></div>
<div class="st"><div class="d">30 dana</div><div class="t">za <span class="gold">tehničku robu i nameštaj</span>: frižider, veš-mašina, šporet, kauč</div></div>
</div>""",
    ZZP + ", čl. 63; „tehnička roba” = aparati za domaćinstvo i sl. (čl. 5).")

# 8 CTA
add("""<div style="margin-top:120px"><div class="kick">Pre nego što klikneš „kupi”</div>
<h1 style="font-size:96px">Popust je<br>popust tek <span class="gold">uz dokaz</span></h1>
<div class="lead">Pošalji ovo nekome ko čeka Crni petak za novu veš-mašinu ili kauč.</div>
<div class="note">Pravila važe za Srbiju. Hrvatska i Slovenija imaju slično EU pravilo o 30 dana.</div>
<div class="tag">Prati @stanologija · sutra: kuriozitet iz gradnje</div></div>""")

d.render(HERE, extra_css=EXTRA)
contact_sheet(HERE, N, "/tmp/claude-0/-home-claude-stanologija-slike/73a40f82-7297-59f2-9643-f26a37cb3a1c/scratchpad/sheet.jpg")
