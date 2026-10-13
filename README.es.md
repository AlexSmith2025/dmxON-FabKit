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

---

## Compatibilidad

| | dmxON FabKit |
|---|---|
| **Autodesk Fusion (Electronics), Windows 10/11** | ✅ probado en Fusion **2705.1.11** (octubre de 2026) |
| Autodesk Fusion en macOS | ❌ usa herramientas de Windows (`curl.exe`, `tar.exe`, `robocopy`, Windows Script Host, Microsoft Edge) |
| EAGLE 9.x | ❌ necesita el comando `MANUFACTURING EXPORT` de Fusion para el Gerber |
| KiCad, Altium, EasyEDA | ❌ |

También hace falta: **Microsoft Edge** (incluido en Windows) para los PDF; internet para el catálogo de JLCPCB y las huellas de EasyEDA (todo lo demás funciona sin conexión). Si una nueva versión de Fusion rompe algo, [abra un issue](https://github.com/AlexSmith2025/dmxON-FabKit-Fusion-Electronics/issues).

---

## Instalación

1. [**Descargue `dmxON-FabKit.zip`**](https://github.com/AlexSmith2025/dmxON-FabKit-Fusion-Electronics/releases/latest/download/dmxON-FabKit.zip) y descomprímalo donde quiera.
2. En Fusion Electronics: **Automation → Run ULP → `INSTALL.ulp`** desde la carpeta descomprimida, elija el idioma y pulse **Instalar**.
3. **Reinicie Fusion.** `dmxON_FabKit` aparece en la lista **Run ULP** junto a los ULP integrados — su carpeta `Documentos\dmxON\dmxON-FabKit` va primero y los ULP integrados de Fusion se mantienen.

El instalador copia el proyecto en `Documentos\dmxON\dmxON-FabKit` y añade esa carpeta a las carpetas de ULP mediante los ajustes propios de Fusion. Ejecutar `INSTALL.ulp` de nuevo actualiza los archivos; **Quitar** devuelve a Fusion sus carpetas anteriores. Alternativa manual: mantenga la carpeta descomprimida completa (`dmxON_FabKit.ulp` carga `lib\` y `config\` de su lado) y ejecútelo con `RUN 'C:/ruta/dmxON_FabKit.ulp'`.

---

## Inicio rápido

1. Abra la **placa** en Fusion Electronics y **guárdela** (Ctrl+S) — Fusion exporta el Gerber desde la última versión guardada.
2. **Automation → Run ULP → `dmxON_FabKit`**.
3. Elija el **idioma** en la esquina superior derecha del diálogo (inglés por defecto), la carpeta y pulse **Crear paquete**.
4. Fusion puede mostrar la ventana **CAM Export File List** — pulse **OK** (es la exportación normal de Gerber).
5. Al cabo de un minuto se abre la carpeta del paquete. Empiece por `index.html`.

Consejo: ejecute antes [**dmxON JLC Rules**](https://github.com/AlexSmith2025/dmxON-JLC-Rules-Fusion-Electronics) — configura las reglas de diseño de JLCPCB y la pila de capas, y pasa a FabKit el grosor de la placa y el color de la máscara. Ambas herramientas comparten el ajuste de idioma.

### El diálogo

| Pestaña | Qué ajusta |
|---|---|
| **Idioma** (arriba a la derecha) | English, Русский, Español, Deutsch, Polski — el diálogo cambia al instante; el informe y la documentación se escriben en el mismo idioma |
| **Salida** | carpeta; qué crear: Gerber, documentación A4, PDF, hojas de tóner; qué va al BOM/CPL: THT, centro de pads, designadores omitidos |
| **Piezas** | búsqueda en el catálogo, Basic/Preferred, sustitutos, verificación de huellas, revisión de atributos, escritura de `LCSC_PART`, número de placas, tensión mínima de condensadores, tarifa de alimentador, importación de BOM |
| **Placa** | grosor, color de máscara y serigrafía, acabado — para el informe, el formulario de pedido y la vista |
| **Cajetín** | producto, n.º de documento, revisión, cliente, nota (por placa); empresa y firmas (comunes) |
| **Acerca de** | versión, autor, licencia, enlaces |

Todos los ajustes se recuerdan.

---

## Resultado

```
<placa>_FabKit/
├── index.html                          página de inicio
├── 01_JLCPCB_ORDER/
│   ├── JLCPCB_GERBER/
│   │   ├── <placa>_Gerber_JLCPCB.zip   ← subir a jlcpcb.com
│   │   └── unpacked/                   los mismos archivos para revisar
│   ├── <placa>_JLCPCB_BOM.csv          ← PCB Assembly: BOM
│   └── <placa>_JLCPCB_CPL.csv          ← PCB Assembly: CPL
├── 02_REPORT/                          informe + vistas previas de capas
├── 03_ASSEMBLY_DOCS/                   documentación A4 (HTML + PDF)
└── 04_TONER_TRANSFER_1to1/             HOW_TO_PRINT + 7 hojas PDF
```

Cada ejecución **borra y vuelve a crear** el paquete de la placa — pero solo si la carpeta la creó FabKit (contiene la marca `.dmxon-fabkit`). Una carpeta ajena con el mismo nombre nunca se toca.

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
RUN dmxON_FabKit.ulp -batch <carpeta> [-lang en|ru|es|de|pl] [-offline] [-boards N] [-import archivo] [-nogerber] [-nodocs] [-notoner] [-nopdf] [-keep]
```

| Opción | Significado |
|---|---|
| `-batch <carpeta>` | sin diálogo, en esta carpeta, sin escribir atributos |
| `-lang <código>` | idioma del informe y la documentación (por defecto, el último elegido en el diálogo) |
| `-offline` | sin catálogo ni EasyEDA |
| `-boards N` | placas en el pedido |
| `-import <archivo>` | BOM de JLCPCB (xlsx/csv/txt) |
| `-nogerber -nodocs -notoner -nopdf` | omitir parte del paquete |
| `-keep` | conservar la carpeta temporal para depurar |

---

## Solución de problemas

| Síntoma | Qué hacer |
|---|---|
| `dmxON_FabKit` no aparece en la lista Run ULP tras instalar | reinicie Fusion — lee su lista de carpetas al arrancar |
| Ventana **CAM Export File List** | pulse **OK**: Fusion pide confirmar la exportación de Gerber |
| «Your PCB design has changed. CAM output is generated using the last saved version» | pulse **Cancel**, guarde la placa (Ctrl+S) y vuelva a ejecutar FabKit — si no, el Gerber sale de la versión guardada antigua (por ejemplo, sin las nuevas reglas) |
| «El catálogo de JLCPCB no respondió» | compruebe internet y el proxy; el paquete se crea igualmente sin conexión |
| No hay PDF | Microsoft Edge (o Chrome) debe estar instalado en su carpeta por defecto |
| «Requieren atención» | lea cada línea: tensiones, polaridad, pinout, stock |

---

## Cómo funciona

La fase 1 (ULP) analiza la placa y escribe BOM/CPL y borradores, la fase 2 (comandos de Fusion) ejecuta `MANUFACTURING EXPORT` y la fase 3 (el mismo ULP con `-finish`) genera Gerber, vistas previas, informe, documentación y hojas de tóner. Los textos en español, alemán y polaco están en `lib/fk_lang.ulp`, que se genera a partir de `lang/strings.tsv`. Detalles: [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) · cambios: [CHANGELOG.md](CHANGELOG.md).

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
