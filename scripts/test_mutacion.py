#!/usr/bin/env python3
"""
FIS120 / FIS12125 · Certamen 3 · UTFSM
Suite Integral de Pruebas de Mutación (Mutation Testing)
Verifica que las suites de prueba fallen determinísticamente ante defectos:
  1. Ejecuta primero la línea base SIN mutar y exige exit 0.
  2. Tras la mutación, exige exit != 0 Y la presencia de texto explicativo esperado.
Mutaciones evaluadas:
  (a) Mutación A: Cambia correctValue en +2% -> verificar_numericos.py DEBE FALLAR con [FAIL] y ID.
  (b) Mutación B: Cambia ln 2 por ln 3 en verificar.py -> verificar.py DEBE FALLAR con [FAIL] y 'Ayudantía 11 P2'.
  (c) Mutación C: Borra una figura en img/ -> check_figures.py DEBE FALLAR con [FAIL] y nombre de figura.
  (d) Mutación D: Introduce barra extra \\\\ en js/data/ -> lint_latex.py DEBE FALLAR con [FAIL] y archivo.
  (e) Mutación E: Introduce \frac{ sin cerrar en module0.js -> verify_browser_katex.py DEBE FALLAR con [FAIL].
  (f) Mutación F: Cambia número en statement sin cambiar correctValue -> verificar_numericos.py DEBE FALLAR con [FAIL] y ID.
"""

import os
import sys
import re
import shutil
import tempfile
import subprocess

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PYTHON_EXE = sys.executable

def run_baseline(cmd, env=None, cwd=BASE_DIR, name=""):
    """Ejecuta comando sin mutación previa y exige exit code 0."""
    res = subprocess.run(cmd, env=env, cwd=cwd, capture_output=True, text=True, encoding='utf-8', errors='ignore')
    if res.returncode != 0:
        print(f"  [BASELINE FAIL] La prueba previa de línea base para '{name}' falló (código {res.returncode}):")
        print(res.stdout)
        print(res.stderr)
        return False
    return True

def run_mutation_a():
    """(a) Cambiar un correctValue en +2% -> verificar_numericos.py debe fallar con [FAIL] y m0_ex2."""
    print("\n--- Ejecutando Mutación A: correctValue +2% en m0_ex2 ---")
    
    # 1. Línea base
    base_cmd = [PYTHON_EXE, os.path.join(BASE_DIR, 'scripts', 'verificar_numericos.py')]
    if not run_baseline(base_cmd, name="Mutación A Línea Base"):
        return False

    with tempfile.TemporaryDirectory() as tmpdir:
        temp_data = os.path.join(tmpdir, 'data')
        shutil.copytree(os.path.join(BASE_DIR, 'js', 'data'), temp_data)

        target_file = os.path.join(temp_data, 'module0.js')
        with open(target_file, 'r', encoding='utf-8') as f:
            content = f.read()

        # Mutar correctValue de m0_ex2 (0.015 -> 0.0153)
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
        res = subprocess.run(base_cmd, env=env, cwd=BASE_DIR, capture_output=True, text=True, encoding='utf-8', errors='ignore')

        output = res.stdout + res.stderr
        has_fail_code = res.returncode != 0
        has_fail_tag = "[FAIL]" in output
        has_exercise_id = "m0_ex2" in output

        if has_fail_code and has_fail_tag and has_exercise_id:
            print(f"  [PASS] Mutación A detectada exitosamente: exit {res.returncode}, contiene '[FAIL]' y 'm0_ex2'")
            return True
        else:
            print(f"  [FAIL] Mutación A NO cumplió criterios: code={res.returncode}, tag={has_fail_tag}, id={has_exercise_id}")
            print(output[:300])
            return False

def run_mutation_b():
    """(b) Cambiar ln 2 por ln 3 en verificar.py -> verificar.py debe fallar con [FAIL] y 'Ayudantía 11 P2'."""
    print("\n--- Ejecutando Mutación B: ln 2 por ln 3 en verificar.py ---")
    orig_script = os.path.join(BASE_DIR, 'scripts', 'verificar.py')

    # 1. Línea base
    base_cmd = [PYTHON_EXE, orig_script]
    if not run_baseline(base_cmd, name="Mutación B Línea Base"):
        return False

    with tempfile.TemporaryDirectory() as tmpdir:
        temp_script = os.path.join(tmpdir, 'verificar_mutated.py')
        with open(orig_script, 'r', encoding='utf-8') as f:
            content = f.read()

        mutated_content = content.replace("sp.log(2)", "sp.log(3)", 1)
        assert mutated_content != content, "No se pudo aplicar la mutación B en verificar.py"

        with open(temp_script, 'w', encoding='utf-8') as f:
            f.write(mutated_content)

        cmd = [PYTHON_EXE, temp_script]
        res = subprocess.run(cmd, cwd=BASE_DIR, capture_output=True, text=True, encoding='utf-8', errors='ignore')

        output = res.stdout + res.stderr
        has_fail_code = res.returncode != 0
        has_fail_tag = "[FAIL]" in output
        has_expected_text = "Ayudantía 11 P2" in output

        if has_fail_code and has_fail_tag and has_expected_text:
            print(f"  [PASS] Mutación B detectada exitosamente: exit {res.returncode}, contiene '[FAIL]' y 'Ayudantía 11 P2'")
            return True
        else:
            print(f"  [FAIL] Mutación B NO cumplió criterios: code={res.returncode}, tag={has_fail_tag}, text={has_expected_text}")
            print(output[:300])
            return False

def run_mutation_c():
    """(c) Borrar una figura -> check_figures.py debe fallar con [FAIL] y 'mod0_cross_product.svg'."""
    print("\n--- Ejecutando Mutación C: borrar mod0_cross_product.svg ---")
    
    with tempfile.TemporaryDirectory() as tmpdir:
        temp_img = os.path.join(tmpdir, 'img')
        temp_report = os.path.join(tmpdir, 'salida_figuras_temp.txt')
        shutil.copytree(os.path.join(BASE_DIR, 'img'), temp_img)

        # 1. Línea base en copia limpia
        env_base = os.environ.copy()
        env_base['IMG_DIR'] = temp_img
        env_base['FIGURES_REPORT'] = temp_report
        cmd = [PYTHON_EXE, os.path.join(BASE_DIR, 'scripts', 'check_figures.py')]
        if not run_baseline(cmd, env=env_base, name="Mutación C Línea Base"):
            return False

        # 2. Mutación: Borrar figura
        target_svg = os.path.join(temp_img, 'mod0_cross_product.svg')
        if os.path.exists(target_svg):
            os.remove(target_svg)

        res = subprocess.run(cmd, env=env_base, cwd=BASE_DIR, capture_output=True, text=True, encoding='utf-8', errors='ignore')
        output = res.stdout + res.stderr
        has_fail_code = res.returncode != 0
        has_fail_tag = "[FAIL]" in output
        has_fig_name = "mod0_cross_product.svg" in output

        if has_fail_code and has_fail_tag and has_fig_name:
            print(f"  [PASS] Mutación C detectada exitosamente: exit {res.returncode}, contiene '[FAIL]' y 'mod0_cross_product.svg'")
            return True
        else:
            print(f"  [FAIL] Mutación C NO cumplió criterios: code={res.returncode}, tag={has_fail_tag}, fig={has_fig_name}")
            print(output[:300])
            return False

def run_mutation_d():
    """(d) Barra invertida extra \\\\ en js/data/ -> lint_latex.py debe fallar con [FAIL] y 'module0.js'."""
    print("\n--- Ejecutando Mutación D: barra invertida extra \\\\\\\\ en module0.js ---")
    
    with tempfile.TemporaryDirectory() as tmpdir:
        temp_data = os.path.join(tmpdir, 'data')
        shutil.copytree(os.path.join(BASE_DIR, 'js', 'data'), temp_data)

        # 1. Línea base
        cmd = [PYTHON_EXE, os.path.join(BASE_DIR, 'scripts', 'lint_latex.py'), temp_data]
        if not run_baseline(cmd, name="Mutación D Línea Base"):
            return False

        # 2. Mutación: agregar \\\\vec{B} en module0.js
        target_file = os.path.join(temp_data, 'module0.js')
        with open(target_file, 'r', encoding='utf-8') as f:
            content = f.read()

        mutated_content = content.replace(r'\\vec{B}', r'\\\\vec{B}', 1)
        if mutated_content == content:
            mutated_content = content.replace('title:', 'title: "\\\\\\\\text{Error}",', 1)

        with open(target_file, 'w', encoding='utf-8') as f:
            f.write(mutated_content)

        res = subprocess.run(cmd, cwd=BASE_DIR, capture_output=True, text=True, encoding='utf-8', errors='ignore')
        output = res.stdout + res.stderr
        has_fail_code = res.returncode != 0
        has_fail_tag = "[FAIL]" in output
        has_file_name = "module0.js" in output

        if has_fail_code and has_fail_tag and has_file_name:
            print(f"  [PASS] Mutación D detectada exitosamente: exit {res.returncode}, contiene '[FAIL]' y 'module0.js'")
            return True
        else:
            print(f"  [FAIL] Mutación D NO cumplió criterios: code={res.returncode}, tag={has_fail_tag}, file={has_file_name}")
            print(output[:300])
            return False

def run_mutation_e():
    """(e) Introducir \\frac{ sin cerrar en module0.js -> verify_browser_katex.py debe fallar con [FAIL] y error KaTeX."""
    print("\n--- Ejecutando Mutación E: \\frac{ sin cerrar en module0.js ---")
    
    target_file = os.path.join(BASE_DIR, 'js', 'data', 'module0.js')
    backup_file = target_file + '.bak'
    port = int(os.environ.get("PORT", "8080"))
    cmd = [PYTHON_EXE, os.path.join(BASE_DIR, 'scripts', 'verify_browser_katex.py'), '--port', str(port), '--module', 'mod0', '--no-report']

    # 1. Línea base
    if not run_baseline(cmd, name="Mutación E Línea Base"):
        return False

    # 2. Mutar con respaldo seguro y restauración en finally
    shutil.copyfile(target_file, backup_file)
    try:
        with open(target_file, 'r', encoding='utf-8') as f:
            content = f.read()

        # Inyectar $$\frac{1}{ sin cerrar para que el archivo contenga \frac y cause error real en KaTeX
        mutated_content = content.replace("$$", "$$\\frac{1}{", 1)
        assert mutated_content != content, "No se pudo inyectar \\frac{ sin cerrar en module0.js"
        assert r"\frac" in mutated_content, "El archivo mutado debe contener \\frac"

        with open(target_file, 'w', encoding='utf-8') as f:
            f.write(mutated_content)

        res = subprocess.run(cmd, cwd=BASE_DIR, capture_output=True, text=True, encoding='utf-8', errors='ignore')
        output = res.stdout + res.stderr
        has_fail_code = res.returncode != 0
        has_fail_tag = "[FAIL]" in output
        has_katex = bool(re.search(r'katex', output, re.IGNORECASE))
        has_katex_error = bool(re.search(r'[1-9]\d*\s+errores\s+katex', output, re.IGNORECASE))

        if has_fail_code and has_fail_tag and has_katex and has_katex_error:
            print(f"  [PASS] Mutación E detectada exitosamente: exit {res.returncode}, detectó error real de KaTeX en [mod0]")
            return True
        else:
            print(f"  [FAIL] Mutación E NO cumplió criterios: code={res.returncode}, tag={has_fail_tag}, katex={has_katex}, error={has_katex_error}")
            print(output[:400])
            return False
    finally:
        if os.path.exists(backup_file):
            shutil.copyfile(backup_file, target_file)
            os.remove(backup_file)

def run_mutation_f():
    """(f) Cambiar un número del enunciado sin cambiar correctValue -> verificar_numericos.py debe fallar con [FAIL] y ID."""
    print("\n--- Ejecutando Mutación F: cambiar número de statement en m0_ex2 ---")
    
    base_cmd = [PYTHON_EXE, os.path.join(BASE_DIR, 'scripts', 'verificar_numericos.py')]
    if not run_baseline(base_cmd, name="Mutación F Línea Base"):
        return False

    with tempfile.TemporaryDirectory() as tmpdir:
        temp_data = os.path.join(tmpdir, 'data')
        shutil.copytree(os.path.join(BASE_DIR, 'js', 'data'), temp_data)

        target_file = os.path.join(temp_data, 'module0.js')
        with open(target_file, 'r', encoding='utf-8') as f:
            content = f.read()

        # Cambiar B = 0.5 \text{ T} por B = 0.9 \text{ T} en el enunciado de m0_ex2 sin tocar correctValue (0.015)
        mutated_content = content.replace("B = 0.5", "B = 0.9", 1)
        assert mutated_content != content, "No se pudo mutar el enunciado de m0_ex2 en module0.js"

        with open(target_file, 'w', encoding='utf-8') as f:
            f.write(mutated_content)

        env = os.environ.copy()
        env['DATA_DIR'] = temp_data
        res = subprocess.run(base_cmd, env=env, cwd=BASE_DIR, capture_output=True, text=True, encoding='utf-8', errors='ignore')

        output = res.stdout + res.stderr
        has_fail_code = res.returncode != 0
        has_fail_tag = "[FAIL]" in output
        has_exercise_id = "m0_ex2" in output

        if has_fail_code and has_fail_tag and has_exercise_id:
            print(f"  [PASS] Mutación F detectada exitosamente: exit {res.returncode}, contiene '[FAIL]' y 'm0_ex2'")
            return True
        else:
            print(f"  [FAIL] Mutación F NO cumplió criterios: code={res.returncode}, tag={has_fail_tag}, id={has_exercise_id}")
            print(output[:300])
            return False

def run_mutation_g():
    """(g) Cambiar color de trazo de un SVG a color fijo (#000000) -> verify_figures_contrast.py debe fallar en modo oscuro."""
    print("\n--- Ejecutando Mutación G: trazo negro fijo (#000000) en mod0_coords.svg ---")
    port = int(os.environ.get("PORT", "8080"))
    base_cmd = [PYTHON_EXE, os.path.join(BASE_DIR, 'scripts', 'verify_figures_contrast.py'), str(port)]

    # 1. Línea base
    if not run_baseline(base_cmd, name="Mutación G Línea Base"):
        return False

    with tempfile.TemporaryDirectory() as tmpdir:
        temp_img = os.path.join(tmpdir, 'img')
        temp_preview = os.path.join(tmpdir, '_preview')
        shutil.copytree(os.path.join(BASE_DIR, 'img'), temp_img)

        target_svg = os.path.join(temp_img, 'mod0_coords.svg')
        with open(target_svg, 'r', encoding='utf-8') as f:
            content = f.read()

        # Mutar un trazo a color fijo #000000
        mutated_content = re.sub(r'stroke="var\(--fig-azul[^"]*\)"', 'stroke="#000000"', content, count=1)
        if mutated_content == content:
            mutated_content = content.replace('stroke="currentColor"', 'stroke="#000000"', 1)
        assert mutated_content != content, "No se pudo mutar el trazo en mod0_coords.svg"

        with open(target_svg, 'w', encoding='utf-8') as f:
            f.write(mutated_content)

        env = os.environ.copy()
        env['IMG_DIR'] = temp_img
        env['PREVIEW_DIR'] = temp_preview
        res = subprocess.run(base_cmd, env=env, cwd=BASE_DIR, capture_output=True, text=True, encoding='utf-8', errors='ignore')

        output = res.stdout + res.stderr
        has_fail_code = res.returncode != 0
        has_fail_tag = "[FAIL]" in output
        has_fig_name = "mod0_coords.svg" in output
        has_dark_mode = "DARK" in output.upper()
        has_contrast_fail = ("contraste insuficiente" in output.lower() or "3:1" in output)

        if has_fail_code and has_fail_tag and has_fig_name and has_dark_mode and has_contrast_fail:
            print(f"  [PASS] Mutación G detectada exitosamente: exit {res.returncode}, detectó trazo fijo #000000 con fallo de contraste en modo oscuro")
            return True
        else:
            print(f"  [FAIL] Mutación G NO cumplió criterios: code={res.returncode}, tag={has_fail_tag}, fig={has_fig_name}, dark={has_dark_mode}, contrast={has_contrast_fail}")
            print(output[:400])
            return False

def main():
    print("=" * 75)
    print("SUITE INTEGRAL DE PRUEBAS DE MUTACIÓN (MUTATION TESTING)")
    print("=" * 75)

    results = {
        "A (correctValue +2%)": run_mutation_a(),
        "B (ln 2 por ln 3 en verificar.py)": run_mutation_b(),
        "C (borrado de figura en img/)": run_mutation_c(),
        "D (escape cuádruple en LaTeX)": run_mutation_d(),
        "E (fórmula KaTeX malformada en JS)": run_mutation_e(),
        "F (parámetro de statement alterado)": run_mutation_f(),
        "G (trazo negro #000000 en modo oscuro)": run_mutation_g()
    }

    print("\n" + "=" * 75)
    passed_count = sum(1 for v in results.values() if v)
    total_count = len(results)
    print(f"RESUMEN PRUEBAS DE MUTACIÓN: {passed_count}/{total_count} MUTACIONES RECHAZADAS EXITOSAMENTE")
    print("=" * 75)

    for name, ok in results.items():
        print(f"  • Mutación {name:38s}: {'DETECTADA [PASS]' if ok else 'FALLO NO DETECTADO [FAIL]'}")

    if passed_count == total_count:
        print("\nTodas las suites de prueba son sensibles a fallos y rechazan mutaciones críticas.")
        sys.exit(0)
    else:
        print("\n[ERROR] Algunas mutaciones no fueron detectadas correctamente por los verificadores.")
        sys.exit(1)

if __name__ == '__main__':
    main()
