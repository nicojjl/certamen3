#!/usr/bin/env python3
"""
FIS120 / FIS12125 · Certamen 3 · UTFSM
Script de Verificación de Consistencia Numérica Independiente y Rigurosa
1. Extrae todos los ejercicios con type: 'numerical' de js/data/module*.js.
2. Falla (exit 1) si algún ejercicio carece de correctValue o tolerance.
3. Extrae los parámetros numéricos directamente desde el enunciado (statement) y
   valida que coincidan exactamente con las variables de cálculo físico.
4. Evalúa la solución física teórica de forma independiente.
5. Compara el valor web vs valor teórico con tolerancia estricta
   (error relativo <= 1e-6 para exactos, o <= 1e-3 para valores con redondeo de 3-4 cifras significativas),
   NUNCA usando la tolerancia laxa de respuesta de estudiante.
6. Falla si algún ejercicio numérico no tiene fórmula registrada.
"""

import os
import re
import sys
import math

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, 'js', 'data')

# Constantes físicas fundamentales
MU_0 = 4.0 * math.pi * 1e-7      # H/m
EPS_0 = 8.854e-12                 # F/m
G_GRAV = 9.8                      # m/s^2

# Definición de fórmulas teóricas, parámetros esperados y extractores de enunciado
NUMERICAL_REGISTRY = {
    'm0_ex2': {
        'title': 'Flujo Vectorial con Producto Punto',
        'params_patterns': {
            'B': r'B\s*=\s*([0-9\.]+)\s*\\text\{\s*T\s*\}',
            'a': r'a\s*=\s*([0-9\.]+)\s*\\text\{\s*m\s*\}',
            'b': r'b\s*=\s*([0-9\.]+)\s*\\text\{\s*m\s*\}',
            'theta': r'\\theta\s*=\s*([0-9\.]+)\s*\^\\circ'
        },
        'formula_str': 'B * a * b * cos(theta_rad)',
        'compute': lambda p: p['B'] * p['a'] * p['b'] * math.cos(math.radians(p['theta'])),
        'strict_tol': 1e-6
    },
    'm1_ex2': {
        'title': 'Campo a Distancia de Cable Infinito',
        'params_patterns': {
            'I': r'I\s*=\s*([0-9\.]+)\s*\\text\{\s*A\s*\}',
            'r': r'r\s*=\s*[0-9\.]+\s*\\text\{\s*cm\s*\}\s*=\s*([0-9\.]+)\s*\\text\{\s*m\s*\}'
        },
        'formula_str': 'mu0 * I / (2 * pi * r)',
        'compute': lambda p: (MU_0 * p['I']) / (2.0 * math.pi * p['r']),
        'strict_tol': 1e-6
    },
    'm1_ex5': {
        'title': 'Punto de Campo Neto Nulo entre Dos Cables Paralelos',
        'params_patterns': {
            'I1': r'I_1\s*=\s*([0-9\.]+)\s*\\text\{\s*A\s*\}',
            'I2': r'I_2\s*=\s*([0-9\.]+)\s*\\text\{\s*A\s*\}',
            'd': r'd\s*=\s*([0-9\.]+)\s*\\text\{\s*cm\s*\}'
        },
        'formula_str': 'd * I1 / (I1 + I2)',
        'compute': lambda p: p['d'] * p['I1'] / (p['I1'] + p['I2']),
        'strict_tol': 1e-6
    },
    'm2_ex2': {
        'title': 'Cálculo de Corriente con Densidad Parabólica',
        'params_patterns': {
            'a': r'a\s*=\s*([0-9\.]+)\s*\\text\{\s*m\s*\}',
            'J0': r'J_0\s*=\s*([0-9\.]+)\s*\\text\{\s*A/m\s*\}\^2'
        },
        'formula_str': 'pi * J0 * a^2',
        'compute': lambda p: math.pi * p['J0'] * (p['a'] ** 2),
        'strict_tol': 1e-3  # Web declara 3.1416 (redondeo de pi * 400 * 0.0025 = pi)
    },
    'm3_ex2': {
        'title': 'Campo en el Interior de Conductor Homogéneo',
        'params_patterns': {
            'R': r'R\s*=\s*[0-9\.]+\s*\\text\{\s*cm\s*\}\s*=\s*([0-9\.]+)\s*\\text\{\s*m\s*\}',
            'I': r'I\s*=\s*([0-9\.]+)\s*\\text\{\s*A\s*\}',
            'r': r'r\s*=\s*[0-9\.]+\s*\\text\{\s*cm\s*\}\s*=\s*([0-9\.]+)\s*\\text\{\s*m\s*\}'
        },
        'formula_str': 'mu0 * I * r / (2 * pi * R^2)',
        'compute': lambda p: (MU_0 * p['I'] * p['r']) / (2.0 * math.pi * (p['R'] ** 2)),
        'strict_tol': 1e-6
    },
    'm4_ex2': {
        'title': 'fem Inducida en Espira Cuadrada con Campo Lineal',
        'params_patterns': {
            'L': r'L\s*=\s*([0-9\.]+)\s*\\text\{\s*m\s*\}',
            'R': r'R\s*=\s*([0-9\.]+)\s*\\,\s*\\Omega',
            'dB_dt': r'\\frac\{dB\}\{dt\}\s*=\s*(-?[0-9\.]+)\s*\\text\{\s*T/s\s*\}'
        },
        'formula_str': '((L^2 * |dB_dt|) / R) * 1000  [mA]',
        'compute': lambda p: (((p['L'] ** 2) * abs(p['dB_dt'])) / p['R']) * 1000.0,
        'strict_tol': 1e-6
    },
    'm5_ex2': {
        'title': 'Fuerza Magnética sobre Conductor',
        'params_patterns': {
            'L': r'L\s*=\s*([0-9\.]+)\s*\\text\{\s*m\s*\}',
            'I': r'I\s*=\s*([0-9\.]+)\s*\\text\{\s*A\s*\}',
            'B': r'B\s*=\s*([0-9\.]+)\s*\\text\{\s*T\s*\}'
        },
        'formula_str': 'I * L * B',
        'compute': lambda p: p['I'] * p['L'] * p['B'],
        'strict_tol': 1e-6
    },
    'm5_ex4': {
        'title': 'Cálculo Numérico de Velocidad Terminal',
        'params_patterns': {
            'm': r'm\s*=\s*([0-9\.]+)\s*\\text\{\s*kg\s*\}',
            'R': r'R\s*=\s*([0-9\.]+)\s*\\,\s*\\Omega',
            'L': r'L\s*=\s*([0-9\.]+)\s*\\text\{\s*m\s*\}',
            'B': r'B\s*=\s*([0-9\.]+)\s*\\text\{\s*T\s*\}',
            'g': r'g\s*=\s*([0-9\.]+)\s*\\text\{\s*m/s\s*\}\^2'
        },
        'formula_str': '(m * g * R) / (B^2 * L^2)',
        'compute': lambda p: (p['m'] * p['g'] * p['R']) / ((p['B'] ** 2) * (p['L'] ** 2)),
        'strict_tol': 1e-6
    },
    'm6_ex2': {
        'title': 'fem Inducida por Acoplamiento Mutuo',
        'params_patterns': {
            'M': r'M\s*=\s*([0-9\.]+)\s*\\text\{\s*H\s*\}',
            'dI_dt': r'\\frac\{dI_1\}\{dt\}\s*=\s*([0-9\.]+)\s*\\text\{\s*A/s\s*\}'
        },
        'formula_str': 'M * dI_dt',
        'compute': lambda p: p['M'] * p['dI_dt'],
        'strict_tol': 1e-6
    },
    'm6_ex4': {
        'title': 'Voltaje en Transformador Reductor',
        'params_patterns': {
            'Np': r'N_p\s*=\s*([0-9]+)\s*\\text\{\s*vueltas\s*\}',
            'Ns': r'N_s\s*=\s*([0-9]+)\s*\\text\{\s*vueltas\s*\}',
            'Vp': r'V_p\s*=\s*([0-9\.]+)\s*\\text\{\s*V\s*\}'
        },
        'formula_str': 'Vp * (Ns / Np)',
        'compute': lambda p: p['Vp'] * (p['Ns'] / p['Np']),
        'strict_tol': 1e-6
    },
    'm7_ex2': {
        'title': 'Energía Almacenada en Inductor',
        'params_patterns': {
            'L': r'L\s*=\s*([0-9\.]+)\s*\\text\{\s*H\s*\}',
            'I': r'I\s*=\s*([0-9\.]+)\s*\\text\{\s*A\s*\}'
        },
        'formula_str': '0.5 * L * I^2',
        'compute': lambda p: 0.5 * p['L'] * (p['I'] ** 2),
        'strict_tol': 1e-6
    },
    'm7_ex4': {
        'title': 'fem Inducida en Apertura Brusca de Circuito',
        'params_patterns': {
            'L': r'L\s*=\s*([0-9\.]+)\s*\\text\{\s*H\s*\}',
            'dI': r'([0-9\.]+)\s*\\text\{\s*A\s*\}',
            'dt': r'\\Delta t\s*=\s*[0-9\.]+\s*\\text\{\s*ms\s*\}\s*=\s*([0-9\.]+)\s*\\text\{\s*s\s*\}'
        },
        'formula_str': 'L * (dI / dt)',
        'compute': lambda p: p['L'] * (p['dI'] / p['dt']),
        'strict_tol': 1e-6
    },
    'm8_ex2': {
        'title': 'Cálculo de Constante de Tiempo RC',
        'params_patterns': {
            'R': r'R\s*=\s*([0-9\.]+)\s*\\,\s*\\Omega',
            'C': r'C\s*=\s*[0-9\.]+\s*\\,\s*\\mu\\text\{\s*F\s*\}\s*=\s*([0-9\.\s\\times\-\^\{\}]+)\s*\\text\{\s*F\s*\}'
        },
        'formula_str': 'R * C * 1000  [ms]',
        'compute': lambda p: p['R'] * p['C'] * 1000.0,
        'strict_tol': 1e-6
    },
    'm9_ex2': {
        'title': 'Cálculo de Resistencia Crítica',
        'params_patterns': {
            'L': r'L\s*=\s*([0-9\.]+)\s*\\text\{\s*H\s*\}',
            'C': r'C\s*=\s*[0-9\.]+\s*\\,\s*\\mu\\text\{\s*F\s*\}\s*=\s*([0-9\.\s\\times\-\^\{\}]+)\s*\\text\{\s*F\s*\}'
        },
        'formula_str': '2 * sqrt(L / C)',
        'compute': lambda p: 2.0 * math.sqrt(p['L'] / p['C']),
        'strict_tol': 1e-6
    },
    'm10_ex2': {
        'title': 'Cálculo de Corriente de Desplazamiento',
        'params_patterns': {
            'A': r'A\s*=\s*([0-9\.]+)\s*\\text\{\s*m\s*\}\^2',
            'dE_dt': r'\\frac\{dE\}\{dt\}\s*=\s*([0-9\.\s\\times\-\^\{\}]+)\s*\\text\{\s*V/\(m',
            'eps0': r'\\varepsilon_0\s*=\s*([0-9\.\s\\times\-\^\{\}]+)\s*\\text\{\s*F/m\s*\}'
        },
        'formula_str': 'eps0 * A * dE_dt',
        'compute': lambda p: p['eps0'] * p['A'] * p['dE_dt'],
        'strict_tol': 1e-6
    }
}

def parse_scientific_num(val_str):
    """Convierte cadenas con notación científica en LaTeX o texto a float."""
    s = val_str.replace(' ', '').replace('\\times10^{', 'e').replace('}', '')
    s = s.replace('\\cdot10^{', 'e').replace('10^', '1e')
    return float(s)

def parse_module_exercises(file_path):
    """
    Parsea todos los ejercicios de un archivo JS y retorna una lista de diccionarios.
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    blocks = re.split(r'\{\s*id:\s*[\'"]', content)
    exercises = []
    for block in blocks[1:]:
        m_id = re.match(r"^([^'\"]+)", block)
        if not m_id:
            continue
        ex_id = m_id.group(1)

        m_type = re.search(r"type:\s*['\"]([^'\"]+)['\"]", block)
        ex_type = m_type.group(1) if m_type else 'unknown'

        m_title = re.search(r"title:\s*['\"]([^'\"]+)['\"]", block)
        title = m_title.group(1) if m_title else ex_id

        # statement
        m_stmt = re.search(r"statement:\s*`([^`]+)`", block)
        statement = m_stmt.group(1) if m_stmt else ''

        # correctValue
        m_cv = re.search(r"correctValue:\s*([0-9eE\.\-]+)", block)
        correct_val = float(m_cv.group(1)) if m_cv else None

        # tolerance
        m_tol = re.search(r"tolerance:\s*([0-9eE\.\-]+)", block)
        tolerance = float(m_tol.group(1)) if m_tol else None

        # units
        m_un = re.search(r"units:\s*['\"]([^'\"]*)['\"]", block)
        units = m_un.group(1) if m_un else ''

        exercises.append({
            'id': ex_id,
            'title': title,
            'type': ex_type,
            'statement': statement,
            'correctValue': correct_val,
            'tolerance': tolerance,
            'units': units,
            'raw_block': block
        })

    return exercises

def extract_statement_parameters(ex_id, statement, patterns):
    """
    Extrae los parámetros numéricos requeridos desde el enunciado.
    Falla explícitamente si algún parámetro no se puede extraer.
    """
    # Normalizar barras dobles de strings JS a barras simples para matching estándar
    normalized_stmt = statement.replace('\\\\', '\\')
    params = {}
    for param_name, pat in patterns.items():
        m = re.search(pat, normalized_stmt)
        if not m:
            raise ValueError(f"No se pudo extraer el parámetro '{param_name}' con el patrón r'{pat}' del enunciado de {ex_id}.")
        raw_val = m.group(1)
        params[param_name] = parse_scientific_num(raw_val)
    return params

def main():
    sys.stdout.reconfigure(encoding='utf-8')
    print("=" * 75)
    print("VERIFICACIÓN RIGUROSA DE EJERCICIOS NUMÉRICOS (TOLERANCIA ESTRICTA <= 1e-3)")
    print("=" * 75)

    files = sorted([f for f in os.listdir(DATA_DIR) if f.startswith('module') and f.endswith('.js')])

    total_numerical = 0
    passed_numerical = 0
    failures = []
    missing_formulas = []

    for fname in files:
        fpath = os.path.join(DATA_DIR, fname)
        all_exs = parse_module_exercises(fpath)

        for ex in all_exs:
            ex_id = ex['id']
            ex_type = ex['type']

            # Solo procesamos ejercicios con type: 'numerical'
            if ex_type != 'numerical':
                # Si no es numerical pero tiene correctValue, emitir advertencia
                if ex['correctValue'] is not None:
                    failures.append(f"[{fname}] {ex_id}: Ejercicio tiene type='{ex_type}' pero declara correctValue={ex['correctValue']}.")
                continue

            total_numerical += 1
            print(f"\n[{fname}] -> {ex_id} ('{ex['title']}'):")

            # 1. Validar que tenga correctValue y tolerance declarados (no ignorar en silencio)
            if ex['correctValue'] is None:
                msg = f"[{fname}] {ex_id}: FALLA CRÍTICA: Ejercicio type='numerical' no tiene 'correctValue' declarado."
                print(f"  [FAIL] {msg}")
                failures.append(msg)
                continue

            if ex['tolerance'] is None:
                msg = f"[{fname}] {ex_id}: FALLA CRÍTICA: Ejercicio type='numerical' no tiene 'tolerance' declarada."
                print(f"  [FAIL] {msg}")
                failures.append(msg)
                continue

            # 2. Validar que tenga fórmula registrada en el registro
            if ex_id not in NUMERICAL_REGISTRY:
                msg = f"[{fname}] {ex_id}: FALLA: No tiene fórmula teórica registrada en scripts/verificar_numericos.py."
                print(f"  [FAIL] {msg}")
                failures.append(msg)
                missing_formulas.append(ex_id)
                continue

            reg = NUMERICAL_REGISTRY[ex_id]
            patterns = reg['params_patterns']
            compute_fn = reg['compute']
            formula_str = reg['formula_str']
            strict_tol = reg['strict_tol']
            web_val = ex['correctValue']
            units = ex['units']

            # 3. Extraer parámetros directamente del enunciado y verificar consistencia
            try:
                extracted_params = extract_statement_parameters(ex_id, ex['statement'], patterns)
                print(f"  • Parámetros extraídos del statement: {extracted_params}")
            except Exception as e:
                msg = f"[{fname}] {ex_id}: Error extrayendo parámetros del enunciado: {e}"
                print(f"  [FAIL] {msg}")
                failures.append(msg)
                continue

            # 4. Calcular valor teórico independiente
            try:
                calc_val = compute_fn(extracted_params)
            except Exception as e:
                msg = f"[{fname}] {ex_id}: Error en el cálculo físico teórico: {e}"
                print(f"  [FAIL] {msg}")
                failures.append(msg)
                continue

            # 5. Comparar con tolerancia estricta (<= 1e-6 o <= 1e-3 si redondeado)
            ref_denom = abs(calc_val) if abs(calc_val) > 1e-12 else 1.0
            rel_err = abs(calc_val - web_val) / ref_denom

            if rel_err <= strict_tol:
                passed_numerical += 1
                status = "EXACTO" if rel_err <= 1e-6 else "REDONDEADO VÁLIDO"
                print(f"  [PASS] {status} | Fórmula: {formula_str}")
                print(f"         Web = {web_val} {units} | Calc = {calc_val:.8g} {units}")
                print(f"         Error Relativo = {rel_err:.2e} <= Umbral Estricto = {strict_tol:.1e}")
            else:
                msg = (f"[{fname}] {ex_id}: DISCREPANCIA FUERA DE TOLERANCIA ESTRICTA!\n"
                       f"       Web = {web_val} {units} | Calc = {calc_val:.8g} {units}\n"
                       f"       Error Relativo = {rel_err:.4e} > Umbral Estricto = {strict_tol:.1e}\n"
                       f"       (Tolerancia del estudiante en web era {ex['tolerance']:.1%}, pero verificación exige <= {strict_tol:.1e})")
                print(f"  [FAIL] {msg}")
                failures.append(msg)

    print("\n" + "=" * 75)
    print(f"RESUMEN FINAL DE CONSISTENCIA NUMÉRICA: {passed_numerical}/{total_numerical} CORRECTOS")
    print("=" * 75)

    if missing_formulas:
        print("\nEJERCICIOS NUMÉRICOS SIN FÓRMULA REGISTRADA:")
        for mf in missing_formulas:
            print(f" - {mf}")

    if failures:
        print(f"\nSE DETECTARON {len(failures)} FALLAS EN LA VERIFICACIÓN:")
        for f in failures:
            print(f" • {f}")
        sys.exit(1)
    else:
        print("Todos los parámetros coinciden con los enunciados y todos los valores son físicamente exactos.")
        sys.exit(0)

if __name__ == '__main__':
    main()
