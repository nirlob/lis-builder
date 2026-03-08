# LIS Builder - Instalador

Una aplicación Python con GTK 4 para instalar LIS (Licensing System) en tu sistema.

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

### Primera vez:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 main.py
```

### Próximas veces:

```bash
source venv/bin/activate
python3 main.py
```

## Características

- Instalador con interfaz GTK 4
- StackSidebar con múltiples pasos de instalación:
  - **Presentation**: Bienvenida al usuario
  - **License**: Aceptación de términos
  - **Administrator**: Configuración del administrador
  - **Directories**: Selección de directorios de instalación
  - **Options**: Selección de componentes
  - **Finish**: Confirmación de completado

## Estructura del Proyecto

```
lis-builder/
├── main.py              # Aplicación principal
├── requirements.txt     # Dependencias
├── README.md           # Este archivo
├── .gitignore          # Archivos a ignorar en Git
└── pages/              # Módulo de páginas
    ├── __init__.py
    ├── presentation.py  # Página de presentación
    ├── license.py      # Página de licencia
    ├── administrator.py # Página de administrador
    ├── directories.py  # Página de directorios
    ├── options.py      # Página de opciones
    └── finish.py       # Página de finalización
```

## Autor

Jose - 2026
