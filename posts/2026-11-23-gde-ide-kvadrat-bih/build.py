import sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "tools"))
from stanologija import Deck, bars, contact_sheet

KM_EUR = 1.95583                       # fiksni kurs (valutni odbor CBBiH)
CENA = 3238                            # KM/m², nov stan, BiH, 3. kvartal 2026 (BHAS)
DELOVI = [("Gradnja", 1954), ("Ostalo", 910), ("Zemljište", 374)]
M2 = 55

def km(x): return f"{x:,.0f} KM".replace(",", ".")
def pct(x): return f"{x:.1f}".replace(".", ",") + "%"

EXTRA = """
.compact .row{margin-bottom:26px}.compact .lab{width:250px;flex-shrink:0;font-size:36px}
.tbl{margin-top:40px;width:100%;border-collapse:collapse;font-size:32px}
.tbl td{padding:18px 0;border-bottom:1px solid #2A4562;vertical-align:middle}
.tbl td.r{text-align:right;font-family:Oswald;font-weight:600;font-size:42px;white-space:nowrap;padding-left:18px}
.tbl td.o{color:var(--muted)}
.tbl td.n{color:var(--gold)}
.tbl td.up{color:#E07A5F}.tbl td.dn{color:#7FC8A9}
.tbl th{font-size:22px;color:var(--muted);font-weight:600;text-align:right;letter-spacing:2px;padding-bottom:6px}
.tbl th:first-child{text-align:left}
.li{font-size:33px;line-height:1.4;padding:16px 0 16px 54px;border-bottom:1px solid #2A4562;position:relative}
.li:before{content:"•";position:absolute;left:10px;top:8px;font-family:Oswald;font-weight:700;font-size:48px;color:var(--gold)}
.split{display:flex;height:90px;margin-top:50px;border-radius:4px;overflow:hidden}
.split div{display:flex;align-items:center;justify-content:center;font-family:Oswald;font-weight:600;font-size:34px;color:var(--navy)}
"""

d = Deck(n=8)
add = d.add

# 1 HOOK
add(f"""<div style="margin-top:120px"><div class="kick">BiH · nov stan · 3. kvartal 2026.</div>
<h1>Gde ide<br>tvoj novac<br>za <span class="gold">kvadrat?</span></h1>
<div class="lead">Kvadrat novogradnje u BiH košta <span class="gold">{km(CENA)}</span> (oko 1.656 €). Statistika ga je rastavila na delove.</div>
<div class="tag">Prevuci →</div></div>""",
    alt="Slajd 1/8, STANOLOGIJA. Naslov: Gde ide tvoj novac za kvadrat? BiH, nov stan, 3. kvartal 2026. Kvadrat novogradnje u BiH košta 3.238 KM (oko 1.656 €). Statistika ga je rastavila na delove. Prevuci.")

# 2 CENA
add(f"""<div class="kick">Prosečna cena</div><h2>3.238 KM<br>po kvadratu</h2>
<div class="card"><b>+8,2%</b>u odnosu na isti kvartal 2025.</div>
<div class="card"><b>+332 KM</b>po m² za dve godine. U 3. kvartalu 2024. kvadrat je bio 2.906 KM.</div>
<div class="note">Prodato je 1.176 novih stanova (64.321 m²) od jula do kraja septembra 2026.</div>""",
    "Izvor: Agencija za statistiku BiH, Cijene prodatih novih stanova, 3. kv. 2026 (preneli RTV Slon 20.11. i Srpskainfo 22.11.2026). 1 € = 1,95583 KM.")

# 3 RAZLAGANJE
sp = "".join(f'<div style="width:{v/CENA*100:.2f}%;background:{c}">{pct(v/CENA*100)}</div>'
             for (l, v), c in zip(DELOVI, ["#E6B256", "#C9A15A", "#9FB0C2"]))
add(f"""<div class="kick">Razlaganje jednog m²</div><h2>Od 3.238 KM<br>ide na...</h2>
<div class="compact" style="margin-top:56px">{bars(DELOVI, 1954*560/450, km, hi=lambda v: v > 1000)}</div>
<div class="split">{sp}</div>
<div class="note"><span class="gold">Gradnja</span> = radovi i dobit izvođača. <span class="gold">Ostalo</span> = dozvole, projekat, nadzor, porezi, kamate, PDV, troškovi i zarada investitora.</div>""",
    "Izvor: Agencija za statistiku BiH, 3. kv. 2026. Udeli: Obračun STANOLOGIJA (deo ÷ 3.238).",
    alt="Slajd 3/8, STANOLOGIJA. Grafikon: od 3.238 KM po m² novog stana u BiH (3. kvartal 2026) na gradnju i dobit izvođača ide 1.954 KM (60,3%), na ostale troškove uključujući PDV 910 KM (28,1%), a na građevinsko zemljište 374 KM (11,6%). Gradnja je najveći deo, zemljište najmanji. Ostalo obuhvata dozvole, projekat, nadzor, poreze, kamate, PDV, troškove i zaradu investitora. Izvor: Agencija za statistiku BiH.")

# 4 STAN OD 55 m2
rows = "".join(f'<tr><td>{l}</td><td class="r n">{km(v*M2)}</td></tr>' for l, v in DELOVI)
add(f"""<div class="kick">Prosečan prodat stan · 55 m²</div><h2>Tvojih<br>178.090 KM</h2>
<table class="tbl" style="margin-top:44px">{rows}<tr><td><b>Ukupno</b></td><td class="r">{km(CENA*M2)}</td></tr></table>
<div class="card" style="font-size:32px;padding:30px 40px"><b style="font-size:56px">20.570 KM</b>je zemljište. Gradnja je 5 puta veći trošak.</div>""",
    "Obračun STANOLOGIJA: 55 m² × cena dela po m² (BHAS, 3. kv. 2026). 55 m² = prosečan prodat nov stan prema RTV Slon / BHAS. ≈ 91.056 € po kursu 1,95583.")

# 5 DVE GODINE
T = [("Gradnja", 1699, 1954, "+15,0%", "up"), ("Ostalo", 814, 910, "+11,8%", "up"), ("Zemljište", 394, 374, "−5,1%", "dn")]
rows = "".join(f'<tr><td>{l}</td><td class="r o">{km(a)[:-3]}</td><td class="r n">{km(b)[:-3]}</td><td class="r {c}">{p}</td></tr>'
               for l, a, b, p, c in T)
add(f"""<div class="kick">Šta je poskupelo · 2024 → 2026</div><h2>Zemljište je<br><span class="gold">pojeftinilo</span></h2>
<table class="tbl" style="margin-top:50px"><tr><th></th><th>3. KV 2024</th><th>3. KV 2026</th><th>RAZLIKA</th></tr>{rows}</table>
<div class="note" style="margin-top:36px">Cenu kvadrata vuku <span class="gold">radovi i ostali troškovi</span>, ne plac.</div>""",
    "KM po m², nov stan, BiH. Izvor: Agencija za statistiku BiH (preneo Srpskainfo, 22.11.2026).",
    alt="Slajd 5/8, STANOLOGIJA. Tabela, KM po m² novog stana u BiH, 3. kvartal 2024 prema 3. kvartalu 2026: gradnja 1.699 → 1.954 KM (+15,0%), ostali troškovi 814 → 910 KM (+11,8%), građevinsko zemljište 394 → 374 KM (−5,1%). Naslov: Zemljište je pojeftinilo. Cenu kvadrata vuku radovi i ostali troškovi, ne plac. Izvor: Agencija za statistiku BiH, preneo Srpskainfo 22.11.2026.")

# 6 OSTALO
add("""<div class="kick">Šta je u „ostalo”</div><h2>910 KM koje<br>ne vidiš</h2>
<div style="margin-top:40px">
<div class="li">Dozvole, projektovanje, geodetski radovi</div>
<div class="li">Nadzor i osiguranje</div>
<div class="li">Porezi i PDV</div>
<div class="li">Kamate na kredite investitora</div>
<div class="li">Troškovi i zarada investitora</div></div>
<div class="note">Zarada investitora <span class="gold">nije posebno prikazana</span>. Skrivena je u ovoj stavci.</div>""",
    "Izvor: Agencija za statistiku BiH, metodološka napomena (saopštenje 2. kv. 2026, 20.8.2026); Srpskainfo 22.11.2026.")

# 7 TRZISTE
add("""<div class="kick">Tržište 2026.</div><h2>Kupuje se više,<br>gradi manje</h2>
<div class="card" style="padding:30px 40px"><b>+26,9%</b>više prodatih novih stanova za 9 meseci 2026. nego za isti period 2025. Cena m² +11,7%.</div>
<div class="card" style="padding:30px 40px"><b>6.385</b>stanova u izgradnji krajem septembra. Godinu ranije 6.936 (−7,9%).</div>
<div class="note">U odnosu na 2. kvartal (3.311 KM) kvadrat je u 3. kvartalu jeftiniji 2,2%. Jedan kvartal još nije trend.</div>""",
    "Izvor: Agencija za statistiku BiH, 2. i 3. kv. 2026; RTV Slon 20.11.2026. Kvartalna promena: Obračun STANOLOGIJA (3.238 ÷ 3.311 − 1). Poslednja rečenica je mišljenje.")

# 8 CTA
add("""<div style="margin-top:150px"><div class="kick">Pre kapare</div>
<h1 style="font-size:96px">Kupuješ stan<br>u <span class="gold">BiH?</span></h1>
<div class="lead">Znaj šta plaćaš: 60% je gradnja, 12% plac, a ostatak su troškovi i zarada investitora.</div>
<div class="note">Statistika važi za prosek BiH i samo nove stanove (bez starih i roh-bau).</div>
<div class="tag">Pošalji ovo nekome ko kupuje stan</div></div>""")

d.render(HERE, extra_css=EXTRA)
contact_sheet(HERE, 8, "/tmp/claude-0/-home-claude-stanologija-slike/eaa90489-d52d-5809-89a9-70115a2d4013/scratchpad/sheet.jpg")
