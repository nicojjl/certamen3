# NOTAS DE REVISIÓN Y VERIFICACIÓN FÍSICA
**FIS120 / FIS12125 · Certamen 3 (2026-2) · UTFSM**

Este documento recopila las verificaciones analíticas, convenciones de signos, elección de normales y casos límite de todos los problemas de ayudantías, pautas y simulacros integrados en la plataforma web.

---

### Módulo 0: Repaso Matemático y Conceptual
- **Producto vectorial:** Se enfatiza la anticonmutatividad $\vec{B}\times\vec{A} = -(\vec{A}\times\vec{B})$ y la regla de la mano derecha.
- **Jacobiano en cilíndricas:** En integrales de superficie plana perpendicular al eje $z$, $d\vec{A} = r\,dr\,d\theta\,\hat{k}$. Al haber simetría azimutal, $\int_0^{2\pi} d\theta = 2\pi \implies dA = 2\pi r dr$.
- **Dimensionalidad:**
  - $\tau_C = RC$: $[\Omega][F] = \left(\frac{V}{A}\right)\left(\frac{A\cdot s}{V}\right) = s$ (segundos).
  - $\tau_L = L/R$: $[H]/[\Omega] = \left(\frac{V\cdot s}{A}\right)\left(\frac{A}{V}\right) = s$ (segundos).
  - Verificado conforme al formulario oficial.

---

### Módulo 1: Biot-Savart y Campo de Cables
- **Problema de Simulacro 2 (Arco y segmento finito):**
  - **Arco:** Radio $R$, 4to cuadrante ($\Delta\theta = \pi/2$), corriente antihoraria. Regla mano derecha: $\vec{B}_{arco} = +\frac{\mu_0 I}{8R}\hat{k}$.
  - **Segmento finito:** Longitud $4R$ ($z \in [-2R, 2R]$), ubicado en $x=2R, y=0$, corriente $+I\hat{k}$.
    - Distancia mínima al origen: $d = 2R$.
    - Semi-longitud: $L = 2R$.
    - Factor de longitud: $\frac{2L}{\sqrt{d^2+L^2}} = \frac{4R}{\sqrt{4R^2+4R^2}} = \frac{4}{2\sqrt{2}} = \sqrt{2}$.
    - Magnitud: $B_{seg} = \frac{\mu_0 I}{4\pi (2R)} \sqrt{2} = \frac{\sqrt{2}\mu_0 I}{8\pi R}$.
    - Dirección por Biot-Savart: $d\vec{l} \times \hat{r}_{obs} = \hat{k} \times (-\hat{\imath}) = -\hat{\jmath}$.
    - Campo total en $O$: $\vec{B}_{neto} = -\frac{\sqrt{2}\mu_0 I}{8\pi R}\hat{\jmath} + \frac{\mu_0 I}{8R}\hat{k}$. Verificado y coherente.
- **Segmentos alineados con el punto de observación:** Aportan $d\vec{B} = 0$ puesto que $d\vec{l}\times\hat{r} = 0$.

---

### Módulo 2: Densidad de Corriente $J(r)$
- **Ayudantía 9 Problema 2:** $J(r) = 2J_0(1 - r^2/a^2)\hat{k}$.
  - Corriente total: $I_T = \int_0^a 2J_0(1 - r^2/a^2) 2\pi r dr = 4\pi J_0 \left[\frac{r^2}{2} - \frac{r^4}{4a^2}\right]_0^a = 4\pi J_0 \frac{a^2}{4} = \pi J_0 a^2$.
- **Pauta C3 Problema 1:** Densidad escalonada:
  - $J_0$ para $0 \le r \le R/2$ y $3J_0$ para $R/2 < r \le R$.
  - $I = J_0 \pi (R/2)^2 + 3J_0 \pi [R^2 - (R/2)^2] = \frac{1}{4}\pi J_0 R^2 + \frac{9}{4}\pi J_0 R^2 = \frac{10}{4}\pi J_0 R^2 = \frac{5}{2}\pi J_0 R^2$.
  - Por tanto: $J_0 = \frac{2I}{5\pi R^2}$. Verificado exactamente con la pauta oficial.
- **Ayudantía 9 Problema 4:** $J_1(\theta) = \alpha \sin^2\theta \hat{k}$.
  - $I_1 = \int_0^{R_1} r dr \int_0^{2\pi} \alpha \sin^2\theta d\theta = \frac{R_1^2}{2} \cdot \alpha \pi = \frac{\pi \alpha R_1^2}{2}$.
  - Igualando con corriente exterior $I_2 = J_0 \pi(R_2^2 - R_1^2)$:
  - $\alpha = \frac{2 J_0 (R_2^2 - R_1^2)}{R_1^2}$.

---

### Módulo 3: Ley de Ampère y Simetrías
- **Pauta C3 Problema 1b:**
  - $r \le R/2$: $B(r) = \frac{\mu_0 J_0 r}{2}\hat{\theta}$.
  - $R/2 < r \le R$: $I_{enc}(r) = \pi J_0 (3r^2 - R^2/2) \implies B(r) = \frac{\mu_0 J_0}{2r}\left(3r^2 - \frac{R^2}{2}\right)\hat{\theta}$.
  - Continuidad en $r = R/2$: $B(R/2^-) = \mu_0 J_0 R / 4$, $B(R/2^+) = \frac{\mu_0 J_0}{R}(3 R^2/4 - R^2/2) = \frac{\mu_0 J_0 R}{4}$. ¡Continuo!
  - Continuidad en $r = R$: $B(R^-) = \frac{\mu_0 J_0}{2R}(3R^2 - R^2/2) = \frac{5}{4}\mu_0 J_0 R = \frac{\mu_0 I}{2\pi R}$. ¡Continuo!
- **Toroide rectangular (Simulacro P1):**
  - $B(r) = \frac{\mu_0 N I}{2\pi r}\hat{\phi}$ en $a < r < b$; cero fuera.
  - Flujo por vuelta: $\Phi_1 = \int_a^b \frac{\mu_0 N I}{2\pi r} h dr = \frac{\mu_0 N I h}{2\pi} \ln(b/a)$.
  - Inductancia mutua con cable axial: Flujo del cable a través de las $N$ vueltas: $M = \frac{N \mu_0 h}{2\pi}\ln(b/a)$. Verificado recíprocamente.

---

### Módulo 4: Flujo Magnético y Faraday-Lenz
- **Espira alejándose de cable infinito (Simulacro P2):**
  - $\Phi_B(t) = \int_{d(t)}^{d(t)+a} \frac{\mu_0 I}{2\pi x} b dx = \frac{\mu_0 I b}{2\pi} \ln\left(1 + \frac{a}{d_0 + vt}\right)$.
  - fem inducida: $\varepsilon = -\frac{d\Phi_B}{dt} = \frac{\mu_0 I b v a}{2\pi (d_0+vt)(d_0+vt+a)}$.
  - Sentido de Lenz: El flujo entrante $\otimes$ disminuye conforme la espira se aleja $\implies$ se induce corriente en sentido horario para reforzar el campo hacia adentro.

---

### Módulo 5: fem de Movimiento y Rieles
- **Varilla cayendo por gravedad (Ayudantía 10 P3):**
  - $\vec{B} = -B_0\hat{\jmath}$, varilla de largo $L$ cae en $-\hat{k}$ con velocidad $v(t)$.
  - $\varepsilon = B_0 L v(t)$, corriente $i = \frac{B_0 L v}{R}$.
  - Fuerza magnética de frenado: $F_m = i L B_0 = \frac{B_0^2 L^2 v}{R}$ dirigida hacia arriba.
  - Ecuación de movimiento: $mg - \frac{B_0^2 L^2 v}{R} = m \frac{dv}{dt}$.
  - Velocidad terminal ($a = 0$): $v_{term} = \frac{mgR}{B_0^2 L^2}$. Coherente en dimensiones y límites.

---

### Módulo 6: Inductancia Mutua y Transformadores
- **Solenoide y bobina cuadrada coaxial (Simulacro P3):**
  - Como $L > 2a$, el campo magnético del solenoide es no nulo solo dentro del cilindro de radio $a$: $B = \mu_0 n I_1$.
  - Todo el flujo que enlaza la bobina cuadrada proviene del área circular $\pi a^2$: $\Phi_{1 vuelta} = (\mu_0 n I_1)(\pi a^2)$.
  - Flujo total sobre las $N$ espiras: $\Phi_{total} = N \mu_0 n \pi a^2 I_1$.
  - Inductancia mutua: $M = \mu_0 n N \pi a^2$ (independiente de $L$ siempre que $L > 2a$).

---

### Módulo 8: Circuitos RC y RL
- **Problema de la Pauta C3 (2026-1 P3):**
  - $C = 5\,\mu\text{F}$, $R = 370\,\Omega$, $\mathcal{E} = 112\,\text{V}$.
  - Igualdad de constantes de tiempo: $\tau_L = \tau_C \implies L/R = RC \implies L = R^2 C = (370)^2 \cdot 5\times 10^{-6} \approx 0.6845\text{ H}$.
  - Corriente de régimen en posición 1: $I_{fuente} = \mathcal{E}/R = 112/370 \approx 0.3027\text{ A}$.
  - Posición 2: $I_C(t) = \frac{\mathcal{E}}{R} e^{-t/RC} = 0.303 e^{-t/1.85\text{ ms}}\text{ A}$. $I_L(t) = \mathcal{E}/R = 0.303\text{ A}$ (constante porque sigue alimentado por la fuente). Verificado exactamente con la pauta.

---

### Módulo 10: Maxwell y Síntesis Conceptual
- **Paradoja del condensador y lazo $\Gamma$:**
  - Superficie $S_1$ (disco plano): atravesada por la corriente de conducción $I(t) \implies \oint_\Gamma \vec{B}\cdot d\vec{l} = \mu_0 I(t)$.
  - Superficie $S_2$ (bolsa entre placas): ninguna corriente de conducción la atraviesa ($I_{cond} = 0$). Sin Maxwell, daría $0$.
  - Con el término de Maxwell: $\Phi_E = E A = \left(\frac{Q(t)}{\varepsilon_0 A}\right) A = \frac{Q(t)}{\varepsilon_0} \implies I_d = \varepsilon_0 \frac{d\Phi_E}{dt} = \frac{dQ}{dt} = I(t)$. Por tanto $\mu_0 I_d = \mu_0 I(t)$, resolviendo la paradoja idénticamente.
- **Campo entre placas a distancia $r < R$:**
  - Lazo circular de radio $r < R$: $\oint \vec{B}\cdot d\vec{l} = B(r) 2\pi r = \mu_0 \varepsilon_0 \frac{d}{dt}\left(E \cdot \pi r^2\right) = \mu_0 \varepsilon_0 \pi r^2 \frac{dE}{dt}$.
  - Como $\frac{dE}{dt} = \frac{I(t)}{\varepsilon_0 \pi R^2} \implies B(r) 2\pi r = \mu_0 \pi r^2 \frac{I(t)}{\pi R^2} = \mu_0 I(t) \frac{r^2}{R^2} \implies B(r) = \frac{\mu_0 I(t) r}{2\pi R^2}$. Verificado.
