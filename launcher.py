#!/usr/bin/env python3
"""
Universal launcher for LIS Builder
Works on macOS and Linux.
"""

import os
import subprocess


def main():
    # Cambiar al directorio del script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)

    # Obtener el intérprete de Python del venv
    python_exe = os.path.join(script_dir, "venv", "bin", "python3")

    # Verificar que el venv existe
    if not os.path.exists(python_exe):
        print(f"Error: Virtual environment not found at {python_exe}")
        print("Please run: python3 -m venv venv")
        return

    # Ejecutar main.py
    try:
        subprocess.run([python_exe, "main.py"], check=False)
    except FileNotFoundError:
        print(f"Error: Could not find Python executable at {python_exe}")

if __name__ == "__main__":
    main()
