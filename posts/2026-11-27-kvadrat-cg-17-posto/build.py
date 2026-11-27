import sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "tools"))
from stanologija import Deck, contact_sheet, bars

EXTRA = """
.duo{display:flex;gap:28px;margin-top:50px}
.duo .c{flex:1;background:#16304A;border-top:8px solid #3A5470;padding:36px 34px}
.duo .c.h{border-top-color:var(--gold)}
.duo .c .n{font-family:Oswald;font-weight:600;font-size:38px;text-transform:uppercase;line-height:1.1}
.duo .c .g{font-family:Oswald;font-weight:700;font-size:80px;color:var(--gold);line-height:1.05;margin-top:14px}
.duo .c .t{font-size:29px;line-height:1.45;margin-top:10px;color:var(--cream)}
.lab{width:300px !important;font-size:32px !important}
.li{font-size:33px;line-height:1.4;padding:16px 0 16px 54px;border-bottom:1px solid #2A4562;position:relative}
.li:before{content:"•";position:absolute;left:10px;top:8px;font-family:Oswald;font-weight:700;font-size:48px;color:var(--gold)}
.li b{color:var(--gold)}
.tb{width:100%;border-collapse:collapse;margin-top:44px;font-size:31px}
.tb th{font-family:Oswald;font-weight:500;color:var(--gold);text-align:right;padding:12px 8px;font-size:28px;letter-spacing:1px;text-transform:uppercase}
.tb th:first-child,.tb td:first-child{text-align:left}
.tb td{padding:20px 8px;border-bottom:1px solid #2A4562;text-align:right}
.tb td b{font-family:Oswald;font-weight:600;font-size:40px}
.up{color:var(--gold);font-weight:700}
"""

N = 9
d = Deck(n=N)
add = d.add
M3 = "Monstat, Cijene stanova u novogradnji, 3. kv. 2026 (preliminarno; preneli Investitor.me i Dan, 19.11.2026)"
M2 = "Monstat 2. kv. 2026 (20.8.2026)"
M1 = "Monstat 3. kv. 2025 (20.11.2025)"

# 1 HOOK
add("""<div style="margin-top:110px"><div class="kick">Crna Gora · novi Monstat podaci</div>
<h1>Čekao si godinu?<br><span class="gold">Stan je skuplji 18.800 €</span></h1>
<div class="lead">Kvadrat novogradnje u Crnoj Gori: <span class="gold">2.604 €</span>. Za godinu dana <span class="gold">+16,9%</span>.</div>
<div class="tag">Prevuci →</div></div>""",
    "Izvor: " + M3 + ". Stan 50 m²: obračun STANOLOGIJA (50 × 376 €).")

# 2 ISTI STAN
add("""<div class="kick">Isti stan, godinu kasnije</div><h2>Stan od 50 m²<br><span class="gold">u novogradnji</span></h2>
<div class="duo">
<div class="c"><div class="n">3. kvartal 2025.</div><div class="g">111.400 €</div><div class="t">2.228 €/m²</div></div>
<div class="c h"><div class="n">3. kvartal 2026.</div><div class="g">130.200 €</div><div class="t">2.604 €/m²</div></div>
</div>
<div class="card"><b>+18.800 €</b>za iste kvadrate. U Podgorici: 107.650 → 126.500 € (+18.850 €).</div>""",
    "Izvor: " + M1 + "; " + M3 + ". Podgorica 2.153 → 2.530 €/m². Stan 50 m²: obračun STANOLOGIJA (cena/m² × 50).",
    alt="Dve kartice: stan od 50 m² u novogradnji u Crnoj Gori. U 3. kvartalu 2025. koštao je 111.400 € (2.228 € po m²), u 3. kvartalu 2026. košta 130.200 € (2.604 € po m²). Razlika: 18.800 € za iste kvadrate. U Podgorici: sa 107.650 na 126.500 €, odnosno 18.850 € više. Izvor: Monstat; obračun STANOLOGIJA, cena po m² puta 50.")

# 3 DVE GODINE
R = [("3. kv. 2024", 1854), ("3. kv. 2025", 2228), ("1. kv. 2026", 2445), ("2. kv. 2026", 2557), ("3. kv. 2026", 2604)]
add(f"""<div class="kick">Kvadrat novogradnje · Crna Gora</div><h2>Za dve godine<br><span class="gold">+40,5%</span></h2>
<div style="margin-top:56px">{bars(R, 2604*560/470, lambda v: f"{v:,} €".replace(",", "."), hi=lambda v: v == 2604)}</div>
<div class="note">Kvadrat je za dve godine skuplji <b class="gold">750 €</b>. Stan od 50 m²: <b class="gold">+37.500 €</b>.</div>""",
    "Izvor: Monstat, saopštenja 3. kv. 2025, 2. kv. 2026 i 3. kv. 2026 (preliminarni podaci). Promena i stan 50 m²: obračun STANOLOGIJA.",
    alt="Stubičasti grafikon prosečne cene kvadrata novogradnje u Crnoj Gori, evra po m². 3. kvartal 2024: 1.854. 3. kvartal 2025: 2.228. 1. kvartal 2026: 2.445. 2. kvartal 2026: 2.557. 3. kvartal 2026: 2.604 (najviše). Za dve godine plus 40,5%, odnosno 750 € po m², što je 37.500 € za stan od 50 m². Izvor: Monstat; obračun STANOLOGIJA.")

# 4 REGIONI
add("""<div class="kick">Po regionima · 3. kvartal 2026.</div><h2>Gde kvadrat<br><span class="gold">najbrže raste</span></h2>
<table class="tb"><tr><th>Region</th><th>2025.</th><th>2026.</th><th>Za godinu</th></tr>
<tr><td><b>Primorje</b></td><td>2.458 €</td><td><b class="gold">3.192 €</b></td><td class="up">+29,9%</td></tr>
<tr><td><b>Podgorica</b></td><td>2.153 €</td><td><b>2.530 €</b></td><td class="up">+17,5%</td></tr>
<tr><td><b>Sever</b></td><td>1.578 €</td><td><b>1.748 €</b></td><td class="up">+10,8%</td></tr>
<tr><td><b>Središnji</b></td><td>nema prodaje</td><td><b>2.250 €</b></td><td>–</td></tr>
</table>
<div class="note">Na primorju je kvadrat za godinu skuplji 734 €. Kvadrat na primorju je 1.444 € skuplji nego na severu.</div>""",
    "Izvor: " + M1 + "; " + M3 + ". Cene u 3. kvartalu. Promene: obračun STANOLOGIJA. Regionalni proseci zavise od toga koji su stanovi prodati u kvartalu.",
    alt="Tabela cena kvadrata novogradnje u Crnoj Gori po regionima, 3. kvartal 2025. prema 3. kvartalu 2026. Primorje: 2.458 € na 3.192 €, plus 29,9%. Podgorica: 2.153 € na 2.530 €, plus 17,5%. Sever: 1.578 € na 1.748 €, plus 10,8%. Središnji region: u 3. kvartalu 2025. nije bilo prodaje, u 2026. 2.250 €. Na primorju je kvadrat za godinu skuplji 734 €, a 1.444 € skuplji nego na severu. Izvor: Monstat; promene obračun STANOLOGIJA.")

# 5 STRUKTURA
add("""<div class="kick">Gde ide tvojih 2.604 €</div><h2>Zemljište nije<br><span class="gold">krivac</span></h2>
<table class="tb"><tr><th>Deo cene po m²</th><th>2025.</th><th>2026.</th><th>Promena</th></tr>
<tr><td><b>Građenje</b></td><td>1.706 €</td><td><b>1.982 €</b></td><td class="up">+16,2%</td></tr>
<tr><td><b>Ostali troškovi</b></td><td>197 €</td><td><b>315 €</b></td><td class="up">+59,9%</td></tr>
<tr><td><b>Zemljište</b></td><td>325 €</td><td><b>307 €</b></td><td>−5,5%</td></tr>
</table>
<div class="note">Građenje je 76% cene kvadrata. Uređenje zemljišta je čak pojeftinilo. „Ostali troškovi” su PDV, naknade, priključci, projekat i kamate.</div>""",
    "Izvor: " + M1 + "; " + M3 + ". Cena građenja uključuje i dobit investitora (Monstat metodologija). Udeo i promene: obračun STANOLOGIJA.",
    alt="Tabela strukture cene kvadrata novogradnje u Crnoj Gori, 3. kvartal 2025. prema 3. kvartalu 2026. Građenje: 1.706 € na 1.982 €, plus 16,2%. Ostali troškovi (PDV, naknade, priključci, projekat, kamate): 197 € na 315 €, plus 59,9%. Uređenje građevinskog zemljišta: 325 € na 307 €, minus 5,5%. Građenje čini 76% cene kvadrata od 2.604 €. Izvor: Monstat; obračun STANOLOGIJA.")

# 6 USPORAVANJE
add("""<div class="kick">Dobra vest? Delimično</div><h2>Rast se<br><span class="gold">usporava</span></h2>
<div class="duo">
<div class="c"><div class="n">1. → 2. kvartal</div><div class="g">+4,6%</div><div class="t">2.445 → 2.557 €/m²<br>Podgorica +4,8%</div></div>
<div class="c h"><div class="n">2. → 3. kvartal</div><div class="g">+1,8%</div><div class="t">2.557 → 2.604 €/m²<br>Podgorica +0,8%</div></div>
</div>
<div class="note">Sporiji rast nije pad. I u ovom „mirnom” kvartalu stan od 50&nbsp;m² poskupeo je <b class="gold">2.350 €</b> za tri meseca.</div>""",
    "Izvor: " + M2 + "; " + M3 + ". Podgorica 2.395 → 2.510 → 2.530 €/m². Promene i stan 50 m² (50 × 47 €): obračun STANOLOGIJA.",
    alt="Dve kartice o kvartalnom rastu cene kvadrata novogradnje u Crnoj Gori. Od 1. do 2. kvartala 2026: plus 4,6% (2.445 na 2.557 € po m²), Podgorica plus 4,8%. Od 2. do 3. kvartala 2026: plus 1,8% (2.557 na 2.604 € po m²), Podgorica plus 0,8%. Sporiji rast nije pad: i u ovom kvartalu stan od 50 m² poskupeo je 2.350 € za tri meseca. Izvor: Monstat; obračun STANOLOGIJA.")

# 7 REGION EX-YU
add("""<div class="kick">A u komšiluku?</div><h2>Kvadrat novogradnje<br><span class="gold">u regionu</span></h2>
<table class="tb"><tr><th>Zemlja</th><th>Period</th><th>€/m²</th><th>Za godinu</th></tr>
<tr><td><b>Hrvatska</b></td><td>1. pol. 2026.</td><td><b>2.994 €</b></td><td class="up">+8,7%</td></tr>
<tr><td><b>Crna Gora</b></td><td>3. kv. 2026.</td><td><b class="gold">2.604 €</b></td><td class="up">+16,9%</td></tr>
<tr><td><b>BiH</b></td><td>3. kv. 2026.</td><td><b>1.656 €</b></td><td class="up">+8,2%</td></tr>
</table>
<div class="note">Crna Gora je jeftinija od Hrvatske, ali kvadrat joj raste skoro duplo brže. Zagreb: 3.518 €/m² (+18,9%).</div>""",
    "Izvor: DZS, Cijene prodanih novih stanova, 1. pol. 2026 (7.9.2026); Monstat 3. kv. 2026; BHAS 3. kv. 2026 (3.238 KM; preneli Klix i Face.ba, 20.11.2026; 1 € = 1,95583 KM). Metodologije se razlikuju.",
    alt="Tabela prosečne cene kvadrata novogradnje u regionu, poslednji zvanični podaci. Hrvatska, 1. polugodište 2026: 2.994 € po m², plus 8,7% za godinu. Crna Gora, 3. kvartal 2026: 2.604 €, plus 16,9%. BiH, 3. kvartal 2026: 1.656 € (3.238 KM), plus 8,2%. Crna Gora je jeftinija od Hrvatske, ali joj kvadrat raste skoro duplo brže. Zagreb: 3.518 € po m², plus 18,9%. Izvori: DZS, Monstat, BHAS; metodologije se razlikuju.")

# 8 ZAKLJUCAK
add("""<div class="kick">Šta iz ovoga sledi</div><h2>Čekanje<br><span class="gold">nije besplatno</span></h2>
<div class="li">Za godinu dana stan od 50&nbsp;m² poskupeo je <b>18.800&nbsp;€</b>. To je više od dve prosečne godišnje kirije u CG.</div>
<div class="li">Rast je usporio na <b>+1,8%</b> kvartalno, ali cene i dalje idu gore, ne dole.</div>
<div class="li">Najbrže skače <b>primorje (+29,9%)</b>. Ako kupuješ za život, a ne za sezonu, Podgorica i sever su i dalje jeftiniji.</div>""",
    "Izvor: Monstat 3. kv. 2025, 2. kv. 2026 i 3. kv. 2026; kirija: Estitor, 3. kv. 2026, prosečna oglasna kirija u CG 715 €/mes. (× 12 = 8.580 €; × 2 = 17.160 €). Obračun STANOLOGIJA. Ovo nije prognoza cena.")

# 9 CTA
add("""<div style="margin-top:120px"><div class="kick">Pre nego što kažeš „sačekaću”</div>
<h1 style="font-size:96px">+16,9% za<br><span class="gold">godinu dana</span></h1>
<div class="lead">Pošalji ovo nekome ko čeka da stanovi u Crnoj Gori pojeftine.</div>
<div class="tag">Prati @stanologija · sutra: mere i standardi u stanu</div></div>""")

d.render(HERE, extra_css=EXTRA)
contact_sheet(HERE, N, "/tmp/claude-0/-home-claude-stanologija-slike/c1185a26-389b-5993-b6b2-d59325dc7fa4/scratchpad/sheet.jpg")
