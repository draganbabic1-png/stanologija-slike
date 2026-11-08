# STANOLOGIJA - dnevni playbook

Svaki dan: jedan carousel za Instagram @stanologija (faceless profil o stanovima i nekretninama, region ex-YU).
Claude istražuje, pravi slajdove i caption, šalje Draganu na odobrenje. **Objava tek kad Dragan napiše "objavi".**

## Pravila sadržaja (obavezno)
- Nikad ne izmišljati podatke. Svaki broj ima izvor (sitno na slajdu + u captionu).
- Razdvojiti činjenicu, procenu i mišljenje (procene označiti kao procene).
- Prednost podacima iz poslednjih 12 meseci; datum podatka uvek naveden.
- Sopstveni obračuni označeni "Obračun STANOLOGIJA" sa formulom.
- Jezik: srpski, latinica. Ton: stručan ali pristupačan, bez praznih fraza, malo duhovit.

## Stubovi i rotacija tema (ne ponavljaj stub dva dana zaredom)
1. Tržište (cene, kirije, trendovi, gradski okršaji Beograd/Zagreb/Ljubljana/Sarajevo/Podgorica/Skoplje, plata vs stan)
2. Standardi i dimenzije (pravilnici, ergonomija: kuhinja, vrata, visine, kupatilo) - jak stub, izvor = pravilnik/Neufert
3. Edukacija / pravni (kupovina stana korak po korak, skriveni troškovi, porez na prenos, kapara, uknjižba)
4. Enterijer i opremanje (praktično, sa brojevima)
5. Kuriozeti (istorija gradnje, rekordi, mitovi vs istina)
Pogledaj `posts/LOG.md` da izbegneš ponavljanje i izbalansiraš stubove.

## Tehnički tok
1. Repo: `draganbabic1-png/stanologija-slike` (dodaj u sesiju sa add_repo, access push; kloniraj u /home/claude/stanologija-slike).
2. Folder: `posts/YYYY-MM-DD-kratka-tema/` sa `build.py`, `caption.txt`, `01.jpg..NN.jpg`.
3. Slajdovi: kopiraj obrazac iz `posts/2026-11-kirije-beograd/build.py`; alat `tools/stanologija.py` (Deck, bars, eur, contact_sheet).
   - 1080x1350 JPEG, 6-9 slajdova. Slajd 1 = hook (pitanje/broj), poslednji = CTA (komentar/sačuvaj/podeli).
   - Brend: tamno plava #0E2133, zlatna #E6B256, krem #F4EFE6; Oswald (naslovi), Montserrat (tekst).
   - Posle rendera napravi contact_sheet i POGLEDAJ ga (Read) - proveri preklapanja teksta i izvora.
4. Caption: max 2200 znakova; hook, ključni brojevi, CTA, izvori, 10-15 hashtagova (#stanologija prvi).
5. Commit + push na main. Proveri da svaki raw link vraća 200 image/jpeg:
   `https://raw.githubusercontent.com/draganbabic1-png/stanologija-slike/main/posts/<slug>/NN.jpg`
6. Pošalji Draganu slike (SendUserFile) + ceo caption (SendUserMessage) + push notifikaciju. Čekaj "objavi".
7. Na "objavi": Windsor.ai, connector `instagram`, account `17841478090435807`, action `create_carousel_post`
   sa `image_urls` (raw linkovi po redu) i `caption`. Upiši media id u `posts/LOG.md` i push.

## Komentari
Pre nove teme pogledaj komentare na prethodnim objavama (Windsor get_data, connector instagram) i predloži Draganu odgovore. Ne objavljuj odgovore bez odobrenja.
