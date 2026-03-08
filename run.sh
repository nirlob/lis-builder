#!/bin/bash
# Script para ejecutar LIS Builder en macOS/Linux

# Obtener el directorio donde está este script
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Cambiar al directorio del proyecto
cd "$SCRIPT_DIR"

# Activar el entorno virtual
source venv/bin/activate

# Ejecutar la aplicación
python3 main.py
