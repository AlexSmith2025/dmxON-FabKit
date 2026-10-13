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
  MANUFACTURING EXPORT '<tmp>/cam.zip'
  RUN dmxON_FabKit.ulp -finish '<tmp>/state.txt'

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
| `fk_docs.ulp` | A4 sheets and title block |
| `fk_finish.ulp` | phase 3 |

`INSTALL.ulp` (project root) copies the project to `Documents\dmxON\dmxON-FabKit` and adds it to `EAGLE:Directories.Ulp` through `cfgset`; Fusion applies directory changes after a restart.

## ULP specifics in Fusion

- `output()` writes in the Windows ANSI code page: all non-ASCII text goes out as numeric HTML references (`h()`, `asc()`), CSV stays ASCII.
- `netget`/`netpost` do not work in Fusion — requests run through a single `curl.exe` batch.
- Edge returns before the PDF is fully written: phase 3 waits until the file size stops growing.
- Images for PDFs avoid SVG masks (cut-outs are painted with the background colour): not every viewer or printer handles masks in PDFs.
- Fusion's command line takes one command at a time; the phase-2 chain is passed via `exit()`.
- ULP `char` is 8-bit: a Unicode character by code (`&#1058;` → «Т») is taken from literal tables (`uchar()` in `fk_core`: Cyrillic, Latin-1, Latin Extended-A, punctuation).
- Helper commands go through `dmxon_fabkit_run.vbs` (`wscript`, windowless): on Windows 11 every console call would otherwise open a Terminal window. If Windows Script Host is disabled — fallback to `cmd.exe`.
- `tar.exe` cannot take Cyrillic arguments: archives are built and unpacked in the temp folder with Latin names (`cd /d` + relative paths).
