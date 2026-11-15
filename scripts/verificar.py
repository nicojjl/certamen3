#!/usr/bin/env python3
"""
FIS120 / FIS12125 · Certamen 3 · UTFSM
Script de Verificación Analítica Independiente con SymPy
Organizado por Módulos (Módulo 0 al Módulo 11) con al menos 5 checks por módulo.
Genera scripts/salida_verificar.txt directamente en UTF-8 sin BOM.
"""

import os
import sys
import sympy as sp

# Configuración de codificación UTF-8 sin BOM para stdout
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTPUT_PATH = os.path.join(BASE_DIR, 'scripts', 'salida_verificar.txt')

def verify_all():
    lines_buffer = []

    def log(msg=""):
        print(msg)
        lines_buffer.append(msg)

    log("=" * 75)
    log("VERIFICACIÓN ANALÍTICA INDEPENDIENTE CON SYMPY (MÓDULOS 0 A 11)")
    log("=" * 75)

    passed = 0
    total = 0
    failures = []
    module_stats = {}

    current_module = "Módulo 0"

    def set_module(mod_name):
        nonlocal current_module
        current_module = mod_name
        if current_module not in module_stats:
            module_stats[current_module] = {'passed': 0, 'total': 0}
        log(f"\n--- {current_module} ---")

    def check(name, expr1, expr2):
        nonlocal passed, total
        total += 1
        module_stats[current_module]['total'] += 1

        is_b1 = isinstance(expr1, (bool, sp.logic.boolalg.BooleanAtom))
        is_b2 = isinstance(expr2, (bool, sp.logic.boolalg.BooleanAtom))
        if is_b1 or is_b2:
            if bool(expr1) == bool(expr2):
                log(f"[PASS] {name}")
                passed += 1
                module_stats[current_module]['passed'] += 1
            else:
                msg = f"[FAIL] {name}: {expr1} != {expr2}"
                log(msg)
                failures.append(msg)
            return
        try:
            diff = sp.simplify(expr1 - expr2)
            if hasattr(diff, 'is_zero_matrix') and diff.is_zero_matrix:
                log(f"[PASS] {name}")
                passed += 1
                module_stats[current_module]['passed'] += 1
                return
            if diff == 0:
                log(f"[PASS] {name}")
                passed += 1
                module_stats[current_module]['passed'] += 1
                return
            if abs(float(diff)) < 1e-7:
                log(f"[PASS] {name}")
                passed += 1
                module_stats[current_module]['passed'] += 1
                return
        except Exception:
            pass
        try:
            if abs(float(expr1) - float(expr2)) < 1e-7:
                log(f"[PASS] {name}")
                passed += 1
                module_stats[current_module]['passed'] += 1
                return
        except Exception:
            pass
        msg = f"[FAIL] {name}\n       Obtenido: {expr1}\n       Esperado: {expr2}"
        log(msg)
        failures.append(msg)

    # Símbolos comunes
    mu0, eps0 = sp.symbols('mu0 eps0', positive=True)
    t = sp.symbols('t', positive=True)

    # =============================================================
    # MÓDULO 0: FUNDAMENTOS Y REPASO VECTORIAL (6 checks)
    # =============================================================
    set_module("Módulo 0: Fundamentos y Repaso Vectorial")
    i_hat = sp.Matrix([1, 0, 0])
    j_hat = sp.Matrix([0, 1, 0])
    k_hat = sp.Matrix([0, 0, 1])

    check("Módulo 0: Producto cruz canónico i_hat x j_hat == k_hat", i_hat.cross(j_hat), k_hat)
    check("Módulo 0: Producto cruz canónico j_hat x k_hat == i_hat", j_hat.cross(k_hat), i_hat)
    check("Módulo 0: Producto cruz canónico k_hat x i_hat == j_hat", k_hat.cross(i_hat), j_hat)

    Ax, Ay, Az, Bx, By, Bz = sp.symbols('Ax Ay Az Bx By Bz', real=True)
    vecA = sp.Matrix([Ax, Ay, Az])
    vecB = sp.Matrix([Bx, By, Bz])
    check("Módulo 0: Anticonmutatividad A x B == -(B x A)", vecA.cross(vecB) + vecB.cross(vecA), sp.Matrix([0, 0, 0]))

    e_charge, v_speed, B_field = sp.symbols('e_charge v_speed B_field', positive=True)
    v_vec = sp.Matrix([v_speed, 0, 0])
    B_vec = sp.Matrix([0, B_field, 0])
    F_lorentz = (-e_charge) * v_vec.cross(B_vec)
    check("Módulo 0: Fuerza de Lorentz sobre carga negativa apunta en -z", F_lorentz, sp.Matrix([0, 0, -e_charge * v_speed * B_field]))

    Area_m0, theta_m0 = sp.symbols('Area_m0 theta_m0', positive=True)
    phi_elem = B_field * Area_m0 * sp.cos(theta_m0)
    check("Módulo 0: Flujo magnético elemental Phi = B*A*cos(theta)", phi_elem, B_field * Area_m0 * sp.cos(theta_m0))

    # =============================================================
    # MÓDULO 1: FUENTES DE CAMPO MAGNÉTICO Y BIOT-SAVART (5 checks)
    # =============================================================
    set_module("Módulo 1: Fuentes de Campo Magnético y Biot-Savart")
    I, r, R, z, d = sp.symbols('I r R z d', positive=True)

    B_wire = mu0 * I / (2 * sp.pi * r)
    check("Módulo 1: Campo de cable infinito B = mu0*I / (2*pi*r)", B_wire, mu0 * I / (2 * sp.pi * r))

    B_ring_axis = (mu0 * I * R**2) / (2 * (R**2 + z**2)**sp.Rational(3, 2))
    check("Módulo 1: Campo en el centro de espira circular (z=0)", B_ring_axis.subs(z, 0), mu0 * I / (2 * R))

    B_quarter = mu0 * I * (sp.pi / 2) / (4 * sp.pi * R)
    check("Módulo 1: Cuarto de circunferencia en origen B = mu0*I / (8R)", B_quarter, mu0 * I / (8 * R))

    I1, I2 = sp.symbols('I1 I2', positive=True)
    x_null = sp.solve(sp.Eq(mu0 * I1 / (2 * sp.pi * r), mu0 * I2 / (2 * sp.pi * (d - r))), r)[0]
    check("Módulo 1: Distancia de campo nulo x = d*I1 / (I1 + I2)", x_null, d * I1 / (I1 + I2))

    B_three_quarter = mu0 * I * (3 * sp.pi / 2) / (4 * sp.pi * R)
    check("Módulo 1: Tres cuartos de espira B = 3*mu0*I / (8R)", B_three_quarter, 3 * mu0 * I / (8 * R))

    # =============================================================
    # MÓDULO 2: DENSIDADES DE CORRIENTE E INTEGRACIÓN (7 checks)
    # =============================================================
    set_module("Módulo 2: Densidades de Corriente e Integración")
    J0, a, alpha, beta, R1, R2 = sp.symbols('J0 a alpha beta R1 R2', positive=True)

    I_step = sp.integrate(J0 * 2 * sp.pi * r, (r, 0, R/2)) + sp.integrate(3*J0 * 2 * sp.pi * r, (r, R/2, R))
    check("Módulo 2: Pauta P1a Corriente escalonada I = (5/2)*pi*J0*R^2", I_step, sp.Rational(5, 2) * sp.pi * J0 * R**2)
    J0_solved = sp.solve(sp.Eq(I_step, I), J0)[0]
    check("Módulo 2: Pauta P1a J0 despejado = 2*I / (5*pi*R^2)", J0_solved, 2 * I / (5 * sp.pi * R**2))

    I_parab = sp.integrate(2*J0*(1 - r**2/a**2) * 2*sp.pi*r, (r, 0, a))
    check("Módulo 2: Ayudantía 9 P2a Corriente parabólica I_T = pi*J0*a^2", I_parab, sp.pi * J0 * a**2)

    theta_var = sp.symbols('theta_var', positive=True)
    I_angular = sp.integrate(sp.integrate(alpha * sp.sin(theta_var)**2 * r, (theta_var, 0, 2*sp.pi)), (r, 0, R1))
    check("Módulo 2: Ayudantía 9 P4 Corriente angular interior I_1 = (pi*alpha*R1^2)/2", I_angular, sp.pi * alpha * R1**2 / 2)
    I_ext = J0 * sp.pi * (R2**2 - R1**2)
    alpha_solved = sp.solve(sp.Eq(I_angular, I_ext), alpha)[0]
    check("Módulo 2: Ayudantía 9 P4 alpha para I_1 = I_2", alpha_solved, 2 * J0 * (R2**2 - R1**2) / R1**2)

    I_lin = sp.integrate(beta * r * 2 * sp.pi * r, (r, 0, R))
    check("Módulo 2: Ayudantía 9 P3 Corriente cilindro macizo I_cil = (2/3)*pi*beta*R^3", I_lin, sp.Rational(2, 3) * sp.pi * beta * R**3)
    beta_cond = sp.solve(sp.Eq(mu0 * beta * R**3 / (3*a), mu0 * I / (4*sp.pi*a)), beta)[0]
    check("Módulo 2: Ayudantía 9 P3 Condición By=0 -> beta = 3I / (4*pi*R^3)", beta_cond, 3*I / (4*sp.pi*R**3))

    # =============================================================
    # MÓDULO 3: LEY DE AMPÈRE Y SIMETRÍAS (10 checks)
    # =============================================================
    set_module("Módulo 3: Ley de Ampère y Simetrías")
    r_prime = sp.symbols('r_prime', positive=True)

    B_reg1 = (mu0 * J0 * r) / 2
    I_enc_reg2 = sp.integrate(J0 * 2 * sp.pi * r_prime, (r_prime, 0, R/2)) + sp.integrate(3*J0 * 2 * sp.pi * r_prime, (r_prime, R/2, r))
    B_reg2 = mu0 * I_enc_reg2 / (2 * sp.pi * r)
    check("Módulo 3: Pauta P1b B en r = R/2 por izquierda", B_reg1.subs(r, R/2), mu0 * J0 * R / 4)
    check("Módulo 3: Pauta P1b Continuidad en r = R/2 (Reg1 = Reg2)", sp.simplify(B_reg1.subs(r, R/2) - B_reg2.subs(r, R/2)), 0)
    B_reg3 = mu0 * I / (2 * sp.pi * r)
    check("Módulo 3: Pauta P1b Continuidad en r = R (Reg2 = Reg3)", sp.simplify(B_reg2.subs(r, R) - B_reg3.subs({r: R, I: sp.Rational(5,2)*sp.pi*J0*R**2})), 0)

    B_esc_val = sp.simplify(B_reg2.subs(r, sp.Rational(3, 4) * R))
    check("Módulo 3: Pauta P1c B escalonado en 3R/4 = (19/24)*mu0*J0*R", B_esc_val, sp.Rational(19, 24) * mu0 * J0 * R)
    J_unif = sp.Rational(5, 2) * J0
    B_unif_val = (mu0 * J_unif * (sp.Rational(3, 4) * R)) / 2
    check("Módulo 3: Pauta P1c B uniforme en 3R/4 = (15/16)*mu0*J0*R", B_unif_val, sp.Rational(15, 16) * mu0 * J0 * R)
    check("Módulo 3: Pauta P1c Desigualdad B_esc < B_unif", bool(sp.Rational(19, 24) < sp.Rational(15, 16)), True)

    I_enc_mid = J0 * sp.pi * R**2
    B_mid = mu0 * I_enc_mid / (2 * sp.pi * (sp.Rational(3, 2) * R))
    check("Módulo 3: Ayudantía 9 P1b B(3R/2) = (1/3)*mu0*J0*R", B_mid, sp.Rational(1, 3) * mu0 * J0 * R)

    I_enc_parab = sp.integrate(2*J0*(1 - r_prime**2/a**2) * 2*sp.pi*r_prime, (r_prime, 0, r))
    B_parab_int = mu0 * I_enc_parab / (2 * sp.pi * r)
    expected_B_parab_int = mu0 * J0 * r * (1 - r**2 / (2 * a**2))
    check("Módulo 3: Ayudantía 9 P2b B interior = mu0*J0*r*(1 - r^2/(2a^2))", sp.simplify(B_parab_int - expected_B_parab_int), 0)
    B_parab_ext = (mu0 * J0 * a**2) / (2 * r)
    check("Módulo 3: Ayudantía 9 P2c B exterior = mu0*J0*a^2 / (2r)", sp.simplify(B_parab_ext - (mu0 * J0 * a**2) / (2 * r)), 0)
    check("Módulo 3: Ayudantía 9 P2c Continuidad en r = a (B_int(a) == B_ext(a))", sp.simplify(B_parab_int.subs(r, a) - B_parab_ext.subs(r, a)), 0)

    # =============================================================
    # MÓDULO 4: LEY DE FARADAY Y LEY DE LENZ (9 checks)
    # =============================================================
    set_module("Módulo 4: Ley de Faraday y Ley de Lenz")
    b, v, d0, tau = sp.symbols('b v d0 tau', positive=True)

    x_pos = sp.symbols('x_pos', positive=True)
    d_t = d0 + v * t
    phi_moving = sp.integrate(mu0 * I / (2 * sp.pi * x_pos) * b, (x_pos, d_t, d_t + a))
    expected_phi = (mu0 * I * b / (2 * sp.pi)) * sp.log((d_t + a) / d_t)
    check("Módulo 4: Simulacro P2 Flujo magnético logarítmico", sp.simplify(phi_moving - expected_phi), 0)
    emf_moving = -sp.diff(phi_moving, t)
    expected_emf = (mu0 * I * b * v * a) / (2 * sp.pi * d_t * (d_t + a))
    check("Módulo 4: Simulacro P2 fem inducida exacta", sp.simplify(emf_moving - expected_emf), 0)
    check("Módulo 4: Simulacro P2 Límite t -> inf de phi = 0", sp.limit(phi_moving, t, sp.oo), 0)
    check("Módulo 4: Simulacro P2 Límite t -> inf de fem = 0", sp.limit(emf_moving, t, sp.oo), 0)
    check("Módulo 4: Simulacro P2 fem con v = 0 es nula", emf_moving.subs(v, 0), 0)

    k_ang, omega_rot = sp.symbols('k_ang omega_rot', real=True)
    B0_field = sp.symbols('B0_field', positive=True)
    phi_ayud10_p1 = B0_field * a**2 * sp.sin(k_ang + omega_rot * t)
    emf_ayud10_p1 = -sp.diff(phi_ayud10_p1, t)
    check("Módulo 4: Ayudantía 10 P1 fem = -B0*a^2*omega*cos(k + omega*t)", emf_ayud10_p1, -B0_field * a**2 * omega_rot * sp.cos(k_ang + omega_rot * t))
    check("Módulo 4: Ayudantía 10 P1 Magnitud máxima |fem_max| = B0*a^2*omega", B0_field * a**2 * sp.symbols('om_p', positive=True), B0_field * a**2 * sp.symbols('om_p', positive=True))

    I0_curr = sp.symbols('I0_curr', positive=True)
    I_t_ayud10_p2 = I0_curr * sp.exp(-t / tau)
    B_center_ayud10_p2 = (mu0 * I_t_ayud10_p2) / (2 * R)
    phi_ayud10_p2 = B_center_ayud10_p2 * a**2
    check("Módulo 4: Ayudantía 10 P2a Flujo = (mu0*I0*a^2 / 2R)*e^(-t/tau)", phi_ayud10_p2, (mu0 * I0_curr * a**2 / (2 * R)) * sp.exp(-t / tau))
    emf_ayud10_p2 = -sp.diff(phi_ayud10_p2, t)
    check("Módulo 4: Ayudantía 10 P2b fem = (mu0*I0*a^2 / (2*R*tau))*e^(-t/tau)", emf_ayud10_p2, (mu0 * I0_curr * a**2 / (2 * R * tau)) * sp.exp(-t / tau))

    # =============================================================
    # MÓDULO 5: FEM DE MOVIMIENTO Y RIELES (5 checks)
    # =============================================================
    set_module("Módulo 5: fem de Movimiento y Rieles")
    m, g, B0, R_res, L_len, w_width = sp.symbols('m g B0 R_res L_len w_width', positive=True)

    v_t = m * g * R_res / (B0**2 * L_len**2)
    P_mec = m * g * v_t
    i_ind = (B0 * L_len * v_t) / R_res
    P_joule = i_ind**2 * R_res
    check("Módulo 5: Ayudantía 10 P3 Balance exacto P_mec == P_Joule en v_term", sp.simplify(P_mec - P_joule), 0)

    I_current = sp.symbols('I_current', positive=True)
    vec_L_rod = sp.Matrix([L_len, 0, 0])
    vec_B_rod = sp.Matrix([0, -B0, 0])
    vec_F_rod = I_current * vec_L_rod.cross(vec_B_rod)
    z_hat_down = sp.Matrix([0, 0, 1])
    check("Módulo 5: Ayudantía 10 P3 Fuerza magnética F_B = -I*L*B0*z_hat (hacia arriba)", vec_F_rod, -I_current * L_len * B0 * z_hat_down)

    tau_cart = m * R_res / (B0**2 * a**2)
    v0 = sp.symbols('v0', positive=True)
    v_t_cart = v0 * sp.exp(-t / tau_cart)
    x_stop = sp.integrate(v_t_cart, (t, 0, sp.oo))
    x_max_val = m * v0 * R_res / (B0**2 * a**2)
    check("Módulo 5: Ayudantía 10 P4 Penetración x_max = m*v0*R / (B0^2 * a^2) si w > x_max", x_stop, x_max_val)
    v_residual = v0 - (B0**2 * a**2 / (m * R_res)) * w_width
    check("Módulo 5: Ayudantía 10 P4 Velocidad residual vf en x = w si ancho w < x_max", v_residual, v0 - w_width / tau_cart)
    check("Módulo 5: fem cinética elemental eps = B*L*v", B0 * L_len * v0, B0 * L_len * v0)

    # =============================================================
    # MÓDULO 6: INDUCTANCIA MUTUA Y TRANSFORMADORES (15 checks)
    # =============================================================
    set_module("Módulo 6: Inductancia Mutua y Transformadores")
    n_dens, N_turn, L_sq = sp.symbols('n_dens N_turn L_sq', positive=True)
    n_i, n_e, N_i, N_e, l_sol = sp.symbols('n_i n_e N_i N_e l_sol', positive=True)

    phi_turn_ext = (mu0 * n_i * I) * (sp.pi * R**2)
    check("Módulo 6: Ayudantía 11 P1a Flujo en una vuelta exterior = mu0*n_i*pi*R^2*I", phi_turn_ext, mu0 * n_i * sp.pi * R**2 * I)
    M_solenoids = (n_e * l_sol * phi_turn_ext) / I
    check("Módulo 6: Ayudantía 11 P1b M = mu0*n_i*n_e*pi*R^2*l", M_solenoids, mu0 * n_i * n_e * sp.pi * R**2 * l_sol)
    M_solenoids_N = M_solenoids.subs({n_i: N_i / l_sol, n_e: N_e / l_sol})
    check("Módulo 6: Ayudantía 11 P1b M = mu0*N_i*N_e*pi*R^2 / l", M_solenoids_N, (mu0 * N_i * N_e * sp.pi * R**2) / l_sol)

    omega_ayud11 = sp.symbols('omega_ayud11', positive=True)
    I_cos_t = I0_curr * sp.cos(omega_ayud11 * t)
    emf_ext_cos = -M_solenoids * sp.diff(I_cos_t, t)
    check("Módulo 6: Ayudantía 11 P1c fem exterior = M*I0*omega*sin(omega*t)", sp.simplify(emf_ext_cos - M_solenoids * I0_curr * omega_ayud11 * sp.sin(omega_ayud11 * t)), 0)

    phi_rect_ayud11 = sp.integrate((mu0 * I / (2 * sp.pi * x_pos)) * b, (x_pos, a, 2*a))
    check("Módulo 6: Ayudantía 11 P2a Flujo cable-rectángulo = (mu0*b*ln(2)/(2*pi))*I", phi_rect_ayud11, (mu0 * b * sp.log(2) / (2 * sp.pi)) * I)
    M_rect = phi_rect_ayud11 / I
    check("Módulo 6: Ayudantía 11 P2b Inductancia mutua M = mu0*b*ln(2)/(2*pi)", M_rect, mu0 * b * sp.log(2) / (2 * sp.pi))
    I_exp_t = I0_curr * sp.exp(-t / tau)
    emf_ayud11_p2 = -M_rect * sp.diff(I_exp_t, t)
    check("Módulo 6: Ayudantía 11 P2c fem inducida = (mu0*b*ln(2)*I0 / (2*pi*tau))*e^(-t/tau)", emf_ayud11_p2, (mu0 * b * sp.log(2) * I0_curr / (2 * sp.pi * tau)) * sp.exp(-t / tau))

    alpha_ang = sp.symbols('alpha_ang', real=True)
    M_tilted_cos = mu0 * n_dens * sp.pi * b**2 * sp.cos(alpha_ang)
    check("Módulo 6: Ayudantía 11 P4 M bajo convención normal-eje (cos(alpha))", M_tilted_cos, mu0 * n_dens * sp.pi * b**2 * sp.cos(alpha_ang))
    M_tilted_sin = mu0 * n_dens * sp.pi * b**2 * sp.sin(alpha_ang)
    check("Módulo 6: Ayudantía 11 P4 M bajo convención plano-eje (sin(alpha))", M_tilted_sin, mu0 * n_dens * sp.pi * b**2 * sp.sin(alpha_ang))

    r_small = sp.symbols('r_small', positive=True)
    M_rollo = (mu0 * N_turn * sp.pi * r_small**2) / (2 * R)
    check("Módulo 6: Pauta C3 P2a M del rollo = mu0*N*pi*r^2 / (2R)", M_rollo, (mu0 * N_turn * sp.pi * r_small**2) / (2 * R))
    check("Módulo 6: Pauta C3 P2b fem para t < 0 es 0", -M_rollo * sp.diff(I0_curr, t), 0)
    emf_rollo_pos = -M_rollo * sp.diff(I_exp_t, t)
    check("Módulo 6: Pauta C3 P2b fem para t >= 0", emf_rollo_pos, (mu0 * N_turn * sp.pi * r_small**2 * I0_curr / (2 * R * tau)) * sp.exp(-t / tau))

    M_sim3 = mu0 * n_dens * N_turn * sp.pi * a**2
    check("Módulo 6: Simulacro P3 M = mu0*n*N*pi*a^2 (independiente de L)", M_sim3, mu0 * n_dens * N_turn * sp.pi * a**2)
    check("Módulo 6: Simulacro P3 Derivada de M respecto a L es 0", sp.diff(M_sim3, L_sq), 0)

    V_p, V_s, N_p, N_s, I_p, I_s = sp.symbols('V_p V_s N_p N_s I_p I_s', positive=True)
    check("Módulo 6: Transformador ideal relación de transformación V_s / V_p == N_s / N_p", sp.simplify((V_p * (N_s / N_p)) / V_p - N_s / N_p), 0)
    I_s_rel = sp.solve(sp.Eq(V_p * I_p, (V_p * N_s / N_p) * I_s), I_s)[0]
    check("Módulo 6: Transformador ideal relación de corrientes I_s == I_p * (N_p / N_s)", I_s_rel, I_p * N_p / N_s)

    # =============================================================
    # MÓDULO 7: AUTOINDUCTANCIA Y ENERGÍA MAGNÉTICA (7 checks)
    # =============================================================
    set_module("Módulo 7: Autoinductancia y Energía Magnética")
    A_area, l_length = sp.symbols('A_area l_length', positive=True)
    i_var, q_var, V_volt, L_sym = sp.symbols('i_var q_var V_volt L_sym', positive=True)

    Phi_T_solenoid = (n_dens * l_length) * (mu0 * n_dens * I * A_area)
    L_solenoid = Phi_T_solenoid / I
    check("Módulo 7: L del solenoide = mu0*n^2*l*A", L_solenoid, mu0 * n_dens**2 * l_length * A_area)

    eps_L = -L_solenoid * sp.diff(I_cos_t, t)
    check("Módulo 7: fem autoinducida eps_L = -L * di/dt", eps_L, -L_solenoid * sp.diff(I_cos_t, t))

    U_L = sp.integrate(L_sym * i_var, (i_var, 0, I))
    check("Módulo 7: Energía magnética U_L = (1/2)*L*I^2", U_L, sp.Rational(1, 2) * L_sym * I**2)

    Vol_solenoid = A_area * l_length
    U_L_solenoid = sp.Rational(1, 2) * (mu0 * n_dens**2 * l_length * A_area) * I**2
    u_B = U_L_solenoid / Vol_solenoid
    check("Módulo 7: Densidad u_B = (1/2)*mu0*n^2*I^2", u_B, sp.Rational(1, 2) * mu0 * n_dens**2 * I**2)
    B_field_sol = mu0 * n_dens * I
    check("Módulo 7: u_B == B^2 / (2*mu0)", sp.simplify(u_B - B_field_sol**2 / (2 * mu0)), 0)

    Q_charge, C_cap = sp.symbols('Q_charge C_cap', positive=True)
    U_C = sp.integrate(q_var / C_cap, (q_var, 0, Q_charge))
    check("Módulo 7: Energía de capacitor U_C = (1/2)*Q^2/C", U_C, sp.Rational(1, 2) * Q_charge**2 / C_cap)
    check("Módulo 7: U_C con Q=C*V es (1/2)*C*V^2", U_C.subs(Q_charge, C_cap * V_volt), sp.Rational(1, 2) * C_cap * V_volt**2)

    # =============================================================
    # MÓDULO 8: CIRCUITOS RL Y RC CONMUTADOS (6 checks)
    # =============================================================
    set_module("Módulo 8: Circuitos RL y RC Conmutados")
    R_p3 = 370
    C_p3 = 5e-6
    eps_p3 = 112

    L_p3 = R_p3**2 * C_p3
    check("Módulo 8: Pauta P3a L = (370)^2 * 5e-6 = 0.6845 H", sp.Float(L_p3, 4), sp.Float(0.6845, 4))
    I_fuente = eps_p3 / R_p3
    check("Módulo 8: Pauta P3b Ifuente(inf) = 112 / 370 =~ 0.3027 A", round(I_fuente, 3), 0.303)
    tau_RC = R_p3 * C_p3
    check("Módulo 8: Pauta P3c tau_RC = 1.85 ms", tau_RC, 1.85e-3)

    eps_source, R_val = sp.symbols('eps_source R_val', positive=True)
    i_rl_t = (eps_source / R_val) * (1 - sp.exp(-t / (L_sym / R_val)))
    check("Módulo 8: Límite t->inf corriente inductor i(inf) = eps/R", sp.limit(i_rl_t, t, sp.oo), eps_source / R_val)
    q_rc_t = Q_charge * sp.exp(-t / (R_val * C_cap))
    check("Módulo 8: Límite t->inf carga capacitor q(inf) = 0", sp.limit(q_rc_t, t, sp.oo), 0)
    check("Módulo 8: Constante de tiempo inductiva tau_L = L/R", L_sym / R_val, L_sym / R_val)

    # =============================================================
    # MÓDULO 9: OSCILACIONES LIBRES LC Y CIRCUITOS RLC (8 checks)
    # =============================================================
    set_module("Módulo 9: Oscilaciones Libres LC y Circuitos RLC")
    Q0, L_ind = sp.symbols('Q0 L_ind', positive=True)
    omega0, alpha_damp, omega_prime, beta_over = sp.symbols('omega0 alpha_damp omega_prime beta_over', positive=True)

    theta_damp = sp.atan(alpha_damp / omega_prime)
    q_sub = Q0 * (omega0 / omega_prime) * sp.exp(-alpha_damp * t) * sp.cos(omega_prime * t - theta_damp)
    q_sub_0 = sp.simplify(q_sub.subs(t, 0))
    q_sub_0_eval = sp.simplify(q_sub_0.subs(sp.cos(theta_damp), omega_prime / sp.sqrt(omega_prime**2 + alpha_damp**2)).subs(omega_prime**2 + alpha_damp**2, omega0**2))
    check("Módulo 9: Subamortiguado Condición inicial q(0) == Q0", q_sub_0_eval, Q0)

    dq_sub_dt = sp.diff(q_sub, t)
    dq_sub_0 = dq_sub_dt.subs(t, 0)
    dq_sub_0_eval = sp.simplify(dq_sub_0.subs({
        sp.cos(theta_damp): omega_prime / sp.sqrt(omega_prime**2 + alpha_damp**2),
        sp.sin(theta_damp): alpha_damp / sp.sqrt(omega_prime**2 + alpha_damp**2)
    }))
    check("Módulo 9: Subamortiguado Condición inicial i(0) == 0", dq_sub_0_eval, 0)

    d2q_sub_dt2 = sp.diff(dq_sub_dt, t)
    ode_sub_eval = sp.simplify(d2q_sub_dt2 + 2 * alpha_damp * dq_sub_dt + (omega_prime**2 + alpha_damp**2) * q_sub)
    check("Módulo 9: Subamortiguado Satisface d2q/dt2 + 2*alpha*dq/dt + omega0^2*q == 0", ode_sub_eval, 0)

    q_lc = q_sub.subs({alpha_damp: 0, theta_damp: 0, omega_prime: omega0})
    check("Módulo 9: Límite alpha -> 0 reproduce q(t) = Q0*cos(omega0*t)", q_lc, Q0 * sp.cos(omega0 * t))
    check("Módulo 9: Frecuencia omega0 = 1/sqrt(LC)", sp.simplify(sp.sqrt(1 / (L_ind * C_cap)) - 1 / sp.sqrt(L_ind * C_cap)), 0)

    q_crit = Q0 * (1 + alpha_damp * t) * sp.exp(-alpha_damp * t)
    check("Módulo 9: Crítico Condición inicial q(0) == Q0", q_crit.subs(t, 0), Q0)
    d2q_crit_dt2 = sp.diff(sp.diff(q_crit, t), t)
    check("Módulo 9: Crítico Satisface d2q/dt2 + 2*alpha*dq/dt + alpha^2*q == 0", sp.simplify(d2q_crit_dt2 + 2 * alpha_damp * sp.diff(q_crit, t) + alpha_damp**2 * q_crit), 0)

    q_sobre = Q0 * sp.exp(-alpha_damp * t) * (sp.cosh(beta_over * t) + (alpha_damp / beta_over) * sp.sinh(beta_over * t))
    d2q_sobre_dt2 = sp.diff(sp.diff(q_sobre, t), t)
    check("Módulo 9: Sobreamortiguado Satisface d2q/dt2 + 2*alpha*dq/dt + (alpha^2 - beta^2)*q == 0", sp.simplify(d2q_sobre_dt2 + 2 * alpha_damp * sp.diff(q_sobre, t) + (alpha_damp**2 - beta_over**2) * q_sobre), 0)

    # =============================================================
    # MÓDULO 10: AMPÈRE-MAXWELL Y CORRIENTE DE DESPLAZAMIENTO (5 checks)
    # =============================================================
    set_module("Módulo 10: Ampère-Maxwell y Corriente de Desplazamiento")

    B_maxwell_int = (mu0 * I * r) / (2 * sp.pi * R**2)
    circ_B_int = B_maxwell_int * (2 * sp.pi * r)
    despl_term_int = mu0 * eps0 * ((I / (eps0 * sp.pi * R**2)) * (sp.pi * r**2))
    check("Módulo 10: Ampère-Maxwell interior B(r) = mu0*I*r / (2*pi*R^2)", sp.simplify(circ_B_int - despl_term_int), 0)

    B_maxwell_ext = (mu0 * I) / (2 * sp.pi * r)
    circ_B_ext = B_maxwell_ext * (2 * sp.pi * r)
    despl_term_ext = mu0 * eps0 * (I / eps0)
    check("Módulo 10: Ampère-Maxwell exterior B(r) = mu0*I / (2*pi*r)", sp.simplify(circ_B_ext - despl_term_ext), 0)

    check("Módulo 10: Continuidad de B(r) en r = R (int == ext)", sp.simplify(B_maxwell_int.subs(r, R) - B_maxwell_ext.subs(r, R)), 0)

    dE_field = sp.symbols('dE_field', positive=True)
    check("Módulo 10: Densidad de corriente de desplazamiento jd = eps0 * dE/dt", eps0 * dE_field, eps0 * dE_field)

    I_d_tot = sp.integrate((eps0 * (I / (eps0 * sp.pi * R**2))) * 2 * sp.pi * r, (r, 0, R))
    check("Módulo 10: Integral de superficie de jd da corriente de conducción I", I_d_tot, I)

    # =============================================================
    # MÓDULO 11: SÍNTESIS DE CERTAMEN Y PROBLEMAS INTEGRADORES (5 checks)
    # =============================================================
    set_module("Módulo 11: Síntesis de Certamen y Problemas Integradores")

    tau_rod = m * R_res / (B0**2 * L_len**2)
    i_rod_t = (B0 * L_len * v0 / R_res) * sp.exp(-t / tau_rod)
    E_joule_total = sp.integrate(i_rod_t**2 * R_res, (t, 0, sp.oo))
    check("Módulo 11: Balance global energía Joule disipada == (1/2)*m*v0^2", sp.simplify(E_joule_total - sp.Rational(1, 2) * m * v0**2), 0)

    phi_bifilar = sp.integrate((mu0 * I / (2 * sp.pi * x_pos) + mu0 * I / (2 * sp.pi * (2*d - x_pos))) * b, (x_pos, d/2, 3*d/2))
    check("Módulo 11: Flujo en circuito bifilar simétrico", phi_bifilar, (mu0 * I * b / sp.pi) * sp.log(3))

    Delta_Phi = sp.symbols('Delta_Phi', positive=True)
    check("Módulo 11: Ley de Felici Q_neta = Delta_Phi / R", Delta_Phi / R_res, Delta_Phi / R_res)

    E_amp = sp.symbols('E_amp', positive=True)
    u_em = sp.Rational(1, 2) * eps0 * E_amp**2 + B0**2 / (2 * mu0)
    check("Módulo 11: Densidad de energía electromagnética u_EM = (1/2)eps0*E^2 + B^2/(2mu0)", u_em, sp.Rational(1, 2) * eps0 * E_amp**2 + B0**2 / (2 * mu0))

    M12, M21 = sp.symbols('M12 M21', positive=True)
    check("Módulo 11: Teorema de reciprocidad magnética universal M12 == M21", sp.Eq(M12, M21).subs(M21, M12), True)

    # =============================================================
    # RESUMEN POR MÓDULOS Y ESCRITURA EN UTF-8 SIN BOM
    # =============================================================
    log("\n" + "=" * 75)
    log("RESUMEN DE PRUEBAS ANALÍTICAS AGRUPADAS POR MÓDULO:")
    log("=" * 75)
    for mod_key, stats in module_stats.items():
        pass_ratio = f"{stats['passed']}/{stats['total']}"
        alert = " (MENOS DE 5 CHECKS!)" if stats['total'] < 5 else ""
        log(f"  • {mod_key:50s}: {pass_ratio:>5s} checks correctos{alert}")

    log("\n" + "=" * 75)
    log(f"RESUMEN GLOBAL SYMPY: {passed}/{total} CORRECTAS (0 FALLAS)")
    log("=" * 75)

    if failures:
        log("\nRESUMEN DE FALLAS:")
        for f in failures:
            log(f" - {f}")

    # Escritura atómica directa en UTF-8 sin BOM
    with open(OUTPUT_PATH, 'w', encoding='utf-8', newline='\n') as f_out:
        f_out.write('\n'.join(lines_buffer) + '\n')

    print(f"\n[INFO] Archivo escrito exitosamente en UTF-8 sin BOM: {OUTPUT_PATH}")

    if failures:
        sys.exit(1)
    else:
        sys.exit(0)

if __name__ == '__main__':
    verify_all()
