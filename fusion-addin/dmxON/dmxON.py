"""dmxON for Fusion Electronics.

The dmxON tab in the PCB and schematic editors (FabKit, JLC Rules, backup, updates),
registration of the dmxON folders in Fusion's ULP / design rules / CAM lists,
update check against GitHub releases and a full local backup of the design folder.

dmxON by AlexSmith 2026 · see LICENSE.md
"""
import datetime
import glob
import json
import os
import re
import shutil
import sys
import tempfile
import threading
import time
import traceback
import urllib.request
import webbrowser
import zipfile

import adsk.core
import adsk.fusion

try:
    import adsk.electron
    HAS_ELECTRON = True
except ImportError:
    HAS_ELECTRON = False
try:
    import adsk.drawing
except ImportError:
    pass

ADDIN_VERSION = '1.4.0'
APP = adsk.core.Application.get()
UI = APP.userInterface
HERE = os.path.dirname(os.path.abspath(__file__))
RES = os.path.join(HERE, 'resources')


def documents_dir():
    """The Documents folder as Fusion's $HOME sees it (it may be moved, e.g. to OneDrive)."""
    try:
        import ctypes
        buf = ctypes.create_unicode_buffer(1024)
        if ctypes.windll.shell32.SHGetFolderPathW(None, 5, None, 0, buf) == 0 and buf.value:   # CSIDL_PERSONAL
            return buf.value
    except Exception:
        pass
    return os.path.join(os.path.expanduser('~'), 'Documents')


BASE = os.path.join(documents_dir(), 'dmxON')
INBOX = os.path.join(BASE, '.inbox')          # requests from the dmxON ULPs (register, backup)
ALIVE = os.path.join(BASE, '.dmxon-addin')    # heartbeat: the ULPs see that the add-in is running
SETTINGS_FILE = os.path.join(BASE, 'dmxON-addin.json')
EVT = 'dmxON_event'
GITHUB = 'https://github.com/'

TOOLS = [
    {'id': 'fabkit', 'name': 'dmxON FabKit', 'dir': 'dmxON-FabKit', 'ulp': 'dmxON_FabKit.ulp',
     'repo': 'AlexSmith2025/dmxON-FabKit-Fusion-Electronics', 'asset': 'dmxON-FabKit.zip', 'rules': ''},
    {'id': 'jlc', 'name': 'dmxON JLC Rules', 'dir': 'dmxON-JLC-Rules', 'ulp': 'dmxON_JLC_Setup.ulp',
     'repo': 'AlexSmith2025/dmxON-JLC-Rules-Fusion-Electronics', 'asset': 'dmxON-JLC-Rules.zip', 'rules': 'rules'},
]
TOOL = {t['id']: t for t in TOOLS}

# option ids of Preferences → General → Electronics → Directory
OPTS = {'ulp': 'ElectronUlpDirectory', 'dru': 'ElectronDesignRulesDirectory', 'cam': 'ElectronCamDirectory'}
WORKSPACES = ('BoardLayoutEnvironement', 'SchEditorEnvironement')
TAB_ID = 'dmxONTab'
COMMANDS = (  # command id, action, icon folder
    ('dmxON_FabKit', 'fabkit', 'fabkit'),
    ('dmxON_JLC', 'jlc', 'jlc'),
    ('dmxON_Backup', 'backup', 'backup'),
    ('dmxON_Update', 'update', 'update'),
    ('dmxON_Settings', 'settings', 'settings'),
    ('dmxON_Help', 'help', 'help'),
)

LANGS = ('en', 'ru', 'es', 'de', 'pl')
LANG_NAMES = ('English', 'Русский', 'Español', 'Deutsch', 'Polski')

TEXT = {
    'en': {
        'cmd_fabkit': 'FabKit', 'tip_fabkit': 'dmxON FabKit — complete manufacturing package for JLCPCB: Gerber, drill, BOM/CPL, ISO / GOST documentation and PDF.',
        'cmd_jlc': 'JLC Rules', 'tip_jlc': 'dmxON JLC Rules — JLCPCB design rules and stack-ups for 2/4/6/8 layers.',
        'cmd_backup': 'Backup', 'tip_backup': 'Back up the whole cloud folder of this design to this computer: EAGLE .sch/.brd/.lbr, Fusion .f3d archives, drawings as PDF and all other files. Restorable on any account or computer.',
        'cmd_update': 'Updates', 'tip_update': 'Check GitHub for new versions of the dmxON tools and install them.',
        'cmd_settings': 'Settings', 'tip_settings': 'dmxON settings: language, backups, automatic update check.',
        'cmd_help': 'Help', 'tip_help': 'Open the dmxON documentation on GitHub.',
        'open_board': 'Open a PCB (board) design first.',
        'not_installed': '{0} is not installed.\n\nDownload and install the latest version from GitHub now?',
        'net_error': 'No connection to GitHub:\n{0}',
        'up_none': 'All dmxON tools are up to date.\n\n{0}',
        'up_list': 'Available on GitHub:\n\n{0}\n\nInstall now?',
        'up_missing': 'not installed',
        'up_found': 'New dmxON versions are available:\n\n{0}\n\nInstall now? (Updates → later; Settings → turn off the check)',
        'up_done': 'Installed:\n\n{0}',
        'up_restart': 'The dmxON add-in was updated to {0}. Restart Fusion to finish.',
        'up_progress': 'Installing {0} {1}…',
        'bk_title': 'dmxON backup',
        'bk_nodoc': 'Save the design to the cloud first — the backup copies its cloud folder.',
        'bk_scan': 'Reading the folder…',
        'bk_item': '{0} ({1} of {2})',
        'bk_done': 'Backup saved:\n{0}\n\nFiles: {1} of {2}.{3}\n\nOpen the folder?',
        'bk_errors': '\nNot copied: {0}',
        'bk_cancel': 'Backup cancelled.',
        'panel_service': 'SERVICE',
        'set_title': 'dmxON settings',
        'set_lang': 'Language',
        'set_update': 'Check for updates daily',
        'set_root': 'Backup folder',
        'set_browse': 'Browse…',
        'set_keep': 'Keep backups per folder',
        'set_info': 'Installed',
        'cancel': 'Cancel',
        'restore': (
            'dmxON backup — how to restore\n'
            '=============================\n\n'
            'The archive holds the latest versions of every file in the Fusion cloud folder.\n\n'
            '* .sch / .brd / .lbr — EAGLE 9 electronics files (schematic, board, library).\n'
            '  Fusion: File → Open → Open from my computer, select the .sch (its .brd is taken with it),\n'
            '  or Data panel → Upload. The schematic and the board open as one Electronics design.\n'
            '* .f3d — Fusion archives of 3D designs (with all components). Upload them the same way.\n'
            '* .pdf — drawings exported as PDF; the other files are copied unchanged.\n'
            '* _dmxON_* — the dmxON package made at the time of the backup (Gerber, BOM/CPL, documents).\n\n'
            'manifest.json lists every file with its cloud version and id.\n'),
    },
    'ru': {
        'cmd_fabkit': 'FabKit', 'tip_fabkit': 'dmxON FabKit — полный пакет для изготовления на JLCPCB: Gerber, сверловка, BOM/CPL, документация по ISO / ГОСТ и PDF.',
        'cmd_jlc': 'JLC Rules', 'tip_jlc': 'dmxON JLC Rules — правила проектирования и стеки слоёв JLCPCB для 2/4/6/8 слоёв.',
        'cmd_backup': 'Бэкап', 'tip_backup': 'Сохранить на этот компьютер всю облачную папку проекта: EAGLE .sch/.brd/.lbr, архивы Fusion .f3d, чертежи в PDF и все остальные файлы. Восстанавливается на любом аккаунте и компьютере.',
        'cmd_update': 'Обновления', 'tip_update': 'Проверить на GitHub новые версии инструментов dmxON и установить их.',
        'cmd_settings': 'Настройки', 'tip_settings': 'Настройки dmxON: язык, бэкапы, автоматическая проверка обновлений.',
        'cmd_help': 'Справка', 'tip_help': 'Открыть описание dmxON на GitHub.',
        'open_board': 'Сначала откройте плату (PCB).',
        'not_installed': '{0} не установлен.\n\nСкачать с GitHub и установить последнюю версию сейчас?',
        'net_error': 'Нет связи с GitHub:\n{0}',
        'up_none': 'Все инструменты dmxON — последних версий.\n\n{0}',
        'up_list': 'На GitHub есть:\n\n{0}\n\nУстановить сейчас?',
        'up_missing': 'не установлен',
        'up_found': 'Вышли новые версии dmxON:\n\n{0}\n\nУстановить сейчас? (Обновления — позже; Настройки — отключить проверку)',
        'up_done': 'Установлено:\n\n{0}',
        'up_restart': 'Надстройка dmxON обновлена до {0}. Перезапустите Fusion, чтобы закончить.',
        'up_progress': 'Установка {0} {1}…',
        'bk_title': 'Бэкап dmxON',
        'bk_nodoc': 'Сначала сохраните проект в облако — бэкап копирует его облачную папку.',
        'bk_scan': 'Чтение папки…',
        'bk_item': '{0} ({1} из {2})',
        'bk_done': 'Бэкап сохранён:\n{0}\n\nФайлов: {1} из {2}.{3}\n\nОткрыть папку?',
        'bk_errors': '\nНе скопированы: {0}',
        'bk_cancel': 'Бэкап отменён.',
        'panel_service': 'СЕРВИС',
        'set_title': 'Настройки dmxON',
        'set_lang': 'Язык',
        'set_update': 'Проверять обновления раз в день',
        'set_root': 'Папка бэкапов',
        'set_browse': 'Обзор…',
        'set_keep': 'Хранить бэкапов на папку',
        'set_info': 'Установлено',
        'cancel': 'Отмена',
        'restore': (
            'Бэкап dmxON — как восстановить\n'
            '==============================\n\n'
            'В архиве — последние версии всех файлов облачной папки Fusion.\n\n'
            '* .sch / .brd / .lbr — файлы электроники в формате EAGLE 9 (схема, плата, библиотека).\n'
            '  Fusion: File → Open → Open from my computer, выберите .sch (его .brd подхватится),\n'
            '  или Data panel → Upload. Схема и плата откроются как один проект Electronics design.\n'
            '* .f3d — архивы 3D-моделей Fusion со всеми компонентами. Загружаются так же.\n'
            '* .pdf — чертежи, выгруженные в PDF; остальные файлы скопированы без изменений.\n'
            '* _dmxON_* — пакет dmxON, собранный в момент бэкапа (Gerber, BOM/CPL, документы).\n\n'
            'В manifest.json — список файлов с версией и id в облаке.\n'),
    },
    'es': {
        'cmd_fabkit': 'FabKit', 'tip_fabkit': 'dmxON FabKit — paquete completo de fabricación para JLCPCB: Gerber, taladros, BOM/CPL, documentación ISO / GOST y PDF.',
        'cmd_jlc': 'JLC Rules', 'tip_jlc': 'dmxON JLC Rules — reglas de diseño y apilados de JLCPCB para 2/4/6/8 capas.',
        'cmd_backup': 'Copia', 'tip_backup': 'Copiar a este ordenador toda la carpeta en la nube del diseño: EAGLE .sch/.brd/.lbr, archivos Fusion .f3d, planos en PDF y el resto de archivos. Se restaura en cualquier cuenta u ordenador.',
        'cmd_update': 'Actualizar', 'tip_update': 'Buscar en GitHub nuevas versiones de las herramientas dmxON e instalarlas.',
        'cmd_settings': 'Ajustes', 'tip_settings': 'Ajustes de dmxON: idioma, copias de seguridad, búsqueda automática de actualizaciones.',
        'cmd_help': 'Ayuda', 'tip_help': 'Abrir la documentación de dmxON en GitHub.',
        'open_board': 'Abra primero un diseño de PCB (placa).',
        'not_installed': '{0} no está instalado.\n\n¿Descargar e instalar ahora la última versión desde GitHub?',
        'net_error': 'Sin conexión con GitHub:\n{0}',
        'up_none': 'Todas las herramientas dmxON están actualizadas.\n\n{0}',
        'up_list': 'Disponible en GitHub:\n\n{0}\n\n¿Instalar ahora?',
        'up_missing': 'no instalado',
        'up_found': 'Hay nuevas versiones de dmxON:\n\n{0}\n\n¿Instalar ahora? (Actualizar → más tarde; Ajustes → desactivar la búsqueda)',
        'up_done': 'Instalado:\n\n{0}',
        'up_restart': 'El complemento dmxON se actualizó a {0}. Reinicie Fusion para terminar.',
        'up_progress': 'Instalando {0} {1}…',
        'bk_title': 'Copia de seguridad dmxON',
        'bk_nodoc': 'Guarde primero el diseño en la nube: la copia guarda su carpeta en la nube.',
        'bk_scan': 'Leyendo la carpeta…',
        'bk_item': '{0} ({1} de {2})',
        'bk_done': 'Copia guardada:\n{0}\n\nArchivos: {1} de {2}.{3}\n\n¿Abrir la carpeta?',
        'bk_errors': '\nNo copiados: {0}',
        'bk_cancel': 'Copia cancelada.',
        'panel_service': 'SERVICIO',
        'set_title': 'Ajustes de dmxON',
        'set_lang': 'Idioma',
        'set_update': 'Buscar actualizaciones a diario',
        'set_root': 'Carpeta de copias',
        'set_browse': 'Examinar…',
        'set_keep': 'Copias a conservar por carpeta',
        'set_info': 'Instalado',
        'cancel': 'Cancelar',
        'restore': (
            'Copia de seguridad dmxON — cómo restaurar\n'
            '=========================================\n\n'
            'El archivo contiene las últimas versiones de todos los archivos de la carpeta de Fusion.\n\n'
            '* .sch / .brd / .lbr — archivos de electrónica EAGLE 9 (esquema, placa, biblioteca).\n'
            '  Fusion: File → Open → Open from my computer, elija el .sch (su .brd se toma con él),\n'
            '  o Data panel → Upload. Esquema y placa se abren como un único Electronics design.\n'
            '* .f3d — archivos Fusion de los diseños 3D con todos sus componentes. Se suben igual.\n'
            '* .pdf — planos exportados a PDF; el resto de archivos se copia sin cambios.\n'
            '* _dmxON_* — el paquete dmxON generado en el momento de la copia (Gerber, BOM/CPL, documentos).\n\n'
            'manifest.json enumera cada archivo con su versión e id en la nube.\n'),
    },
    'de': {
        'cmd_fabkit': 'FabKit', 'tip_fabkit': 'dmxON FabKit — vollständiges Fertigungspaket für JLCPCB: Gerber, Bohrdaten, BOM/CPL, Dokumentation nach ISO / GOST und PDF.',
        'cmd_jlc': 'JLC Rules', 'tip_jlc': 'dmxON JLC Rules — JLCPCB-Designregeln und Lagenaufbauten für 2/4/6/8 Lagen.',
        'cmd_backup': 'Sicherung', 'tip_backup': 'Den gesamten Cloud-Ordner des Designs auf diesen Rechner sichern: EAGLE .sch/.brd/.lbr, Fusion-.f3d-Archive, Zeichnungen als PDF und alle übrigen Dateien. Auf jedem Konto und Rechner wiederherstellbar.',
        'cmd_update': 'Updates', 'tip_update': 'Auf GitHub nach neuen Versionen der dmxON-Werkzeuge suchen und sie installieren.',
        'cmd_settings': 'Einstellungen', 'tip_settings': 'dmxON-Einstellungen: Sprache, Sicherungen, automatische Update-Prüfung.',
        'cmd_help': 'Hilfe', 'tip_help': 'Die dmxON-Dokumentation auf GitHub öffnen.',
        'open_board': 'Öffnen Sie zuerst ein PCB-Design (Platine).',
        'not_installed': '{0} ist nicht installiert.\n\nJetzt die neueste Version von GitHub herunterladen und installieren?',
        'net_error': 'Keine Verbindung zu GitHub:\n{0}',
        'up_none': 'Alle dmxON-Werkzeuge sind aktuell.\n\n{0}',
        'up_list': 'Auf GitHub verfügbar:\n\n{0}\n\nJetzt installieren?',
        'up_missing': 'nicht installiert',
        'up_found': 'Neue dmxON-Versionen sind verfügbar:\n\n{0}\n\nJetzt installieren? (Updates → später; Einstellungen → Prüfung abschalten)',
        'up_done': 'Installiert:\n\n{0}',
        'up_restart': 'Das dmxON-Add-in wurde auf {0} aktualisiert. Fusion zum Abschluss neu starten.',
        'up_progress': '{0} {1} wird installiert…',
        'bk_title': 'dmxON-Sicherung',
        'bk_nodoc': 'Speichern Sie das Design zuerst in der Cloud — die Sicherung kopiert seinen Cloud-Ordner.',
        'bk_scan': 'Ordner wird gelesen…',
        'bk_item': '{0} ({1} von {2})',
        'bk_done': 'Sicherung gespeichert:\n{0}\n\nDateien: {1} von {2}.{3}\n\nOrdner öffnen?',
        'bk_errors': '\nNicht kopiert: {0}',
        'bk_cancel': 'Sicherung abgebrochen.',
        'panel_service': 'SERVICE',
        'set_title': 'dmxON-Einstellungen',
        'set_lang': 'Sprache',
        'set_update': 'Täglich nach Updates suchen',
        'set_root': 'Sicherungsordner',
        'set_browse': 'Durchsuchen…',
        'set_keep': 'Sicherungen je Ordner behalten',
        'set_info': 'Installiert',
        'cancel': 'Abbrechen',
        'restore': (
            'dmxON-Sicherung — Wiederherstellung\n'
            '===================================\n\n'
            'Das Archiv enthält die neuesten Versionen aller Dateien des Fusion-Cloud-Ordners.\n\n'
            '* .sch / .brd / .lbr — Elektronikdateien im EAGLE-9-Format (Schaltplan, Platine, Bibliothek).\n'
            '  Fusion: File → Open → Open from my computer, die .sch wählen (die .brd wird mitgenommen),\n'
            '  oder Data panel → Upload. Schaltplan und Platine öffnen sich als ein Electronics design.\n'
            '* .f3d — Fusion-Archive der 3D-Designs mit allen Komponenten. Ebenso hochladen.\n'
            '* .pdf — als PDF exportierte Zeichnungen; alle übrigen Dateien unverändert kopiert.\n'
            '* _dmxON_* — das zum Zeitpunkt der Sicherung erzeugte dmxON-Paket (Gerber, BOM/CPL, Dokumente).\n\n'
            'manifest.json listet jede Datei mit Cloud-Version und ID.\n'),
    },
    'pl': {
        'cmd_fabkit': 'FabKit', 'tip_fabkit': 'dmxON FabKit — kompletny pakiet produkcyjny dla JLCPCB: Gerber, wiercenia, BOM/CPL, dokumentacja wg ISO / GOST i PDF.',
        'cmd_jlc': 'JLC Rules', 'tip_jlc': 'dmxON JLC Rules — reguły projektowe i stosy warstw JLCPCB dla 2/4/6/8 warstw.',
        'cmd_backup': 'Kopia', 'tip_backup': 'Zapisać na tym komputerze cały folder projektu z chmury: EAGLE .sch/.brd/.lbr, archiwa Fusion .f3d, rysunki w PDF i wszystkie pozostałe pliki. Do odtworzenia na dowolnym koncie i komputerze.',
        'cmd_update': 'Aktualizacje', 'tip_update': 'Sprawdzić na GitHubie nowe wersje narzędzi dmxON i je zainstalować.',
        'cmd_settings': 'Ustawienia', 'tip_settings': 'Ustawienia dmxON: język, kopie zapasowe, automatyczne sprawdzanie aktualizacji.',
        'cmd_help': 'Pomoc', 'tip_help': 'Otworzyć dokumentację dmxON na GitHubie.',
        'open_board': 'Najpierw otwórz projekt PCB (płytkę).',
        'not_installed': '{0} nie jest zainstalowany.\n\nPobrać z GitHuba i zainstalować najnowszą wersję teraz?',
        'net_error': 'Brak połączenia z GitHubem:\n{0}',
        'up_none': 'Wszystkie narzędzia dmxON są aktualne.\n\n{0}',
        'up_list': 'Dostępne na GitHubie:\n\n{0}\n\nZainstalować teraz?',
        'up_missing': 'nie zainstalowano',
        'up_found': 'Są nowe wersje dmxON:\n\n{0}\n\nZainstalować teraz? (Aktualizacje → później; Ustawienia → wyłączyć sprawdzanie)',
        'up_done': 'Zainstalowano:\n\n{0}',
        'up_restart': 'Dodatek dmxON zaktualizowano do {0}. Uruchom ponownie Fusion, aby zakończyć.',
        'up_progress': 'Instalacja {0} {1}…',
        'bk_title': 'Kopia zapasowa dmxON',
        'bk_nodoc': 'Najpierw zapisz projekt w chmurze — kopia zapisuje jego folder w chmurze.',
        'bk_scan': 'Odczyt folderu…',
        'bk_item': '{0} ({1} z {2})',
        'bk_done': 'Kopia zapisana:\n{0}\n\nPliki: {1} z {2}.{3}\n\nOtworzyć folder?',
        'bk_errors': '\nNie skopiowano: {0}',
        'bk_cancel': 'Kopia anulowana.',
        'panel_service': 'SERWIS',
        'set_title': 'Ustawienia dmxON',
        'set_lang': 'Język',
        'set_update': 'Codziennie sprawdzaj aktualizacje',
        'set_root': 'Folder kopii',
        'set_browse': 'Przeglądaj…',
        'set_keep': 'Liczba kopii na folder',
        'set_info': 'Zainstalowano',
        'cancel': 'Anuluj',
        'restore': (
            'Kopia zapasowa dmxON — jak odtworzyć\n'
            '====================================\n\n'
            'Archiwum zawiera najnowsze wersje wszystkich plików folderu Fusion w chmurze.\n\n'
            '* .sch / .brd / .lbr — pliki elektroniki w formacie EAGLE 9 (schemat, płytka, biblioteka).\n'
            '  Fusion: File → Open → Open from my computer, wybierz .sch (jego .brd zostanie dołączony),\n'
            '  albo Data panel → Upload. Schemat i płytka otworzą się jako jeden Electronics design.\n'
            '* .f3d — archiwa Fusion projektów 3D ze wszystkimi komponentami. Wgrywa się je tak samo.\n'
            '* .pdf — rysunki wyeksportowane do PDF; pozostałe pliki skopiowano bez zmian.\n'
            '* _dmxON_* — pakiet dmxON utworzony w chwili kopii (Gerber, BOM/CPL, dokumenty).\n\n'
            'manifest.json zawiera listę plików z wersją i id w chmurze.\n'),
    },
}

HANDLERS = []
STOP = threading.Event()
LOCK = threading.Lock()
STATE = {'lang': 'en', 'settings': {}, 'worker': None}


# ---------------------------------------------------------------- settings and language
def tr(key, *a):
    s = TEXT.get(STATE['lang'], TEXT['en']).get(key) or TEXT['en'].get(key, key)
    for i, v in enumerate(a):
        s = s.replace('{%d}' % i, str(v))
    return s


def load_settings():
    s = {'auto_update': True, 'last_check': 0, 'lang': '', 'backup_root': '', 'backup_keep': 30}
    try:
        with open(SETTINGS_FILE, encoding='utf-8') as f:
            s.update(json.load(f))
    except (OSError, ValueError):
        pass
    STATE['settings'] = s
    return s


def save_settings():
    with LOCK:
        try:
            os.makedirs(BASE, exist_ok=True)
            with open(SETTINGS_FILE, 'w', encoding='utf-8') as f:
                json.dump(STATE['settings'], f, ensure_ascii=False, indent=1)
        except OSError:
            pass


def ulp_settings():
    """dmxON values saved by the ULPs (cfgset) in Fusion's electronics rc file: language, standard."""
    files = glob.glob(os.path.join(os.environ.get('APPDATA', ''), 'Autodesk', 'Neutron Platform', 'Options', '*', 'electronoptiongroup_eagle.rc'))
    out = {}
    if not files:
        return out
    try:
        with open(max(files, key=os.path.getmtime), encoding='utf-8', errors='replace') as f:
            for line in f:
                m = re.match(r'\s*ULP:(dmxon[\w.]*)\s*=\s*"(.*)"\s*$', line)
                if m:
                    out[m.group(1)] = m.group(2)
    except OSError:
        pass
    return out


def pick_lang():
    lg = STATE['settings'].get('lang') or ulp_settings().get('dmxon.lang', '')
    STATE['lang'] = lg if lg in LANGS else 'en'


# ---------------------------------------------------------------- tools and Fusion folders
def tool_dir(t):
    return os.path.join(BASE, t['dir'])


def is_installed(t):
    return os.path.isfile(os.path.join(tool_dir(t), t['ulp']))


def tool_version(t):
    if not is_installed(t):
        return ''
    try:
        with open(os.path.join(tool_dir(t), 'VERSION'), encoding='utf-8') as f:
            return f.read().strip()
    except OSError:
        return '?'


def vtuple(v):
    return tuple(int(x) for x in re.findall(r'\d+', v or '')[:4]) or (0,)


def opt_get(key):
    r = APP.executeTextCommand('Options.Get ' + key)
    parts = r.split(' has value ', 1)
    return parts[1].strip() if len(parts) == 2 else ''


def norm(p):
    return os.path.normcase(os.path.normpath(p.strip().replace('/', os.sep)))


# Fusion's preferences are shared by every computer of the Autodesk account, so absolute paths of
# one machine (C:\\Users\\name\\…, webdeploy\\production\\<build>) are wrong on the others. The lists keep
# only variables Fusion expands on each machine: $HOME = this user's Documents, $EAGLEDIR = LibEagle of
# the running build. Both dmxON tools are always listed, installed here or not, so that computers do
# not rewrite the shared value back and forth.
DMX_ENTRIES = {
    'ulp': ['$HOME\\dmxON\\dmxON-FabKit', '$HOME\\dmxON\\dmxON-JLC-Rules'],
    'dru': ['$HOME\\dmxON\\dmxON-JLC-Rules\\rules'],
    'cam': ['$HOME\\dmxON\\dmxON-JLC-Rules\\rules'],
}


def is_dmxon(entry):
    u = entry.replace('/', '\\').lower()
    return '\\dmxon\\dmxon-fabkit' in u or '\\dmxon\\dmxon-jlc-rules' in u


def portable(entry):
    """A built-in folder of some Fusion build → $EAGLEDIR\\…; anything else unchanged."""
    e = entry.replace('/', '\\')
    i = e.lower().find('\\applications\\electron\\libeagle\\')
    if i >= 0:
        return '$EAGLEDIR\\' + e[i + len('\\applications\\electron\\libeagle\\'):]
    return entry


def register():
    """dmxON folders first in Fusion's ULP / design rules / CAM lists, as variables; the built-in folders stay."""
    changed = False
    for kind, key in OPTS.items():
        try:
            cur = [e.strip() for e in opt_get(key).split(';') if e.strip()]
        except RuntimeError:
            continue
        rest, seen = [], set(x.lower() for x in DMX_ENTRIES[kind])
        for e in cur:
            if is_dmxon(e):
                continue
            e = portable(e)
            if e.lower() not in seen:
                seen.add(e.lower())
                rest.append(e)
        new = DMX_ENTRIES[kind] + rest
        if new != cur:
            APP.executeTextCommand('Options.Set %s "%s"' % (key, ';'.join(new)))
            changed = True
    if changed:
        APP.executeTextCommand('Options.Save')
        APP.executeTextCommand('Options.Reload')
    return changed


# ---------------------------------------------------------------- GitHub
def http_get(url, dst=None):
    req = urllib.request.Request(url, headers={'User-Agent': 'dmxON-Fusion-addin/' + ADDIN_VERSION,
                                               'Accept': 'application/vnd.github+json'})
    with urllib.request.urlopen(req, timeout=30) as r:
        if dst is None:
            return r.read()
        with open(dst, 'wb') as f:
            shutil.copyfileobj(r, f)
    return None


def gh_latest(t):
    j = json.loads(http_get('https://api.github.com/repos/%s/releases/latest' % t['repo']).decode('utf-8'))
    url = next((a.get('browser_download_url') for a in j.get('assets', []) if a.get('name') == t['asset']), None)
    return {'id': t['id'], 'name': t['name'], 'ver': (j.get('tag_name') or '').lstrip('vV'),
            'url': url or j.get('zipball_url'), 'page': j.get('html_url', ''), 'cur': tool_version(t)}


def check_updates(with_missing):
    out = []
    for t in TOOLS:
        cur = tool_version(t)
        if not cur and not with_missing:
            continue
        info = gh_latest(t)
        if not cur or vtuple(info['ver']) > vtuple(cur):
            out.append(info)
    return out


def describe(infos):
    lines = []
    for i in infos:
        lines.append('• %s  %s → %s' % (i['name'], i['cur'] or tr('up_missing'), i['ver']))
    return '\n'.join(lines)


def install_tool(info):
    """Download the release zip, copy it over Documents\\dmxON\\<tool>; a newer add-in in the zip replaces this one."""
    t = TOOL[info['id']]
    tmp = tempfile.mkdtemp(prefix='dmxon_up_')
    try:
        zp = os.path.join(tmp, 'pkg.zip')
        http_get(info['url'], zp)
        ex = os.path.join(tmp, 'x')
        with zipfile.ZipFile(zp) as z:
            for n in z.namelist():
                p = os.path.normpath(os.path.join(ex, n))
                if not p.startswith(os.path.normpath(ex) + os.sep):
                    raise RuntimeError('bad path in archive: ' + n)
            z.extractall(ex)
        src = None
        for root, _dirs, files in os.walk(ex):
            if t['ulp'] in files:
                src = root
                break
        if not src:
            raise RuntimeError(t['ulp'] + ' not found in ' + info['url'])
        shutil.copytree(src, tool_dir(t), dirs_exist_ok=True,
                        ignore=shutil.ignore_patterns('.git', '.github', 'INSTALL.ulp'))
        return update_addin(os.path.join(src, 'fusion-addin', 'dmxON'))
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def addin_version(folder):
    try:
        with open(os.path.join(folder, 'dmxON.manifest'), encoding='utf-8') as f:
            return json.load(f).get('version', '')
    except (OSError, ValueError):
        return ''


def update_addin(src):
    """Copy a newer add-in over the installed one (takes effect after a Fusion restart)."""
    v = addin_version(src)
    if not v or vtuple(v) <= vtuple(ADDIN_VERSION):
        return ''
    if os.path.basename(os.path.dirname(HERE)).lower() != 'addins':
        return ''
    shutil.copytree(src, HERE, dirs_exist_ok=True)
    return v


def run_updates(infos):
    done, newer = [], ''
    pd = UI.createProgressDialog()
    pd.isCancelButtonShown = False
    pd.show('dmxON', '', 0, len(infos))
    try:
        for k, i in enumerate(infos):
            pd.message = tr('up_progress', i['name'], i['ver'])
            pd.progressValue = k
            adsk.doEvents()
            newer = install_tool(i) or newer
            done.append('• %s %s' % (i['name'], i['ver']))
    finally:
        pd.hide()
    register()
    msg = tr('up_done', '\n'.join(done))
    if newer:
        msg += '\n\n' + tr('up_restart', newer)
    UI.messageBox(msg, 'dmxON')


def do_update(manual, infos=None):
    try:
        if infos is None:
            infos = check_updates(manual)
    except Exception as e:  # network, proxy, rate limit
        if manual:
            UI.messageBox(tr('net_error', e), 'dmxON')
        return
    if not infos:
        if manual:
            UI.messageBox(tr('up_none', '\n'.join('• %s %s' % (t['name'], tool_version(t)) for t in TOOLS if is_installed(t))), 'dmxON')
        return
    text = tr('up_list' if manual else 'up_found', describe(infos))
    if UI.messageBox(text, 'dmxON', adsk.core.MessageBoxButtonTypes.YesNoButtonType) == adsk.core.DialogResults.DialogYes:
        try:
            run_updates(infos)
        except Exception as e:
            UI.messageBox(tr('net_error', e), 'dmxON')


# ---------------------------------------------------------------- running the ULPs
def end_command():
    """After a ULP the electronics editor stays in its select command; end it so Fusion is idle again."""
    try:
        UI.terminateActiveCommand()
    except Exception:
        pass


def run_tool(key):
    t = TOOL[key]
    if not is_installed(t):
        if UI.messageBox(tr('not_installed', t['name']), 'dmxON', adsk.core.MessageBoxButtonTypes.YesNoButtonType) != adsk.core.DialogResults.DialogYes:
            return
        try:
            run_updates([gh_latest(t)])
        except Exception as e:
            UI.messageBox(tr('net_error', e), 'dmxON')
            return
    prod = APP.activeProduct
    ptype = prod.productType if prod else ''
    if ptype == 'SchematicProductType' and HAS_ELECTRON:
        # from the schematic: switch to its board
        try:
            adsk.electron.Schematic.cast(prod).linkedBoard.parentDocument.activate()
            adsk.doEvents()
            prod = APP.activeProduct
            ptype = prod.productType if prod else ''
        except Exception:
            pass
    if ptype != 'BoardProductType':
        UI.messageBox(tr('open_board'), 'dmxON')
        return
    register()
    ulp = os.path.join(tool_dir(t), t['ulp']).replace('\\', '/').replace("'", "''")
    APP.executeTextCommand("Electron.run RUN '%s'" % ulp)
    end_command()


# ---------------------------------------------------------------- backup of the design folder
def safe(name):
    s = re.sub(r'[<>:"/\\|?*\x00-\x1f]', '_', name or '').strip(' .')
    return s or '_'


def folder_chain(folder):
    names = []
    f = folder
    while f is not None:
        if getattr(f, 'isRoot', False) or f.parentFolder is None:
            break
        names.append(f.name)
        f = f.parentFolder
    return list(reversed(names))


def walk(folder, rel=()):
    for df in folder.dataFiles:
        yield df, rel
    for sub in folder.dataFolders:
        yield from walk(sub, rel + (safe(sub.name),))


def open_ids():
    ids = set()
    for d in APP.documents:
        try:
            if d.dataFile:
                ids.add(d.dataFile.id)
        except Exception:
            pass
    return ids


def find_open(df):
    for d in APP.documents:
        try:
            if d.dataFile and d.dataFile.id == df.id:
                return d
        except Exception:
            pass
    return None


class Opened:
    """A cloud file opened for export; whatever was opened on the way is closed again."""

    def __init__(self, df):
        self.df = df
        self.before = open_ids()
        self.doc = find_open(df)

    def __enter__(self):
        if self.doc is None:
            try:
                self.doc = APP.documents.open(self.df, False)
            except Exception:
                self.doc = APP.documents.open(self.df, True)
        return self.doc

    def __exit__(self, *exc):
        for d in list(APP.documents):
            try:
                if d.isValid and d.dataFile and d.dataFile.id not in self.before and not d.isModified:
                    d.close(False)
            except Exception:
                pass
        return False


def eagle_export(prod, kind, path):
    if kind == 'brd':
        em = adsk.electron.Board.cast(prod).exportManager
        opts = em.createEagleBrdExportOptions(path)
    elif kind == 'sch':
        em = adsk.electron.Schematic.cast(prod).exportManager
        opts = em.createEagleSchExportOptions(path)
    else:
        em = adsk.electron.Library.cast(prod).exportManager
        opts = em.createEagleLbrExportOptions(path)
    if not opts or not em.execute(opts):
        raise RuntimeError('EAGLE export failed')


def unique(out, name):
    """name, or name (2), name (3)… when several cloud files share a name."""
    base, ext = os.path.splitext(name)
    k = 2
    while os.path.exists(os.path.join(out, name)):
        name = '%s (%d)%s' % (base, k, ext)
        k += 1
    return name


KIND = {'fsch': 'sch', 'fbrd': 'brd', 'flbr': 'lbr'}


def export_open(df, out):
    """An opened schematic, board or library as an EAGLE file."""
    doc = find_open(df)
    if doc is None:
        raise RuntimeError('not opened')
    kind = KIND[df.fileExtension.lower()]
    name = unique(out, safe(df.name) + '.' + kind)
    eagle_export(doc.products.item(0), kind, os.path.join(out, name))
    return name


def export_design(df, out):
    """Electronics design (.fprj): its schematic and board as EAGLE files; returns {file id: written name}."""
    kids = [c for c in df.childReferences if (c.fileExtension or '').lower() in ('fsch', 'fbrd')] if df.hasChildReferences else []
    done = {}
    with Opened(df):
        for c in kids:
            done[c.id] = export_open(c, out)
    if not done:
        raise RuntimeError('no schematic or board in the design')
    return done


def export_single(df, out):
    """Schematic, board or library outside the designs of this folder."""
    if df.fileExtension.lower() != 'flbr' and df.hasParentReferences:
        # opened through its design: a file linked to several designs would otherwise ask which one to open
        parent = next((p for p in df.parentReferences if (p.fileExtension or '').lower() == 'fprj'), None)
        if parent is not None:
            with Opened(parent):
                return export_open(df, out)
    with Opened(df):
        return export_open(df, out)


def export_file(df, out):
    """Any other cloud file into folder out; returns the written file name."""
    ext = (df.fileExtension or '').lower()
    base = safe(df.name)
    if ext in ('f3d', 'f3z', 'f2d'):
        with Opened(df) as doc:
            if ext == 'f2d':
                drw = adsk.drawing.Drawing.cast(doc.products.itemByProductType('DrawingProductType'))
                name = unique(out, base + '.pdf')
                opts = drw.exportManager.createPDFExportOptions(os.path.join(out, name))
                opts.openPDF = False
                drw.exportManager.execute(opts)
                return name
            des = adsk.fusion.Design.cast(doc.products.itemByProductType('DesignProductType'))
            name = unique(out, base + '.f3d')
            des.exportManager.execute(des.exportManager.createFusionArchiveExportOptions(os.path.join(out, name)))
            return name
    name = unique(out, base + ('.' + ext if ext and not base.lower().endswith('.' + ext) else ''))
    if not df.download(os.path.join(out, name), None):
        raise RuntimeError('download failed')
    return name


def hub_name():
    try:
        return APP.data.activeHub.name
    except Exception:
        return ''


def backup(reason='manual', extra=None, quiet=False, target=None, name=None):
    """Back up the cloud folder of the active design (or of the data file target)."""
    doc = APP.activeDocument
    df = target or (doc.dataFile if doc else None)
    if df is None:
        if not quiet:
            UI.messageBox(tr('bk_nodoc'), tr('bk_title'))
        return ''
    folder, project = df.parentFolder, df.parentProject
    chain = folder_chain(folder)
    stamp = datetime.datetime.now().strftime('%Y-%m-%d_%H%M%S')
    root = STATE['settings'].get('backup_root') or os.path.join(BASE, 'Backups')
    dest = os.path.join(root, safe(project.name), *[safe(c) for c in chain])
    # из FabKit: архив — в производственную папку пакета, рядом с Gerber и документацией
    in_pkg = bool(extra and os.path.isdir(extra))
    if in_pkg:
        dest = os.path.join(extra, '05_BACKUP')
    top = safe(folder.name if chain else project.name)
    work = tempfile.mkdtemp(prefix='dmxon_bk_')
    pd = UI.createProgressDialog()
    pd.cancelButtonText = tr('cancel')
    pd.isCancelButtonShown = True
    pd.show(tr('bk_title'), tr('bk_scan'), 0, 1)
    adsk.doEvents()
    try:
        items = list(walk(folder))
        # designs first: their schematics and boards are then already saved
        items.sort(key=lambda it: 0 if (it[0].fileExtension or '').lower() == 'fprj' else 1)
        pd.maximumValue = max(1, len(items))
        files, errors, covered = [], [], {}
        for k, (f, rel) in enumerate(items):
            if pd.wasCancelled:
                if not quiet:
                    UI.messageBox(tr('bk_cancel'), tr('bk_title'))
                return ''
            pd.message = tr('bk_item', f.name, k + 1, len(items))
            pd.progressValue = k
            adsk.doEvents()
            out = os.path.join(work, top, *rel)
            os.makedirs(out, exist_ok=True)
            ext = (f.fileExtension or '').lower()
            rec = {'name': f.name, 'type': ext, 'version': f.versionNumber, 'id': f.id,
                   'folder': '/'.join(rel), 'file': '', 'status': 'ok'}
            try:
                if f.id in covered:
                    rec['file'] = covered[f.id]
                elif ext == 'fprj':
                    done = export_design(f, out)
                    covered.update(done)
                    rec['file'] = ', '.join(sorted(done.values()))
                elif ext in ('fsch', 'fbrd', 'flbr'):
                    rec['file'] = export_single(f, out)
                else:
                    rec['file'] = export_file(f, out)
            except Exception as e:
                rec['status'] = 'error: %s' % e
                errors.append(f.name + '.' + ext)
            files.append(rec)
        if extra and os.path.isdir(extra) and not in_pkg:
            shutil.copytree(extra, os.path.join(work, top, '_dmxON_' + safe(reason), os.path.basename(extra.rstrip('\\/'))),
                            dirs_exist_ok=True)
        meta = {'dmxON': ADDIN_VERSION, 'created': datetime.datetime.now().isoformat(timespec='seconds'),
                'reason': reason, 'hub': hub_name(),
                'project': project.name, 'folder': '/'.join(chain), 'files': files}
        with open(os.path.join(work, top, 'manifest.json'), 'w', encoding='utf-8') as fh:
            json.dump(meta, fh, ensure_ascii=False, indent=1)
        with open(os.path.join(work, top, 'RESTORE.txt'), 'w', encoding='utf-8') as fh:
            fh.write(tr('restore'))
        os.makedirs(dest, exist_ok=True)
        zname = safe(name) if (in_pkg and name) else top      # из FabKit: <плата>_v<версия>_cloud
        zpath = os.path.join(dest, '%s_%s.zip' % (zname, stamp))
        with zipfile.ZipFile(zpath, 'w', zipfile.ZIP_DEFLATED) as z:
            for r, _d, fs in os.walk(work):
                for n in fs:
                    p = os.path.join(r, n)
                    z.write(p, os.path.relpath(p, work))
        keep = max(1, int(STATE['settings'].get('backup_keep') or 30))
        old = sorted(glob.glob(os.path.join(dest, zname + '_????-??-??_??????.zip')))
        for o in old[:-keep]:
            try:
                os.remove(o)
            except OSError:
                pass
    finally:
        pd.hide()
        shutil.rmtree(work, ignore_errors=True)
        try:
            if doc.isValid and APP.activeDocument != doc:
                doc.activate()
        except Exception:
            pass
    ok = sum(1 for r in files if r['status'] == 'ok')
    if not quiet or errors:
        err = tr('bk_errors', ', '.join(errors)) if errors else ''
        if UI.messageBox(tr('bk_done', zpath, ok, len(files), err), tr('bk_title'),
                         adsk.core.MessageBoxButtonTypes.YesNoButtonType) == adsk.core.DialogResults.DialogYes:
            os.startfile(dest)
    return zpath


# ---------------------------------------------------------------- FabKit: STEP of the board
def export_board_step(path):
    """STEP of the active board with its component models. «3D PCB» opens the design's linked 3D PCB or builds a new,
    unsaved one from the current board; it is exported and, when it was not open before, closed without saving."""
    board_doc = APP.activeDocument
    if not board_doc or board_doc.objectType != 'adsk::electron::BoardDocument':
        return ''
    cd = UI.commandDefinitions.itemById('Switch3dPcbDocCmd')
    if cd is None:
        return ''
    before = [d for d in APP.documents]
    try:
        cd.execute()
        des, last, stable, t0 = None, -1, 0, time.time()
        while time.time() - t0 < 180:                       # the 3D PCB is built asynchronously
            adsk.doEvents()
            ad = APP.activeDocument
            if ad and ad.objectType == 'adsk::fusion::FusionDocument':
                d = adsk.fusion.Design.cast(ad.products.itemByProductType('DesignProductType'))
                n = d.rootComponent.allOccurrences.count if d else 0
                if n > 0 and n == last:
                    stable += 1
                    if stable >= 6:
                        des = d
                        break
                else:
                    stable = 0
                last = n
            time.sleep(0.25)
        if des is None:
            return ''
        pcb_doc = APP.activeDocument
        os.makedirs(os.path.dirname(path), exist_ok=True)
        em = des.exportManager
        ok = em.execute(em.createSTEPExportOptions(path, des.rootComponent))
        if not any(pcb_doc == d for d in before):
            pcb_doc.close(False)
        return path if ok and os.path.exists(path) else ''
    except Exception:
        return ''
    finally:
        try:
            if board_doc.isValid:
                board_doc.activate()
                adsk.doEvents()
        except Exception:
            pass


# ---------------------------------------------------------------- FabKit: Gerber through the CAM job, then phase 3
def fabkit_cam(req):
    """Electron.mfgexport writes <dir>/<CAM job name>/... without the One-Click Export dialog; FabKit gets them as cam.zip."""
    zipp, cam, fin = req.get('zip', ''), req.get('cam', ''), req.get('finish', '')
    tmpd = os.path.dirname(zipp)
    out = os.path.join(tmpd, 'mfg')
    os.makedirs(out, exist_ok=True)
    t0 = time.time() - 2
    try:
        APP.executeTextCommand('Electron.mfgexport "%s" "%s"' % (os.path.join(out, 'cam').replace('\\', '/'), cam.replace('\\', '/')))
        files = []
        for r, _d, fs in os.walk(out):
            files += [os.path.join(r, f) for f in fs if os.path.getmtime(os.path.join(r, f)) >= t0]
        if files:
            with zipfile.ZipFile(zipp, 'w', zipfile.ZIP_DEFLATED) as z:
                for f in files:
                    z.write(f, os.path.relpath(f, out))
    except Exception:
        pass                                   # phase 3 reports the missing cam.zip
    if fin:
        APP.executeTextCommand('Electron.run "%s"' % fin.rstrip(';').replace('"', "'"))
        end_command()


# ---------------------------------------------------------------- JLC Rules: grid of the board's schematic
def schematic_of(board_doc):
    """The schematic document of the board's Electronics design (opened)."""
    try:
        for p in board_doc.dataFile.parentReferences:
            if (p.fileExtension or '').lower() != 'fprj':
                continue
            for c in p.childReferences:
                if (c.fileExtension or '').lower() == 'fsch':
                    d = find_open(c)
                    if d:
                        return d
    except Exception:
        pass
    for d in APP.documents:
        if d.objectType == 'adsk::electron::SchematicDocument' and d.name == board_doc.name:
            return d
    return None


def schematic_grid(cmd):
    """Run a GRID command in the schematic that belongs to the active board, then return to the board."""
    board_doc = APP.activeDocument
    if not board_doc or not cmd.upper().startswith('GRID '):
        return
    sch = schematic_of(board_doc)
    if sch is None:
        return
    sch.activate()
    adsk.doEvents()
    APP.executeTextCommand('Electron.run "%s"' % cmd.replace('"', "'"))
    end_command()
    board_doc.activate()
    adsk.doEvents()


# ---------------------------------------------------------------- requests from the ULPs
def read_json(path):
    raw = open(path, 'rb').read()
    for enc in ('utf-8', 'cp1251', 'latin-1'):
        try:
            return json.loads(raw.decode(enc))
        except (UnicodeDecodeError, ValueError):
            continue
    return {}


def do_inbox():
    for f in sorted(glob.glob(os.path.join(INBOX, '*.json'))):
        try:
            req = read_json(f)
        finally:
            try:
                os.remove(f)
            except OSError:
                pass
        lg = req.get('lang')
        if lg in LANGS and lg != STATE['lang'] and not STATE['settings'].get('lang'):
            STATE['lang'] = lg
            rebuild_ui()
        what = req.get('do')
        if what == 'register':
            register()
        elif what == 'backup':
            # STEP first: it needs the board to be the active document
            out = req.get('out') or ''
            if req.get('step') and out and os.path.isdir(out):
                export_board_step(os.path.join(out, '05_BACKUP', os.path.basename(req.get('step'))))
            backup(req.get('tool', 'ulp'), out, quiet=True, name=req.get('name'))
        elif what == 'fabkit_cam':
            fabkit_cam(req)
        elif what == 'grid':
            schematic_grid(req.get('cmd', ''))


# ---------------------------------------------------------------- UI
def fire(payload):
    APP.fireCustomEvent(EVT, json.dumps(payload))


def dispatch(data):
    what = data.get('do')
    if STATE.get('busy') and what in ('inbox', 'update_found', 'rebuild'):
        return
    STATE['busy'] = what not in ('rebuild',)
    try:
        dispatch_one(what, data)
    finally:
        STATE['busy'] = False


def dispatch_one(what, data):
    if what in ('fabkit', 'jlc'):
        run_tool(what)
    elif what == 'backup':
        backup()
    elif what == 'update':
        do_update(True)
    elif what == 'update_found':
        do_update(False, data.get('infos'))
    elif what == 'help':
        page = GITHUB + TOOL['fabkit']['repo']
        webbrowser.open(page + ('' if STATE['lang'] == 'en' else '/blob/main/README.%s.md' % STATE['lang']))
    elif what == 'inbox':
        do_inbox()
    elif what == 'rebuild':
        rebuild_ui()


class EventHandler(adsk.core.CustomEventHandler):
    def notify(self, args):
        try:
            dispatch(json.loads(args.additionalInfo or '{}'))
        except Exception:
            UI.messageBox('dmxON:\n' + traceback.format_exc())


class ButtonCreated(adsk.core.CommandCreatedEventHandler):
    def __init__(self, action):
        super().__init__()
        self.action = action

    def notify(self, args):
        # no inputs: the command ends at once, the work runs after it from the event queue
        fire({'do': self.action})


class SettingsCreated(adsk.core.CommandCreatedEventHandler):
    def notify(self, args):
        cmd = args.command
        cmd.okButtonText = 'OK'
        inp = cmd.commandInputs
        s = STATE['settings']
        dd = inp.addDropDownCommandInput('lang', tr('set_lang'), adsk.core.DropDownStyles.TextListDropDownStyle)
        for code, name in zip(LANGS, LANG_NAMES):
            dd.listItems.add(name, code == STATE['lang'])
        inp.addBoolValueInput('auto_update', tr('set_update'), True, '', bool(s.get('auto_update', True)))
        inp.addStringValueInput('backup_root', tr('set_root'), s.get('backup_root') or os.path.join(BASE, 'Backups'))
        inp.addBoolValueInput('browse', tr('set_browse'), False, '', False)
        inp.addIntegerSpinnerCommandInput('backup_keep', tr('set_keep'), 1, 999, 1, int(s.get('backup_keep') or 30))
        info = ['dmxON add-in %s' % ADDIN_VERSION] + ['%s %s' % (t['name'], tool_version(t) or '—') for t in TOOLS]
        inp.addTextBoxCommandInput('info', tr('set_info'), '<br>'.join(info), len(info), True)
        for h in (SettingsChanged(), SettingsExecute()):
            (cmd.inputChanged if isinstance(h, SettingsChanged) else cmd.execute).add(h)
            HANDLERS.append(h)


class SettingsChanged(adsk.core.InputChangedEventHandler):
    def notify(self, args):
        if args.input.id != 'browse':
            return
        dlg = UI.createFolderDialog()
        dlg.title = tr('set_root')
        root = args.inputs.itemById('backup_root')
        dlg.initialDirectory = root.value
        if dlg.showDialog() == adsk.core.DialogResults.DialogOK:
            root.value = dlg.folder


class SettingsExecute(adsk.core.CommandEventHandler):
    def notify(self, args):
        inp = args.command.commandInputs
        s = STATE['settings']
        sel = inp.itemById('lang').selectedItem
        lg = LANGS[sel.index] if sel else STATE['lang']
        s['auto_update'] = inp.itemById('auto_update').value
        root = inp.itemById('backup_root').value.strip()
        s['backup_root'] = '' if norm(root) == norm(os.path.join(BASE, 'Backups')) else root
        s['backup_keep'] = inp.itemById('backup_keep').value
        if lg != STATE['lang']:
            s['lang'] = lg
            STATE['lang'] = lg
            fire({'do': 'rebuild'})
        save_settings()


def remove_ui():
    for wsid in WORKSPACES:
        ws = UI.workspaces.itemById(wsid)
        if not ws:
            continue
        tab = ws.toolbarTabs.itemById(TAB_ID)
        if tab:
            for p in list(tab.toolbarPanels):
                if p.id.startswith('dmxON'):
                    p.deleteMe()
            tab.deleteMe()
    for cid, _a, _i in COMMANDS:
        cd = UI.commandDefinitions.itemById(cid)
        if cd:
            cd.deleteMe()


def build_ui():
    for cid, action, icon in COMMANDS:
        cd = UI.commandDefinitions.addButtonDefinition(cid, tr('cmd_' + action), tr('tip_' + action), os.path.join(RES, icon))
        h = SettingsCreated() if action == 'settings' else ButtonCreated(action)
        cd.commandCreated.add(h)
        HANDLERS.append(h)
    for wsid in WORKSPACES:
        ws = UI.workspaces.itemById(wsid)
        if not ws:
            continue
        tab = ws.toolbarTabs.itemById(TAB_ID) or ws.toolbarTabs.add(TAB_ID, 'dmxON')
        groups = (('dmxONTools_' + wsid, 'dmxON', COMMANDS[:3]), ('dmxONService_' + wsid, tr('panel_service'), COMMANDS[3:]))
        for pid, pname, cmds in groups:
            panel = tab.toolbarPanels.itemById(pid) or tab.toolbarPanels.add(pid, pname)
            for cid, _a, _i in cmds:
                ctl = panel.controls.addCommand(UI.commandDefinitions.itemById(cid))
                ctl.isPromoted = True
                ctl.isPromotedByDefault = True


def rebuild_ui():
    remove_ui()
    build_ui()


# ---------------------------------------------------------------- background: inbox, heartbeat, update check
def worker():
    next_update = time.time() + 60
    beat = 0
    while not STOP.wait(2):
        try:
            if time.time() - beat > 30:
                beat = time.time()
                with open(ALIVE, 'w', encoding='utf-8') as f:
                    f.write(ADDIN_VERSION)
            if glob.glob(os.path.join(INBOX, '*.json')):
                fire({'do': 'inbox'})
            s = STATE['settings']
            if s.get('auto_update', True) and time.time() >= next_update:
                next_update = time.time() + 6 * 3600
                if time.time() - float(s.get('last_check') or 0) > 20 * 3600:
                    infos = check_updates(False)
                    s['last_check'] = time.time()
                    save_settings()
                    if infos:
                        fire({'do': 'update_found', 'infos': infos})
        except Exception:
            pass


def run(context):
    try:
        os.makedirs(INBOX, exist_ok=True)
        load_settings()
        pick_lang()
        ev = APP.registerCustomEvent(EVT)
        h = EventHandler()
        ev.add(h)
        HANDLERS.append(h)
        try:
            register()
        except Exception:
            pass
        rebuild_ui()
        STOP.clear()
        th = threading.Thread(target=worker, name='dmxON', daemon=True)
        th.start()
        STATE['worker'] = th
    except Exception:
        UI.messageBox('dmxON:\n' + traceback.format_exc())


def stop(context):
    try:
        STOP.set()
        remove_ui()
        APP.unregisterCustomEvent(EVT)
        HANDLERS.clear()
        try:
            os.remove(ALIVE)
        except OSError:
            pass
    except Exception:
        UI.messageBox('dmxON:\n' + traceback.format_exc())
