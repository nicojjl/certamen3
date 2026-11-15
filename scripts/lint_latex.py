#!/usr/bin/env python3
"""
FIS120 / FIS12125 · Certamen 3 · UTFSM
Linter de secuencias de escape de LaTeX en archivos JavaScript
Verifica:
1. Que ningún archivo en js/data/*.js contenga barras simples
   inadvertidas seguidas de t, b, n, r, f, v, u, x (secuencias de escape nativas de JS).
2. Que no existan secuencias de 4 o más barras invertidas seguidas (\\\\\\\\ o más).
"""

import glob
import os
import re
import sys

TARGET_CHARS = "tbnrfvux"
# Patrón 1: barra invertida que NO esté precedida por otra barra invertida,
# seguida de una de las letras diana (t, b, n, r, f, v, u, x).
PATTERN_SINGLE_SLASH = re.compile(r"(?<!\\)\\([tbnrfvux][a-zA-Z]*)")

# Patrón 2: 4 o más barras invertidas consecutivas
PATTERN_OVERESCAPED = re.compile(r"\\{4,}")

def lint_files():
    data_dir = sys.argv[1] if len(sys.argv) > 1 else os.environ.get("DATA_DIR") or os.path.join(os.path.dirname(__file__), "..", "js", "data")
    js_files = sorted(glob.glob(os.path.join(data_dir, "*.js")))
    
    total_violations = 0
    violations_by_file = {}

    for filepath in js_files:
        filename = os.path.basename(filepath)
        with open(filepath, "r", encoding="utf-8") as f:
            lines = f.readlines()

        file_violations = []
        for line_num, line in enumerate(lines, start=1):
            # Check 1: barras simples seguidas de caracteres diana
            for match in PATTERN_SINGLE_SLASH.finditer(line):
                matched_token = match.group(0)
                file_violations.append((line_num, "single_slash", matched_token, line.strip()))

            # Check 2: 4 o más barras invertidas consecutivas
            for match in PATTERN_OVERESCAPED.finditer(line):
                matched_token = match.group(0)
                file_violations.append((line_num, "quad_slash", f"{len(matched_token)} barras", line.strip()))

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
            for line_num, vtype, token, line_content in viols:
                snippet = line_content if len(line_content) <= 80 else line_content[:77] + "..."
                if vtype == "single_slash":
                    print(f"  Línea {line_num:4d}: Barra simple con token '{token}' -> {snippet}")
                else:
                    print(f"  Línea {line_num:4d}: Secuencia de {token} -> {snippet}")
        print("\nCorrige los escapes:")
        print("  - Barras simples: duplica la barra (ej: \\\\theta, \\\\frac).")
        print("  - 4+ barras: reduce a dos barras (\\\\) o usa \\\\cr en entornos matriciales/cases.")
        sys.exit(1)
    else:
        print(f"[OK] 0 secuencias de escape no deseadas encontradas en {len(js_files)} archivos analizados.")
        print("  - 0 barras simples con caracteres de control de JS (t, b, n, r, f, v, u, x).")
        print("  - 0 secuencias de 4 o más barras invertidas.")
        sys.exit(0)

if __name__ == "__main__":
    lint_files()
