import sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "tools"))
from stanologija import Deck, bars, eur, contact_sheet

STANOVI = [("Mamutica", 1169), ("Karaburma*", 1000), ("Lamele 21", 795), ("Rudo (3)", 570)]
def n(v): return f"{v:,}".replace(",", ".")

EXTRA = """
.compact .row{margin-bottom:22px}.compact .bar{height:62px}.compact .lab{width:250px;flex-shrink:0;font-size:34px}.compact .val{font-size:42px}
.grid{display:grid;grid-template-columns:1fr 1fr;gap:22px;margin-top:44px}
.cell{background:#16304A;padding:26px 30px;border-top:6px solid var(--gold)}
.cell b{display:block;font-family:Oswald;font-weight:700;font-size:70px;color:var(--gold);line-height:1.05}
.cell span{font-size:28px;line-height:1.35;display:block;margin-top:6px}
"""

d = Deck(n=8)
add = d.add

add("""<div style="margin-top:130px"><div class="kick">Kuriozeti · ex-YU</div>
<h1>Da li bi živeo<br>sa <span class="gold">5.000<br>komšija?</span></h1>
<div class="lead">Zgrade u kojima živi više ljudi nego u mnogim selima. Najveće stambene grdosije Zagreba i Beograda, u brojevima.</div>
<div class="tag">Prevuci →</div></div>""")

add("""<div class="kick">Zagreb · Travno</div><h2>Mamutica</h2>
<div class="grid">
<div class="cell"><b>1.169</b><span>stanova</span></div>
<div class="cell"><b>~5.000</b><span>stanara</span></div>
<div class="cell"><b>240 m</b><span>dužina</span></div>
<div class="cell"><b>19</b><span>spratova, oko 60 m visine</span></div>
<div class="cell"><b>2 god.</b><span>od kamena temeljca (1974) do useljenja (1976)</span></div>
<div class="cell"><b>256</b><span>garaža i 24 lokala</span></div></div>
<div class="note">Najveća zgrada u Hrvatskoj po zapremini. Stanovi od 40 do 130 m².</div>""",
    "Izvori: B92, 14.10.2024; Wikipedia (Mamutica). Broj stanara je procena.")

add("""<div class="kick">Novi Beograd · Blok 21</div><h2>Lamele: zgrada<br>duga skoro 1 km</h2>
<div class="grid">
<div class="cell"><b>~1 km</b><span>9 lamela spojenih u niz</span></div>
<div class="cell"><b>62</b><span>ulaza na 4 adrese</span></div>
<div class="cell"><b>795</b><span>stanova</span></div>
<div class="cell"><b>~3.500</b><span>stanara</span></div></div>
<div class="note">Najduža zgrada bivše Jugoslavije. Projektovao tim „Beogradskih pet" predvođen Mihailom Čankom.</div>""",
    "Izvori: Telegraf, 4.11.2019 (glavni urbanista Beograda); Novosti, 20.12.2020. Neki izvori navode 798 stanova.")

add(f"""<div class="kick">Okršaj</div><h2>Ko ima<br>najviše stanova?</h2>
<div class="compact" style="margin-top:60px">{bars(STANOVI, 1169*560/470, n, hi=lambda v: v >= 1169)}</div>
<div class="note">Mamutica je i dalje rekorder. Ali Beograd je dobio dozvolu za zgradu koja joj se približava.</div>""",
    "Broj stanova po zgradi/kompleksu. *Karaburma: planirano, oko 1.000 (N1, 7.6.2025). Rudo = 3 solitera ukupno. Izvori: B92; Telegraf; Wikipedia (Eastern City Gate).")

add("""<div class="kick">Beograd · Istočna kapija</div><h2>Rudo: kad beton<br>pada sa fasade</h2>
<div class="grid">
<div class="cell"><b>3 × 28</b><span>spratova</span></div>
<div class="cell"><b>570</b><span>stanova (190 po zgradi)</span></div>
<div class="cell"><b>1976.</b><span>useljenje, fasada nije bila završena</span></div>
<div class="cell"><b>60 kg</b><span>komadi betona do te težine padali sa zgrada (2013)</span></div></div>
<div class="card" style="font-size:31px;padding:28px 40px"><b style="font-size:52px">4 miliona €</b>procena za fasadu po savremenim standardima. Stanari su tada skupili oko 110.000 €.</div>""",
    "Izvor: Wikipedia (Eastern City Gate), podaci o fasadi iz 2013. Stanje fasade danas nije obuhvaćeno.")

add("""<div class="kick">Beograd · Karaburma · u planu</div><h2>Nova Mamutica<br>na Karaburmi?</h2>
<div class="grid">
<div class="cell"><b>~1.000</b><span>stanova</span></div>
<div class="cell"><b>250 m</b><span>dužina „zida"</span></div>
<div class="cell"><b>~3.000</b><span>novih komšija (procena stanara kraja)</span></div>
<div class="cell"><b>1.500+</b><span>novih parking mesta</span></div></div>
<div class="note">Ugao Uralske i Diljske. Grad je odbio dozvolu, investitor ju je dobio od Republike. Stanari protestuju: infrastruktura se ne širi.</div>""",
    "Izvor: N1, 7.6.2025. Brojevi su iz najave projekta, ne iz gotove zgrade. Trenutnu fazu gradnje nismo proverili.")

add("""<div class="kick">Za poređenje · Evropa</div><h2>A napolju<br>ima i većih</h2>
<div class="card" style="font-size:31px;padding:28px 40px"><b style="font-size:52px">Karl-Marx-Hof, Beč</b>1930. Oko 1,1 km dužine i oko 1.400 stanova.</div>
<div class="card" style="font-size:31px;padding:28px 40px"><b style="font-size:52px">Akademika Zabolotnog, Kijev</b>Prvi stanari 1980. Oko 4.500 stanova i preko 12.000 stanara.</div>
<div class="note">Mamutica je po broju stanova u istoj ligi sa bečkim rekorderom. Kijevska zgrada ima skoro četiri Mamutice.</div>""",
    "Izvor: nekretnine.rs, 18.3.2026. Poslednja rečenica: Obračun STANOLOGIJA, 4.500 ÷ 1.169 ≈ 3,8.")

add("""<div style="margin-top:160px"><div class="kick">Tvoj red</div>
<h1 style="font-size:96px">Pošalji ovo<br><span class="gold">komšiji</span></h1>
<div class="lead">Pošalji ovo nekome ko živi u Mamutici, Lamelama ili sličnoj grdosiji. A ti napiši: koja je najveća zgrada u tvom gradu?</div>
<div class="tag">Pošalji · Sačuvaj · Komentariši</div></div>""")

d.render(HERE, extra_css=EXTRA)
contact_sheet(HERE, 8, "/tmp/claude-0/-home-claude-stanologija-slike/f1006d50-3ba9-526a-806c-06eeddc09804/scratchpad/sheet.jpg")
