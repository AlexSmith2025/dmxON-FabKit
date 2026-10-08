# История версий / Changelog

Версия меняется при каждой переделке: `FK_VERSION` и `FK_DATE` в `lib/fk_core.ulp`, файл `VERSION` и запись здесь.
The version is bumped on every change: `FK_VERSION` and `FK_DATE` in `lib/fk_core.ulp`, the `VERSION` file and an entry here.

Нумерация / Numbering: `MAJOR.MINOR.PATCH` — новая возможность → MINOR, исправление → PATCH.
New feature → MINOR, fix → PATCH.

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
