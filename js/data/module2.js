/**
 * MÓDULO 2: DENSIDAD DE CORRIENTE Y CORRIENTE TOTAL
 * FIS120 / FIS12125 · UTFSM
 */

window.MODULE_DATA_MOD2 = {
  number: '2',
  title: 'Densidad de Corriente J(r) y Corriente Total',
  description: 'Integración del vector densidad de corriente en conductores con perfiles homogéneos y no homogéneos: perfiles parabólicos, lineales, escalonados (efecto pelicular) y angulares.',
  hasInteractive: false,
  theory: `
    <p>
      En conductores reales o modelos avanzados de telecomunicaciones y física de plasmas, la corriente no siempre se distribuye uniformemente en la sección transversal. La <strong>densidad de corriente volumétrica</strong> $\\vec{J}$ cuantifica el flujo de carga por unidad de área normal y por unidad de tiempo.
    </p>

    <div class="box-formula">
      <strong>1. Relación Fundamental Integral (Formulario C3):</strong>
      $$I = \\iint_S \\vec{J} \\cdot d\\vec{A}$$
      <p>
        Para un conductor cilíndrico alineado con el eje $z$ cuya sección transversal está en el plano $xy$ y con corriente fluyendo hacia $+\\hat{k}$:
        $$d\\vec{A} = r\\,dr\\,d\\theta\\,\\hat{k}$$
        Si $\\vec{J} = J(r)\\,\\hat{k}$ no depende del ángulo azimutal $\\theta$:
        $$\\int_0^{2\\pi} d\\theta = 2\\pi \\implies d\\vec{A}_{anillo} = 2\\pi r\\,dr\\,\\hat{k}$$
        $$I = \\int_{r_{min}}^{r_{max}} J(r)\\, 2\\pi r\\,dr$$
      </p>
    </div>

    <div class="figure-container">
      <img src="img/mod2_j_profiles.svg" alt="Perfiles de Densidad de Corriente">
      <div class="figure-caption">Comparación de perfiles radiales $J(r)$: parabólico (Ayudantía 9 P2), lineal $\\beta r$ (Ayudantía 9 P3) y escalonado (Pauta C3 P1).</div>
    </div>

    <div class="box-method">
      <strong>2. Perfiles Radiales Emblemáticos en Evaluaciones UTFSM:</strong>
      <p>
        <strong>A. Densidad Parabólica Decreciente:</strong> $J(r) = 2J_0\\left(1 - \\frac{r^2}{a^2}\\right)$ (Ayudantía 9 P2)
        $$I_T = \\int_0^a 2J_0\\left(1 - \\frac{r^2}{a^2}\\right) 2\\pi r\\,dr = 4\\pi J_0 \\left[\\frac{r^2}{2} - \\frac{r^4}{4a^2}\\right]_0^a = 4\\pi J_0 \\left(\\frac{a^2}{2} - \\frac{a^2}{4}\\right) = \\pi J_0 a^2$$
        <br>
        <strong>B. Densidad Lineal Creciente:</strong> $J(r) = \\beta r$ (Ayudantía 9 P3)
        $$I_T = \\int_0^R (\\beta r) 2\\pi r\\,dr = 2\\pi \\beta \\int_0^R r^2\\,dr = \\frac{2\\pi \\beta R^3}{3}$$
        <br>
        <strong>C. Densidad Escalonada - Efecto Pelicular:</strong> (Pauta C3 2026-1 P1)
        $$J(r) = \\begin{cases} J_0, & 0 \\le r \\le R/2 \\\\ 3J_0, & R/2 < r \\le R \\end{cases}$$
        $$I = J_0 \\pi \\left(\\frac{R}{2}\\right)^2 + 3J_0 \\pi \\left[R^2 - \\left(\\frac{R}{2}\\right)^2\\right] = \\frac{\\pi J_0 R^2}{4} + \\frac{9\\pi J_0 R^2}{4} = \\frac{10\\pi J_0 R^2}{4} = \\frac{5}{2}\\pi J_0 R^2$$
        Despejando: $J_0 = \\frac{2I}{5\\pi R^2}$.
      </p>
    </div>

    <div class="figure-container">
      <img src="img/mod2_coaxial_stepped.svg" alt="Sección Transversal Escalonada">
      <div class="figure-caption">Sección transversal del cable con densidad escalonada de la Pauta Oficial C3: mayor densidad en la periferia exterior.</div>
    </div>

    <div class="box-warning">
      <strong>Errores Frecuentes en el Certamen:</strong><br>
      1. Escribir $I = J \\cdot A$ cuando $J$ depende de $r$. ¡Si $J$ no es constante, la multiplicación directa es un error conceptual grave de 0 puntos!<br>
      2. En tubos o coronas circulares ($R_1 \\le r \\le R_2$), integrar erróneamente desde $0$ en lugar de $R_1$.<br>
      3. No considerar el signo de la densidad cuando hay corrientes en sentidos opuestos: $\\vec{J}_1 = J_1\\hat{k}$ vs $\\vec{J}_2 = -J_2\\hat{k}$.
    </div>
  `,
  exercises: [
    {
      id: 'm2_ex1',
      title: 'Corriente en un Conductor Homogéneo',
      level: 'basic',
      source: 'Fundamentos de Conducción',
      type: 'multiple_choice',
      statement: `
        Un cable de cobre cilíndrico de radio $R = 1.0\\text{ mm}$ transporta una densidad de corriente uniforme de magnitud $J = 3.0 \\times 10^6\\text{ A/m}^2$. ¿Cuál es la corriente total $I$ que atraviesa el cable?
      `,
      options: [
        '$9.42\\text{ A}$',
        '$3.14\\text{ A}$',
        '$18.8\\text{ A}$',
        '$0.94\\text{ A}$'
      ],
      correctOption: 0,
      explanation: `
        Dado que la densidad de corriente es estrictamente uniforme:
        $$I = J \\cdot A = J \\cdot (\\pi R^2) = (3.0 \\times 10^6\\text{ A/m}^2) \\cdot (\\pi \\cdot (1.0 \\times 10^{-3}\\text{ m})^2) = 3.0\\pi \\approx 9.425\\text{ A}$$
      `
    },
    {
      id: 'm2_ex2',
      title: 'Cálculo de Corriente con Densidad Parabólica',
      level: 'basic',
      source: 'Ayudantía 9 Problema 2a',
      type: 'numerical',
      statement: `
        Considere un cable cilíndrico de radio $a = 0.050\\text{ m}$ con densidad de corriente $\\vec{J}(r) = 2J_0\\left(1 - \\frac{r^2}{a^2}\\right)\\hat{k}$. Si $J_0 = 400.0\\text{ A/m}^2$, calcule numéricamente la corriente total $I_T$ en amperios.
      `,
      placeholder: 'Ej: 3.14',
      units: 'A',
      correctValue: 3.1416,
      tolerance: 0.03,
      explanation: `
        La integral analítica da:
        $$I_T = \\pi J_0 a^2 = \\pi \\cdot 400.0 \\cdot (0.050)^2 = \\pi \\cdot 400.0 \\cdot 0.0025 = \\pi \\approx 3.1416\\text{ A}$$
      `
    },
    {
      id: 'm2_ex3',
      title: 'Distribución Radial de Corriente en Conductor Macizo',
      level: 'intermediate',
      source: 'Concepto Densidad UTFSM',
      type: 'true_false',
      statement: `
        Si un cilindro conductor macizo de radio $R$ transporta una corriente con densidad $J(r) = C r^2$ ($C > 0$), la mitad exterior del cable ($R/2 < r \\le R$) transporta exactamente 15 veces más corriente que la mitad interior ($0 \\le r \\le R/2$).
      `,
      correct: true,
      justification: `
        Verdadero. La corriente encerrada hasta un radio $r$ es:
        $$I(r) = \\int_0^r C r'^{2} 2\\pi r' dr' = 2\\pi C \\left[\\frac{r'^4}{4}\\right]_0^r = \\frac{\\pi C r^4}{2}$$
        Para la mitad interior ($r = R/2$):
        $$I_{int} = I(R/2) = \\frac{\\pi C (R/2)^4}{2} = \\frac{\\pi C R^4}{32}$$
        La corriente total es $I_{tot} = I(R) = \\frac{\\pi C R^4}{2} = \\frac{16\\pi C R^4}{32} = 16 I_{int}$.<br>
        Por tanto, la corriente en la mitad exterior es $I_{ext} = I_{tot} - I_{int} = 15 I_{int}$. ¡15 veces mayor!
      `
    },
    {
      id: 'm2_ex4',
      title: 'Corriente en Casquete Cilíndrico Exterior',
      level: 'intermediate',
      source: 'Ayudantía 9 Problema 1a',
      type: 'multiple_choice',
      statement: `
        Un cable coaxial tiene un conductor exterior hueco con radio interno $2R$ y radio externo $4R$, transportando una densidad de corriente uniforme $\\vec{J}_2 = 2J_0(-\\hat{k})$. ¿Cuál es la magnitud de la corriente total $I_2$ que circula por este casquete exterior?
      `,
      options: [
        '$24\\pi J_0 R^2$',
        '$12\\pi J_0 R^2$',
        '$28\\pi J_0 R^2$',
        '$32\\pi J_0 R^2$'
      ],
      correctOption: 0,
      explanation: `
        El área de la sección transversal de la corona circular es:
        $$A = \\pi ((4R)^2 - (2R)^2) = \\pi (16R^2 - 4R^2) = 12\\pi R^2$$
        Como $J_2 = 2J_0$ es uniforme en esta región:
        $$I_2 = J_2 \\cdot A = (2J_0) \\cdot (12\\pi R^2) = 24\\pi J_0 R^2$$
      `
    },
    {
      id: 'm2_ex5',
      title: 'Densidad Lineal en Cilindro Infinito',
      level: 'intermediate',
      source: 'Ayudantía 9 Problema 3',
      type: 'multiple_choice',
      statement: `
        Un cilindro conductor macizo de radio $R$ transporta una densidad de corriente $\\vec{J}(r) = \\beta r\\hat{k}$ con $\\beta > 0$. ¿Cuál es la corriente total encerrada por el cilindro?
      `,
      options: [
        '$\\frac{2\\pi \\beta R^3}{3}$',
        '$\\pi \\beta R^3$',
        '$\\frac{\\pi \\beta R^3}{2}$',
        '$\\frac{4\\pi \\beta R^3}{3}$'
      ],
      correctOption: 0,
      explanation: `
        Integrando sobre anillos concéntricos:
        $$I = \\int_0^R (\\beta r) 2\\pi r\\,dr = 2\\pi \\beta \\int_0^R r^2\\,dr = 2\\pi \\beta \\left[\\frac{r^3}{3}\\right]_0^R = \\frac{2\\pi \\beta R^3}{3}$$
      `
    },
    {
      id: 'm2_ex6',
      title: 'Efecto Pelicular Escalonado: Determinación de J₀',
      level: 'certamen',
      source: 'Pauta Certamen 3 2026-1 Problema 1a',
      type: 'step_by_step',
      figure: 'img/mod2_coaxial_stepped.svg',
      figureCaption: 'Sección transversal del conductor: $J_0$ para $r \\le R/2$ y $3J_0$ para $R/2 < r \\le R$.',
      statement: `
        Un ingeniero en telecomunicaciones estudia el efecto pelicular en un cable coaxial de radio $R$. Modela la dependencia radial con una función escalonada que reproduce una corriente total $I$:
        $$J(r) = \\begin{cases} J_0, & 0 \\le r \\le R/2 \\\\ 3J_0, & R/2 < r \\le R \\end{cases}$$
        Usando la condición de corriente total, determine la expresión analítica para $J_0$ en función de $R$ e $I$.
      `,
      steps: [
        {
          title: 'Paso 1: Planteamiento de la integral de corriente en regiones separadas',
          content: `
            La corriente total $I$ es la integral de superficie de $J(r)$ sobre el disco de radio $R$:
            $$I = \\int_0^R J(r) 2\\pi r\\,dr = \\int_0^{R/2} J_0 2\\pi r\\,dr + \\int_{R/2}^R 3J_0 2\\pi r\\,dr$$
          `
        },
        {
          title: 'Paso 2: Evaluación analítica de cada integral de superficie',
          content: `
            • Para la zona interior ($0 \\le r \\le R/2$):
            $$I_{int} = 2\\pi J_0 \\left[\\frac{r^2}{2}\\right]_0^{R/2} = 2\\pi J_0 \\left(\\frac{R^2}{8}\\right) = \\frac{\\pi J_0 R^2}{4}$$
            • Para la capa exterior ($R/2 < r \\le R$):
            $$I_{ext} = 6\\pi J_0 \\left[\\frac{r^2}{2}\\right]_{R/2}^R = 3\\pi J_0 \\left(R^2 - \\frac{R^2}{4}\\right) = 3\\pi J_0 \\left(\\frac{3R^2}{4}\\right) = \\frac{9\\pi J_0 R^2}{4}$$
          `
        },
        {
          title: 'Paso 3: Suma y despeje de J₀',
          content: `
            Sumando ambas contribuciones:
            $$I = I_{int} + I_{ext} = \\frac{\\pi J_0 R^2}{4} + \\frac{9\\pi J_0 R^2}{4} = \\frac{10\\pi J_0 R^2}{4} = \\frac{5\\pi J_0 R^2}{2}$$
            Despejando $J_0$:
            $$J_0 = \\frac{2I}{5\\pi R^2}$$
            <strong>Chequeo dimensional:</strong> $[I / R^2] = \\text{A/m}^2$, unidades correctas de densidad de corriente volumétrica.
          `
        }
      ]
    },
    {
      id: 'm2_ex7',
      title: 'Densidad con Dependencia Angular: Condición de Igualdad',
      level: 'certamen',
      source: 'Ayudantía 9 Problema 4a,b',
      type: 'step_by_step',
      statement: `
        Se cuenta con un cable coaxial muy largo con un cilindro interior de radio $R_1$ y un cascarón exterior de radio externo $R_2$ (radio interno $R_1$). El cilindro interior cuenta con una densidad no uniforme $\\vec{J}_1(\\theta) = \\alpha \\sin^2(\\theta)\\,\\hat{k}$. El cascarón exterior cuenta con una densidad uniforme $\\vec{J}_2 = J_0(-\\hat{k})$.<br>
        a) Determine la corriente total $I_1$ del cilindro interior.<br>
        b) Si las corrientes de ambos conductores son de igual magnitud y sentido opuesto, determine $\\alpha$ en función de $J_0, R_1$ y $R_2$.
      `,
      steps: [
        {
          title: 'Paso 1: Integral en dos dimensiones (radial y angular)',
          content: `
            En el cilindro interior, la densidad depende explícitamente del ángulo $\\theta$, por lo que no podemos reducir el diferencial a $2\\pi r dr$:
            $$d\\vec{A} = r\\,dr\\,d\\theta\\,\\hat{k}$$
            $$I_1 = \\int_0^{R_1} r\\,dr \\int_0^{2\\pi} \\alpha \\sin^2(\\theta)\\,d\\theta$$
          `
        },
        {
          title: 'Paso 2: Uso del formulario oficial para la integral trigonométrica',
          content: `
            Del formulario de integrales oficial: $\\int \\sin^2\\theta d\\theta = \\frac{\\theta}{2} - \\frac{\\sin 2\\theta}{4}$.<br>
            Evaluando en $[0, 2\\pi]$:
            $$\\int_0^{2\\pi} \\sin^2(\\theta)\\,d\\theta = \\left[\\frac{\\theta}{2} - \\frac{\\sin 2\\theta}{4}\\right]_0^{2\\pi} = \\frac{2\\pi}{2} - 0 = \\pi$$
            La integral radial es simplemente:
            $$\\int_0^{R_1} r\\,dr = \\frac{R_1^2}{2}$$
            Por lo tanto:
            $$I_1 = \\alpha \\cdot \\pi \\cdot \\frac{R_1^2}{2} = \\frac{\\pi \\alpha R_1^2}{2}$$
          `
        },
        {
          title: 'Paso 3: Condición de compensación con el cascarón exterior',
          content: `
            El cascarón exterior tiene sección circular entre $R_1$ y $R_2$:
            $$A_{ext} = \\pi(R_2^2 - R_1^2)$$
            Como su densidad es uniforme con magnitud $J_0$:
            $$I_2 = J_0 \\pi(R_2^2 - R_1^2)$$
            Igualando magnitudes de corriente ($I_1 = I_2$):
            $$\\frac{\\pi \\alpha R_1^2}{2} = J_0 \\pi (R_2^2 - R_1^2)$$
            Simplificando $\\pi$ y despejando la constante $\\alpha$:
            $$\\alpha = \\frac{2J_0 (R_2^2 - R_1^2)}{R_1^2} = 2J_0 \\left(\\frac{R_2^2}{R_1^2} - 1\\right)$$
          `
        }
      ]
    },
    {
      id: 'm2_ex8',
      title: 'Efecto Pelicular en Telecomunicaciones',
      level: 'certamen',
      source: 'Pauta C3 Problema 1 Conceptual',
      type: 'conceptual',
      statement: `
        ¿Por qué en aplicaciones de alta frecuencia (como radiofrecuencia o telecomunicaciones) la corriente tiende a concentrarse en la superficie del conductor (efecto pelicular) en lugar de distribuirse uniformemente?
      `,
      modelAnswer: `
        El efecto pelicular (*skin effect*) es una consecuencia directa de la <strong>Ley de Faraday-Lenz</strong> aplicada al interior del propio conductor.<br><br>
        Cuando una corriente alterna $I(t)$ de alta frecuencia circula por un conductor, produce un campo magnético variable en el tiempo $\\vec{B}(t)$ concéntrico dentro del material. Este flujo magnético variable induce campos eléctricos inducidos y corrientes parásitas (de Foucault) que, por la Ley de Lenz, se oponen a la variación de la corriente en el núcleo del conductor, debilitando fuertemente el flujo de carga en el centro.<br><br>
        En cambio, hacia la periferia exterior, el apantallamiento de flujo es menor y las corrientes inducidas refuerzan la corriente principal. Esto produce una densidad de corriente $J(r)$ que crece exponencialmente hacia el borde, confinando la conducción a una capa superficial delgada llamada *profundidad de penetración* ($\\delta = \\sqrt{2/\\omega \\mu \\sigma}$).
      `,
      rubric: `
        • 5 pts: Relacionar el fenómeno con la inducción electromagnética (Faraday-Lenz) debida a corrientes alternas.<br>
        • 5 pts: Explicar cómo las corrientes parásitas internas cancelan el flujo central y refuerzan la periferia.
      `
    }
  ]
};
