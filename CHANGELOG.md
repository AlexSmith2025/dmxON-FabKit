# Changelog

The version is bumped on every change: `FK_VERSION` and `FK_DATE` in `lib/fk_core.ulp`, the `VERSION` file and an entry here.
Numbering: `MAJOR.MINOR.PATCH` — new feature → MINOR, fix → PATCH.

---

## 2.5.1 — 2026-10-16

**Fixed**

- **Document tables fit their columns.** The ISO parts list sizes its columns from the content (the longest part number, manufacturer or title decides the minimum, the rest is shared by the amount of text) and picks the largest text height that fits — 3.5, 3.0, 2.5 or 2.2 mm; part numbers and order codes are no longer cut off. Long words wrap instead of being clipped in every table, and row heights follow the real word wrapping, so pages break correctly. The standard GOST column widths stay; a header word wider than its GOST column («Поз. обозначение») is set smaller instead of breaking.
- The parts list title no longer repeats the part number that has its own column («red, 0603» instead of «NCD0603R3 red NCD0603R3»); the GOST specification and list of elements drop the duplicate too. Manufacturer names lose the bracketed note («UNI-ROYAL» instead of «UNI-ROYAL(Uniroyal Elec)»).

---

## 2.5.0 — 2026-10-16

**Changed**

- **FabKit writes the design backup itself.** The backup option (on by default, shared key `dmxon.backup`) saves the schematic and board — the EAGLE 9 files Fusion hands to ULPs, with unsaved changes and embedded libraries — as `<board>_v<version>_backup_<date>.zip` in `05_BACKUP` of the package, with no add-in needed. With the dmxON add-in (1.3.0) running, the whole cloud design folder (3D, drawings, other files) is added there as `<board>_v<version>_cloud_<date>.zip`. The start page links the backup.

---

## 2.4.0 — 2026-10-16

**Changed**

- **The design-folder backup goes into the production package.** With «Back up the whole design folder» on, the dmxON add-in (1.2.0) writes `<folder>_<date>.zip` into `<board>_v<version>_FabKit\05_BACKUP` — next to Gerber, BOM/CPL and the documentation — instead of `Documents\dmxON\Backups`; the start page links it. The package is not copied into that archive any more (it is right beside it). The Backup button on the dmxON tab still saves to `Documents\dmxON\Backups` (or the folder set in the add-in settings).

---

## 2.3.0 — 2026-10-16

**New**

- **One version everywhere.** The board version is kept in the design as the global attribute `REV` and edited in the **Version (Rev.)** field of the Title tab. It is part of the package folder and every file name — `<board>_v<version>_FabKit/`, `…_JLCPCB_BOM.csv`, `…_JLCPCB_CPL.csv`, `…_Gerber_JLCPCB.zip` and the Gerber files inside it, the report, the assembly documentation, the toner-transfer sheets — and of the ISO title blocks, the report and the start page. FabKit takes the version from a `REV` it wrote earlier, otherwise from the text on the board («Ver. 1.4»; a frame template's `REV`, often «A», does not override it), otherwise from the last entry, and writes it into the design on OK. The manufacturability check warns when the board text, `REV` and the package disagree. Packages of different versions are kept side by side.

**Changed**

- ISO 5457 centring marks run from the trimmed edge to the frame only; they no longer cross the title block or the drawing area.

---

## 2.2.2 — 2026-10-16

**Fixed**

- **LEDs and diodes are no longer placed backwards.** Polarized two-pin parts are matched to the JLC footprint by anode and cathode — the pin names of the board's schematic symbol (A, C/K, +/−) against the pin names of the JLC (EasyEDA) symbol — instead of by pad numbers 1/2. Libraries number these pads differently (a Würth LED: 1 = cathode; LCSC LEDs: 1 = anode), so the CPL could turn an LED by 180°; before, this was only flagged as «check the polarity mark in the preview». The footprint table shows «anode and cathode» for such parts.
- The `LCSC_PART` attributes FabKit writes into the design are hidden; they used to appear as visible text on tValues.

---

## 2.2.1 — 2026-10-14

**Fixed**

- **Works on every computer of the account.** Fusion shares its preferences and the ULP settings across all computers of an Autodesk account, so paths saved on one computer (`C:\Users\<name>\…`, `webdeploy\production\<build>`) reached the others, and the ULPs and rules were not found there. The dmxON add-in 1.1.0 writes the folders as `$HOME\dmxON\…` and `$EAGLEDIR\…`, which Fusion expands on each computer to its own Documents and program folder, and converts the paths of other computers it finds; the ULPs take the user folder only from paths that exist on this computer. An output folder saved on another computer is replaced with `Desktop\FabKit`. Run `INSTALL.ulp` (or **dmxON → Updates**) once on each computer.
- Four texts of 2.2.0 — the circuit diagram title, «sheet», the circuit diagram option and the add-in's Gerber phase — are now translated into Spanish, German and Polish.

**Changed**

- dmxON add-in 1.1.0: also sets the schematic grid for dmxON JLC Rules 1.3.0.

---

## 2.2.0 — 2026-10-13

**New**

- **Documentation to ISO or GOST.** A **Standard** selector next to the language (shared with dmxON JLC Rules):
  - **ISO**: sheets per ISO 5457 (frame, grid zones, centring marks), title block per ISO 7200, document list, fabrication drawing, assembly drawing, parts list per ISO 7573, assembly instruction; notes reference IPC-6012F / IPC-A-600M, IPC J-STD-001J / IPC-A-610J, IPC-4101F, IPC-SM-840E, J-STD-003D, IPC-9252B, IEC 61340-5-1:2024, J-STD-033D / J-STD-020F, IEC 81346-2:2019.
  - **GOST (ESKD)**: title blocks per GOST R 2.104-2023 (forms 1, 2, 2a and the extra columns), specification per GOST R 2.106-2019, assembly drawing (СБ), PCB drawing per GOST 2.417-91 with the GOST R 53429-2009 accuracy class, list of elements (ПЭ3) and circuit diagram (Э3) per GOST 2.701-2008 / 2.702-2011.
- **Circuit diagram** sheets (GOST Э3 / IEC 61082-1 circuit diagram) drawn from the schematic, without your own frame: the frame and title block follow the chosen standard; a wide schematic goes onto an elongated sheet (A3×3 … A3×7, GOST 2.301 / ISO 5457) so the text stays readable. Works around two Fusion ULP defects: symbol geometry read through an instance comes transformed twice (corrected, checked against the net wires), and `polygons()` of a symbol stops the ULP (symbol polygons are read from the schematic file instead).
- **Assembly drawing that can be read**: designators at least 1.8 mm high on paper (ISO 3098), inside the part when they fit, otherwise next to it, never on top of another designator or body. When the board is too dense, the overview sheet shows detail frames A, B, … and each detail follows on its own sheet at a larger standard scale.
- **dmxON add-in for Fusion** (`fusion-addin/dmxON`, installed by `INSTALL.ulp`): a **dmxON** tab in the PCB and schematic editors with FabKit, JLC Rules, Backup, Updates, Settings and Help; it registers the dmxON folders in Fusion's ULP / design rules / CAM lists (the setting Fusion really reads) and repairs them after Fusion updates.
- **Gerber without the «CAM Export File List» window**: with the add-in running and dmxON JLC Rules installed, Gerber is exported silently through the dmxON JLCPCB CAM job (already in JLCPCB names); otherwise the regular `MANUFACTURING EXPORT` is used.
- **Backup of the whole design folder**: option «Back up the whole design folder to this computer». After the package is built the add-in saves every file of the cloud folder — schematics, boards and libraries as EAGLE 9 files, 3D designs as Fusion archives (.f3d), drawings as PDF, other files unchanged — plus the FabKit package, into `Documents\dmxON\Backups\<project>\<folder>\<folder>_<date>.zip` with `manifest.json` and restore instructions. Restorable on any account or computer.
- **Updates from GitHub**: the add-in checks the latest releases once a day and installs new versions on request (Updates button).
- **PCB part number** field on the Title tab (the fabrication drawing's identification number).
- `-std iso|gost`, `-nosch`, `-nobackup` for batch mode.

**Changed**

- Parts lists and the specification write designator ranges (`R1–R5` for ISO, `R1…R5` for GOST 2.701); numbers after `$` (Fusion's `LED$5`) count too; very long cells continue on the next row.
- Non-polar two-pin parts (resistors such as `33R`, ceramic capacitors) get no polarity key.
- GOST: document codes are separated by a space (`… СБ`, `… Э3`, `… ПЭ3`, GOST 2.102); the date column shows `DD.MM.YY`.
- `INSTALL.ulp` installs the add-in instead of writing `EAGLE:Directories.*` (Fusion ignores those) and undoes what 2.1.0 wrote there.
- The board name drops Fusion's «(~recovered)» mark.

---

## 2.1.0 — 2026-10-13 (not released separately; included in 2.2.0)

**New**

- **Five languages, one at a time.** The dialog, the report, the A4 documentation, the toner-transfer sheets and the start page now come out in a single language — English (default), Russian, Spanish, German or Polish — instead of Russian with English subtitles. The language is picked in the top-right corner of the dialog and switches it at once; dmxON JLC Rules uses the same setting.
- `-lang en|ru|es|de|pl` for batch mode.
- **`INSTALL.ulp`** — copies FabKit to `Documents\dmxON\dmxON-FabKit` and adds the folder to Fusion's ULP directories through Fusion's own settings, so `dmxON_FabKit` is in the Run ULP list after a restart. **Remove** restores the previous folders (shared with the dmxON JLC Rules installer).
- Translation table `lang/strings.tsv` → `lib/fk_lang.ulp` (Spanish, German, Polish), keyed by the English text.
- README in English, Russian, Spanish, German and Polish; a donation card for each language.

**Changed**

- BOM notes are stored once, in the selected language; warnings are tracked by a flag instead of searching the text for «WARNING».
- Changelog, license and architecture notes are in English only.

---

## 2.0.5 — 2026-10-13

**Changed**

- The repository is renamed to **dmxON-FabKit-Fusion-Electronics** so it is easier to find when searching for «Fusion Electronics». Links in the program and docs are updated; GitHub redirects the old addresses.

---

## 2.0.4 — 2026-10-13

**Changed**

- About tab: links to GitHub and to supporting the project (PayPal); links open in the browser.
- README in English (main page) and Russian (`README.ru.md`): banner, version and download badges, a Download button, a compatibility table. Fixed: FabKit runs in Fusion only — EAGLE 9 has no `MANUFACTURING EXPORT` command.
- README: save the board before running — Fusion exports Gerber from the last saved version; what to answer to Fusion's «Your PCB design has changed…».
- Releases carry a ready `dmxON-FabKit.zip` (a permanent link to the latest version).

---

## 2.0.3 — 2026-10-12

**Documentation**

- README: a link to the companion project [dmxON JLC Rules](https://github.com/AlexSmith2025/dmxON-JLC-Rules-Fusion-Electronics) — JLCPCB rules for 2, 4, 6 and 8 layers and a board setup.

---

## 2.0.2 — 2026-10-09

**Fixed**

- Manufacturability check: layers extending beyond the board outline (copper — error; silkscreen, mask, paste — warning with the overshoot).
- The toner-sheet scale bar is exactly 50 mm including line width (was 50.5 mm). Sheet scale verified by measurement: outline 198 × 74 mm.
- Toner instructions: a non-ASCII character in the English text fixed.

---

## 2.0.1 — 2026-10-08

**Fixed**

- Cyrillic folders and names: the package path, title block and summary window are no longer garbled (characters are restored from a table instead of an 8-bit `char`).
- Gerber zip and XLSX import in Cyrillic folders: `tar.exe` now runs from the temp folder with Latin names.
- Helper commands no longer pop up console/Terminal windows (run via windowless `wscript`); PDF waiting without flashing windows.
- If the package folder cannot be created — a clear message right away instead of a chain of errors.
- Real parts whose footprint has no paste (e.g. an SOD-123 diode) stay in BOM/CPL with a warning instead of being dropped as jumpers.
- Pin 1: the exact name «1» wins over thermal vias named `P$1`; lead pitch is taken from SMD pads (QFN, DPAK).
- Ceramic chips 0402…2512 no longer appear on the «Pin 1 and polarity» sheet.
- The footprint table no longer lists substitute-candidate pairs.
- Soldering-step tables no longer run under the title block; columns are balanced.
- The dialog fits a 1024×768 screen: shorter labels and tabs.
- Import: text copied from the JLCPCB order page is recognised before CSV.

---

## 2.0.0 — 2026-10-08

First release of dmxON FabKit.

**New**

- One-run production package: Gerber + BOM + CPL + report + A4 documentation + toner sheets.
- JLCPCB Gerber: Protel names (GTL, GBL, G1…, GTS, GTP, GTO, GKO, XLN), upload zip, detection of layers, thickness, min track and hole.
- Own Gerber RS-274X and Excellon parser: layer previews, realistic board render, drill map.
- Manufacturability check against JLCPCB capabilities (track width, holes, thin copper artwork).
- Substitutes for missing parts, checked against the board pads, cheapest wins.
- Catalogue prices, batch cost, Extended feeder fees.
- Import of a finished JLCPCB BOM (xlsx, csv, order-page text).
- A4 documentation: cover with contents, fabrication spec, layers, assembly drawings at standard scale, soldering steps, pin-1/polarity keys, BOM; frame and title block editable in the browser; PDF via Microsoft Edge.
- 1:1 toner-transfer sheets from Gerber: copper, silkscreen, UV mask, drill guide; 50 mm scale bar.
- All output in Russian and English.
- Tabbed dialog, per-board title block, batch mode.
- The board package is rebuilt from scratch; only folders carrying the FabKit marker are deleted.

**Based on**

- LCSC selection, EasyEDA footprint verification and CPL rotation fixes from the earlier `jlcpcb_export.ulp` (1.x), rewritten as modules.
