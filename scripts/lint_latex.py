#!/usr/bin/env python3
"""
FIS120 / FIS12125 · Certamen 3 · UTFSM
Linter de secuencias de escape de LaTeX en archivos JavaScript
Verifica que ningún archivo en js/data/*.js contenga barras simples
inadvertidas seguidas de t, b, n, r, f, v, u, x (secuencias de escape nativas de JS).
"""

import glob
import os
import re
import sys

TARGET_CHARS = "tbnrfvux"
# Patrón: barra invertida que NO esté precedida por otra barra invertida,
# seguida de una de las letras diana (t, b, n, r, f, v, u, x).
PATTERN = re.compile(r"(?<!\\)\\([tbnrfvux][a-zA-Z]*)")

def lint_files():
    data_dir = os.path.join(os.path.dirname(__file__), "..", "js", "data")
    js_files = sorted(glob.glob(os.path.join(data_dir, "*.js")))
    
    total_violations = 0
    violations_by_file = {}

    for filepath in js_files:
        filename = os.path.basename(filepath)
        with open(filepath, "r", encoding="utf-8") as f:
            lines = f.readlines()

        file_violations = []
        for line_num, line in enumerate(lines, start=1):
            # Buscar barras simples seguidas de caracteres diana
            for match in PATTERN.finditer(line):
                matched_token = match.group(0)
                file_violations.append((line_num, matched_token, line.strip()))

        if file_violations:
            violations_by_file[filename] = file_violations
            total_violations += len(file_violations)

    print("=" * 70)
    print("LINT LATEX ESCAPES (js/data/*.js)")
    print("=" * 70)

    if total_violations > 0:
        print(f"[FAIL] Se encontraron {total_violations} secuencias de escape no deseadas:\n")
        for filename, viols in violations_by_file.items():
            print(f"--- {filename} ({len(viols)} errores) ---")
            for line_num, token, line_content in viols:
                snippet = line_content if len(line_content) <= 80 else line_content[:77] + "..."
                print(f"  Línea {line_num:4d}: Token '{token}' -> {snippet}")
        print("\nCorrige los escapes duplicando las barras (ej: \\\\theta, \\\\frac).")
        sys.exit(1)
    else:
        print(f"[OK] 0 secuencias de escape mal escapadas encontradas en {len(js_files)} archivos analizados.")
        print("Todos los comandos LaTeX con t, b, n, r, f, v, u, x están correctamente escapados con doble barra.")
        sys.exit(0)

if __name__ == "__main__":
    lint_files()
