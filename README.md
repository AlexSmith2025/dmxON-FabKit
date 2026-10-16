<p align="center">
  <img src="docs/assets/banner.svg" alt="dmxON FabKit — from an Autodesk Fusion Electronics board to a complete JLCPCB order" width="100%">
</p>

<p align="center">
  <a href="https://github.com/AlexSmith2025/dmxON-FabKit-Fusion-Electronics/releases/latest"><img src="https://img.shields.io/github/v/release/AlexSmith2025/dmxON-FabKit-Fusion-Electronics?style=for-the-badge&color=b4744a&label=release" alt="Latest release"></a>
  <a href="https://github.com/AlexSmith2025/dmxON-FabKit-Fusion-Electronics/releases"><img src="https://img.shields.io/github/downloads/AlexSmith2025/dmxON-FabKit-Fusion-Electronics/total?style=for-the-badge&color=24574a&label=downloads" alt="Downloads"></a>
  <img src="https://img.shields.io/badge/Autodesk%20Fusion-Electronics-e2ab7f?style=for-the-badge&logo=autodesk&logoColor=white" alt="Autodesk Fusion Electronics">
  <img src="https://img.shields.io/badge/Windows-10%20%7C%2011-3b4a5a?style=for-the-badge" alt="Windows 10 | 11">
  <a href="https://www.paypal.com/donate/?business=smith.show2025%40gmail.com&no_recurring=0&item_name=dmxON+FabKit&currency_code=EUR"><img src="https://img.shields.io/badge/PayPal-Donate-003087?style=for-the-badge&logo=paypal&logoColor=white" alt="Donate with PayPal"></a>
</p>

<p align="center">
  <a href="https://github.com/AlexSmith2025/dmxON-FabKit-Fusion-Electronics/releases/latest/download/dmxON-FabKit.zip"><img src="https://img.shields.io/badge/%E2%AC%87%20Download-dmxON--FabKit.zip-b4744a?style=for-the-badge" alt="Download the latest version"></a>
</p>

<p align="center">
  <b>English</b> · <a href="README.ru.md">Русский</a> · <a href="README.es.md">Español</a> · <a href="README.de.md">Deutsch</a> · <a href="README.pl.md">Polski</a>
</p>

<p align="center">
  <a href="#installation">Installation</a> ·
  <a href="#quick-start">Quick start</a> ·
  <a href="#compatibility">Compatibility</a> ·
  <a href="#output">Output</a> ·
  <a href="#ordering-at-jlcpcb">Ordering</a> ·
  <a href="#support-the-project">Donate</a>
</p>

**dmxON FabKit is a ULP for Autodesk Fusion Electronics (Fusion 360 Electronics) that turns a board into a complete JLCPCB order in one run: Gerber zip with JLCPCB names, BOM and CPL with automatic LCSC part selection and substitutes, an interactive report, A4 assembly documentation and 1:1 toner-transfer sheets.**

<p align="center">
  <a href="https://www.paypal.com/donate/?business=smith.show2025%40gmail.com&no_recurring=0&item_name=dmxON+FabKit&currency_code=EUR"><img src="docs/assets/donate.svg" alt="Support dmxON FabKit with PayPal — smith.show2025@gmail.com" width="760"></a>
</p>

---

## What it does

| | |
|---|---|
| 🏭 | **JLCPCB Gerber and drill**: GTL/GBL/G1…/GTS/GTP/GTO/GKO/XLN names, an upload-ready zip; layers and board parameters detected automatically |
| 🧾 | **BOM and CPL for assembly** with automatic LCSC part selection — resistors and capacitors by value, package and voltage, everything else by manufacturer part number |
| 📐 | **Footprint verification** against the JLC (EasyEDA) library: CPL rotation and centre come from pad alignment; mirrored and non-fitting packages are flagged |
| 🔁 | **Substitutes**: if a part is missing, out of stock or its package does not fit, an alternative is found, checked against the board pads and the cheapest one wins |
| 💲 | **Cost**: catalogue prices for the whole batch, Extended feeder fees, the most expensive lines |
| 📊 | **HTML report**: realistic board render, layer toggles, Gerber gallery, drilling, manufacturability check, placement with designators |
| 📄 | **A4 documentation** for manual assembly: cover, fabrication spec, layers, assembly drawings at standard scale, step-by-step soldering order, IC keys, BOM; editable title block; PDF |
| 🖨️ | **Toner transfer 1:1**: a PDF per layer (copper, silkscreen, mask, drill), top sheets mirrored, a 50 mm bar to check the scale |
| 📥 | **Import a finished JLCPCB BOM** (xlsx, csv or text from the order page) — your verified part numbers win |
| 🌐 | **5 languages**: English, Russian, Spanish, German, Polish — the dialog, the report and all documents in the language you pick |
| 📏 | **Documentation to ISO or GOST**: sheets and title blocks per ISO 5457 / ISO 7200 or GOST R 2.104-2023; document list, fabrication and assembly drawings, parts list (ISO 7573) or specification (GOST R 2.106-2019), list of elements; IPC and IEC references in the notes |
| 🔌 | **Circuit diagram** from your schematic in the standard frame (GOST Э3 / IEC 61082-1) on A4, A3 or an elongated A3×n sheet, so the text stays readable |
| 🧩 | **dmxON tab in Fusion** (add-in): FabKit, JLC Rules, backup and updates in one click; Gerber without the CAM confirmation window |
| 💾 | **Backup of the whole design folder**: schematics, boards and libraries as EAGLE files, 3D designs as `.f3d`, drawings as PDF, plus the package — restorable on any account or computer |
| 🔄 | **Updates from GitHub**: a daily check, install on request |

---

## Compatibility

| | dmxON FabKit |
|---|---|
| **Autodesk Fusion (Electronics), Windows 10/11** | ✅ tested on Fusion **2705.1.30** (October 2026) |
| Autodesk Fusion on macOS | ❌ uses Windows tools (`curl.exe`, `tar.exe`, `robocopy`, Windows Script Host, Microsoft Edge) |
| EAGLE 9.x | ❌ needs Fusion's `MANUFACTURING EXPORT` command for Gerber |
| KiCad, Altium, EasyEDA | ❌ |

Also needed: **Microsoft Edge** (built into Windows) for PDFs; internet for the JLCPCB catalogue and EasyEDA footprints (everything else works offline). If a new Fusion build breaks something, please [open an issue](https://github.com/AlexSmith2025/dmxON-FabKit-Fusion-Electronics/issues).

---

## Installation

1. [**Download `dmxON-FabKit.zip`**](https://github.com/AlexSmith2025/dmxON-FabKit-Fusion-Electronics/releases/latest/download/dmxON-FabKit.zip) and unpack it anywhere.
2. In Fusion Electronics: **Automation → Run ULP → `INSTALL.ulp`** from the unpacked folder, choose the language and press **Install**.
3. **Restart Fusion once.** The PCB and schematic editors get a **dmxON** tab — FabKit, JLC Rules, Backup, Updates, Settings, Help — and `dmxON_FabKit` is also in **Run ULP**.

The installer copies the project to `Documents\dmxON\dmxON-FabKit` and installs the **dmxON add-in** (`%APPDATA%\Autodesk\Autodesk Fusion 360\API\AddIns\dmxON`). The add-in puts the dmxON folders first in Fusion's ULP, design rules and CAM lists (Preferences → General → Electronics → Directory) — Fusion's built-in ULPs stay — and repairs those paths after Fusion updates. Running `INSTALL.ulp` again updates the files; **Remove** deletes the copied project and, with the last dmxON tool, the add-in. Without a restart the add-in can be started from **Utilities → Add-Ins → Scripts and Add-Ins → dmxON → Run**. Manual alternative without the add-in: keep the unpacked folder intact and run `RUN 'C:/path/dmxON_FabKit.ulp'`.

**Several computers.** Fusion shares its preferences — and FabKit's settings — across every computer of your Autodesk account. The add-in therefore writes the folders as `$HOME\dmxON\…` and `$EAGLEDIR\…`, which Fusion expands on each computer to its own Documents and program folder, and FabKit ignores an output folder that belongs to another computer (it uses `Desktop\FabKit` instead). Run `INSTALL.ulp` once on every computer (or **dmxON → Updates** where the tab already exists) so the files are there.

---

## Quick start

1. Open the **board** in Fusion Electronics and **save it** (Ctrl+S) — Fusion exports Gerber from the last saved version.
2. Press **dmxON → FabKit** (or **Automation → Run ULP → `dmxON_FabKit`**).
3. Pick the **standard** (ISO or GOST) and the **language** in the top-right corner, choose the folder and press **Build package**.
4. With the dmxON add-in and dmxON JLC Rules installed, Gerber is exported silently through the dmxON JLCPCB CAM job. Without them Fusion may show a **CAM Export File List** window — press **OK**.
5. About a minute later the package folder opens. Start with `index.html`. With the backup option on, the add-in then saves the whole design folder into the package, `05_BACKUP`.

Tip: run [**dmxON JLC Rules**](https://github.com/AlexSmith2025/dmxON-JLC-Rules-Fusion-Electronics) first — it sets up JLCPCB design rules and the layer stack-up, and passes the board thickness and mask colour to FabKit. Both tools share the language setting.

### The dialog

| Tab | What it sets |
|---|---|
| **Language** (top right) | English, Русский, Español, Deutsch, Polski — the dialog switches at once; the report and documents are written in the same language |
| **Standard** (top right) | ISO or GOST — which documentation set is written; shared with dmxON JLC Rules |
| **Output** | folder; backup of the design folder; what to build: Gerber, documentation, circuit diagram, PDF, toner sheets; what goes into BOM/CPL: THT, pad centre, skipped designators |
| **Parts** | catalogue search, Basic/Preferred, substitutes, footprint check, attribute re-check, writing `LCSC_PART`, board quantity, minimum capacitor voltage, feeder fee, BOM import |
| **PCB** | thickness, mask and silkscreen colour, finish — for the report, the order form and the render |
| **Title** | product, document number, version (Rev.), customer, note (per board); company and signatures (shared) |
| **About** | version, author, license, links |

All settings are remembered.

---

## Output

```
<board>_v<version>_FabKit/
├── index.html                          start page
├── 01_JLCPCB_ORDER/
│   ├── JLCPCB_GERBER/
│   │   ├── <board>_v<version>_Gerber_JLCPCB.zip ← upload to jlcpcb.com
│   │   └── unpacked/                   the same files for review
│   ├── <board>_v<version>_JLCPCB_BOM.csv ← PCB Assembly: BOM
│   └── <board>_v<version>_JLCPCB_CPL.csv ← PCB Assembly: CPL
├── 02_REPORT/                          report + layer previews
├── 03_ASSEMBLY_DOCS/                   documentation to ISO or GOST (HTML + PDF)
├── 04_TONER_TRANSFER_1to1/             HOW_TO_PRINT + 7 PDF sheets
└── 05_BACKUP/                          backup of the whole design folder (dmxON add-in)
```

Every run **deletes and rebuilds** the board's package — but only if FabKit created that folder (it holds a `.dmxon-fabkit` marker). A foreign folder with the same name is never touched.

**One version everywhere.** The board version is stored in the design as the global attribute `REV` and set in the **Version (Rev.)** field of the **Title** tab. It is part of the package folder and every file name (`<board>_v<version>_…`, the Gerber files inside the zip too), the ISO title blocks and the report. The first time, FabKit takes the version printed on the board (a text such as «Ver. 1.4») or a `REV` it wrote earlier — a `REV` left by a frame template (often «A») does not override the board text — and writes it into the design when you press OK. The report warns when the board text, `REV` and the package disagree. Packages of different versions are kept side by side; a new run replaces only the package of the same version.

---

## Ordering at JLCPCB

1. **jlcpcb.com → Order now → Add gerber file** → `01_JLCPCB_ORDER/JLCPCB_GERBER/<board>_Gerber_JLCPCB.zip`.
2. PCB parameters — from the report («Order» section).
3. **PCB Assembly** → BOM `…_JLCPCB_BOM.csv`, CPL `…_JLCPCB_CPL.csv`.
4. In the JLCPCB preview check the parts listed under **«Need attention»** in the report.

### Part numbers — order of precedence

1. **BOM import** (Parts tab or `-import file`).
2. **Attribute** on the part: `LCSC_PART`, `LCSC`, `JLCPCB_PART`, `JLC` …
3. **JLCPCB catalogue search**: R/C by value, package and voltage; others by the manufacturer part number from the value or an `MPN` / `MANUFACTURER_PART_NUMBER` attribute.
4. **Substitute** if missing, out of stock or the package does not fit.

Useful attributes: `JLC_PACKAGE`, `JLC_ROTATION`, `JLC_COMMENT`, `VOLTAGE`, `DNP` / `JLC_EXCLUDE`, `BOM=EXCLUDE`. Own package and rotation mapping — `config/fk_package_map.txt`.

---

## Toner transfer

Sheets are built from **the same Gerber files** the factory gets: pours, clearances and cut-outs are exact; white dots mark drill centres. Print on a laser printer at **100 % / Actual size**, never «Fit to page», and check the 50 mm bar. Top sheets are mirrored, bottom ones are not.

---

## Batch mode

```
RUN dmxON_FabKit.ulp -batch <folder> [-std iso|gost] [-lang en|ru|es|de|pl] [-offline] [-boards N] [-import file] [-nogerber] [-nodocs] [-nosch] [-notoner] [-nopdf] [-nobackup] [-keep]
```

| Flag | Meaning |
|---|---|
| `-batch <folder>` | no dialog, into this folder, no attribute writes |
| `-lang <code>` | language of the report and documents (default: the language last picked in the dialog) |
| `-std iso\|gost` | documentation standard (default: the one last picked in the dialog) |
| `-nosch` | no circuit diagram |
| `-nobackup` | no backup of the design folder |
| `-offline` | no catalogue and EasyEDA |
| `-boards N` | boards in the order |
| `-import <file>` | JLCPCB BOM (xlsx/csv/txt) |
| `-nogerber -nodocs -notoner -nopdf` | skip part of the package |
| `-keep` | keep the temp folder for debugging |

---

## Troubleshooting

| Symptom | What to do |
|---|---|
| No **dmxON** tab after installing | restart Fusion once, or start the add-in: **Utilities → Add-Ins → Scripts and Add-Ins → dmxON → Run** |
| On another computer the ULPs or rules are not found, the paths point to the first computer | Fusion shares its preferences across your Autodesk account. Update to FabKit 2.2.1 / JLC Rules 1.3.0 (add-in 1.1.0) and run `INSTALL.ulp` once on that computer: the folders are then stored as `$HOME\dmxON\…` and work on every computer |
| **CAM Export File List** window | press **OK**: Fusion asks to confirm the Gerber export. With the dmxON add-in and dmxON JLC Rules installed the window does not appear |
| «Backup skipped: the dmxON add-in is not running» | install with `INSTALL.ulp` and restart Fusion |
| «Your PCB design has changed. CAM output is generated using the last saved version» | press **Cancel**, save the board (Ctrl+S) and run FabKit again — otherwise Gerber is made from the old saved version (for example without new design rules) |
| «catalogue did not answer» | check internet and proxy; the package is still built offline |
| No PDF | Microsoft Edge (or Chrome) must be installed in its default folder |
| «Need attention» | read every line: voltages, polarity, pinout, stock |

---

## How it works

Phase 1 (ULP) analyses the board and writes BOM/CPL and drafts, phase 2 (Fusion commands) runs `MANUFACTURING EXPORT`, phase 3 (the same ULP with `-finish`) builds Gerber, previews, report, documentation and toner sheets. Texts in Spanish, German and Polish come from `lib/fk_lang.ulp`, generated from `lang/strings.tsv`. Details: [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) · changelog: [CHANGELOG.md](CHANGELOG.md). The **dmxON add-in** (`fusion-addin/dmxON`, Python) does what a ULP cannot: Fusion's directory preferences, the dmxON tab, silent Gerber through `Electron.mfgexport`, cloud backups and updates; the ULPs leave it requests in `Documents\dmxON\.inbox`.

---

## Support the project

dmxON FabKit is **free**. Behind it are weeks of work: a Gerber and Excellon parser, part selection against the JLCPCB catalogue, footprint matching, documentation in five languages and real orders checked against it. If it saved you an evening of preparing a JLCPCB order, a wrong part or a failed assembly — please support further development: new versions, catalogue changes at JLCPCB and fixes for new Fusion releases.

<p align="center">
  <a href="https://www.paypal.com/donate/?business=smith.show2025%40gmail.com&no_recurring=0&item_name=dmxON+FabKit&currency_code=EUR"><img src="docs/assets/donate.svg" alt="Support dmxON FabKit with PayPal" width="760"></a>
</p>

<p align="center">
  <b>PayPal:</b> <a href="https://www.paypal.com/donate/?business=smith.show2025%40gmail.com&no_recurring=0&item_name=dmxON+FabKit&currency_code=EUR">smith.show2025@gmail.com</a> — any amount helps. Thank you! ⭐ A star on GitHub also helps other people find the project.
</p>

---

## License

Free to use with attribution; copying the code, modification and commercial use are not permitted — see [LICENSE.md](LICENSE.md). JLCPCB and LCSC are trademarks of their owners; this project is not affiliated with them.

**dmxON by AlexSmith 2026** · [dmxon512.com](https://dmxon512.com) · companion project: [dmxON JLC Rules](https://github.com/AlexSmith2025/dmxON-JLC-Rules-Fusion-Electronics)
