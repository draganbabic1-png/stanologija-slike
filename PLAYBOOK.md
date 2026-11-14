# STANOLOGIJA - dnevni playbook

Svaki dan: jedan carousel + Reel + Story za Instagram @stanologija (faceless profil o stanovima i nekretninama, region ex-YU).
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
   - 1080x1350 JPEG, 6-9 slajdova. Slajd 1 = hook (pitanje/broj, naslov najviše 5-7 reči), poslednji = CTA.
   - CTA uvek traži SLANJE ("Pošalji ovo nekome ko..."), jer su slanja (DM) najjači signal za doseg ka nepratiocima. Komentar/sačuvaj su sekundarni.
   - Brend: tamno plava #0E2133, zlatna #E6B256, krem #F4EFE6; Oswald (naslovi), Montserrat (tekst).
   - Posle rendera napravi contact_sheet i POGLEDAJ ga (Read) - proveri preklapanja teksta i izvora.
   - Reel + Story: `python3 tools/reel.py posts/<slug> --slides 1,a,b,c,N` (4-6 najjačih slajdova: hook, 2-4 ključna broja, CTA; ~13-17 s).
     Pravi `reel.mp4` (1080x1920) i `story.jpg`. Pogledaj bar jedan kadar reela (ffmpeg -ss) pre slanja.
4. Caption: max 2200 znakova. Prva rečenica = hook sa ključnim rečima (pretraga po njima). Ključni brojevi, CTA sa slanjem, izvori.
   NAJVIŠE 5 hashtagova (Instagram limit; hashtagovi ne donose doseg): #stanologija + 4 tematska.
   Reel caption: kraći (do ~600 znakova): hook, 2-3 broja, "Ceo pregled sa izvorima u carousel objavi na profilu", izvori skraćeno, isti hashtagovi.
5. Commit + push na main. Proveri da svaki raw link vraća 200 (image/jpeg za slike, reel.mp4 200 i veličina > 0):
   `https://raw.githubusercontent.com/draganbabic1-png/stanologija-slike/main/posts/<slug>/NN.jpg`
6. Pošalji Draganu slike + reel.mp4 + story.jpg (SendUserFile) + oba captiona (SendUserMessage) + push notifikaciju. Čekaj "objavi".
7. Na "objavi" (Windsor.ai, connector `instagram`, account `17841478090435807`), redom:
   a) `create_carousel_post`: `image_urls` (raw linkovi po redu) + `caption` iz caption.txt.
   b) `create_video_post`: `video_url` = raw link reel.mp4, `caption` iz reel_caption.txt, `share_to_feed` true, `thumb_offset` 0.
   c) `create_story`: `image_url` = raw link story.jpg.
   Upiši media id-jeve (carousel / reel / story) u `posts/LOG.md` i push. Ako jedan korak ne uspe, javi tačno koji i ne ponavljaj ostale.

## Rast (šta algoritam nagrađuje, 2026)
- Slanja u DM > lajkovi za doseg ka nepratiocima; vreme gledanja za Reels. Reels donose doseg, carousel angažman.
- Najviše 5 hashtagova; ključne reči u prvoj rečenici captiona, imenu profila i biu.
- Reel je obavezan svaki dan (glavni izvor dosega ka nepratiocima; nedelja 8-14.11: reel prosek 55 dosega, carousel 8,7).
- Najmanje 2x nedeljno tema vezana za vest staru do 48 h (u okviru rotacije stubova).
- Reel hook: pitanje u 2. licu o novcu ili svakodnevici ("Raste li ti rata...?", "Koliko ti..."), prvi kadar do 6 reči.
- Doslednost: svaki dan, objave razmaknute nekoliko sati ako ih ima više.
- Nedeljni izveštaj (nedelja uveče): doseg, slanja, sačuvano, novi pratioci po objavi, reel vs carousel; zaključak šta ponoviti.

## Komentari
Pre nove teme pogledaj komentare na prethodnim objavama (Windsor get_data, connector instagram) i predloži Draganu odgovore. Ne objavljuj odgovore bez odobrenja.
