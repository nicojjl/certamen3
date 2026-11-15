#!/usr/bin/env python3
"""
FIS120 / FIS12125 · Certamen 3 · UTFSM
Script de Verificación de Consistencia Numérica Independiente
Recorre todos los js/data/module*.js, extrae los ejercicios numéricos con 'correctValue',
calcula el resultado analítico independiente con fórmulas de física en Python y valida
que el valor de la web coincide estrictamente dentro de la tolerancia declarada.
"""

import os
import re
import sys
import math

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, 'js', 'data')

# Constantes físicas fundamentales (CODATA / UTFSM)
MU_0 = 4.0 * math.pi * 1e-7      # H/m (permeabilidad en el vacío)
EPS_0 = 8.854e-12                 # F/m (permitividad en el vacío)
G_GRAV = 9.8                      # m/s^2 (aceleración de gravedad estándar)

def theoretical_solutions():
    """
    Diccionario de soluciones teóricas calculadas de forma 100% independiente
    a partir de los primeros principios y parámetros del enunciado.
    """
    solutions = {}

    # Módulo 0 - Ejercicio 2 (m0_ex2): Flujo magnético vectorial
    # B = 0.50 T, a = 0.20 m, b = 0.30 m, theta = 60 deg
    A_m0 = 0.20 * 0.30
    solutions['m0_ex2'] = {
        'title': 'Flujo Vectorial con Producto Punto',
        'formula': 'B * A * cos(theta)',
        'calc': 0.50 * A_m0 * math.cos(math.radians(60))
    }

    # Módulo 1 - Ejercicio 2 (m1_ex2): Campo magnético de cable infinito
    # I = 15.0 A, r = 0.060 m
    solutions['m1_ex2'] = {
        'title': 'Campo a Distancia de Cable Infinito',
        'formula': 'mu0 * I / (2 * pi * r)',
        'calc': (MU_0 * 15.0) / (2.0 * math.pi * 0.060)
    }

    # Módulo 1 - Ejercicio 5 (m1_ex5): Punto de campo neto nulo entre cables paralelos
    # d = 30.0 cm, I1 = 4.0 A, I2 = 8.0 A
    solutions['m1_ex5'] = {
        'title': 'Punto de Campo Neto Nulo entre Cables',
        'formula': 'd * I1 / (I1 + I2)',
        'calc': 30.0 * 4.0 / (4.0 + 8.0)
    }

    # Módulo 2 - Ejercicio 2 (m2_ex2): Corriente total con perfil parabólico J(r)
    # J0 = 400.0 A/m^2, a = 0.050 m -> I_T = pi * J0 * a^2
    solutions['m2_ex2'] = {
        'title': 'Corriente con Densidad Parabólica',
        'formula': 'pi * J0 * a^2',
        'calc': math.pi * 400.0 * (0.050 ** 2)
    }

    # Módulo 3 - Ejercicio 2 (m3_ex2): Campo interior de cilindro macizo homogéneo
    # I = 16.0 A, R = 0.040 m, r = 0.020 m (r = R/2)
    solutions['m3_ex2'] = {
        'title': 'Campo Interior Conductor Homogéneo',
        'formula': 'mu0 * I * r / (2 * pi * R^2)',
        'calc': (MU_0 * 16.0 * 0.020) / (2.0 * math.pi * (0.040 ** 2))
    }

    # Módulo 4 - Ejercicio 2 (m4_ex2): Corriente inducida en espira cuadrada
    # L = 0.20 m, dB/dt = 0.50 T/s, R = 4.0 ohm -> I_ind = (L^2 * |dB/dt|) / R
    solutions['m4_ex2'] = {
        'title': 'Corriente Inducida en Espira Cuadrada',
        'formula': '(L^2 * |dB/dt|) / R',
        'calc': ((0.20 ** 2) * 0.50 / 4.0) * 1000.0  # en mA
    }

    # Módulo 5 - Ejercicio 2 (m5_ex2): Fuerza magnética sobre varilla
    # I = 2.5 A, L = 0.40 m, B = 0.80 T -> F = I * L * B
    solutions['m5_ex2'] = {
        'title': 'Fuerza Magnética sobre Conductor',
        'formula': 'I * L * B',
        'calc': 2.5 * 0.40 * 0.80
    }

    # Módulo 5 - Ejercicio 4 (m5_ex4): Velocidad terminal en caída por rieles
    # m = 0.050 kg, g = 9.8 m/s^2, R = 2.0 ohm, B = 0.50 T, L = 0.25 m
    # vt = (m * g * R) / (B^2 * L^2)
    solutions['m5_ex4'] = {
        'title': 'Velocidad Terminal en Caída por Rieles',
        'formula': '(m * g * R) / (B^2 * L^2)',
        'calc': (0.050 * G_GRAV * 2.0) / ((0.50 ** 2) * (0.25 ** 2))
    }

    # Módulo 6 - Ejercicio 2 (m6_ex2): fem inducida por inductancia mutua
    # M = 0.35 H, dI1/dt = 60.0 A/s -> |eps| = M * |dI1/dt|
    solutions['m6_ex2'] = {
        'title': 'fem Inducida por Acoplamiento Mutuo',
        'formula': 'M * |dI/dt|',
        'calc': 0.35 * 60.0
    }

    # Módulo 6 - Ejercicio 4 (m6_ex4): Relación de voltajes en transformador ideal
    # Vp = 220.0 V, Np = 800, Ns = 40 -> Vs = Vp * (Ns / Np)
    solutions['m6_ex4'] = {
        'title': 'Voltaje en Transformador Reductor',
        'formula': 'Vp * (Ns / Np)',
        'calc': 220.0 * (40.0 / 800.0)
    }

    # Módulo 7 - Ejercicio 2 (m7_ex2): Energía magnética almacenada en inductor
    # L = 0.80 H, I = 3.0 A -> UL = 0.5 * L * I^2
    solutions['m7_ex2'] = {
        'title': 'Energía Almacenada en Inductor',
        'formula': '0.5 * L * I^2',
        'calc': 0.5 * 0.80 * (3.0 ** 2)
    }

    # Módulo 7 - Ejercicio 4 (m7_ex4): fem autoinducida en apertura de circuito
    # L = 0.40 H, Delta_i = 2.0 A, Delta_t = 0.0040 s -> |eps_L| = L * Delta_i / Delta_t
    solutions['m7_ex4'] = {
        'title': 'fem Autoinducida en Apertura Brusca',
        'formula': 'L * (Delta_i / Delta_t)',
        'calc': 0.40 * (2.0 / 0.0040)
    }

    # Módulo 8 - Ejercicio 2 (m8_ex2): Constante de tiempo RC (Pauta C3 P3c)
    # R = 370 ohm, C = 5.0e-6 F -> tau_C = R * C (en ms)
    solutions['m8_ex2'] = {
        'title': 'Constante de Tiempo RC',
        'formula': 'R * C * 1000',
        'calc': 370.0 * 5.0e-6 * 1000.0  # en ms
    }

    # Módulo 9 - Ejercicio 2 (m9_ex2): Resistencia crítica en circuito RLC
    # L = 0.20 H, C = 5.0e-6 F -> Rcrit = 2 * sqrt(L / C)
    solutions['m9_ex2'] = {
        'title': 'Resistencia Crítica RLC',
        'formula': '2 * sqrt(L / C)',
        'calc': 2.0 * math.sqrt(0.20 / 5.0e-6)
    }

    # Módulo 10 - Ejercicio 2 (m10_ex2): Corriente de desplazamiento en capacitor
    # eps0 = 8.854e-12 F/m, A = 0.050 m^2, dE/dt = 2.0e11 V/(m*s) -> Id = eps0 * A * dE/dt
    solutions['m10_ex2'] = {
        'title': 'Corriente de Desplazamiento',
        'formula': 'eps0 * A * (dE/dt)',
        'calc': EPS_0 * 0.050 * 2.0e11
    }

    return solutions

def extract_numerical_exercises(file_path):
    """
    Analiza un archivo js/data/module*.js y extrae los ejercicios de tipo numérico.
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Patrón para identificar bloques de ejercicios numéricos
    pattern = re.compile(
        r"id:\s*['\"]([^'\"]+)['\"].*?"
        r"type:\s*['\"]numerical['\"].*?"
        r"correctValue:\s*([0-9eE\.\-]+).*?"
        r"tolerance:\s*([0-9eE\.\-]+)",
        re.DOTALL
    )

    exercises = []
    # También podemos buscar objetos por ID y propiedades
    # Para ser robustos, busquemos cada bloque { id: ..., type: 'numerical', ... }
    blocks = re.split(r'\{\s*id:\s*[\'"]', content)
    for block in blocks[1:]:
        ex_id_match = re.match(r"^([^'\"]+)", block)
        if not ex_id_match:
            continue
        ex_id = ex_id_match.group(1)

        type_match = re.search(r"type:\s*['\"]([^'\"]+)['\"]", block)
        if not type_match or type_match.group(1) != 'numerical':
            continue

        val_match = re.search(r"correctValue:\s*([0-9eE\.\-]+)", block)
        tol_match = re.search(r"tolerance:\s*([0-9eE\.\-]+)", block)
        units_match = re.search(r"units:\s*['\"]([^'\"]*)['\"]", block)

        if val_match and tol_match:
            correct_val = float(val_match.group(1))
            tol = float(tol_match.group(1))
            units = units_match.group(1) if units_match else ''
            exercises.append({
                'id': ex_id,
                'correctValue': correct_val,
                'tolerance': tol,
                'units': units
            })

    return exercises

def main():
    print("=" * 70)
    print("VERIFICACIÓN DE CONSISTENCIA NUMÉRICA INDEPENDIENTE")
    print("=" * 70)

    theor_db = theoretical_solutions()
    passed = 0
    total = 0
    failures = []

    files = sorted([f for f in os.listdir(DATA_DIR) if f.startswith('module') and f.endswith('.js')])

    found_ids = set()

    for fname in files:
        fpath = os.path.join(DATA_DIR, fname)
        num_exs = extract_numerical_exercises(fpath)
        if not num_exs:
            continue

        print(f"\n[{fname}] ({len(num_exs)} ejercicios numéricos):")
        for ex in num_exs:
            total += 1
            ex_id = ex['id']
            found_ids.add(ex_id)
            web_val = ex['correctValue']
            tol = ex['tolerance']
            units = ex['units']

            if ex_id not in theor_db:
                msg = f"[FAIL] Ejercicio '{ex_id}' en {fname} no tiene fórmula teórica registrada en el script de prueba."
                print(f"  {msg}")
                failures.append(msg)
                continue

            theor_info = theor_db[ex_id]
            calc_val = theor_info['calc']
            formula = theor_info['formula']
            title = theor_info['title']

            rel_err = abs(calc_val - web_val) / (abs(calc_val) if abs(calc_val) > 1e-12 else 1.0)
            is_valid = rel_err <= tol

            if is_valid:
                passed += 1
                print(f"  [PASS] {ex_id} ({title}):")
                print(f"         Fórmula: {formula}")
                print(f"         Web = {web_val} {units} | Calc = {calc_val:.6g} {units} | Err = {rel_err:.2%} <= Tol = {tol:.1%}")
            else:
                msg = (f"[FAIL] {ex_id} ({title}): Discrepancia fuera de tolerancia!\n"
                       f"       Web = {web_val} {units}, Calc = {calc_val:.6g} {units}\n"
                       f"       Error Relativo = {rel_err:.2%} > Tolerancia Permitida = {tol:.1%}")
                print(f"  {msg}")
                failures.append(msg)

    # Verificar que no quedaron soluciones teóricas huérfanas
    missing_in_web = set(theor_db.keys()) - found_ids
    if missing_in_web:
        for m in missing_in_web:
            msg = f"[WARN] Solución teórica '{m}' no fue encontrada en los archivos de datos JS."
            print(msg)

    print("\n" + "=" * 70)
    print(f"RESUMEN NUMÉRICO: {passed}/{total} EJERCICIOS CORRECTOS Y DENTRO DE TOLERANCIA")
    print("=" * 70)

    if failures or passed != len(theor_db):
        print(f"\nSE DETECTARON {len(failures)} FALLAS EN LA CONSISTENCIA NUMÉRICA:")
        for f in failures:
            print(f" - {f}")
        sys.exit(1)
    else:
        print("Todos los valores de correctValue coinciden estrictamente con la física teórica.")
        sys.exit(0)

if __name__ == '__main__':
    main()
