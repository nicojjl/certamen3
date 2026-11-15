# NOTAS DE REVISIÓN Y VERIFICACIÓN FÍSICA
**FIS120 / FIS12125 · Certamen 3 (2026-2) · UTFSM**

Este documento recopila las deducciones analíticas completas, convenciones de signos, elección de vectores normales, sentido físico según Lenz, chequeo de unidades y casos límite de todos los problemas de las ayudantías (9, 10, 11), el simulacro oficial y la pauta de certamen incorporados en la plataforma web.

---

## 1. MÓDULO 0: REPASO MATEMÁTICO Y VECTORIAL

### 1.1. Álgebra Vectorial y Regla de la Mano Derecha
- **Anticonmutatividad:** $\vec{A}\times\vec{B} = -(\vec{B}\times\vec{A})$.
- **Versores canónicos cilíndricos:** $\hat{r}\times\hat{\theta} = \hat{k}$, $\hat{\theta}\times\hat{k} = \hat{r}$, $\hat{k}\times\hat{r} = \hat{\theta}$.
- **Elementos de línea y superficie:**
  - $d\vec{l} = dr\,\hat{r} + r\,d\theta\,\hat{\theta} + dz\,\hat{k}$.
  - Para disco plano en $z = \text{cte}$: $d\vec{A} = r\,dr\,d\theta\,\hat{k}$. Con simetría azimutal: $dA = 2\pi r dr$.
  - Para superficie lateral cilíndrica de radio $R$: $d\vec{A} = R\,d\theta\,dz\,\hat{r}$.

### 1.2. Análisis Dimensional
- **Campo magnético:** $[B] = \text{Tesla [T]} = \frac{\text{N}}{\text{A}\cdot\text{m}} = \frac{\text{kg}}{\text{A}\cdot\text{s}^2}$.
- **Permeabilidad del vacío:** $[\mu_0] = \frac{\text{T}\cdot\text{m}}{\text{A}} = \frac{\text{H}}{\text{m}} = \frac{\text{N}}{\text{A}^2} = 4\pi\times 10^{-7}\left[\frac{\text{H}}{\text{m}}\right]$.
- **Inductancia:** $[L] = [M] = \text{Henrio [H]} = \frac{\text{V}\cdot\text{s}}{\text{A}} = \Omega\cdot\text{s}$.
- **Constantes de tiempo:**
  - $\tau_C = RC$: $[\Omega][\text{F}] = \left(\frac{\text{V}}{\text{A}}\right)\left(\frac{\text{A}\cdot\text{s}}{\text{V}}\right) = \text{s}$.
  - $\tau_L = L/R$: $[\text{H}]/[\Omega] = \left(\frac{\text{V}\cdot\text{s}}{\text{A}}\right)\left(\frac{\text{A}}{\text{V}}\right) = \text{s}$.

---

## 2. MÓDULO 1: LEY DE BIOT-SAVART

### 2.1. Cable Recto y Espiras Circulares
- **Cable recto infinito:** $B = \frac{\mu_0 I}{2\pi r}$, dirección azimutal $+\hat{\theta}$.
- **Espira circular en su eje:** $\vec{B}(z) = \frac{\mu_0 I R^2}{2(R^2+z^2)^{3/2}}\hat{k}$. En el centro ($z=0$): $B(0) = \frac{\mu_0 I}{2R}$.
- **Arco circular de ángulo $\Delta\theta$:** $B = \frac{\mu_0 I \Delta\theta}{4\pi R}$. Para semicírculo ($\Delta\theta = \pi$): $B = \frac{\mu_0 I}{4R}$; para cuarto de círculo ($\Delta\theta = \pi/2$): $B = \frac{\mu_0 I}{8R}$.
- **Segmentos radiales dirigidos hacia el punto de observación:** $d\vec{l}\times\hat{r} = 0 \implies \vec{B} = 0$.

### 2.2. Ejercicio Original: Arco y Segmento Finito (Antes rotulado erróneamente como Simulacro P2)
- **Arco en 4to cuadrante:** Radio $R$, corriente $I$ antihoraria $\implies \vec{B}_{arco} = +\frac{\mu_0 I}{8R}\hat{k}$.
- **Segmento finito paralelo a $z$:** Longitud $4R$ ($z \in [-2R, 2R]$), en $x = 2R, y = 0$, corriente $+I\hat{k}$.
  - Distancia al origen: $d = 2R$. Factor de extremos: $\frac{2L}{\sqrt{d^2+L^2}} = \frac{4R}{\sqrt{4R^2+4R^2}} = \sqrt{2}$.
  - Magnitud: $B_{seg} = \frac{\mu_0 I}{4\pi(2R)}\sqrt{2} = \frac{\sqrt{2}\mu_0 I}{8\pi R}$.
  - Dirección: $d\vec{l}\times\hat{r}_{obs} = \hat{k}\times(-\hat{\imath}) = -\hat{\jmath}$.
  - Campo neto en el origen: $\vec{B}(O) = -\frac{\sqrt{2}\mu_0 I}{8\pi R}\hat{\jmath} + \frac{\mu_0 I}{8R}\hat{k}$.
  - *Clasificación:* Ejercicio original (no oficial).

---

## 3. MÓDULO 2: DENSIDAD DE CORRIENTE $J(r)$

### 3.1. Ayudantía 9 Problema 2: Perfil Parabólico
- $\vec{J}(r) = 2J_0\left(1 - \frac{r^2}{a^2}\right)\hat{k}$ para $r \le a$.
- Corriente total:
  $$I_T = \int_0^a 2J_0\left(1 - \frac{r^2}{a^2}\right) 2\pi r dr = 4\pi J_0 \left[\frac{r^2}{2} - \frac{r^4}{4a^2}\right]_0^a = 4\pi J_0 \left(\frac{a^2}{2} - \frac{a^2}{4}\right) = \pi J_0 a^2$$

### 3.2. Pauta C3 2026-1 Problema 1: Efecto Pelicular Escalonado
- Conductor cilíndrico de radio $R$:
  $$J(r) = \begin{cases} J_0, & 0 \le r \le R/2 \\ 3J_0, & R/2 < r \le R \end{cases}$$
- Corriente total $I$:
  $$I = J_0 \pi \left(\frac{R}{2}\right)^2 + 3J_0 \pi \left[R^2 - \left(\frac{R}{2}\right)^2\right] = \frac{\pi J_0 R^2}{4} + 3\pi J_0 \frac{3R^2}{4} = \frac{10\pi J_0 R^2}{4} = \frac{5}{2}\pi J_0 R^2$$
  $$\implies J_0 = \frac{2I}{5\pi R^2}$$

### 3.3. Ayudantía 9 Problema 4: Dependencia Angular
- Cilindro interior radio $R_1$: $\vec{J}_1(\theta) = \alpha \sin^2\theta\,\hat{k}$. Cascarón exterior $R_1 < r < R_2$: $\vec{J}_2 = J_0(-\hat{k})$.
- Corriente interior:
  $$I_1 = \int_0^{R_1} r dr \int_0^{2\pi} \alpha \sin^2\theta d\theta = \frac{R_1^2}{2} \cdot \alpha \pi = \frac{\pi \alpha R_1^2}{2}$$
- Corriente exterior: $I_2 = J_0 \pi (R_2^2 - R_1^2)$.
- Condición de corrientes iguales y opuestas ($I_1 = I_2$):
  $$\frac{\pi \alpha R_1^2}{2} = \pi J_0 (R_2^2 - R_1^2) \implies \alpha = \frac{2J_0 (R_2^2 - R_1^2)}{R_1^2}$$

---

## 4. MÓDULO 3: LEY DE AMPÈRE Y SIMETRÍAS

### 4.1. Ayudantía 9 Problema 1: Cable Coaxial Asimétrico
- Cilindro interior radio $R$, $\vec{J}_1 = J_0\hat{k}$.
- Cascarón exterior $2R < r < 4R$, $\vec{J}_2 = 2J_0(-\hat{k})$.
- Corrientes:
  - $I_1 = J_0 \pi R^2$.
  - $I_2 = 2J_0 \pi [(4R)^2 - (2R)^2] = 2J_0 \pi (16 - 4) R^2 = 24\pi J_0 R^2$.
- **Campo en $r = 3R/2$ (aislante intermedio $R < r < 2R$):**
  - $I_{enc} = I_1 = \pi J_0 R^2$.
  - $\oint \vec{B}\cdot d\vec{l} = B(r) 2\pi r = \mu_0 \pi J_0 R^2 \implies B(3R/2) = \frac{\mu_0 \pi J_0 R^2}{2\pi(3R/2)} = \frac{\mu_0 J_0 R}{3}\hat{\theta}$.
- **Campo en $r = 5R$ (exterior $r > 4R$):**
  - $I_{enc} = I_1 - I_2 = \pi J_0 R^2 - 24\pi J_0 R^2 = -23\pi J_0 R^2$.
  - $\vec{B}(5R) = \frac{\mu_0(-23\pi J_0 R^2)}{2\pi(5R)}\hat{\theta} = -\frac{23}{10}\mu_0 J_0 R\,\hat{\theta}$.

### 4.2. Ayudantía 9 Problema 3: Superposición Fuera de Eje
- **Cilindro macizo:** Eje en $\vec{r}_1 = -a\hat{\imath}$, radio $R < a$, densidad $\vec{J} = \beta r'\hat{k}$.
  - Corriente total: $I_{cil} = \int_0^R (\beta r') 2\pi r' dr' = \frac{2\pi \beta R^3}{3}$.
  - En el origen $O$ ($r = a > R$): el campo es el de una línea con corriente $I_{cil}$ en $(-a, 0)$.
  - Vector posición desde el eje hacia el origen: $\vec{r} = a\hat{\imath}$.
  - Dirección: $\hat{k}\times\hat{\imath} = +\hat{\jmath}$.
  - $\vec{B}_1(O) = \frac{\mu_0 I_{cil}}{2\pi a}\hat{\jmath} = \frac{\mu_0 \beta R^3}{3a}\hat{\jmath}$.
- **Cable infinito:** En $\vec{r}_2 = a(\hat{\imath} - \hat{\jmath}) = (a, -a, 0)$, corriente $I\hat{k}$.
  - Vector desde el cable hacia el origen: $\vec{d} = -a\hat{\imath} + a\hat{\jmath}$, distancia $d = a\sqrt{2}$.
  - Versor tangencial en el origen: $\hat{k} \times \left(\frac{-\hat{\imath}+\hat{\jmath}}{\sqrt{2}}\right) = \frac{-\hat{\jmath}-\hat{\imath}}{\sqrt{2}} = -\frac{\hat{\imath}+\hat{\jmath}}{\sqrt{2}}$.
  - $\vec{B}_2(O) = \frac{\mu_0 I}{2\pi(a\sqrt{2})}\left(-\frac{\hat{\imath}+\hat{\jmath}}{\sqrt{2}}\right) = -\frac{\mu_0 I}{4\pi a}(\hat{\imath} + \hat{\jmath})$.
- **Campo total en el origen:**
  $$\vec{B}_{neto}(O) = -\frac{\mu_0 I}{4\pi a}\hat{\imath} + \left(\frac{\mu_0 \beta R^3}{3a} - \frac{\mu_0 I}{4\pi a}\right)\hat{\jmath}$$
- **Condición para que solo tenga componente en $x$ ($B_y = 0$):**
  $$\frac{\mu_0 \beta R^3}{3a} = \frac{\mu_0 I}{4\pi a} \implies \beta = \frac{3I}{4\pi R^3}$$

### 4.3. Pauta C3 2026-1 Problema 1c: Comparación en $r = 3R/4$
- **Caso Uniforme ($J' = I/\pi R^2$):**
  $$I'_{enc} = J' \pi \left(\frac{3R}{4}\right)^2 = \frac{9}{16}I = \frac{9}{16}\left(\frac{5}{2}\pi J_0 R^2\right) = \frac{45}{32}\pi J_0 R^2$$
  $$B_{unif}\left(\frac{3R}{4}\right) = \frac{\mu_0 I'_{enc}}{2\pi(3R/4)} = \frac{\mu_0 \frac{45}{32}\pi J_0 R^2}{\frac{3}{2}\pi R} = \frac{15}{16}\mu_0 J_0 R \approx 0.9375\text{ }\mu_0 J_0 R$$
- **Caso Escalonado ($J_0$ en $r \le R/2$ y $3J_0$ en $R/2 < r \le R$):**
  $$I_{enc} = J_0 \pi \frac{R^2}{4} + 3J_0 \pi \left[\frac{9R^2}{16} - \frac{R^2}{4}\right] = \pi J_0 R^2 \left[\frac{4}{16} + \frac{15}{16}\right] = \frac{19}{16}\pi J_0 R^2$$
  $$B_{esc}\left(\frac{3R}{4}\right) = \frac{\mu_0 \frac{19}{16}\pi J_0 R^2}{2\pi(3R/4)} = \frac{19}{24}\mu_0 J_0 R \approx 0.7917\text{ }\mu_0 J_0 R$$
- **Comparación:** $\frac{19}{24} \approx 0.792 < \frac{15}{16} \approx 0.938 \implies B_{esc} < B_{unif}$ en $r = 3R/4$.

### 4.4. Simulacro C3 Problema 1: Toroide Ideal de Sección Rectangular
- $a < r < b$, altura $h$, $N$ vueltas, corriente $I$.
- Lazo circular de radio $r$: $\oint \vec{B}\cdot d\vec{l} = B(r) 2\pi r = \mu_0 N I \implies \vec{B}(r) = \frac{\mu_0 N I}{2\pi r}\hat{\phi}$ para $a < r < b$, y $\vec{B} = 0$ fuera.
- Flujo sobre una vuelta: $\phi_1 = \int_a^b \frac{\mu_0 N I}{2\pi r} h dr = \frac{\mu_0 N I h}{2\pi}\ln(b/a)$.
- Inductancia mutua con cable axial (corriente $I_c\hat{k}$):
  El cable genera $\vec{B}_c = \frac{\mu_0 I_c}{2\pi r}\hat{\phi}$.
  Flujo del cable sobre las $N$ vueltas: $\Phi = N \int_a^b \left(\frac{\mu_0 I_c}{2\pi r}\right) h dr = \frac{\mu_0 N I_c h}{2\pi}\ln(b/a)$.
  $$M = \frac{\mu_0 N h}{2\pi}\ln\left(\frac{b}{a}\right)$$

---

## 5. MÓDULO 4: FLUJO MAGNÉTICO Y LEY DE FARADAY-LENZ

### 5.1. Ayudantía 10 Problema 1: Espira con Campo Rotatorio
- Espira cuadrada de lado $a$ en el plano $xy$.
- Campo $\vec{B}(t) = B_0 \cos(k + \omega t)\hat{\imath} + B_0 \sin(k + \omega t)\hat{k}$.
- Normal elegida: $\hat{n} = \hat{k}$ (perpendicular al plano de la espira).
- Flujo: $\phi_B(t) = \vec{B}\cdot\hat{n} a^2 = B_0 a^2 \sin(k + \omega t)$.
- fem inducida: $\varepsilon(t) = -\frac{d\phi_B}{dt} = -B_0 a^2 \omega \cos(k + \omega t)$.
- Magnitud máxima: $|\varepsilon|_{max} = B_0 a^2 \omega$.

### 5.2. Ayudantía 10 Problema 2: Espira Circular y Espira Cuadrada en su Centro
- Espira circular de radio $R$, corriente $I(t) = I_0 e^{-t/\tau}$ antihoraria.
- Espira cuadrada central de lado $a \ll R$.
- Campo en el centro: $\vec{B} = \frac{\mu_0 I(t)}{2R}\hat{k}$ (saliente, $\odot$). Como $a \ll R$, es uniforme sobre el área $a^2$.
- Flujo sobre la espira cuadrada (normal $\hat{n} = +\hat{k}$):
  $$\phi_B(t) = \frac{\mu_0 I_0 a^2}{2R} e^{-t/\tau}$$
- fem inducida:
  $$\varepsilon(t) = -\frac{d\phi_B}{dt} = \frac{\mu_0 I_0 a^2}{2R\tau} e^{-t/\tau}$$
- **Sentido por Lenz:** La corriente exterior disminuye $\implies$ el flujo saliente $\odot$ disminuye $\implies$ la espira cuadrada induce corriente en sentido **antihorario** para reforzar el flujo saliente original.

### 5.3. Ayudantía 11 Problema 3: Campo Espacio-Temporal $\vec{B}(y,t) = \alpha y^2 e^{-\beta t}\hat{k}$
- Rectángulo de base $L$ (en $x$) y altura $H$ (en $y$), lado inferior en $y = C$, luego $y \in [C, C+H]$.
- Normal elegida: $\hat{n} = +\hat{k}$ (saliente, concordante con circulación antihoraria).
- Flujo:
  $$\phi_B(t) = \int_C^{C+H} (\alpha y^2 e^{-\beta t}) L dy = \frac{\alpha L}{3} \left[(C+H)^3 - C^3\right] e^{-\beta t}$$
- fem inducida:
  $$\varepsilon(t) = -\frac{d\phi_B}{dt} = \frac{\alpha \beta L}{3}\left[(C+H)^3 - C^3\right] e^{-\beta t}$$
- **Sentido por Lenz:** El campo saliente ($\hat{k}$) decae en el tiempo ($e^{-\beta t}$) $\implies d\phi_B/dt < 0$. Para oponerse a la disminución, la corriente inducida debe reforzar el campo saliente $\odot \implies$ circula en **sentido antihorario**.

### 5.4. Simulacro C3 Problema 2: Espira Alejándose de Cable Infinito
- Cable en eje $y$ con corriente $I\hat{\jmath}$. Espira rectangular de lados $a$ (en $x$) y $b$ (en $y$) alejándose con $\vec{v} = v\hat{\imath}$. Posición $x \in [d(t), d(t)+a]$ con $d(t) = d_0 + vt$.
- Campo magnético del cable: $\vec{B}(x) = \frac{\mu_0 I}{2\pi x}(-\hat{k})$ (entrante $\otimes$).
- Normal elegida: $\hat{n} = -\hat{k}$ (entrante, concordante con circulación horaria).
- Flujo magnético:
  $$\phi_B(t) = \int_{d(t)}^{d(t)+a} \left(\frac{\mu_0 I}{2\pi x}\right) b dx = \frac{\mu_0 I b}{2\pi}\ln\left(\frac{d_0+vt+a}{d_0+vt}\right) = \frac{\mu_0 I b}{2\pi}\ln\left(1 + \frac{a}{d_0+vt}\right)$$
- fem inducida ($\varepsilon = -d\phi_B/dt$):
  $$\frac{d\phi_B}{dt} = \frac{\mu_0 I b}{2\pi} \frac{1}{1 + \frac{a}{d(t)}} \left(-\frac{a v}{d(t)^2}\right) = -\frac{\mu_0 I b v a}{2\pi d(t)(d(t)+a)}$$
  $$\varepsilon(t) = -\frac{d\phi_B}{dt} = +\frac{\mu_0 I b v a}{2\pi (d_0+vt)(d_0+vt+a)}$$
- **Sentido por Lenz:** Al alejarse, el campo entrante $\otimes$ se debilita $\implies$ el flujo entrante disminuye $\implies$ la corriente inducida genera campo entrante propio $\otimes \implies$ circula en **sentido horario**. Como $\hat{n}$ fue elegida entrante, el signo positivo de $\varepsilon$ coincide con circulación horaria.

---

## 6. MÓDULO 5: FEM DE MOVIMIENTO Y RIELES

### 6.1. Ayudantía 10 Problema 3: Varilla en Rieles con Gravedad
- Rieles paralelos verticales separados por distancia $L$, resistencia $R$, masa $m$.
- Convención de ejes del PDF: eje $x$ hacia la derecha ($\hat{x}$), eje $z$ vertical hacia abajo ($\hat{z}$), eje $y$ perpendicular saliente de la página ($\hat{y}$, con $\hat{x}\times\hat{y}=\hat{z}$).
- Campo magnético uniforme: $\vec{B} = -B_0\hat{\jmath}$ (entrante al plano $xz$ del circuito, $\otimes$).
- Posición de caída de la varilla: $z(t)$, velocidad hacia abajo: $\vec{v}(t) = \dot{z}\hat{z} = v(t)\hat{z}$ (hacia abajo, $+z$).
- Área enlazada en el plano $xz$: $A(t) = L z(t)$.
- Vector normal elegido (entrante): $\hat{n} = -\hat{\jmath}$ ($\otimes$), con sentido (+) de circulación horario.
- Flujo magnético: $\phi_B(t) = \vec{B}\cdot(A\hat{n}) = (-B_0\hat{\jmath})\cdot(L z(t)(-\hat{\jmath})) = B_0 L z(t) > 0$.
- Variación de flujo: $\frac{d\phi_B}{dt} = B_0 L \dot{z} = B_0 L v(t) > 0$ (positiva, el flujo entrante aumenta al caer).
- fem inducida: $\varepsilon = -\frac{d\phi_B}{dt} = -B_0 L v(t) < 0$ (signo negativo respecto a la normal $\implies$ circulación en **sentido antihorario**).
- **Sentido por Lenz:** El flujo entrante $\otimes$ aumenta a medida que la varilla cae $\implies$ la corriente inducida genera campo saliente $\odot$ ($+B_{ind}\hat{\jmath}$) para oponerse al aumento $\implies$ por regla de la mano derecha, circula en **sentido antihorario** (de izquierda a derecha a través de la varilla móvil: $\vec{L} = L\hat{x}$).
- Corriente inducida: $i(t) = \frac{B_0 L v(t)}{R}$.
- Fuerza magnética de Lorentz sobre la varilla (verificada con SymPy `sp.Matrix.cross`):
  $$\vec{F}_B = i\vec{L}\times\vec{B} = (i L \hat{x}) \times (-B_0 \hat{\jmath}) = -i L B_0 (\hat{x}\times\hat{\jmath}) = -i L B_0 \hat{z} = -\frac{B_0^2 L^2 v}{R}\hat{z}$$
  Como $\hat{z}$ apunta hacia abajo, $-\hat{z}$ apunta **hacia arriba**, actuando como fuerza retardadora de frenado que se opone directamente al peso gravitatorio $m\vec{g} = mg\hat{z}$.
- Ecuación de movimiento de Newton en el eje $z$:
  $$m\frac{dv}{dt} = mg - \frac{B_0^2 L^2}{R}v$$
- Velocidad terminal ($dv/dt = 0$):
  $$v_{term} = \frac{mg R}{B_0^2 L^2}$$
- **Balance de potencias:**
  - Potencia mecánica entregada por la gravedad: $P_{mec} = F_g v_{term} = mg v_{term} = \frac{m^2 g^2 R}{B_0^2 L^2}$.
  - Potencia disipada por efecto Joule en la resistencia: $P_{Joule} = i^2 R = \left(\frac{B_0 L v_{term}}{R}\right)^2 R = \frac{B_0^2 L^2 v_{term}^2}{R} = \frac{m^2 g^2 R}{B_0^2 L^2}$.
  - $P_{mec} = P_{Joule}$ confirma rigurosamente el principio de conservación de energía.

### 6.2. Ayudantía 10 Problema 4: Carrito Conductor Entrando al Campo
- Espira conductora de lado $a$, masa $m$, resistencia $R$, velocidad inicial $\vec{v}_0 = v_0\hat{\imath}$.
- Entra a región $x > 0$ con campo saliente $\vec{B} = B_0\hat{k}$.
- Longitud dentro del campo: $x(t)$. Área dentro del campo: $A(t) = a x(t)$.
- Flujo saliente: $\phi_B(t) = B_0 a x(t)$ (con $\hat{n} = +\hat{k}$).
- fem inducida: $\varepsilon = -\frac{d\phi_B}{dt} = -B_0 a v(t)$.
- **Sentido por Lenz:** El flujo saliente $\odot$ aumenta al penetrar $\implies$ la corriente inducida debe generar campo entrante $\otimes \implies$ circula en **sentido horario**.
- Corriente: $i(t) = \frac{B_0 a v(t)}{R}$.
- Fuerza magnética sobre el lado que corta líneas de campo ($x = x(t)$):
  La corriente en ese tramo va hacia $-y$ ($-\hat{\jmath}$):
  $$\vec{F}_B = i(-a\hat{\jmath})\times(B_0\hat{k}) = -i a B_0\hat{\imath} = -\frac{B_0^2 a^2 v}{R}\hat{\imath}$$
  ¡La fuerza magnética frena al carrito hacia la izquierda!
- Ecuación diferencial:
  $$m\frac{dv}{dt} = -\frac{B_0^2 a^2}{R}v \implies v(t) = v_0 e^{-t/\tau}, \quad \tau = \frac{m R}{B_0^2 a^2}$$
- Distancia máxima de penetración (válida si el largo de la espira en avance $w > x_{\max}$):
  $$m v \frac{dv}{dx} = -\frac{B_0^2 a^2}{R} v \implies m(v - v_0) = -\frac{B_0^2 a^2}{R} x \implies v(x) = v_0 - \frac{B_0^2 a^2}{m R} x$$
  Haciendo $v = 0$:
  $$x_{\max} = \frac{m v_0 R}{B_0^2 a^2}$$
- **Condición geométrica y caso alternativo:**
  - **Caso 1 ($w > x_{\max}$):** La espira se frena y se detiene completamente ($v = 0$) en $x = x_{\max}$ mientras aún está penetrando, quedando parcialmente inmersa.
  - **Caso 2 ($w \le x_{\max}$):** La espira ingresa completamente al campo en $x = w$ antes de detenerse, con velocidad residual $v_f = v_0 - \frac{B_0^2 a^2 w}{m R} > 0$. Una vez dentro, el área inmersa es constante ($A = a \cdot w$), por lo que $\phi_B = \text{cte} \implies \varepsilon_{ind} = 0 \implies i = 0 \implies \vec{F}_B = \vec{0}$. Por el Principio de Inercia de Newton, el carrito continúa avanzando indefinidamente con velocidad constante $v_f$.

---

## 7. MÓDULO 6: INDUCTANCIA MUTUA Y TRANSFORMADORES

### 7.1. Ayudantía 11 Problema 1: Bobinas Concéntricas
- Solenoide interno radio $R$, $N_i$ espiras, largo $l$ ($n_i = N_i/l$). Solenoide externo radio $3R$, $N_e$ espiras, largo $l$.
- Corriente en interno: $I_i(t) = I_0 \cos(\omega t)$ antihoraria.
- Campo interno: $B_i = \mu_0 n_i I_i = \mu_0 \frac{N_i}{l}I_i$ para $r < R$, y $B_i = 0$ para $r > R$.
- Flujo sobre UNA vuelta de la bobina externa ($r = 3R$):
  $$\phi_1 = \iint_{r \le 3R} \vec{B}_i\cdot d\vec{A} = B_i (\pi R^2) = \mu_0 \frac{N_i}{l} \pi R^2 I_i$$
  (El radio $3R$ no entra en el flujo porque no hay campo fuera de $R$).
- Inductancia mutua:
  $$M = \frac{N_e \phi_1}{I_i} = \mu_0 \frac{N_i N_e \pi R^2}{l}$$
- fem inducida en la bobina exterior:
  $$\varepsilon_e(t) = -M \frac{dI_i}{dt} = -M \frac{d}{dt}(I_0 \cos\omega t) = M I_0 \omega \sin(\omega t) = \mu_0 \frac{N_i N_e \pi R^2}{l} I_0 \omega \sin(\omega t)$$

### 7.2. Ayudantía 11 Problema 2: Cable Infinito y Rectángulo Conductor
- Cable con $I(t) = I_0 e^{-t/\tau}$. Rectángulo en $x \in [a, 2a]$, altura $b$.
- $\phi_B(t) = \int_a^{2a} \frac{\mu_0 I(t)}{2\pi x} b dx = \frac{\mu_0 b \ln 2}{2\pi} I(t)$.
- $M = \frac{\phi_B(t)}{I(t)} = \frac{\mu_0 b \ln 2}{2\pi}$.
- fem inducida: $\varepsilon(t) = \frac{\mu_0 b \ln 2}{2\pi\tau} I_0 e^{-t/\tau}$ en **sentido horario**.

### 7.3. Ayudantía 11 Problema 4: Solenoide con Espira Inclinada en Ángulo $\alpha$
- Solenoide largo de radio $a$, densidad de vueltas $n$, campo interno uniforme $\vec{B} = \mu_0 n I \hat{z}$.
- Espira circular de radio $b < a$ centrada en el interior de la bobina.
- **Distinción crucial de convención geométrica según la figura oficial del certamen:**
  - **Convención de la figura oficial del PDF (ángulo entre eje y plano de la espira):** En el diagrama original de la Ayudantía 11, el arco $\alpha$ está acotado entre el eje longitudinal horizontal ($\hat{z}$) y el *plano* geométrico de la espira circular. Dado que la normal unitaria $\hat{n}$ es ortogonal a dicho plano, el ángulo entre $\vec{B}$ y $\hat{n}$ es el ángulo complementario: $\theta_n = 90^\circ - \alpha$.
    - $\vec{B}\cdot\hat{n} = B \cos(90^\circ - \alpha) = B \sin\alpha$.
    - Flujo magnético sobre la espira: $\phi_B(t) = (\mu_0 n I(t))(\pi b^2)\sin\alpha = \mu_0 n \pi b^2 \sin\alpha\,I(t)$.
    - Inductancia mutua: $M = \frac{\phi_B(t)}{I(t)} = \mu_0 n \pi b^2 \sin\alpha$.
    - fem inducida con $I(t) = I_0 \sin(\omega t)$:
      $$\varepsilon(t) = -M \frac{dI}{dt} = -\mu_0 n \pi b^2 \sin\alpha\,I_0 \omega \cos(\omega t)$$
    - *Chequeo de casos límite:*
      - Si $\alpha = 0^\circ$ (espira paralela al eje longitudinal): las líneas de campo pasan rasantes a la espira, el flujo es cero y $M = 0$, coincidiendo con $\sin(0^\circ) = 0$.
      - Si $\alpha = 90^\circ$ (espira ortogonal al eje longitudinal): el campo incide frontalmente, el flujo es máximo y $M = \mu_0 n \pi b^2$, coincidiendo con $\sin(90^\circ) = 1$.
  - **Convención alternativa (ángulo entre eje y vector normal $\hat{n}$):** Si un texto define $\alpha$ como el ángulo entre el eje longitudinal $\hat{z}$ y el *vector normal* $\hat{n}$ de la espira:
    - $\vec{B}\cdot\hat{n} = B \cos\alpha$.
    - $\phi_B(t) = \mu_0 n \pi b^2 \cos\alpha\,I(t)$.
    - $M = \mu_0 n \pi b^2 \cos\alpha$.
    - $\varepsilon(t) = -\mu_0 n \pi b^2 \cos\alpha\,I_0 \omega \cos(\omega t)$.
  - Ambas variantes han sido comprobadas con SymPy en `scripts/verificar.py`. La web presenta la convención de la figura oficial ($\sin\alpha$) con una nota aclaratoria sobre la convención alternativa ($\cos\alpha$).

### 7.4. Pauta C3 2026-1 Problema 2: Rollo con Espira Central Pequeña
- Rollo plano de $N$ espiras de radio $R$. Espira central de radio $r \ll R$.
- Campo en el centro: $B(t) = \frac{N \mu_0 I(t)}{2R}$.
- Flujo en la pequeña espira: $\Phi_B = B (\pi r^2) = \frac{N \mu_0 \pi r^2}{2R} I(t)$.
- Inductancia mutua: $M = \frac{N \mu_0 \pi r^2}{2R}$.
- Corriente $I(t) = I_0$ para $t < 0$ y $I(t) = I_0 e^{-t/\tau}$ para $t \ge 0$.
  - Para $t < 0$: $dI/dt = 0 \implies \varepsilon_{ind} = 0$.
  - Para $t \ge 0$: $\varepsilon_{ind} = -M \frac{dI}{dt} = \frac{N \mu_0 \pi r^2 I_0}{2R\tau} e^{-t/\tau}$.
  - Sentido por Lenz ($t \ge 0$): Flujo saliente disminuye $\implies$ corriente inducida en **sentido antihorario**.

### 7.5. Ayudantía 11 Conceptual: Transformador Ideal
- Relación de voltajes: $\frac{V_s}{V_p} = \frac{N_s}{N_p}$.
- Corriente continua: Al ser $I_p = \text{cte}$, $d\phi_B/dt = 0 \implies V_s = 0$. Además, sin reactancia inductiva se quema el bobinado por sobrecorriente.

---

## 8. MÓDULO 7: AUTOINDUCTANCIA Y ENERGÍA MAGNÉTICA

### 8.1. Solenoide Ideal
- $B = \mu_0 n I$. Flujo en $N = n l$ espiras de área $A$: $\Phi = N (B A) = (n l)(\mu_0 n I A) = \mu_0 n^2 l A I$.
- Autoinductancia:
  $$L = \frac{\Phi}{I} = \mu_0 n^2 l A$$
- fem autoinducida: $\varepsilon_L = -\frac{d\Phi}{dt} = -L \frac{di}{dt}$.
- Energía magnética almacenada:
  $$U_L = \int_0^I L i di = \frac{1}{2} L I^2$$
- Densidad volumétrica de energía:
  $$u_B = \frac{U_L}{l A} = \frac{\frac{1}{2}(\mu_0 n^2 l A) I^2}{l A} = \frac{(\mu_0 n I)^2}{2\mu_0} = \frac{B^2}{2\mu_0}$$

### 8.2. Toroide Rectangular
- $a < r < b$, altura $h$, $N$ vueltas: $B(r) = \frac{\mu_0 N I}{2\pi r}$.
- Flujo total: $\Phi = N \int_a^b \frac{\mu_0 N I h}{2\pi r} dr = \frac{\mu_0 N^2 I h}{2\pi}\ln(b/a)$.
- Autoinductancia:
  $$L = \frac{\mu_0 N^2 h}{2\pi}\ln\left(\frac{b}{a}\right)$$
- Energía por integral de volumen:
  $$U_L = \iiint \frac{B^2}{2\mu_0} dV = \int_a^b \frac{1}{2\mu_0}\left(\frac{\mu_0 N I}{2\pi r}\right)^2 (2\pi r h dr) = \frac{\mu_0 N^2 I^2 h}{4\pi}\int_a^b \frac{dr}{r} = \frac{\mu_0 N^2 I^2 h}{4\pi}\ln\left(\frac{b}{a}\right) = \frac{1}{2} L I^2$$

---

## 9. MÓDULO 8: CIRCUITOS TRANSIENTES RC Y RL

### 9.1. Pauta C3 2026-1 Problema 3: Circuito con Interruptor de 2 Posiciones
- $C = 5\text{ }\mu\text{F}$, $R = 370\text{ }\Omega$, $\mathcal{E} = 112\text{ V}$.
- **a) Igualdad de constantes $\tau_L = \tau_C$:**
  $$\frac{L}{R} = RC \implies L = R^2 C = (370)^2 \cdot (5\times 10^{-6}) = 136900 \times 5\times 10^{-6} = 0.6845\text{ H}$$
- **b) Régimen permanente en posición 1 ($t \to \infty$):**
  - Condensador cargado $\implies$ circuito abierto ($I_C = 0$).
  - Inductor en régimen permanente $\implies$ conductor ideal ($V_L = 0$).
  - Corriente de la fuente: $I_{fuente} = \frac{\mathcal{E}}{R} = \frac{112}{370} \approx 0.3027\text{ A}$.
- **c) Conmutación a posición 2:**
  - Rama RC desconectada de la fuente: descarga con $q(0) = C\mathcal{E}$:
    $$I_C(t) = \frac{\mathcal{E}}{R} e^{-t/RC} = \frac{112}{370} e^{-t/(1.85\times 10^{-3})} \approx 0.303 e^{-t/1.85\text{ ms}}\text{ A}$$
  - Rama RL sigue conectada a la fuente $\implies$ permanece en su valor de régimen estacionario:
    $$I_L(t) = \frac{\mathcal{E}}{R} = 0.303\text{ A}$$

---

## 10. MÓDULO 9: CIRCUITOS OSCILANTES LC Y RLC

### 10.1. Circuito LC Libre
- Ecuación: $-L\frac{d^2q}{dt^2} - \frac{q}{C} = 0 \implies \frac{d^2q}{dt^2} + \omega_0^2 q = 0$.
- Frecuencia natural: $\omega_0 = \frac{1}{\sqrt{LC}}$.
- Solución: $q(t) = Q_0 \cos(\omega_0 t)$, $i(t) = -\omega_0 Q_0 \sin(\omega_0 t)$.
- Conservación de energía: $U_{tot} = \frac{q(t)^2}{2C} + \frac{1}{2}L i(t)^2 = \frac{Q_0^2}{2C} = \text{cte}$.

### 10.2. Circuito RLC Serie y los Tres Regímenes
- Ecuación diferencial del formulario:
  $$-L\frac{d^2q}{dt^2} - R\frac{dq}{dt} - \frac{q}{C} = 0 \iff \frac{d^2q}{dt^2} + 2\alpha \frac{dq}{dt} + \omega_0^2 q = 0$$
- Factor de amortiguamiento: $\alpha = \frac{R}{2L}$.
- **1. Subamortiguado ($\alpha < \omega_0 \iff R < 2\sqrt{L/C}$):**
  - Frecuencia amortiguada: $\omega' = \sqrt{\omega_0^2 - \alpha^2}$.
  - Solución del formulario:
    $$q(t) = Q_0 \frac{\omega_0}{\omega'} e^{-\alpha t} \cos\left(\omega' t - \arctan\left(\frac{\alpha}{\omega'}\right)\right)$$
- **2. Críticamente amortiguado ($\alpha = \omega_0 \iff R = R_{crit} = 2\sqrt{L/C}$):**
  - Retorno asintótico más rápido a cero sin sobrepaso oscilatorio.
  - Solución: $q(t) = Q_0 (1 + \alpha t) e^{-\alpha t}$.
- **3. Sobreamortiguado ($\alpha > \omega_0 \iff R > 2\sqrt{L/C}$):**
  - Decaimiento puramente exponencial no oscilatorio con dos constantes de tiempo.

---

## 11. MÓDULO 10: MAXWELL Y SÍNTESIS CONCEPTUAL

### 11.1. Paradoja de Ampère y Corriente de Desplazamiento
- Ecuación corregida por Maxwell: $\oint_\Gamma \vec{B}\cdot d\vec{l} = \mu_0 (I_{cond} + I_d)$, con $I_d = \varepsilon_0 \frac{d\phi_E}{dt}$.
- Condensador circular plano de radio $R$:
  - Superficie $S_1$ (disco que corta el cable): $I_{cond} = I(t)$, $I_d = 0 \implies \oint_\Gamma \vec{B}\cdot d\vec{l} = \mu_0 I(t)$.
  - Superficie $S_2$ (bolsa entre placas): $I_{cond} = 0$. $\phi_E = E A = \frac{Q(t)}{\varepsilon_0 A} A = \frac{Q(t)}{\varepsilon_0} \implies I_d = \varepsilon_0 \frac{d\phi_E}{dt} = \frac{dQ}{dt} = I(t)$.
  - $\oint_\Gamma \vec{B}\cdot d\vec{l} = \mu_0 I_d = \mu_0 I(t)$. Ambas superficies dan exactamente el mismo resultado.
- **Campo $B(r)$ entre placas ($r < R$):**
  - Para un lazo de radio $r < R$: $\phi_E(r) = E (\pi r^2) = \frac{Q(t)}{\varepsilon_0 \pi R^2} (\pi r^2) = \frac{Q(t) r^2}{\varepsilon_0 R^2}$.
  - $I_{d,enc} = \varepsilon_0 \frac{d\phi_E(r)}{dt} = I(t) \frac{r^2}{R^2}$.
  - $\oint \vec{B}\cdot d\vec{l} = B(r) 2\pi r = \mu_0 I(t)\frac{r^2}{R^2} \implies \vec{B}(r) = \frac{\mu_0 I(t) r}{2\pi R^2}\hat{\theta}$.

### 11.2. Pauta C3 Conceptual: Cocina de Inducción
- **Condición del campo:** Debe ser alterno de alta frecuencia ($\partial\vec{B}/\partial t \neq 0$).
- **Olla de acero:** Conductor metálico ferromagnético $\implies$ circulan fuertes corrientes de Foucault (Eddy currents) que disipan calor rápidamente por efecto Joule ($P = I^2 R$).
- **Olla de greda:** Material cerámico aislante ($\rho \to \infty$) $\implies$ corrientes inducidas despreciables $\implies$ no calienta.

---

## 12. ESTADO DE VERIFICACIÓN ANALÍTICA

### 12.1. Salida de Verificación SymPy (scripts/verificar.py)
La verificación analítica simbólica completa se ejecuta de forma reproducible e independiente mediante el script `scripts/verificar.py`. La salida detallada con el registro de las 87 pruebas unitarias exitosas (87/87 [PASS], exit code 0) se encuentra almacenada y disponible en el archivo de texto dedicado:

> 📄 **Reporte Completo de Salida:** [scripts/salida_verificar.txt](file:///d:/ALGORITMICA/fis120-certamen3/scripts/salida_verificar.txt) (o ruta relativa de repositorio: [scripts/salida_verificar.txt](scripts/salida_verificar.txt)).

#### Resumen Cuantitativo de la Suite de Verificación
- **Módulos evaluados:** 12 módulos (Módulo 0 al Módulo 11).
- **Pruebas analíticas SymPy:** 87 pruebas ejecutadas, 87 pruebas pasadas (0 fallas).
- **Pruebas de consistencia numérica:** 15 ejercicios evaluados contra cálculo físico teórico independiente en `scripts/verificar_numericos.py` (15/15 correctos dentro de tolerancia).
- **Auditoría KaTeX y DOM interactivo:** 12 módulos navegados e interactuados con Playwright en `scripts/verify_browser_katex.py` (2052 fórmulas renderizadas, 0 errores KaTeX, 0 errores de consola, 0 comandos sueltos).
- **Validación vectorial SVG y TikZ:** 25 figuras analizadas en `scripts/check_figures.py` (25/25 XML válido, < 120 KB, sin referencias externas HTTP).

---

### 12.2. Tabla de Sentidos, Vectores Normales y Signos (Razonado a Mano)

> [!NOTE]
> La verificación de signos algebraicos según el vector normal elegido ($\hat{n}$) y la orientación física del sentido de circulación mediante la **Ley de Lenz** no puede ser automatizada con SymPy de forma geométrica tridimensional; por ende, se presenta a continuación la tabla de verificación formal **razonada a mano** para cada uno de los problemas clave de inducción.

| Problema / Sistema | Campo Externo $\vec{B}_{\text{ext}}$ | Vector Normal $\hat{n}$ y Sentido (+) | Variación de Flujo $\frac{d\Phi_B}{dt}$ | Signo de fem $\varepsilon = -\frac{d\Phi_B}{dt}$ | Campo Inducido $\vec{B}_{\text{ind}}$ (Lenz) | Sentido Físico de Circulación (razonado a mano) | Comportamiento Dinámico / Comprobación Física |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Espira alejándose de cable infinito** *(Simulacro P2 / M4 P7)* | $\vec{B} = -\frac{\mu_0 I}{2\pi x}\hat{k}$ ($\otimes$, entrante al plano $xy$) | $\hat{n} = -\hat{k}$ ($\otimes$)<br>Sentido (+): **Horario** | **Negativa** ($\frac{d\Phi_B}{dt} < 0$), pues la distancia $x(t) = d_0 + vt$ crece y el campo se debilita. | $\varepsilon > 0$<br>(circula en sentido +) | $\vec{B}_{\text{ind}} = \otimes$ (entrante, busca compensar el flujo perdido) | **Horario** *(razonado a mano)* | Por la regla de la mano derecha, la corriente en la rama izquierda (más cercana al cable) sube ($+\hat{\jmath}$), sintiendo una fuerza magnética de atracción hacia el cable ($-\hat{\imath}$), frenando el alejamiento. |
| **Varilla conductora en rieles verticales** *(Ayudantía 10 P3 / M5 P5)* | $\vec{B} = -B_0\hat{\jmath}$ ($\otimes$, entrante al plano $xz$, con $x$ a la derecha, $z$ hacia abajo e $y$ saliente) | $\hat{n} = -\hat{\jmath}$ ($\otimes$)<br>Sentido (+): **Horario** | **Positiva** ($\frac{d\Phi_B}{dt} = B_0 L v > 0$), pues al caer la varilla con velocidad $\vec{v} = v\hat{z}$ hacia abajo, el área $A(z) = L z$ aumenta. | $\varepsilon = -B_0 L v < 0$<br>(circula en sentido opuesto al +, antihorario) | $\vec{B}_{\text{ind}} = \odot = +B_{ind}\hat{\jmath}$ (saliente, se opone al aumento de campo entrante) | **Antihorario** *(razonado a mano)* | La corriente en la varilla fluye hacia la derecha ($+\hat{x}$). La fuerza magnética resultante es $\vec{F}_B = I(L\hat{x})\times(-B_0\hat{\jmath}) = -I L B_0\hat{z}$ (hacia arriba, pues $\hat{z}$ apunta hacia abajo y $-\hat{z}$ apunta hacia arriba), frenando la caída hasta alcanzar la velocidad límite terminal $v_{term} = \frac{mgR}{B_0^2 L^2}$. |
| **Carrito conductor entrando a zona con campo** *(Ayudantía 10 P4 / M5 P6)* | $\vec{B} = +B_0\hat{k}$ ($\odot$, saliente uniforme) | $\hat{n} = +\hat{k}$ ($\odot$)<br>Sentido (+): **Antihorario** | **Positiva** ($\frac{d\Phi_B}{dt} > 0$), pues penetra con velocidad $v$ aumentando el área inmersa ($dA/dt = a v > 0$). | $\varepsilon < 0$<br>(circula en sentido opuesto al +) | $\vec{B}_{\text{ind}} = \otimes$ (entrante, se opone al incremento de flujo saliente) | **Horario** *(razonado a mano)* | En el alambre frontal delantero inmerso, la corriente circula hacia abajo ($-\hat{\jmath}$). La fuerza magnética es $\vec{F}_B = I_{\text{ind}}(-a\hat{\jmath})\times(B_0\hat{k}) = -I_{\text{ind}}a B_0\hat{\imath}$ (hacia atrás): la fuerza siempre frena al móvil. |
| **Cable infinito con $I(t) = I_0 e^{-t/\tau}$ y rectángulo** *(Ayudantía 11 P2 / M6 P6)* | $\vec{B} = -\frac{\mu_0 I(t)}{2\pi x}\hat{k}$ ($\otimes$, entrante al plano) | $\hat{n} = -\hat{k}$ ($\otimes$)<br>Sentido (+): **Horario** | **Negativa** ($\frac{d\Phi_B}{dt} < 0$), pues la corriente en el cable se extingue exponencialmente en el tiempo. | $\varepsilon > 0$<br>(circula en sentido +) | $\vec{B}_{\text{ind}} = \otimes$ (entrante, intenta sostener el campo que desaparece) | **Horario** *(razonado a mano)* | Por la regla de la mano derecha, pulgar hacia adentro ($\otimes$) induce circulación horaria, conforme al principio de inercia electromagnética de Lenz. |
| **Rectángulo en campo dependiente $B(y,t) = \alpha y^2 e^{-\beta t}\hat{k}$** *(Ayudantía 11 P3 / M4 P8)* | $\vec{B} = +\alpha y^2 e^{-\beta t}\hat{k}$ ($\odot$, saliente espacial y temporal) | $\hat{n} = +\hat{k}$ ($\odot$)<br>Sentido (+): **Antihorario** | **Negativa** ($\frac{d\Phi_B}{dt} < 0$), pues el factor $e^{-\beta t}$ decae para todo punto del espacio. | $\varepsilon > 0$<br>(circula en sentido +) | $\vec{B}_{\text{ind}} = \odot$ (saliente, refuerza el flujo decreciente) | **Antihorario** *(razonado a mano)* | Pulgar hacia afuera ($\odot$) produce giro antihorario en los dedos, sosteniendo el flujo inductivo. |
| **Rollo plano circular con pequeña espira concéntrica** *(Pauta C3 2026-1 P2 / M6 P7c)* | $\vec{B}(t) = +\frac{N\mu_0 I(t)}{2R}\hat{k}$ ($\odot$, saliente por corriente antihoraria) | $\hat{n} = +\hat{k}$ ($\odot$)<br>Sentido (+): **Antihorario** | Para $t < 0$: nula ($\frac{d\Phi_B}{dt} = 0$).<br>Para $t \ge 0$: **Negativa** ($\frac{d\Phi_B}{dt} < 0$), pues $I(t) = I_0 e^{-t/\tau}$ decae. | Para $t < 0$: $\varepsilon = 0$.<br>Para $t \ge 0$: $\varepsilon > 0$ (en sentido +). | Para $t < 0$: ninguna.<br>Para $t \ge 0$: $\vec{B}_{\text{ind}} = \odot$ (saliente, apoya al campo saliente externo en caída). | Para $t < 0$: **Sin fem**.<br>Para $t \ge 0$: **Antihorario** *(razonado a mano)* | La espira central busca contrarrestar la pérdida de flujo saliente inyectando líneas de campo propias en el mismo sentido original ($+\hat{k}$). |

---

### 12.3. Aspectos Conceptuales Razonados a Mano
1. **Cocina de inducción (Pauta C3 Conceptual):**
   - El fondo ferromagnético del sartén de acero concentra las líneas de campo alterno de alta frecuencia y disipa calor mediante corrientes de Foucault (efecto Joule $I^2 R$) y pérdidas por histéresis del ciclo ferromagnético. En contraste, la greda (cerámica dieléctrica) carece de electrones libres ($\rho \to \infty$), por lo que no se generan corrientes inducidas y no hay calentamiento apreciable.
2. **Aproximación de modelo escalonado vs. efecto pelicular continuo (Pauta C3 P1):**
   - En régimen senoidal real, la densidad de corriente decae exponencialmente desde la superficie hacia el eje según $J(r) \approx J_s e^{-(R-r)/\delta}$ con profundidad de penetración $\delta = \sqrt{2/(\omega \mu \sigma)}$. La pauta adopta un modelo escalonado discreto de dos capas concéntricas ($J_0$ y $3J_0$) para hacer el problema analíticamente soluble en el certamen sin recurrir a funciones de Bessel de orden cero.
3. **Efectos de borde en inductancia mutua:**
   - La fórmula $M = \mu_0 n N \pi a^2$ asume que el solenoide es infinitamente largo respecto a su diámetro ($l \gg 2a$). Para bobinas cortas, el factor de desmagnetización reduce el campo axial en los extremos a la mitad ($B_{borde} \approx \frac{1}{2}B_{centro}$), provocando un coeficiente de acoplamiento magnético $k < 1$.

---

## 13. ERRORES ENCONTRADOS Y CORREGIDOS

1. **Rotulación de Simulacro P2 vs. Ejercicio Original de Arco y Segmento:**
   - *Error anterior:* En el Módulo 1 y versiones iniciales de las notas, el ejercicio de superposición de arco circular y segmento rectilíneo finito estaba rotulado como "Problema 2 Simulacros C3 UTFSM".
   - *Corrección:* El verdadero Problema 2 del simulacro oficial es la espira rectangular que se aleja con velocidad constante $v$ de un cable infinito con corriente. Se reclasificó el ejercicio del arco y segmento como `Ejercicio original (no oficial)` y se ubicó el Problema 2 oficial en el Módulo 4 (`m4_ex7`) y en el Módulo 11 (`m11_prob2`).

2. **Geometría de Bobinas Concéntricas en Ayudantía 11 P1:**
   - *Error anterior:* Se modelaba como dos espiras planas en un mismo plano mediante aproximación de campo central.
   - *Corrección:* El enunciado oficial especifica "dos espiras ideales concéntricas muy largas" (solenoides ideales concéntricos de longitud $l$). Se corrigió la deducción rigurosa del flujo concatenado $\phi_1 = \mu_0 \frac{N_i}{l}\pi R^2 I$ y la inductancia mutua $M = \mu_0 \frac{N_i N_e \pi R^2}{l}$ en el Módulo 6 (`m6_ex5`) y en las notas de revisión.

3. **Geometría de la Pequeña Espira Central en Ayudantía 10 P2 vs Pauta C3 P2:**
   - *Error anterior:* Se mezclaban en un solo ejercicio la espira central cuadrada de Ayudantía 10 P2 y la espira circular con corriente constante previa $t < 0$ de Pauta C3 P2.
   - *Corrección:* Se separaron explícitamente: en Módulo 4 (`m4_ex6`) se modela fielmente la espira cuadrada de lado $a \ll R$ con $A = a^2$ de la Ayudantía 10 P2, y en Módulo 6 (`m6_ex7c`) se incorporó el problema completo de la Pauta C3 2026-1 P2 (rollo plano de $N$ vueltas con espira circular de radio $r \ll R$ y corriente $I(t)$ para $t < 0$ y $t \ge 0$).

4. **Incorporación de la Espira Inclinada en Ángulo $\alpha$ (Ayudantía 11 P4):**
   - *Error anterior:* No existía un ejercicio interactivo específico para la bobina larga con espira inclinada en ángulo $\alpha$ respecto al eje longitudinal.
   - *Corrección:* Se creó `m6_ex7b` en el Módulo 6 con la deducción analítica de $M = \mu_0 n \pi b^2 \cos\alpha$ y la fem inducida correspondiente.

5. **Explicitud en Convenciones de Vector Normal y Signo en Faraday-Lenz:**
   - *Error anterior:* Varias soluciones calculaban directamente $|\varepsilon| = d\phi/dt$ sin explicitar el vector normal $\hat{n}$, el signo algebraico de $\varepsilon$ ni el sentido de circulación asociado.
   - *Corrección:* Se explicitó en todos los problemas de Faraday-Lenz el vector normal elegido, el sentido positivo de circulación por regla de la mano derecha, el signo de $\varepsilon = -d\phi/dt$ y la justificación física de Lenz.

6. **Escapes de Caracteres en Strings de JavaScript y KaTeX:**
   - *Error anterior:* Caracteres como `\frac`, `\odot`, `\otimes`, `\varepsilon`, `\pm`, `\vec`, `\Omega` dentro de template literals de JavaScript se escribían con barra simple, provocando que JS los interpretara como secuencias de escape nativas (`\f` form-feed, `\v` vertical tab), generando errores de renderizado de KaTeX (ej. 2 errores en Módulo 4).
   - *Corrección:* Se estandarizó el doble escape `\\frac`, `\\odot`, `\\otimes`, `\\varepsilon`, `\\pm`, `\\vec`, `\\Omega` en todos los archivos de datos JS, logrando 0 errores de KaTeX en los 12 módulos.
