/**
 * MÓDULO 10: MAXWELL Y SÍNTESIS CONCEPTUAL
 * FIS120 / FIS12125 · UTFSM
 */

window.MODULE_DATA_MOD10 = {
  number: '10',
  title: 'Maxwell y Síntesis Conceptual',
  description: 'Las 4 ecuaciones de Maxwell en forma integral, corriente de desplazamiento, paradoja de Ampère en condensadores (superficies S1 vs S2), campo B entre placas y aplicaciones como la cocina de inducción.',
  hasInteractive: false,
  theory: `
    <p>
      James Clerk Maxwell unificó la electricidad, el magnetismo y la óptica en un conjunto coherente de cuatro ecuaciones fundamentales. Su contribución cumbre fue añadir la <strong>corriente de desplazamiento</strong> a la Ley de Ampère, corrigiendo una contradicción matemática fundamental y prediciendo la existencia de las ondas electromagnéticas.
    </p>

    <div class="box-formula">
      <strong>1. Las Cuatro Ecuaciones de Maxwell en Forma Integral (Vacío con Fuentes):</strong>
      <ol style="padding-left: 1.2rem; margin-top: 0.5rem;">
        <li>
          <strong>Ley de Gauss para el Campo Eléctrico:</strong>
          $$\\oiint_S \\vec{E} \\cdot d\\vec{A} = \\frac{Q_{enc}}{\\varepsilon_0}$$
          <em>Significado físico:</em> El flujo eléctrico neto a través de una superficie cerrada es proporcional a la carga neta encerrada; las cargas eléctricas actúan como fuentes o sumideros de líneas de $\\vec{E}$.
        </li>
        <li style="margin-top: 0.6rem;">
          <strong>Ley de Gauss para el Campo Magnético:</strong>
          $$\\oiint_S \\vec{B} \\cdot d\\vec{A} = 0$$
          <em>Significado físico:</em> El flujo magnético neto a través de cualquier superficie cerrada es siempre cero; no existen monopolos magnéticos aislados en la naturaleza y las líneas de $\\vec{B}$ son cerradas.
        </li>
        <li style="margin-top: 0.6rem;">
          <strong>Ley de Faraday-Lenz:</strong>
          $$\\oint_\\Gamma \\vec{E} \\cdot d\\vec{l} = -\\frac{d\\phi_B}{dt} = -\\frac{d}{dt} \\iint_S \\vec{B} \\cdot d\\vec{A}$$
          <em>Significado físico:</em> Un flujo magnético variable en el tiempo engendra un campo eléctrico no conservativo cuyas líneas de campo se cierran sobre sí mismas.
        </li>
        <li style="margin-top: 0.6rem;">
          <strong>Ley de Ampère-Maxwell:</strong>
          $$\\oint_\\Gamma \\vec{B} \\cdot d\\vec{l} = \\mu_0 I_{cond} + \\mu_0 \\varepsilon_0 \\frac{d\\phi_E}{dt}$$
          <em>Significado físico:</em> El campo magnético es producido tanto por corrientes de cargas en movimiento (conducción) como por campos eléctricos que varían en el tiempo (desplazamiento).
        </li>
      </ol>
    </div>

    <div class="figure-container">
      <img src="img/mod10_maxwell_capacitor.svg" alt="Paradoja del Condensador">
      <div class="figure-caption">Paradoja del condensador (Simulacro C3 Pregunta Conceptual): el lazo $\\Gamma$ puede cerrarse mediante el disco plano $S_1$ o la bolsa $S_2$ que pasa entre las placas.</div>
    </div>

    <div class="box-method">
      <strong>2. La Paradoja de Ampère y su Resolución por Maxwell:</strong>
      <p>
        Consideremos el lazo cerrado $\\Gamma$ alrededor del cable que carga un condensador:
        <br>• Si usamos la superficie plana $S_1$ (disco plano), el cable conductor la atraviesa transportando corriente $I(t)$:
        $$\\oint_\\Gamma \\vec{B} \\cdot d\\vec{l} = \\mu_0 I(t)$$
        • Si usamos la superficie deformada en forma de bolsa $S_2$, que pasa a través del espacio vacío entre las placas: ninguna corriente de conducción atraviesa $S_2$ ($I_{cond} = 0$). Sin el término de Maxwell, la ley predeciría falsamente $\\oint_\\Gamma \\vec{B}\\cdot d\\vec{l} = 0$, una contradicción matemática inaceptable porque la integral sobre el lazo $\\Gamma$ debe ser única.
        <br><br>
        <strong>Resolución de Maxwell:</strong>
        Entre las placas existe un campo eléctrico variable $E(t) = \\frac{Q(t)}{\\varepsilon_0 A}$. El flujo eléctrico a través de la bolsa $S_2$ es $\\phi_E = E A = \\frac{Q(t)}{\\varepsilon_0}$.
        <br>La <strong>corriente de desplazamiento</strong> que atraviesa la bolsa $S_2$ es:
        $$I_d = \\varepsilon_0 \\frac{d\\phi_E}{dt} = \\varepsilon_0 \\frac{d}{dt}\\left(\\frac{Q(t)}{\\varepsilon_0}\\right) = \\frac{dQ}{dt} = I(t)$$
        Por tanto:
        $$\\oint_\\Gamma \\vec{B} \\cdot d\\vec{l} = \\mu_0 I_d = \\mu_0 I(t)$$
        ¡El resultado es idéntico e independiente de la superficie escogida!
      </p>
    </div>

    <div class="box-warning">
      <strong>Pregunta Clásica de Pauta: Cocina de Inducción:</strong><br>
      La cocina de inducción funciona generando un campo magnético de alta frecuencia mediante una bobina bajo la placa de vitrocerámica.
      <br>• <strong>Olla de Acero:</strong> Es un conductor metálico ferromagnético. El campo alterno induce corrientes de Foucault (Eddy) en su base, las cuales disipan calor intensamente por efecto Joule ($P = I_{ind}^2 R$), calentando velozmente la olla y el agua.
      <br>• <strong>Olla de Greda:</strong> Es un material cerámico no conductor (dieléctrico). Prácticamente no se inducen corrientes en ella, por lo que no disipa energía térmica apreciable y no calienta por inducción.
    </div>
  `,
  exercises: [
    {
      id: 'm10_ex1',
      title: 'Identificación de las Ecuaciones de Maxwell',
      level: 'basic',
      source: 'Simulacro C3 Conceptual a',
      type: 'multiple_choice',
      statement: `
        ¿Cuál de las siguientes ecuaciones de Maxwell formaliza la inexistencia de monopolos magnéticos aislados en la naturaleza?
      `,
      options: [
        '$\\oiint \\vec{B} \\cdot d\\vec{A} = 0$',
        '$\\oiint \\vec{E} \\cdot d\\vec{A} = Q_{enc}/\\varepsilon_0$',
        '$\\oint \\vec{E} \\cdot d\\vec{l} = -d\\phi_B/dt$',
        '$\\oint \\vec{B} \\cdot d\\vec{l} = \\mu_0 I$'
      ],
      correctOption: 0,
      explanation: `
        La Ley de Gauss para el magnetismo $\\oiint \\vec{B} \\cdot d\\vec{A} = 0$ establece que no existen fuentes puntuales (cargas magnéticas aisladas) de donde emanen o converjan líneas de campo magnético. Toda línea de campo magnético es una curva cerrada continua.
      `
    },
    {
      id: 'm10_ex2',
      title: 'Cálculo de Corriente de Desplazamiento',
      level: 'basic',
      source: 'Fundamentos de Ondas EM',
      type: 'numerical',
      statement: `
        Entre las placas de un condensador circular plano de área $A = 0.050\\text{ m}^2$, el campo eléctrico uniforme varía a una tasa constante de $\\frac{dE}{dt} = 2.0 \\times 10^{11}\\text{ V/(m}\\cdot\\text{s)}$. Sabiendo que $\\varepsilon_0 = 8.854 \\times 10^{-12}\\text{ F/m}$, calcule la corriente de desplazamiento $I_d$ en amperios.
      `,
      placeholder: 'Ej: 0.0885',
      units: 'A',
      correctValue: 0.08854,
      tolerance: 0.03,
      explanation: `
        $$I_d = \\varepsilon_0 \\frac{d\\phi_E}{dt} = \\varepsilon_0 A \\frac{dE}{dt} = (8.854 \\times 10^{-12}\\text{ F/m}) \\cdot (0.050\\text{ m}^2) \\cdot (2.0 \\times 10^{11}\\text{ V/(m}\\cdot\\text{s)}) = 0.08854\\text{ A} \\approx 88.5\\text{ mA}$$
      `
    },
    {
      id: 'm10_ex3',
      title: 'Monopolos Magnéticos y Líneas de B',
      level: 'intermediate',
      source: 'Conceptos de Campo Magnético',
      type: 'true_false',
      statement: `
        Si en el futuro se descubriera experimentalmente un monopolo magnético (una partícula con carga magnética neta $q_m$), la ecuación $\\oiint \\vec{B}\\cdot d\\vec{A} = 0$ tendría que modificarse para igualar a $\\mu_0 q_{m,enc}$, de forma análoga a la ley de Gauss electrostática.
      `,
      correct: true,
      justification: `
        Verdadero. La ecuación $\\oiint \\vec{B}\\cdot d\\vec{A} = 0$ refleja la ausencia empírica de cargas magnéticas. De existir un monopolo magnético $q_m$, las líneas de $\\vec{B}$ nacerían en él, requiriendo que el flujo neto cerrado fuese proporcional a la carga magnética encerrada $\\mu_0 q_{m,enc}$.
      `
    },
    {
      id: 'm10_ex4',
      title: 'Campo Magnético Inducido entre Placas de Condensador',
      level: 'intermediate',
      source: 'Simulacro C3 Conceptual c',
      type: 'multiple_choice',
      statement: `
        Durante la carga de un condensador de placas circulares de radio $R$ mediante corriente $I(t)$, ¿cuál es la dependencia radial del campo magnético $B(r)$ en la región entre las placas para $r < R$?
      `,
      options: [
        '$B(r) \\propto r$ (crece linealmente con la distancia al eje)',
        '$B(r) \\propto 1/r$ (decae hiperbólicamente)',
        '$B(r) = 0$ (no hay campo magnético en el dieléctrico)',
        '$B(r) \\propto r^2$ (crece cuadráticamente)'
      ],
      correctOption: 0,
      explanation: `
        Para $r < R$, el lazo circular de radio $r$ encierra solo una fracción $\\frac{\\pi r^2}{\\pi R^2} = \\frac{r^2}{R^2}$ de la corriente de desplazamiento total $I_d = I(t)$.<br>
        Por Ampère-Maxwell:
        $$B(r) 2\\pi r = \\mu_0 I(t) \\frac{r^2}{R^2} \\implies B(r) = \\frac{\\mu_0 I(t) r}{2\\pi R^2}$$
        El campo crece linealmente desde cero en el eje hasta su valor máximo en el borde $r = R$.
      `
    },
    {
      id: 'm10_ex5',
      title: 'Resolución de la Paradoja de Ampère en el Condensador',
      level: 'certamen',
      source: 'Simulacro Certamen 3 Pregunta Conceptual b',
      type: 'step_by_step',
      figure: 'img/mod10_maxwell_capacitor.svg',
      figureCaption: 'Lazo $\\Gamma$ alrededor del cable: disco plano $S_1$ vs bolsa entre placas $S_2$.',
      statement: `
        Un condensador de placas circulares de radio $R$ se carga mediante corriente de conducción $I(t)$. Aplique la ley de Ampère sin el término de Maxwell al lazo $\\Gamma$, primero usando la superficie $S_1$ y luego la $S_2$. ¿Qué contradicción aparece? ¿Cómo la resuelve la ecuación de Ampère-Maxwell?
      `,
      steps: [
        {
          title: 'Paso 1: Aplicación de la ley original de Ampère sobre S1',
          content: `
            La superficie $S_1$ es un disco plano apoyado en el lazo $\\Gamma$. El cable de alimentación físico atraviesa $S_1$, por lo que la corriente de conducción enlazada es:
            $$I_{enl}(S_1) = I(t)$$
            La Ley de Ampère clásica predice:
            $$\\oint_\\Gamma \\vec{B} \\cdot d\\vec{l} = \\mu_0 I(t)$$
          `
        },
        {
          title: 'Paso 2: Aplicación sobre la superficie en forma de bolsa S2',
          content: `
            La superficie $S_2$ tiene el mismo contorno perimetral $\\Gamma$, pero se abomba hacia adelante pasando por el espacio interplacas del condensador sin tocar el cable ni las placas.<br>
            En el espacio entre placas no hay transporte de cargas libres de conducción ($I_{cond} = 0$).<br>
            Por lo tanto, la Ley de Ampère sin Maxwell daría:
            $$\\oint_\\Gamma \\vec{B} \\cdot d\\vec{l} = \\mu_0 (0) = 0$$
          `
        },
        {
          title: 'Paso 3: Identificación de la contradicción física y matemática',
          content: `
            La integral del primer miembro $\\oint_\\Gamma \\vec{B} \\cdot d\\vec{l}$ es exactamente la misma curva cerrada $\\Gamma$ en el espacio, por lo que su valor debe ser único e independiente de la superficie imaginaria elegida.<br>
            Sin embargo, la ley clásica predice simultáneamente $\\mu_0 I(t)$ y $0$. ¡Esta contradicción matemática demostraba que la ley de Ampère estaba incompleta!
          `
        },
        {
          title: 'Paso 4: Solución de Maxwell mediante la corriente de desplazamiento',
          content: `
            Maxwell postuló que un campo eléctrico variable en el tiempo $\\frac{\\partial \\vec{E}}{\\partial t}$ genera campo magnético exactamente igual que una corriente real.<br>
            El campo eléctrico uniforme entre las placas en el instante $t$ es $E(t) = \\frac{Q(t)}{\\varepsilon_0 A}$, donde $A$ es el área de las placas.<br>
            El flujo eléctrico total a través de la bolsa $S_2$ es $\\phi_E = E(t) \\cdot A = \\frac{Q(t)}{\\varepsilon_0}$.<br>
            Calculamos la <strong>corriente de desplazamiento</strong>:
            $$I_d = \\varepsilon_0 \\frac{d\\phi_E}{dt} = \\varepsilon_0 \\frac{d}{dt}\\left(\\frac{Q(t)}{\\varepsilon_0}\\right) = \\frac{dQ}{dt} = I(t)$$
            Con la ecuación de Ampère-Maxwell:
            $$\\oint_\\Gamma \\vec{B} \\cdot d\\vec{l} = \\mu_0 (I_{cond} + I_d) = \\mu_0 (0 + I(t)) = \\mu_0 I(t)$$
            ¡Ambas superficies entregan exactamente el mismo resultado $\\mu_0 I(t)$, resolviendo la paradoja con total coherencia!
          `
        }
      ]
    },
    {
      id: 'm10_ex6',
      title: 'Campo B(r) entre Placas para r < R',
      level: 'certamen',
      source: 'Simulacro Certamen 3 Pregunta Conceptual c',
      type: 'step_by_step',
      statement: `
        Entre las placas circulares de radio $R$ del condensador en proceso de carga con corriente $I(t)$, calcule el vector campo magnético a una distancia radial $r < R$ del eje central en función de $I(t), r$ y $R$.
      `,
      steps: [
        {
          title: 'Paso 1: Elección de lazo amperiano coaxial',
          content: `
            Por la simetría cilíndrica del condensador circular y de las líneas axiales de $\\vec{E}$, el campo magnético inducido $\\vec{B}$ describe circunferencias azimutales centradas en el eje.<br>
            Elegimos un lazo amperiano circular de radio $r < R$ en el plano perpendicular al eje entre las placas:
            $$\\oint_\\Gamma \\vec{B} \\cdot d\\vec{l} = B(r) 2\\pi r$$
          `
        },
        {
          title: 'Paso 2: Corriente de desplazamiento encerrada por el lazo de radio r',
          content: `
            Como no hay corriente de conducción entre las placas ($I_{cond} = 0$), toda la circulación se debe a la corriente de desplazamiento.<br>
            El flujo eléctrico a través del círculo de radio $r$ es:
            $$\\phi_E(r) = E(t) \\cdot (\\pi r^2)$$
            La corriente de desplazamiento enlazada por el lazo es:
            $$I_{d, enl}(r) = \\varepsilon_0 \\frac{d\\phi_E(r)}{dt} = \\varepsilon_0 (\\pi r^2) \\frac{dE}{dt}$$
          `
        },
        {
          title: 'Paso 3: Relación con la corriente de carga total I(t) y despeje de B(r)',
          content: `
            Recordando que $E(t) = \\frac{Q(t)}{\\varepsilon_0 \\pi R^2}$:
            $$\\frac{dE}{dt} = \\frac{1}{\\varepsilon_0 \\pi R^2} \\frac{dQ}{dt} = \\frac{I(t)}{\\varepsilon_0 \\pi R^2}$$
            Sustituyendo en la corriente de desplazamiento:
            $$I_{d, enl}(r) = \\varepsilon_0 (\\pi r^2) \\left( \\frac{I(t)}{\\varepsilon_0 \\pi R^2} \\right) = I(t) \\frac{r^2}{R^2}$$
            Aplicando Ampère-Maxwell:
            $$B(r) 2\\pi r = \\mu_0 I_{d, enl}(r) = \\mu_0 I(t) \\frac{r^2}{R^2}$$
            Despejando $B(r)$:
            $$B(r) = \\frac{\\mu_0 I(t) r}{2\\pi R^2}$$
            <strong>Chequeo dimensional:</strong> En el borde $r = R$, $B(R) = \\frac{\\mu_0 I(t)}{2\\pi R}$, coincidiendo exactamente con el campo magnético en la superficie de un cable de radio $R$.
          `
        }
      ]
    },
    {
      id: 'm10_ex7',
      title: 'Cocina de Inducción: Olla de Acero vs. Olla de Greda',
      level: 'certamen',
      source: 'Pauta Certamen 3 2026-1 Pregunta Conceptual',
      type: 'conceptual',
      statement: `
        Una cocina de inducción calienta los recipientes mediante el uso de un campo magnético. Si se dispone de dos ollas de tamaño similar: una olla de acero y una olla de greda tradicional, ambas contienen la misma cantidad de agua inicialmente a igual temperatura.<br>
        Explique qué condición debe cumplir el campo magnético y cuál de las dos ollas permitirá calentar el agua de forma más eficiente. Justifique su respuesta utilizando argumentos físicos.
      `,
      modelAnswer: `
        <strong>1. Condición sobre el campo magnético:</strong><br>
        El campo magnético debe ser <strong>variable en el tiempo</strong> (debe ser un campo de corriente alterna de alta frecuencia, típicamente $20\\text{–}50\\text{ kHz}$). Si el campo fuera estacionario/constante en el tiempo, $\\frac{d\\phi_B}{dt} = 0$ y por la Ley de Faraday no se induciría ninguna fuerza electromotriz.
        <br><br>
        <strong>2. Comparación entre la olla de acero y la olla de greda:</strong><br>
        La <strong>olla de acero</strong> permitirá calentar el agua de manera incomparablemente más eficiente.
        <br><br>
        <strong>Justificación física:</strong><br>
        • De acuerdo con la Ley de Faraday-Lenz ($\\varepsilon = -\\frac{d\\phi_B}{dt}$), el campo magnético variable induce campos eléctricos y corrientes circulares cerradas (corrientes de Foucault o *Eddy currents*) en cualquier material que se coloque sobre la placa.
        <br>• El <strong>acero</strong> es un material conductor eléctrico y además ferromagnético. Su conductividad permite la libre circulación de grandes corrientes inducidas, las cuales disipan energía térmica intensamente por <strong>efecto Joule</strong> ($P = I_{ind}^2 R = \\frac{\\varepsilon^2}{R}$) directamente en la base metálica de la olla, transfiriendo ese calor por conducción al agua.
        <br>• En cambio, la <strong>greda tradicional</strong> es un material cerámico cocido de carácter dieléctrico (muy baja o nula conductividad eléctrica libre). Al no haber portadores de carga libres apreciables, la corriente inducida es prácticamente cero ($I_{ind} \\approx 0$), impidiendo toda disipación de calor por efecto Joule. Por ello, la olla de greda no se calienta en una cocina de inducción.
      `,
      rubric: `
        • 3 pts: Explicar que el campo B debe ser variable en el tiempo (Faraday).<br>
        • 4 pts: Olla de acero conductora -> induce corrientes de Foucault -> disipación Joule P = I^2 R.<br>
        • 3 pts: Olla de greda dieléctrica/aislante -> no circulan corrientes apreciables -> no calienta.
      `
    }
  ]
};
