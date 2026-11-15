/**
 * MÓDULO 11: SIMULACRO FINAL COMPLETO CERTAMEN 3
 * FIS120 / FIS12125 · UTFSM
 */

const MODULE_DATA_MOD11 = {
  number: '11',
  title: 'SIMULACRO FINAL CERTAMEN 3',
  description: 'Certamen 3 completo cronometrado (2026-2) en formato oficial UTFSM: 3 problemas analíticos de 30 puntos cada uno + 1 pregunta conceptual de 10 puntos (Total: 100 puntos), con rúbrica detallada y autoevaluación.',
  hasInteractive: false,
  theory: `
    <div class="exam-timer-bar">
      <div>
        <strong>⏱️ Temporizador de Certamen Oficial:</strong><br>
        <span style="font-size: 0.85rem; color: var(--text-muted);">Tiempo sugerido UTFSM: 90 minutos.</span>
      </div>
      <div style="display: flex; align-items: center; gap: 0.8rem;">
        <span class="timer-clock" id="exam-timer-display">90:00</span>
        <button class="btn btn-sm btn-primary" id="btn-timer-toggle" onclick="MODULE_DATA_MOD11.toggleTimer()">Iniciar</button>
        <button class="btn btn-sm" onclick="MODULE_DATA_MOD11.resetTimer()">Reiniciar</button>
      </div>
    </div>

    <div class="box-note">
      <strong>Instrucciones Oficiales Certamen 3 FIS120/121:</strong><br>
      • Certamen de carácter individual, sin préstamos y sin consultas.<br>
      • Cada problema consta de 3 incisos de 10 puntos cada uno (30 pts por problema). La pregunta conceptual vale 10 puntos en total. Total certamen: 100 puntos.<br>
      • Tienes disponible el <strong>Formulario Oficial</strong> en cualquier momento abriendo el botón <em>"📋 Formulario"</em> en la barra superior.<br>
      • Al terminar cada inciso, despliega su solución modelo oficial y asígnate tu puntaje en el selector de autoevaluación para obtener tu nota estimada.
    </div>

    <div id="exam-score-summary" class="box-method" style="display: flex; justify-content: space-between; align-items: center; margin-top: 1rem;">
      <div>
        <strong>Puntaje Total Acumulado:</strong> <span id="user-total-score" style="font-size: 1.3rem; font-weight: bold; color: var(--accent);">0</span> / 100 puntos
      </div>
      <div>
        <strong>Nota Estimada UTFSM:</strong> <span id="user-estimated-grade" style="font-size: 1.3rem; font-weight: bold; color: var(--accent);">10</span> / 100
      </div>
    </div>
  `,
  timerInterval: null,
  timeLeft: 90 * 60,
  timerRunning: false,

  toggleTimer() {
    const btn = document.getElementById('btn-timer-toggle');
    if (this.timerRunning) {
      clearInterval(this.timerInterval);
      this.timerRunning = false;
      if (btn) btn.textContent = 'Reanudar';
    } else {
      this.timerRunning = true;
      if (btn) btn.textContent = 'Pausar';
      this.timerInterval = setInterval(() => {
        if (this.timeLeft > 0) {
          this.timeLeft--;
          this.updateTimerDisplay();
        } else {
          clearInterval(this.timerInterval);
          this.timerRunning = false;
          alert('¡Tiempo de certamen concluido! Procede a autoevaluar tus respuestas.');
        }
      }, 1000);
    }
  },

  resetTimer() {
    clearInterval(this.timerInterval);
    this.timerRunning = false;
    this.timeLeft = 90 * 60;
    const btn = document.getElementById('btn-timer-toggle');
    if (btn) btn.textContent = 'Iniciar';
    this.updateTimerDisplay();
  },

  updateTimerDisplay() {
    const display = document.getElementById('exam-timer-display');
    if (!display) return;
    const mins = Math.floor(this.timeLeft / 60);
    const secs = this.timeLeft % 60;
    display.textContent = `${mins.toString().padStart(2, '0')}:${secs.toString().padStart(2, '0')}`;
  },

  updateScore() {
    let total = 0;
    const scores = JSON.parse(localStorage.getItem('fis120_exam_scores') || '{}');
    for (const key in scores) {
      total += Number(scores[key] || 0);
    }
    const scoreEl = document.getElementById('user-total-score');
    const gradeEl = document.getElementById('user-estimated-grade');
    if (scoreEl) scoreEl.textContent = total;
    if (gradeEl) {
      // Escala estándar chilena de certamen (0 a 100)
      gradeEl.textContent = total;
    }
  },

  setScore(subproblemId, pts) {
    const scores = JSON.parse(localStorage.getItem('fis120_exam_scores') || '{}');
    scores[subproblemId] = pts;
    localStorage.setItem('fis120_exam_scores', JSON.stringify(scores));
    this.updateScore();
  },

  exercises: [
    {
      id: 'm11_prob1',
      title: 'Problema 1: Toroide Ideal Rectangular y Cable Axial (30 Puntos)',
      level: 'certamen',
      source: 'Simulacro Certamen 3 2026-2',
      type: 'step_by_step',
      figure: 'img/mod3_toroid_simulacro.svg',
      figureCaption: 'Toroide rectangular de $N$ vueltas y cable axial morado con corriente $I_c$.',
      statement: `
        Un toroide ideal de sección rectangular, con radio interior $a$, radio exterior $b$ y altura $h$, está formado por $N$ vueltas de alambre por las que circula una corriente $I$. El arrollamiento es tal que el campo en el interior apunta en sentido antihorario visto desde arriba ($+\\hat{\\phi}$).<br><br>
        <strong>a) (10 pts)</strong> Utilizando la ley de Ampère, determine el vector campo magnético $\\vec{B}$ en todo el espacio ($r < a$, $a < r < b$ y $r > b$). Justifique la elección del lazo amperiano.<br>
        <strong>b) (10 pts)</strong> Calcule el flujo magnético $\\Phi_1$ a través de una vuelta del toroide (su sección rectangular) y el flujo total enlazado por las $N$ vueltas.<br>
        <strong>c) (10 pts)</strong> Por el eje del toroide pasa un cable recto infinito con corriente $I_c$ hacia $+z$. Determine la inductancia mutua $M$ entre el cable y el toroide.
      `,
      steps: [
        {
          title: 'Paso 1: Solución Oficial Inciso a (10 Puntos) - Campo en todo el espacio',
          content: `
            <strong>1. Elección de lazo y simetría:</strong> Por simetría axial alrededor del eje $z$, $\\vec{B} = B(r)\\,\\hat{\\phi}$. Escogemos un lazo amperiano circular $\\Gamma$ de radio $r$ concéntrico con el eje $z$.<br>
            $$\\oint_\\Gamma \\vec{B} \\cdot d\\vec{l} = B(r) 2\\pi r$$
            <strong>2. Regiones:</strong><br>
            • $r < a$: $I_{enl} = 0 \\implies \\vec{B} = \\vec{0}$.<br>
            • $a < r < b$: El lazo enlaza las $N$ vueltas interiores, cada una con corriente $I$:
            $$I_{enl} = N I \\implies B(r) 2\\pi r = \\mu_0 N I \\implies \\vec{B}(r) = \\frac{\\mu_0 N I}{2\\pi r}\\,\\hat{\\phi}$$
            • $r > b$: Cada vuelta entra y sale de la superficie encerrada $\\implies I_{enl} = N I - N I = 0 \\implies \\vec{B} = \\vec{0}$.<br><br>
            <div style="margin-top: 0.5rem; font-size: 0.9rem;">
              <strong>Autocalificación Inciso a:</strong>
              <select onchange="MODULE_DATA_MOD11.setScore('p1_a', this.value)" class="input-number" style="max-width: 140px;">
                <option value="0">0 pts</option>
                <option value="3">3 pts (Planteamiento)</option>
                <option value="7">7 pts (B en interior)</option>
                <option value="10" selected>10 pts (Pauta completa)</option>
              </select>
            </div>
          `
        },
        {
          title: 'Paso 2: Solución Oficial Inciso b (10 Puntos) - Flujo magnético',
          content: `
            La sección transversal rectangular tiene base $dr$ y altura $h$, con $dA = h\\,dr$.<br>
            El flujo magnético a través de <strong>una sola espira rectangular</strong> es:
            $$\\Phi_1 = \\int_a^b B(r)\\, h\\,dr = \\int_a^b \\left( \\frac{\\mu_0 N I}{2\\pi r} \\right) h\\,dr = \\frac{\\mu_0 N I h}{2\\pi} \\int_a^b \\frac{dr}{r} = \\frac{\\mu_0 N I h}{2\\pi} \\ln\\left(\\frac{b}{a}\\right)$$
            El flujo total enlazado por las $N$ vueltas completas del toroide es:
            $$\\Phi_{total} = N \\Phi_1 = \\frac{\\mu_0 N^2 I h}{2\\pi} \\ln\\left(\\frac{b}{a}\\right)$$
            <div style="margin-top: 0.5rem; font-size: 0.9rem;">
              <strong>Autocalificación Inciso b:</strong>
              <select onchange="MODULE_DATA_MOD11.setScore('p1_b', this.value)" class="input-number" style="max-width: 140px;">
                <option value="0">0 pts</option>
                <option value="4">4 pts (Integral de flujo)</option>
                <option value="7">7 pts (Phi_1 correcto)</option>
                <option value="10" selected>10 pts (Total con factor N^2)</option>
              </select>
            </div>
          `
        },
        {
          title: 'Paso 3: Solución Oficial Inciso c (10 Puntos) - Inductancia mutua cable-toroide',
          content: `
            <strong>Método 1 (Directo):</strong> El cable axial transporta corriente $I_c$ en $+z$. Su campo a distancia $r$ es:
            $$\\vec{B}_{cable}(r) = \\frac{\\mu_0 I_c}{2\\pi r}\\,\\hat{\\phi}$$
            El flujo de este campo a través de una espira rectangular del toroide es:
            $$\\phi_{c1} = \\int_a^b \\frac{\\mu_0 I_c}{2\\pi r} h\\,dr = \\frac{\\mu_0 I_c h}{2\\pi} \\ln\\left(\\frac{b}{a}\\right)$$
            El flujo total a través de las $N$ espiras del toroide es:
            $$\\Phi_{mutuo} = N \\phi_{c1} = \\frac{\\mu_0 N I_c h}{2\\pi} \\ln\\left(\\frac{b}{a}\\right)$$
            Por la definición de inductancia mutua $M = \\frac{\\Phi_{mutuo}}{I_c}$:
            $$M = \\frac{\\mu_0 N h}{2\\pi} \\ln\\left(\\frac{b}{a}\\right)$$
            <strong>Método 2 (Por Reciprocidad):</strong> A partir del campo del toroide, el flujo enlazado por el cable axial cerrado en el infinito da idéntico resultado.<br><br>
            <div style="margin-top: 0.5rem; font-size: 0.9rem;">
              <strong>Autocalificación Inciso c:</strong>
              <select onchange="MODULE_DATA_MOD11.setScore('p1_c', this.value)" class="input-number" style="max-width: 140px;">
                <option value="0">0 pts</option>
                <option value="4">4 pts (Planteamiento)</option>
                <option value="7">7 pts (Flujo correcto)</option>
                <option value="10" selected>10 pts (M simplificado y verificado)</option>
              </select>
            </div>
          `
        }
      ]
    },
    {
      id: 'm11_prob2',
      title: 'Problema 2: Espira Rectangular Alejándose de Cable Infinito (30 Puntos)',
      level: 'certamen',
      source: 'Simulacro Certamen 3 2026-2',
      type: 'step_by_step',
      figure: 'img/mod4_faraday_moving_loop.svg',
      figureCaption: 'Espira rectangular alejándose con $\\vec{v} = v\\hat{\\imath}$ en el plano $xy$.',
      statement: `
        Un cable recto infinito sobre el eje $y$ transporta corriente constante $I$ en sentido $+y$. Una espira rectangular conductora de lados $a$ (en $x$) y $b$ (en $y$) y resistencia $R$ se aleja del cable con velocidad constante $\\vec{v} = v\\hat{\\imath}$. En $t=0$ su lado más cercano está a distancia $d_0$, por lo que $d(t) = d_0 + vt$.<br><br>
        <strong>a) (10 pts)</strong> Usando la ley de Ampère, determine el campo magnético del cable a una distancia $x$ y el flujo magnético $\\phi_B(t)$ a través de la espira. Indique el vector normal escogido.<br>
        <strong>b) (10 pts)</strong> Determine la fem inducida $\\varepsilon_{ind}(t)$ en la espira.<br>
        <strong>c) (10 pts)</strong> Indique el sentido de la corriente inducida fundamentado con la ley de Lenz y determine su magnitud $I_{ind}(t)$.
      `,
      steps: [
        {
          title: 'Paso 1: Solución Oficial Inciso a (10 Puntos) - Campo y Flujo',
          content: `
            1. Por Ampère, para un cable infinito sobre el eje $y$ con corriente en $+\\hat{\\jmath}$:
            $$\\vec{B}(x) = -\\frac{\\mu_0 I}{2\\pi x}\\,\\hat{k} \\quad (\\text{entra a la página } \\otimes)$$
            2. Escogemos el vector normal hacia adentro: $\\hat{n} = -\\hat{k}$, con $d\\vec{A} = b\\,dx(-\\hat{k})$.<br>
            3. Flujo magnético integrando desde $x = d(t)$ hasta $x = d(t) + a$:
            $$\\phi_B(t) = \\int_{d(t)}^{d(t)+a} \\frac{\\mu_0 I}{2\\pi x} b\\,dx = \\frac{\\mu_0 I b}{2\\pi} \\ln\\left(\\frac{d(t)+a}{d(t)}\\right) = \\frac{\\mu_0 I b}{2\\pi} \\ln\\left(1 + \\frac{a}{d_0 + vt}\\right)$$
            <div style="margin-top: 0.5rem; font-size: 0.9rem;">
              <strong>Autocalificación Inciso a:</strong>
              <select onchange="MODULE_DATA_MOD11.setScore('p2_a', this.value)" class="input-number" style="max-width: 140px;">
                <option value="0">0 pts</option>
                <option value="3">3 pts (B del cable)</option>
                <option value="7">7 pts (Planteamiento integral)</option>
                <option value="10" selected>10 pts (Flujo logarítmico con normal)</option>
              </select>
            </div>
          `
        },
        {
          title: 'Paso 2: Solución Oficial Inciso b (10 Puntos) - fem Inducida',
          content: `
            Aplicando la Ley de Faraday $\\varepsilon_{ind} = -\\frac{d\\phi_B}{dt}$ y regla de la cadena con $\\frac{d}{dt}d(t) = v$:
            $$\\frac{d\\phi_B}{dt} = \\frac{\\mu_0 I b}{2\\pi} \\frac{d}{dt} \\left[ \\ln(d(t)+a) - \\ln(d(t)) \\right] = \\frac{\\mu_0 I b}{2\\pi} \\left( \\frac{v}{d(t)+a} - \\frac{v}{d(t)} \\right) = \\frac{\\mu_0 I b v}{2\\pi} \\left( \\frac{-a}{d(t)(d(t)+a)} \\right)$$
            Por lo tanto:
            $$\\varepsilon_{ind}(t) = -\\frac{d\\phi_B}{dt} = \\frac{\\mu_0 I b v a}{2\\pi (d_0 + vt)(d_0 + vt + a)}$$
            <div style="margin-top: 0.5rem; font-size: 0.9rem;">
              <strong>Autocalificación Inciso b:</strong>
              <select onchange="MODULE_DATA_MOD11.setScore('p2_b', this.value)" class="input-number" style="max-width: 140px;">
                <option value="0">0 pts</option>
                <option value="4">4 pts (Derivada planteada)</option>
                <option value="7">7 pts (Regla de la cadena)</option>
                <option value="10" selected>10 pts (fem simplificada exacta)</option>
              </select>
            </div>
          `
        },
        {
          title: 'Paso 3: Solución Oficial Inciso c (10 Puntos) - Sentido de Lenz y Corriente',
          content: `
            <strong>Fundamentación física según Lenz:</strong><br>
            A medida que la espira se mueve hacia la derecha con velocidad $v\\hat{\\imath}$, la distancia al cable aumenta, por lo que el campo magnético entrante ($\\otimes$) es cada vez más débil y el flujo entrante $\\phi_B(t)$ disminuye.<br>
            De acuerdo con la Ley de Lenz, la corriente inducida debe oponerse a esta disminución de flujo generando su propio campo magnético inducido en el <strong>mismo sentido del campo original</strong> (hacia adentro de la página $\\otimes$).<br>
            Por regla de la mano derecha, para generar campo entrante, la corriente inducida debe circular en <strong>sentido horario</strong>.<br>
            Por Ley de Ohm:
            $$I_{ind}(t) = \\frac{\\varepsilon_{ind}(t)}{R} = \\frac{\\mu_0 I b v a}{2\\pi R (d_0 + vt)(d_0 + vt + a)}$$
            <div style="margin-top: 0.5rem; font-size: 0.9rem;">
              <strong>Autocalificación Inciso c:</strong>
              <select onchange="MODULE_DATA_MOD11.setScore('p2_c', this.value)" class="input-number" style="max-width: 140px;">
                <option value="0">0 pts</option>
                <option value="4">4 pts (Solo sentido horario sin justificar)</option>
                <option value="7">7 pts (Justificación Lenz)</option>
                <option value="10" selected>10 pts (Justificación + corriente Ohm)</option>
              </select>
            </div>
          `
        }
      ]
    },
    {
      id: 'm11_prob3',
      title: 'Problema 3: Solenoide Ideal y Bobina Cuadrada (30 Puntos)',
      level: 'certamen',
      source: 'Simulacro Certamen 3 2026-2',
      type: 'step_by_step',
      figure: 'img/mod6_mutual_solenoid_square.svg',
      figureCaption: 'Solenoide coaxial de radio $a$ y bobina cuadrada de $N$ espiras de lado $L > 2a$.',
      statement: `
        Un solenoide ideal muy largo de radio $a$ y $n$ vueltas por unidad de longitud transporta una corriente $I(t)$ que vista de frente circula antihoraria. Rodeando al solenoide hay una bobina de $N$ espiras cuadradas de lado $L > 2a$, coaxial con él.<br><br>
        <strong>a) (10 pts)</strong> Determine la inductancia mutua $M$ entre el solenoide y la bobina cuadrada.<br>
        <strong>b) (10 pts)</strong> La corriente en el solenoide varía según $I(t) = I_0(1 - e^{-t/\\tau})$. Determine la fem inducida en la bobina cuadrada y su sentido por Lenz.<br>
        <strong>c) (10 pts)</strong> El solenoide se desconecta y por la bobina cuadrada circula $I_2(t) = \\alpha t$. Sin calcular el campo de la bobina, determine la fem inducida en el solenoide justificando mediante reciprocidad. ¿Depende este resultado de $L$?
      `,
      steps: [
        {
          title: 'Paso 1: Solución Oficial Inciso a (10 Puntos) - Inductancia mutua',
          content: `
            El solenoide ideal produce un campo magnético uniforme en su interior:
            $$B = \\mu_0 n I_1$$
            y cero fuera ($r > a$).<br>
            Como $L > 2a$, la bobina cuadrada encierra completamente toda la sección circular del solenoide. El flujo que atraviesa cada vuelta de la bobina cuadrada proviene únicamente del área con campo:
            $$\\phi_{12} = B \\cdot (\\pi a^2) = (\\mu_0 n I_1) (\\pi a^2)$$
            Para las $N$ espiras de la bobina cuadrada:
            $$\\Phi_{total} = N \\phi_{12} = \\mu_0 n N \\pi a^2 I_1$$
            Por tanto:
            $$M = \\frac{\\Phi_{total}}{I_1} = \\mu_0 n N \\pi a^2$$
            <div style="margin-top: 0.5rem; font-size: 0.9rem;">
              <strong>Autocalificación Inciso a:</strong>
              <select onchange="MODULE_DATA_MOD11.setScore('p3_a', this.value)" class="input-number" style="max-width: 140px;">
                <option value="0">0 pts</option>
                <option value="4">4 pts (Flujo circular pi a^2)</option>
                <option value="7">7 pts (Multiplicar por N)</option>
                <option value="10" selected>10 pts (M exacto)</option>
              </select>
            </div>
          `
        },
        {
          title: 'Paso 2: Solución Oficial Inciso b (10 Puntos) - fem con corriente exponencial',
          content: `
            Derivamos la corriente $I_1(t) = I_0(1 - e^{-t/\\tau})$:
            $$\\frac{dI_1}{dt} = \\frac{I_0}{\\tau} e^{-t/\\tau}$$
            La fem inducida en la bobina cuadrada es:
            $$\\varepsilon_2(t) = -M \\frac{dI_1}{dt} = -\\frac{\\mu_0 n N \\pi a^2 I_0}{\\tau} e^{-t/\\tau}$$
            Su magnitud es:
            $$|\\varepsilon_2(t)| = \\frac{\\mu_0 n N \\pi a^2 I_0}{\\tau} e^{-t/\\tau}$$
            <strong>Sentido por Lenz:</strong> Como la corriente $I_1$ crece con el tiempo, el flujo saliente $\\odot$ aumenta. La bobina cuadrada se opone generando campo entrante $\\otimes$, lo que corresponde a <strong>sentido horario</strong>.
            <div style="margin-top: 0.5rem; font-size: 0.9rem;">
              <strong>Autocalificación Inciso b:</strong>
              <select onchange="MODULE_DATA_MOD11.setScore('p3_b', this.value)" class="input-number" style="max-width: 140px;">
                <option value="0">0 pts</option>
                <option value="4">4 pts (Derivada de I(t))</option>
                <option value="7">7 pts (Magnitud fem)</option>
                <option value="10" selected>10 pts (fem + sentido de Lenz)</option>
              </select>
            </div>
          `
        },
        {
          title: 'Paso 3: Solución Oficial Inciso c (10 Puntos) - Reciprocidad y dependencia de L',
          content: `
            Por el <strong>Teorema de Reciprocidad</strong>, la inductancia mutua entre dos circuitos es simétrica:
            $$M_{12} = M_{21} = M = \\mu_0 n N \\pi a^2$$
            La fem inducida en el solenoide cuando circula $I_2(t) = \\alpha t$ en la bobina cuadrada es:
            $$|\\varepsilon_{solenoide}| = M \\left|\\frac{dI_2}{dt}\\right| = (\\mu_0 n N \\pi a^2) \\frac{d}{dt}(\\alpha t) = \\mu_0 n N \\pi a^2 \\alpha$$
            <strong>¿Depende de L?</strong><br>
            <strong>NO depende de $L$</strong>. Físicamente, el campo magnético generado por el solenoide está estrictamente confinado dentro del radio $a$ y es nulo en el exterior ($r > a$). Cualquier flujo enlazado entre ambos circuitos ocurre exclusivamente dentro del cilindro de radio $a$. Mientras $L > 2a$, aumentar el tamaño de la bobina cuadrada solo añade área vacía sin campo magnético.
            <div style="margin-top: 0.5rem; font-size: 0.9rem;">
              <strong>Autocalificación Inciso c:</strong>
              <select onchange="MODULE_DATA_MOD11.setScore('p3_c', this.value)" class="input-number" style="max-width: 140px;">
                <option value="0">0 pts</option>
                <option value="4">4 pts (Uso de reciprocidad)</option>
                <option value="7">7 pts (fem = mu0 n N pi a^2 alpha)</option>
                <option value="10" selected>10 pts (Justificación física de no dependencia de L)</option>
              </select>
            </div>
          `
        }
      ]
    },
    {
      id: 'm11_prob4_conceptual',
      title: 'Pregunta Conceptual: Ecuaciones de Maxwell y Condensador (10 Puntos)',
      level: 'certamen',
      source: 'Simulacro Certamen 3 2026-2',
      type: 'step_by_step',
      figure: 'img/mod10_maxwell_capacitor.svg',
      figureCaption: 'Condensador circular cargado por corriente $I(t)$ con lazo $\\Gamma$ y superficies $S_1, S_2$.',
      statement: `
        Un condensador de placas paralelas circulares de radio $R$ se carga mediante una corriente de conducción $I(t)$. Se desprecian efectos de borde.<br><br>
        <strong>a) (4 pts)</strong> Escriba las cuatro ecuaciones de Maxwell en forma integral (en el vacío con fuentes) y explique en una frase qué establece cada una.<br>
        <strong>b) (3 pts)</strong> Aplique la ley de Ampère sin el término de Maxwell al lazo $\\Gamma$, primero usando la superficie $S_1$ y luego la $S_2$. ¿Qué contradicción aparece? ¿Cómo la resuelve la ecuación de Ampère-Maxwell?<br>
        <strong>c) (3 pts)</strong> Entre las placas, calcule el campo magnético a una distancia radial $r < R$ del eje en función de $I(t), r$ y $R$.
      `,
      steps: [
        {
          title: 'Paso 1: Solución Oficial Inciso a (4 Puntos) - Las 4 Ecuaciones de Maxwell',
          content: `
            1. $\\oiint \\vec{E}\\cdot d\\vec{A} = \\frac{Q_{enc}}{\\varepsilon_0}$: El flujo eléctrico a través de una superficie cerrada es proporcional a la carga eléctrica neta encerrada.<br>
            2. $\\oiint \\vec{B}\\cdot d\\vec{A} = 0$: No existen monopolos magnéticos aislados en la naturaleza; las líneas de $\\vec{B}$ siempre forman curvas cerradas.<br>
            3. $\\oint \\vec{E}\\cdot d\\vec{l} = -\\frac{d\\phi_B}{dt}$: Un flujo magnético variable en el tiempo engendra un campo eléctrico no conservativo.<br>
            4. $\\oint \\vec{B}\\cdot d\\vec{l} = \\mu_0 I_{cond} + \\mu_0 \\varepsilon_0 \\frac{d\\phi_E}{dt}$: El campo magnético es generado tanto por corrientes de conducción de cargas libres como por campos eléctricos variables en el tiempo.
            <div style="margin-top: 0.5rem; font-size: 0.9rem;">
              <strong>Autocalificación Inciso a:</strong>
              <select onchange="MODULE_DATA_MOD11.setScore('p4_a', this.value)" class="input-number" style="max-width: 140px;">
                <option value="0">0 pts</option>
                <option value="2">2 pts (2 ecuaciones)</option>
                <option value="4" selected>4 pts (4 ecuaciones con frases completas)</option>
              </select>
            </div>
          `
        },
        {
          title: 'Paso 2: Solución Oficial Inciso b (3 Puntos) - Paradoja del Condensador',
          content: `
            • Con la superficie plana $S_1$: el cable conductor la cruza transportando corriente de conducción $\\implies \\oint_\\Gamma \\vec{B}\\cdot d\\vec{l} = \\mu_0 I(t)$.<br>
            • Con la superficie abombada $S_2$: pasa entre las placas sin tocar el alambre, por lo que $I_{cond} = 0 \\implies \\oint_\\Gamma \\vec{B}\\cdot d\\vec{l} = 0$.<br>
            <strong>Contradicción:</strong> Para el mismo lazo $\\Gamma$, la circulación magnética tendría dos valores incompatibles ($\\mu_0 I(t) \\neq 0$).<br>
            <strong>Resolución de Ampère-Maxwell:</strong> Entre las placas el campo eléctrico varía al acumularse carga, generando un flujo eléctrico $\\phi_E = Q(t)/\\varepsilon_0$. La corriente de desplazamiento a través de $S_2$ es $I_d = \\varepsilon_0 \\frac{d\\phi_E}{dt} = \\frac{dQ}{dt} = I(t)$. Con el término $\\mu_0 I_d$, la integral sobre $S_2$ resulta exactamente igual a $\\mu_0 I(t)$, restaurando la unicidad.
            <div style="margin-top: 0.5rem; font-size: 0.9rem;">
              <strong>Autocalificación Inciso b:</strong>
              <select onchange="MODULE_DATA_MOD11.setScore('p4_b', this.value)" class="input-number" style="max-width: 140px;">
                <option value="0">0 pts</option>
                <option value="1">1 pt (Plantea contradicción)</option>
                <option value="3" selected>3 pts (Contradicción + deducción de I_d)</option>
              </select>
            </div>
          `
        },
        {
          title: 'Paso 3: Solución Oficial Inciso c (3 Puntos) - Campo B(r) para r < R',
          content: `
            Para un lazo circular de radio $r < R$ concéntrico entre las placas:<br>
            $$\\oint_\\Gamma \\vec{B}\\cdot d\\vec{l} = B(r) 2\\pi r = \\mu_0 I_{d, enl}(r)$$
            Como el campo eléctrico es uniforme en el disco de radio $R$, la fracción de corriente de desplazamiento encerrada en el radio $r$ es la razón de áreas:
            $$I_{d, enl}(r) = I(t) \\frac{\\pi r^2}{\\pi R^2} = I(t) \\frac{r^2}{R^2}$$
            Igualando:
            $$B(r) 2\\pi r = \\mu_0 I(t) \\frac{r^2}{R^2} \\implies B(r) = \\frac{\\mu_0 I(t) r}{2\\pi R^2}$$
            <div style="margin-top: 0.5rem; font-size: 0.9rem;">
              <strong>Autocalificación Inciso c:</strong>
              <select onchange="MODULE_DATA_MOD11.setScore('p4_c', this.value)" class="input-number" style="max-width: 140px;">
                <option value="0">0 pts</option>
                <option value="1">1 pt (Fracción de área)</option>
                <option value="3" selected>3 pts (B(r) despejado con mu0 I r / 2 pi R^2)</option>
              </select>
            </div>
          `
        }
      ]
    }
  ]
};
