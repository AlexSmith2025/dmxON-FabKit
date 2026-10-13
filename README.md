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
  <b>English</b> · <a href="README.ru.md">Русский</a> &nbsp;|&nbsp;
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
| 🌐 | Everything in **English and Russian** |

---

## Compatibility

| | dmxON FabKit |
|---|---|
| **Autodesk Fusion (Electronics), Windows 10/11** | ✅ tested on Fusion **2705.1.11** (October 2026) |
| Autodesk Fusion on macOS | ❌ uses Windows tools (`curl.exe`, `tar.exe`, Windows Script Host, Microsoft Edge) |
| EAGLE 9.x | ❌ needs Fusion's `MANUFACTURING EXPORT` command for Gerber |
| KiCad, Altium, EasyEDA | ❌ |

Also needed: **Microsoft Edge** (built into Windows) for PDFs; internet for the JLCPCB catalogue and EasyEDA footprints (everything else works offline). If a new Fusion build breaks something, please [open an issue](https://github.com/AlexSmith2025/dmxON-FabKit-Fusion-Electronics/issues).

---

## Installation

1. [**Download `dmxON-FabKit.zip`**](https://github.com/AlexSmith2025/dmxON-FabKit-Fusion-Electronics/releases/latest/download/dmxON-FabKit.zip) and unpack it anywhere, e.g. `Documents\dmxON-FabKit`.
2. Keep the layout: `dmxON_FabKit.ulp` loads its modules from `lib\` and settings from `config\` next to it.
3. Optional: add the folder to **Electronics → Preferences → Directories → ULPs**.

---

## Quick start

1. Open the **board** in Fusion Electronics and **save it** (Ctrl+S) — Fusion exports Gerber from the last saved version.
2. Run **Automation → Run ULP → `dmxON_FabKit.ulp`** or type `RUN 'C:/path/dmxON_FabKit.ulp'`.
3. Choose the folder in the dialog and press **Build package**.
4. Fusion may show a **CAM Export File List** window — press **OK** (that is the regular Gerber export).
5. About a minute later the package folder opens. Start with `index.html`.

Tip: run [**dmxON JLC Rules**](https://github.com/AlexSmith2025/dmxON-JLC-Rules-Fusion-Electronics) first — it sets up JLCPCB design rules and the layer stack-up, and passes the board thickness and mask colour to FabKit.

### The dialog

| Tab | What it sets |
|---|---|
| **Output** | folder; what to build: Gerber, A4 docs, PDF, toner sheets; what goes into BOM/CPL: THT, pad centre, skipped designators |
| **Parts** | catalogue search, Basic/Preferred, substitutes, footprint check, attribute re-check, writing `LCSC_PART`, board quantity, minimum capacitor voltage, feeder fee, BOM import |
| **PCB** | thickness, mask and silkscreen colour, finish — for the report, the order form and the render |
| **Title** | product, document number, revision, customer, note (per board); company and signatures (shared) |
| **About** | version, author, license, links |

All settings are remembered.

---

## Output

```
<board>_FabKit/
├── index.html                          start page
├── 01_JLCPCB_ORDER/
│   ├── JLCPCB_GERBER/
│   │   ├── <board>_Gerber_JLCPCB.zip   ← upload to jlcpcb.com
│   │   └── unpacked/                   the same files for review
│   ├── <board>_JLCPCB_BOM.csv          ← PCB Assembly: BOM
│   └── <board>_JLCPCB_CPL.csv          ← PCB Assembly: CPL
├── 02_REPORT/                          report + layer previews
├── 03_ASSEMBLY_DOCS/                   A4 documentation (HTML + PDF)
└── 04_TONER_TRANSFER_1to1/             HOW_TO_PRINT + 7 PDF sheets
```

Every run **deletes and rebuilds** the board's package — but only if FabKit created that folder (it holds a `.dmxon-fabkit` marker). A foreign folder with the same name is never touched.

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
RUN dmxON_FabKit.ulp -batch <folder> [-offline] [-boards N] [-import file] [-nogerber] [-nodocs] [-notoner] [-nopdf] [-keep]
```

| Flag | Meaning |
|---|---|
| `-batch <folder>` | no dialog, into this folder, no attribute writes |
| `-offline` | no catalogue and EasyEDA |
| `-boards N` | boards in the order |
| `-import <file>` | JLCPCB BOM (xlsx/csv/txt) |
| `-nogerber -nodocs -notoner -nopdf` | skip part of the package |
| `-keep` | keep the temp folder for debugging |

---

## Troubleshooting

| Symptom | What to do |
|---|---|
| **CAM Export File List** window | press **OK**: Fusion asks to confirm the Gerber export |
| «Your PCB design has changed. CAM output is generated using the last saved version» | press **Cancel**, save the board (Ctrl+S) and run FabKit again — otherwise Gerber is made from the old saved version (for example without new design rules) |
| «catalogue did not answer» | check internet and proxy; the package is still built offline |
| No PDF | Microsoft Edge (or Chrome) must be installed in its default folder |
| «Need attention» | read every line: voltages, polarity, pinout, stock |

---

## How it works

Phase 1 (ULP) analyses the board and writes BOM/CPL and drafts, phase 2 (Fusion commands) runs `MANUFACTURING EXPORT`, phase 3 (the same ULP with `-finish`) builds Gerber, previews, report, documentation and toner sheets. Details: [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) · changelog: [CHANGELOG.md](CHANGELOG.md).

---

## Support the project

dmxON FabKit is **free**. Behind it are weeks of work: a Gerber and Excellon parser, part selection against the JLCPCB catalogue, footprint matching, documentation and real orders checked against it. If it saved you an evening of preparing a JLCPCB order, a wrong part or a failed assembly — please support further development: new versions, catalogue changes at JLCPCB and fixes for new Fusion releases.

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
