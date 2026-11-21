import sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "tools"))
from stanologija import Deck, bars, eur, contact_sheet

# Izvori:
# - KADENA Sotheby's International Realty, "Market Report Novi Beograd: premium novogradnja", oktobar 2026 (snimak oglasa 7.10.2026;
#   150 jedinstvenih oglasa za prodaju u završenim kompleksima, Halo oglasi / 4zida / Nadji Dom; medijane traženih cena).
#   Isti izveštaj navodi RGZ 1. pol. 2026: Beograd prosek 3.219 €/m² (+13,9%), Novi Beograd 3.385 / novogradnja 3.473 (+15,7%),
#   kupovina od investitora (medijana): SOUL 64 4.020, Wellport 3.667; tabela premije: Soul 64 +30%, Wellport +39%,
#   Airport Garden +33% (3.286), Lux 51 +20% (3.214); kirije i bruto prinosi; krediti 40,2% (1. pol. 2023: 22,5%).
# - Nova.rs, 21.11.2026 (M. Milovanović): Blok 64/65, prenosi KADENA i RGZ.

EXTRA = """
.tbl{margin-top:36px;width:100%;border-collapse:collapse;font-size:34px}
.tbl th{font-size:24px;color:var(--muted);font-weight:600;text-align:right;padding-bottom:10px;letter-spacing:1px;text-transform:uppercase}
.tbl th:first-child{text-align:left}
.tbl td{padding:22px 0;border-bottom:1px solid #2A4562}
.tbl td.r{text-align:right;font-family:Oswald;font-weight:600;font-size:44px;white-space:nowrap;padding-left:18px}
.tbl td.g{color:var(--gold)}
.lab{width:320px;font-size:32px}
.val{font-size:40px}
.row{margin-bottom:26px}
.bar{height:60px}
.two{display:flex;gap:28px;margin-top:40px}
.two .card{flex:1;margin-top:0;padding:32px 34px;font-size:30px}
.two .card b{font-size:62px}
.st{display:flex;align-items:flex-start;margin-bottom:30px;font-size:34px;line-height:1.4}
.st .n{font-family:Oswald;font-weight:700;font-size:56px;color:var(--gold);width:70px;flex:none;line-height:1}
"""

KAD = "KADENA Sotheby's, Market Report Novi Beograd, okt. 2026 (oglasi 7.10.2026)"
RGZ = "RGZ, 1. polugodište 2026 (preko KADENA izveštaja)"
d = Deck(n=8)
add = d.add

add("""<div style="margin-top:110px"><div class="kick">Novi Beograd · oglas vs ugovor</div>
<h1>Isti blok,<br><span class="gold">dve cene</span></h1>
<div class="lead">Gotov stan iz preprodaje se oglašava i do <span class="gold">39% skuplje</span> nego što su kupci plaćali investitoru u istoj zgradi.</div>
<div class="tag">Prevuci →</div></div>""",
    KAD + "; " + RGZ + ".")

add("""<div class="kick">Polazna tačka</div><h2>Šta stvarno plaćamo,<br>a šta se traži</h2>
<div class="two">
<div class="card"><b>3.473 €</b>prosek ugovora za novogradnju, Novi Beograd (RGZ, 1. pol. 2026)</div>
<div class="card"><b>4.750 €</b>medijana oglasa, 150 stanova u vodećim kompleksima (okt. 2026)</div>
</div>
<div class="note" style="margin-top:34px">Ceo Beograd: prosek ugovora <b>3.219 €/m²</b>, +13,9% za godinu dana. Oglas je cena pre pregovora, ugovor je ono što je zaista plaćeno.</div>""",
    RGZ + "; " + KAD + ". Cene po m².")

add("""<div class="kick">Cena po m²</div><h2>Od investitora<br>vs preprodaja</h2>
<table class="tbl">
<tr><th>Kompleks</th><th>Investitor</th><th>Oglas</th><th>Razlika</th></tr>
<tr><td>Wellport</td><td class="r">3.667</td><td class="r">5.091</td><td class="r g">+39%</td></tr>
<tr><td>Airport Garden</td><td class="r">3.286</td><td class="r">4.375</td><td class="r g">+33%</td></tr>
<tr><td>Soul 64</td><td class="r">4.020</td><td class="r">5.221</td><td class="r g">+30%</td></tr>
<tr><td>Lux 51</td><td class="r">3.214</td><td class="r">3.855</td><td class="r g">+20%</td></tr>
</table>
<div class="note" style="margin-top:26px">Investitor = medijana ugovora RGZ, 1. pol. 2026. Oglas = medijana traženih cena, 7.10.2026.</div>""",
    KAD + " (tabela premije gotovog stana). Razlika = oglas ÷ investitor − 1.")

add("""<div class="kick">Obračun STANOLOGIJA</div><h2>Stan od 60 m²<br>u Wellportu</h2>
<div class="two">
<div class="card"><b>220.020 €</b>po ceni ugovora sa investitorom</div>
<div class="card"><b>305.460 €</b>po medijani oglasa za gotov stan</div>
</div>
<div class="big" style="font-size:150px;margin-top:50px">+85.440 €</div>
<div class="lead" style="margin-top:6px">razlika za istu kvadraturu. Po beogradskom proseku ugovora to je još oko <span class="gold">26 m²</span> stana.</div>""",
    "Obračun STANOLOGIJA: 60 × 3.667 = 220.020 €; 60 × 5.091 = 305.460 €; razlika 85.440 € ÷ 3.219 €/m² (RGZ, Beograd, 1. pol. 2026) ≈ 26,5 m². Oglasne cene, pre pregovora.")

add(f"""<div class="kick">Zgrada određuje cenu</div><h2>Medijana oglasa<br>po kompleksu, €/m²</h2>
<div style="margin-top:40px">{bars([("West 65 Kula",5975),("Soul 64",5221),("Wellport",5091),("A Blok",5078),("West 65",4952),("Belvil",4518),("Airport Garden",4375),("Lux 51",3855)], 5975*560/390, lambda v: f"{v:,}".replace(",", "."), hi=lambda v: v>=5000)}</div>
<div class="note">Ista opština, razlika između zgrada <b>preko 50%</b>.</div>""",
    KAD + ". Prikazani kompleksi sa 7+ oglasa; 5.975 ÷ 3.855 = 1,55.")

add("""<div class="kick">Zašto tolika razlika</div><h2>Nije sve<br>čista zarada</h2>
<div style="margin-top:40px">
<div class="st"><span class="n">1</span><div><b>Oglas nije ugovor.</b> Tražena cena je pre pregovora, prodaja se obično zaključi niže.</div></div>
<div class="st"><span class="n">2</span><div><b>Vreme.</b> Cena kod investitora se dogovara rano, a ugovor u RGZ-u se vidi i godinu dana kasnije. Kvadrat je u međuvremenu poskupeo.</div></div>
<div class="st"><span class="n">3</span><div><b>Rizik.</b> Ko kupi od investitora čeka gradnju i rizikuje rokove. Gotov stan je useljiv odmah.</div></div>
</div>""",
    KAD + ": napomene o poređenju (tražene vs ugovorene cene, vremenski razmak, različit proizvod).")

add("""<div class="kick">A ako ga izdaš?</div><h2>Kirija i bruto prinos</h2>
<table class="tbl">
<tr><th>Kompleks</th><th>Kirija</th><th>Prinos</th></tr>
<tr><td>Soul 64</td><td class="r">1.200 €</td><td class="r g">5,0%</td></tr>
<tr><td>Airport Garden</td><td class="r">1.200 €</td><td class="r g">5,2%</td></tr>
<tr><td>West 65</td><td class="r">1.550 €</td><td class="r g">4,5%</td></tr>
<tr><td>Wellport</td><td class="r">1.675 €</td><td class="r g">3,9%</td></tr>
</table>
<div class="note" style="margin-top:26px">Medijana tražene mesečne kirije. Neto prinos (posle poreza, troškova, praznog hoda) je obično 1-1,5 p.p. niži.</div>""",
    KAD + "; bruto prinos = kirija po m² × 12 ÷ cena po m² istog tipa stana (138 oglasa za izdavanje).")

add("""<div style="margin-top:150px"><div class="kick">Tvoj red</div>
<h1 style="font-size:92px">Pošalji<br><span class="gold">onome</span><br>ko kupuje stan</h1>
<div class="lead">Pošalji ovo nekome ko gleda stanove na Novom Beogradu, pre nego što prihvati prvu cenu iz oglasa. U komentaru: investitor ili gotov stan?</div>
<div class="tag">Pošalji · Sačuvaj</div></div>""")

d.render(HERE, extra_css=EXTRA)
contact_sheet(HERE, 8, "/tmp/claude-0/-home-claude-stanologija-slike/9c7b7bad-5139-5297-95d9-174254a7d47d/scratchpad/sheet.jpg")
