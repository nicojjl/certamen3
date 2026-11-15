/**
 * MÓDULO 4: FLUJO MAGNÉTICO Y LEY DE FARADAY-LENZ
 * FIS120 / FIS12125 · UTFSM
 */

window.MODULE_DATA_MOD4 = {
  number: '4',
  title: 'Flujo Magnético y Ley de Faraday-Lenz',
  description: 'Cálculo riguroso de flujo magnético en campos no homogéneos, fuerza electromotriz inducida, sentido de circulación por la Ley de Lenz y principio de conservación de energía.',
  hasInteractive: false,
  theory: `
    <p>
      La inducción electromagnética es el principio central sobre el cual descansan los generadores, motores y transformadores modernos. Michael Faraday descubrió que cualquier variación temporal en el flujo magnético que atraviesa un circuito cerrado induce en él una fuerza electromotriz (fem). Heinrich Lenz formalizó la dirección de dicha fem.
    </p>

    <div class="box-formula">
      <strong>1. Definiciones Fundamentales (Formulario C3):</strong>
      <p>
        • <strong>Flujo Magnético:</strong>
        $$\\phi_B = \\iint_S \\vec{B} \\cdot d\\vec{A} = \\iint_S |\\vec{B}| \\cos\\theta\\,dA$$
        • <strong>Ley de Faraday-Lenz:</strong>
        $$\\varepsilon_{ind} = \\oint_\\Gamma \\vec{E}_{ind} \\cdot d\\vec{l} = -\\frac{d\\phi_B}{dt}$$
        • <strong>Ley de Ohm para Corriente Inducida:</strong>
        $$I_{ind}(t) = \\frac{|\\varepsilon_{ind}(t)|}{R}$$
      </p>
    </div>

    <div class="figure-container">
      <img src="img/mod4_faraday_moving_loop.svg" alt="Espira alejándose de cable">
      <div class="figure-caption">Espira rectangular alejándose de un cable recto infinito (Simulacro C3 P2): el flujo entrante disminuye, induciendo corriente horaria.</div>
    </div>

    <div class="box-method">
      <strong>2. Cómo Determinar el Sentido de Lenz Sin Equivocarse:</strong>
      <ol style="padding-left: 1.2rem; margin-top: 0.5rem;">
        <li><strong>Identifica el campo original $\\vec{B}_{ext}$:</strong> ¿Entra ($\otimes$) o sale ($\odot$) del plano de la espira?</li>
        <li><strong>Analiza la tendencia del flujo $\\phi_B(t)$ con el tiempo:</strong>
          <br>• Si el flujo <em>aumenta</em> ($\frac{d\phi_B}{dt} > 0$), la espira <strong>se opone al incremento</strong> generando un campo inducido $\\vec{B}_{ind}$ en sentido <em>contrario</em> a $\\vec{B}_{ext}$.
          <br>• Si el flujo <em>disminuye</em> ($\frac{d\phi_B}{dt} < 0$), la espira <strong>se opone a la disminución</strong> generando un campo inducido $\\vec{B}_{ind}$ en el <em>mismo sentido</em> que $\\vec{B}_{ext}$ para reforzarlo.
        </li>
        <li><strong>Aplica la regla de la mano derecha:</strong> Apunta el pulgar en la dirección del campo inducido $\\vec{B}_{ind}$; los dedos que abrazan la espira indicarán el sentido de la corriente inducida $I_{ind}$ (horario o antihorario).</li>
      </ol>
    </div>

    <div class="box-warning">
      <strong>Errores Fatales en el Certamen:</strong><br>
      1. Confundir la dirección del campo existente con el cambio del flujo: la corriente inducida no se opone al campo magnético, se opone a su <em>VARIACIÓN TEMPORAL</em> ($d\\phi_B/dt$). Si un campo gigantesco es constante en el tiempo, $\\varepsilon_{ind} = 0$.<br>
      2. Olvidar que si el área o el ángulo cambian en el tiempo, también hay fem inducida, aunque $\\vec{B}$ sea espacial y temporalmente constante.
    </div>
  `,
  exercises: [
    {
      id: 'm4_ex1',
      title: 'fem con Flujo Armónico en el Tiempo',
      level: 'basic',
      source: 'Fundamentos de Inducción',
      type: 'multiple_choice',
      statement: `
        El flujo magnético a través de una bobina de $N = 50\\text{ vueltas}$ varía según la función $\\phi_B(t) = 0.040 \\cos(100\\pi t)\\text{ Wb}$. ¿Cuál es la magnitud máxima de la fem inducida en la bobina?
      `,
      options: [
        '$628.3\\text{ V}$',
        '$12.57\\text{ V}$',
        '$2.00\\text{ V}$',
        '$200.0\\text{ V}$'
      ],
      correctOption: 0,
      explanation: `
        Por la Ley de Faraday para $N$ espiras:
        $$\\varepsilon_{ind} = -N \\frac{d\\phi_B}{dt} = -50 \\cdot \\frac{d}{dt}\\left(0.040\\cos(100\\pi t)\\right) = -50 \\cdot (-0.040 \\cdot 100\\pi \\sin(100\\pi t)) = 200\\pi \\sin(100\\pi t)$$
        La amplitud máxima es:
        $$\\varepsilon_{\\max} = 200\\pi \\approx 628.32\\text{ V}$$
      `
    },
    {
      id: 'm4_ex2',
      title: 'fem Inducida en Espira Cuadrada con Campo Lineal',
      level: 'basic',
      source: 'Ejercicios de Clase UTFSM',
      type: 'numerical',
      statement: `
        Una espira cuadrada conductora de lado $L = 0.20\\text{ m}$ y resistencia $R = 4.0\\,\\Omega$ está orientada perpendicularmente a un campo magnético uniforme que disminuye a razón constante $\\frac{dB}{dt} = -0.50\\text{ T/s}$. Calcule la corriente inducida $I_{ind}$ en miliamperios (mA).
      `,
      placeholder: 'Ej: 5.0',
      units: 'mA',
      correctValue: 5.0,
      tolerance: 0.04,
      explanation: `
        El área de la espira es $A = L^2 = (0.20)^2 = 0.040\\text{ m}^2$.<br>
        Como el campo es perpendicular, $\\phi_B = B \\cdot A$.<br>
        $$|\\varepsilon_{ind}| = \\left| -\\frac{d\\phi_B}{dt} \\right| = A \\left|\\frac{dB}{dt}\\right| = 0.040\\text{ m}^2 \\cdot 0.50\\text{ T/s} = 0.020\\text{ V}$$
        Por Ley de Ohm:
        $$I_{ind} = \\frac{|\\varepsilon_{ind}|}{R} = \\frac{0.020\\text{ V}}{4.0\\,\\Omega} = 0.0050\\text{ A} = 5.0\\text{ mA}$$
      `
    },
    {
      id: 'm4_ex3',
      title: 'Aplicación Directa de la Regla de Lenz',
      level: 'intermediate',
      source: 'Preguntas Conceptuales FIS120',
      type: 'true_false',
      statement: `
        Si un campo magnético uniforme saliente del plano de la página ($\odot$) está disminuyendo con el tiempo, la corriente inducida en una espira en dicho plano circulará en sentido antihorario.
      `,
      correct: true,
      justification: `
        Verdadero. El campo saliente ($\odot$) está decreciendo en el tiempo. Por la Ley de Lenz, la corriente inducida se opone a esta disminución intentando mantener el flujo original; por ende, debe producir un campo inducido $\\vec{B}_{ind}$ que también apunte hacia afuera de la página ($\odot$). Por regla de la mano derecha, dedos curvados en sentido antihorario producen un campo saliente.
      `
    },
    {
      id: 'm4_ex4',
      title: 'Espira Cuadrada con Campo de Inclinación Rotatoria',
      level: 'certamen',
      source: 'Ayudantía 10 Problema 1',
      type: 'multiple_choice',
      statement: `
        Una espira cuadrada de lado $a$ situada en el plano $xy$ está bajo un campo de magnitud constante $B_0$ cuyo ángulo de elevación respecto al plano $xy$ varía según $\\phi(t) = k + \\omega t$. ¿Cuál es el valor máximo de la fem inducida $|\\varepsilon_{ind}|$?
      `,
      options: [
        '$B_0 a^2 \\omega$',
        '$B_0 a^2 \\omega / 2$',
        '$2 B_0 a^2 \\omega$',
        '$B_0 a \\omega^2$'
      ],
      correctOption: 0,
      explanation: `
        El vector normal a la espira en el plano $xy$ es $\\hat{n} = \\hat{k}$ (perpendicular al plano).<br>
        Si $\\phi(t)$ es el ángulo de elevación respecto al plano $xy$, la componente de $\\vec{B}$ perpendicular al plano es $B_z = B_0 \\sin(\\phi(t)) = B_0 \\sin(k + \\omega t)$.<br>
        El flujo magnético es:
        $$\\phi_B(t) = B_z \\cdot A = B_0 a^2 \\sin(k + \\omega t)$$
        La fem inducida es:
        $$\\varepsilon_{ind}(t) = -\\frac{d\\phi_B}{dt} = -B_0 a^2 \\omega \\cos(k + \\omega t)$$
        Por lo tanto, la magnitud máxima es $|\\varepsilon_{ind}|_{\\max} = B_0 a^2 \\omega$.
      `
    },
    {
      id: 'm4_ex5',
      title: 'Campo Espacio-Temporal B(y,t) sobre Rectángulo Fijo',
      level: 'certamen',
      source: 'Ayudantía 11 Problema 3',
      type: 'step_by_step',
      statement: `
        En una región del espacio hay un campo magnético dado por:
        $$\\vec{B}(y,t) = \\alpha y^2 e^{-\\beta t}\\,\\hat{k}$$
        siendo $\\alpha, \\beta > 0$. Un rectángulo conductor de lados $H$ (en $y$) y $L$ (en $x$) con resistencia $R$ está fijo sobre el plano $xy$, con su lado inferior ubicado en la recta $y = C$.<br>
        a) Encuentre el flujo del campo magnético $\\phi_B(t)$ a través del rectángulo.<br>
        b) Determine la magnitud de la fem inducida $|\\varepsilon_{ind}(t)|$.<br>
        c) Determine el sentido de la corriente inducida justificando con Lenz.
      `,
      steps: [
        {
          title: 'Paso 1: Integral de superficie con campo no homogéneo',
          content: `
            El campo apunta en $+\\hat{k}$ y varía cuadráticamente con la coordenada $y$.<br>
            Escogemos el vector normal de la espira en dirección $\\hat{n} = +\\hat{k}$. El diferencial de área es una franja horizontal de ancho $L$ y altura diferencial $dy$:
            $$d\\vec{A} = L\\,dy\\,\\hat{k}$$
            Los límites en $y$ van desde la base $y = C$ hasta el extremo superior $y = C + H$:
            $$\\phi_B(t) = \\int_C^{C+H} (\\alpha y^2 e^{-\\beta t}\\,\\hat{k}) \\cdot (L\\,dy\\,\\hat{k}) = \\alpha L e^{-\\beta t} \\int_C^{C+H} y^2 dy$$
          `
        },
        {
          title: 'Paso 2: Evaluación analítica del flujo magnético',
          content: `
            Evaluando la integral polinómica:
            $$\\int_C^{C+H} y^2 dy = \\left[\\frac{y^3}{3}\\right]_C^{C+H} = \\frac{(C+H)^3 - C^3}{3}$$
            Por lo tanto:
            $$\\phi_B(t) = \\frac{\\alpha L}{3} \\left[ (C+H)^3 - C^3 \\right] e^{-\\beta t}$$
          `
        },
        {
          title: 'Paso 3: Cálculo de la fem inducida por Faraday',
          content: `
            Derivamos respecto al tiempo aplicando la regla de la cadena:
            $$\\varepsilon_{ind}(t) = -\\frac{d\\phi_B}{dt} = -\\frac{\\alpha L}{3} \\left[ (C+H)^3 - C^3 \\right] (-\\beta e^{-\\beta t}) = \\frac{\\alpha \\beta L}{3} \\left[ (C+H)^3 - C^3 \\right] e^{-\\beta t}$$
            La magnitud es:
            $$|\\varepsilon_{ind}(t)| = \\frac{\\alpha \\beta L}{3} \\left[ (C+H)^3 - C^3 \\right] e^{-\\beta t}$$
          `
        },
        {
          title: 'Paso 4: Determinación del sentido de Lenz',
          content: `
            El campo exterior apunta en $+\\hat{k}$ (saliendo de la página).<br>
            Debido al factor $e^{-\\beta t}$ con $\\beta > 0$, la magnitud del campo está <strong>disminuyendo</strong> exponencialmente en el tiempo ($d\\phi_B/dt < 0$).<br>
            Por la Ley de Lenz, la corriente inducida debe oponerse a la disminución del flujo, generando un campo inducido en la misma dirección $+\\hat{k}$ (saliendo de la página).<br>
            Por regla de la mano derecha, un campo saliente exige que la corriente inducida circule en <strong>sentido antihorario</strong>.
          `
        }
      ]
    },
    {
      id: 'm4_ex6',
      title: 'Espira Circular con Espira Cuadrada Concéntrica',
      level: 'certamen',
      source: 'Ayudantía 10 Problema 2',
      type: 'step_by_step',
      statement: `
        Se tiene una espira circular de radio $R$ por la que circula una corriente $I(t) = I_0 e^{-t/\\tau}$ ($t > 0$) en sentido antihorario. En su centro se ubica una pequeña espira conductora cuadrada de lado $a$ ($a \\ll R$) coplanar con ella.<br>
        a) Calcule el flujo magnético a través de la pequeña espira cuadrada.<br>
        b) Calcule la fem inducida en la espira cuadrada.<br>
        c) Fundamente con la Ley de Lenz el sentido de la corriente inducida.
      `,
      steps: [
        {
          title: 'Paso 1: Aproximación de campo uniforme en el centro',
          content: `
            En el centro de una espira circular de radio $R$ con corriente $I(t)$ antihoraria, el campo magnético apunta hacia arriba ($+\\hat{k}$) y vale:
            $$B(t) = \\frac{\\mu_0 I(t)}{2R} = \\frac{\\mu_0 I_0}{2R} e^{-t/\\tau}$$
            Dado que la espira central cuadrada tiene lado $a \\ll R$, la variación espacial del campo sobre su superficie es despreciable, por lo que podemos considerarlo rigurosamente uniforme sobre toda su área $A = a^2$.
          `
        },
        {
          title: 'Paso 2: Flujo magnético sobre la espira cuadrada',
          content: `
            Tomando como vector normal $\\hat{n} = +\\hat{k}$ (saliente, concordante con el campo):
            $$\\phi_B(t) = \\iint_{\\text{cuadrado}} \\vec{B}\\cdot d\\vec{A} = B(t) \\cdot a^2 = \\frac{\\mu_0 a^2 I_0}{2R} e^{-t/\\tau}$$
          `
        },
        {
          title: 'Paso 3: fem inducida y sentido según Lenz',
          content: `
            Por la Ley de Faraday-Lenz:
            $$\\varepsilon_{ind}(t) = -\\frac{d\\phi_B}{dt} = -\\frac{\\mu_0 a^2 I_0}{2R} \\left(-\\frac{1}{\\tau} e^{-t/\\tau}\\right) = \\frac{\\mu_0 a^2 I_0}{2R\\tau} e^{-t/\\tau}$$
            <strong>Sentido según Lenz:</strong><br>
            Para $t > 0$, la corriente exterior decae en el tiempo ($dI/dt < 0$), lo que produce una disminución del flujo magnético saliente ($\\odot$). Por el principio de Lenz, la corriente inducida debe generar un campo magnético que compense dicha disminución, es decir, un campo también saliente ($\\odot$).<br>
            Por la regla de la mano derecha, para generar un campo hacia afuera, la corriente inducida en la espira cuadrada debe circular en <strong>sentido antihorario</strong>.
          `
        }
      ]
    },
    {
      id: 'm4_ex7',
      title: 'Espira Alejándose de Cable Recto Infinito',
      level: 'certamen',
      source: 'Simulacro Certamen 3 Problema 2',
      type: 'step_by_step',
      figure: 'img/mod4_faraday_moving_loop.svg',
      figureCaption: 'Cable recto infinito con corriente $+I\\hat{\\jmath}$ y espira alejándose con $\\vec{v} = v\\hat{\\imath}$.',
      statement: `
        Un cable recto infinito sobre el eje $y$ transporta corriente $I$ hacia $+y$. Una espira rectangular de lados $a$ (en $x$) y $b$ (en $y$) y resistencia $R$ se aleja del cable con velocidad $\\vec{v} = v\\hat{\\imath}$. En el instante $t$, su lado más cercano está a distancia $d(t) = d_0 + vt$.<br>
        a) Determine el campo del cable a distancia $x$ y el flujo $\\phi_B(t)$ a través de la espira indicando el vector normal escogido.<br>
        b) Determine la fem inducida $\\varepsilon_{ind}(t)$.<br>
        c) Indique el sentido de la corriente inducida fundamentado con Lenz y calcule su magnitud $I_{ind}(t)$.
      `,
      steps: [
        {
          title: 'Paso 1: Campo magnético y elección del vector normal',
          content: `
            Por la Ley de Ampère, el campo magnético a distancia perpendicular $x > 0$ de un cable con corriente $I$ en $+\\hat{\\jmath}$ es:
            $$\\vec{B}(x) = -\\frac{\\mu_0 I}{2\\pi x}\\,\\hat{k} \\quad (\\text{entra a la página } \\otimes)$$
            Escogemos el vector normal de la espira hacia adentro: $\\hat{n} = -\\hat{k}$.<br>
            El diferencial de área es una franja de altura $b$ y ancho $dx$: $d\\vec{A} = b\\,dx(-\\hat{k})$.
          `
        },
        {
          title: 'Paso 2: Integral de flujo magnético en función de d(t)',
          content: `
            $$\\phi_B(t) = \\int_{d(t)}^{d(t)+a} \\left(-\\frac{\\mu_0 I}{2\\pi x}\\hat{k}\\right) \\cdot \\left(-b\\,dx\\hat{k}\\right) = \\frac{\\mu_0 I b}{2\\pi} \\int_{d(t)}^{d(t)+a} \\frac{dx}{x} = \\frac{\\mu_0 I b}{2\\pi} \\ln\\left(\\frac{d(t)+a}{d(t)}\\right)$$
            Sustituyendo $d(t) = d_0 + vt$:
            $$\\phi_B(t) = \\frac{\\mu_0 I b}{2\\pi} \\ln\\left(1 + \\frac{a}{d_0 + vt}\\right)$$
          `
        },
        {
          title: 'Paso 3: Derivada temporal y fem inducida',
          content: `
            Derivamos respecto a $t$ recordando que $\\frac{d}{dt} d(t) = v$:
            $$\\frac{d\\phi_B}{dt} = \\frac{\\mu_0 I b}{2\\pi} \\left( \\frac{1}{d(t)+a} - \\frac{1}{d(t)} \\right) \\frac{d(d)}{dt} = \\frac{\\mu_0 I b v}{2\\pi} \\left( \\frac{-a}{d(t)(d(t)+a)} \\right)$$
            Por Faraday:
            $$\\varepsilon_{ind}(t) = -\\frac{d\\phi_B}{dt} = \\frac{\\mu_0 I b v a}{2\\pi (d_0 + vt)(d_0 + vt + a)}$$
          `
        },
        {
          title: 'Paso 4: Sentido por Lenz y magnitud de corriente',
          content: `
            Al alejarse la espira, el campo magnético entrante $\\otimes$ se debilita, por lo que el flujo entrante disminuye.<br>
            Según la Ley de Lenz, la espira se opone a esta pérdida generando un campo inducido que también entre a la página ($\\otimes$).<br>
            Por regla de la mano derecha, para generar campo entrante, la corriente inducida debe circular en <strong>sentido horario</strong>.<br>
            Su magnitud es:
            $$I_{ind}(t) = \\frac{\\varepsilon_{ind}(t)}{R} = \\frac{\\mu_0 I b v a}{2\\pi R (d_0 + vt)(d_0 + vt + a)}$$
          `
        }
      ]
    },
    {
      id: 'm4_ex8',
      title: 'Signo Negativo en Faraday-Lenz y Conservación de Energía',
      level: 'certamen',
      source: 'Ayudantía 10 Problema Conceptual 1',
      type: 'conceptual',
      statement: `
        Explique por qué en la ley de Faraday-Lenz la fem inducida es proporcional a la razón de cambio del flujo magnético con signo negativo ($\\varepsilon = -\\frac{d\\phi_B}{dt}$). ¿No podría ser con signo positivo? ¿Qué violaría un signo positivo?
      `,
      modelAnswer: `
        El signo negativo en la Ley de Faraday es una exigencia ineludible del <strong>Principio de Conservación de la Energía</strong>.<br><br>
        <strong>¿Qué ocurriría si el signo fuera positivo ($\\varepsilon = +\\frac{d\\phi_B}{dt}$)?</strong><br>
        Si el signo fuese positivo, cualquier pequeño aumento inicial en el flujo magnético induciría una corriente en un sentido tal que crearía un campo magnético adicional en la <em>misma dirección</em> del cambio, aumentando aún más el flujo. Este incremento de flujo induciría una corriente aún mayor, la cual generaría más campo, en un proceso de realimentación positiva descontrolada (inestabilidad infinita).<br><br>
        Se obtendría así energía eléctrica y disipación de calor por efecto Joule infinita a partir de una perturbación infinitesimal sin realizar ningún trabajo mecánico externo, lo cual constituiría una máquina de movimiento perpetuo de primera especie y violaría el Primer y Segundo Principios de la Termodinámica.<br><br>
        Por tanto, el signo negativo (Ley de Lenz) asegura que el sistema siempre ejerza una fuerza resistente de frenado mecánico (o contra-fem) que demanda suministrar trabajo externo exactamente igual a la energía eléctrica generada.
      `,
      rubric: `
        • 5 pts: Explicar la realimentación positiva descontrolada si el signo fuera positivo.<br>
        • 5 pts: Concluir rigurosamente con la violación del Principio de Conservación de la Energía y la necesidad de trabajo mecánico compensatorio.
      `
    }
  ]
};
