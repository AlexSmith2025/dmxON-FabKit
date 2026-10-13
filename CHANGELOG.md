# Changelog

The version is bumped on every change: `FK_VERSION` and `FK_DATE` in `lib/fk_core.ulp`, the `VERSION` file and an entry here.
Numbering: `MAJOR.MINOR.PATCH` — new feature → MINOR, fix → PATCH.

---

## 2.1.0 — 2026-10-13

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
