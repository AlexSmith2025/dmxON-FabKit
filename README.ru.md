<p align="center">
  <img src="docs/assets/banner.svg" alt="dmxON FabKit — из платы Autodesk Fusion Electronics в полный заказ JLCPCB" width="100%">
</p>

<p align="center">
  <a href="https://github.com/AlexSmith2025/dmxON-FabKit-Fusion-Electronics/releases/latest"><img src="https://img.shields.io/github/v/release/AlexSmith2025/dmxON-FabKit-Fusion-Electronics?style=for-the-badge&color=b4744a&label=release" alt="Последняя версия"></a>
  <a href="https://github.com/AlexSmith2025/dmxON-FabKit-Fusion-Electronics/releases"><img src="https://img.shields.io/github/downloads/AlexSmith2025/dmxON-FabKit-Fusion-Electronics/total?style=for-the-badge&color=24574a&label=downloads" alt="Скачиваний"></a>
  <img src="https://img.shields.io/badge/Autodesk%20Fusion-Electronics-e2ab7f?style=for-the-badge&logo=autodesk&logoColor=white" alt="Autodesk Fusion Electronics">
  <img src="https://img.shields.io/badge/Windows-10%20%7C%2011-3b4a5a?style=for-the-badge" alt="Windows 10 | 11">
  <a href="https://www.paypal.com/donate/?business=smith.show2025%40gmail.com&no_recurring=0&item_name=dmxON+FabKit&currency_code=EUR"><img src="https://img.shields.io/badge/PayPal-%D0%BF%D0%BE%D0%B4%D0%B4%D0%B5%D1%80%D0%B6%D0%B0%D1%82%D1%8C-003087?style=for-the-badge&logo=paypal&logoColor=white" alt="Поддержать через PayPal"></a>
</p>

<p align="center">
  <a href="https://github.com/AlexSmith2025/dmxON-FabKit-Fusion-Electronics/releases/latest/download/dmxON-FabKit.zip"><img src="https://img.shields.io/badge/%E2%AC%87%20%D0%A1%D0%BA%D0%B0%D1%87%D0%B0%D1%82%D1%8C-dmxON--FabKit.zip-b4744a?style=for-the-badge" alt="Скачать последнюю версию"></a>
</p>

<p align="center">
  <a href="README.md">English</a> · <b>Русский</b> · <a href="README.es.md">Español</a> · <a href="README.de.md">Deutsch</a> · <a href="README.pl.md">Polski</a>
</p>

<p align="center">
  <a href="#установка">Установка</a> ·
  <a href="#быстрый-старт">Быстрый старт</a> ·
  <a href="#совместимость">Совместимость</a> ·
  <a href="#что-получается">Что получается</a> ·
  <a href="#заказ-на-jlcpcb">Заказ</a> ·
  <a href="#поддержать-проект">Поддержать</a>
</p>

**dmxON FabKit — ULP для Autodesk Fusion Electronics (Fusion 360 Electronics), который за один запуск делает из платы полный заказ JLCPCB: архив Gerber с именами JLCPCB, BOM и CPL с автоматическим подбором деталей LCSC и заменами, интерактивный отчёт, документацию A4 для ручной сборки и листы ЛУТ 1:1.**

<p align="center">
  <a href="https://www.paypal.com/donate/?business=smith.show2025%40gmail.com&no_recurring=0&item_name=dmxON+FabKit&currency_code=EUR"><img src="docs/assets/donate.ru.svg" alt="Поддержать dmxON FabKit через PayPal — smith.show2025@gmail.com" width="760"></a>
</p>

---

## Что делает

| | |
|---|---|
| 🏭 | **Gerber и сверловка под JLCPCB**: имена GTL/GBL/G1…/GTS/GTP/GTO/GKO/XLN, архив для загрузки; слои и параметры платы определяются сами |
| 🧾 | **BOM и CPL для монтажа** с автоматическим подбором деталей LCSC — резисторы и конденсаторы по номиналу, корпусу и напряжению, остальное по номеру производителя |
| 📐 | **Сверка посадочных мест** с библиотекой JLC (EasyEDA): поворот и центр в CPL — по совмещению площадок; зеркальные и неподходящие корпуса отмечаются |
| 🔁 | **Замены**: если детали нет, нет на складе или корпус не подходит — ищется аналог, сверяется с площадками платы, побеждает самый дешёвый |
| 💲 | **Стоимость**: цены каталога на весь тираж, плата за катушки Extended, самые дорогие строки |
| 📊 | **Отчёт HTML**: реалистичный вид платы, переключение слоёв, галерея Gerber, сверловка, проверка технологичности, расстановка с обозначениями |
| 📄 | **Документация A4** для ручной сборки: титул, параметры изготовления, слои, сборочные чертежи в стандартном масштабе, порядок пайки по шагам, ключи микросхем, BOM; редактируемый штамп; PDF |
| 🖨️ | **ЛУТ 1:1**: PDF на каждый слой (медь, шелкография, маска, сверловка), верхние листы зеркальные, шкала 50 мм для проверки масштаба |
| 📥 | **Импорт готовой BOM JLCPCB** (xlsx, csv или текст со страницы заказа) — проверенные вами номера главнее |
| 🌐 | **5 языков**: английский, русский, испанский, немецкий, польский — диалог, отчёт и вся документация на выбранном языке |

---

## Совместимость

| | dmxON FabKit |
|---|---|
| **Autodesk Fusion (Electronics), Windows 10/11** | ✅ проверено на Fusion **2705.1.11** (октябрь 2026) |
| Autodesk Fusion на macOS | ❌ нужны инструменты Windows (`curl.exe`, `tar.exe`, `robocopy`, Windows Script Host, Microsoft Edge) |
| EAGLE 9.x | ❌ для Gerber нужна команда Fusion `MANUFACTURING EXPORT` |
| KiCad, Altium, EasyEDA | ❌ |

Ещё нужно: **Microsoft Edge** (есть в Windows) для PDF; интернет для каталога JLCPCB и посадочных мест EasyEDA (всё остальное работает без сети). Если новая сборка Fusion что-то сломала — [напишите в issues](https://github.com/AlexSmith2025/dmxON-FabKit-Fusion-Electronics/issues).

---

## Установка

1. [**Скачайте `dmxON-FabKit.zip`**](https://github.com/AlexSmith2025/dmxON-FabKit-Fusion-Electronics/releases/latest/download/dmxON-FabKit.zip) и распакуйте куда угодно.
2. В Fusion Electronics: **Automation → Run ULP → `INSTALL.ulp`** из распакованной папки, выберите язык и нажмите **Установить**.
3. **Перезапустите Fusion.** `dmxON_FabKit` появится в списке **Run ULP** рядом со встроенными — его папка `Документы\dmxON\dmxON-FabKit` идёт первой, встроенные ULP Fusion остаются на месте.

Установщик копирует проект в `Документы\dmxON\dmxON-FabKit` и добавляет эту папку в папки ULP через собственные настройки Fusion. Повторный запуск `INSTALL.ulp` обновляет файлы; **Удалить** возвращает Fusion прежние папки. Вручную: держите распакованную папку целиком (`dmxON_FabKit.ulp` берёт рядом `lib\` и `config\`) и запускайте `RUN 'C:/путь/dmxON_FabKit.ulp'`.

---

## Быстрый старт

1. Откройте **плату** в Fusion Electronics и **сохраните** её (Ctrl+S) — Gerber Fusion выгружает из последней сохранённой версии.
2. **Automation → Run ULP → `dmxON_FabKit`**.
3. В правом верхнем углу диалога выберите **язык** (по умолчанию английский), папку — и **Создать пакет**.
4. Fusion может показать окно **CAM Export File List** — нажмите **OK** (это обычная выгрузка Gerber).
5. Примерно через минуту откроется папка пакета. Начните с `index.html`.

Совет: сначала запустите [**dmxON JLC Rules**](https://github.com/AlexSmith2025/dmxON-JLC-Rules-Fusion-Electronics) — он настроит правила JLCPCB и стек слоёв, а толщину платы и цвет маски передаст в FabKit. Язык у обоих инструментов общий.

### Диалог

| Вкладка | Что задаёт |
|---|---|
| **Язык** (справа сверху) | English, Русский, Español, Deutsch, Polski — диалог переключается сразу; отчёт и документация пишутся на том же языке |
| **Выгрузка** | папка; что создать: Gerber, документацию A4, PDF, листы ЛУТ; что идёт в BOM/CPL: THT, центр площадок, пропускаемые обозначения |
| **Детали** | поиск в каталоге, Basic/Preferred, замены, сверка посадочных мест, перепроверка атрибутов, запись `LCSC_PART`, число плат, мин. напряжение конденсаторов, плата за катушку, импорт BOM |
| **Плата** | толщина, цвет маски и шелкографии, покрытие — для отчёта, формы заказа и вида платы |
| **Штамп** | изделие, обозначение, редакция, заказчик, примечание (для платы); организация и подписи (общие) |
| **Инфо** | версия, автор, лицензия, ссылки |

Все настройки запоминаются.

---

## Что получается

```
<плата>_FabKit/
├── index.html                          стартовая страница
├── 01_JLCPCB_ORDER/
│   ├── JLCPCB_GERBER/
│   │   ├── <плата>_Gerber_JLCPCB.zip   ← загрузить на jlcpcb.com
│   │   └── unpacked/                   те же файлы для просмотра
│   ├── <плата>_JLCPCB_BOM.csv          ← PCB Assembly: BOM
│   └── <плата>_JLCPCB_CPL.csv          ← PCB Assembly: CPL
├── 02_REPORT/                          отчёт + превью слоёв
├── 03_ASSEMBLY_DOCS/                   документация A4 (HTML + PDF)
└── 04_TONER_TRANSFER_1to1/             HOW_TO_PRINT + 7 листов PDF
```

Каждый запуск **удаляет и создаёт заново** пакет платы — но только если папку создал FabKit (в ней метка `.dmxon-fabkit`). Чужая папка с тем же именем не трогается.

---

## Заказ на JLCPCB

1. **jlcpcb.com → Order now → Add gerber file** → `01_JLCPCB_ORDER/JLCPCB_GERBER/<плата>_Gerber_JLCPCB.zip`.
2. Параметры платы — из отчёта (раздел «Заказ»).
3. **PCB Assembly** → BOM `…_JLCPCB_BOM.csv`, CPL `…_JLCPCB_CPL.csv`.
4. В предпросмотре JLCPCB проверьте детали из раздела отчёта **«Требуют внимания»**.

### Номера деталей — что главнее

1. **Импорт BOM** (вкладка «Детали» или `-import файл`).
2. **Атрибут** детали: `LCSC_PART`, `LCSC`, `JLCPCB_PART`, `JLC` …
3. **Поиск в каталоге JLCPCB**: R/C по номиналу, корпусу и напряжению; остальное по номеру производителя из номинала или атрибута `MPN` / `MANUFACTURER_PART_NUMBER`.
4. **Замена**, если детали нет, нет на складе или корпус не подходит.

Полезные атрибуты: `JLC_PACKAGE`, `JLC_ROTATION`, `JLC_COMMENT`, `VOLTAGE`, `DNP` / `JLC_EXCLUDE`, `BOM=EXCLUDE`. Свои соответствия корпусов и поворотов — `config/fk_package_map.txt`.

---

## ЛУТ

Листы строятся из **тех же Gerber**, что уходят на завод: заливки, зазоры и вырезы точные; белые точки — центры отверстий. Печать на лазерном принтере в масштабе **100 % («Фактический размер»)**, без «Вписать в страницу»; проверьте шкалу 50 мм. Верхние листы зеркальные, нижние — нет.

---

## Пакетный режим

```
RUN dmxON_FabKit.ulp -batch <папка> [-lang en|ru|es|de|pl] [-offline] [-boards N] [-import файл] [-nogerber] [-nodocs] [-notoner] [-nopdf] [-keep]
```

| Ключ | Что значит |
|---|---|
| `-batch <папка>` | без диалога, в эту папку, атрибуты не пишутся |
| `-lang <код>` | язык отчёта и документации (по умолчанию — последний выбранный в диалоге) |
| `-offline` | без каталога и EasyEDA |
| `-boards N` | плат в заказе |
| `-import <файл>` | BOM JLCPCB (xlsx/csv/txt) |
| `-nogerber -nodocs -notoner -nopdf` | пропустить часть пакета |
| `-keep` | оставить временную папку для отладки |

---

## Если что-то не так

| Что видно | Что делать |
|---|---|
| После установки `dmxON_FabKit` нет в списке Run ULP | перезапустите Fusion — список папок он читает при старте |
| Окно **CAM Export File List** | нажмите **OK**: Fusion просит подтвердить выгрузку Gerber |
| «Your PCB design has changed. CAM output is generated using the last saved version» | нажмите **Cancel**, сохраните плату (Ctrl+S) и запустите FabKit заново — иначе Gerber будет из старой сохранённой версии (например, без новых правил) |
| «каталог не ответил» | проверьте интернет и прокси; пакет всё равно соберётся без сети |
| Нет PDF | нужен Microsoft Edge (или Chrome) в стандартной папке |
| «Требуют внимания» | прочитайте каждую строку: напряжения, полярность, цоколёвка, склад |

---

## Как устроено

Фаза 1 (ULP) разбирает плату и пишет BOM/CPL и заготовки, фаза 2 (команды Fusion) запускает `MANUFACTURING EXPORT`, фаза 3 (тот же ULP с `-finish`) собирает Gerber, превью, отчёт, документацию и листы ЛУТ. Испанские, немецкие и польские тексты — в `lib/fk_lang.ulp`, он создаётся из `lang/strings.tsv`. Подробно: [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) · история версий: [CHANGELOG.md](CHANGELOG.md).

---

## Поддержать проект

dmxON FabKit **бесплатный**. За ним недели работы: разбор Gerber и Excellon, подбор деталей по каталогу JLCPCB, сверка посадочных мест, документация на пяти языках и проверка на реальных заказах. Если он сэкономил вам вечер подготовки заказа, неверную деталь или неудачную сборку — поддержите дальнейшую работу: новые версии, изменения каталога JLCPCB и исправления под новые сборки Fusion.

<p align="center">
  <a href="https://www.paypal.com/donate/?business=smith.show2025%40gmail.com&no_recurring=0&item_name=dmxON+FabKit&currency_code=EUR"><img src="docs/assets/donate.ru.svg" alt="Поддержать dmxON FabKit через PayPal" width="760"></a>
</p>

<p align="center">
  <b>PayPal:</b> <a href="https://www.paypal.com/donate/?business=smith.show2025%40gmail.com&no_recurring=0&item_name=dmxON+FabKit&currency_code=EUR">smith.show2025@gmail.com</a> — любая сумма помогает. Спасибо! ⭐ Звезда на GitHub тоже помогает людям найти проект.
</p>

---

## Лицензия

Использование бесплатно с указанием автора; копирование кода, изменение и коммерческое использование запрещены — см. [LICENSE.md](LICENSE.md). JLCPCB и LCSC — товарные знаки их владельцев; проект с ними не связан.

**dmxON by AlexSmith 2026** · [dmxon512.com](https://dmxon512.com) · соседний проект: [dmxON JLC Rules](https://github.com/AlexSmith2025/dmxON-JLC-Rules-Fusion-Electronics)
