<p align="center">
  <img src="docs/assets/banner.svg" alt="dmxON FabKit — od płytki Autodesk Fusion Electronics do kompletnego zamówienia JLCPCB" width="100%">
</p>

<p align="center">
  <a href="https://github.com/AlexSmith2025/dmxON-FabKit-Fusion-Electronics/releases/latest"><img src="https://img.shields.io/github/v/release/AlexSmith2025/dmxON-FabKit-Fusion-Electronics?style=for-the-badge&color=b4744a&label=release" alt="Najnowsza wersja"></a>
  <a href="https://github.com/AlexSmith2025/dmxON-FabKit-Fusion-Electronics/releases"><img src="https://img.shields.io/github/downloads/AlexSmith2025/dmxON-FabKit-Fusion-Electronics/total?style=for-the-badge&color=24574a&label=downloads" alt="Pobrania"></a>
  <img src="https://img.shields.io/badge/Autodesk%20Fusion-Electronics-e2ab7f?style=for-the-badge&logo=autodesk&logoColor=white" alt="Autodesk Fusion Electronics">
  <img src="https://img.shields.io/badge/Windows-10%20%7C%2011-3b4a5a?style=for-the-badge" alt="Windows 10 | 11">
  <a href="https://www.paypal.com/donate/?business=smith.show2025%40gmail.com&no_recurring=0&item_name=dmxON+FabKit&currency_code=EUR"><img src="https://img.shields.io/badge/PayPal-Wesprzyj-003087?style=for-the-badge&logo=paypal&logoColor=white" alt="Wesprzyj przez PayPal"></a>
</p>

<p align="center">
  <a href="https://github.com/AlexSmith2025/dmxON-FabKit-Fusion-Electronics/releases/latest/download/dmxON-FabKit.zip"><img src="https://img.shields.io/badge/%E2%AC%87%20Pobierz-dmxON--FabKit.zip-b4744a?style=for-the-badge" alt="Pobierz najnowszą wersję"></a>
</p>

<p align="center">
  <a href="README.md">English</a> · <a href="README.ru.md">Русский</a> · <a href="README.es.md">Español</a> · <a href="README.de.md">Deutsch</a> · <b>Polski</b>
</p>

<p align="center">
  <a href="#instalacja">Instalacja</a> ·
  <a href="#szybki-start">Szybki start</a> ·
  <a href="#zgodność">Zgodność</a> ·
  <a href="#wynik">Wynik</a> ·
  <a href="#zamówienie-w-jlcpcb">Zamówienie</a> ·
  <a href="#wesprzyj-projekt">Wesprzyj</a>
</p>

**dmxON FabKit to ULP dla Autodesk Fusion Electronics (Fusion 360 Electronics), który w jednym przebiegu zamienia płytkę w kompletne zamówienie JLCPCB: zip z plikami Gerber o nazwach JLCPCB, BOM i CPL z automatycznym doborem części LCSC i zamiennikami, interaktywny raport, dokumentację montażową A4 i arkusze 1:1 do termotransferu.**

<p align="center">
  <a href="https://www.paypal.com/donate/?business=smith.show2025%40gmail.com&no_recurring=0&item_name=dmxON+FabKit&currency_code=EUR"><img src="docs/assets/donate.pl.svg" alt="Wesprzyj dmxON FabKit przez PayPal — smith.show2025@gmail.com" width="760"></a>
</p>

---

## Co robi

| | |
|---|---|
| 🏭 | **Gerber i wiercenie dla JLCPCB**: nazwy GTL/GBL/G1…/GTS/GTP/GTO/GKO/XLN, zip gotowy do wgrania; warstwy i parametry płytki wykrywane automatycznie |
| 🧾 | **BOM i CPL do montażu** z automatycznym doborem części LCSC — rezystory i kondensatory wg wartości, obudowy i napięcia, reszta wg numeru producenta |
| 📐 | **Sprawdzanie footprintów** z biblioteką JLC (EasyEDA): obrót i środek w CPL z dopasowania padów; lustrzane i niepasujące obudowy są oznaczane |
| 🔁 | **Zamienniki**: gdy części brakuje, nie ma jej w magazynie lub obudowa nie pasuje, szukany jest odpowiednik, sprawdzany z padami płytki — wygrywa najtańszy |
| 💲 | **Koszt**: ceny katalogowe dla całej partii, opłaty za podajniki Extended, najdroższe pozycje |
| 📊 | **Raport HTML**: realistyczny widok płytki, przełączanie warstw, galeria Gerber, wiercenie, kontrola wykonalności, rozmieszczenie z oznaczeniami |
| 📄 | **Dokumentacja A4** do montażu ręcznego: strona tytułowa, specyfikacja produkcji, warstwy, rysunki montażowe w skali normowej, kolejność lutowania krok po kroku, klucze układów, BOM; edytowalna tabliczka; PDF |
| 🖨️ | **Termotransfer 1:1**: PDF dla każdej warstwy (miedź, opisy, maska, wiercenie), arkusze górne lustrzane, pasek 50 mm do sprawdzenia skali |
| 📥 | **Import gotowej BOM JLCPCB** (xlsx, csv lub tekst ze strony zamówienia) — Twoje sprawdzone numery mają pierwszeństwo |
| 🌐 | **5 języków**: angielski, rosyjski, hiszpański, niemiecki, polski — okno, raport i cała dokumentacja w wybranym języku |
| 📏 | **Dokumentacja wg ISO lub GOST**: arkusze i tabliczki wg ISO 5457 / ISO 7200 albo GOST R 2.104-2023; wykaz dokumentów, rysunki wykonawczy i montażowy, wykaz części (ISO 7573) lub specyfikacja (GOST R 2.106-2019), wykaz elementów; odwołania do IPC i IEC w uwagach |
| 🔌 | **Schemat elektryczny** z Twojego schematu w ramce normy (GOST Э3 / IEC 61082-1) na A4, A3 lub wydłużonym arkuszu A3×n, tak aby tekst był czytelny |
| 🧩 | **Karta dmxON w Fusion** (dodatek): FabKit, JLC Rules, kopia zapasowa i aktualizacje jednym kliknięciem; Gerber bez okna potwierdzenia CAM |
| 💾 | **Kopia całego folderu projektu**: schematy, płytki i biblioteki jako pliki EAGLE, projekty 3D jako `.f3d`, rysunki jako PDF oraz pakiet — do odtworzenia na dowolnym koncie i komputerze |
| 🔄 | **Aktualizacje z GitHuba**: sprawdzanie raz dziennie, instalacja na żądanie |

---

## Zgodność

| | dmxON FabKit |
|---|---|
| **Autodesk Fusion (Electronics), Windows 10/11** | ✅ sprawdzone na Fusion **2705.1.30** (październik 2026) |
| Autodesk Fusion na macOS | ❌ korzysta z narzędzi Windows (`curl.exe`, `tar.exe`, `robocopy`, Windows Script Host, Microsoft Edge) |
| EAGLE 9.x | ❌ do Gerber potrzebne jest polecenie Fusion `MANUFACTURING EXPORT` |
| KiCad, Altium, EasyEDA | ❌ |

Potrzebne są też: **Microsoft Edge** (wbudowany w Windows) do PDF; internet do katalogu JLCPCB i footprintów EasyEDA (reszta działa offline). Jeśli nowa wersja Fusion coś zepsuje, [zgłoś issue](https://github.com/AlexSmith2025/dmxON-FabKit-Fusion-Electronics/issues).

---

## Instalacja

1. [**Pobierz `dmxON-FabKit.zip`**](https://github.com/AlexSmith2025/dmxON-FabKit-Fusion-Electronics/releases/latest/download/dmxON-FabKit.zip) i rozpakuj w dowolnym miejscu.
2. W Fusion Electronics: **Automation → Run ULP → `INSTALL.ulp`** z rozpakowanego folderu, wybierz język i naciśnij **Zainstaluj**.
3. **Uruchom ponownie Fusion jeden raz.** Edytory płytki i schematu dostaną kartę **dmxON** — FabKit, JLC Rules, Kopia, Aktualizacje, Ustawienia, Pomoc — a `dmxON_FabKit` będzie też w **Run ULP**.

Instalator kopiuje projekt do `Dokumenty\dmxON\dmxON-FabKit` i instaluje **dodatek dmxON** (`%APPDATA%\Autodesk\Autodesk Fusion 360\API\AddIns\dmxON`). Dodatek stawia foldery dmxON na początku list ULP, reguł projektowych i CAM w Fusion (Preferences → General → Electronics → Directory) — wbudowane ULP pozostają — i naprawia te ścieżki po aktualizacjach Fusion. Ponowne uruchomienie `INSTALL.ulp` aktualizuje pliki; **Usuń** kasuje skopiowany projekt, a z ostatnim narzędziem dmxON także dodatek. Bez ponownego uruchomienia dodatek można włączyć: **Utilities → Add-Ins → Scripts and Add-Ins → dmxON → Run**. Ręcznie, bez dodatku: zachowaj cały rozpakowany folder i uruchamiaj `RUN 'C:/ścieżka/dmxON_FabKit.ulp'`.

**Kilka komputerów.** Fusion współdzieli ustawienia — także ustawienia FabKit — między wszystkimi komputerami konta Autodesk. Dlatego dodatek zapisuje foldery jako `$HOME\dmxON\…` i `$EAGLEDIR\…`, które Fusion rozwija na każdym komputerze do jego własnych Dokumentów i folderu programu, a FabKit pomija folder wyjściowy należący do innego komputera (używa `Pulpit\FabKit`). Uruchom `INSTALL.ulp` raz na każdym komputerze (albo **dmxON → Aktualizacje** tam, gdzie karta już jest), aby pliki tam były.

---

## Szybki start

1. Otwórz **płytkę** w Fusion Electronics i **zapisz ją** (Ctrl+S) — Fusion eksportuje Gerber z ostatniej zapisanej wersji.
2. Naciśnij **dmxON → FabKit** (albo **Automation → Run ULP → `dmxON_FabKit`**).
3. W prawym górnym rogu wybierz **normę** (ISO lub GOST) i **język**, folder, i naciśnij **Utwórz pakiet**.
4. Z dodatkiem dmxON i zainstalowanym dmxON JLC Rules Gerber eksportuje się bez okien przez zadanie CAM dmxON JLCPCB. Bez nich Fusion może pokazać okno **CAM Export File List** — naciśnij **OK**.
5. Po około minucie otworzy się folder pakietu. Zacznij od `index.html`. Przy włączonej kopii dodatek zapisze potem cały folder projektu w pakiecie, w `05_BACKUP`.

Wskazówka: najpierw uruchom [**dmxON JLC Rules**](https://github.com/AlexSmith2025/dmxON-JLC-Rules-Fusion-Electronics) — ustawia reguły projektowe JLCPCB i stos warstw oraz przekazuje do FabKit grubość płytki i kolor maski. Oba narzędzia mają wspólne ustawienie języka.

### Okno

| Karta | Co ustawia |
|---|---|
| **Język** (prawy górny róg) | English, Русский, Español, Deutsch, Polski — okno przełącza się od razu; raport i dokumentacja powstają w tym samym języku |
| **Norma** (prawy górny róg) | ISO lub GOST — jaki komplet dokumentacji powstaje; wspólna z dmxON JLC Rules |
| **Wyjście** | folder; kopia folderu projektu; co utworzyć: Gerber, dokumentację, schemat elektryczny, PDF, arkusze do termotransferu; co trafia do BOM/CPL: THT, środek padów, pomijane oznaczenia |
| **Części** | wyszukiwanie w katalogu, Basic/Preferred, zamienniki, sprawdzanie footprintów, ponowna kontrola atrybutów, zapis `LCSC_PART`, liczba płytek, min. napięcie kondensatorów, opłata za podajnik, import BOM |
| **Płytka** | grubość, kolor maski i opisów, wykończenie — do raportu, formularza zamówienia i widoku |
| **Tabliczka** | wyrób, nr dokumentu, wersja (Rev.), klient, uwagi (dla płytki); firma i podpisy (wspólne) |
| **O programie** | wersja, autor, licencja, linki |

Wszystkie ustawienia są zapamiętywane.

---

## Wynik

```
<płytka>_v<wersja>_FabKit/
├── index.html                          strona startowa
├── 01_JLCPCB_ORDER/
│   ├── JLCPCB_GERBER/
│   │   ├── <płytka>_v<wersja>_Gerber_JLCPCB.zip ← wgraj na jlcpcb.com
│   │   └── unpacked/                   te same pliki do podglądu
│   ├── <płytka>_v<wersja>_JLCPCB_BOM.csv ← PCB Assembly: BOM
│   └── <płytka>_v<wersja>_JLCPCB_CPL.csv ← PCB Assembly: CPL
├── 02_REPORT/                          raport + podglądy warstw
├── 03_ASSEMBLY_DOCS/                   dokumentacja wg ISO lub GOST (HTML + PDF)
├── 04_TONER_TRANSFER_1to1/             HOW_TO_PRINT + 7 arkuszy PDF
└── 05_BACKUP/                          kopia całego folderu projektu (dodatek dmxON)
```

Każde uruchomienie **usuwa i tworzy od nowa** pakiet płytki — ale tylko wtedy, gdy folder utworzył FabKit (zawiera znacznik `.dmxon-fabkit`). Obcy folder o tej samej nazwie nigdy nie jest ruszany.

**Jedna wersja wszędzie.** Wersja płytki jest zapisana w projekcie jako atrybut globalny `REV` i ustawiana w polu **Wersja (Rev.)** na karcie **Tabliczka**. Wchodzi do nazwy folderu pakietu i wszystkich plików (`<płytka>_v<wersja>_…`, także plików Gerber w archiwum), do tabliczek ISO i do raportu. Za pierwszym razem FabKit bierze wersję wydrukowaną na płytce (tekst w rodzaju «Ver. 1.4») albo `REV` zapisany wcześniej przez FabKit — `REV` z szablonu ramki (często «A») nie wygrywa z napisem na płytce — i po OK zapisuje ją w projekcie. Raport ostrzega, gdy napis na płytce, `REV` i pakiet się różnią. Pakiety różnych wersji leżą obok siebie; nowe uruchomienie zastępuje tylko pakiet tej samej wersji.

---

## Zamówienie w JLCPCB

1. **jlcpcb.com → Order now → Add gerber file** → `01_JLCPCB_ORDER/JLCPCB_GERBER/<płytka>_Gerber_JLCPCB.zip`.
2. Parametry płytki — z raportu (sekcja «Zamówienie»).
3. **PCB Assembly** → BOM `…_JLCPCB_BOM.csv`, CPL `…_JLCPCB_CPL.csv`.
4. W podglądzie JLCPCB sprawdź części z sekcji raportu **«Wymagają uwagi»**.

### Numery części — kolejność pierwszeństwa

1. **Import BOM** (karta Części lub `-import plik`).
2. **Atrybut** części: `LCSC_PART`, `LCSC`, `JLCPCB_PART`, `JLC` …
3. **Wyszukiwanie w katalogu JLCPCB**: R/C wg wartości, obudowy i napięcia; reszta wg numeru producenta z wartości lub atrybutu `MPN` / `MANUFACTURER_PART_NUMBER`.
4. **Zamiennik**, gdy części brakuje, nie ma jej w magazynie lub obudowa nie pasuje.

Przydatne atrybuty: `JLC_PACKAGE`, `JLC_ROTATION`, `JLC_COMMENT`, `VOLTAGE`, `DNP` / `JLC_EXCLUDE`, `BOM=EXCLUDE`. Własne przypisania obudów i obrotów — `config/fk_package_map.txt`.

---

## Termotransfer

Arkusze powstają z **tych samych plików Gerber**, które trafiają do fabryki: wylewki, odstępy i wycięcia są dokładne; białe kropki to środki otworów. Drukuj na drukarce laserowej w skali **100 % («Rzeczywisty rozmiar»)**, nigdy z «Dopasuj do strony», i sprawdź pasek 50 mm. Arkusze górne są lustrzane, dolne nie.

---

## Tryb wsadowy

```
RUN dmxON_FabKit.ulp -batch <folder> [-std iso|gost] [-lang en|ru|es|de|pl] [-offline] [-boards N] [-import plik] [-nogerber] [-nodocs] [-nosch] [-notoner] [-nopdf] [-nobackup] [-keep]
```

| Opcja | Znaczenie |
|---|---|
| `-batch <folder>` | bez okna, do tego folderu, bez zapisu atrybutów |
| `-lang <kod>` | język raportu i dokumentacji (domyślnie ostatnio wybrany w oknie) |
| `-std iso\|gost` | norma dokumentacji (domyślnie ostatnio wybrana w oknie) |
| `-nosch` | bez schematu elektrycznego |
| `-nobackup` | bez kopii folderu projektu |
| `-offline` | bez katalogu i EasyEDA |
| `-boards N` | liczba płytek w zamówieniu |
| `-import <plik>` | BOM JLCPCB (xlsx/csv/txt) |
| `-nogerber -nodocs -notoner -nopdf` | pomiń część pakietu |
| `-keep` | zachowaj folder tymczasowy do debugowania |

---

## Rozwiązywanie problemów

| Objaw | Co zrobić |
|---|---|
| Po instalacji brak karty **dmxON** | uruchom ponownie Fusion jeden raz albo włącz dodatek: **Utilities → Add-Ins → Scripts and Add-Ins → dmxON → Run** |
| Na innym komputerze nie ma ULP ani reguł, ścieżki prowadzą do pierwszego komputera | Fusion współdzieli ustawienia w całym koncie Autodesk. Zaktualizuj do FabKit 2.2.1 / JLC Rules 1.3.0 (dodatek 1.1.0) i raz uruchom `INSTALL.ulp` na tym komputerze: foldery są wtedy zapisane jako `$HOME\dmxON\…` i działają na każdym komputerze |
| Okno **CAM Export File List** | naciśnij **OK**: Fusion prosi o potwierdzenie eksportu Gerber. Z dodatkiem dmxON i dmxON JLC Rules okno się nie pojawia |
| «Kopię pominięto: dodatek dmxON nie działa» | zainstaluj przez `INSTALL.ulp` i uruchom ponownie Fusion |
| «Your PCB design has changed. CAM output is generated using the last saved version» | naciśnij **Cancel**, zapisz płytkę (Ctrl+S) i uruchom FabKit ponownie — inaczej Gerber powstanie ze starej zapisanej wersji (np. bez nowych reguł) |
| «Katalog JLCPCB nie odpowiedział» | sprawdź internet i proxy; pakiet i tak powstanie offline |
| Brak PDF | Microsoft Edge (lub Chrome) musi być zainstalowany w domyślnym folderze |
| «Wymagają uwagi» | przeczytaj każdą pozycję: napięcia, polaryzacja, wyprowadzenia, magazyn |

---

## Jak to działa

Faza 1 (ULP) analizuje płytkę i zapisuje BOM/CPL oraz szkice, faza 2 (polecenia Fusion) uruchamia `MANUFACTURING EXPORT`, faza 3 (ten sam ULP z `-finish`) tworzy Gerber, podglądy, raport, dokumentację i arkusze do termotransferu. Teksty hiszpańskie, niemieckie i polskie są w `lib/fk_lang.ulp`, generowanym z `lang/strings.tsv`. Szczegóły: [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) · zmiany: [CHANGELOG.md](CHANGELOG.md). **Dodatek dmxON** (`fusion-addin/dmxON`, Python) robi to, czego nie potrafi ULP: ustawienia folderów Fusion, kartę dmxON, Gerber bez okien przez `Electron.mfgexport`, kopie z chmury i aktualizacje; ULP zostawiają mu zlecenia w `Dokumenty\dmxON\.inbox`.

---

## Wesprzyj projekt

dmxON FabKit jest **darmowy**. Za nim stoją tygodnie pracy: parser Gerber i Excellon, dobór części z katalogu JLCPCB, dopasowanie footprintów, dokumentacja w pięciu językach i sprawdzenie na prawdziwych zamówieniach. Jeśli zaoszczędził Ci wieczór przygotowywania zamówienia, błędną część lub nieudany montaż — wesprzyj dalszy rozwój: nowe wersje, zmiany katalogu JLCPCB i poprawki pod nowe wersje Fusion.

<p align="center">
  <a href="https://www.paypal.com/donate/?business=smith.show2025%40gmail.com&no_recurring=0&item_name=dmxON+FabKit&currency_code=EUR"><img src="docs/assets/donate.pl.svg" alt="Wesprzyj dmxON FabKit przez PayPal" width="760"></a>
</p>

<p align="center">
  <b>PayPal:</b> <a href="https://www.paypal.com/donate/?business=smith.show2025%40gmail.com&no_recurring=0&item_name=dmxON+FabKit&currency_code=EUR">smith.show2025@gmail.com</a> — każda kwota pomaga. Dziękuję! ⭐ Gwiazdka na GitHub też pomaga innym znaleźć projekt.
</p>

---

## Licencja

Bezpłatne użycie z podaniem autora; kopiowanie kodu, modyfikacja i użycie komercyjne są zabronione — zob. [LICENSE.md](LICENSE.md). JLCPCB i LCSC są znakami towarowymi ich właścicieli; projekt nie jest z nimi powiązany.

**dmxON by AlexSmith 2026** · [dmxon512.com](https://dmxon512.com) · projekt siostrzany: [dmxON JLC Rules](https://github.com/AlexSmith2025/dmxON-JLC-Rules-Fusion-Electronics)
