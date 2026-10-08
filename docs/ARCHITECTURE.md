# Как устроен dmxON FabKit / How dmxON FabKit works

## Три фазы / Three phases

ULP не может сам дождаться выгрузки Gerber во Fusion, поэтому работа идёт в три фазы.
A ULP cannot wait for Fusion's Gerber export by itself, so the work runs in three phases.

```
Фаза 1 / Phase 1   dmxON_FabKit.ulp            (редактор платы / board editor)
  диалог → элементы, контур, площадки → строки BOM → каталог JLCPCB (curl) →
  посадочные места EasyEDA → замены → BOM/CPL → заготовки отчёта и документации →
  файл состояния → exit("<команды фазы 2>")
  dialog → elements, outline, pads → BOM lines → JLCPCB catalogue (curl) →
  EasyEDA footprints → substitutes → BOM/CPL → report and docs drafts →
  state file → exit("<phase 2 commands>")

Фаза 2 / Phase 2   команды Fusion / Fusion commands
  [ATTRIBUTE … LCSC_PART …]          по желанию / optional
  MANUFACTURING EXPORT '<tmp>/cam.zip'
  RUN dmxON_FabKit.ulp -finish '<tmp>/state.txt'

Фаза 3 / Phase 3   dmxON_FabKit.ulp -finish
  распаковка → имена JLCPCB → архив → разбор Gerber/Excellon → превью и вид платы →
  отчёт и документация из заготовок → PDF (Edge) → листы ЛУТ → index.html → метка папки
  unpack → JLCPCB names → zip → Gerber/Excellon parsing → previews and render →
  report and docs from drafts → PDF (Edge) → toner sheets → index.html → folder marker
```

Заготовки HTML содержат строки-метки (`<!--FK:RENDER-->`, `<!--FK:ORDER-->`, `<!--FK:GERBER-->`, `<!--FK:FABSPEC-->`, `<!--FK:LAYERS-->`, `<!--FK:COVERIMG-->`, `<!--FK:TOC-->`), третья фаза вставляет на их место готовые разделы; `{{SHEET}}`/`{{SHEETS}}` нумеруют листы.
HTML drafts carry marker lines that phase 3 replaces with finished sections; `{{SHEET}}`/`{{SHEETS}}` number the sheets.

## Модули / Modules (`lib/`)

| Файл / File | Назначение / Purpose |
|---|---|
| `fk_strings.ulp` | строки, CSV, HTML-сущности, пути / strings, CSV, HTML entities, paths |
| `fk_core.ulp` | версия, настройки, двуязычные строки, состояние между фазами / version, options, bilingual strings, cross-phase state |
| `fk_values.ulp` | номиналы R/C/L / component values |
| `fk_packages.ulp` | корпуса: имя на плате → корпус JLC, файл сопоставления / packages: board name → JLC package, mapping file |
| `fk_net.ulp` | запросы (netget/curl), JSON, поиск в каталоге, цены / requests, JSON, catalogue search, prices |
| `fk_candidates.ulp` | кандидаты номера изготовителя / manufacturer part number candidates |
| `fk_model.ulp` | данные элементов и строк BOM / element and BOM line data |
| `fk_lookup.ulp` | подбор номера для строки BOM / part selection for a BOM line |
| `fk_footprint.ulp` | посадочные места EasyEDA, совмещение площадок, CPL / EasyEDA footprints, pad alignment, CPL |
| `fk_subs.ulp` | замены / substitutes |
| `fk_draw.ulp` | контур, графика корпусов, шаги пайки, чертежи / outline, part graphics, soldering steps, drawings |
| `fk_gerber.ulp` | Gerber/Excellon: имена, разбор, SVG / names, parsing, SVG |
| `fk_import.ulp` | импорт BOM JLCPCB / JLCPCB BOM import |
| `fk_report.ulp` | отчёт HTML (фаза 1) / HTML report (phase 1) |
| `fk_docs.ulp` | листы A4 и штамп / A4 sheets and title block |
| `fk_finish.ulp` | фаза 3 / phase 3 |

## Особенности ULP во Fusion / ULP specifics in Fusion

- `output()` пишет в однобайтовой кодировке Windows: весь не-ASCII текст выводится числовыми ссылками HTML (`h()`, `asc()`), CSV — только ASCII.
  `output()` writes in the Windows ANSI code page: all non-ASCII text goes out as numeric HTML references, CSV stays ASCII.
- `netget`/`netpost` во Fusion не работают — запросы выполняет `curl.exe` одним пакетом.
  `netget`/`netpost` do not work in Fusion — requests run through a single `curl.exe` batch.
- Edge возвращает управление раньше, чем допишет PDF: фаза 3 ждёт, пока размер файла перестанет расти.
  Edge returns before the PDF is fully written: phase 3 waits until the file size stops growing.
- Картинки для PDF рисуются без SVG-масок (вырезы — цветом фона): маски в PDF понимают не все просмотрщики и принтеры.
  Images for PDFs avoid SVG masks (cut-outs are painted with the background colour): not every viewer or printer handles masks in PDFs.
- Командная строка Fusion принимает одну команду за раз; цепочка фазы 2 передаётся через `exit()`.
  Fusion's command line takes one command at a time; the phase-2 chain is passed via `exit()`.
