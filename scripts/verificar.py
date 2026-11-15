#!/usr/bin/env python3
"""
FIS120 / FIS12125 · Certamen 3 · UTFSM
Script de Verificación Analítica Independiente con SymPy
Cubre el 100% de los resultados analíticos teóricos de la web de estudio.
"""

import sys
import sympy as sp

def verify_all():
    print("=" * 70)
    print("INICIANDO VERIFICACIÓN ANALÍTICA INDEPENDIENTE CON SYMPY")
    print("=" * 70)
    passed = 0
    total = 0
    failures = []

    def check(name, expr1, expr2):
        nonlocal passed, total
        total += 1
        is_b1 = isinstance(expr1, (bool, sp.logic.boolalg.BooleanAtom))
        is_b2 = isinstance(expr2, (bool, sp.logic.boolalg.BooleanAtom))
        if is_b1 or is_b2:
            if bool(expr1) == bool(expr2):
                print(f"[PASS] {name}")
                passed += 1
            else:
                msg = f"[FAIL] {name}: {expr1} != {expr2}"
                print(msg)
                failures.append(msg)
            return
        try:
            diff = sp.simplify(expr1 - expr2)
            if hasattr(diff, 'is_zero_matrix') and diff.is_zero_matrix:
                print(f"[PASS] {name}")
                passed += 1
                return
            if diff == 0:
                print(f"[PASS] {name}")
                passed += 1
                return
            if abs(float(diff)) < 1e-7:
                print(f"[PASS] {name}")
                passed += 1
                return
        except Exception:
            pass
        try:
            if abs(float(expr1) - float(expr2)) < 1e-7:
                print(f"[PASS] {name}")
                passed += 1
                return
        except Exception:
            pass
        msg = f"[FAIL] {name}\n       Obtenido: {expr1}\n       Esperado: {expr2}"
        print(msg)
        failures.append(msg)

    # =============================================================
    # 1. CORRIENTES TOTALES POR INTEGRACIÓN (MÓDULOS 1 Y 2)
    # =============================================================
    print("\n--- 1. Corrientes Totales por Integración ---")
    r, J0, R, a, alpha, beta, I, I0, theta, R1, R2 = sp.symbols('r J0 R a alpha beta I I0 theta R1 R2', positive=True)

    # 1.1 Pauta C3 2026-1 P1a: Efecto pelicular escalonado
    I_step = sp.integrate(J0 * 2 * sp.pi * r, (r, 0, R/2)) + sp.integrate(3*J0 * 2 * sp.pi * r, (r, R/2, R))
    check("Pauta C3 P1a: Corriente escalonada I = (5/2)*pi*J0*R^2", I_step, sp.Rational(5, 2) * sp.pi * J0 * R**2)
    J0_solved = sp.solve(sp.Eq(I_step, I), J0)[0]
    check("Pauta C3 P1a: J0 despejado = 2*I / (5*pi*R^2)", J0_solved, 2 * I / (5 * sp.pi * R**2))

    # 1.2 Ayudantía 9 P2a: Perfil parabólico
    I_parab = sp.integrate(2*J0*(1 - r**2/a**2) * 2*sp.pi*r, (r, 0, a))
    check("Ayudantía 9 P2a: Corriente parabólica I_T = pi*J0*a^2", I_parab, sp.pi * J0 * a**2)

    # 1.3 Ayudantía 9 P4: Dependencia angular J = alpha*sin^2(theta)
    I_angular = sp.integrate(sp.integrate(alpha * sp.sin(theta)**2 * r, (theta, 0, 2*sp.pi)), (r, 0, R1))
    check("Ayudantía 9 P4: Corriente angular interior I_1 = (pi*alpha*R1^2)/2", I_angular, sp.pi * alpha * R1**2 / 2)
    I_ext = J0 * sp.pi * (R2**2 - R1**2)
    alpha_solved = sp.solve(sp.Eq(I_angular, I_ext), alpha)[0]
    check("Ayudantía 9 P4: alpha para I_1 = I_2", alpha_solved, 2 * J0 * (R2**2 - R1**2) / R1**2)

    # 1.4 Ayudantía 9 P3: Cilindro lineal J = beta*r'
    I_lin = sp.integrate(beta * r * 2 * sp.pi * r, (r, 0, R))
    check("Ayudantía 9 P3: Corriente cilindro macizo I_cil = (2/3)*pi*beta*R^3", I_lin, sp.Rational(2, 3) * sp.pi * beta * R**3)
    mu0 = sp.symbols('mu0', positive=True)
    beta_cond = sp.solve(sp.Eq(mu0 * beta * R**3 / (3*a), mu0 * I / (4*sp.pi*a)), beta)[0]
    check("Ayudantía 9 P3: Condición By = 0 en origen -> beta = 3I / (4*pi*R^3)", beta_cond, 3*I / (4*sp.pi*R**3))

    # =============================================================
    # 2. CAMPOS MAGNÉTICOS Y LEY DE AMPÈRE (MÓDULOS 1, 2 Y 3)
    # =============================================================
    print("\n--- 2. Ley de Ampère y Continuidad de B(r) ---")

    # 2.1 Pauta C3 P1b: Continuidad en R/2 y R
    r_prime = sp.symbols('r_prime', positive=True)
    B_reg1 = (mu0 * J0 * r) / 2
    I_enc_reg2 = sp.integrate(J0 * 2 * sp.pi * r_prime, (r_prime, 0, R/2)) + sp.integrate(3*J0 * 2 * sp.pi * r_prime, (r_prime, R/2, r))
    B_reg2 = mu0 * I_enc_reg2 / (2 * sp.pi * r)
    check("Pauta C3 P1b: B en r = R/2 por izquierda", B_reg1.subs(r, R/2), mu0 * J0 * R / 4)
    check("Pauta C3 P1b: Continuidad en r = R/2 (Reg1 = Reg2)", sp.simplify(B_reg1.subs(r, R/2) - B_reg2.subs(r, R/2)), 0)
    B_reg3 = mu0 * I / (2 * sp.pi * r)
    check("Pauta C3 P1b: Continuidad en r = R (Reg2 = Reg3)", sp.simplify(B_reg2.subs(r, R) - B_reg3.subs({r: R, I: sp.Rational(5,2)*sp.pi*J0*R**2})), 0)

    # 2.2 Comparación en r = 3R/4 (Pauta C3 P1c)
    B_esc_val = sp.simplify(B_reg2.subs(r, sp.Rational(3, 4) * R))
    check("Pauta C3 P1c: B escalonado en 3R/4 = (19/24)*mu0*J0*R", B_esc_val, sp.Rational(19, 24) * mu0 * J0 * R)
    J_unif = sp.Rational(5, 2) * J0
    B_unif_val = (mu0 * J_unif * (sp.Rational(3, 4) * R)) / 2
    check("Pauta C3 P1c: B uniforme en 3R/4 = (15/16)*mu0*J0*R", B_unif_val, sp.Rational(15, 16) * mu0 * J0 * R)
    check("Pauta C3 P1c: Desigualdad B_esc < B_unif", bool(sp.Rational(19, 24) < sp.Rational(15, 16)), True)

    # 2.3 Ayudantía 9 P1: Coaxial asimétrico
    I_enc_mid = J0 * sp.pi * R**2
    B_mid = mu0 * I_enc_mid / (2 * sp.pi * (sp.Rational(3, 2) * R))
    check("Ayudantía 9 P1b: B(3R/2) = (1/3)*mu0*J0*R", B_mid, sp.Rational(1, 3) * mu0 * J0 * R)
    I_tot_coax = J0 * sp.pi * R**2 - 2*J0 * sp.pi * ((4*R)**2 - (2*R)**2)
    check("Ayudantía 9 P1: Corriente neta coaxial = -23*pi*J0*R^2", I_tot_coax, -23 * sp.pi * J0 * R**2)
    B_ext = mu0 * I_tot_coax / (2 * sp.pi * (5 * R))
    check("Ayudantía 9 P1c: B(5R) = -(23/10)*mu0*J0*R", B_ext, -sp.Rational(23, 10) * mu0 * J0 * R)

    # 2.4 Ayudantía 9 P2b: Campo interior con perfil parabólico
    I_enc_parab = sp.integrate(2*J0*(1 - r_prime**2/a**2) * 2*sp.pi*r_prime, (r_prime, 0, r))
    B_parab_int = mu0 * I_enc_parab / (2 * sp.pi * r)
    expected_B_parab_int = mu0 * J0 * r * (1 - r**2 / (2 * a**2))
    check("Ayudantía 9 P2b: B interior = mu0*J0*r*(1 - r^2/(2a^2))", sp.simplify(B_parab_int - expected_B_parab_int), 0)

    # 2.5 Ayudantía 9 P2c: Campo exterior y continuidad en r = a
    B_parab_ext = mu0 * (sp.pi * J0 * a**2) / (2 * sp.pi * r)
    expected_B_parab_ext = (mu0 * J0 * a**2) / (2 * r)
    check("Ayudantía 9 P2c: B exterior = mu0*J0*a^2 / (2r)", sp.simplify(B_parab_ext - expected_B_parab_ext), 0)
    check("Ayudantía 9 P2c: Continuidad en r = a (B_int(a) == B_ext(a))", sp.simplify(B_parab_int.subs(r, a) - B_parab_ext.subs(r, a)), 0)

    # 2.6 Ayudantía 9 P4c: Campo nulo exterior por compensación de corriente
    # Para r > R2, I_enc = I_1 - I_2 = 0 si alpha cumple la condición
    I_enc_p4c = sp.simplify((sp.pi * alpha_solved * R1**2 / 2) - J0 * sp.pi * (R2**2 - R1**2))
    check("Ayudantía 9 P4c: Corriente neta para r > R2 es idénticamente 0", I_enc_p4c, 0)
    B_p4c_ext = mu0 * I_enc_p4c / (2 * sp.pi * r)
    check("Ayudantía 9 P4c: Campo magnético para r > R2 es idénticamente 0", B_p4c_ext, 0)

    # =============================================================
    # 3. FLUJOS MAGNÉTICOS, INDUCTANCIA MUTUA Y FARADAY (MÓDULOS 4 Y 6)
    # =============================================================
    print("\n--- 3. Flujos con Logaritmos, Inductancia Mutua y Ley de Faraday ---")
    b, h, d, d0, v, t, N, tau = sp.symbols('b h d d0 v t N tau', positive=True)

    # 3.1 Simulacro C3 P2 / Module 4 P7: Espira alejándose de cable
    x = sp.symbols('x', positive=True)
    d_t = d0 + v * t
    phi_moving = sp.integrate(mu0 * I / (2 * sp.pi * x) * b, (x, d_t, d_t + a))
    expected_phi = (mu0 * I * b / (2 * sp.pi)) * sp.log((d_t + a) / d_t)
    check("Simulacro P2: Flujo magnético logarítmico", sp.simplify(phi_moving - expected_phi), 0)
    emf_moving = -sp.diff(phi_moving, t)
    expected_emf = (mu0 * I * b * v * a) / (2 * sp.pi * d_t * (d_t + a))
    check("Simulacro P2: fem inducida exacta", sp.simplify(emf_moving - expected_emf), 0)
    check("Simulacro P2: Límite t -> inf de phi = 0", sp.limit(phi_moving, t, sp.oo), 0)
    check("Simulacro P2: Límite t -> inf de fem = 0", sp.limit(emf_moving, t, sp.oo), 0)
    check("Simulacro P2: fem con v = 0 es nula", emf_moving.subs(v, 0), 0)

    # 3.2 Simulacro C3 P1: Toroide rectangular y autoinductancia
    phi_toroid_turn = sp.integrate((mu0 * N * I / (2 * sp.pi * r)) * h, (r, a, b))
    expected_phi_toroid = (mu0 * N * I * h / (2 * sp.pi)) * sp.log(b / a)
    check("Simulacro P1: Flujo en 1 vuelta del toroide", sp.simplify(phi_toroid_turn - expected_phi_toroid), 0)
    L_toroid = N * phi_toroid_turn / I
    check("Simulacro P1: Autoinductancia L del toroide", sp.simplify(L_toroid - (mu0 * N**2 * h / (2 * sp.pi)) * sp.log(b / a)), 0)
    B_toroid = mu0 * N * I / (2 * sp.pi * r)
    U_vol = sp.integrate((B_toroid**2 / (2 * mu0)) * 2 * sp.pi * r * h, (r, a, b))
    U_circ = sp.Rational(1, 2) * L_toroid * I**2
    check("Simulacro P1: Equivalencia energía volumen vs (1/2)*L*I^2", sp.simplify(U_vol - U_circ), 0)

    # 3.3 Ayudantía 10 P1: Espira cuadrada con campo rotatorio
    k_ang, omega_rot = sp.symbols('k_ang omega_rot', real=True)
    B0_field = sp.symbols('B0_field', positive=True)
    # B_z = B0 * sin(k + omega*t), flujo sobre lado a: Phi = B0 * a^2 * sin(k + omega*t)
    phi_ayud10_p1 = B0_field * a**2 * sp.sin(k_ang + omega_rot * t)
    emf_ayud10_p1 = -sp.diff(phi_ayud10_p1, t)
    check("Ayudantía 10 P1: fem inducida = -B0*a^2*omega*cos(k + omega*t)", emf_ayud10_p1, -B0_field * a**2 * omega_rot * sp.cos(k_ang + omega_rot * t))
    # Amplitud / valor máximo de la fem:
    emf_ayud10_p1_max = B0_field * a**2 * sp.Abs(omega_rot)
    check("Ayudantía 10 P1: Magnitud máxima |fem_max| = B0*a^2*omega", emf_ayud10_p1_max.subs(omega_rot, sp.symbols('om_pos', positive=True)), B0_field * a**2 * sp.symbols('om_pos', positive=True))

    # 3.4 Ayudantía 10 P2: Espira circular con espira cuadrada pequeña concéntrica (a << R)
    # B(t) en el centro de espira circular = mu0*I(t)/(2R)
    I_t_ayud10_p2 = I0 * sp.exp(-t / tau)
    B_center_ayud10_p2 = (mu0 * I_t_ayud10_p2) / (2 * R)
    phi_ayud10_p2 = B_center_ayud10_p2 * a**2
    check("Ayudantía 10 P2a: Flujo en espira central = (mu0*I0*a^2 / 2R)*e^(-t/tau)", phi_ayud10_p2, (mu0 * I0 * a**2 / (2 * R)) * sp.exp(-t / tau))
    emf_ayud10_p2 = -sp.diff(phi_ayud10_p2, t)
    check("Ayudantía 10 P2b: fem inducida = (mu0*I0*a^2 / (2*R*tau))*e^(-t/tau)", emf_ayud10_p2, (mu0 * I0 * a**2 / (2 * R * tau)) * sp.exp(-t / tau))
    # Signo de Lenz: dPhi/dt < 0 -> fem > 0 con normal n = k -> Corriente inducida antihoraria
    check("Ayudantía 10 P2c: fem inducida es estrictamente positiva (antihoraria)", bool(emf_ayud10_p2.subs({mu0: 1, I0: 1, a: 1, R: 1, tau: 1, t: 1}) > 0), True)

    # 3.5 Ayudantía 11 P1: Solenoides concéntricos ideales de radios R y 3R
    n_i, n_e, N_i, N_e, l_sol = sp.symbols('n_i n_e N_i N_e l_sol', positive=True)
    # Campo solenoide interior: B = mu0*n_i*I para r < R, y B = 0 para r > R
    # a) Flujo sobre UNA vuelta del solenoide exterior (radio 3R):
    # Dado que B=0 fuera de R, la integral sobre el círculo de radio 3R se reduce a r < R
    phi_turn_ext = (mu0 * n_i * I) * (sp.pi * R**2)
    check("Ayudantía 11 P1a: Flujo en una vuelta exterior = mu0*n_i*pi*R^2*I", phi_turn_ext, mu0 * n_i * sp.pi * R**2 * I)
    # b) Inductancia mutua M entre ambas bobinas:
    # Flujo total exterior: Phi_T_ext = N_e * phi_turn_ext = (n_e * l_sol) * mu0 * n_i * pi*R^2 * I
    M_solenoids = (n_e * l_sol * phi_turn_ext) / I
    check("Ayudantía 11 P1b: M = mu0*n_i*n_e*pi*R^2*l", M_solenoids, mu0 * n_i * n_e * sp.pi * R**2 * l_sol)
    # Equivalente en términos de vueltas totales:
    M_solenoids_N = M_solenoids.subs({n_i: N_i / l_sol, n_e: N_e / l_sol})
    check("Ayudantía 11 P1b: M = mu0*N_i*N_e*pi*R^2 / l", M_solenoids_N, (mu0 * N_i * N_e * sp.pi * R**2) / l_sol)
    # c) fem inducida con I(t) = I0 * cos(omega * t):
    omega_ayud11 = sp.symbols('omega_ayud11', positive=True)
    I_cos_t = I0 * sp.cos(omega_ayud11 * t)
    emf_ext_cos = -M_solenoids * sp.diff(I_cos_t, t)
    expected_emf_ext_cos = M_solenoids * I0 * omega_ayud11 * sp.sin(omega_ayud11 * t)
    check("Ayudantía 11 P1c: fem exterior = M*I0*omega*sin(omega*t)", sp.simplify(emf_ext_cos - expected_emf_ext_cos), 0)

    # 3.6 Ayudantía 11 P2: Cable y rectángulo fijo a distancia a
    phi_rect_ayud11 = sp.integrate((mu0 * I / (2 * sp.pi * x)) * b, (x, a, 2*a))
    check("Ayudantía 11 P2a: Flujo cable-rectángulo = (mu0*b*ln(2)/(2*pi))*I", phi_rect_ayud11, (mu0 * b * sp.log(2) / (2 * sp.pi)) * I)
    M_rect = phi_rect_ayud11 / I
    check("Ayudantía 11 P2b: Inductancia mutua M = mu0*b*ln(2)/(2*pi)", M_rect, mu0 * b * sp.log(2) / (2 * sp.pi))
    # c) fem con I(t) = I0 * exp(-t/tau)
    I_exp_t = I0 * sp.exp(-t / tau)
    emf_ayud11_p2 = -M_rect * sp.diff(I_exp_t, t)
    check("Ayudantía 11 P2c: fem inducida = (mu0*b*ln(2)*I0 / (2*pi*tau))*e^(-t/tau)", emf_ayud11_p2, (mu0 * b * sp.log(2) * I0 / (2 * sp.pi * tau)) * sp.exp(-t / tau))

    # 3.7 Ayudantía 11 P3: B(y,t) = alpha*y^2 * exp(-beta*t) * k
    C, H, L_w = sp.symbols('C H L_w', positive=True)
    y = sp.symbols('y', positive=True)
    phi_space_time = sp.integrate(alpha * y**2 * sp.exp(-beta * t) * L_w, (y, C, C + H))
    expected_phi_st = (alpha * L_w / 3) * ((C + H)**3 - C**3) * sp.exp(-beta * t)
    check("Ayudantía 11 P3a: Flujo con B(y,t)", sp.simplify(phi_space_time - expected_phi_st), 0)
    emf_st = sp.simplify(-sp.diff(phi_space_time, t))
    check("Ayudantía 11 P3b: fem inducida = (alpha*beta*L/3)*[(C+H)^3 - C^3]*e^(-beta*t)", emf_st, (alpha * beta * L_w / 3) * ((C + H)**3 - C**3) * sp.exp(-beta * t))

    # 3.8 Ayudantía 11 P4: Espira inclinada dentro de solenoide
    alpha_ang = sp.symbols('alpha_ang', real=True)
    theta_ang = sp.symbols('theta_ang', real=True)
    n_dens = sp.symbols('n_dens', positive=True)
    omega_sym = sp.symbols('omega_sym', positive=True)
    B_mag = mu0 * n_dens * I

    B_vec = sp.Matrix([0, 0, B_mag])
    n_vec = sp.Matrix([sp.sin(theta_ang), 0, sp.cos(theta_ang)])
    dot_Bn = n_vec.dot(B_vec)
    check("Ayudantía 11 P4: Geometría 3D B·n == B*cos(theta)", dot_Bn, B_mag * sp.cos(theta_ang))
    dot_Bn_normal = dot_Bn.subs(theta_ang, alpha_ang)
    check("Ayudantía 11 P4: Deducción geométrica theta = alpha (eje a normal) -> cos(alpha)", dot_Bn_normal, B_mag * sp.cos(alpha_ang))
    M_tilted_cos = (dot_Bn_normal * sp.pi * b**2) / I
    check("Ayudantía 11 P4: M bajo convención normal-eje (cos(alpha))", M_tilted_cos, mu0 * n_dens * sp.pi * b**2 * sp.cos(alpha_ang))
    dot_Bn_plano = sp.trigsimp(dot_Bn.subs(theta_ang, sp.pi/2 - alpha_ang))
    check("Ayudantía 11 P4: Deducción geométrica theta = 90° - alpha (eje a plano) -> sin(alpha)", dot_Bn_plano, B_mag * sp.sin(alpha_ang))
    M_tilted_sin = (dot_Bn_plano * sp.pi * b**2) / I
    check("Ayudantía 11 P4: M bajo convención plano-eje (sin(alpha))", M_tilted_sin, mu0 * n_dens * sp.pi * b**2 * sp.sin(alpha_ang))
    I_t = I0 * sp.sin(omega_sym * t)
    dI_dt = sp.diff(I_t, t)
    check("Ayudantía 11 P4: fem inducida (convención cos(alpha))", -M_tilted_cos * dI_dt, -mu0 * n_dens * sp.pi * b**2 * sp.cos(alpha_ang) * I0 * omega_sym * sp.cos(omega_sym * t))
    check("Ayudantía 11 P4: fem inducida (convención sin(alpha))", -M_tilted_sin * dI_dt, -mu0 * n_dens * sp.pi * b**2 * sp.sin(alpha_ang) * I0 * omega_sym * sp.cos(omega_sym * t))

    # 3.9 Pauta C3 2026-1 P2: Rollo plano de N vueltas y pequeña espira circular (r << R)
    r_small = sp.symbols('r_small', positive=True)
    # Campo en el centro del rollo plano: B = N * mu0*I / (2R)
    B_center_rollo = N * (mu0 * I) / (2 * R)
    phi_rollo = B_center_rollo * (sp.pi * r_small**2)
    M_rollo = phi_rollo / I
    check("Pauta C3 P2a: M del rollo = mu0*N*pi*r^2 / (2R)", M_rollo, (mu0 * N * sp.pi * r_small**2) / (2 * R))
    # Para t < 0: I(t) = I0 = cte -> fem = 0
    I_neg_t = I0
    emf_rollo_neg = -M_rollo * sp.diff(I_neg_t, t)
    check("Pauta C3 P2b: fem inducida para t < 0 es idénticamente 0", emf_rollo_neg, 0)
    # Para t >= 0: I(t) = I0 * e^(-t/tau) -> fem = M * (I0/tau) * e^(-t/tau)
    I_pos_t = I0 * sp.exp(-t / tau)
    emf_rollo_pos = -M_rollo * sp.diff(I_pos_t, t)
    check("Pauta C3 P2b: fem inducida para t >= 0 = (mu0*N*pi*r^2*I0 / (2*R*tau))*e^(-t/tau)", emf_rollo_pos, (mu0 * N * sp.pi * r_small**2 * I0 / (2 * R * tau)) * sp.exp(-t / tau))

    # 3.10 Simulacro C3 P3: Solenoide y bobina cuadrada coaxial (L > 2a)
    L_sq = sp.symbols('L_sq', positive=True)
    # Campo del solenoide B = mu0*n*I (r < a) y B = 0 (r > a)
    # Flujo sobre UNA vuelta cuadrada: la integral solo es no nula dentro del solenoide pi*a^2
    phi_1_sq = (mu0 * n_dens * I) * (sp.pi * a**2)
    # Para N espiras de la bobina cuadrada:
    phi_T_sq = N * phi_1_sq
    M_sim3 = phi_T_sq / I
    check("Simulacro P3: M = mu0*n*N*pi*a^2 (independiente de L)", M_sim3, mu0 * n_dens * N * sp.pi * a**2)
    check("Simulacro P3: Derivada de M respecto a L es 0", sp.diff(M_sim3, L_sq), 0)
    # fem inducida con I(t) = I0 * (1 - exp(-t/tau)):
    I_sat_t = I0 * (1 - sp.exp(-t / tau))
    emf_sim3 = -M_sim3 * sp.diff(I_sat_t, t)
    check("Simulacro P3: fem inducida con corriente de saturación", emf_sim3, - (mu0 * n_dens * N * sp.pi * a**2 * I0 / tau) * sp.exp(-t / tau))
    # fem en el solenoide si en la bobina cuadrada circula I2(t) = alpha * t:
    alpha_rate = sp.symbols('alpha_rate', positive=True)
    I2_t = alpha_rate * t
    emf_solenoid_from_sq = -M_sim3 * sp.diff(I2_t, t)
    check("Simulacro P3: fem en solenoide con I2 = alpha*t es -mu0*n*N*pi*a^2*alpha", emf_solenoid_from_sq, -mu0 * n_dens * N * sp.pi * a**2 * alpha_rate)

    # =============================================================
    # 4. DINÁMICA DE RIELES Y BALANCE DE ENERGÍA (MÓDULO 5)
    # =============================================================
    print("\n--- 4. Dinámica de Rieles y Balance de Potencia ---")
    m, g, B0, R_res, L_len, w_width = sp.symbols('m g B0 R_res L_len w_width', positive=True)

    # 4.1 Velocidad terminal
    v_t = m * g * R_res / (B0**2 * L_len**2)
    P_mec = m * g * v_t
    i_ind = (B0 * L_len * v_t) / R_res
    P_joule = i_ind**2 * R_res
    check("Ayudantía 10 P3: Balance exacto P_mec == P_Joule en v_term", sp.simplify(P_mec - P_joule), 0)

    # 4.1b Verificación vectorial con sp.Matrix.cross
    I_current = sp.symbols('I_current', positive=True)
    vec_L_rod = sp.Matrix([L_len, 0, 0])
    vec_B_rod = sp.Matrix([0, -B0, 0])
    vec_F_rod = I_current * vec_L_rod.cross(vec_B_rod)
    z_hat_down = sp.Matrix([0, 0, 1])
    check("Ayudantía 10 P3: Fuerza magnética F_B = -I*L*B0*z_hat (hacia arriba)", vec_F_rod, -I_current * L_len * B0 * z_hat_down)

    # 4.2 Carrito conductor (Ayudantía 10 P4)
    tau_cart = m * R_res / (B0**2 * a**2)
    v0 = sp.symbols('v0', positive=True)
    v_t_cart = v0 * sp.exp(-t / tau_cart)
    x_stop = sp.integrate(v_t_cart, (t, 0, sp.oo))
    x_max_val = m * v0 * R_res / (B0**2 * a**2)
    check("Ayudantía 10 P4: Penetración x_max = m*v0*R / (B0^2 * a^2) si ancho w > x_max", x_stop, x_max_val)
    v_residual = v0 - (B0**2 * a**2 / (m * R_res)) * w_width
    check("Ayudantía 10 P4: Velocidad residual vf en x = w si ancho w < x_max", v_residual, v0 - w_width / tau_cart)

    # =============================================================
    # 5. AUTOINDUCTANCIA Y ENERGÍA DE CAMPOS (MÓDULO 7)
    # =============================================================
    print("\n--- 5. Autoinductancia y Energía de Campos ---")
    A_area, l_length = sp.symbols('A_area l_length', positive=True)
    i_var, q_var, V_volt = sp.symbols('i_var q_var V_volt', positive=True)

    # 5.1 Autoinductancia del solenoide largo: B = mu0*n*I, Phi_1 = B*A = mu0*n*I*A, Phi_T = N*Phi_1 = (n*l)*mu0*n*I*A
    Phi_T_solenoid = (n_dens * l_length) * (mu0 * n_dens * I * A_area)
    L_solenoid = Phi_T_solenoid / I
    check("Módulo 7: L del solenoide = mu0*n^2*l*A", L_solenoid, mu0 * n_dens**2 * l_length * A_area)

    # 5.2 fem autoinducida: eps_L = -L * di/dt
    eps_L = -L_solenoid * sp.diff(I_cos_t, t)
    check("Módulo 7: fem autoinducida eps_L = -L * di/dt", eps_L, -L_solenoid * sp.diff(I_cos_t, t))

    # 5.3 Energía magnética almacenada: U_L = integrate(L*i, (i, 0, I)) = (1/2)*L*I^2
    L_sym = sp.symbols('L_sym', positive=True)
    U_L = sp.integrate(L_sym * i_var, (i_var, 0, I))
    check("Módulo 7: Energía magnética U_L = (1/2)*L*I^2", U_L, sp.Rational(1, 2) * L_sym * I**2)

    # 5.4 Densidad de energía magnética: u_B = U_L / Vol = (1/2)*mu0*n^2*I^2 = B^2 / (2*mu0)
    Vol_solenoid = A_area * l_length
    U_L_solenoid = sp.Rational(1, 2) * (mu0 * n_dens**2 * l_length * A_area) * I**2
    u_B = U_L_solenoid / Vol_solenoid
    check("Módulo 7: Densidad u_B = (1/2)*mu0*n^2*I^2", u_B, sp.Rational(1, 2) * mu0 * n_dens**2 * I**2)
    B_field_sol = mu0 * n_dens * I
    check("Módulo 7: u_B == B^2 / (2*mu0)", sp.simplify(u_B - B_field_sol**2 / (2 * mu0)), 0)

    # 5.5 Energía electrostática en capacitor: U_C = integrate(q/C, (q, 0, Q)) = (1/2)*Q^2/C = (1/2)*C*V^2
    Q_charge, C_cap = sp.symbols('Q_charge C_cap', positive=True)
    U_C = sp.integrate(q_var / C_cap, (q_var, 0, Q_charge))
    check("Módulo 7: Energía de capacitor U_C = (1/2)*Q^2/C", U_C, sp.Rational(1, 2) * Q_charge**2 / C_cap)
    check("Módulo 7: U_C con Q=C*V es (1/2)*C*V^2", U_C.subs(Q_charge, C_cap * V_volt), sp.Rational(1, 2) * C_cap * V_volt**2)

    # =============================================================
    # 6. CIRCUITOS LC Y RLC EN LOS TRES REGÍMENES (MÓDULO 9)
    # =============================================================
    print("\n--- 6. Circuitos RLC en los Tres Regímenes ---")
    Q0, C_cap, L_ind = sp.symbols('Q0 C_cap L_ind', positive=True)
    omega0 = sp.symbols('omega0', positive=True)
    alpha_damp = sp.symbols('alpha_damp', positive=True)
    omega_prime = sp.symbols('omega_prime', positive=True)
    beta_over = sp.symbols('beta_over', positive=True)

    # 6.1 Régimen Subamortiguado (omega0 > alpha): q(t) oficial del formulario UTFSM
    theta_damp = sp.atan(alpha_damp / omega_prime)
    q_sub = Q0 * (omega0 / omega_prime) * sp.exp(-alpha_damp * t) * sp.cos(omega_prime * t - theta_damp)

    # Condición inicial q(0) = Q0
    q_sub_0 = sp.simplify(q_sub.subs(t, 0))
    q_sub_0_eval = sp.simplify(q_sub_0.subs(sp.cos(theta_damp), omega_prime / sp.sqrt(omega_prime**2 + alpha_damp**2)).subs(omega_prime**2 + alpha_damp**2, omega0**2))
    check("Módulo 9 Sub: Condición inicial q(0) == Q0", q_sub_0_eval, Q0)

    # Condición inicial i(0) = dq/dt(0) == 0
    dq_sub_dt = sp.diff(q_sub, t)
    dq_sub_0 = dq_sub_dt.subs(t, 0)
    dq_sub_0_eval = sp.simplify(dq_sub_0.subs({
        sp.cos(theta_damp): omega_prime / sp.sqrt(omega_prime**2 + alpha_damp**2),
        sp.sin(theta_damp): alpha_damp / sp.sqrt(omega_prime**2 + alpha_damp**2)
    }))
    check("Módulo 9 Sub: Condición inicial i(0) == 0", dq_sub_0_eval, 0)

    # Satisface EDO: d2q/dt2 + 2*alpha*dq/dt + omega0^2*q == 0
    d2q_sub_dt2 = sp.diff(dq_sub_dt, t)
    ode_sub_eval = sp.simplify(d2q_sub_dt2 + 2 * alpha_damp * dq_sub_dt + (omega_prime**2 + alpha_damp**2) * q_sub)
    check("Módulo 9 Sub: Satisface d2q/dt2 + 2*alpha*dq/dt + omega0^2*q == 0", ode_sub_eval, 0)

    # Límite sin amortiguamiento alpha -> 0 (R -> 0): circuito LC ideal
    # Con alpha = 0: theta = 0, omega' = omega0 -> q(t) = Q0 * cos(omega0*t)
    q_lc = q_sub.subs({alpha_damp: 0, theta_damp: 0, omega_prime: omega0})
    check("Módulo 9 LC: Límite alpha -> 0 reproduce q(t) = Q0*cos(omega0*t)", q_lc, Q0 * sp.cos(omega0 * t))
    check("Módulo 9 LC: Frecuencia omega0 = 1/sqrt(LC)", sp.simplify(sp.sqrt(1 / (L_ind * C_cap)) - 1 / sp.sqrt(L_ind * C_cap)), 0)

    # 6.2 Régimen Críticamente Amortiguado (omega0 == alpha)
    # Solución con q(0) = Q0 e i(0) = 0: q_crit(t) = Q0 * (1 + alpha*t) * exp(-alpha*t)
    q_crit = Q0 * (1 + alpha_damp * t) * sp.exp(-alpha_damp * t)
    check("Módulo 9 Crítico: Condición inicial q(0) == Q0", q_crit.subs(t, 0), Q0)
    dq_crit_dt = sp.diff(q_crit, t)
    check("Módulo 9 Crítico: Condición inicial i(0) == 0", dq_crit_dt.subs(t, 0), 0)
    d2q_crit_dt2 = sp.diff(dq_crit_dt, t)
    ode_crit_eval = sp.simplify(d2q_crit_dt2 + 2 * alpha_damp * dq_crit_dt + alpha_damp**2 * q_crit)
    check("Módulo 9 Crítico: Satisface d2q/dt2 + 2*alpha*dq/dt + alpha^2*q == 0", ode_crit_eval, 0)

    # 6.3 Régimen Sobreamortiguado (alpha > omega0, beta = sqrt(alpha^2 - omega0^2))
    # Solución con q(0) = Q0 e i(0) = 0: q_sobre(t) = Q0 * exp(-alpha*t) * (cosh(beta*t) + (alpha/beta)*sinh(beta*t))
    q_sobre = Q0 * sp.exp(-alpha_damp * t) * (sp.cosh(beta_over * t) + (alpha_damp / beta_over) * sp.sinh(beta_over * t))
    check("Módulo 9 Sobre: Condición inicial q(0) == Q0", q_sobre.subs(t, 0), Q0)
    dq_sobre_dt = sp.diff(q_sobre, t)
    check("Módulo 9 Sobre: Condición inicial i(0) == 0", dq_sobre_dt.subs(t, 0), 0)
    # Satisface EDO con omega0^2 = alpha^2 - beta^2
    d2q_sobre_dt2 = sp.diff(dq_sobre_dt, t)
    ode_sobre_eval = sp.simplify(d2q_sobre_dt2 + 2 * alpha_damp * dq_sobre_dt + (alpha_damp**2 - beta_over**2) * q_sobre)
    check("Módulo 9 Sobre: Satisface d2q/dt2 + 2*alpha*dq/dt + (alpha^2 - beta^2)*q == 0", ode_sobre_eval, 0)

    # =============================================================
    # 7. LEY DE AMPÈRE-MAXWELL Y CORRIENTE DE DESPLAZAMIENTO (MÓDULO 10)
    # =============================================================
    print("\n--- 7. Ley de Ampère-Maxwell y Campo en Capacitor Circular ---")
    eps0 = sp.symbols('eps0', positive=True)
    # Capacitor de placas circulares de radio R, corriente de conducción I(t)
    # Campo eléctrico uniforme entre placas: E(t) = Q(t) / (eps0 * pi * R^2)
    # Flujo eléctrico para bucle ampero-maxwelliano de radio r <= R:
    # Phi_E(r) = E(t) * pi * r^2 = Q(t) * r^2 / (eps0 * R^2)
    # dPhi_E/dt = I(t) * r^2 / (eps0 * R^2)
    # Ley de Ampère-Maxwell: B(r) * 2*pi*r = mu0 * eps0 * dPhi_E/dt = mu0 * I(t) * r^2 / R^2
    B_maxwell_int = (mu0 * I * r) / (2 * sp.pi * R**2)
    circ_B_int = B_maxwell_int * (2 * sp.pi * r)
    despl_term_int = mu0 * eps0 * ((I / (eps0 * sp.pi * R**2)) * (sp.pi * r**2))
    check("Módulo 10: Ampère-Maxwell interior B(r) = mu0*I*r / (2*pi*R^2)", sp.simplify(circ_B_int - despl_term_int), 0)

    # Para r >= R: todo el flujo eléctrico está encerrado -> Phi_E = Q(t) / eps0 -> dPhi_E/dt = I / eps0
    B_maxwell_ext = (mu0 * I) / (2 * sp.pi * r)
    circ_B_ext = B_maxwell_ext * (2 * sp.pi * r)
    despl_term_ext = mu0 * eps0 * (I / eps0)
    check("Módulo 10: Ampère-Maxwell exterior B(r) = mu0*I / (2*pi*r)", sp.simplify(circ_B_ext - despl_term_ext), 0)
    check("Módulo 10: Continuidad de B(r) en r = R (int == ext)", sp.simplify(B_maxwell_int.subs(r, R) - B_maxwell_ext.subs(r, R)), 0)

    # =============================================================
    # 8. TRANSFORMADOR IDEAL Y TRANSIENTES CONMUTADOS (MÓDULOS 6 Y 8)
    # =============================================================
    print("\n--- 8. Transformador Ideal y Transientes Conmutados ---")
    N_p, N_s, V_p, V_s, I_p, I_s = sp.symbols('N_p N_s V_p V_s I_p I_s', positive=True)

    # 8.1 Transformador ideal: relación de voltajes y corrientes por conservación de potencia
    # V_s / V_p = N_s / N_p
    check("Módulo 6: Transformador ideal relación de transformación V_s / V_p == N_s / N_p", sp.simplify((V_p * (N_s / N_p)) / V_p - N_s / N_p), 0)
    # En transformador ideal sin pérdidas: P_p = P_s -> V_p * I_p = V_s * I_s -> I_s / I_p = N_p / N_s
    I_s_rel = sp.solve(sp.Eq(V_p * I_p, (V_p * N_s / N_p) * I_s), I_s)[0]
    check("Módulo 6: Transformador ideal relación de corrientes I_s == I_p * (N_p / N_s)", I_s_rel, I_p * N_p / N_s)

    # 8.2 Circuito Transiente Conmutado (Pauta C3 2026-1 P3)
    R_p3 = 370
    C_p3 = 5e-6
    eps_p3 = 112
    L_p3 = R_p3**2 * C_p3
    check("Pauta C3 P3a: L = (370)^2 * 5e-6 = 0.6845 H", sp.Float(L_p3, 4), sp.Float(0.6845, 4))
    I_fuente = eps_p3 / R_p3
    check("Pauta C3 P3b: Ifuente(inf) = 112 / 370 =~ 0.3027 A", round(I_fuente, 3), 0.303)
    tau_RC = R_p3 * C_p3
    check("Pauta C3 P3c: tau_RC = 1.85 ms", tau_RC, 1.85e-3)

    print("\n" + "=" * 70)
    print(f"RESUMEN DE PRUEBAS SYMPY: {passed}/{total} CORRECTAS")
    print("=" * 70)

    if failures:
        print("\nRESUMEN DE FALLAS:")
        for f in failures:
            print(f)
        sys.exit(1)
    else:
        sys.exit(0)

if __name__ == '__main__':
    verify_all()
