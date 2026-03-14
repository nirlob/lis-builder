# LIS Builder - Generador de Instaladores para Linux

Una aplicación Python con GTK 4 para generar instaladores `.lis` para aplicaciones Linux (similar a AppImage, pero con instalación completa).

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

### Ejecutar desde VSCode

Presiona **F5** para ejecutar y depurar automáticamente (funciona en cualquier SO).

VSCode automáticamente:
- ✅ Detecta el venv
- ✅ Ejecuta mediante `main.py` (macOS y Linux)
- ✅ Abre en modo depuración

### Ejecutar manualmente desde terminal

**macOS/Linux:**
```bash
./run.sh
```

## Características

- **HeaderBar** con botón Build para generar .lis
- **Menú** con opciones (About, Settings, Quit)
- **StackSidebar** con secciones modulares:
  - **Home**: Información básica del proyecto (nombre, versión, descripción, icono, licencia, privilegios sudo)
  - **Files**: Archivos y carpetas a incluir en el instalador
  - **Settings**: Directorios de instalación (home del usuario) y requisitos del sistema Linux
  - **Installer**: Configuración del instalador (iconos, accesos directos en escritorio/menú, idiomas)
  - **Advanced**: Variables de entorno, comandos post-instalación, archivos de configuración del sistema
  - **Build**: Vista previa y construcción del archivo .lis

## Estructura del Proyecto

```
lis-builder/
├── main.py              # Aplicación principal
├── run.sh              # Script para ejecutar en macOS/Linux
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
