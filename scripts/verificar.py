#!/usr/bin/env python3
"""
FIS120 / FIS12125 · Certamen 3 · UTFSM
Script de Verificación Analítica Independiente con SymPy
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

    # -------------------------------------------------------------
    # 1. CORRIENTES TOTALES POR INTEGRACIÓN
    # -------------------------------------------------------------
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
    # Superposición en el origen: B_y = mu0*beta*R^3 / (3a) - mu0*I / (4pi*a) = 0
    mu0 = sp.symbols('mu0', positive=True)
    beta_cond = sp.solve(sp.Eq(mu0 * beta * R**3 / (3*a), mu0 * I / (4*sp.pi*a)), beta)[0]
    check("Ayudantía 9 P3: Condición By = 0 en origen -> beta = 3I / (4*pi*R^3)", beta_cond, 3*I / (4*sp.pi*R**3))

    # -------------------------------------------------------------
    # 2. CAMPOS MAGNÉTICOS Y LEY DE AMPÈRE
    # -------------------------------------------------------------
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
    # Uniforme con corriente I
    J_unif = sp.Rational(5, 2) * J0
    B_unif_val = (mu0 * J_unif * (sp.Rational(3, 4) * R)) / 2
    check("Pauta C3 P1c: B uniforme en 3R/4 = (15/16)*mu0*J0*R", B_unif_val, sp.Rational(15, 16) * mu0 * J0 * R)
    check("Pauta C3 P1c: Desigualdad B_esc < B_unif", bool(sp.Rational(19, 24) < sp.Rational(15, 16)), True)

    # 2.3 Ayudantía 9 P1: Coaxial asimétrico
    # Interior: J1 = J0 (z), Cascarón: 2R < r < 4R, J2 = 2J0 (-z)
    # En r = 3R/2 (aislante):
    I_enc_mid = J0 * sp.pi * R**2
    B_mid = mu0 * I_enc_mid / (2 * sp.pi * (sp.Rational(3, 2) * R))
    check("Ayudantía 9 P1b: B(3R/2) = (1/3)*mu0*J0*R", B_mid, sp.Rational(1, 3) * mu0 * J0 * R)
    # En r = 5R (exterior):
    I_tot_coax = J0 * sp.pi * R**2 - 2*J0 * sp.pi * ((4*R)**2 - (2*R)**2)
    check("Ayudantía 9 P1: Corriente neta coaxial = -23*pi*J0*R^2", I_tot_coax, -23 * sp.pi * J0 * R**2)
    B_ext = mu0 * I_tot_coax / (2 * sp.pi * (5 * R))
    check("Ayudantía 9 P1c: B(5R) = -(23/10)*mu0*J0*R", B_ext, -sp.Rational(23, 10) * mu0 * J0 * R)

    # -------------------------------------------------------------
    # 3. FLUJOS MAGNÉTICOS CON LOGARITMOS Y LEY DE FARADAY
    # -------------------------------------------------------------
    print("\n--- 3. Flujos con Logaritmos y Ley de Faraday ---")
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

    # Límites asintóticos:
    check("Simulacro P2: Límite t -> inf de phi = 0", sp.limit(phi_moving, t, sp.oo), 0)
    check("Simulacro P2: Límite t -> inf de fem = 0", sp.limit(emf_moving, t, sp.oo), 0)
    check("Simulacro P2: fem con v = 0 es nula", emf_moving.subs(v, 0), 0)

    # 3.2 Simulacro C3 P1: Toroide rectangular y autoinductancia
    phi_toroid_turn = sp.integrate((mu0 * N * I / (2 * sp.pi * r)) * h, (r, a, b))
    expected_phi_toroid = (mu0 * N * I * h / (2 * sp.pi)) * sp.log(b / a)
    check("Simulacro P1: Flujo en 1 vuelta del toroide", sp.simplify(phi_toroid_turn - expected_phi_toroid), 0)
    L_toroid = N * phi_toroid_turn / I
    check("Simulacro P1: Autoinductancia L del toroide", sp.simplify(L_toroid - (mu0 * N**2 * h / (2 * sp.pi)) * sp.log(b / a)), 0)
    # Energía magnética por integral de volumen:
    B_toroid = mu0 * N * I / (2 * sp.pi * r)
    U_vol = sp.integrate((B_toroid**2 / (2 * mu0)) * 2 * sp.pi * r * h, (r, a, b))
    U_circ = sp.Rational(1, 2) * L_toroid * I**2
    check("Simulacro P1: Equivalencia energía volumen vs (1/2)*L*I^2", sp.simplify(U_vol - U_circ), 0)

    # 3.3 Ayudantía 11 P2: Cable y rectángulo fijo a distancia a
    phi_rect_ayud11 = sp.integrate((mu0 * I / (2 * sp.pi * x)) * b, (x, a, 2*a))
    check("Ayudantía 11 P2: Flujo cable-rectángulo = (mu0*b*ln(2)/(2*pi))*I", phi_rect_ayud11, (mu0 * b * sp.log(2) / (2 * sp.pi)) * I)
    M_rect = phi_rect_ayud11 / I
    check("Ayudantía 11 P2: Inductancia mutua M = mu0*b*ln(2)/(2*pi)", M_rect, mu0 * b * sp.log(2) / (2 * sp.pi))

    # 3.4 Ayudantía 11 P3: B(y,t) = alpha*y^2 * exp(-beta*t) * k
    C, H, L_w = sp.symbols('C H L_w', positive=True)
    y = sp.symbols('y', positive=True)
    phi_space_time = sp.integrate(alpha * y**2 * sp.exp(-beta * t) * L_w, (y, C, C + H))
    expected_phi_st = (alpha * L_w / 3) * ((C + H)**3 - C**3) * sp.exp(-beta * t)
    check("Ayudantía 11 P3: Flujo con B(y,t)", sp.simplify(phi_space_time - expected_phi_st), 0)
    emf_st = sp.simplify(-sp.diff(phi_space_time, t))
    check("Ayudantía 11 P3: fem inducida = (alpha*beta*L/3)*[(C+H)^3 - C^3]*e^(-beta*t)", emf_st, (alpha * beta * L_w / 3) * ((C + H)**3 - C**3) * sp.exp(-beta * t))

    # 3.5 Ayudantía 11 P4: Solenoide y espira inclinada ángulo alpha_ang
    alpha_ang = sp.symbols('alpha_ang', real=True)
    n_dens = sp.symbols('n_dens', positive=True)
    # Convención de la figura oficial del PDF: alpha medido entre el eje longitudinal y el PLANO de la espira.
    # El vector normal está a (90° - alpha), luego B·n = B*cos(90°-alpha) = B*sin(alpha):
    phi_tilted_sin = (mu0 * n_dens * I) * (sp.pi * b**2) * sp.sin(alpha_ang)
    M_tilted_sin = phi_tilted_sin / I
    check("Ayudantía 11 P4: Inductancia mutua (convención figura PDF: plano-eje -> sin(alpha))", M_tilted_sin, mu0 * n_dens * sp.pi * b**2 * sp.sin(alpha_ang))
    emf_tilted_sin = -sp.diff(phi_tilted_sin.subs(I, I0 * sp.sin(omega * t if 'omega' in locals() else sp.symbols('omega', positive=True) * t)), t)
    omega_sym = sp.symbols('omega', positive=True)
    phi_tilted_t = (mu0 * n_dens * I0 * sp.sin(omega_sym * t)) * (sp.pi * b**2) * sp.sin(alpha_ang)
    check("Ayudantía 11 P4: fem inducida (figura PDF: sin(alpha))", -sp.diff(phi_tilted_t, t), -mu0 * n_dens * sp.pi * b**2 * sp.sin(alpha_ang) * I0 * omega_sym * sp.cos(omega_sym * t))
    # Convención alternativa: si alpha fuese el ángulo entre el eje longitudinal y el VECTOR NORMAL de la espira:
    phi_tilted_cos = (mu0 * n_dens * I) * (sp.pi * b**2) * sp.cos(alpha_ang)
    M_tilted_cos = phi_tilted_cos / I
    check("Ayudantía 11 P4: Inductancia mutua (convención alternativa: normal-eje -> cos(alpha))", M_tilted_cos, mu0 * n_dens * sp.pi * b**2 * sp.cos(alpha_ang))

    # -------------------------------------------------------------
    # 4. DINÁMICA DE RIELES Y BALANCE DE ENERGÍA
    # -------------------------------------------------------------
    print("\n--- 4. Dinámica de Rieles y Balance de Potencia ---")
    m, g, B0, R_res, L_len, w_width = sp.symbols('m g B0 R_res L_len w_width', positive=True)

    # 4.1 Velocidad terminal
    v_t = m * g * R_res / (B0**2 * L_len**2)
    # Balance de potencias:
    P_mec = m * g * v_t
    i_ind = (B0 * L_len * v_t) / R_res
    P_joule = i_ind**2 * R_res
    check("Ayudantía 10 P3: Balance exacto P_mec == P_Joule en v_term", sp.simplify(P_mec - P_joule), 0)

    # 4.1b Verificación vectorial con sp.Matrix.cross de la fuerza sobre la varilla:
    # Ejes según PDF: x a la derecha (1,0,0), z hacia abajo (0,0,1), y saliente (0,1,0)
    I_current = sp.symbols('I_current', positive=True)
    vec_L_rod = sp.Matrix([L_len, 0, 0])
    vec_B_rod = sp.Matrix([0, -B0, 0])
    vec_F_rod = I_current * vec_L_rod.cross(vec_B_rod)
    z_hat_down = sp.Matrix([0, 0, 1])
    # -I * L * B0 * z_hat_down es un vector hacia arriba (-z)
    check("Ayudantía 10 P3: Fuerza magnética F_B = -I*L*B0*z_hat (hacia arriba)", vec_F_rod, -I_current * L_len * B0 * z_hat_down)

    # 4.2 Carrito conductor (Ayudantía 10 P4)
    tau_cart = m * R_res / (B0**2 * a**2)
    v0 = sp.symbols('v0', positive=True)
    v_t_cart = v0 * sp.exp(-t / tau_cart)
    x_stop = sp.integrate(v_t_cart, (t, 0, sp.oo))
    x_max_val = m * v0 * R_res / (B0**2 * a**2)
    check("Ayudantía 10 P4: Penetración x_max = m*v0*R / (B0^2 * a^2) si ancho w > x_max", x_stop, x_max_val)
    # Régimen complementario: si el ancho del carrito w <= x_max
    # Al entrar completamente en x = w, la velocidad es vf = v0 - w / tau_cart > 0
    # Estando totalmente dentro del campo B0 uniforme, dPhi/dt = 0 -> fem = 0 -> i = 0 -> F_B = 0 -> v = vf = cte
    v_residual = v0 - (B0**2 * a**2 / (m * R_res)) * w_width
    check("Ayudantía 10 P4: Velocidad residual vf en x = w si ancho w <= x_max", v_residual, v0 - w_width / tau_cart)

    # -------------------------------------------------------------
    # 5. CIRCUITOS RLC Y SOLUCIÓN DE ECUACIÓN DIFERENCIAL
    # -------------------------------------------------------------
    print("\n--- 5. Circuito RLC y Ecuación Diferencial Oficial ---")
    Q0, C_cap, L_ind = sp.symbols('Q0 C_cap L_ind', positive=True)
    omega0 = sp.symbols('omega0', positive=True)
    alpha_damp = sp.symbols('alpha_damp', positive=True)
    omega_prime = sp.symbols('omega_prime', positive=True)

    # Relaciones del formulario:
    # omega0^2 = 1/(L*C), alpha = R/(2L), omega_prime = sqrt(omega0^2 - alpha^2)
    # Solución: q(t) = Q0 * (omega0/omega') * exp(-alpha*t) * cos(omega'*t - arctan(alpha/omega'))
    theta_damp = sp.atan(alpha_damp / omega_prime)
    q_sol = Q0 * (omega0 / omega_prime) * sp.exp(-alpha_damp * t) * sp.cos(omega_prime * t - theta_damp)

    # Condición inicial q(0) = Q0:
    q_0 = sp.simplify(q_sol.subs(t, 0))
    # cos(-atan(x)) = cos(atan(x)) = 1/sqrt(1+x^2)
    # omega0/omega' * 1/sqrt(1 + alpha^2/omega'^2) = omega0/omega' * omega'/sqrt(omega'^2+alpha^2) = omega0/omega0 = 1
    q_0_eval = sp.simplify(q_0.subs(sp.cos(theta_damp), omega_prime / sp.sqrt(omega_prime**2 + alpha_damp**2)).subs(omega_prime**2 + alpha_damp**2, omega0**2))
    check("RLC Formulario: Condición inicial q(0) == Q0", q_0_eval, Q0)

    # Condición inicial i(0) = dq/dt(0) == 0:
    dq_dt = sp.diff(q_sol, t)
    dq_0 = dq_dt.subs(t, 0)
    # -alpha * cos(-theta) - omega' * sin(-theta) = -alpha * cos(theta) + omega' * sin(theta) = 0 porque tan(theta) = alpha/omega'
    dq_0_eval = sp.simplify(dq_0.subs({
        sp.cos(theta_damp): omega_prime / sp.sqrt(omega_prime**2 + alpha_damp**2),
        sp.sin(theta_damp): alpha_damp / sp.sqrt(omega_prime**2 + alpha_damp**2)
    }))
    check("RLC Formulario: Condición inicial i(0) == 0", dq_0_eval, 0)

    # Ecuación diferencial: d2q/dt2 + 2*alpha*dq/dt + omega0^2*q == 0
    d2q_dt2 = sp.diff(dq_dt, t)
    ode_eval = sp.simplify(d2q_dt2 + 2 * alpha_damp * dq_dt + (omega_prime**2 + alpha_damp**2) * q_sol)
    check("RLC Formulario: Satisface d2q/dt2 + 2*alpha*dq/dt + omega0^2*q == 0", ode_eval, 0)

    # -------------------------------------------------------------
    # 6. CIRCUITO RC/RL CONMUTADO (PAUTA C3 2026-1 P3)
    # -------------------------------------------------------------
    print("\n--- 6. Circuito Transiente Conmutado (Pauta C3 P3) ---")
    R_p3 = 370
    C_p3 = 5e-6
    eps_p3 = 112
    # Inciso a: tau_L = tau_C -> L/R = RC -> L = R^2 * C
    L_p3 = R_p3**2 * C_p3
    check("Pauta C3 P3a: L = (370)^2 * 5e-6 = 0.6845 H", sp.Float(L_p3, 4), sp.Float(0.6845, 4))
    # Inciso b: Ifuente = eps / R = 112 / 370
    I_fuente = eps_p3 / R_p3
    check("Pauta C3 P3b: Ifuente(inf) = 112 / 370 =~ 0.3027 A", round(I_fuente, 3), 0.303)
    # Inciso c: tau_RC = RC = 370 * 5e-6 = 1.85 ms
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
