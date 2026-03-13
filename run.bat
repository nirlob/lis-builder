@echo off
REM Script para ejecutar LIS Builder en Windows

REM Obtener el directorio del script
cd /d "%~dp0"

REM Activar el entorno virtual
call venv\Scripts\activate.bat

REM Ejecutar la aplicación
python main.py
