import sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "tools"))
from stanologija import Deck, contact_sheet

EXTRA = """
.tb{width:100%;border-collapse:collapse;margin-top:44px;font-size:33px}
.tb th{font-family:Oswald;font-weight:500;color:var(--gold);text-align:left;padding:12px 8px;font-size:28px;letter-spacing:1px;text-transform:uppercase}
.tb td{padding:22px 8px;border-bottom:1px solid #2A4562;vertical-align:top}
.tb td b{font-family:Oswald;font-weight:600;font-size:40px}
.tb td.r{text-align:right;font-family:Oswald;font-weight:600;font-size:42px;white-space:nowrap}
.li{font-size:33px;line-height:1.4;padding:16px 0 16px 54px;border-bottom:1px solid #2A4562;position:relative}
.li:before{content:"•";position:absolute;left:10px;top:8px;font-family:Oswald;font-weight:700;font-size:48px;color:var(--gold)}
.li b{color:var(--gold)}
.duo{display:flex;gap:28px;margin-top:46px}
.duo .c{flex:1;background:#16304A;border-top:8px solid #3A5470;padding:34px 32px}
.duo .c.h{border-top-color:var(--gold)}
.duo .c .n{font-family:Oswald;font-weight:600;font-size:34px;text-transform:uppercase;line-height:1.15}
.duo .c .g{font-family:Oswald;font-weight:700;font-size:92px;color:var(--gold);line-height:1.05;margin-top:12px}
.duo .c .t{font-size:28px;line-height:1.45;margin-top:8px}
"""

N = 9
d = Deck(n=N)
add = d.add
OD = "Odluka o opštim pravilima kućnog reda u stambenim i stambeno-poslovnim zgradama na teritoriji grada Beograda („Sl. list grada Beograda”, br. 101/2019)"
UR = "Uredba o indikatorima buke, graničnim vrednostima… („Sl. glasnik RS”, br. 75/2010), Prilog 2"

# 1 HOOK
add("""<div style="margin-top:110px"><div class="kick">Beograd · kućni red</div>
<h1>Komšija buši<br><span class="gold">u nedelju u 9?</span></h1>
<div class="lead">U Beogradu je nedeljom tišina do <span class="gold">10.00</span>. Kazna za stanara: <span class="gold">5.000 dinara</span>.</div>
<div class="tag">Prevuci →</div></div>""",
    "Izvor: " + OD + ", čl. 5, 12 i 39.")

# 2 PROBLEM / MIT
add("""<div class="kick">Najčešća zabluda</div><h2>Tišina ne počinje<br><span class="gold">tek u 22h</span></h2>
<div class="duo">
<div class="c"><div class="n">Staro pravilo<br>(do 2019.)</div><div class="g">13–17</div><div class="t">i od 22 do 6 časova</div></div>
<div class="c h"><div class="n">Važi sada<br>(radni dan)</div><div class="g">16–18</div><div class="t">i od 22 do 7 časova</div></div>
</div>
<div class="card" style="font-size:33px">Ako pamtiš „posle ručka od 13 do 17”, to je kućni red iz 1983. (sa izmenama). Novi važi od kraja 2019.</div>""",
    "Izvor: " + OD + ", čl. 5 (čl. 42 ukida Odluku o kućnom redu, „Sl. list grada Beograda” 11/83). Staro vreme odmora: Kurir, 14.11.2019.",
    alt="Dve kartice: najčešća zabluda je da tišina počinje tek u 22 časa. Staro pravilo u Beogradu (do 2019.): odmor od 13 do 17 i od 22 do 6 časova. Pravilo koje važi sada, radnim danom: od 16 do 18 i od 22 do 7 časova. Ako pamtiš „posle ručka od 13 do 17”, to je kućni red iz 1983, a novi važi od kraja 2019. Izvor: Odluka o opštim pravilima kućnog reda grada Beograda, Sl. list 101/2019, čl. 5; Kurir 14.11.2019.")

# 3 RASPORED
add("""<div class="kick">Vreme odmora · Beograd</div><h2>Kad mora<br><span class="gold">da bude tiho</span></h2>
<table class="tb"><tr><th>Dan</th><th>Ujutru do</th><th>Popodne</th><th>Uveče od</th></tr>
<tr><td><b>Pon–pet</b></td><td class="r">7.00</td><td class="r">16–18</td><td class="r">22.00</td></tr>
<tr><td><b>Subota</b></td><td class="r gold">8.00</td><td class="r">14–18</td><td class="r">22.00</td></tr>
<tr><td><b>Nedelja</b></td><td class="r gold">10.00</td><td class="r">14–18</td><td class="r">22.00</td></tr>
</table>
<div class="note">Isto važi i za kosačice i motorne testere oko zgrade. Leto i zima se ne razlikuju.</div>""",
    "Izvor: " + OD + ", čl. 5 st. 1 i 2. Tabela: prikaz STANOLOGIJA prema tekstu člana 5.",
    alt="Tabela vremena odmora u stambenim zgradama u Beogradu. Ponedeljak do petak: tišina ujutru do 7.00, popodne od 16 do 18, uveče od 22.00. Subota: ujutru do 8.00, popodne od 14 do 18, uveče od 22.00. Nedelja: ujutru do 10.00, popodne od 14 do 18, uveče od 22.00. Isto važi i za kosačice i motorne testere oko zgrade; leto i zima se ne razlikuju. Izvor: Odluka o opštim pravilima kućnog reda grada Beograda, Sl. list 101/2019, član 5.")

# 4 RADOVI
add("""<div class="kick">Renoviraš stan?</div><h2>Bušilica ima<br><span class="gold">svoja pravila</span></h2>
<div class="li">Pre radova obavesti <b>upravnika zgrade</b> (i pokaži odobrenje, ako ga zakon traži).</div>
<div class="li">Na vidnom mestu okači obaveštenje: <b>dan početka, vrsta i trajanje</b> radova.</div>
<div class="li">Radovi <b>ne smeju u vreme odmora</b>. Izuzetak su samo hitne intervencije (npr. pukla cev).</div>
<div class="li">Bušenje u nedelju u 9 = <b>prekršaj</b>, i kad je „samo jedna rupa”.</div>""",
    "Izvor: " + OD + ", čl. 12 st. 2 i 4; kazna čl. 39 tač. 9. Primer „pukla cev”: tumačenje STANOLOGIJA.")

# 5 SLAVLJE
add("""<div class="kick">Slava, rođendan, žurka</div><h2>Slavlje je dozvoljeno,<br><span class="gold">ali uz najavu</span></h2>
<div class="card"><b>2 dana ranije</b>okači obaveštenje komšijama da će biti okupljanja.</div>
<div class="card"><b>od 1.00</b>posle ponoći mora biti mir i tišina, i uz najavu.</div>
<div class="note">Bez najave važe obična pravila: tišina od 22.00.</div>""",
    "Izvor: " + OD + ", čl. 5 st. 3 i čl. 5 st. 1. Napomena „bez najave”: tumačenje STANOLOGIJA.")

# 6 DECIBELI
add("""<div class="kick">Koliko je „glasno”?</div><h2>Tvoja spavaća soba<br><span class="gold">ima limit</span></h2>
<div class="duo">
<div class="c"><div class="n">Dan i veče<br>6–22 h</div><div class="g">35 dB</div><div class="t">spavaća i dnevna soba, zatvoreni prozori</div></div>
<div class="c h"><div class="n">Noć<br>22–6 h</div><div class="g">30 dB</div><div class="t">spavaća i dnevna soba, zatvoreni prozori</div></div>
</div>
<div class="note">Kućni red upućuje na ove granice. Napolju, u čisto stambenoj zoni: 55 dB danju, 45 dB noću. Važe za ukupnu buku, ne meri se „na uvo”.</div>""",
    "Izvor: " + UR + ", Tabele 1 i 2; čl. 5 (dan 6–18, veče 18–22, noć 22–6). " + "Kućni red Beograda čl. 6 st. 2 upućuje na „graničnu vrednost indikatora buke, određenu propisom”.",
    alt="Dve kartice sa zakonskim granicama buke u stanu u Srbiji. Dan i veče, od 6 do 22 časa: 35 decibela u spavaćoj i dnevnoj sobi, pri zatvorenim prozorima. Noć, od 22 do 6 časova: 30 decibela. Kućni red Beograda upućuje na ove granice. Napolju, u čisto stambenoj zoni: 55 dB danju i 45 dB noću. Vrednosti važe za ukupnu buku i utvrđuju se merenjem. Izvor: Uredba o indikatorima buke, graničnim vrednostima..., Sl. glasnik RS 75/2010, Prilog 2.")

# 7 KAZNE
add("""<div class="kick">Koliko košta buka</div><h2>Kazne po<br><span class="gold">kućnom redu</span></h2>
<table class="tb"><tr><th>Ko</th><th style="text-align:right">Fiksna kazna</th></tr>
<tr><td><b>Stanar (fizičko lice)</b></td><td class="r gold">5.000 din</td></tr>
<tr><td><b>Preduzetnik</b></td><td class="r">25.000 din</td></tr>
<tr><td><b>Firma kao stanar</b></td><td class="r">50.000 din</td></tr>
<tr><td><b>Upravnik iz zgrade</b></td><td class="r">10.000 din</td></tr>
<tr><td><b>Profesionalni upravnik</b></td><td class="r">20.000 din</td></tr>
</table>
<div class="note">Ista kazna i za tresenje stolnjaka sa terase i bacanje stvari kroz prozor.</div>""",
    "Izvor: " + OD + ", čl. 39 (stanar: tač. 2, 3, 7, 9) i čl. 40 (upravnik). Prekršajni nalog izdaje inspektor ili komunalni milicionar (čl. 38 st. 4).",
    alt="Tabela fiksnih kazni po kućnom redu Beograda. Stanar, fizičko lice: 5.000 dinara. Preduzetnik: 25.000 dinara. Firma kao stanar: 50.000 dinara. Upravnik izabran iz zgrade: 10.000 dinara. Profesionalni upravnik: 20.000 dinara. Ista kazna stanaru i za tresenje stolnjaka sa terase i bacanje stvari kroz prozor. Izvor: Odluka o opštim pravilima kućnog reda grada Beograda, Sl. list 101/2019, čl. 39 i 40.")

# 8 ZAKLJUCAK / KAKO
add("""<div class="kick">Šta da radiš</div><h2>Prvo razgovor,<br><span class="gold">pa prijava</span></h2>
<div class="li">Prvi korak: zvono na vrata. Možda komšija <b>ne zna</b> za 16–18 i nedelju do 10.</div>
<div class="li">Ne vredi? Prijavu može da podnese <b>upravnik ili bilo koji stanar</b> nadležnoj inspekciji.</div>
<div class="li"><b>Komunalna milicija</b> kontroliše kućni red i može na licu mesta da izda prekršajni nalog.</div>
<div class="li">Van Beograda? Svaki grad ima <b>svoju odluku</b> i svoje sate. Proveri pre svađe.</div>""",
    "Izvor: " + OD + ", čl. 37 i 38. Saveti „zvono na vrata” i „proveri pre svađe”: mišljenje STANOLOGIJA.")

# 9 CTA
add("""<div style="margin-top:120px"><div class="kick">Sačuvaj raspored, a još bolje:</div>
<h1 style="font-size:96px">Nedelja:<br><span class="gold">tišina do 10</span></h1>
<div class="lead">Pošalji ovo komšiji koji buši vikendom ujutru (ili komšijskoj Viber grupi zgrade).</div>
<div class="tag">Prati @stanologija · sutra: cene stanova</div></div>""")

d.render(HERE, extra_css=EXTRA)
contact_sheet(HERE, N, sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "..", "..", "..", "sheet.jpg"))
