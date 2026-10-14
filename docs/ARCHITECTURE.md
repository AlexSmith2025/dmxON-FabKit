# How dmxON FabKit works

## Three phases

A ULP cannot wait for Fusion's Gerber export by itself, so the work runs in three phases.

```
Phase 1   dmxON_FabKit.ulp            (board editor)
  dialog → elements, outline, pads → BOM lines → JLCPCB catalogue (curl) →
  EasyEDA footprints → substitutes → BOM/CPL → report and docs drafts →
  state file → exit("<phase 2 commands>")

Phase 2   Fusion commands
  [ATTRIBUTE … LCSC_PART …]          optional
  MANUFACTURING EXPORT '<tmp>/cam.zip'       or, with the dmxON add-in and the dmxON JLCPCB
  RUN dmxON_FabKit.ulp -finish '<tmp>/state.txt'   CAM job: request «fabkit_cam» → Electron.mfgexport

Phase 3   dmxON_FabKit.ulp -finish
  unpack → JLCPCB names → zip → Gerber/Excellon parsing → previews and render →
  report and docs from drafts → PDF (Edge) → toner sheets → index.html → folder marker
```

HTML drafts carry marker lines (`<!--FK:RENDER-->`, `<!--FK:ORDER-->`, `<!--FK:GERBER-->`, `<!--FK:FABSPEC-->`, `<!--FK:LAYERS-->`, `<!--FK:COVERIMG-->`, `<!--FK:TOC-->`) that phase 3 replaces with finished sections; `<!--FK:PAGE title-->` lines feed the table of contents; `{{SHEET}}`/`{{SHEETS}}` number the sheets.

## Languages

- Every user-visible text is written in the code as a pair: `L("Russian", "English")`, or `Lf("…{0}…", "…{0}…", a, b, c)` for templates.
- `ui_lang` selects the language: 0 English (default), 1 Russian, 2 Spanish, 3 German, 4 Polish. English and Russian come straight from the code; Spanish, German and Polish are looked up by the English text in `lib/fk_lang.ulp` (hash table built on first use).
- `lib/fk_lang.ulp` is generated from `lang/strings.tsv` (columns `en ru es de pl`); edit the TSV, not the generated file. A missing translation falls back to English.
- The choice is stored in the Fusion setting `dmxon.lang`, shared with dmxON JLC Rules. Phase 1 writes it into the state file, so phase 3 uses the same language even with `-lang` in batch mode.
- Internal codes (for example where a part number came from) stay language-independent and are turned into text only for output.

## Modules (`lib/`)

| File | Purpose |
|---|---|
| `fk_strings.ulp` | strings, CSV, HTML entities, paths |
| `fk_lang.ulp` | Spanish, German and Polish texts (generated) |
| `fk_core.ulp` | version, options, language selection, files, cross-phase state |
| `fk_values.ulp` | component values R/C/L |
| `fk_packages.ulp` | packages: board name → JLC package, mapping file |
| `fk_net.ulp` | requests (netget/curl), JSON, catalogue search, prices |
| `fk_candidates.ulp` | manufacturer part number candidates |
| `fk_model.ulp` | element and BOM line data, notes and warnings |
| `fk_lookup.ulp` | part selection for a BOM line |
| `fk_footprint.ulp` | EasyEDA footprints, pad alignment, CPL |
| `fk_subs.ulp` | substitutes |
| `fk_draw.ulp` | outline, part graphics, soldering steps, drawings |
| `fk_gerber.ulp` | Gerber/Excellon: names, parsing, SVG |
| `fk_import.ulp` | JLCPCB BOM import |
| `fk_report.ulp` | HTML report (phase 1) |
| `fk_addin.ulp` | link to the dmxON add-in: heartbeat, request files, add-in version |
| `fk_sheet.ulp` | sheets per ISO 5457 / ISO 7200 or GOST R 2.104-2023: frames, grid zones, title blocks (forms 1, 2, 2a), elongated formats A3×n; documents of the set (identifiers, names) |
| `fk_sch.ulp` | circuit diagram (GOST Э3 / IEC 61082-1): the schematic as SVG on a sheet of the chosen standard |
| `fk_docs.ulp` | documentation set: specification (GOST R 2.106) or parts list (ISO 7573), assembly drawing with placed designators and detail sheets, list of elements, assembly instruction |
| `fk_finish.ulp` | phase 3: Gerber, fabrication drawing, document list, sheet numbering, PDF |

`INSTALL.ulp` (project root) copies the project to `Documents\dmxON\dmxON-FabKit` and installs the dmxON add-in, which registers the folder in Fusion's ULP list (see below). It also undoes the `EAGLE:Directories.*` entries written by 2.1.0 — Fusion does not read them.

## Documentation standards

`doc_std` (`dmxon.std`, shared with dmxON JLC Rules): 0 ISO, 1 GOST. ISO: document list → fabrication drawing → assembly drawing → parts list → circuit diagram → assembly instruction. GOST: specification → assembly drawing (СБ) → PCB drawing → circuit diagram (Э3) → list of elements (ПЭ3) → assembly instruction (ТИ). A sheet is one HTML line `<!--FK:PAGE key|id|type|title-->` + page; phase 3 counts `{{S:key}}` / `{{N:key}}` per document.

Assembly drawing: `lbl_place()` puts each designator inside the part when it fits at ≥ 1.8 mm on paper (ISO 3098), otherwise next to it without touching other designators or bodies. If some do not fit at the overview scale, a larger standard scale is searched and the side is split into detail sheets (zones A, B, … / А, Б, …) framed on the overview.

## Circuit diagram and two Fusion defects

- Symbol geometry read through an instance (`I.gate.symbol.wires/pins/texts…`) comes transformed twice: `p_read = M·(M·l + p) + p`. The true point is `M⁻¹·(p_read − p)`. `sc_collect()` checks 200 pins against the net wire ends both ways and applies the correction only where it matches (should Fusion fix this, the correction switches itself off). Smashed texts (`I.texts()`) and nets are correct.
- Any `polygons()` loop of a symbol stops the ULP. Symbol polygons are read from the schematic XML that Fusion keeps for the open document (`S.name`) with `xmlelements()` and placed with the instance transform.
- The user's frame (a `FRAME` device or a symbol with frames) is left out: frame and title block come from the standard. A wide schematic goes on A3×3 … A3×7 so that the text is at least ~1.3 mm on paper; a non-basic format is marked «*» in the GOST specification.

## The dmxON add-in (`fusion-addin/dmxON`)

A Fusion add-in in Python does what a ULP cannot. It is shared by dmxON FabKit and dmxON JLC Rules (both repositories carry the same copy; `INSTALL.ulp` installs the newer one into `%APPDATA%\Autodesk\Autodesk Fusion 360\API\AddIns\dmxON`).

- **Folders.** Fusion reads its ULP, design-rule and CAM folders from its own preferences (`ElectronUlpDirectory`, `ElectronDesignRulesDirectory`, `ElectronCamDirectory` in `NGlobalOptions.xml`), not from `EAGLE:Directories.*`. The add-in sets them with the text commands `Options.Set` + `Options.Save` + `Options.Reload` (effective at once): the dmxON folders of the installed tools first, Fusion's built-in folders after them. Fusion's preferences — and the ULP settings of `cfgset` — are shared by every computer of the Autodesk account, so the lists hold variables, not paths of one computer: `$HOME\dmxON\dmxON-FabKit`, `$HOME\dmxON\dmxON-JLC-Rules` (`$HOME` = this user's Documents) and `$EAGLEDIR\…` for Fusion's built-in folders (LibEagle of the running build); both tools are always listed so that computers do not rewrite the shared value back and forth, and paths of other computers (`C:\Users\<name>\…`, `webdeploy\production\<build>`) are converted. The ULPs take the user folder only from paths that exist on this computer (`local_home()`, `home_here()` in `fk_addin.ulp` / `jr_addin.ulp`).
- **The dmxON tab** in the PCB and schematic editors: FabKit, JLC Rules, Backup, Updates, Settings, Help. Buttons only queue a custom event; the work runs after the command ends (`Electron.run RUN '…'` for the ULPs).
- **Requests from ULPs.** A ULP writes a JSON file into `Documents\dmxON\.inbox` (`addin_request()` in `fk_addin.ulp` / `jr_addin.ulp`); a background thread notices it and fires a custom event, handled when Fusion is idle. `Documents\dmxON\.dmxon-addin` is a heartbeat refreshed every 30 s — `addin_alive()` tells a ULP whether the add-in runs.
  - `register` — re-apply the folders (after `INSTALL.ulp`).
  - `fabkit_cam` — Gerber through `Electron.mfgexport <dir> <camjob>` with the dmxON JLCPCB CAM job (no «CAM Export File List» window), zipped into FabKit's `cam.zip`, then `RUN dmxON_FabKit.ulp -finish …`.
  - `backup` — back up the design folder (below), adding the FabKit package.
  - `grid` — run a `GRID …` command in the schematic of the active board (dmxON JLC Rules sets the schematic grid), then return to the board.
- **Backup.** Every file of the active design's cloud folder (recursively): an Electronics design (`.fprj`) is opened and its schematic and board — found through `childReferences` — are written as EAGLE 9 files (`adsk.electron … exportManager.createEagleSchExportOptions / createEagleBrdExportOptions`); a schematic or board outside a design of the folder is opened through its parent design (opening it directly may ask which design to use); libraries → `.lbr`; 3D designs → Fusion archive `.f3d`; drawings → PDF; other files → `DataFile.download`. Documents opened on the way are closed again. Result: `Documents\dmxON\Backups\<project>\<folders>\<folder>_<date>.zip` with `manifest.json` (cloud id and version of every file) and `RESTORE.txt`; the newest N backups per folder are kept.
- **Updates.** Once a day (and on the Updates button) `https://api.github.com/repos/<repo>/releases/latest` is compared with the `VERSION` file of each installed tool; the release asset zip is unpacked over `Documents\dmxON\<tool>`; a newer add-in inside it replaces this one after a Fusion restart.
- **Language** of the add-in: its own setting, else `dmxon.lang` of the ULPs (read from Fusion's `electronoptiongroup_eagle.rc`), else the language sent with the last ULP request.


## ULP specifics in Fusion

- `output()` writes in the Windows ANSI code page: all non-ASCII text goes out as numeric HTML references (`h()`, `asc()`), CSV stays ASCII.
- `netget`/`netpost` do not work in Fusion — requests run through a single `curl.exe` batch.
- Edge returns before the PDF is fully written: phase 3 waits until the file size stops growing.
- Images for PDFs avoid SVG masks (cut-outs are painted with the background colour): not every viewer or printer handles masks in PDFs.
- Fusion's command line takes one command at a time; the phase-2 chain is passed via `exit()`.
- ULP `char` is 8-bit: a Unicode character by code (`&#1058;` → «Т») is taken from literal tables (`uchar()` in `fk_core`: Cyrillic, Latin-1, Latin Extended-A, punctuation).
- Helper commands go through `dmxon_fabkit_run.vbs` (`wscript`, windowless): on Windows 11 every console call would otherwise open a Terminal window. If Windows Script Host is disabled — fallback to `cmd.exe`.
- `tar.exe` cannot take Cyrillic arguments: archives are built and unpacked in the temp folder with Latin names (`cd /d` + relative paths).
