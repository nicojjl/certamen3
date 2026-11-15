#!/usr/bin/env python3
"""
FIS120 / FIS12125 · Certamen 3 · UTFSM
Script de Prueba de Mutación (Mutation Testing)
Verifica que las suites de prueba fallen de manera determinista al introducir defectos:
  (a) Mutación A: Cambia un correctValue en +2% en una copia de js/data/ -> verificar_numericos.py DEBE FALLAR.
  (b) Mutación B: Cambia un resultado analítico conocido en verificar.py (ln 2 por ln 3) -> verificar.py DEBE FALLAR.
  (c) Mutación C: Borra una figura en una copia de img/ -> check_figures.py DEBE FALLAR.
  (d) Mutación D: Introduce una barra invertida extra (\\\\) en un js/data/ -> lint_latex.py DEBE FALLAR.

Sale con código 0 solo si las 4 mutaciones fueron detectadas y rechazadas exitosamente (exit code != 0 en cada una).
"""

import os
import sys
import re
import shutil
import tempfile
import subprocess

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PYTHON_EXE = sys.executable

def run_mutation_a():
    """(a) Cambiar un correctValue en +2% -> verificar_numericos.py debe fallar."""
    print("\n--- Ejecutando Mutación A: correctValue +2% ---")
    with tempfile.TemporaryDirectory() as tmpdir:
        temp_data = os.path.join(tmpdir, 'data')
        shutil.copytree(os.path.join(BASE_DIR, 'js', 'data'), temp_data)

        target_file = os.path.join(temp_data, 'module0.js')
        with open(target_file, 'r', encoding='utf-8') as f:
            content = f.read()

        def replacer(m):
            val = float(m.group(1))
            mutated_val = round(val * 1.02, 6)
            return f"correctValue: {mutated_val}"

        mutated_content = re.sub(r'correctValue:\s*([0-9\.]+)', replacer, content, count=1)
        assert mutated_content != content, "No se pudo aplicar la mutación A en module0.js"

        with open(target_file, 'w', encoding='utf-8') as f:
            f.write(mutated_content)

        env = os.environ.copy()
        env['DATA_DIR'] = temp_data
        cmd = [PYTHON_EXE, os.path.join(BASE_DIR, 'scripts', 'verificar_numericos.py')]
        res = subprocess.run(cmd, env=env, capture_output=True, text=True)

        if res.returncode != 0:
            print(f"  [PASS] Mutación A detectada exitosamente: verificar_numericos.py falló con código {res.returncode}")
            return True
        else:
            print("  [FAIL] Mutación A NO detectada: verificar_numericos.py no detectó la alteración del 2%")
            return False

def run_mutation_b():
    """(b) Cambiar ln 2 por ln 3 en verificar.py -> verificar.py debe fallar."""
    print("\n--- Ejecutando Mutación B: ln 2 por ln 3 en verificar.py ---")
    with tempfile.TemporaryDirectory() as tmpdir:
        temp_script = os.path.join(tmpdir, 'verificar_mutated.py')
        orig_script = os.path.join(BASE_DIR, 'scripts', 'verificar.py')

        with open(orig_script, 'r', encoding='utf-8') as f:
            content = f.read()

        # Reemplazar sp.log(2) por sp.log(3) en Ayudantía 11 P2
        mutated_content = content.replace("sp.log(2)", "sp.log(3)", 1)
        assert mutated_content != content, "No se pudo aplicar la mutación B en verificar.py"

        with open(temp_script, 'w', encoding='utf-8') as f:
            f.write(mutated_content)

        cmd = [PYTHON_EXE, temp_script]
        res = subprocess.run(cmd, cwd=BASE_DIR, capture_output=True, text=True)

        if res.returncode != 0:
            print(f"  [PASS] Mutación B detectada exitosamente: verificar.py falló con código {res.returncode}")
            return True
        else:
            print("  [FAIL] Mutación B NO detectada: verificar.py no detectó el cambio ln 2 -> ln 3")
            return False

def run_mutation_c():
    """(c) Borrar una figura -> check_figures.py debe fallar."""
    print("\n--- Ejecutando Mutación C: borrar una figura ---")
    with tempfile.TemporaryDirectory() as tmpdir:
        temp_img = os.path.join(tmpdir, 'img')
        shutil.copytree(os.path.join(BASE_DIR, 'img'), temp_img)

        # Borrar una figura SVG
        target_svg = os.path.join(temp_img, 'mod0_cross_product.svg')
        if os.path.exists(target_svg):
            os.remove(target_svg)

        env = os.environ.copy()
        env['IMG_DIR'] = temp_img
        cmd = [PYTHON_EXE, os.path.join(BASE_DIR, 'scripts', 'check_figures.py')]
        res = subprocess.run(cmd, env=env, cwd=BASE_DIR, capture_output=True, text=True)

        if res.returncode != 0:
            print(f"  [PASS] Mutación C detectada exitosamente: check_figures.py falló con código {res.returncode}")
            return True
        else:
            print("  [FAIL] Mutación C NO detectada: check_figures.py no detectó la figura faltante")
            return False

def run_mutation_d():
    """(d) Introducir \\\\ extra -> lint_latex.py debe fallar."""
    print("\n--- Ejecutando Mutación D: barra invertida extra \\\\ en js/data/ ---")
    with tempfile.TemporaryDirectory() as tmpdir:
        temp_data = os.path.join(tmpdir, 'data')
        shutil.copytree(os.path.join(BASE_DIR, 'js', 'data'), temp_data)

        # Insertar cuatro barras invertidas consecutivas (\\\\) en module0.js
        target_file = os.path.join(temp_data, 'module0.js')
        with open(target_file, 'r', encoding='utf-8') as f:
            content = f.read()

        mutated_content = content.replace('\\\\vec{A}', '\\\\\\\\vec{A}', 1)
        assert mutated_content != content, "No se pudo aplicar la mutación D en module0.js"

        with open(target_file, 'w', encoding='utf-8') as f:
            f.write(mutated_content)

        cmd = [PYTHON_EXE, os.path.join(BASE_DIR, 'scripts', 'lint_latex.py'), temp_data]
        res = subprocess.run(cmd, capture_output=True, text=True)

        if res.returncode != 0:
            print(f"  [PASS] Mutación D detectada exitosamente: lint_latex.py falló con código {res.returncode}")
            return True
        else:
            print("  [FAIL] Mutación D NO detectada: lint_latex.py no detectó el escape cuádruple")
            return False

def main():
    print("=" * 75)
    print("SUITE DE PRUEBAS DE MUTACIÓN (MUTATION TESTING)")
    print("=" * 75)

    results = {
        "Mutación A (correctValue +2%)": run_mutation_a(),
        "Mutación B (ln 2 por ln 3 en verificar.py)": run_mutation_b(),
        "Mutación C (borrado de figura en img/)": run_mutation_c(),
        "Mutación D (escape cuádruple en LaTeX)": run_mutation_d(),
    }

    passed_count = sum(1 for v in results.values() if v)
    total_count = len(results)

    print("\n" + "=" * 75)
    print(f"RESUMEN PRUEBAS DE MUTACIÓN: {passed_count}/{total_count} MUTACIONES RECHAZADAS EXITOSAMENTE")
    print("=" * 75)

    for name, ok in results.items():
        status = "DETECTADA [PASS]" if ok else "NO DETECTADA [FAIL]"
        print(f"  • {name:48s}: {status}")

    if passed_count == total_count:
        print("\nTodas las suites de prueba son sensibles a fallos y rechazan mutaciones críticas.")
        sys.exit(0)
    else:
        print(f"\n[ERROR] Se detectaron {total_count - passed_count} mutaciones no atrapadas.")
        sys.exit(1)

if __name__ == '__main__':
    main()
