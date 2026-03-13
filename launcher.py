#!/usr/bin/env python3
"""
Universal launcher for LIS Builder
Works on Windows, macOS and Linux
"""

import sys
import os
import subprocess

def main():
    # Cambiar al directorio del script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
    
    # Obtener el intérprete de Python del venv
    if sys.platform == "win32":
        python_exe = os.path.join(script_dir, "venv", "Scripts", "python.exe")
    else:
        python_exe = os.path.join(script_dir, "venv", "bin", "python3")
    
    # Verificar que el venv existe
    if not os.path.exists(python_exe):
        print(f"Error: Virtual environment not found at {python_exe}")
        print("Please run: python3 -m venv venv")
        sys.exit(1)
    
    # Ejecutar main.py
    try:
        subprocess.run([python_exe, "main.py"], check=False)
    except FileNotFoundError:
        print(f"Error: Could not find Python executable at {python_exe}")
        sys.exit(1)

if __name__ == "__main__":
    main()
