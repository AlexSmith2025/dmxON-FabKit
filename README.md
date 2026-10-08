# dmxON FabKit

**Полный производственный пакет JLCPCB из платы Fusion Electronics — одной командой.**
**A complete JLCPCB production package from a Fusion Electronics board — in one run.**

`v2.0.1` · 2026-10-08 · **dmxON by AlexSmith 2026** · [лицензия / license](LICENSE.md)

---

## Что делает / What it does

| | Русский | English |
|---|---|---|
| 🏭 | **Gerber и сверловка под JLCPCB**: имена GTL/GBL/G1…/GTS/GTP/GTO/GKO/XLN, архив для загрузки, слои и параметры платы определяются сами | **Gerber and drill for JLCPCB**: GTL/GBL/G1…/GTS/GTP/GTO/GKO/XLN names, an upload-ready zip, layers and board parameters detected automatically |
| 🧾 | **BOM и CPL для сборки** с автоматическим подбором номеров LCSC (резисторы и конденсаторы — по номиналу, корпусу и напряжению; остальное — по номеру изготовителя) | **BOM and CPL for assembly** with automatic LCSC part selection (resistors and capacitors by value, package and voltage; everything else by manufacturer part number) |
| 📐 | **Сверка посадочных мест** с библиотекой JLC (EasyEDA): поворот и центр в CPL берутся из совмещения площадок, зеркальные и неподходящие корпуса помечаются | **Footprint verification** against the JLC (EasyEDA) library: CPL rotation and centre come from pad alignment, mirrored and non-fitting packages are flagged |
| 🔁 | **Замены**: если детали нет в каталоге, нет на складе или корпус не подходит — ищется аналог, проверяется по площадкам платы и выбирается самый дешёвый | **Substitutes**: if a part is missing, out of stock or its package does not fit, an alternative is found, checked against the board pads and the cheapest one wins |
| 💲 | **Стоимость**: цены каталога на весь тираж, плата за катушки Extended, самые дорогие позиции | **Cost**: catalogue prices for the whole batch, Extended feeder fees, the most expensive lines |
| 📊 | **Отчёт HTML**: реалистичный вид платы (слои раздвигаются при наведении), переключатели слоёв, галерея Gerber, сверловка, проверка технологичности, расстановка с обозначениями | **HTML report**: realistic board render (layers explode on hover), layer toggles, Gerber gallery, drilling, manufacturability check, placement with designators |
| 📄 | **Документация A4** для ручной сборки: титул, параметры изготовления, слои, сборочные чертежи в стандартном масштабе, порядок пайки по шагам, ключи микросхем, спецификация; рамка и штамп с правкой прямо в браузере; PDF | **A4 documentation** for manual assembly: cover, fabrication spec, layers, assembly drawings at standard scale, step-by-step soldering order, IC keys, BOM; frame and title block editable right in the browser; PDF |
| 🖨️ | **ЛУТ 1:1**: PDF каждого слоя для переноса тонером (медь, шелкография, маска, сверловка), верх уже зеркальный, шкала 50 мм для проверки масштаба | **Toner transfer 1:1**: a PDF per layer (copper, silkscreen, mask, drill), top sheets already mirrored, a 50 mm bar to check the scale |
| 📥 | **Импорт готовой BOM JLCPCB** (`Download Selected Parts List`, любой CSV/XLSX с Designator и LCSC или текст со страницы заказа) — ваши проверенные номера главнее атрибутов | **Import a finished JLCPCB BOM** (`Download Selected Parts List`, any CSV/XLSX with Designator and LCSC, or text copied from the order page) — your verified part numbers win over attributes |
| 🌐 | Всё — на русском и английском | Everything in Russian and English |

---

## Требования / Requirements

- **Autodesk Fusion** (Electronics) на **Windows 10/11**; работает и в EAGLE 9.
  **Autodesk Fusion** (Electronics) on **Windows 10/11**; also runs in EAGLE 9.
- **Microsoft Edge** (есть в Windows) — для PDF. / for PDFs.
- `curl.exe` и `tar.exe` — встроены в Windows 10/11. / built into Windows 10/11.
- Интернет — для каталога JLCPCB и посадочных мест EasyEDA (без него всё остальное работает).
  Internet — for the JLCPCB catalogue and EasyEDA footprints (everything else works offline).

---

## Установка / Installation

1. Скачайте последнюю версию со страницы [Releases](https://github.com/AlexSmith2025/dmxON-FabKit/releases/latest) (архив **Source code (zip)**) и распакуйте в любую папку, например `Documents\dmxON-FabKit`.
   Download the latest version from [Releases](https://github.com/AlexSmith2025/dmxON-FabKit/releases/latest) (**Source code (zip)**) and unpack it anywhere, e.g. `Documents\dmxON-FabKit`.
2. Структуру не меняйте: `dmxON_FabKit.ulp` ищет модули в `lib\` и настройки в `config\` рядом с собой.
   Keep the layout: `dmxON_FabKit.ulp` loads its modules from `lib\` and settings from `config\` next to it.
3. По желанию добавьте папку в пути ULP: **Electronics → Preferences → Directories → ULPs**.
   Optionally add the folder to the ULP paths: **Electronics → Preferences → Directories → ULPs**.

---

## Быстрый старт / Quick start

1. Откройте **плату** (Board) в Fusion Electronics. / Open the **board** in Fusion Electronics.
2. Запустите / Run: **Automation → Run ULP → `dmxON_FabKit.ulp`**
   или в командной строке / or in the command line: `RUN 'C:/путь/path/dmxON_FabKit.ulp'`
3. В диалоге выберите папку и нажмите **Создать пакет / Build package**.
   Choose the folder in the dialog and press **Build package**.
4. Fusion может показать окно **CAM Export File List** — нажмите **OK** (это штатная выгрузка Gerber).
   Fusion may show a **CAM Export File List** window — press **OK** (that is the regular Gerber export).
5. Через минуту откроется папка пакета. Начните с `index.html`.
   About a minute later the package folder opens. Start with `index.html`.

### Диалог / Dialog

| Вкладка / Tab | Что настраивается / What it sets |
|---|---|
| **Выгрузка / Output** | папка; что создать: Gerber, документацию A4, PDF, листы ЛУТ; что идёт в BOM/CPL: THT, центр площадок, исключаемые обозначения / folder; what to build: Gerber, A4 docs, PDF, toner sheets; what goes into BOM/CPL: THT, pad centre, skipped designators |
| **Детали / Parts** | поиск в каталоге, Basic/Preferred, замены, сверка посадочных мест, перепроверка атрибутов, запись `LCSC_PART`, число плат, мин. напряжение конденсаторов, плата за катушку, импорт BOM / catalogue search, Basic/Preferred, substitutes, footprint check, attribute re-check, writing `LCSC_PART`, board quantity, min capacitor voltage, feeder fee, BOM import |
| **Плата / PCB** | толщина, цвет маски и шелкографии, покрытие — для отчёта, формы заказа и вида платы / thickness, mask and silk colour, finish — for the report, the order form and the render |
| **Штамп / Title** | изделие, обозначение, редакция, заказчик, примечание (у каждой платы свои); организация и подписи (общие) / product, document No., revision, customer, note (per board); company and signatures (shared) |
| **Инфо / About** | версия, автор, лицензия / version, author, license |

Все настройки запоминаются. / All settings are remembered.

---

## Что получается / Output

```
<плата>_FabKit/                         <board>_FabKit/
├── index.html                          стартовая страница / start page
├── 01_JLCPCB_ORDER/
│   ├── JLCPCB_GERBER/
│   │   ├── <плата>_Gerber_JLCPCB.zip   ← загрузить на jlcpcb.com / upload to jlcpcb.com
│   │   └── unpacked/                   те же файлы для просмотра / same files for review
│   ├── <плата>_JLCPCB_BOM.csv          ← PCB Assembly: BOM
│   └── <плата>_JLCPCB_CPL.csv          ← PCB Assembly: CPL
├── 02_REPORT/
│   ├── <плата>_Report.html             отчёт / report
│   └── img/                            превью слоёв / layer previews
├── 03_ASSEMBLY_DOCS/
│   ├── <плата>_Assembly_A4.html        правка штампа в браузере / edit the title block in the browser
│   └── <плата>_Assembly_A4.pdf
└── 04_TONER_TRANSFER_1to1/
    ├── HOW_TO_PRINT.html
    ├── <плата>_01_TOP_COPPER_mirrored.pdf
    ├── <плата>_02_BOTTOM_COPPER.pdf
    ├── <плата>_03_TOP_SILK_mirrored.pdf
    ├── <плата>_04_BOTTOM_SILK.pdf
    ├── <плата>_05_TOP_SOLDERMASK_UV_mirrored.pdf
    ├── <плата>_06_BOTTOM_SOLDERMASK_UV.pdf
    └── <плата>_07_DRILL_GUIDE.pdf
```

При каждом запуске пакет платы **удаляется и создаётся заново** — но только если папку создал FabKit (в ней есть метка `.dmxon-fabkit`). Чужую папку с тем же именем FabKit не тронет: спросит или создаст новую с датой.
Every run **deletes and rebuilds** the board's package — but only if FabKit created that folder (it holds a `.dmxon-fabkit` marker). A foreign folder with the same name is never touched: FabKit asks or creates a new dated folder.

---

## Заказ на JLCPCB / Ordering at JLCPCB

1. **jlcpcb.com → Order now → Add gerber file** → `01_JLCPCB_ORDER/JLCPCB_GERBER/<плата>_Gerber_JLCPCB.zip`.
2. Параметры платы — из отчёта (раздел «Заказ»). / PCB parameters — from the report («Order» section).
3. **PCB Assembly** → BOM `…_JLCPCB_BOM.csv`, CPL `…_JLCPCB_CPL.csv`.
4. В предпросмотре JLCPCB проверьте детали из раздела отчёта **«Требуют внимания»**.
   In the JLCPCB preview check the parts listed under **«Need attention»** in the report.

---

## Номера деталей / Part numbers

Порядок / Order of precedence:

1. **Импорт BOM** (вкладка «Детали» или `-import файл`). / **BOM import** (Parts tab or `-import file`).
2. **Атрибут** на детали: `LCSC_PART`, `LCSC`, `JLCPCB_PART`, `JLC` … / **Attribute** on the part.
3. **Подбор по каталогу JLCPCB**: R/C — по номиналу, корпусу и напряжению (мин. напряжение задаётся), остальные — по номеру изготовителя из номинала или атрибута `MPN`/`MANUFACTURER_PART_NUMBER`.
   **JLCPCB catalogue search**: R/C by value, package and voltage (minimum voltage configurable), others by the manufacturer part number from the value or an `MPN`/`MANUFACTURER_PART_NUMBER` attribute.
4. **Замена**, если детали нет, нет на складе или корпус не подходит. / **Substitute** if missing, out of stock or the package does not fit.

Полезные атрибуты / Useful attributes: `JLC_PACKAGE`, `JLC_ROTATION`, `JLC_COMMENT`, `VOLTAGE`, `DNP` / `JLC_EXCLUDE`, `BOM=EXCLUDE`.
Своё сопоставление корпусов и поправок поворота — в `config/fk_package_map.txt`. / Own package and rotation mapping — `config/fk_package_map.txt`.

---

## ЛУТ / Toner transfer

- Листы строятся из **тех же Gerber**, что уходят на завод: заливки, зазоры и вырезы точные; белые точки — центры отверстий.
  Sheets are built from **the same Gerber files** the factory gets: pours, clearances and cut-outs are exact; white dots mark drill centres.
- Печать: лазерный принтер, **100 % / «Фактический размер»**, без «Вписать в страницу». Проверьте шкалу 50 мм.
  Print on a laser printer at **100 % / Actual size**, never «Fit to page». Check the 50 mm bar.
- Верх уже зеркальный, низ — нет (так и нужно). / Top sheets are mirrored, bottom ones are not (as intended).

---

## Пакетный режим / Batch mode

```
RUN dmxON_FabKit.ulp -batch <папка/folder> [-offline] [-boards N] [-import file] [-nogerber] [-nodocs] [-notoner] [-nopdf] [-keep]
```

| Ключ / Flag | Значение / Meaning |
|---|---|
| `-batch <folder>` | без диалога, в эту папку, атрибуты не пишутся / no dialog, into this folder, no attribute writes |
| `-offline` | без каталога и EasyEDA / no catalogue and EasyEDA |
| `-boards N` | плат в заказе / boards in the order |
| `-import <file>` | BOM JLCPCB (xlsx/csv/txt) |
| `-nogerber -nodocs -notoner -nopdf` | пропустить часть пакета / skip part of the package |
| `-keep` | оставить временную папку для разбора / keep the temp folder for debugging |

---

## Если что-то не так / Troubleshooting

| Симптом / Symptom | Что делать / What to do |
|---|---|
| Окно **CAM Export File List** | нажать **OK**: это подтверждение выгрузки Gerber во Fusion / press **OK**: Fusion asks to confirm the Gerber export |
| «Каталог JLCPCB не ответил» / «catalogue did not answer» | проверьте интернет и прокси; без сети пакет всё равно собирается / check internet and proxy; the package is still built offline |
| Нет PDF / No PDF | нужен Microsoft Edge (или Chrome) в стандартной папке / Microsoft Edge (or Chrome) must be installed in its default folder |
| «Требуют внимания» / «Need attention» | прочитайте каждую строку: там напряжения, полярность, цоколёвка, склад / read every line: voltages, polarity, pinout, stock |

---

## Как устроено / How it works

Подробно — [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md). Коротко: фаза 1 (ULP) анализирует плату и пишет BOM/CPL и заготовки, фаза 2 (команды Fusion) делает `MANUFACTURING EXPORT`, фаза 3 (тот же ULP с `-finish`) собирает Gerber, превью, отчёт, документацию и листы ЛУТ.
Details — [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md). In short: phase 1 (ULP) analyses the board and writes BOM/CPL and drafts, phase 2 (Fusion commands) runs `MANUFACTURING EXPORT`, phase 3 (the same ULP with `-finish`) builds Gerber, previews, report, documentation and toner sheets.

История версий / Changelog — [CHANGELOG.md](CHANGELOG.md).

---

## Лицензия / License

Бесплатно с указанием автора; копирование кода, изменение и коммерческое использование запрещены — см. [LICENSE.md](LICENSE.md).
Free to use with attribution; copying the code, modification and commercial use are not permitted — see [LICENSE.md](LICENSE.md).

**dmxON by AlexSmith 2026**
