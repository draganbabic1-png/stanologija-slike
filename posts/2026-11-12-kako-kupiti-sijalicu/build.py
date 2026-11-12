import sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "tools"))
from stanologija import Deck, bars, contact_sheet

# EU Uredba 244/2009, Prilog II, Tabela 6: LED lumeni koji odgovaraju klasičnoj sijalici
EKV = [("25 W", 249), ("40 W", 470), ("60 W", 806), ("75 W", 1055), ("100 W", 1521)]
# EU Uredba 2019/2015: klase energetske efikasnosti (lm/W)
KLASE = [("A", "210+"), ("B", "185–210"), ("C", "160–185"), ("D", "135–160"), ("E", "110–135"), ("F", "85–110"), ("G", "ispod 85")]
LM = 806
def w(x): return f"{LM/x:.1f}".replace(".", ",")
WATT = ["do " + w(210), w(210)+"–"+w(185), w(185)+"–"+w(160), w(160)+"–"+w(135), w(135)+"–"+w(110), w(110)+"–"+w(85), "preko "+w(85)]

def lm(v): return f"{v:,} lm".replace(",", ".")
def kwh(v): return (f"{v:.1f}" if v % 1 else f"{v:.0f}").replace(".", ",") + " kWh"

EXTRA = """
.compact .row{margin-bottom:24px}.compact .bar{height:62px}.compact .lab{width:190px;flex-shrink:0;font-size:36px}.compact .val{font-size:42px}
.tbl{margin-top:36px;width:100%;border-collapse:collapse;font-size:32px}
.tbl td{padding:11px 0;border-bottom:1px solid #2A4562;vertical-align:middle}
.tbl td.k{font-family:Oswald;font-weight:700;font-size:44px;width:90px;color:var(--gold)}
.tbl td.r{text-align:right;font-family:Oswald;font-weight:500;font-size:38px;white-space:nowrap}
.tbl th{font-size:22px;color:var(--muted);font-weight:600;text-align:right;letter-spacing:2px;padding-bottom:6px}
.tbl th:first-child{text-align:left}
.tbl tr.hl td{background:#16304A}
.kel{display:flex;align-items:center;padding:16px 0;border-bottom:1px solid #2A4562}
.kel .sw{width:64px;height:64px;border-radius:50%;flex-shrink:0;margin-right:30px}
.kel .kv{font-family:Oswald;font-weight:600;font-size:46px;width:190px;flex-shrink:0}
.kel .tx{font-size:30px;line-height:1.35}.kel .tx small{display:block;color:var(--muted);font-size:24px}
.li{font-size:33px;line-height:1.4;padding:20px 0 20px 64px;border-bottom:1px solid #2A4562;position:relative}
.li:before{content:"✓";position:absolute;left:0;top:16px;font-family:Oswald;font-weight:700;font-size:40px;color:var(--gold)}
.li small{display:block;font-size:25px;color:var(--muted);margin-top:4px}
"""

d = Deck(n=8)
add = d.add

add("""<div style="margin-top:130px"><div class="kick">Rasveta · 4 broja sa kutije</div>
<h1>Ne kupuj<br>sijalicu<br><span class="gold">po vatima</span></h1>
<div class="lead">Vati kažu koliko sijalica troši, ne koliko svetli. Evo šta zapravo treba da čitaš na kutiji.</div>
<div class="tag">Prevuci →</div></div>""")

add(f"""<div class="kick">1 · Lumeni (lm) = svetlo</div><h2>Koliko lumena<br>menja staru sijalicu</h2>
<div class="compact" style="margin-top:50px">{bars(EKV, 1521, lm, hi=lambda v: v == 806)}</div>
<div class="note">Levo: snaga stare (obične) sijalice. Desno: koliko lumena mora da ima LED da bi smela da se reklamira kao njena zamena. Klasična 60 W = <span class="gold">806 lm</span>.</div>""",
    "Izvor: Uredba Komisije (EZ) 244/2009, Prilog II, Tabela 6 (vrednosti za LED).")

rows = "".join(f'<tr{" class=hl" if k in ("E","F") else ""}><td class="k">{k}</td><td class="r">{t}</td><td class="r">{wt} W</td></tr>' for (k, t), wt in zip(KLASE, WATT))
add(f"""<div class="kick">2 · Energetska klasa</div><h2>Nova skala A–G<br>je mnogo strožija</h2>
<table class="tbl"><tr><th>KLASA</th><th>LUMENA PO VATU</th><th>LED OD 806 LM TROŠI</th></tr>{rows}</table>
<div class="note">Od 1. septembra 2021. nema više A++. Ista LED sijalica koja je bila „A+” danas je obično E ili F.</div>""",
    "Izvor: Delegirana uredba (EU) 2019/2015 (klase). Obračun STANOLOGIJA: vati = 806 lm ÷ lm/W. „Obično E ili F” je procena STANOLOGIJA.")

POT = [("Obična", 60), ("LED F", 9.5), ("LED C", 5.0)]
add(f"""<div class="kick">3 · Potrošnja</div><h2>Isto svetlo,<br>6 do 12 puta manje struje</h2>
<div class="compact" style="margin-top:50px">{bars(POT, 60, kwh, hi=lambda v: v < 60)}</div>
<div class="card" style="font-size:31px;padding:28px 40px"><b style="font-size:52px">−84% do −92%</b>potrošnje na svakih 1.000 sati gorenja (oko 11 meseci ako svetli 3 sata dnevno).</div>""",
    "Obračun STANOLOGIJA za 806 lm i 1.000 h: obična 60 W = 60 kWh; LED klase F najviše 9,5 kWh; LED klase C najviše 5,0 kWh. Pomnoži sa cenom kWh sa svog računa.")

K = [("#FFB46B","2700 K","Toplo bela","spavaća, dnevna, trpezarija"),("#FFC88A","3000 K","Svetlija topla","kupatilo, hodnik, akcenti"),
     ("#FFDDB5","3500 K","Neutralna","kuhinja, kućna kancelarija"),("#FFF0DE","4000 K","Hladnija bela","radna ploča, ogledalo"),("#F2F5FF","5000 K","Dnevna","garaža, podrum, ostava")]
kel = "".join(f'<div class="kel"><div class="sw" style="background:{c}"></div><div class="kv">{k}</div><div class="tx">{n}<small>{r}</small></div></div>' for c,k,n,r in K)
add(f"""<div class="kick">4 · Kelvini (K) = boja svetla</div><h2>Topla ili<br>hladna?</h2>
<div style="margin-top:34px">{kel}</div>
<div class="note">Kelvini ne menjaju jačinu svetla, samo njegovu boju.</div>""",
    "Izvor: Feit Electric, vodič za temperaturu boje (preporuke proizvođača, ne propis).")

add("""<div class="kick">5 · CRI (Ra) = verne boje</div><h2>Zašto ti hrana<br>izgleda sivo</h2>
<div class="big" style="margin-top:46px">Ra 80</div>
<div class="lead" style="margin-top:10px">je zakonski minimum za sijalice u EU od <span class="gold">1. septembra 2021.</span> Maksimum je 100.</div>
<div class="card" style="font-size:31px;padding:28px 40px"><b style="font-size:46px">Savet</b>Za kuhinju, kupatilo i ogledalo traži Ra 90 ili više. Boja hrane, kože i šminke izgleda prirodnije.</div>""",
    "Izvor: Uredba Komisije (EU) 2019/2020, Prilog II, Tabela 4. Savet o Ra 90+ je mišljenje STANOLOGIJA.")

add("""<div class="kick">Podsetnik za prodavnicu</div><h2>Na kutiji traži</h2>
<div style="margin-top:36px">
<div class="li">Lumene, ne vate<small>806 lm = stara 60 W · 1.521 lm = stara 100 W</small></div>
<div class="li">Klasu što bliže A<small>razlika se vidi na računu, ne na sijalici</small></div>
<div class="li">2700–3000 K za odmor<small>3500–4000 K za rad i kuvanje</small></div>
<div class="li">Ra 80 je minimum<small>Ra 90+ gde su boje važne</small></div></div>""",
    "Izvori: Uredbe (EZ) 244/2009, (EU) 2019/2015 i (EU) 2019/2020; Feit Electric. Pravila EU; van EU proveri šta piše na kutiji.")

add("""<div style="margin-top:160px"><div class="kick">Tvoj red</div>
<h1 style="font-size:100px">Pošalji ovo<br>nekome ko <span class="gold">oprema<br>stan</span></h1>
<div class="lead">Ili onome ko i dalje pita prodavca „imate li neku od 60 vati?”</div>
<div class="tag">Pošalji · Sačuvaj za prodavnicu</div></div>""")

d.render(HERE, extra_css=EXTRA)
contact_sheet(HERE, 8, "/tmp/claude-0/-home-claude-stanologija-slike/54ed6c6e-9ad7-5a61-ab4a-906c689b856f/scratchpad/sheet.jpg")
