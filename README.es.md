<p align="center">
  <img src="docs/assets/banner.svg" alt="dmxON FabKit — de una placa de Autodesk Fusion Electronics a un pedido completo de JLCPCB" width="100%">
</p>

<p align="center">
  <a href="https://github.com/AlexSmith2025/dmxON-FabKit-Fusion-Electronics/releases/latest"><img src="https://img.shields.io/github/v/release/AlexSmith2025/dmxON-FabKit-Fusion-Electronics?style=for-the-badge&color=b4744a&label=release" alt="Última versión"></a>
  <a href="https://github.com/AlexSmith2025/dmxON-FabKit-Fusion-Electronics/releases"><img src="https://img.shields.io/github/downloads/AlexSmith2025/dmxON-FabKit-Fusion-Electronics/total?style=for-the-badge&color=24574a&label=downloads" alt="Descargas"></a>
  <img src="https://img.shields.io/badge/Autodesk%20Fusion-Electronics-e2ab7f?style=for-the-badge&logo=autodesk&logoColor=white" alt="Autodesk Fusion Electronics">
  <img src="https://img.shields.io/badge/Windows-10%20%7C%2011-3b4a5a?style=for-the-badge" alt="Windows 10 | 11">
  <a href="https://www.paypal.com/donate/?business=smith.show2025%40gmail.com&no_recurring=0&item_name=dmxON+FabKit&currency_code=EUR"><img src="https://img.shields.io/badge/PayPal-Donar-003087?style=for-the-badge&logo=paypal&logoColor=white" alt="Donar con PayPal"></a>
</p>

<p align="center">
  <a href="https://github.com/AlexSmith2025/dmxON-FabKit-Fusion-Electronics/releases/latest/download/dmxON-FabKit.zip"><img src="https://img.shields.io/badge/%E2%AC%87%20Descargar-dmxON--FabKit.zip-b4744a?style=for-the-badge" alt="Descargar la última versión"></a>
</p>

<p align="center">
  <a href="README.md">English</a> · <a href="README.ru.md">Русский</a> · <b>Español</b> · <a href="README.de.md">Deutsch</a> · <a href="README.pl.md">Polski</a>
</p>

<p align="center">
  <a href="#instalación">Instalación</a> ·
  <a href="#inicio-rápido">Inicio rápido</a> ·
  <a href="#compatibilidad">Compatibilidad</a> ·
  <a href="#resultado">Resultado</a> ·
  <a href="#pedido-en-jlcpcb">Pedido</a> ·
  <a href="#apoye-el-proyecto">Donar</a>
</p>

**dmxON FabKit es un ULP para Autodesk Fusion Electronics (Fusion 360 Electronics) que convierte una placa en un pedido completo de JLCPCB en una sola ejecución: zip de Gerber con nombres JLCPCB, BOM y CPL con selección automática de piezas LCSC y sustitutos, un informe interactivo, documentación A4 de montaje y hojas 1:1 para transferencia de tóner.**

<p align="center">
  <a href="https://www.paypal.com/donate/?business=smith.show2025%40gmail.com&no_recurring=0&item_name=dmxON+FabKit&currency_code=EUR"><img src="docs/assets/donate.es.svg" alt="Apoye dmxON FabKit con PayPal — smith.show2025@gmail.com" width="760"></a>
</p>

---

## Qué hace

| | |
|---|---|
| 🏭 | **Gerber y taladrado para JLCPCB**: nombres GTL/GBL/G1…/GTS/GTP/GTO/GKO/XLN y un zip listo para subir; capas y parámetros de la placa detectados automáticamente |
| 🧾 | **BOM y CPL para montaje** con selección automática de piezas LCSC — resistencias y condensadores por valor, encapsulado y tensión, el resto por número de pieza del fabricante |
| 📐 | **Verificación de huellas** con la biblioteca JLC (EasyEDA): rotación y centro del CPL a partir de la alineación de pads; se señalan encapsulados espejados o que no encajan |
| 🔁 | **Sustitutos**: si una pieza falta, no hay stock o su encapsulado no encaja, se busca una alternativa, se comprueba con los pads de la placa y gana la más barata |
| 💲 | **Coste**: precios del catálogo para todo el lote, tarifas de alimentador Extended, las líneas más caras |
| 📊 | **Informe HTML**: vista realista de la placa, conmutación de capas, galería Gerber, taladrado, comprobación de fabricabilidad, colocación con designadores |
| 📄 | **Documentación A4** para montaje manual: portada, especificación de fabricación, capas, planos de montaje a escala normalizada, orden de soldadura paso a paso, marcas de CI, BOM; cajetín editable; PDF |
| 🖨️ | **Transferencia de tóner 1:1**: un PDF por capa (cobre, serigrafía, máscara, taladrado), hojas superiores espejadas, barra de 50 mm para comprobar la escala |
| 📥 | **Importar una BOM de JLCPCB terminada** (xlsx, csv o texto de la página del pedido) — sus números verificados tienen prioridad |
| 🌐 | **5 idiomas**: inglés, ruso, español, alemán y polaco — el diálogo, el informe y toda la documentación en el idioma elegido |
| 📏 | **Documentación ISO o GOST**: hojas y cuadros de rotulación según ISO 5457 / ISO 7200 o GOST R 2.104-2023; lista de documentos, planos de fabricación y de montaje, lista de piezas (ISO 7573) o especificación (GOST R 2.106-2019), lista de elementos; referencias IPC e IEC en las notas |
| 🔌 | **Esquema eléctrico** a partir de su esquema, en el marco de la norma (GOST Э3 / IEC 61082-1), en A4, A3 o una hoja alargada A3×n para que el texto se lea |
| 🧩 | **Pestaña dmxON en Fusion** (complemento): FabKit, JLC Rules, copia de seguridad y actualizaciones con un clic; Gerber sin la ventana de confirmación de CAM |
| 💾 | **Copia de seguridad de toda la carpeta del diseño**: esquemas, placas y bibliotecas como archivos EAGLE, diseños 3D como `.f3d`, planos en PDF y el paquete; se restaura en cualquier cuenta u ordenador |
| 🔄 | **Actualizaciones desde GitHub**: comprobación diaria, instalación a petición |

---

## Compatibilidad

| | dmxON FabKit |
|---|---|
| **Autodesk Fusion (Electronics), Windows 10/11** | ✅ probado en Fusion **2705.1.30** (octubre de 2026) |
| Autodesk Fusion en macOS | ❌ usa herramientas de Windows (`curl.exe`, `tar.exe`, `robocopy`, Windows Script Host, Microsoft Edge) |
| EAGLE 9.x | ❌ necesita el comando `MANUFACTURING EXPORT` de Fusion para el Gerber |
| KiCad, Altium, EasyEDA | ❌ |

También hace falta: **Microsoft Edge** (incluido en Windows) para los PDF; internet para el catálogo de JLCPCB y las huellas de EasyEDA (todo lo demás funciona sin conexión). Si una nueva versión de Fusion rompe algo, [abra un issue](https://github.com/AlexSmith2025/dmxON-FabKit-Fusion-Electronics/issues).

---

## Instalación

1. [**Descargue `dmxON-FabKit.zip`**](https://github.com/AlexSmith2025/dmxON-FabKit-Fusion-Electronics/releases/latest/download/dmxON-FabKit.zip) y descomprímalo en cualquier carpeta.
2. En Fusion Electronics: **Automation → Run ULP → `INSTALL.ulp`** de la carpeta descomprimida, elija el idioma y pulse **Instalar**.
3. **Reinicie Fusion una vez.** Los editores de placa y esquema tendrán la pestaña **dmxON** — FabKit, JLC Rules, Copia, Actualizar, Ajustes, Ayuda — y `dmxON_FabKit` también estará en **Run ULP**.

El instalador copia el proyecto en `Documentos\dmxON\dmxON-FabKit` e instala el **complemento dmxON** (`%APPDATA%\Autodesk\Autodesk Fusion 360\API\AddIns\dmxON`). El complemento pone las carpetas dmxON las primeras en las listas de ULP, reglas de diseño y CAM de Fusion (Preferences → General → Electronics → Directory) — los ULP integrados se mantienen — y repara esas rutas tras las actualizaciones de Fusion. Ejecutar `INSTALL.ulp` de nuevo actualiza los archivos; **Eliminar** borra el proyecto copiado y, con la última herramienta dmxON, el complemento. Sin reiniciar, el complemento se inicia desde **Utilities → Add-Ins → Scripts and Add-Ins → dmxON → Run**. Alternativa manual sin complemento: conserve la carpeta descomprimida completa y ejecute `RUN 'C:/ruta/dmxON_FabKit.ulp'`.

**Varios ordenadores.** Fusion comparte sus preferencias —y los ajustes de FabKit— entre todos los ordenadores de su cuenta de Autodesk. Por eso el complemento guarda las carpetas como `$HOME\dmxON\…` y `$EAGLEDIR\…`, que Fusion expande en cada ordenador a sus propios Documentos y carpeta del programa, y FabKit ignora una carpeta de salida que pertenece a otro ordenador (usa `Escritorio\FabKit`). Ejecute `INSTALL.ulp` una vez en cada ordenador (o **dmxON → Actualizar** donde ya exista la pestaña) para que los archivos estén allí.

---

## Inicio rápido

1. Abra la **placa** en Fusion Electronics y **guárdela** (Ctrl+S): Fusion exporta el Gerber desde la última versión guardada.
2. Pulse **dmxON → FabKit** (o **Automation → Run ULP → `dmxON_FabKit`**).
3. Elija la **norma** (ISO o GOST) y el **idioma** arriba a la derecha, la carpeta, y pulse **Crear paquete**.
4. Con el complemento dmxON y dmxON JLC Rules instalados, el Gerber se exporta sin ventanas con el trabajo CAM dmxON JLCPCB. Sin ellos Fusion puede mostrar la ventana **CAM Export File List**: pulse **OK**.
5. Un minuto después se abre la carpeta del paquete. Empiece por `index.html`. Con la copia de seguridad activada, el complemento guarda después toda la carpeta del diseño en el paquete, en `05_BACKUP`.

Consejo: ejecute antes [**dmxON JLC Rules**](https://github.com/AlexSmith2025/dmxON-JLC-Rules-Fusion-Electronics) — configura las reglas de diseño de JLCPCB y la pila de capas, y pasa a FabKit el grosor de la placa y el color de la máscara. Ambas herramientas comparten el ajuste de idioma.

### El diálogo

| Pestaña | Qué ajusta |
|---|---|
| **Idioma** (arriba a la derecha) | English, Русский, Español, Deutsch, Polski — el diálogo cambia al instante; el informe y la documentación se escriben en el mismo idioma |
| **Norma** (arriba a la derecha) | ISO o GOST: qué documentación se genera; compartida con dmxON JLC Rules |
| **Salida** | carpeta; copia de seguridad de la carpeta del diseño; qué crear: Gerber, documentación, esquema eléctrico, PDF, hojas de tóner; qué va al BOM/CPL: THT, centro de pads, designadores omitidos |
| **Piezas** | búsqueda en el catálogo, Basic/Preferred, sustitutos, verificación de huellas, revisión de atributos, escritura de `LCSC_PART`, número de placas, tensión mínima de condensadores, tarifa de alimentador, importación de BOM |
| **Placa** | grosor, color de máscara y serigrafía, acabado — para el informe, el formulario de pedido y la vista |
| **Cajetín** | producto, n.º de documento, versión (Rev.), cliente, nota (por placa); empresa y firmas (comunes) |
| **Acerca de** | versión, autor, licencia, enlaces |

Todos los ajustes se recuerdan.

---

## Resultado

```
<placa>_v<versión>_FabKit/
├── index.html                          página de inicio
├── 01_JLCPCB_ORDER/
│   ├── JLCPCB_GERBER/
│   │   ├── <placa>_v<versión>_Gerber_JLCPCB.zip ← subir a jlcpcb.com
│   │   └── unpacked/                   los mismos archivos para revisar
│   ├── <placa>_v<versión>_JLCPCB_BOM.csv ← PCB Assembly: BOM
│   └── <placa>_v<versión>_JLCPCB_CPL.csv ← PCB Assembly: CPL
├── 02_REPORT/                          informe + vistas previas de capas
├── 03_ASSEMBLY_DOCS/                   documentación ISO o GOST (HTML + PDF)
├── 04_TONER_TRANSFER_1to1/             HOW_TO_PRINT + 7 hojas PDF
└── 05_BACKUP/                          copia de toda la carpeta del diseño (complemento dmxON)
```

Cada ejecución **borra y vuelve a crear** el paquete de la placa — pero solo si la carpeta la creó FabKit (contiene la marca `.dmxon-fabkit`). Una carpeta ajena con el mismo nombre nunca se toca.

**Una versión en todas partes.** La versión de la placa se guarda en el diseño como atributo global `REV` y se fija en el campo **Versión (Rev.)** de la pestaña **Cajetín**. Forma parte del nombre de la carpeta del paquete y de todos los archivos (`<placa>_v<versión>_…`, también los Gerber del zip), de los cajetines ISO y del informe. La primera vez, FabKit toma la versión impresa en la placa (un texto como «Ver. 1.4») o un `REV` que escribió antes —un `REV` de una plantilla de marco (a menudo «A») no se impone al texto de la placa— y la guarda en el diseño al pulsar OK. El informe avisa si el texto de la placa, `REV` y el paquete no coinciden. Los paquetes de distintas versiones conviven; una nueva ejecución solo reemplaza el paquete de la misma versión.

---

## Pedido en JLCPCB

1. **jlcpcb.com → Order now → Add gerber file** → `01_JLCPCB_ORDER/JLCPCB_GERBER/<placa>_Gerber_JLCPCB.zip`.
2. Parámetros de la placa — del informe (sección «Pedido»).
3. **PCB Assembly** → BOM `…_JLCPCB_BOM.csv`, CPL `…_JLCPCB_CPL.csv`.
4. En la vista previa de JLCPCB compruebe las piezas de la sección **«Requieren atención»** del informe.

### Números de pieza — orden de prioridad

1. **Importación de BOM** (pestaña Piezas o `-import archivo`).
2. **Atributo** de la pieza: `LCSC_PART`, `LCSC`, `JLCPCB_PART`, `JLC` …
3. **Búsqueda en el catálogo de JLCPCB**: R/C por valor, encapsulado y tensión; el resto por el número de pieza del fabricante tomado del valor o de un atributo `MPN` / `MANUFACTURER_PART_NUMBER`.
4. **Sustituto** si falta, no hay stock o el encapsulado no encaja.

Atributos útiles: `JLC_PACKAGE`, `JLC_ROTATION`, `JLC_COMMENT`, `VOLTAGE`, `DNP` / `JLC_EXCLUDE`, `BOM=EXCLUDE`. Correspondencias propias de encapsulados y rotaciones — `config/fk_package_map.txt`.

---

## Transferencia de tóner

Las hojas se generan a partir de **los mismos Gerber** que van a la fábrica: rellenos, separaciones y recortes son exactos; los puntos blancos marcan los centros de los taladros. Imprima en una impresora láser al **100 % («Tamaño real»)**, nunca con «Ajustar a la página», y compruebe la barra de 50 mm. Las hojas superiores están espejadas, las inferiores no.

---

## Modo por lotes

```
RUN dmxON_FabKit.ulp -batch <carpeta> [-std iso|gost] [-lang en|ru|es|de|pl] [-offline] [-boards N] [-import archivo] [-nogerber] [-nodocs] [-nosch] [-notoner] [-nopdf] [-nobackup] [-keep]
```

| Opción | Significado |
|---|---|
| `-batch <carpeta>` | sin diálogo, en esta carpeta, sin escribir atributos |
| `-lang <código>` | idioma del informe y la documentación (por defecto, el último elegido en el diálogo) |
| `-std iso\|gost` | norma de la documentación (por defecto, la última elegida en el diálogo) |
| `-nosch` | sin esquema eléctrico |
| `-nobackup` | sin copia de seguridad de la carpeta del diseño |
| `-offline` | sin catálogo ni EasyEDA |
| `-boards N` | placas en el pedido |
| `-import <archivo>` | BOM de JLCPCB (xlsx/csv/txt) |
| `-nogerber -nodocs -notoner -nopdf` | omitir parte del paquete |
| `-keep` | conservar la carpeta temporal para depurar |

---

## Solución de problemas

| Síntoma | Qué hacer |
|---|---|
| No aparece la pestaña **dmxON** tras instalar | reinicie Fusion una vez o inicie el complemento: **Utilities → Add-Ins → Scripts and Add-Ins → dmxON → Run** |
| En otro ordenador no se encuentran los ULP ni las reglas; las rutas apuntan al primer ordenador | Fusion comparte sus preferencias en toda la cuenta de Autodesk. Actualice a FabKit 2.2.1 / JLC Rules 1.3.0 (complemento 1.1.0) y ejecute `INSTALL.ulp` una vez en ese ordenador: las carpetas se guardan como `$HOME\dmxON\…` y funcionan en cualquier ordenador |
| Ventana **CAM Export File List** | pulse **OK**: Fusion pide confirmar la exportación de Gerber. Con el complemento dmxON y dmxON JLC Rules la ventana no aparece |
| «Copia omitida: el complemento dmxON no está en marcha» | instale con `INSTALL.ulp` y reinicie Fusion |
| «Your PCB design has changed. CAM output is generated using the last saved version» | pulse **Cancel**, guarde la placa (Ctrl+S) y vuelva a ejecutar FabKit — si no, el Gerber sale de la versión guardada antigua (por ejemplo, sin las nuevas reglas) |
| «El catálogo de JLCPCB no respondió» | compruebe internet y el proxy; el paquete se crea igualmente sin conexión |
| No hay PDF | Microsoft Edge (o Chrome) debe estar instalado en su carpeta por defecto |
| «Requieren atención» | lea cada línea: tensiones, polaridad, pinout, stock |

---

## Cómo funciona

La fase 1 (ULP) analiza la placa y escribe BOM/CPL y borradores, la fase 2 (comandos de Fusion) ejecuta `MANUFACTURING EXPORT` y la fase 3 (el mismo ULP con `-finish`) genera Gerber, vistas previas, informe, documentación y hojas de tóner. Los textos en español, alemán y polaco están en `lib/fk_lang.ulp`, que se genera a partir de `lang/strings.tsv`. Detalles: [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) · cambios: [CHANGELOG.md](CHANGELOG.md). El **complemento dmxON** (`fusion-addin/dmxON`, Python) hace lo que un ULP no puede: las preferencias de carpetas de Fusion, la pestaña dmxON, Gerber sin ventanas mediante `Electron.mfgexport`, copias de seguridad desde la nube y actualizaciones; los ULP le dejan peticiones en `Documentos\dmxON\.inbox`.

---

## Apoye el proyecto

dmxON FabKit es **gratuito**. Detrás hay semanas de trabajo: un analizador de Gerber y Excellon, selección de piezas con el catálogo de JLCPCB, verificación de huellas, documentación en cinco idiomas y pedidos reales comprobados. Si le ahorró una tarde preparando un pedido de JLCPCB, una pieza equivocada o un montaje fallido, apoye el desarrollo: nuevas versiones, cambios del catálogo de JLCPCB y correcciones para nuevas versiones de Fusion.

<p align="center">
  <a href="https://www.paypal.com/donate/?business=smith.show2025%40gmail.com&no_recurring=0&item_name=dmxON+FabKit&currency_code=EUR"><img src="docs/assets/donate.es.svg" alt="Apoye dmxON FabKit con PayPal" width="760"></a>
</p>

<p align="center">
  <b>PayPal:</b> <a href="https://www.paypal.com/donate/?business=smith.show2025%40gmail.com&no_recurring=0&item_name=dmxON+FabKit&currency_code=EUR">smith.show2025@gmail.com</a> — cualquier cantidad ayuda. ¡Gracias! ⭐ Una estrella en GitHub también ayuda a que otros encuentren el proyecto.
</p>

---

## Licencia

Uso gratuito citando al autor; no se permite copiar el código, modificarlo ni usarlo comercialmente — vea [LICENSE.md](LICENSE.md). JLCPCB y LCSC son marcas de sus propietarios; este proyecto no está vinculado a ellos.

**dmxON by AlexSmith 2026** · [dmxon512.com](https://dmxon512.com) · proyecto hermano: [dmxON JLC Rules](https://github.com/AlexSmith2025/dmxON-JLC-Rules-Fusion-Electronics)
