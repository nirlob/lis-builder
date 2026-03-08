# LIS Builder - Generador de Instaladores

Una aplicación Python con GTK 4 para generar instaladores con extensión `.lis` (similar a .msc de Windows, Inno Setup, NSIS, etc.)

## Requisitos

- Python 3.7+
- PyGObject
- GTK 4 (necesario para el sistema)

## Instalación

### En macOS con Homebrew:

```bash
brew install gtk4 pygobject3
```

### Instalar dependencias de Python:

```bash
pip3 install -r requirements.txt
```

## Ejecución

### Configuración inicial (una sola vez)

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

**Windows (PowerShell):**
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

**Windows (CMD):**
```cmd
python -m venv venv
venv\Scripts\activate.bat
pip install -r requirements.txt
```

### Ejecutar desde VSCode

Presiona **F5** para ejecutar y depurar automáticamente (funciona en cualquier SO).

VSCode automáticamente:
- ✅ Detecta el venv
- ✅ Ejecuta mediante `launcher.py` (compatible con Windows, macOS y Linux)
- ✅ Abre en modo depuración

### Ejecutar manualmente desde terminal

**macOS/Linux:**
```bash
./run.sh
```

**Windows (CMD):**
```cmd
run.bat
```

**Windows (PowerShell):**
```powershell
.\run.bat
```

## Características

- **HeaderBar** con botón Build para generar .lis
- **Menú** con opciones (About, Settings, Quit)
- **StackSidebar** con secciones modulares:
  - **Home**: Información básica del proyecto (nombre, versión, descripción, icono, licencia, privilegios)
  - **Files**: Archivos y carpetas a incluir en el instalador
  - **Settings**: Directorios de instalación y requisitos del sistema
  - **Installer**: Configuración del instalador (iconos, accesos directos, idiomas)
  - **Advanced**: Variables de entorno, comandos post-instalación, registro de Windows
  - **Build**: Vista previa y construcción del archivo .lis

## Estructura del Proyecto

```
lis-builder/
├── main.py              # Aplicación principal
├── launcher.py          # Script universal para ejecutar en todos los SO
├── run.sh              # Script para ejecutar en macOS/Linux
├── run.bat             # Script para ejecutar en Windows
├── requirements.txt    # Dependencias
├── README.md           # Este archivo
├── .gitignore          # Archivos a ignorar en Git
├── .vscode/
│   ├── launch.json     # Configuración de depuración VSCode
│   ├── tasks.json      # Tareas opcionales de VSCode
│   └── settings.json   # Configuración del proyecto
└── pages/              # Módulo de páginas
    ├── __init__.py
    ├── home.py         # Información del proyecto
    ├── files.py        # Archivos a incluir
    ├── settings.py     # Configuración de directorios y requisitos
    ├── installer.py    # Configuración del instalador
    ├── advanced.py     # Opciones avanzadas
    └── build.py        # Construcción y vista previa
```

## Autor

Jose - 2026
