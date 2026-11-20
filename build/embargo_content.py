# -*- coding: utf-8 -*-
"""„Embargo” (Katharsys, rozdz. „Into the Wild”, scenariusz startowy) — adaptacja na Degenesis 2.0.
Streszczenie i teksty do czytania napisane od nowa własnymi słowami. Zmiany względem oryginału opisane w rozdziale 0."""

def read(txt):
    return f'<blockquote class="d2-read"><p>{txt}</p></blockquote>'

def gm(txt):
    return f'<div class="d2-gmnote"><p>{txt}</p></div>'

def box(title, rows):
    return f"<h3>{title}</h3><ul>" + "".join(f"<li>{r}</li>" for r in rows) + "</ul>"

ADVENTURE = [
("0. Zanim zaczniesz", """
<p><b>Embargo</b> to oficjalny scenariusz startowy z podręcznika Katharsys, przerobiony na zasady Degenesis 2.0. Wystarcza na 1–2 sesje (5–8 godzin) dla 3–5 postaci. Dzieje się na rubieżach Protektoratu w Borce: w przydrożnej karczmie <b>Tumbler</b> i w ruinach magazynów, gdzie ukryto tajną bazę Kronikarzy zwaną <b>Wektorem</b>.</p>
<p>To przygoda o pułapce, która nie była zastawiona na bohaterów. Drużyna wchodzi w środek cudzej wojny o fałszywe pieniądze i musi zrozumieć, kto naprawdę stoi po drugiej stronie, zanim będzie za późno.</p>
<h3>Struktura</h3>
<table><tr><th>Akt</th><th>Sceny</th><th>Nastrój</th><th>Mapa</th></tr>
<tr><td>I. Karczma</td><td>1. Tumbler · 2. Iskry · 3. Spowiedź Tokena</td><td>dziwna gościnność, nagła przemoc</td><td>Tumbler — osada, Tumbler — izba</td></tr>
<tr><td>II. Ruiny</td><td>4. Labirynt runów · 5. Fałszywa Alkowa</td><td>śledztwo, napięcie, eksplozja</td><td>Ruiny magazynów i Wektor</td></tr>
<tr><td>III. Dzicz</td><td>6. Zjazd · 7. Dzicz Kowala</td><td>ciemność, polowanie, pułapki</td><td>Wektor — hala (Dzicz)</td></tr>
<tr><td>IV. Wektor</td><td>8. Wnętrze · 9. Spalarnia i finał</td><td>zasadzki, prawda, wybór</td><td>Wektor — wnętrze i spalarnia</td></tr></table>
<h3>Co jest w module</h3>
<ul><li><b>Sceny</b>: 5 map z siatką 1 m (osada, izba, ruiny, hala, wnętrze Wektora).</li>
<li><b>Aktorzy</b>: 12 postaci niezależnych z portretami i żetonami, wataha Gendo jako Banda, Śledztwo z tropami i zegarami, 4 Lokacje z Cechami, 3 Frakcje, Rejestr Długów.</li>
<li><b>Dzienniki</b>: ta przygoda, „Szkoła MG: Embargo” (jak to poprowadzić krok po kroku) i handouty dla graczy.</li></ul>
<h3>Zmiany względem oryginału</h3>
<ul><li><b>Śmiertelność.</b> W podręczniku nieudany skok w szybie zabija na miejscu. W 2.0 śmierć grozi tylko przy <b>Stawce Śmierci</b>, którą ogłaszasz z góry, więc upadek to ciężka rana i Konsekwencja (szczegóły w scenie 6). Jeśli grupa chce gry bardziej zabójczej, ogłoś Stawkę przed skokiem.</li>
<li><b>Merl.</b> W oryginale dwunastoletnia Merl jest „żoną” Sędziego Magnusa. Zmieniliśmy to: Merl jest jego <b>podopieczną</b>, którą rodzina Dacrois „oddała mu pod opiekę”, żeby przywiązać Sędziego do karczmy. Niepokój zostaje — dziwna, zaborcza rodzina i człowiek prawa, który dał się kupić miską mięsa — ale bez wątku dziecięcego małżeństwa.</li>
<li><b>Mechanika.</b> Profile przeliczone na 2.0 (pule, Próg, skala NPC). Testy z Trudnością 4 i 6 zostawiliśmy jako 3–4, bo w 2.0 drabina wyników daje „Tak, ale…”.</li>
<li><b>Dodatki 2.0</b> oznaczone [2.0]: Cechy miejsc, tropy kluczowe, zegary, Dług i Imię, nagrody w PD.</li></ul>
""" + gm("Źródło: Katharsys, scenariusz „Embargo” (s. 340–353 w numeracji podręcznika). Ten moduł to prywatna adaptacja do gry przy twoim stole — nie rozpowszechniaj go publicznie. Oryginalne mapy można pobrać ze strony degenesis.com; w module są mapy narysowane od nowa.")),

("1. Prawda (tylko MG)", """
<h3>Kto, co i dlaczego</h3>
<p><b>Nullify</b>, Scalar Kronikarzy, od lat działa w cieniu Klastra. Uważa, że kto kontroluje Drafty, ten kontroluje Kronikarzy i cały cywilizowany świat. Postanowił złamać algorytm, którym Klaster zabezpiecza każdy banknot. Na linii przesyłu danych między dwiema dużymi Alkowami urządził tajną bazę — <b>Wektor</b> — w dawnym, zautomatyzowanym magazynie kontenerów. Jego ludzie (Fuse'owie i Shutterzy) oczyścili okoliczne ruiny ze Złomiarzy: pokryli mury <b>fałszywymi runami</b> „wszystko wyczyszczone”, a tych, którzy przejrzeli podstęp, zabili. Jednym z nich był Złomiarz <b>Draff</b>.</p>
<p>Gdy maszyny Nullify'a zebrały dość kodów, Scalar zrobił próbę: zamiast kazać zabić Złomiarza, który przyszedł pod Wektor, zapłacił mu <b>wydrukowanymi u siebie Draftami</b>. Tym Złomiarzem był <b>Kowal</b>, legenda z Borki, Niedźwiedź Jaskiniowy. Fałszywki szybko wyszły na jaw. Klaster nałożył na Kowala <b>embargo</b> — najcięższą urzędową karę Kronikarzy: żadna Alkowa nie kupi od niego artefaktu, jego twarz wisi obok zabójców Kronikarzy. Nullify zrozumiał, że próba się nie udała, wrócił do Klastra poprawiać algorytm i zapomniał o Złomiarzu.</p>
<p><b>Kowal nie zapomniał.</b> Wydusił prawdę z Kronikarza w słabo strzeżonej Alkowie, odnalazł Wektor, wymordował obsługę bazy i zastawił pułapkę. Ściągnął <b>Giadę</b>, Apokaliptyczną Kukułkę udającą Kronikarkę, i kazał jej płacić fałszywkami każdemu, kto przyniesie znalezisko. Chce, żeby fałszywe Drafty znów krążyły — żeby ten, kto je wymyślił, przyszedł posprzątać. Wtedy Kowal go dopadnie.</p>
<h3>Jak to się zazębia z postaciami</h3>
<ol><li>Kilka dni temu <b>Jatzek</b>, niezbyt rozgarnięty syn karczmarzy Dacrois, znalazł w ruinach artefakt i dostał za niego od „Kronikarki” (Giady) garść Draftów.</li>
<li>W południe zapłacił nimi w karczmie. Resztę wydano <b>Tokenowi</b>, samotnemu Kronikarzowi z pobliskiej Alkowy. Token zeskanował banknot — i alarm poszedł do Klastra. Zdradził w ten sposób rodzinę, z którą żyje od lat.</li>
<li>Sygnał odebrał Nullify. Wysłał <b>Case'a</b>, swojego Fuse'a, z dwoma Shutterami: mają po cichu usunąć ślady fałszywek, zanim ruszy oficjalne śledztwo Klastra.</li>
<li>Postacie przyjeżdżają do Tumblera akurat wtedy, gdy Shutterzy siedzą w izbie — i Jatzek wraca z kolejną garścią Draftów.</li></ol>
<h3>Kto czego chce</h3>
<table><tr><th>Kto</th><th>Chce</th><th>Boi się</th><th>Sekret</th></tr>
<tr><td>Kowal (Złomiarz)</td><td>dopaść twórcę fałszywek i odzyskać imię</td><td>że nigdy się nie oczyści</td><td>zabił obsługę Wektora; bierze dziwne specyfiki z Brennen</td></tr>
<tr><td>Giada (Apokaliptyczka)</td><td>wyjść z tego żywa i dobrze zarobić</td><td>Case'a; że Kowal ją poświęci</td><td>jest Kukułką; zna plan Kowala</td></tr>
<tr><td>Case (Fuse)</td><td>zatrzeć ślady przed Klastrem</td><td>gniewu Nullify'a</td><td>pracuje dla zdrajcy Klastra</td></tr>
<tr><td>Token (Kronikarz)</td><td>uratować Dacroisów i siebie</td><td>Klastra i wstydu</td><td>to on wywołał alarm; „artefakt” dla drużyny to bomba</td></tr>
<tr><td>Magnus (Sędzia)</td><td>świętego spokoju i pełnej miski</td><td>prawdziwej walki</td><td>nie ma ani jednego naboju</td></tr>
<tr><td>Mama Dacrois</td><td>sprzedać jedzenie, chronić syna</td><td>obcych</td><td>wie więcej o Jatzeku, niż mówi</td></tr></table>
""" + gm("Nullify nie pojawia się w tej przygodzie. Siedzi w Justitian i nadaje się na przeciwnika całej kampanii: działa przez pośredników, sprawdza bohaterów zleceniami, a ujawni się dopiero, gdy drużyna zacznie mu zagrażać.")),

("2. Scena 1: Tumbler", read("Droga od kilku dni ciągnie się przez nic. Wreszcie przy rozjeździe stoi przekrzywiona tablica z wypalonym napisem: TUMBLER. Za nią, w zagłębieniu między wydmami pyłu, rozciąga się długi, niski budynek z dymiącym kominem. Z otwartych drzwi niesie się brzęk garnków i zapach pieczonego mięsa. Obok stoi coś na kształt kapliczki z blachy i anten — Alkowa Kronikarzy. Nad wszystkim góruje drewniana wieża strażnicza.") +
 read("Na szczycie wieży ktoś stoi. Szeroki kapelusz, twarz w cieniu, lufa karabinu wycelowana prosto w was.") + """
<p><b>Rzut (opcjonalny):</b> INT+Legendy (Trudność 2) — ktoś kiedyś wspominał o gorzelni o tej nazwie na skraju Protektoratu. Czasy świetności ma za sobą.</p>
<h3>Wieża i Sędzia Magnus</h3>
<p>Jeśli postacie pomachają, postać na wieży odmacha. Po chwili po drabinie schodzi z sapaniem otyły Sędzia. Na dole opiera się na karabinie i łapie oddech, nie spuszczając przybyszy z oczu. Za nim zwinnie zeskakuje blada dziewczynka, może dwunastoletnia, i staje w jego cieniu.</p>
""" + read("Grubas ociera pot z czoła rękawem, rozmazując kurz. Uśmiecha się szeroko. — Magnus. Sędzia miejski Magnus. — Głos ma cichy, miękki, prawie miły. Kładzie dłoń na karku dziewczynki. — A to Merl, moja mała. Moja rodzina. Nie gap się tak, kochanie. — Drzwi karczmy skrzypią. Chuda kobieta o długich, białych włosach macha do was z progu. — Zapraszamy! — woła. Magnus rozkłada ramiona. — Nalegamy. Prawda, że nalegamy? — Nachyla się do was konspiracyjnie. — Jest mięso!") + """
<h3>Izba</h3>
""" + read("W środku jest ciemnawo i duszno. Kurz wisi w smugach światła. W kącie siedzi dwóch ludzi i w milczeniu wpatruje się w garnek z mięsem. Górne połowy ich twarzy, od kości policzkowych po linię włosów, są czarne od sadzy. Głowy mają niedbale ogolone, kosmyki zwisają im na czoła.") + """
<p>To dwaj <b>Shutterzy</b>, wysłani przez Case'a na zwiad. INS+Percepcja (3) przy podejściu: na czołach mają wzór linii, może kod kreskowy Kronikarzy, a z płatka ucha każdego wycięto kawałek wielkości paznokcia. Jeśli ktoś do nich podejdzie, patrzą pusto i odwracają się bez słowa.</p>
<p><b>Mama Dacrois</b> sadza gości i stawia miski z mięsem w ciemnym sosie. Ma blisko osadzone oczy, oblizuje wargi i za każdym razem stoi odrobinę za blisko. — Sama zarżnęłam. Dobre? Jeszcze? — Jedzenie jest w porządku, trochę kwaskowe. To Gendo. Magnus z Merl wychodzą: „Mamy robotę”.</p>
<p><b>Alkowa:</b> postacie mogą od razu zajrzeć do <b>Tokena</b> — sprzedać złom albo wypytać o okolicę. Jeśli przyjdą przed sceną 2, Token jest roztrzęsiony. INS+Empatia (2): to poczucie winy. Zapytany, burczy, że „inni Kronikarze zawsze go denerwują”, i kiwa głową w stronę karczmy.</p>
<h3>Cechy miejsca [2.0]</h3>
<ul><li><b>Ciasna izba pełna butelek</b> (jawna) — każda walka w środku coś rozbija.</li>
<li><b>Wieża strażnicza nad drogą</b> (jawna) — widać z niej ruiny na północy i każdego, kto nadchodzi.</li>
<li><b>Piwnica Ojca Dacrois</b> (ukryta) — tam rozbiera się Gendo; schody za ladą, hak, beczki solanki.</li></ul>
<h3>Tropy</h3>
<ul><li><b>Kluczowy:</b> dwaj obcy przy stole to Kronikarze bez masek, Shutterzy — w zwykłej karczmie nie mają czego szukać.</li>
<li><b>Odsłona:</b> Token jest roztrzęsiony od rana i nie wychodzi z Alkowy (Ostrzeżenie); ruiny na północy kiedyś roiły się od Złomiarzy, a od dwóch zim nikt tam nie chodzi (Szczegół).</li></ul>
""" + gm("Daj tej scenie oddychać. Gracze powinni poczuć, że coś tu jest „nie tak”: za dużo uśmiechów, za mało gości, Sędzia bez naboi, dziewczynka, która patrzy za długo. Nie odpowiadaj na to wprost. Niepokój to twoje główne narzędzie w akcie I.") + "<p><b>Mapa:</b> Tumbler — osada, potem Tumbler — izba. <b>Odgłosy:</b> „Pochmurny dzień”, w izbie „Wnętrze budynku”.</p>"),

("3. Scena 2: Iskry", read("Ledwo zdążyliście się rozsiąść, gdy drzwi uderzają o ścianę. Wpada wielki, zwalisty chłopak o okrągłej, miękkiej twarzy i biegnie do lady. — Mama! — głos ma głuchy, bez wyrazu. — Zrobiłem Drafty! — Wyciąga z kieszeni całe garście banknotów i rzuca je na blat. Mama Dacrois przegląda je drżącymi rękami. — Jatzek… — gładzi go po policzku. — Coś ty zrobił? Chłopak odwraca się do izby. Oczy błyszczą mu z radości. — Zarobiłem — mówi i wydyma usta.") +
 read("— Też chciałbym wiedzieć. — Ten głos jest twardy i chrapliwy. Jeden z umorusanych sadzą podrywa się od stołu, dopada Jatzeka i bije go w twarz. — Coś ty zrobił? — Nie czeka na odpowiedź. Bije znowu, goni chłopaka wzdłuż lady. Drugi wstaje, staje między wami a nimi i unosi dłoń. — Nie wasza sprawa. — Pierwszy wyciąga Shocker. Iskry. Krzyk. Jatzek pada przed ladą i trzęsie się, buty tłuką o deski. — Zostawcie mnie! — Matka krzyczy „nie, nie!”, ale nie śmie wyjść zza lady.") + """
<p>Ojciec Dacrois jest w piwnicy i rozbiera tuszę Gendo. Zanim zrozumie, co się dzieje na górze, będzie za późno.</p>
<h3>Jeśli postacie się nie wtrącą</h3>
<p>Shutterzy katują Jatzeka Shockerami, aż przestanie się ruszać. Nie spodziewają się odpowiedzi — uznali, że jakaś dzika rodzina obrabowała Wektor. Teraz sprzątają i wracają do Justitian. <b>Zegar „Czystka Case'a” +2.</b></p>
<h3>Jeśli pobiegną po Magnusa</h3>
<p>Magnus za karczmą uczy Merl trzymać młotek. Walczyć nigdy nie umiał, a lata miski mięsa nie pomogły, ale w kryzysie się nie zawiesza: łapie młotek i drepcze do karczmy. Pomoże, ale to kosztuje czas, którego Jatzek nie ma (<b>Koszt: Jatzek otrzymuje ranę Krytyczną</b>, chyba że ktoś inny działał w środku).</p>
<h3>Jeśli wejdą do walki</h3>
<ul><li><b>Zastraszenie:</b> pierwszy Shutter wrzeszczy: — Spieprzać, dziwolągi! Starcie: jego PSY+Dominacja 6K przeciw PSY+Wiara/Wola każdej postaci, która chce działać. Przegrany traci pierwszą rundę i Ego równe Wyzwalaczom Shuttera.</li>
<li><b>Runda 1:</b> jeden Shutter kopie stoły i krzesła pod nogi atakujących (Cecha „Przewrócone stoły” z darmowym wywołaniem przeciw wejściu w zwarcie: −2K). Atakuje Shockerem każdego w zasięgu.</li>
<li>Drugi przeskakuje ladę i chwyta Mamę Dacrois jako tarczę: <b>Obrona +2 przeciw strzałom</b> do niego [2.0: w podręczniku +3]. Po rundzie skręca jej głowę — kobieta krzyczy z bólu. Jeśli postacie natychmiast się nie cofną, ogłusza ją kolbą i rzuca w nie.</li>
<li><b>Ucieczka:</b> żaden Shutter nie chce tu umierać. Po drugiej rundzie albo pierwszej ranie Poważnej obaj uciekają do ruin, do Case'a (zegar „Czystka Case'a” +1, Shutterzy wrócą w finale).</li></ul>
<h3>Cechy [2.0]</h3>
<ul><li><b>Butelki za ladą</b> — każdy chybiony strzał w izbie zasypuje ladę szkłem i wódką (wywołanie: oślepić, podpalić, poślizgnąć).</li>
<li><b>Ojciec Dacrois z tasakiem w piwnicy</b> (ukryta) — wołany po imieniu wbiega w rundzie 3.</li></ul>
""" + gm("Shocker w 2.0: trafienie nie zadaje ran, tylko odbiera Ego równe 2 + Wyzwalacze. Przy 0 Ego trafiony pada na rundę i dygocze. To idealne do tej sceny: groza bez trupów. Jatzek ma 4 Ego — trzy celne ciosy i jest w stanie krytycznym.") + "<p><b>Mapa:</b> Tumbler — izba. <b>Żetony:</b> Shutter ×2, Jatzek, Mama Dacrois.</p>"),

("4. Scena 3: Spowiedź Tokena", """
<h3>Wielkie znalezisko Jatzeka</h3>
<p>Nawet jeśli Jatzek przeżyje, jest w szoku i cofa się przed każdym obcym. Rodzice stoją bezradnie i nie przeszkadzają, gdy ktoś próbuje z nim rozmawiać. <b>INS+Empatia (3).</b> Porażka: chłopak młóci rękami i ucieka w kąt. Sukces: uspokaja się i odpowiada prostymi zdaniami:</p>
""" + read("— Nie ukradłem. Znalazłem coś. Wiem, nie wolno chodzić do pułapek. Ale tam znalazłem. Pani Kronikarka powiedziała, że to znalezisko. Chciała. Zapłaciła. Mama z tatą mieli dać klientom. Nie ukradłem!") + """
<p>Jatzek był w Wektorze i dostał stos fałszywych Draftów za artefakt. Kowal chciał zwabić winowajcę — i mu się udało. Chłopak mógłby zaprowadzić drużynę na miejsce, ale jest wyczerpany. Mama Dacrois odsyła go do łóżka.</p>
<h3>Token przychodzi sam</h3>
<p>Żyje czy nie, historia toczy się dalej, bo Token wszystko widział. Poci się, dyszy, zdziera z siebie maskę. Jeśli drużyna nie przyjdzie do Alkowy, wybiega za nimi w łopoczącej pelerynie i prosi, żeby poszli z nim. Załamując ręce, opowiada wszystko — pomija tylko skomplikowane szczegóły. Słowa się z niego wylewają:</p>
""" + read("— To dobrzy ludzie. Oni nic nie zrobili. Jatzek nic nie zrobił, to jeszcze dziecko! … Miał niezarejestrowane Drafty. Tak, pewnie fałszywe. Klaster jest zaalarmowany. Nie odpuści. Ci dwaj w karczmie to dopiero początek czystki. Przyjdą następni… — W oczach stają mu łzy.") + """
<p>Zapytany, skąd Klaster wie, wije się i w końcu przyznaje: zeskanował banknot, żeby sprawdzić, kto jeszcze kupuje tu artefakty, i to uruchomiło zabezpieczenia.</p>
""" + read("— Ale możemy to naprawić. — Nachyla się i szepcze. — Potrzebuję tylko dowodu. Idźcie do tej fałszywej Alkowy i sprzedajcie im to. — Wskazuje na stół: paczka wielkości kota, owinięta taśmą, z kikutami anten. — Weźcie Drafty, przynieście mi je. Zeskanuję, zgłoszę fałszerza Klastrowi. Problem rozwiązany.") + """
<h3>Artefakt jest bombą</h3>
<p>„Odbiornik zerowy, odłączony od Strumienia” to w rzeczywistości ładunek wybuchowy, uruchamiany sygnałem z dowolnego stołu analitycznego w Alkowie. Z zewnątrz nie da się tego poznać, a gruba warstwa taśmy zniechęca do rozpakowania. Podejrzliwym Token mówi, że urządzenie wyśle mu sygnał, gdy dotrze na miejsce.</p>
<ul><li><b>INS+Empatia (3)</b> przeciw jego PSY+Oszustwo (2K): Token coś ukrywa w sprawie paczki. Dwa Wyzwalacze: boi się jej.</li>
<li><b>INT+Artefakty (4)</b> albo rozpakowanie: to bomba. Token przyznaje się, płacząc, i błaga, żeby ją jednak podłożyli: „Oni zabiją Dacroisów!”.</li></ul>
<h3>Jeśli drużyna odmówi</h3>
<p>Token na to nie pozwoli. Z rozpaczy woła Magnusa, a ten przekonuje postacie (CHA+Negocjacje 6K, Postawa ich wobec sprawy Nieufna), że tylko one mogą odwrócić gniew Klastra od Tumblera. W ostateczności Token idzie sam — i ginie w ruinach, a Shutterzy wracają do karczmy nocą (zegar „Czystka Case'a” +2).</p>
<h3>Nagrody tej sceny [2.0]</h3>
<ul><li>Przyjęcie zadania: <b>dług Poważny</b> Tokena wobec drużyny (Rejestr Długów).</li>
<li>Uratowanie Jatzeka: Imię u rodziny Dacrois +1.</li></ul>
""" + gm("To pierwszy moment wyboru moralnego. Token nie jest złym człowiekiem — jest przerażony i postąpił głupio. Graj go jako kogoś, kto sam nie wierzy, że robi dobrze. Jeśli gracze odkryją bombę, nie karz ich: daj im wybór, czy ją podłożyć, i niech ten wybór zmieni finał (patrz scena 9).")),

("5. Scena 4: Labirynt runów", """
<p>„Fałszywa Alkowa” leży w zespole magazynów niedaleko. Token opisał drogę, ale mógł być dokładniejszy: opis prowadzi do kompleksu, ale nie do wejścia.</p>
""" + read("Hale stoją rzędami jak wielkie, zapomniane trumny. Na ich płaskich dachach rosną drzewa i wyciągają gałęzie w niebo jak rozcapierzone palce. Z gałęzi zwisa suchy mech. Korzenie oplatają ściany i nigdzie nie sięgają ziemi. W cienistych przesmykach między halami gęstnieją krzaki. Każda ściana jest pokryta runami Złomiarzy.") + """
<h3>Runy</h3>
<p>Złomiarz w drużynie: <b>INT+Legendy (1)</b>.</p>
<ul><li><b>Sukces:</b> tu musiało być wielkie szukanie. Wiele run jest nieznanych i powinny być stare, a nie są porośnięte porostem. Ktoś wyrył je niedawno — i bardzo wielu „młodych Złomiarzy”. Część run ostrzega przed niebezpieczeństwem.</li>
<li><b>1 Wyzwalacz:</b> znaki są niechlujne i niespójne. Żaden Złomiarz nie robi tak byle jak.</li>
<li><b>2 Wyzwalacze:</b> tylko jedna runa jest prawdziwa: należy do <b>Draffa</b>, znanego Złomiarza, którego od lat nikt nie widział w Justitian. Wszystkie inne to fałszywki.</li></ul>
<h3>Ślady</h3>
<p><b>INS+Orientacja (3)</b> albo <b>INS+Przetrwanie (3)</b>: ślady ciężkiego, powłóczącego nogami człowieka — pewnie Jatzeka. Dwa Wyzwalacze: kilkudniowe ślady wysokiego mężczyzny i kobiety, a między nimi tropy Gendo, raz pod, raz nad śladami mężczyzny — zwierzęta szły razem z nim. Ślady prowadzą prosto do Wektora.</p>
<h3>Punkt widokowy</h3>
<p>Po korzeniach da się wspiąć na dachy (CIA+Atletyka 2). Z góry widać betonowy budynek wyrastający ponad hale w środku kompleksu. Dachy są zarośnięte, częściowo zawalone, połączone zwalonymi pniami. Kto idzie górą, dostrzega w przesmyku sylwetkę mężczyzny, który zauważa, że jest obserwowany, i znika w jednej z hal. <b>To był Case.</b></p>
<h3>Grób Złomiarza</h3>
<p>W halach jest trochę starych instalacji: można z nich wyciągnąć 2K kg złomu techniki IV. I szkielet. Tył czaszki spalony, włosy skręcone i stopione, kości pokryte śladami zębów. Do plecaka przywiązano kilka metalowych płytek z tą samą runą, która jest na murach: runą Draffa. Przy zwłokach leży przerobiony rewolwer z sześcioma nabojami kalibru .50.</p>
<p>Spitalianin lub inny medyk, <b>INT+Medycyna (3)</b>: taką ranę mógł zadać tylko mocny Shocker.</p>
<h3>Cechy [2.0]</h3>
<ul><li><b>Fałszywe runy na każdej ścianie</b> (jawna).</li>
<li><b>Dachy połączone pniami</b> (jawna) — droga górą: cicho i z widokiem, ale łatwo spaść.</li>
<li><b>Grób Draffa</b> (ukryta) — odkrycie daje Odsłonę „Powiązanie”: ktoś zabija Złomiarzy, którzy tu zaglądają.</li></ul>
""" + gm("To scena-nagroda dla uważnych graczy. Nic tu nie atakuje, ale każda informacja zmienia to, co zobaczą dalej. Jeśli ktoś znajdzie grób Draffa i zestawi to z Shockerami Shutterów, ma już połowę prawdy. Zapisz to jako trop na aktorze Śledztwa.") + "<p><b>Mapa:</b> Ruiny magazynów i Wektor. <b>Odgłosy:</b> „Noc — wiatr”.</p>"),

("6. Scena 5: Fałszywa Alkowa", read("Hala Wektora otoczona jest białymi betonowymi wspornikami, o które opierają się wydmy pyłu, zarośnięte suchymi krzakami jak falujące morze. Przed bramą jest pusty plac, po którym tańczą wiry kurzu, rysując spirale i zakręty. Brama jest tak szeroka, że wjechałby nią czołg, ale z zewnątrz widać tylko czarną dziurę. W ciemności mruga kaskada czerwonych i białych świateł.") + """
<p>Tu ślady Jatzeka znikają — wiry pyłu zjadają każdy odcisk w kilka godzin. Kto obejdzie halę, zauważa:</p>
<ul><li>na dachu sieć anten i drutów, kołyszących się na wietrze jak dziwne rośliny;</li>
<li>z boku stalowe drzwi bez klamki i panelu; pył przed nimi był kiedyś odgarnięty, ale już wraca;</li>
<li>w szczelinach między wspornikami ślady dłuta — ktoś wydrążył beton na trzy dłonie, ale nie przebił lśniącej, białej siatki wewnątrz; na jednym wsporniku runa Draffa.</li></ul>
""" + read("Z bramy bucha suche gorąco i silny zapach spalonego drewna. Przeciskacie się w półmroku między stosami blach i beczek ku migającym światłom na końcu hali. Zanim cokolwiek widać, wita was piskliwe, zniekształcone „Witamy!” z Vocodera. Szkielet kontenera wisi na pęku stalowych lin nad czarną jak smoła dziurą. Ścianę od waszej strony wycięto i zastąpiono kratą z okienkiem. W środku jest zimne światło i Kronikarz, który poprawia maskę, jakby była na niego za duża. Za nim stół analityczny, jaki znacie z innych Alkow.") + """
<p>Czarno-żółte boje znaczą krawędź szybu, przedramię od kontenera. Postacie mogą podejść i pokazać artefakt Tokena. „Kronikarz” (Giada) otwiera okienko, bierze paczkę, kładzie ją na stole. Światła migają, żółta lampka pulsuje. Wraca dwoma długimi krokami, kuca i podaje garść Draftów.</p>
""" + read("Paczka trzeszczy i tyka. Kronikarz odwraca się i mówi wysokim, kobiecym głosem: — Co do… — Błysk rozrywa artefakt i stół. Huk trzęsie kratą, a kontener dzwoni jak gong. Kronikarz uderza o pręty i osuwa się na podłogę, Vocoder piszczy w crescendo. W kontenerze błyskają czerwone światła i cały zjeżdża w dół. Na drugim końcu hali brama zaczyna się zamykać, prostokąt światła maleje. Biegniecie, ale nie zdążycie. Brama zatrzaskuje się z łoskotem. Ciemność.") + """
<p>Postacie wpadły w pułapkę Kowala. Dla niego wybuch to dowód, że właściciele Wektora wrócili po swoje. Jest gotowy.</p>
<h3>Co można zrobić w ciemności</h3>
<ul><li>Jedyne światło to czerwona poświata z szybu. Bez źródła światła — dotyk i −2K do wszystkiego, co wymaga wzroku.</li>
<li>W kontenerach są deski, liny stalowe, blachy.</li>
<li>Brama to masywny beton: nie do ruszenia. Mechanizm jest na zewnątrz, kabel biegnie przez halę i znika w szybie.</li>
<li>W szybie, 30–40 kroków niżej, leży fałszywa Alkowa, otwarta od góry, wciąż podpięta liną do sufitu jarzmem. W środku widać silnik.</li>
<li>Kto widział drzwi bez klamki: hala w środku jest mniejsza, niż wydawała się z zewnątrz — drzwi prowadzą do części, do której stąd nie ma dojścia.</li></ul>
""" + gm("Jeśli gracze odkryli bombę i jej nie podłożyli, Giada i tak ich wpuszcza — Kowal od rana czeka na „właścicieli”. Zamiast eksplozji: Giada bierze paczkę, a Kowal zrzuca kontener w dół i zamyka bramę ręcznie. Efekt ten sam, ale drużyna ma bombę w ręku na później.") + "<p><b>Mapa:</b> Ruiny magazynów i Wektor, potem Wektor — hala. <b>Odgłosy:</b> „Podziemia, kanały”; na wybuch — „Grzmot” z Efektów.</p>"),

("7. Scena 6: Zjazd", """
<p>Postacie są uwięzione w hali. Jedyna droga prowadzi w dół. Są dwie możliwości.</p>
<h3>Wspinaczka</h3>
<p>Stalowa lina wisi około dwóch kroków od krawędzi szybu. Da się do niej doskoczyć (<b>CIA+Atletyka 3</b> albo <b>ZRĘ+Mobilność 3</b>) i zjechać (ten sam test). Ostrożni mogą zbudować most z desek i blach z przeciwwagą: <b>INT+Inżynieria (3)</b> i nie trzeba skakać. Zjeżdżający mogą sobie pomagać: postać, która już stoi pewnie, oddaje sukcesy temu, komu brakuje.</p>
<h3>Technika</h3>
<p>Przy ścianie jest awaryjny panel windy, zablokowany przez nadpisanie. Dobry technik otworzy go i usunie blokadę: <b>INT+Inżynieria (4)</b>. Z szarpnięciem winda rusza i da się nią sterować.</p>
<h3>Upadek w 2.0 [zmiana]</h3>
<p>W podręczniku nieudany test oznacza śmierć. W 2.0 bez ogłoszonej <b>Stawki Śmierci</b> nikt tu nie ginie:</p>
<ul><li><b>Tak, ale…</b> — łapie linę w ostatniej chwili: Lekka rana od otartych dłoni albo upuszczony sprzęt.</li>
<li><b>Nie</b> — spada kilka metrów na jarzmo kontenera: rana Poważna i wisi bezradnie, dopóki ktoś go nie wyciągnie.</li>
<li><b>Nie, i…</b> — spada na dno szybu: rana Krytyczna i Konsekwencja (np. złamana noga — do końca przygody −2K do ruchu, albo zgubiona broń).</li></ul>
<p>Jeśli twoja grupa chce grozy, ogłoś Stawkę Śmierci <i>przed</i> pierwszym skokiem. Wtedy „Nie, i…” zabija.</p>
<h3>Na dole</h3>
""" + read("Kontener uderzył w dno w chmurze pyłu i papierów. Dym snuje się między prętami. Po Kronikarzu nie ma śladu. W uchwycie przy stole wisi latarka. Gdy świecicie przez kratę, widzicie halę ciągnącą się w ciemność: szerokie betonowe filary z czerwonymi numerami, niebieskie i zielone kontenery, mgłę pyłu. Lance światła przebijają dziurkowaną tylną ścianę windy. W smugach rysuje się sylwetka.") +
 read("— Mam was. — Głos jest głęboki i dudniący. Coś ciężkiego uderza w stalową ścianę. — Nikt nie robi w konia Kowala. Przegięliście. — Sylwetka się porusza. — Teraz poznacie moją Dzicz. — Światło przygasa, cień zlewa się z ciemnością. Kroki się oddalają.") + """
<p>Latarka: jeśli nikt nie przymocuje jej do ramienia, trzymający ma −1K w walce.</p>
""" + gm("Postacie myślą teraz, że Kowal to szaleniec, który na nie poluje. Kowal myśli, że to ludzie Nullify'a. Oba przekonania są błędne — i to jest serce tej przygody. Pozwól graczom próbować z nim rozmawiać. Na razie tylko kręci głową. Zmieni zdanie dopiero w spalarni (scena 9).")),

("8. Scena 7: Dzicz Kowala", """
<h3>Zdobycz</h3>
<p>Postacie nie są same. Słychać drapanie i tupot dookoła, rozdzielające się na boki. Gdy pierwszy raz zaświecą przez kratę, coś skacze na pręty: paszcza, kły wbite w siatkę, pazury rysujące metal. <b>Gendo.</b> Chude, cuchnie chorobą i Sepsą. Cofa się i drugim skokiem przelatuje nad kratą do środka windy.</p>
<p>Można je atakować przez kraty albo odpychać. Kto nie zareaguje szybko, walczy z dzikim, ale osłabionym Gendo (profil: aktor „Gendo — wychudzone”). Z otwartych właśnie klatek wybiegają kolejne, ale jeszcze nie atakują — wataha czeka na chwilę słabości. W końcu trzeba opuścić windę: jedną ścianę da się odryglować i odchylić. Od tej chwili <b>wataha poluje na drużynę w całej Dziczy</b>.</p>
<h3>Dzicz</h3>
<p>To, co Kowal nazywa „Dziczą”, to labirynt kontenerów, gór złomu, kanistrów, beczek i pojazdów — wszystkiego, co ludzie Nullify'a wyrzucili z kontenerów, szukając artefaktów. Kowal przygotował tu pułapki i „pamiątki z pustkowi”. Ciągła groźba ataku watahy: do tej pory Gendo są ostrożne, ale gdy zdobycz zacznie się wymykać, rzucą się.</p>
<h3>Wyjście</h3>
<p>Kto przeszuka ściany, dostrzega wysoko schody biegnące wzdłuż jednej ściany hali, coraz wyżej, aż do drzwi. Podnóże schodów jest na drugim końcu hali.</p>
<h3>„Tędy”</h3>
<p>Na kontenerach wielkie białe napisy „TĘDY” ze strzałkami. Kto im nie ufa i idzie inaczej, wpada w pułapkę. Dwadzieścia kroków dalej stoi „Kronikarz” sprzed chwili — bez maski widać, że to kobieta. <b>Giada.</b> Przyciska coś do piersi, między palcami żółte światło. Gdy postacie podejdą, wciska guzik, upuszcza to i ucieka.</p>
<p>Na sąsiednim kontenerze Kowal zebrał złom. Linką odpala obciążnik, który uderza w tę ścianę złomu — lawina. Unik: <b>ZRĘ+Mobilność (3)</b> albo <b>CIA+Atletyka (3)</b>. Porażka: 4 obrażenia (pancerz chroni) [2.0: w podręczniku 1K]. Kto idzie za strzałkami „TĘDY”, wpadnie w tę samą pułapkę gdzie indziej.</p>
<p>Kolejna strzałka („TU, GÓRĄ”) jest mniej łaskawa: prowadzi po blachach na dachy kontenerów. Jeśli łączne <b>CIA wszystkich postaci na górze wynosi 9 lub więcej</b>, kruchy metal pęka z trzaskiem i najcięższa postać zapada się po pas. Gendo czują słabość i atakują jej nogi od środka kontenera. Drużyna musi się rozdzielić.</p>
<h3>Pułapki [jako Ruchy MG]</h3>
<p>Kowal chce drużynę rozbić i zmęczyć, więc posyła Giadę, żeby uruchamiała pułapki. Możesz dodawać własne, ale nie każda musi działać — może Gendo dopadnie Giadę, a ta będzie musiała uciekać albo bronić się Shockerem. Każdą pułapkę traktuj jak <b>Ruch MG</b>: zapowiedz zagrożenie (skrzypienie, żółte światło) i daj graczom szansę zareagować.</p>
<h3>Most suwnicy</h3>
<p>Im bliżej środka hali, tym więcej kontenerów. Drogę zastawia most suwnicy, której silnik i tor osadzono wysoko w ścianie. Dawno temu przenosiła kilka kontenerów naraz. Dziś z chwytaków zwisa dziesięć kontenerów, jak gigantyczne dzwonki wietrzne. Siedem jest poza zasięgiem, ale trzy niskie tworzą wiszący most przed ścianą z kontenerów, spięty blachami i linami. Na dole po lewej wejście po rusztowaniu ze złomu, na górze po prawej most kończy się na szczycie ściany kontenerów.</p>
""" + read("Ledwo zaczynacie się wspinać, z głośników dudni głos Kowala: — Chcecie wrócić do swojej starej nory. Zatrzeć ślady. To wyślę wam waszego kumpla. — Na górze znów widzicie Giadę. Przebiega po deskach, kontenery kołyszą się pod jej krokami. Wyciąga kogoś i pcha przed sobą po linie prowadzącej. Postać sunie ku wam coraz szybciej, nogi bezwładnie uderzają o blachy, ręce przyciśnięte do boków, kaptur łopocze na wietrze.") + """
<p>Na wiszącym moście prawie nie ma miejsca na unik. Pierwsza postać: <b>ZRĘ+Mobilność (3)</b> [2.0: w podręczniku 4]. Jeśli odskoczy, może trafić następną — każdy rzuca. Trafiony spada 3–4 metry: Lekka rana, ale na dole czekają Gendo. Jeśli wszyscy zrobią unik, „pocisk” trafia pierwsze Gendo, które z przetrąconym karkiem wyje na dnie hali.</p>
""" + read("Kaptur spada z twarzy. To trup Kronikarza przywiązany drutem do liny. W płatku ucha brakuje mu trójkąta wielkości paznokcia — dokładnie jak u Shutterów w karczmie.") + """
<p>Jeśli postacie odeprą część watahy, Gendo porzucają trudną zdobycz i rzucają się na zwłoki Kronikarza.</p>
<h3>Wataha w 2.0</h3>
<p>Gendo działają jako <b>Banda</b> (aktor „Wataha zdziczałych Gendo”, rozmiar 5): jeden atak na rundę z premią za liczebność, każda rana zabiera 1–2 zwierzęta. Uciekają przy 3 stratach albo ogniu. Pojedyncze Gendo, które wskoczyło do windy, to osobny aktor.</p>
<h3>Cechy [2.0]</h3>
<ul><li><b>Ciemność i pył</b> (jawna) — bez światła −2K do wszystkiego, co wymaga wzroku.</li>
<li><b>Wataha krąży</b> (jawna) — kto zostaje sam, jest celem.</li>
<li><b>Strzałki „TĘDY” prowadzą w pułapki</b> (ukryta; INS+Percepcja 3 albo ktoś, kto zna Apokaliptyków).</li>
<li><b>Głośniki i kamery Kowala</b> (ukryta) — on widzi wszystko; zniszczenie kamer odbiera mu przewagę.</li></ul>
""" + gm("Prowadź Dzicz jak horror, nie jak lochy. Nie rysuj od razu całej mapy — odsłaniaj ją latarką (w Foundry: Token Vision, Mgła i światło na żetonie z latarką). Rozdzielenie drużyny w pękniętym kontenerze to najmocniejszy moment aktu. Daj każdej połówce scenę po kolei, a zegar zagrożenia niech tyka dla obu.") + "<p><b>Mapa:</b> Wektor — hala (Dzicz). <b>Odgłosy:</b> „Podziemia, kanały”.</p>"),

("9. Scena 8: Wnętrze Wektora", """
<h3>Jaskinia Niedźwiedzia</h3>
<p>Ze szczytu ściany widać, że postacie stoją na klifie. Przed nimi rozciąga się wyspa dachów kontenerów. Mniej więcej pośrodku rusztowanie sięga sufitu, a stamtąd w dół, do kontenerów, schodzi wiązka kabli. Przy tylnej ścianie kładka prowadzi na podest pod drzwiami wyjściowymi — zamkniętymi, bez widocznego mechanizmu, tak jak od zewnątrz.</p>
<p>Kto się rozejrzy, znajduje włazy: dachy kontenerów wycięto i odłożono krzywo. Stoją tu setki kontenerów. Shutterzy Nullify'a wycięli ich ściany i przekopali się na wylot, wybierając radia, ekrany, skrzynie kamer i komputery wielkości dłoni. Stary magazyn krył ogromny skarb, ale Nullify nie chciał go sprzedać — musiałby go wymienić na Drafty Kronikarzy. Zamiast tego zaczął łamać ich kod.</p>
<h3>Wnętrze</h3>
""" + read("Wnętrze Wektora to sam szkielet. Zostało kilka ścian, tam gdzie wycięto podłogę, biegną stalowe kratownice. Gdzieniegdzie widać przez nie serce bazy — spalarnię, w której płomień drga między żółtym ogniem a niebieskimi promieniami. Bucha żar. Gdy przechodzicie obok, ekrany ożywają z trzaskiem i pokazują w szybkich seriach ziarniste zdjęcia: ogromny Złomiarz w Alkowie, nad jego głową czerwony napis EMBARGO. Na innych ten sam człowiek przed bramą Wektora, podpisany: OBIEKT PRÓBNY 1, 3000 DRAFTÓW. W rogach siedzą kamery jak przerośnięte owady. Na ekranach widzicie samych siebie.") + """
<h3>Drukarka Draftów</h3>
<p>W jednym bloku kontenerów stoi drukarka wielkości stołu. Mruga jak stroboskop i wypluwa Drafty pokryte symbolami zamiast liczb. Z sufitu zwisają kable, ściany oblepione pożółkłym papierem z liniami, wzorami i schematami: mapa kodu Draftów. <b>INT+Nauka (4)</b> [2.0: w podręczniku 6]: kod liczy się z kilku danych — miejsca, czasu, numeru Kronikarza i wartości banknotu. Kronikarz w drużynie, który to zrozumie, dostaje <b>+1 do Sekretów</b> (Zaplecze).</p>
<p><b>Wniosek [2.0]:</b> to dobry moment, by gracze połączyli tropy (Drafty Jatzeka, fałszywe runy, grób Draffa, zdjęcia EMBARGO, drukarka). Prawidłowa teoria: „ktoś z Kronikarzy drukował tu fałszywki, wrobił w nie Kowala, a Kowal zastawił pułapkę na niego, nie na nas”. MG odpowiada „ciepło” i dodaje fakt: Kowal ma na ekranie zdjęcia Case'a sprzed tygodnia.</p>
<h3>Zasadzka</h3>
<p>Wektor to labirynt otwartych pomieszczeń, krętych korytarzy i ramp, a każdy kąt ma kamerę. Kowal czai się za rogami albo zeskakuje przez włazy w suficie za plecami wrogów, atakuje i znika, zatrzaskując za sobą klapy, albo skacze przez dziury piętro niżej. Jego kroki dudnią po blachach i niosą się echem.</p>
<ul><li><b>Atak z zaskoczenia:</b> zaatakowana postać może się bronić aktywnie (1 Ego): Starcie <b>PSY+Refleks</b> albo <b>CIA+Broń biała</b> (wyższa pula) przeciw jego ataku. Wygrana z 3 Wyzwalaczami — kontratak.</li>
<li>Do walki zmusisz go tylko, wykorzystując bazę:
<ul><li>obserwując ekrany i kamery, drużyna znajduje bezpieczne korytarze (mniej okazji do zasadzki);</li>
<li>zablokowane włazy odcinają mu drogi ucieczki;</li>
<li>zniszczone kamery oślepiają go;</li>
<li>jeśli drużyna się rozdzieli, Kowal schodzi do walki jeden na jeden — a w pojedynkę jest prawie nie do pokonania.</li></ul></li>
<li>Pierwsze sukcesy pokaż, pozwalając komuś kontratakować, zanim Kowal znów zniknie. Kowal zrywa ekrany z uchwytów i rzuca nimi, przewraca kondensatory, które suną po kratownicy, sypiąc iskrami, ciągnie łańcuchy, opuszczając płyty sufitu między sobą a drużyną.</li>
<li>Gdy postacie w końcu przejmą teren, rzucają w <b>Starciu CIA+Atletyka</b> z Kowalem, żeby go dogonić i osaczyć. Pościg prowadzi do spalarni.</li></ul>
<h3>Cechy [2.0]</h3>
<ul><li><b>Kamery i ekrany</b> (jawna) — Kowal widzi drużynę; drużyna, jeśli patrzy, widzi jego.</li>
<li><b>Włazy w suficie i podłodze</b> (jawna).</li>
<li><b>Pulpit w spalarni steruje wszystkim</b> (ukryta) — bramy, światła, winda, drzwi wyjściowe.</li></ul>
""" + gm("Zegar „Gniew Kowala” (4): każda udana zasadzka +1. Gdy się zapełni, Kowal przestaje się bawić i atakuje otwarcie najsłabszą postać. Każde sprytne wykorzystanie bazy (kamery, włazy) cofa zegar o 1. To daje graczom jasny sygnał, że gra się sprytem, nie siłą.") + "<p><b>Mapa:</b> Wektor — wnętrze i spalarnia.</p>"),

("10. Scena 9: Spalarnia i finał", read("Kilka kontenerów przerobiono na piec. W żarze widać białe od gorąca szkielety krzeseł i szafek, ramy pochylone krzywo w płomieniach. Nad ogniem wiszą panele obłożone kwadratowymi kafelkami ceramiki — zbierają żar i zamieniają go w prąd. Cała ściana to pulpit, w którym zbiegają się wszystkie kable. Dźwignie z tabliczkami, oznaczenia białą i niebieską farbą, symbole.") + """
<p>Giada już tu jest. Chowa się za Kowalem i mówi cicho, opanowanym głosem: — Nie podoba mi się to, Kowal. Kowal całuje ją w policzek, nie spuszczając oczu z drużyny. — Idź. Giada przestawia dźwignię. Na jednym z ekranów błyska jasny prostokąt: otwierają się drzwi wyjściowe. Giada stoi jeszcze sekundę, zgrzytając zębami, i odchodzi.</p>
""" + read("Kowal nie atakuje od razu. — Trzeba było zadrzeć z kimś innym — mówi. Na wszystko, co mówicie, tylko kręci głową. Na ekranach widać Giadę uciekającą przez Wektor. Kowal się uśmiecha. — Widać naprawdę nie może być gorzej. — I rusza na was.") + """
<h3>Zwrot</h3>
<p>W trakcie walki, dokładnie w chwili, gdy jedna ze stron zaczyna wygrywać, na ekranie w jasnym prostokącie drzwi pojawia się sylwetka. Kowal ryczy: — Ty sk…! Zostawia drużynę i pędzi obok niej ze spalarni. Maska wyższości pęka, przez szczeliny widać strach.</p>
<ul><li>Jeśli postacie go teraz zatrzymają, nigdy im tego nie wybaczy. Jeśli przeżyje, kiedyś wróci dokończyć walkę.</li>
<li>Jeśli go puszczą, mają cień szansy na dobre zakończenie i Kowala jako sojusznika.</li></ul>
<h3>Case</h3>
<p>Case wchodzi do Wektora drzwiami awaryjnymi. Giada biegnie prosto na niego i nie ma szans z Fuse'em. Kto pobiegnie za Kowalem, widzi Giadę cofającą się przed Case'em na podeście; ten mierzy do niej z pistoletu maszynowego. Kowal biegnie na podest, wrzeszcząc bez przerwy. Od drużyny do Case'a jest niewiele ponad 40 metrów w linii prostej. Jeśli nikt go nie rozproszy, Case pociągnie za spust i skosi Giadę, zanim Kowal dobiegnie. Tylko strzał w Case'a teraz może odwrócić losy — trafienie odrzuci Fuse'a i da Kowalowi czas.</p>
<h3>Czyściciele</h3>
<p>Cokolwiek się stanie, Case wycofuje się na zewnątrz. Jeśli jego Shutterzy przeżyli karczmę, są przy nim. Zaczyna się ostatnia walka. Kowal walczy sam, jeśli jeszcze może — ale drużyny już nie atakuje.</p>
""" + read("Gdy Case pada, od strony ruin nadchodzi tłum Kronikarzy. Ponad dwudziestu, wśród nich Paradygma w lśniącym kombinezonie. Wszyscy mają Shockery albo Cascadery, napięci, gotowi do walki. Jeden z nich biegnie przodem i zdejmuje maskę. To Token. — Spokojnie — mówi. — To my jesteśmy ci dobrzy. — W oczach ma łzy ulgi.") + """
<p>Drużyna musi wyjaśnić, co się stało, ale Token za nią poręczy. Jeśli postacie same nie rozumieją wszystkiego, Paradygma wspomni o embargu i wyjaśni, że opierało się na użyciu fałszywych pieniędzy.</p>
<h3>Jeśli drużyna ma bombę Tokena [2.0]</h3>
<p>Bomba, której nie podłożyli, może zakończyć walkę z Case'em jednym rzutem (rzucona: 10 obrażeń w promieniu 3 m, −1 za metr) — albo zostać dowodem przeciw Tokenowi przed Paradygmą. To ich wybór i ich Dług.</p>
<h3>Walka w 2.0</h3>
<ul><li><b>Kowal</b> (antagonista, Próg 10): topór rzeźniczy 11 obrażeń; Wyzwalacze mogą zamiast obrażeń powalić. Na ataki mentalne odporny (pula 10, „stoik”).</li>
<li><b>Case</b> (weteran, Próg 5): pistolet maszynowy 7 obrażeń, seria (3). Ucieka, gdy dostanie ranę Poważną i nie ma już Shutterów.</li>
<li><b>Giada</b> (weteran): nie chce walczyć. Shocker, pule ZRĘ 8, CIA 5.</li></ul>
""" + gm("Finał opiera się na jednym wyborze: czy drużyna zrozumie, że Kowal nie jest jej wrogiem. Wszystko, co zebrali po drodze (runy, Draff, ekrany, drukarka), ma ich do tego doprowadzić. Jeśli zabiją Kowala w spalarni, przygoda i tak się kończy — ale stracą najciekawszego sojusznika kampanii.")),

("11. Zakończenie i nagrody", """
<p>Drużyna wyszła z pułapki, która nie była na nią zastawiona. Razem z Tokenem wyjaśniła Paradygmie, co działo się w Wektorze i jaką rolę grał Kowal. Kronikarze przejmą bazę, a fałszywe Drafty znikną z obiegu. Ale Nullify uciekł — i nie jest zadowolony, że ktoś mu przeszkodził. To dopiero początek.</p>
<h3>Nagrody w 2.0</h3>
<table><tr><th>Za co</th><th>PD</th><th>Dług i Imię [2.0]</th></tr>
<tr><td>Udział (za każdą sesję)</td><td>5</td><td>—</td></tr>
<tr><td>Jatzek przeżył</td><td>+1</td><td>Imię u rodziny Dacrois +1; Tumbler jako baza</td></tr>
<tr><td>Mama Dacrois cała</td><td>+1</td><td>—</td></tr>
<tr><td>Shutterzy już nikogo nie będą katować</td><td>+1</td><td>—</td></tr>
<tr><td>Kowal ocalony</td><td>+2</td><td><b>dług Krwawy</b> Kowala wobec drużyny</td></tr>
<tr><td>Giada ocalona</td><td>+1</td><td>Kowal jako sojusznik: Złomiarz w drużynie +1 Sojusznicy, inni +1 Sieć</td></tr>
<tr><td>Odkryta tajemnica Wektora (Wniosek)</td><td>+2</td><td>Imię u Kronikarzy +1</td></tr>
<tr><td>Zabicie legendarnego Kowala</td><td>—</td><td>Sława +1 dla zabójców; Imię u Złomiarzy −1</td></tr></table>
<p>Zaplecze rośnie tylko przez fikcję — powyższe zmiany to właśnie takie wydarzenia.</p>
<h3>Tumbler jako baza</h3>
<p>Mieszkańcy Tumblera są w swojej samotności trochę dziwni, ale to dobrzy, przyjaźni ludzie, wdzięczni za pomoc. Drużyna może tu odpoczywać między przygodami i leczyć rany, a nawet stać się częścią tej rodziny: chronić to miejsce i nazywać je domem. Im częściej postacie wracają, tym bardziej się przywiązują. Atak na Tumbler to atak na nie. Jeśli ktoś stąd zniknie, będą go szukać.</p>
<h3>Co dalej (haki na kampanię)</h3>
<ul><li><b>Nullify</b> zapamiętał drużynę. Zaczyna od zleceń przez pośredników, żeby poznać jej słabości.</li>
<li><b>Kowal</b> ma dług Krwawy albo urazę na całe życie. Jedno i drugie wróci.</li>
<li><b>Token</b> poręczył za drużynę przed Paradygmą — Klaster może o tym pamiętać w obie strony.</li>
<li><b>Ciche studnie</b>: Justitian jest kilka dni drogi stąd. Modus (Kronikarz z gotowych postaci) może dostać od Paradygmy zlecenie, które zaprowadzi drużynę do dzielnicy Dostawców.</li></ul>
"""),

("12. Legendy o Kowalu", """
<p>Gdy postacie pierwszy raz usłyszą imię Kowala, mogą sprawdzić, co o nim wiedzą: <b>INT+Legendy (2)</b>. Postacie z Borki +1K, Złomiarze mogą dodać Sekrety jako kości. Za sukces jedna plotka, za każdy Wyzwalacz kolejna (losuj albo wybieraj).</p>
<ol><li>W spelunce w Justitian pobił sześć Wron Bojowych, które oszukały go w karty. Jednemu odgryzł palce.</li>
<li>Doszedł do półfinału walk w dole. Rzucił przeciwnikiem o ścianę tak, że ten już się nie ruszył. Do finału nie stanął — po prostu zniknął na pustkowiach.</li>
<li>Jego jaskinie są dobrze ukryte. Znaczy je kamieniem wielkości pięści z wyrytą swoją runą. Jak zobaczysz taki kamień — uciekaj.</li>
<li>Rzadko chodzi sam. Wie, na co go stać i w czym potrzebuje pomocy.</li>
<li>Kronikarze wyjęli go spod prawa. Od tamtej pory nikt go nie widział.</li>
<li>Wiele zim temu zadawał się z jakimś konowałem z Brennen, dzielnicy Justitian. Te mięśnie na pewno nie są naturalne.</li>
<li>Szybko nudzą go towarzysze. Wyjątkiem jest jedna Apokaliptyczka.</li>
<li>Jest pod embargiem — najcięższą urzędową karą Kronikarzy. Żadna Alkowa nic od niego nie kupi.</li></ol>
"""),

("13. Zegary, frakcje, długi [2.0]", """
<h3>Zegary (na aktorze Śledztwo)</h3>
<ul><li><b>Czystka Case'a</b> (6, start 1): +1 za każdą godzinę zwłoki, +2 jeśli Jatzek umrze w karczmie, +1 jeśli Shutterzy uciekną. Na 3: Case wie o drużynie. Na 6: Case i Shutterzy napadają nocą na Tumbler, żeby „posprzątać świadków”.</li>
<li><b>Gniew Kowala</b> (4, start 0): +1 za każdą udaną zasadzkę w Wektorze. Pełny — Kowal atakuje otwarcie najsłabszą postać. −1 za sprytne użycie kamer, włazów, ekranów.</li>
<li><b>Kronikarze nadchodzą</b> (8, start 2, jawny dla graczy dopiero po spowiedzi Tokena): +1 na scenę. Pełny — Paradygma przybywa do Wektora (finał).</li></ul>
<h3>Frakcje (aktorzy)</h3>
<ul><li><b>Klaster Kronikarzy (Token, Paradygma)</b> — Imię 0. Chce oczyścić system z fałszywek.</li>
<li><b>Ludzie Nullify'a (Case, Shutterzy)</b> — Imię −1 po karczmie. Chcą zatrzeć ślady.</li>
<li><b>Kowal i Giada</b> — Imię −1 na start (myślą, że drużyna to wrogowie). Mogą skoczyć na +2 w finale.</li></ul>
<h3>Rejestr Długów (startowo ukryte)</h3>
<ul><li>Token → drużyna: Poważny („Weźcie paczkę do fałszywej Alkowy”).</li>
<li>Kowal → drużyna: Krwawy (jeśli uratują Giadę albo jego).</li>
<li>Rodzina Dacrois → drużyna: Poważny (jeśli uratują Jatzeka).</li></ul>
"""),
]

GM_SCHOOL = [
("1. Przygotowanie (30 minut)", """
<ol><li><b>Przeczytaj rozdział 1 „Prawda”.</b> Musisz wiedzieć, kto co zrobił, zanim gracze zaczną zgadywać. Reszta przygody to konsekwencje tych pięciu faktów.</li>
<li><b>Zaimportuj moduł</b> (przycisk w zakładce Dzienniki albo prawym na kompendium → Import All Content). Dostaniesz foldery „Embargo” w Scenach, Aktorach i Dziennikach.</li>
<li><b>Otwórz aktora „Śledztwo: Fałszywe Drafty”.</b> Tropy kluczowe są tam wypisane. Zegary ustaw na start (Czystka 1, Kronikarze 2).</li>
<li><b>Ustaw sceny</b>: Tumbler — osada aktywna. Mapy Wektora są przyciemnione. Jeśli chcesz pełnej ciemności, w konfiguracji sceny włącz <i>Token Vision</i> i <i>Fog Exploration</i>, a żetonom postaci daj widzenie i latarkę jako światło (5 m) — ciemność to połowa klimatu.</li>
<li><b>Rozstaw żetony</b>: Magnus i Merl na wieży, Shutterzy przy stole w izbie, Mama Dacrois za ladą.</li>
<li><b>Ustal z graczami ton</b>: przygoda ma przemoc wobec bezbronnych, dziwną rodzinę i trupy. Zapytaj, czego nie chcą przy stole.</li></ol>
"""),
("2. Pierwsze 15 minut", """
<p>Zacznij od drogi. Każdy gracz w jednym zdaniu mówi, skąd wraca jego postać i czego jej brakuje (jedzenia, snu, pieniędzy). To od razu daje powód, żeby zajrzeć do Tumblera.</p>
<p>Przeczytaj tekst z tablicą i wieżą. Wycelowany karabin to test charakteru drużyny: ktoś pomacha, ktoś sięgnie po broń, ktoś się schowa. Wszystko jest dobre — Magnus i tak zejdzie.</p>
<p>W izbie zwolnij. Opisz zapach, kurz, dwóch milczących ludzi z czarnymi twarzami. Pozwól graczom rozmawiać z Mamą Dacrois, zadawać pytania, oglądać Shutterów. Gdy rozmowa zacznie przygasać — wpada Jatzek.</p>
""" + gm("Złota zasada: przemoc w scenie 2 ma być nagła i brzydka. Nie zapowiadaj inicjatywy, dopóki ktoś z graczy nie zdecyduje się działać. Opisz pierwszy cios i zapytaj: co robicie?")),
("3. Jak grać NPC-ów", """
<ul><li><b>Magnus</b> — miękki głos, pot, sapanie. Wszystko robi powoli. Nigdy nie strzela (nie ma naboi), ale celuje do wszystkich. Kocha „rodzinę” Dacrois, bo to pierwsze miejsce, gdzie ktoś go szanuje.</li>
<li><b>Merl</b> — prawie nic nie mówi. Patrzy. Zawsze stoi przy Magnusie. Jeśli gracze zapytają, czy wszystko w porządku, wzrusza ramionami.</li>
<li><b>Mama Dacrois</b> — za blisko, oblizuje wargi, karmi. Jej świat to syn i kuchnia.</li>
<li><b>Jatzek</b> — duże dziecko w ciele olbrzyma. Krótkie zdania bez podmiotu. Dumny z Draftów.</li>
<li><b>Token</b> — mówi szybko, łamie się, załamuje ręce. Kłamie źle. Gdy kłamie, bawi się klamrą peleryny.</li>
<li><b>Shutterzy</b> — prawie nie mówią. Kiedy mówią, rozkazują. Nie chcą tu umierać.</li>
<li><b>Kowal</b> — mało słów, dużo ciszy. Głos z głośników jest spokojny; spokój jest straszniejszy niż krzyk. Powtarza: „Gorzej już nie będzie”.</li>
<li><b>Giada</b> — zawodowiec, który zbyt późno zrozumiał, w co wszedł. Ucieka, nie walczy. W finale można ją przekonać.</li></ul>
"""),
("4. Szyb: jak nie zabić graczy", """
<p>Zjazd do szybu to miejsce, gdzie oryginał zabija. U nas nie, chyba że tak ustalicie. Powiedz to graczom wprost przed skokiem: „Jeśli się nie uda, spadniecie i będzie bolało. Nie umrzecie.” Dzięki temu będą ryzykować, zamiast się zablokować.</p>
<p>Daj im czas na plan. Most z desek, panel windy, lina z asekuracją — każda sensowna propozycja obniża Trudność albo daje +2K (Cecha „Deski i blachy w kontenerach”).</p>
"""),
("5. Dzicz: horror, nie lochy", """
<ul><li>Opisuj dźwięki, zanim pokażesz cokolwiek: tupot, drapanie, oddech.</li>
<li>Pułapki zapowiadaj (żółte światło, skrzypienie) — to <b>Ruchy MG</b>, nie złośliwość. Gracz, który zauważy znak, powinien mieć szansę zareagować.</li>
<li>Gendo atakują tylko słabych i samotnych. Grupa trzymająca się razem z ogniem jest prawie bezpieczna — i powinna to czuć.</li>
<li>Rozdzielenie w pękniętym kontenerze: przeskakuj między grupami co 2–3 minuty gry, zawsze w momencie napięcia.</li></ul>
"""),
("6. Kowal: walka sprytem", """
<p>W Wektorze nie prowadź zwykłej walki rundami, dopóki gracze nie osaczą Kowala. Zasadzka to jeden cios i ucieczka: opisz, rzuć, niech ktoś się broni, Kowal znika. Między zasadzkami pytaj: „Co robicie z bazą?”. Gracze, którzy patrzą w ekrany, blokują włazy i niszczą kamery, cofają zegar „Gniew Kowala” i zmuszają go do walki na ich warunkach.</p>
"""),
("7. Finał i wybór", """
<p>Najważniejsze zdanie przygody to krzyk Kowala, gdy widzi Case'a. Zatrzymaj grę na sekundę i zapytaj: „Kowal biegnie obok was, odsłonięty. Co robicie?”. Wszystko, co gracze zebrali w śledztwie, powinno im teraz pomóc zdecydować.</p>
<p>Po walce zrób krótkie podsumowanie przy wspólnej tablicy tropów: co wiedzieli, czego nie. Przyznaj PD i wpisz długi do Rejestru.</p>
"""),
]

HANDOUTS = [
("Tablica przy drodze", "<p class='d2-read'>TUMBLER — gorzelnia · jadło · nocleg. Pod tablicą ktoś dopisał kredą: <i>mięso codziennie</i>.</p>"),
("Fałszywy Draft", "<p>Banknot Kronikarzy, z pozoru prawdziwy. Kod kreskowy wygląda dobrze, ale skaner Tokena świeci na czerwono: <b>DRAFT NIEZAREJESTROWANY</b>.</p>"),
("Ekran w Wektorze", "<p>Ziarniste zdjęcie: ogromny Złomiarz w Alkowie. Nad jego głową czerwony napis <b>EMBARGO</b>. Na drugim zdjęciu ten sam człowiek przed bramą tej hali: <b>OBIEKT PRÓBNY 1 — 3000 DRAFTÓW</b>.</p>"),
]
