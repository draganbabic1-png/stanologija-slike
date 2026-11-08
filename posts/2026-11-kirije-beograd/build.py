import sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "tools"))
from stanologija import Deck, bars, eur

M2 = [("Centar", 16.7), ("Vračar", 15.4), ("Novi Beograd", 14.1), ("Palilula", 13.4), ("Voždovac", 12.3), ("Mirijevo", 8.9)]
PLATA_EUR = 149577 / 117.2  # ~1276


d = Deck(n=8)
add = d.add

add("""<div style="margin-top:150px"><div class="kick">Beograd · novembar 2026</div>
<h1>Koliko<br>plate ti<br><span class="gold">pojede<br>kirija?</span></h1>
<div class="lead">Računamo za stan od 40 m² u šest delova grada.</div>
<div class="tag">Prevuci →</div></div>""")

add(f"""<div class="kick">Korak 1</div><h2>Cena zakupa<br>po m² mesečno</h2>
<div style="margin-top:70px">{bars(M2, 16.7, lambda v: f"{v:.1f} €".replace('.', ','))}</div>
<div class="note">Centar je skoro duplo skuplji od Mirijeva.</div>""",
    "Izvor: Nekretnine.rs, prosečne oglašene cene, analiza tržišta mart 2026 (ažurirano sept. 2026). Bez režija.")

add(f"""<div class="kick">Korak 2</div><h2>Stan od 40 m²<br>mesečno košta</h2>
<div style="margin-top:70px">{bars([(l, v*40) for l, v in M2], 668, eur)}</div>
<div class="note">Plus režije, plus depozit od 1–2 kirije na ulasku.</div>""",
    "Obračun: cena po m² × 40 m². Izvor cena: Nekretnine.rs (mart 2026).")

add(f"""<div class="kick">Korak 3</div><h2>Prosečna plata<br>u Beogradu</h2>
<div class="big" style="margin-top:60px">149.577</div>
<div class="lead" style="margin-top:10px">dinara neto, jul 2026 ≈ <span class="gold">{eur(PLATA_EUR)}</span></div>
<div class="card"><b>95.036 din</b>Medijalna plata u Srbiji. Polovina zaposlenih zarađuje do tog iznosa, pa je prosek za mnoge previsok.</div>""",
    "Izvor: RZS, prosečna neto zarada Beogradski region, jul 2026; medijalna za Srbiju. Kurs ≈ 117,2 din/€.")

add(f"""<div class="kick">Rezultat</div><h2>Deo plate koji<br>ode na kiriju</h2>
<div style="margin-top:50px">{bars([(l, v*40/PLATA_EUR*100) for l, v in M2], 52.4, lambda v: f"{v:.0f}%", hi=lambda v: v > 30)}</div>
<div class="note">Uobičajeno pravilo: kirija do <span class="gold">30%</span> neto plate. Zlatno = iznad tog praga.</div>""",
    "Obračun STANOLOGIJA: kirija za 40 m² ÷ prosečna neto plata Beogradski region (jul 2026). Jedna plata, bez režija.")

add("""<div class="kick">Šta kažu podstanari</div><h2>Anketa:<br>kirija vs plata</h2><div style="transform:scale(0.92);transform-origin:top left;width:980px">
<div class="card"><b>44,3%</b>podstanara u Beogradu daje između 30% i 50% zarade za kiriju.</div>
<div class="card"><b>60,7%</b>smatra da su kirije potpuno nerealne u odnosu na plate.</div>
<div class="card"><b>7,1%</b>plaća više od 700 € mesečno.</div></div>""",
    "Izvor: anketa portala 4zida, objavljeno april 2026 (Danas/FoNet). Metodologija nije objavljena.")

add("""<div class="kick">Šta se dešava ove jeseni</div><h2>Zakupci su imali<br>prednost. <span class="gold">Do avgusta.</span></h2>
<div class="lead" style="font-size:32px">2025. i početkom 2026. kirije su padale u većini opština.</div>
<div class="card"><b>+20–30%</b>od kraja jula, po proceni jednog beogradskog agenta. Razlozi: novi talas dolazaka iz Rusije i studenti u septembru.</div>
<div class="note">⚠ Ovo je procena sa tržišta, ne zvanična statistika. Pratimo da li će je potvrditi podaci.</div>""",
    "Izvori: City Expert (pad 10–30%, 2025); Srpske novine / Meduza, 29.9.2026 (procena agenta).")

add("""<div style="margin-top:160px"><div class="kick">Tvoj red</div>
<h1 style="font-size:96px">Koliko ti<br>plaćaš i <span class="gold">gde?</span></h1>
<div class="lead">Napiši u komentaru: deo grada, kvadratura, kirija.<br>Iz vaših odgovora pravimo sledeću analizu.</div>
<div class="tag">Sačuvaj · Podeli podstanaru</div></div>""")

d.render(HERE)
