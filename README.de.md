<p align="center">
  <img src="docs/assets/banner.svg" alt="dmxON FabKit — von der Autodesk-Fusion-Electronics-Platine zur kompletten JLCPCB-Bestellung" width="100%">
</p>

<p align="center">
  <a href="https://github.com/AlexSmith2025/dmxON-FabKit-Fusion-Electronics/releases/latest"><img src="https://img.shields.io/github/v/release/AlexSmith2025/dmxON-FabKit-Fusion-Electronics?style=for-the-badge&color=b4744a&label=release" alt="Neueste Version"></a>
  <a href="https://github.com/AlexSmith2025/dmxON-FabKit-Fusion-Electronics/releases"><img src="https://img.shields.io/github/downloads/AlexSmith2025/dmxON-FabKit-Fusion-Electronics/total?style=for-the-badge&color=24574a&label=downloads" alt="Downloads"></a>
  <img src="https://img.shields.io/badge/Autodesk%20Fusion-Electronics-e2ab7f?style=for-the-badge&logo=autodesk&logoColor=white" alt="Autodesk Fusion Electronics">
  <img src="https://img.shields.io/badge/Windows-10%20%7C%2011-3b4a5a?style=for-the-badge" alt="Windows 10 | 11">
  <a href="https://www.paypal.com/donate/?business=smith.show2025%40gmail.com&no_recurring=0&item_name=dmxON+FabKit&currency_code=EUR"><img src="https://img.shields.io/badge/PayPal-Spenden-003087?style=for-the-badge&logo=paypal&logoColor=white" alt="Mit PayPal spenden"></a>
</p>

<p align="center">
  <a href="https://github.com/AlexSmith2025/dmxON-FabKit-Fusion-Electronics/releases/latest/download/dmxON-FabKit.zip"><img src="https://img.shields.io/badge/%E2%AC%87%20Download-dmxON--FabKit.zip-b4744a?style=for-the-badge" alt="Neueste Version herunterladen"></a> <a href="https://github.com/AlexSmith2025/dmxON-Setup-Fusion-Electronics/releases/latest/download/dmxON-Setup.exe"><img src="https://img.shields.io/badge/%E2%AC%87%20Installer-dmxON--Setup.exe-24574a?style=for-the-badge" alt="Download the installer dmxON-Setup.exe"></a>
</p>

<p align="center">
  <a href="README.md">English</a> · <a href="README.ru.md">Русский</a> · <a href="README.es.md">Español</a> · <b>Deutsch</b> · <a href="README.pl.md">Polski</a>
</p>

<p align="center">
  <a href="#installation">Installation</a> ·
  <a href="#schnellstart">Schnellstart</a> ·
  <a href="#kompatibilität">Kompatibilität</a> ·
  <a href="#ergebnis">Ergebnis</a> ·
  <a href="#bestellung-bei-jlcpcb">Bestellung</a> ·
  <a href="#projekt-unterstützen">Spenden</a>
</p>

**dmxON FabKit ist ein ULP für Autodesk Fusion Electronics (Fusion 360 Electronics), das aus einer Platine in einem Durchlauf eine komplette JLCPCB-Bestellung macht: Gerber-Zip mit JLCPCB-Namen, BOM und CPL mit automatischer LCSC-Teileauswahl und Ersatzteilen, ein interaktiver Bericht, A4-Bestückungsdokumentation und 1:1-Blätter für den Tonertransfer.**

<p align="center">
  <a href="https://www.paypal.com/donate/?business=smith.show2025%40gmail.com&no_recurring=0&item_name=dmxON+FabKit&currency_code=EUR"><img src="docs/assets/donate.de.svg" alt="dmxON FabKit mit PayPal unterstützen — smith.show2025@gmail.com" width="760"></a>
</p>

---

## Was es macht

| | |
|---|---|
| 🏭 | **Gerber und Bohrdaten für JLCPCB**: Namen GTL/GBL/G1…/GTS/GTP/GTO/GKO/XLN, ein Zip zum Hochladen; Lagen und Platinenparameter werden automatisch erkannt |
| 🧾 | **BOM und CPL für die Bestückung** mit automatischer LCSC-Teileauswahl — Widerstände und Kondensatoren nach Wert, Gehäuse und Spannung, alles andere nach Herstellerteilenummer |
| 📐 | **Footprint-Prüfung** gegen die JLC-Bibliothek (EasyEDA): Drehung und Mitte im CPL aus dem Pad-Abgleich; gespiegelte und unpassende Gehäuse werden markiert |
| 🔁 | **Ersatzteile**: fehlt ein Teil, ist es nicht vorrätig oder passt das Gehäuse nicht, wird eine Alternative gesucht, gegen die Pads der Platine geprüft — die günstigste gewinnt |
| 💲 | **Kosten**: Katalogpreise für die ganze Charge, Feeder-Gebühren für Extended-Teile, die teuersten Zeilen |
| 📊 | **HTML-Bericht**: realistische Platinenansicht, Lagen-Umschalter, Gerber-Galerie, Bohrungen, Fertigbarkeitsprüfung, Platzierung mit Bezeichnern |
| 📄 | **A4-Dokumentation** für die Handbestückung: Deckblatt, Fertigungsspezifikation, Lagen, Bestückungspläne im Normmaßstab, Lötreihenfolge Schritt für Schritt, IC-Markierungen, BOM; editierbares Schriftfeld; PDF |
| 🖨️ | **Tonertransfer 1:1**: ein PDF pro Lage (Kupfer, Bestückungsdruck, Maske, Bohrungen), obere Blätter gespiegelt, 50-mm-Balken zur Maßstabsprüfung |
| 📥 | **Fertige JLCPCB-BOM importieren** (xlsx, csv oder Text von der Bestellseite) — Ihre geprüften Teilenummern haben Vorrang |
| 🌐 | **5 Sprachen**: Englisch, Russisch, Spanisch, Deutsch, Polnisch — Dialog, Bericht und alle Dokumente in der gewählten Sprache |
| 📏 | **Dokumentation nach ISO oder GOST**: Blätter und Schriftfelder nach ISO 5457 / ISO 7200 oder GOST R 2.104-2023; Dokumentenliste, Fertigungs- und Bestückungszeichnung, Stückliste (ISO 7573) oder Spezifikation (GOST R 2.106-2019), Elementeliste; IPC- und IEC-Verweise in den Anmerkungen |
| 🔌 | **Schaltplan** aus Ihrem Schaltplan im Normrahmen (GOST Э3 / IEC 61082-1) auf A4, A3 oder einem verlängerten A3×n-Blatt, damit der Text lesbar bleibt |
| 🧩 | **Reiter dmxON in Fusion** (Add-in): FabKit, JLC Rules, Sicherung und Updates mit einem Klick; Gerber ohne CAM-Bestätigungsfenster |
| 💾 | **Sicherung des gesamten Designordners**: Schaltpläne, Platinen und Bibliotheken als EAGLE-Dateien, 3D-Designs als `.f3d`, Zeichnungen als PDF und das Paket — auf jedem Konto und Rechner wiederherstellbar |
| 🔄 | **Updates von GitHub**: tägliche Prüfung, Installation auf Wunsch |

---

## Kompatibilität

| | dmxON FabKit |
|---|---|
| **Autodesk Fusion (Electronics), Windows 10/11** | ✅ getestet mit Fusion **2705.1.30** (Oktober 2026) |
| Autodesk Fusion unter macOS | ❌ nutzt Windows-Werkzeuge (`curl.exe`, `tar.exe`, `robocopy`, Windows Script Host, Microsoft Edge) |
| EAGLE 9.x | ❌ braucht den Fusion-Befehl `MANUFACTURING EXPORT` für Gerber |
| KiCad, Altium, EasyEDA | ❌ |

Außerdem nötig: **Microsoft Edge** (in Windows enthalten) für PDFs; Internet für den JLCPCB-Katalog und EasyEDA-Footprints (alles andere funktioniert offline). Wenn ein neuer Fusion-Build etwas kaputt macht, bitte [ein Issue öffnen](https://github.com/AlexSmith2025/dmxON-FabKit-Fusion-Electronics/issues).

---

## Installation

**Am einfachsten:** [**`dmxON-Setup.exe` herunterladen**](https://github.com/AlexSmith2025/dmxON-Setup-Fusion-Electronics/releases/latest/download/dmxON-Setup.exe) und starten — installiert dmxON FabKit, dmxON JLC Rules und das dmxON-Add-in in einem Schritt (neueste Versionen von GitHub, SHA-256 geprüft, ohne Administratorrechte; [dmxON Setup](https://github.com/AlexSmith2025/dmxON-Setup-Fusion-Electronics)). Oder von Hand:

1. [**`dmxON-FabKit.zip` herunterladen**](https://github.com/AlexSmith2025/dmxON-FabKit-Fusion-Electronics/releases/latest/download/dmxON-FabKit.zip) und beliebig entpacken.
2. In Fusion Electronics: **Automation → Run ULP → `INSTALL.ulp`** aus dem entpackten Ordner, Sprache wählen und **Installieren** drücken.
3. **Fusion einmal neu starten.** Platinen- und Schaltplan-Editor erhalten den Reiter **dmxON** — FabKit, JLC Rules, Sicherung, Updates, Einstellungen, Hilfe —, und `dmxON_FabKit` steht auch unter **Run ULP**.

Der Installer kopiert das Projekt nach `Dokumente\dmxON\dmxON-FabKit` und installiert das **dmxON-Add-in** (`%APPDATA%\Autodesk\Autodesk Fusion 360\API\AddIns\dmxON`). Das Add-in setzt die dmxON-Ordner an die Spitze der ULP-, Designregel- und CAM-Listen von Fusion (Preferences → General → Electronics → Directory) — die eingebauten ULPs bleiben — und repariert diese Pfade nach Fusion-Updates. Ein erneuter Start von `INSTALL.ulp` aktualisiert die Dateien; **Entfernen** löscht das kopierte Projekt und mit dem letzten dmxON-Werkzeug auch das Add-in. Ohne Neustart lässt sich das Add-in über **Utilities → Add-Ins → Scripts and Add-Ins → dmxON → Run** starten. Manuell ohne Add-in: den entpackten Ordner vollständig lassen und `RUN 'C:/Pfad/dmxON_FabKit.ulp'` ausführen.

**Mehrere Computer.** Fusion teilt seine Einstellungen — und die von FabKit — zwischen allen Computern Ihres Autodesk-Kontos. Deshalb schreibt das Add-in die Ordner als `$HOME\dmxON\…` und `$EAGLEDIR\…`, die Fusion auf jedem Computer durch dessen eigene Dokumente und Programmordner ersetzt, und FabKit übergeht einen Ausgabeordner, der zu einem anderen Computer gehört (stattdessen `Desktop\FabKit`). `INSTALL.ulp` auf jedem Computer einmal ausführen (oder **dmxON → Updates**, wo der Reiter schon da ist), damit die Dateien dort vorhanden sind.

---

## Schnellstart

1. Die **Platine** in Fusion Electronics öffnen und **speichern** (Strg+S) — Fusion exportiert Gerber aus der zuletzt gespeicherten Version.
2. **dmxON → FabKit** drücken (oder **Automation → Run ULP → `dmxON_FabKit`**).
3. Oben rechts **Norm** (ISO oder GOST) und **Sprache** wählen, den Ordner, und **Paket erstellen** drücken.
4. Mit dmxON-Add-in und installiertem dmxON JLC Rules wird Gerber ohne Fenster über den CAM-Job dmxON JLCPCB exportiert. Ohne sie kann Fusion das Fenster **CAM Export File List** zeigen — **OK** drücken.
5. Etwa eine Minute später öffnet sich der Paketordner. Mit `index.html` beginnen. Die Sicherung (standardmäßig an) legt auch das Design ins Paket: FabKit schreibt Schaltplan und Platine (EAGLE 9, mit ungespeicherten Änderungen) nach `05_BACKUP`, und das dmxON-Add-in legt das Platinen-STEP (mit den Bauteilmodellen) und den gesamten Cloud-Designordner dazu.

Tipp: zuerst [**dmxON JLC Rules**](https://github.com/AlexSmith2025/dmxON-JLC-Rules-Fusion-Electronics) ausführen — es richtet die JLCPCB-Designregeln und den Lagenaufbau ein und übergibt Platinendicke und Maskenfarbe an FabKit. Beide Werkzeuge teilen sich die Spracheinstellung.

### Der Dialog

| Register | Was es einstellt |
|---|---|
| **Sprache** (oben rechts) | English, Русский, Español, Deutsch, Polski — der Dialog wechselt sofort; Bericht und Dokumente entstehen in derselben Sprache |
| **Norm** (oben rechts) | ISO oder GOST — welche Dokumentation erstellt wird; gemeinsam mit dmxON JLC Rules |
| **Ausgabe** | Ordner; Sicherung des Designordners; was erstellen: Gerber, Dokumentation, Schaltplan, PDF, Tonerblätter; was in BOM/CPL kommt: THT, Pad-Mitte, ausgelassene Bezeichner |
| **Teile** | Katalogsuche, Basic/Preferred, Ersatzteile, Footprint-Prüfung, Attribut-Neuprüfung, `LCSC_PART` schreiben, Platinenanzahl, min. Kondensatorspannung, Feeder-Gebühr, BOM-Import |
| **Platine** | Dicke, Masken- und Druckfarbe, Oberfläche — für Bericht, Bestellformular und Ansicht |
| **Schriftfeld** | Produkt, Dokument-Nr., Version (Rev.), Kunde, Bemerkung (pro Platine); Firma und Unterschriften (gemeinsam) |
| **Info** | Version, Autor, Lizenz, Links |

Alle Einstellungen werden gespeichert.

---

## Ergebnis

```
<Platine>_v<Version>_FabKit/
├── index.html                          Startseite
├── 01_JLCPCB_ORDER/
│   ├── JLCPCB_GERBER/
│   │   ├── <Platine>_v<Version>_Gerber_JLCPCB.zip ← auf jlcpcb.com hochladen
│   │   └── unpacked/                   dieselben Dateien zur Ansicht
│   ├── <Platine>_v<Version>_JLCPCB_BOM.csv ← PCB Assembly: BOM
│   └── <Platine>_v<Version>_JLCPCB_CPL.csv ← PCB Assembly: CPL
├── 02_REPORT/                          Bericht + Lagenvorschau
├── 03_ASSEMBLY_DOCS/                   Dokumentation nach ISO oder GOST (HTML + PDF)
├── 04_TONER_TRANSFER_1to1/             HOW_TO_PRINT + 7 PDF-Blätter
└── 05_BACKUP/                          Sicherung: EAGLE-Schaltplan + Platine; STEP und Cloud-Ordner (Add-in)
```

Jeder Lauf **löscht das Paket der Platine und erstellt es neu** — aber nur, wenn FabKit den Ordner angelegt hat (er enthält die Markierung `.dmxon-fabkit`). Ein fremder Ordner mit gleichem Namen wird nie angefasst.

**Eine Version überall.** Die Platinenversion steht im Design als globales Attribut `REV` und wird im Feld **Version (Rev.)** auf dem Reiter **Schriftfeld** gesetzt. Sie ist Teil des Paketordners und aller Dateinamen (`<Platine>_v<Version>_…`, auch der Gerber-Dateien im Zip), der ISO-Schriftfelder und des Berichts. Beim ersten Mal übernimmt FabKit die auf der Platine gedruckte Version (ein Text wie «Ver. 1.4») oder ein früher von FabKit geschriebenes `REV` — ein `REV` aus einer Rahmenvorlage (oft «A») schlägt den Platinentext nicht — und schreibt sie mit OK ins Design. Der Bericht warnt, wenn Platinentext, `REV` und Paket nicht übereinstimmen. Pakete verschiedener Versionen liegen nebeneinander; ein neuer Lauf ersetzt nur das Paket derselben Version.

---

## Bestellung bei JLCPCB

1. **jlcpcb.com → Order now → Add gerber file** → `01_JLCPCB_ORDER/JLCPCB_GERBER/<Platine>_Gerber_JLCPCB.zip`.
2. Platinenparameter — aus dem Bericht (Abschnitt «Bestellung»).
3. **PCB Assembly** → BOM `…_JLCPCB_BOM.csv`, CPL `…_JLCPCB_CPL.csv`.
4. In der JLCPCB-Vorschau die Teile aus dem Berichtsabschnitt **«Achtung erforderlich»** prüfen.

### Teilenummern — Rangfolge

1. **BOM-Import** (Register Teile oder `-import Datei`).
2. **Attribut** am Bauteil: `LCSC_PART`, `LCSC`, `JLCPCB_PART`, `JLC` …
3. **Suche im JLCPCB-Katalog**: R/C nach Wert, Gehäuse und Spannung; alles andere nach der Herstellerteilenummer aus dem Wert oder einem Attribut `MPN` / `MANUFACTURER_PART_NUMBER`.
4. **Ersatzteil**, wenn das Teil fehlt, nicht vorrätig ist oder das Gehäuse nicht passt.

Nützliche Attribute: `JLC_PACKAGE`, `JLC_ROTATION`, `JLC_COMMENT`, `VOLTAGE`, `DNP` / `JLC_EXCLUDE`, `BOM=EXCLUDE`. Eigene Gehäuse- und Drehungszuordnung — `config/fk_package_map.txt`.

---

## Tonertransfer

Die Blätter entstehen aus **denselben Gerber-Dateien** wie für die Fertigung: Kupferflächen, Abstände und Aussparungen sind exakt; weiße Punkte markieren die Bohrmitten. Mit einem Laserdrucker in **100 % («Tatsächliche Größe»)** drucken, niemals «An Seite anpassen», und den 50-mm-Balken prüfen. Obere Blätter sind gespiegelt, untere nicht.

---

## Stapelbetrieb

```
RUN dmxON_FabKit.ulp -batch <Ordner> [-std iso|gost] [-lang en|ru|es|de|pl] [-offline] [-boards N] [-import Datei] [-nogerber] [-nodocs] [-nosch] [-notoner] [-nopdf] [-nobackup] [-keep]
```

| Schalter | Bedeutung |
|---|---|
| `-batch <Ordner>` | ohne Dialog, in diesen Ordner, keine Attribute schreiben |
| `-lang <Code>` | Sprache von Bericht und Dokumenten (Standard: die zuletzt im Dialog gewählte) |
| `-std iso\|gost` | Norm der Dokumentation (Standard: die zuletzt im Dialog gewählte) |
| `-nosch` | ohne Schaltplan |
| `-nobackup` | ohne Sicherung des Designordners |
| `-offline` | ohne Katalog und EasyEDA |
| `-boards N` | Platinen in der Bestellung |
| `-import <Datei>` | JLCPCB-BOM (xlsx/csv/txt) |
| `-nogerber -nodocs -notoner -nopdf` | Teil des Pakets auslassen |
| `-keep` | temporären Ordner zur Fehlersuche behalten |

---

## Fehlerbehebung

| Symptom | Was tun |
|---|---|
| Kein Reiter **dmxON** nach der Installation | Fusion einmal neu starten oder das Add-in starten: **Utilities → Add-Ins → Scripts and Add-Ins → dmxON → Run** |
| Auf einem anderen Computer werden ULPs oder Regeln nicht gefunden, die Pfade zeigen auf den ersten Computer | Fusion teilt seine Einstellungen im ganzen Autodesk-Konto. Auf FabKit 2.2.1 / JLC Rules 1.3.0 (Add-in 1.1.0) aktualisieren und `INSTALL.ulp` auf diesem Computer einmal ausführen: Die Ordner stehen dann als `$HOME\dmxON\…` in den Einstellungen und funktionieren auf jedem Computer |
| Fenster **CAM Export File List** | **OK** drücken: Fusion bittet, den Gerber-Export zu bestätigen. Mit dmxON-Add-in und dmxON JLC Rules erscheint das Fenster nicht |
| «Sicherung übersprungen: Das dmxON-Add-in läuft nicht» | mit `INSTALL.ulp` installieren und Fusion neu starten |
| «Your PCB design has changed. CAM output is generated using the last saved version» | **Cancel** drücken, Platine speichern (Strg+S) und FabKit erneut starten — sonst entsteht Gerber aus der alten gespeicherten Version (z. B. ohne neue Designregeln) |
| «JLCPCB-Katalog hat nicht geantwortet» | Internet und Proxy prüfen; das Paket wird trotzdem offline erstellt |
| Kein PDF | Microsoft Edge (oder Chrome) muss im Standardordner installiert sein |
| «Achtung erforderlich» | jede Zeile lesen: Spannungen, Polarität, Pinbelegung, Lagerbestand |

---

## Wie es funktioniert

Phase 1 (ULP) analysiert die Platine und schreibt BOM/CPL und Entwürfe, Phase 2 (Fusion-Befehle) führt `MANUFACTURING EXPORT` aus, Phase 3 (dasselbe ULP mit `-finish`) erstellt Gerber, Vorschauen, Bericht, Dokumentation und Tonerblätter. Spanische, deutsche und polnische Texte stehen in `lib/fk_lang.ulp`, das aus `lang/strings.tsv` erzeugt wird. Details: [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) · Änderungen: [CHANGELOG.md](CHANGELOG.md). Das **dmxON-Add-in** (`fusion-addin/dmxON`, Python) erledigt, was ein ULP nicht kann: die Ordner-Einstellungen von Fusion, den Reiter dmxON, Gerber ohne Fenster über `Electron.mfgexport`, Sicherungen aus der Cloud und Updates; die ULPs hinterlegen ihm Aufträge in `Dokumente\dmxON\.inbox`.

---

## Projekt unterstützen

dmxON FabKit ist **kostenlos**. Dahinter stecken Wochen Arbeit: ein Gerber- und Excellon-Parser, Teileauswahl über den JLCPCB-Katalog, Footprint-Abgleich, Dokumentation in fünf Sprachen und Prüfung an echten Bestellungen. Wenn es Ihnen einen Abend Bestellvorbereitung, ein falsches Teil oder eine misslungene Bestückung erspart hat — bitte unterstützen Sie die Weiterentwicklung: neue Versionen, Katalogänderungen bei JLCPCB und Anpassungen an neue Fusion-Versionen.

<p align="center">
  <a href="https://www.paypal.com/donate/?business=smith.show2025%40gmail.com&no_recurring=0&item_name=dmxON+FabKit&currency_code=EUR"><img src="docs/assets/donate.de.svg" alt="dmxON FabKit mit PayPal unterstützen" width="760"></a>
</p>

<p align="center">
  <b>PayPal:</b> <a href="https://www.paypal.com/donate/?business=smith.show2025%40gmail.com&no_recurring=0&item_name=dmxON+FabKit&currency_code=EUR">smith.show2025@gmail.com</a> — jeder Betrag hilft. Danke! ⭐ Ein Stern auf GitHub hilft anderen, das Projekt zu finden.
</p>

---

## Lizenz

Kostenlose Nutzung mit Namensnennung; Kopieren des Codes, Änderung und kommerzielle Nutzung sind nicht gestattet — siehe [LICENSE.md](LICENSE.md). JLCPCB und LCSC sind Marken ihrer Inhaber; dieses Projekt steht in keiner Verbindung zu ihnen.

**dmxON by AlexSmith 2026** · [dmxon512.com](https://dmxon512.com) · Schwesterprojekt: [dmxON JLC Rules](https://github.com/AlexSmith2025/dmxON-JLC-Rules-Fusion-Electronics)
