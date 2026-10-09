# История версий / Changelog

Версия меняется при каждой переделке: `FK_VERSION` и `FK_DATE` в `lib/fk_core.ulp`, файл `VERSION` и запись здесь.
The version is bumped on every change: `FK_VERSION` and `FK_DATE` in `lib/fk_core.ulp`, the `VERSION` file and an entry here.

Нумерация / Numbering: `MAJOR.MINOR.PATCH` — новая возможность → MINOR, исправление → PATCH.
New feature → MINOR, fix → PATCH.

---

## 2.0.2 — 2026-10-09

**Исправлено / Fixed**

- Проверка технологичности: слои, выходящие за контур платы (медь — ошибка; шелкография, маска, паста — предупреждение с величиной выхода).
  Manufacturability check: layers extending beyond the board outline (copper — error; silkscreen, mask, paste — warning with the overshoot).
- Шкала на листах ЛУТ — ровно 50 мм с учётом толщины линий (было 50.5 мм). Масштаб листов проверен измерением: контур 198 × 74 мм.
  The toner-sheet scale bar is exactly 50 mm including line width (was 50.5 mm). Sheet scale verified by measurement: outline 198 × 74 mm.
- Инструкция ЛУТ: исправлен не-ASCII символ в английском тексте.
  Toner instructions: a non-ASCII character in the English text fixed.

---

## 2.0.1 — 2026-10-08

**Исправлено / Fixed**

- Папки и имена с кириллицей: путь пакета, штамп и итоговое окно больше не искажаются (символы восстанавливаются по таблице, а не через 8-битный `char`).
  Cyrillic folders and names: the package path, title block and summary window are no longer garbled (characters are restored from a table instead of an 8-bit `char`).
- Архив Gerber и импорт XLSX в папках с кириллицей: `tar.exe` работает из временной папки с латинскими именами.
  Gerber zip and XLSX import in Cyrillic folders: `tar.exe` now runs from the temp folder with Latin names.
- Служебные команды больше не открывают окна консоли/Терминала (запуск через `wscript`, без окна); ожидание PDF — без мигающих окон.
  Helper commands no longer pop up console/Terminal windows (run via windowless `wscript`); PDF waiting without flashing windows.
- Если папку пакета создать нельзя — понятное сообщение сразу, а не цепочка ошибок.
  If the package folder cannot be created — a clear message right away instead of a chain of errors.
- Настоящие детали с посадочным местом без пасты (например, диод SOD-123) остаются в BOM/CPL с предупреждением, а не исключаются как перемычки.
  Real parts whose footprint has no paste (e.g. an SOD-123 diode) stay in BOM/CPL with a warning instead of being dropped as jumpers.
- Вывод 1: точное имя «1» главнее переходных отверстий теплоотвода `P$1`; шаг выводов — по SMD-площадкам (QFN, DPAK).
  Pin 1: the exact name «1» wins over thermal vias named `P$1`; lead pitch is taken from SMD pads (QFN, DPAK).
- Керамические чипы 0402…2512 не попадают в лист «Ключи и полярность».
  Ceramic chips 0402…2512 no longer appear on the «Pin 1 and polarity» sheet.
- Таблица посадочных мест не показывает пары кандидатов в замены.
  The footprint table no longer lists substitute-candidate pairs.
- Таблицы порядка пайки не заходят под штамп; колонки заполняются поровну.
  Soldering-step tables no longer run under the title block; columns are balanced.
- Диалог помещается на экран 1024×768: подписи в две строки, короче вкладки.
  The dialog fits a 1024×768 screen: two-line labels, shorter tabs.
- Импорт: текст со страницы заказа JLCPCB распознаётся раньше таблицы CSV.
  Import: text copied from the JLCPCB order page is recognised before CSV.

---

## 2.0.0 — 2026-10-08

Первый выпуск dmxON FabKit. / First release of dmxON FabKit.

**Новое / New**

- Производственный пакет одной командой: Gerber + BOM + CPL + отчёт + документация A4 + листы ЛУТ.
  One-run production package: Gerber + BOM + CPL + report + A4 documentation + toner sheets.
- Gerber под JLCPCB: имена Protel (GTL, GBL, G1…, GTS, GTP, GTO, GKO, XLN), архив для загрузки, определение слоёв, толщины, мин. линии и отверстия.
  JLCPCB Gerber: Protel names, upload zip, detection of layers, thickness, min track and hole.
- Собственный разбор Gerber RS-274X и Excellon: превью слоёв, реалистичный вид платы, карта сверловки.
  Own Gerber RS-274X and Excellon parser: layer previews, realistic board render, drill map.
- Проверка технологичности против возможностей JLCPCB (ширина линий, отверстия, тонкая графика в меди).
  Manufacturability check against JLCPCB capabilities (track width, holes, thin copper artwork).
- Замены отсутствующих деталей с проверкой по площадкам платы и выбором самой дешёвой.
  Substitutes for missing parts, checked against the board pads, cheapest wins.
- Цены каталога, стоимость тиража, плата за катушки Extended.
  Catalogue prices, batch cost, Extended feeder fees.
- Импорт готовой BOM JLCPCB (xlsx, csv, текст со страницы заказа).
  Import of a finished JLCPCB BOM (xlsx, csv, order-page text).
- Документация A4: титул с содержанием, параметры изготовления, слои, сборочные чертежи в стандартном масштабе, порядок пайки по шагам, ключи и полярность, спецификация; рамка и штамп, поля правятся в браузере; PDF через Microsoft Edge.
  A4 documentation: cover with contents, fabrication spec, layers, assembly drawings at standard scale, soldering steps, pin-1/polarity keys, BOM; frame and title block editable in the browser; PDF via Microsoft Edge.
- Листы ЛУТ 1:1 из Gerber: медь, шелкография, УФ-маска, карта сверловки; шкала 50 мм.
  1:1 toner-transfer sheets from Gerber: copper, silkscreen, UV mask, drill guide; 50 mm scale bar.
- Весь вывод на русском и английском. / All output in Russian and English.
- Диалог с вкладками, штамп для каждой платы, пакетный режим. / Tabbed dialog, per-board title block, batch mode.
- Пакет платы пересоздаётся целиком; удаляются только папки с меткой FabKit.
  The board package is rebuilt from scratch; only folders carrying the FabKit marker are deleted.

**Основа / Based on**

- Подбор номеров LCSC, сверка посадочных мест EasyEDA и поправки поворота CPL из предыдущего скрипта `jlcpcb_export.ulp` (1.x), переписанные модулями.
  LCSC selection, EasyEDA footprint verification and CPL rotation fixes from the earlier `jlcpcb_export.ulp` (1.x), rewritten as modules.
