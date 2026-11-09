# -*- coding: utf-8 -*-
"""Text for the tools section and the tool pages (/apps/<slug>/), in three languages.

Used by tools/build.py. HTML entities are allowed. Product names, versions and paths stay in Latin script."""
ORDER = ["wintool", "upgrade", "v2", "v1", "office"]
NAME = {"wintool": "WinTool by PcNinja", "upgrade": "Windows Upgrade Tool", "v2": "WinUpdate Tool V2",
        "v1": "WinUpdate Tool V1", "office": "Smart Office Installer"}
SHORT = {"wintool": "WinTool", "upgrade": "Windows Upgrade Tool", "v2": "WinUpdate Tool V2",
         "v1": "WinUpdate Tool V1", "office": "Smart Office Installer"}
VER = {"wintool": "v1.0.2", "upgrade": "v1.3.0", "v2": "v2.2.8", "v1": "v1.1.2", "office": "v3.3.15"}
CMD = {"wintool": ".\\WinTool-by-PcNinja.exe", "upgrade": "Get-Help WinUpgradeTool", "v2": "Get-Help WinUpdateTool",
       "v1": "Get-Help WinUpdateTool -V1", "office": "Get-Help SmartOfficeInstaller"}
STEP = {"wintool": None, "upgrade": 4, "v2": 3, "v1": 2, "office": 1}
MONTH = {"wintool": (11, 2026), "upgrade": (10, 2026), "v2": (7, 2026), "v1": (5, 2025), "office": (10, 2024)}

L = {}

# ---------------------------------------------------------------- English
L["en"] = dict(
    dir="ltr", months=["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"],
    nav=["Tools", "Services", "About", "Contact"],
    h2="Tools I build",
    intro="Windows utilities for technicians and advanced home users. Each one is open on GitHub, with release notes and checksums for every download.",
    feat_p="One app for Windows Update, Windows Upgrade and Office. Run it portable or install it from the same EXE; the MSI is there for silent deployment. English, Hebrew and Spanish.",
    latest="Latest", dl="Download", direct="Direct download", dl_gh="Download from GitHub", src="Source", more_wt="More about WinTool", notes="Release notes",
    unsigned="Files are not code-signed; Windows SmartScreen may warn. Check them against SHA256SUMS.txt.",
    caps=[("Windows Update", "Scan, choose what to install, schedule, restart handling. Grew out of WinUpdate Tool."),
          ("Windows Upgrade", "In-place upgrade with checks before it starts. Grew out of Windows Upgrade Tool."),
          ("Office", "Install, offline package, remove. Grew out of Smart Office Installer.")],
    how_h="How it got here",
    how_p="I&#8217;ve been building Windows since the happy days of XP. Every tool here comes from one idea: keep the hardware people already have, and save them every cost I can. Newest first; each step has its own page.",
    today="Today", step="Step", story="The story", in_wt="In WinTool", retired="Retired",
    tools="Tools", fits="Where it fits in the story",
    why_h="Why I built it", does_h="What it does", grew_h="How it grew", carried_h="What carried into WinTool",
    move_h="Moving to WinTool?", go_wt="Go to WinTool", newer="Newer", older="Older",
    placeholder="[Your story: what problem started it]",
    came_h="Coming from an older tool?",
    T={
     "wintool": dict(
        short="All of the steps below in one app. Concept on 30 Oct 2026, first official version on 7 Nov.",
        became="Windows Update + Windows Upgrade + Office, one EXE",
        lede="One app for Windows Update, Windows Upgrade and Office.",
        why=["Each of my tools had its own window, its own logs, its own updater and its own installer. One app writes all of that once, and a PC gets one tool instead of three."],
        does=["One EXE: run it portable or install it, even offline. The MSI is there for silent deployment.",
              "Windows Update: scan, choose which updates to install, scheduled runs, restart handling.",
              "Windows Upgrade: in-place upgrade from an ISO or Microsoft&#8217;s media, with checks before it starts.",
              "Office: Microsoft 365 or Office LTSC 2024, Visio and Project; install, offline package, remove.",
              "Logs, useful links, and a self-update that asks first. English, Hebrew and Spanish; follows Windows dark or light."],
        grew=[("30 Oct 2026", "The idea of one app, written down"), ("7 Nov 2026", "1.0.0, the first official version, and 1.0.1 with reviewed Spanish"), ("8 Nov 2026", "1.0.2")],
        carried=None,
        move="WinTool finds WinUpdate Tool V1 or V2, offers to import the schedule and removes the old tool, so two tools never update the same PC."),
     "upgrade": dict(
        short="In-place upgrade to Windows 10 or 11, built above all for PCs Microsoft no longer supports on paper. From first test to release candidate in two days.",
        became="Became the Windows Upgrade page in WinTool",
        lede="An in-place upgrade to Windows 10 or 11, built above all for the PCs Microsoft no longer supports on paper.",
        why=["This tool runs fine on current hardware, but it was built for the computers Microsoft no longer supports on paper.",
             "I&#8217;ve been working with Windows since the happy days of XP, and I finished my Microsoft systems engineer studies shortly after Server 2003 came out. Over the years I kept sharpening one craft: building custom Windows images. And honestly, what Windows really needs from a PC hasn&#8217;t changed much since Vista.",
             "Alongside that, I&#8217;ve always been the technician of whatever community I lived in. My rule is simple: when life is good to you, that&#8217;s the time to give back. So I try, sincerely, to keep the hardware people already have and to save them every cost I can, above all for those who can least afford a new computer."],
        does=["Guides an in-place upgrade to Windows 10 or 11 on x64 PCs, including older hardware, from an ISO or Microsoft&#8217;s media.",
              "Shows the current Windows version, storage and source choices on one screen. Portable, with a GUI and a command line.",
              "The Windows 11 path for unsupported hardware is experimental. Back up your files first."],
        grew=[("10 Oct 2026", "First private test"), ("11 Oct 2026", "First release candidate"), ("5 Nov 2026", "1.3.0")],
        carried=["The same upgrade engine, ported to .NET Framework 4.8", "Every check before Setup starts: media, edition, language, storage", "Command-line upgrade with WinTool&#8217;s exit codes"],
        move="The Windows Upgrade page in WinTool does the same job, next to updates and Office."),
     "v2": dict(
        short="A new interface where you choose which updates to install, plus an update channel, scheduling, driver audit and a reset for a stuck update service. MSI or portable EXE.",
        became="Became the Windows Update and Schedule pages in WinTool",
        lede="A standalone updater that runs separately from Windows&#8217; built-in Windows Update.",
        why=None,
        does=["Lets you choose which updates to install, a choice Windows Update itself took away in recent years. Leave one out for a while, for example to test after a problem; Windows will offer it again later.",
              "Checks, installs and schedules updates, audits drivers and can reset a stuck update service.",
              "Use it when a PC won&#8217;t update on its own, or to speed up a technician&#8217;s work.",
              "MSI for deployment or a portable EXE. Updates itself after verifying the download."],
        grew=[("Jul 2026", "First release candidate: a new interface and an update channel"), ("Jul to Nov 2026", "Over 30 test and stable releases"), ("5 Nov 2026", "2.2.8, published only after automatic tests pass")],
        carried=["Choosing which updates to install", "Scan, preview and install, rewritten in C#", "Scheduled runs with retry, wake-to-run and run-if-missed", "Restart handling, health check and reset"],
        move="WinTool finds this tool, offers to import its schedule and removes it, so two tools never update the same PC."),
     "v1": dict(
        short="One small EXE for running Windows Update on PCs that would not update on their own. By June 2026 it had an MSI, a portable EXE and a command line.",
        became="Grew into WinUpdate Tool V2",
        lede="Where the Windows Update tools began: a tool for PCs that would not update on their own.",
        why=None,
        does=["A window to check and run Windows Update, schedule runs, read logs and audit drivers.",
              "Command-line modes for status, updates, driver audit, log collection and resetting Windows Update.",
              "MSI with silent deployment, or a portable EXE."],
        grew=[("May 2025", "First build: one small EXE"), ("Jun 2026", "1.1.2: MSI, portable EXE and command line"), ("Jul 2026", "Published on GitHub; V2 takes over")],
        carried=["V1 grew into V2, and WinTool carries the V2 engine", "Scheduled update runs", "Driver audit and silent deployment"],
        move="WinTool finds V1, offers to import its schedule and removes it."),
     "office": dict(
        short="Where it started: a few Office Deployment Tool settings and a one-line script. Then a batch installer, a GUI in March 2026, and three major versions in one week.",
        became="Became the Office page in WinTool",
        lede="Installs or removes Microsoft Office through Microsoft&#8217;s own Office Deployment Tool.",
        why=None,
        does=["Office LTSC 2024 or Microsoft 365 with a choice of update channel, plus optional Visio and Project.",
              "Language selection, removal of an existing Office, and an offline LTSC package.",
              "Updates itself after asking. You need a valid Office license."],
        grew=[("Oct 2024", "Office Deployment Tool settings and a one-line script"), ("Jun 2025", "A batch installer and its first EXE"),
              ("Mar 2026", "A graphical installer, then versions 1.0, 2.0 and 3.0 in one week"), ("Jul 2026", "Published on GitHub at 3.3"), ("Nov 2026", "3.3.15")],
        carried=["The same choices: LTSC 2024, Microsoft 365, Visio, Project, all languages", "The latest Office Deployment Tool, verified before use", "Install, offline package and removal, also from the command line"],
        move="The Office page in WinTool does the same job, next to updates and upgrade."),
    })

# ---------------------------------------------------------------- Spanish
L["es"] = dict(
    dir="ltr", months=["ene","feb","mar","abr","may","jun","jul","ago","sep","oct","nov","dic"],
    nav=["Herramientas", "Servicios", "Sobre mí", "Contacto"],
    h2="Herramientas que creo",
    intro="Utilidades de Windows para técnicos y usuarios avanzados. Todas están abiertas en GitHub, con notas de versión y sumas de verificación para cada descarga.",
    feat_p="Una sola app para Windows Update, la actualización de Windows y Office. Úsala portátil o instálala desde el mismo EXE; el MSI está disponible para despliegue silencioso. En inglés, hebreo y español.",
    latest="Última", dl="Descargar", direct="Descarga directa", dl_gh="Descargar de GitHub", src="Código", more_wt="Más sobre WinTool", notes="Notas de versión",
    unsigned="Los archivos no tienen firma de código; Windows SmartScreen puede avisar. Compruébalos con SHA256SUMS.txt.",
    caps=[("Windows Update", "Buscar, elegir qué instalar, programar, gestionar reinicios. Nació de WinUpdate Tool."),
          ("Actualización de Windows", "Actualización in situ con comprobaciones antes de empezar. Nació de Windows Upgrade Tool."),
          ("Office", "Instalar, paquete sin conexión, desinstalar. Nació de Smart Office Installer.")],
    how_h="Cómo llegamos hasta aquí",
    how_p="Construyo Windows desde los alegres tiempos de XP. Todas estas herramientas nacen de una idea: conservar el hardware que la gente ya tiene y ahorrarle todos los gastos posibles. De la más nueva a la más antigua; cada paso tiene su propia página.",
    today="Hoy", step="Paso", story="La historia", in_wt="En WinTool", retired="Retirada",
    tools="Herramientas", fits="Su lugar en la historia",
    why_h="Por qué la creé", does_h="Qué hace", grew_h="Cómo creció", carried_h="Qué pasó a WinTool",
    move_h="¿Te pasas a WinTool?", go_wt="Ir a WinTool", newer="Más nueva", older="Más antigua",
    placeholder="[Tu historia: qué problema la originó]",
    came_h="¿Vienes de una herramienta anterior?",
    T={
     "wintool": dict(
        short="Todos los pasos de abajo en una sola app. Idea el 30 de octubre de 2026, primera versión oficial el 7 de noviembre.",
        became="Windows Update + actualización de Windows + Office, un solo EXE",
        lede="Una sola app para Windows Update, la actualización de Windows y Office.",
        why=["Cada una de mis herramientas tenía su propia ventana, sus registros, su actualizador y su instalador. Una sola app hace todo eso una vez, y el PC tiene una herramienta en lugar de tres."],
        does=["Un solo EXE: úsalo portátil o instálalo, incluso sin conexión. El MSI está disponible para despliegue silencioso.",
              "Windows Update: buscar, elegir qué actualizaciones instalar, ejecuciones programadas, gestión de reinicios.",
              "Actualización de Windows: actualización in situ desde una ISO o los medios de Microsoft, con comprobaciones antes de empezar.",
              "Office: Microsoft 365 u Office LTSC 2024, Visio y Project; instalar, paquete sin conexión, desinstalar.",
              "Registros, enlaces útiles y una actualización automática que pregunta antes. En inglés, hebreo y español; sigue el modo claro u oscuro de Windows."],
        grew=[("30 oct 2026", "La idea de una sola app, por escrito"), ("7 nov 2026", "1.0.0, la primera versión oficial, y 1.0.1 con el español revisado"), ("8 nov 2026", "1.0.2")],
        carried=None,
        move="WinTool detecta WinUpdate Tool V1 o V2, ofrece importar la programación y desinstala la herramienta antigua, para que nunca haya dos herramientas actualizando el mismo PC."),
     "upgrade": dict(
        short="Actualización in situ a Windows 10 u 11, pensada sobre todo para los PCs que Microsoft ya no admite sobre el papel. De la primera prueba a la versión candidata en dos días.",
        became="Pasó a ser la página de actualización de Windows en WinTool",
        lede="Una actualización in situ a Windows 10 u 11, pensada sobre todo para los PCs que Microsoft ya no admite sobre el papel.",
        why=["Esta herramienta funciona bien en hardware actual, pero se creó para los equipos que Microsoft ya no admite sobre el papel.",
             "Trabajo con Windows desde los alegres tiempos de XP, y terminé mis estudios de ingeniero de sistemas Microsoft poco después de la salida de Server 2003. Con los años seguí afinando un oficio: crear imágenes personalizadas de Windows. Y, sinceramente, lo que Windows realmente necesita de un PC no ha cambiado mucho desde Vista.",
             "Al mismo tiempo, siempre he sido el técnico de cada comunidad en la que he vivido. Mi regla es sencilla: cuando la vida te va bien, es el momento de devolver. Por eso intento, con sinceridad, conservar el hardware que la gente ya tiene y ahorrarle todos los gastos posibles, sobre todo a quienes menos pueden permitirse un PC nuevo."],
        does=["Guía una actualización in situ a Windows 10 u 11 en PCs x64, incluido hardware antiguo, desde una ISO o los medios de Microsoft.",
              "Muestra en una sola pantalla la versión actual de Windows, el almacenamiento y las opciones de origen. Portátil, con interfaz gráfica y línea de comandos.",
              "La ruta a Windows 11 para hardware no compatible es experimental. Haz una copia de seguridad de tus archivos antes."],
        grew=[("10 oct 2026", "Primera prueba privada"), ("11 oct 2026", "Primera versión candidata"), ("5 nov 2026", "1.3.0")],
        carried=["El mismo motor de actualización, portado a .NET Framework 4.8", "Todas las comprobaciones antes de iniciar Setup: medios, edición, idioma, almacenamiento", "Actualización por línea de comandos con los códigos de salida de WinTool"],
        move="La página de actualización de Windows en WinTool hace lo mismo, junto a las actualizaciones y Office."),
     "v2": dict(
        short="Una interfaz nueva en la que eliges qué actualizaciones instalar, con canal de actualizaciones, programación, revisión de controladores y restablecimiento de un servicio de actualización atascado. MSI o EXE portátil.",
        became="Pasó a ser las páginas de Windows Update y programación en WinTool",
        lede="Un actualizador independiente que funciona por separado de Windows Update.",
        why=None,
        does=["Te deja elegir qué actualizaciones instalar, una opción que el propio Windows Update quitó en los últimos años. Puedes dejar una fuera durante un tiempo, por ejemplo para hacer pruebas tras un fallo; Windows volverá a ofrecerla más adelante.",
              "Busca, instala y programa actualizaciones, revisa los controladores y puede restablecer un servicio de actualización atascado.",
              "Úsalo cuando un PC no se actualiza solo o para agilizar el trabajo de un técnico.",
              "MSI para despliegue o EXE portátil. Se actualiza solo después de verificar la descarga."],
        grew=[("jul 2026", "Primera versión candidata: interfaz nueva y canal de actualizaciones"), ("jul a nov 2026", "Más de 30 versiones de prueba y estables"), ("5 nov 2026", "2.2.8, publicada solo después de pasar las pruebas automáticas")],
        carried=["Elegir qué actualizaciones instalar", "Buscar, previsualizar e instalar, reescrito en C#", "Ejecuciones programadas con reintento, activación del equipo y ejecución si se perdió", "Gestión de reinicios, comprobación de estado y restablecimiento"],
        move="WinTool detecta esta herramienta, ofrece importar su programación y la desinstala, para que nunca haya dos herramientas actualizando el mismo PC."),
     "v1": dict(
        short="Un pequeño EXE para ejecutar Windows Update en PCs que no se actualizaban solos. En junio de 2026 ya tenía MSI, EXE portátil y línea de comandos.",
        became="Creció hasta convertirse en WinUpdate Tool V2",
        lede="Donde empezaron las herramientas de Windows Update: una herramienta para PCs que no se actualizaban solos.",
        why=None,
        does=["Una ventana para buscar y ejecutar Windows Update, programar ejecuciones, leer registros y revisar controladores.",
              "Modos de línea de comandos para estado, actualizaciones, revisión de controladores, recopilación de registros y restablecimiento de Windows Update.",
              "MSI con despliegue silencioso o EXE portátil."],
        grew=[("may 2025", "Primera compilación: un pequeño EXE"), ("jun 2026", "1.1.2: MSI, EXE portátil y línea de comandos"), ("jul 2026", "Publicada en GitHub; V2 toma el relevo")],
        carried=["V1 creció hasta V2, y WinTool lleva el motor de V2", "Ejecuciones de actualización programadas", "Revisión de controladores y despliegue silencioso"],
        move="WinTool detecta V1, ofrece importar su programación y la desinstala."),
     "office": dict(
        short="Aquí empezó todo: unas configuraciones de Office Deployment Tool y un script de una línea. Después un instalador por lotes, una interfaz gráfica en marzo de 2026 y tres versiones principales en una semana.",
        became="Pasó a ser la página de Office en WinTool",
        lede="Instala o desinstala Microsoft Office con la herramienta oficial de Microsoft, Office Deployment Tool.",
        why=None,
        does=["Office LTSC 2024 o Microsoft 365 con elección de canal de actualizaciones, y Visio y Project opcionales.",
              "Elección de idioma, desinstalación de un Office existente y paquete LTSC sin conexión.",
              "Se actualiza sola después de preguntar. Necesitas una licencia válida de Office."],
        grew=[("oct 2024", "Configuraciones de Office Deployment Tool y un script de una línea"), ("jun 2025", "Un instalador por lotes y su primer EXE"),
              ("mar 2026", "Un instalador gráfico, y después las versiones 1.0, 2.0 y 3.0 en una semana"), ("jul 2026", "Publicada en GitHub en la 3.3"), ("nov 2026", "3.3.15")],
        carried=["Las mismas opciones: LTSC 2024, Microsoft 365, Visio, Project, todos los idiomas", "La última versión de Office Deployment Tool, verificada antes de usarla", "Instalar, paquete sin conexión y desinstalar, también por línea de comandos"],
        move="La página de Office en WinTool hace lo mismo, junto a las actualizaciones y la actualización de Windows."),
    })

# ---------------------------------------------------------------- Hebrew
L["he"] = dict(
    dir="rtl", months=["ינואר","פברואר","מרץ","אפריל","מאי","יוני","יולי","אוגוסט","ספטמבר","אוקטובר","נובמבר","דצמבר"],
    nav=["כלים", "שירותים", "אודות", "צור קשר"],
    h2="הכלים שאני בונה",
    intro="כלים ל-Windows לטכנאים ולמשתמשים ביתיים מתקדמים. כל אחד מהם פתוח ב-GitHub, עם הערות גרסה ו-checksum לכל הורדה.",
    feat_p="אפליקציה אחת ל-Windows Update, לשדרוג Windows ול-Office. מריצים אותה כניידת או מתקינים מאותו קובץ EXE; ה-MSI זמין להפצה שקטה. באנגלית, עברית וספרדית.",
    latest="חדש", dl="הורדה", direct="הורדה ישירה", dl_gh="הורדה מ-GitHub", src="קוד מקור", more_wt="עוד על WinTool", notes="הערות גרסה",
    unsigned="הקבצים אינם חתומים דיגיטלית, ולכן Windows SmartScreen עשוי להזהיר. בדקו אותם מול SHA256SUMS.txt.",
    caps=[("Windows Update", "סריקה, בחירה מה להתקין, תזמון וטיפול באתחולים. צמח מתוך WinUpdate Tool."),
          ("שדרוג Windows", "שדרוג במקום, עם בדיקות לפני שמתחילים. צמח מתוך Windows Upgrade Tool."),
          ("Office", "התקנה, חבילה לא מקוונת והסרה. צמח מתוך Smart Office Installer.")],
    how_h="איך הגענו לכאן",
    how_p="אני בונה Windows עוד מימי ה-XP העליזים. כל הכלים כאן נולדו מרעיון אחד: להשאיר אצל אנשים את החומרה שכבר יש להם ולחסוך להם כל עלות אפשרית. מהחדש לישן; לכל שלב יש עמוד משלו.",
    today="היום", step="שלב", story="הסיפור", in_wt="חלק מ-WinTool", retired="הוצא משימוש",
    tools="כלים", fits="המקום שלו בסיפור",
    why_h="למה בניתי אותו", does_h="מה הוא עושה", grew_h="איך הוא גדל", carried_h="מה עבר ל-WinTool",
    move_h="עוברים ל-WinTool?", go_wt="ל-WinTool", newer="חדש יותר", older="ישן יותר",
    placeholder="[הסיפור שלך: איזו בעיה הובילה לכלי]",
    came_h="מגיעים מכלי קודם?",
    T={
     "wintool": dict(
        short="כל השלבים שלמטה באפליקציה אחת. הרעיון נכתב ב-30 באוקטובר 2026, והגרסה הרשמית הראשונה יצאה ב-7 בנובמבר.",
        became="Windows Update + שדרוג Windows + Office, בקובץ EXE אחד",
        lede="אפליקציה אחת ל-Windows Update, לשדרוג Windows ול-Office.",
        why=["לכל אחד מהכלים שלי היו חלון משלו, יומנים משלו, מנגנון עדכון משלו ומתקין משלו. אפליקציה אחת עושה את כל זה פעם אחת, ובמחשב יש כלי אחד במקום שלושה."],
        does=["קובץ EXE אחד: מריצים אותו כנייד או מתקינים, גם בלי חיבור לאינטרנט. ה-MSI זמין להפצה שקטה.",
              "Windows Update: סריקה, בחירה אילו עדכונים להתקין, הרצות מתוזמנות וטיפול באתחולים.",
              "שדרוג Windows: שדרוג במקום מקובץ ISO או ממדיה של Microsoft, עם בדיקות לפני שמתחילים.",
              "Office: Microsoft 365 או Office LTSC 2024, עם Visio ו-Project; התקנה, חבילה לא מקוונת והסרה.",
              "יומנים, קישורים שימושיים ועדכון עצמי ששואל קודם. באנגלית, עברית וספרדית; מתאים את עצמו למצב הכהה או הבהיר של Windows."],
        grew=[("30 באוקטובר 2026", "הרעיון של אפליקציה אחת, על הכתב"), ("7 בנובמבר 2026", "גרסה 1.0.0, הגרסה הרשמית הראשונה, וגרסה 1.0.1 עם ספרדית שנבדקה"), ("8 בנובמבר 2026", "גרסה 1.0.2")],
        carried=None,
        move="WinTool מזהה את WinUpdate Tool V1 או V2, מציע לייבא את התזמון ומסיר את הכלי הישן, כך ששני כלים לעולם לא מעדכנים את אותו מחשב."),
     "upgrade": dict(
        short="שדרוג במקום ל-Windows 10 או 11, שנבנה בעיקר בשביל מחשבים ש-Microsoft כבר לא תומכת בהם על הנייר. מהבדיקה הראשונה ועד גרסה מועמדת לשחרור ביומיים.",
        became="הפך לעמוד שדרוג Windows ב-WinTool",
        lede="שדרוג במקום ל-Windows 10 או 11, שנבנה בעיקר בשביל המחשבים ש-Microsoft כבר לא תומכת בהם על הנייר.",
        why=["הכלי עובד היטב גם על חומרה עדכנית, אבל הוא נבנה בשביל המחשבים ש-Microsoft כבר לא תומכת בהם על הנייר.",
             "אני עובד עם Windows עוד מימי ה-XP העליזים, וסיימתי את לימודי מהנדס מערכות Microsoft קצת אחרי שיצא Server 2003. לאורך השנים המשכתי לחדד ולהשחיז מלאכה אחת: בניית אימג&#39;ים מותאמים של Windows. ובכנות, מה ש-Windows באמת צריך ממחשב לא השתנה הרבה מאז Vista.",
             "במקביל תמיד הייתי הטכנאי של כל קהילה שגרתי בה. הכלל שלי פשוט: כשהולך לנו טוב בחיים, זה הזמן להחזיר לקהילה. לכן אני מנסה, בכנות ובתום לב, להשאיר אצל אנשים את החומרה שכבר יש להם ולחסוך להם כל עלות אפשרית, ובמיוחד למי שהכי פחות יכול להרשות לעצמו מחשב חדש."],
        does=["מלווה שדרוג במקום ל-Windows 10 או 11 במחשבי x64, כולל חומרה ישנה, מקובץ ISO או ממדיה של Microsoft.",
              "מציג במסך אחד את גרסת Windows הנוכחית, את מצב האחסון ואת אפשרויות המקור. נייד, עם ממשק גרפי ושורת פקודה.",
              "המסלול ל-Windows 11 בחומרה שאינה נתמכת הוא ניסיוני. גבו את הקבצים לפני שמתחילים."],
        grew=[("10 באוקטובר 2026", "בדיקה פרטית ראשונה"), ("11 באוקטובר 2026", "גרסה מועמדת ראשונה לשחרור"), ("5 בנובמבר 2026", "גרסה 1.3.0")],
        carried=["אותו מנוע שדרוג, מותאם ל-.NET Framework 4.8", "כל הבדיקות לפני ש-Setup מתחיל: מדיה, מהדורה, שפה ואחסון", "שדרוג משורת הפקודה עם קודי היציאה של WinTool"],
        move="עמוד שדרוג Windows ב-WinTool עושה את אותה עבודה, לצד העדכונים ו-Office."),
     "v2": dict(
        short="ממשק חדש שבו בוחרים אילו עדכונים להתקין, עם ערוץ עדכונים, תזמון, בדיקת דרייברים ואיפוס של שירות עדכונים תקוע. MSI או EXE נייד.",
        became="הפך לעמודי Windows Update והתזמון ב-WinTool",
        lede="כלי עדכון עצמאי שפועל בנפרד מ-Windows Update המובנה.",
        why=None,
        does=["בוחרים אילו עדכונים להתקין, יכולת ש-Windows Update עצמו לקח מהמשתמשים בשנים האחרונות. אפשר להשאיר עדכון בחוץ לזמן מה, למשל כדי לבדוק אחרי תקלה; Windows יציע אותו שוב בהמשך.",
              "בודק, מתקין ומתזמן עדכונים, בודק דרייברים ויכול לאפס שירות עדכונים תקוע.",
              "מתאים למחשב שלא מצליח להתעדכן לבד, או כדי לזרז את העבודה של טכנאי.",
              "MSI להפצה או EXE נייד. מעדכן את עצמו אחרי שהוא מאמת את ההורדה."],
        grew=[("יולי 2026", "גרסה מועמדת ראשונה: ממשק חדש וערוץ עדכונים"), ("יולי עד נובמבר 2026", "יותר מ-30 גרסאות ניסיון ויציבות"), ("5 בנובמבר 2026", "גרסה 2.2.8, שמתפרסמת רק אחרי שהבדיקות האוטומטיות עוברות")],
        carried=["בחירה אילו עדכונים להתקין", "סריקה, תצוגה מקדימה והתקנה, שנכתבו מחדש ב-C#", "הרצות מתוזמנות עם ניסיון חוזר, הערת המחשב והשלמת הרצה שהוחמצה", "טיפול באתחולים, בדיקת תקינות ואיפוס"],
        move="WinTool מזהה את הכלי הזה, מציע לייבא את התזמון שלו ומסיר אותו, כך ששני כלים לעולם לא מעדכנים את אותו מחשב."),
     "v1": dict(
        short="קובץ EXE קטן להרצת Windows Update במחשבים שלא התעדכנו לבד. עד יוני 2026 כבר היו לו MSI, EXE נייד ושורת פקודה.",
        became="התפתח ל-WinUpdate Tool V2",
        lede="המקום שבו התחילו כלי העדכונים: כלי למחשבים שלא התעדכנו לבד.",
        why=None,
        does=["חלון לבדיקה ולהרצה של Windows Update, לתזמון הרצות, לקריאת יומנים ולבדיקת דרייברים.",
              "מצבי שורת פקודה לבדיקת מצב, לעדכונים, לבדיקת דרייברים, לאיסוף יומנים ולאיפוס Windows Update.",
              "MSI עם הפצה שקטה, או EXE נייד."],
        grew=[("מאי 2025", "הבנייה הראשונה: קובץ EXE קטן"), ("יוני 2026", "גרסה 1.1.2: MSI, EXE נייד ושורת פקודה"), ("יולי 2026", "פורסם ב-GitHub; V2 נכנס במקומו")],
        carried=["V1 התפתח ל-V2, ו-WinTool נושא את המנוע של V2", "הרצות עדכון מתוזמנות", "בדיקת דרייברים והפצה שקטה"],
        move="WinTool מזהה את V1, מציע לייבא את התזמון שלו ומסיר אותו."),
     "office": dict(
        short="כאן הכול התחיל: כמה הגדרות ל-Office Deployment Tool וסקריפט של שורה אחת. אחר כך מתקין אצווה, ממשק גרפי במרץ 2026 ושלוש גרסאות ראשיות בשבוע אחד.",
        became="הפך לעמוד Office ב-WinTool",
        lede="מתקין או מסיר את Microsoft Office בעזרת Office Deployment Tool, הכלי הרשמי של Microsoft.",
        why=None,
        does=["Office LTSC 2024 או Microsoft 365 עם בחירת ערוץ עדכונים, ו-Visio ו-Project לפי בחירה.",
              "בחירת שפה, הסרה של Office קיים וחבילת LTSC לא מקוונת.",
              "מעדכן את עצמו אחרי שהוא שואל. נדרש רישיון Office בתוקף."],
        grew=[("אוקטובר 2024", "הגדרות ל-Office Deployment Tool וסקריפט של שורה אחת"), ("יוני 2025", "מתקין אצווה וקובץ ה-EXE הראשון שלו"),
              ("מרץ 2026", "מתקין גרפי, ואחריו גרסאות 1.0, 2.0 ו-3.0 בשבוע אחד"), ("יולי 2026", "פורסם ב-GitHub בגרסה 3.3"), ("נובמבר 2026", "גרסה 3.3.15")],
        carried=["אותן אפשרויות: LTSC 2024, Microsoft 365, Visio, Project וכל השפות", "הגרסה האחרונה של Office Deployment Tool, מאומתת לפני השימוש", "התקנה, חבילה לא מקוונת והסרה, גם משורת הפקודה"],
        move="עמוד Office ב-WinTool עושה את אותה עבודה, לצד העדכונים והשדרוג."),
    })

# Personal stories ("Why I built it"). {v1_url} is filled in by build.py.
W = {}
W["en"] = {
 "office": [
  "Since Microsoft moved Office to Click-to-Run, a lot of people have got tangled up installing it.",
  "For years I solved that for them: install scripts built right into the Windows image, and later silent EXEs.",
  "Then I moved from support specialist to automation, and changed my approach: instead of installing for people, I started building tools they can use themselves. The installation stays flexible on purpose, because whatever license goes in later changes the installation after the fact. So we start somewhere, and from there people can get where they need to go."],
 "v1": [
  "This one started on my own PC. Something broke, and I had neither the time nor the patience to reformat. Windows Update kept recommending a &#8220;reinstall&#8221; of Windows, and every attempt failed.",
  "Maybe, then as now, Microsoft holds back upgrades on PCs older than 8th-generation Intel on purpose. I understand why: newer hardware has security features built in. But for people who just want their PC to work, it makes no sense, because those PCs work very well regardless.",
  "So I set out to build a tool that behaves like a system I&#8217;ve managed for a long time at several workplaces: BigFix, where a managed agent does the work in large organizations. I wanted something like it for the personal world, the free world, as I like to call it. After all, that&#8217;s the world I grew up in and came up from.",
  "And that&#8217;s what happened: I built a tool that worked around my problem."],
 "v2": ["The story starts with V1: a problem on my own PC that grew into a tool anyone can use. <a class=\"more\" href=\"{v1_url}\">Read it on the WinUpdate Tool V1 page &#8594;</a>"],
 "upgrade_pre": [
  "With time came upgrade season. I already knew how to install Windows clean while working around Microsoft&#8217;s stricter hardware rules, but upgrading in place was always the hard part. That&#8217;s how Windows Upgrade Tool was born.",
  "Over the years I learned Microsoft&#8217;s less documented ways of upgrading existing systems in place. Safe to say I got the hang of it, and the tool&#8217;s abilities grew with it."],
}
W["es"] = {
 "office": [
  "Desde que Microsoft pasó Office a Hacer clic y ejecutar (Click-to-Run), mucha gente se ha enredado al instalarlo.",
  "Durante años lo resolví por ellos: scripts de instalación integrados en la propia imagen de Windows y, más tarde, EXE silenciosos.",
  "Luego pasé de especialista de soporte a la automatización y cambié de enfoque: en lugar de instalar por la gente, empecé a crear herramientas que pudieran usar por sí mismos. La instalación se mantiene flexible a propósito, porque la licencia que se ponga después cambia la instalación a posteriori. Así que empezamos por algo y, desde ahí, cada uno puede llegar adonde necesite."],
 "v1": [
  "Esta empezó en mi propio PC. Algo falló y no tenía ni el tiempo ni la paciencia para formatearlo. Windows Update no dejaba de recomendarme &#8220;reinstalar&#8221; Windows, y cada intento fallaba.",
  "Puede que, entonces como ahora, Microsoft frene a propósito las actualizaciones en PCs anteriores a los Intel de 8.ª generación. Entiendo el motivo: el hardware nuevo trae seguridad integrada. Pero para quien solo quiere que su PC funcione no tiene sentido, porque esos equipos funcionan muy bien de todos modos.",
  "Así que me propuse crear una herramienta que se comportara como un sistema que administro desde hace mucho en varios trabajos: BigFix, donde un agente gestionado hace el trabajo en grandes organizaciones. Quería algo parecido para el mundo personal, el mundo libre, como me gusta llamarlo. Al fin y al cabo, es el mundo en el que crecí y desde el que llegué hasta aquí.",
  "Y eso fue lo que pasó: creé una herramienta que esquivaba mi problema."],
 "v2": ["La historia empieza con V1: un problema en mi propio PC que creció hasta ser una herramienta para cualquiera. <a class=\"more\" href=\"{v1_url}\">Léela en la página de WinUpdate Tool V1 &#8594;</a>"],
 "upgrade_pre": [
  "Con el tiempo llegó la temporada de actualizaciones. Yo ya sabía instalar Windows desde cero esquivando las reglas de hardware más estrictas de Microsoft, pero actualizar in situ siempre fue lo difícil. Así nació Windows Upgrade Tool.",
  "Con los años aprendí los caminos menos documentados de Microsoft para actualizar in situ sistemas existentes. Se puede decir que le pillé el truco, y las capacidades de la herramienta crecieron con ello."],
}
W["he"] = {
 "office": [
  "מאז ש-Office עבר לתצורת Click-to-Run, הרבה אנשים הסתבכו עם ההתקנה שלו.",
  "שנים פתרתי את זה בשבילם: קבצי התקנה שנבנו כבר בתוך אימג&#39; ה-Windows, ואחר כך גם קובצי EXE שקטים.",
  "כשעברתי מעבודה של מומחה תמיכה לניהול אוטומציה, שיניתי גישה: במקום להתקין בשביל אנשים, התחלתי לבנות כלים שהם יכולים להשתמש בהם בעצמם. ההתקנה נשארת גמישה בכוונה, כי כל רישיון שמכניסים אחר כך משנה את אופי ההתקנה בדיעבד. אז מתחילים ממשהו, ומשם כל אחד יכול להתקדם לאן שהוא צריך."],
 "v1": [
  "הסיפור הזה התחיל במחשב האישי שלי. הייתה לי תקלה, ולא היו לי זמן או סבלנות לפרמט אותו. Windows Update לא הפסיק להמליץ לי על &#8220;התקנה מחדש&#8221; של מערכת ההפעלה, וכל ניסיון נכשל.",
  "יתכן שאז, וגם היום, Microsoft עוצרת בכוונה שדרוגים במחשבים עם מעבדי Intel ישנים מדור 8. זה מובן, כי בחומרה חדשה יש אבטחת מידע מובנית. אבל זה מגוחך בשביל אנשים שרק רוצים שהמחשב יעבוד, כי הוא עובד יפה מאוד למרות הכול.",
  "מכאן יצאתי לבנות כלי שמתנהג כמו מערכת שאני מנהל כבר הרבה זמן בכמה מקומות עבודה: BigFix, שבה סוכן מנוהל עושה את העבודה בארגונים גדולים. רציתי משהו דומה לעולם הפרטי, העולם החינמי כמו שאני אוהב לתאר אותו. בכל זאת, זה העולם שבו גדלתי ושממנו הגעתי עד לכאן.",
  "וזה מה שקרה: בניתי כלי שעוקף את התקלה שהייתה לי אז."],
 "v2": ["הסיפור מתחיל ב-V1: תקלה במחשב האישי שלי שהפכה לכלי שכל אחד יכול להשתמש בו. <a class=\"more\" href=\"{v1_url}\">לסיפור בעמוד של WinUpdate Tool V1 &#8592;</a>"],
 "upgrade_pre": [
  "עם הזמן הגיעה תקופת השדרוגים. כבר ידעתי להתקין Windows נקי תוך עקיפת חוקי החומרה המחמירים של Microsoft, אבל שדרוג במקום תמיד היה החלק הבעייתי. ככה נולד Windows Upgrade Tool.",
  "לאורך השנים למדתי את הדרכים הפחות מתועדות של Microsoft לשדרוג במקום של מערכות קיימות. אפשר לומר שהבנתי את העניין, והיכולות של הכלי גדלו בהתאם."],
}

# The forward-looking vision (timeline "Next" row and the WinTool page).
V = {
 "en": dict(label="Next", when="Soon", title="What&#8217;s next",
   short="Some form of management for personal, home and small-business setups, at the lowest cost possible: a clear view of the health of every PC in the &#8220;organization&#8221;, and real control over it. Soon in my home lab.",
   h="Looking ahead",
   paras=["The next step is some form of management for personal, home and small-organization environments, at the lowest cost possible.",
          "The goal: a clear view of the health of every computer in the &#8220;organization&#8221;, and real control over it. I&#8217;ll be testing options like that in my home lab soon."]),
 "es": dict(label="Próximo", when="Pronto", title="Lo que viene",
   short="Algún tipo de gestión para entornos personales, domésticos y de pequeñas empresas, con el menor gasto posible: una visión clara de la salud de cada PC de la &#8220;organización&#8221; y un control real sobre ella. Pronto en mi laboratorio en casa.",
   h="Mirando hacia adelante",
   paras=["El siguiente paso es algún tipo de gestión para entornos personales, domésticos y de pequeñas organizaciones, con el menor gasto posible.",
          "El objetivo: una visión clara de la salud de cada equipo de la &#8220;organización&#8221; y un control real sobre ella. Pronto probaré opciones así en mi laboratorio en casa."]),
 "he": dict(label="הבא", when="בקרוב", title="מה הלאה",
   short="יכולת ניהול כזו או אחרת לסביבה אישית, ביתית או לארגון קטן, בעלות הנמוכה ביותר שאפשר: תמונה ברורה של מצב הבריאות של כל מחשב ב&#8220;ארגון&#8221;, ושליטה מעולה עליו. בקרוב במעבדה הביתית שלי.",
   h="מבט קדימה",
   paras=["הצעד הבא הוא יכולת ניהול כזו או אחרת לסביבה אישית, ביתית או לארגון קטן, בעלות הנמוכה ביותר שאפשר.",
          "המטרה: תמונה ברורה של מצב הבריאות של כל מחשב ב&#8220;ארגון&#8221;, ושליטה מעולה עליו. בקרוב אבדוק אפשרויות כאלה במעבדה הביתית שלי."]),
}

# Put the stories in place.
for _l in W:
    for _k in ("office", "v1", "v2"):
        L[_l]["T"][_k]["why"] = W[_l][_k]
    L[_l]["T"]["upgrade"]["why"] = W[_l]["upgrade_pre"] + L[_l]["T"]["upgrade"]["why"][1:]
