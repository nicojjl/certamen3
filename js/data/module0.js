/**
 * MÓDULO 0: REPASO MATEMÁTICO Y CONCEPTUAL PARA CERTAMEN 3
 * FIS120 / FIS12125 · UTFSM
 */

const MODULE_DATA_MOD0 = {
  number: '0',
  title: 'Repaso Matemático y Conceptual para C3',
  description: 'Herramientas matemáticas esenciales para el Certamen 3: álgebra vectorial, regla de la mano derecha, coordenadas cilíndricas, integrales del formulario oficial y análisis dimensional de unidades del SI.',
  hasInteractive: false,
  theory: `
    <p>
      El Certamen 3 de FIS120/121 evalúa electromagnetismo aplicado mediante integrales de línea (Ampère, Faraday) e integrales de superficie (densidad de corriente, flujo magnético). Dominar la orientación de vectores y la base cilíndrica es el primer paso indispensable para no perder puntos en signos y diferenciales.
    </p>

    <div class="box-formula">
      <strong>1. Productos Vectoriales y Regla de la Mano Derecha:</strong>
      <p>
        • <strong>Producto Punto (Escalar):</strong> $\\vec{A}\\cdot\\vec{B} = A_x B_x + A_y B_y + A_z B_z = |\\vec{A}||\\vec{B}|\\cos\\theta$. Mide la proyección paralela. Es conmutativo: $\\vec{A}\\cdot\\vec{B} = \\vec{B}\\cdot\\vec{A}$.<br>
        • <strong>Producto Cruz (Vectorial):</strong> $\\vec{C} = \\vec{A}\\times\\vec{B} = (|\\vec{A}||\\vec{B}|\\sin\\theta)\\,\\hat{n}$. Es perpendicular tanto a $\\vec{A}$ como a $\\vec{B}$.<br>
        • <strong>Propiedad Anticonmutativa Crítica:</strong> $\\vec{B}\\times\\vec{A} = -(\\vec{A}\\times\\vec{B})$.
      </p>
    </div>

    <div class="figure-container">
      <img src="img/mod0_cross_product.svg" alt="Producto Cruz y Regla de la Mano Derecha">
      <div class="figure-caption">Regla de la mano derecha: dedos a lo largo de $\\vec{A}$, curvan hacia $\\vec{B}$, pulgar apunta en la dirección de $\\vec{A}\\times\\vec{B}$.</div>
    </div>

    <div class="box-formula">
      <strong>2. Coordenadas Cilíndricas $(r, \\theta, z)$:</strong>
      <p>
        La gran mayoría de los problemas de Ampère y Biot-Savart presentan simetría axial. La base local ortonormal es $\\{\\hat{r}, \\hat{\\theta}, \\hat{k}\\}$ donde:
      </p>
      $$\\hat{r} = \\cos\\theta\\,\\hat{\\imath} + \\sin\\theta\\,\\hat{\\jmath}, \\quad \\hat{\\theta} = -\\sin\\theta\\,\\hat{\\imath} + \\cos\\theta\\,\\hat{\\jmath}, \\quad \\hat{k} = \\hat{k}$$
      <p>
        <strong>Diferenciales Fundamentales:</strong><br>
        • <strong>De línea:</strong> $d\\vec{l} = dr\\,\\hat{r} + r\\,d\\theta\\,\\hat{\\theta} + dz\\,\\hat{k}$ (para un lazo circular de radio $R$, $d\\vec{l} = R\\,d\\theta\\,\\hat{\\theta}$).<br>
        • <strong>De superficie transversal (sección de cable perpendicular al eje $z$):</strong> $d\\vec{A} = r\\,dr\\,d\\theta\\,\\hat{k} = 2\\pi r\\,dr\\,\\hat{k}$ (si no hay dependencia en $\\theta$).<br>
        • <strong>De superficie lateral (manto cilíndrico de radio $R$):</strong> $d\\vec{A} = R\\,d\\theta\\,dz\\,\\hat{r}$.
      </p>
    </div>

    <div class="figure-container">
      <img src="img/mod0_coords.svg" alt="Coordenadas Cilíndricas">
      <div class="figure-caption">Base local cilíndrica $(\\hat{r}, \\hat{\\theta}, \\hat{k})$ y su proyección en el plano $xy$.</div>
    </div>

    <div class="box-method">
      <strong>3. Unidades del SI y Equivalencias Clave:</strong>
      <p>
        • <strong>Campo Magnético ($B$):</strong> $[B] = \\text{Tesla } [\\text{T}] = \\frac{\\text{N}}{\\text{A}\\cdot\\text{m}} = \\frac{\\text{V}\\cdot\\text{s}}{\\text{m}^2}$.<br>
        • <strong>Flujo Magnético ($\\phi_B$):</strong> $[\\phi_B] = \\text{Weber } [\\text{Wb}] = \\text{T}\\cdot\\text{m}^2 = \\text{V}\\cdot\\text{s}$.<br>
        • <strong>Inductancia ($L, M$):</strong> $[L] = \\text{Henrio } [\\text{H}] = \\frac{\\text{Wb}}{\\text{A}} = \\frac{\\text{V}\\cdot\\text{s}}{\\text{A}} = \\Omega\\cdot\\text{s}$.<br>
        • <strong>Permeabilidad del vacío ($\\mu_0$):</strong> $[\\mu_0] = 4\\pi\\times 10^{-7} \\left[\\frac{\\text{H}}{\\text{m}}\\right] = \\left[\\frac{\\text{T}\\cdot\\text{m}}{\\text{A}}\\right] = \\left[\\frac{\\text{N}}{\\text{A}^2}\\right]$.<br>
        • <strong>Constantes de tiempo:</strong> $[\\tau_C] = [RC] = \\Omega\\cdot\\text{F} = \\text{segundos } [\\text{s}]$. $[\\tau_L] = [L/R] = \\frac{\\Omega\\cdot\\text{s}}{\\Omega} = \\text{segundos } [\\text{s}]$.
      </p>
    </div>

    <div class="box-warning">
      <strong>Errores Frecuentes en el Certamen:</strong><br>
      1. Olvidar el jacobiano $r$ al integrar en coordenadas polares/cilíndricas: escribir $dr\\,d\\theta$ en vez de $r\\,dr\\,d\\theta$.<br>
      2. No respetar la regla de la mano derecha entre el sentido de circulación del lazo $d\\vec{l}$ y el vector normal $d\\vec{A}$.<br>
      3. Mezclar vectores cartesianos fijos $(\\hat{\\imath}, \\hat{\\jmath})$ con versores cilíndricos $(\\hat{r}, \\hat{\\theta})$ que dependen de la posición angular $\\theta$.
    </div>
  `,
  exercises: [
    {
      id: 'm0_ex1',
      title: 'Producto Cruz de Versores Canónicos',
      level: 'basic',
      source: 'Repaso Teórico UTFSM',
      type: 'multiple_choice',
      statement: `
        Un electrón se mueve en la dirección $+x$ (versor $\\hat{\\imath}$) en una región con campo magnético uniforme apuntando en la dirección $+y$ (versor $\\hat{\\jmath}$). ¿Hacia qué dirección apunta la fuerza magnética $\\vec{F} = q(\\vec{v}\\times\\vec{B})$ sobre el electrón?
      `,
      options: [
        'Hacia $+z$ (versor $+\\hat{k}$)',
        'Hacia $-z$ (versor $-\\hat{k}$)',
        'Hacia $+y$ (versor $+\\hat{\\jmath}$)',
        'La fuerza es nula porque $\\vec{v}$ y $\\vec{B}$ son perpendiculares'
      ],
      correctOption: 1,
      explanation: `
        Calculamos primero el producto vectorial de las direcciones: $\\hat{\\imath}\\times\\hat{\\jmath} = +\\hat{k}$.<br>
        Como la carga del electrón es negativa ($q = -e < 0$), la fuerza magnética resulta:
        $$\\vec{F} = (-e)(v\\hat{\\imath}\\times B\\hat{\\jmath}) = -evB(\\hat{\\imath}\\times\\hat{\\jmath}) = -evB\\,\\hat{k}$$
        Por lo tanto, la fuerza apunta en la dirección $-\\hat{k}$ (hacia el eje $-z$).
      `
    },
    {
      id: 'm0_ex2',
      title: 'Flujo Vectorial con Producto Punto',
      level: 'basic',
      source: 'Fundamentos FIS120',
      type: 'numerical',
      statement: `
        Un campo magnético uniforme de magnitud $B = 0.50\\text{ T}$ atraviesa un plano rectangular de lados $a = 0.20\\text{ m}$ y $b = 0.30\\text{ m}$. Si el vector normal a la superficie forma un ángulo $\\theta = 60^\\circ$ con las líneas de campo $\\vec{B}$, calcule el flujo magnético $\\phi_B$ a través del rectángulo.
      `,
      placeholder: 'Ej: 0.015',
      units: 'Wb',
      correctValue: 0.015,
      tolerance: 0.03,
      explanation: `
        El área del rectángulo es $A = a\\cdot b = 0.20 \\cdot 0.30 = 0.060\\text{ m}^2$.<br>
        Dado que el campo es uniforme:
        $$\\phi_B = \\vec{B}\\cdot\\vec{A} = B A \\cos\\theta = 0.50 \\cdot 0.060 \\cdot \\cos(60^\\circ) = 0.030 \\cdot 0.5 = 0.015\\text{ Wb}$$
      `
    },
    {
      id: 'm0_ex3',
      title: 'Anticonmutatividad y Orientación de Lazos',
      level: 'intermediate',
      source: 'Concepto Ampère UTFSM',
      type: 'true_false',
      statement: `
        Si invertimos el sentido en que recorremos un lazo amperiano cerrado $\\Gamma$ (de sentido antihorario a sentido horario), la circulación magnética $\\oint_\\Gamma \\vec{B}\\cdot d\\vec{l}$ cambia de signo.
      `,
      correct: true,
      justification: `
        Verdadero. Al invertir el sentido de recorrido del lazo, el elemento diferencial de trayectoria cambia de $d\\vec{l}$ a $-d\\vec{l}$. Por linealidad de la integral:
        $$\\oint_{-\\Gamma} \\vec{B}\\cdot d\\vec{l} = -\\oint_\\Gamma \\vec{B}\\cdot d\\vec{l}$$
        Esto coincide con la regla de la mano derecha: el vector área normal asociado $d\\vec{A}$ también invierte su signo, haciendo coherente $\\mu_0 I_{enl}$.
      `
    },
    {
      id: 'm0_ex4',
      title: 'Análisis Dimensional de la Permeabilidad Magnética',
      level: 'intermediate',
      source: 'Formulario C3',
      type: 'multiple_choice',
      statement: `
        A partir de la Ley de Biot-Savart $dB = \\frac{\\mu_0}{4\\pi} \\frac{I dl \\sin\\theta}{r^2}$ y sabiendo que la fuerza de Lorentz es $F = qvB = I L B$, ¿cuál de las siguientes combinaciones representa dimensionalmente a $\\mu_0$?
      `,
      options: [
        '$\\text{N} / \\text{A}^2$',
        '$\\text{N} \\cdot \\text{A}$',
        '$\\text{T} \\cdot \\text{m}^2 / \\text{A}$',
        '$\\text{V} / (\\text{A}\\cdot\\text{m})$'
      ],
      correctOption: 0,
      explanation: `
        Despejando $\\mu_0$: $[\\mu_0] = [B] \\cdot [r^2] / ([I] \\cdot [dl]) = [B] \\cdot \\text{m} / \\text{A}$.<br>
        De la fuerza magnética: $[B] = [F] / ([I]\\cdot [L]) = \\text{N} / (\\text{A}\\cdot\\text{m})$.<br>
        Sustituyendo: $[\\mu_0] = \\left(\\frac{\\text{N}}{\\text{A}\\cdot\\text{m}}\\right) \\cdot \\frac{\\text{m}}{\\text{A}} = \\frac{\\text{N}}{\\text{A}^2}$.<br>
        También es equivalente a $\\text{T}\\cdot\\text{m}/\\text{A}$ y a $\\text{H}/\\text{m}$.
      `
    },
    {
      id: 'm0_ex5',
      title: 'Jacobiano en Integrales de Sección Circular',
      level: 'intermediate',
      source: 'Cálculo Vectorial para Física',
      type: 'multiple_choice',
      statement: `
        En un cable cilíndrico de radio $R$, se desea calcular la corriente total $I = \\iint \\vec{J}\\cdot d\\vec{A}$ donde $\\vec{J} = J(r)\\,\\hat{k}$. ¿Cuál es la expresión correcta para el diferencial de área $d\\vec{A}$ en el plano transversal perpendicular a $\\hat{k}$?
      `,
      options: [
        '$d\\vec{A} = r\\,dr\\,d\\theta\\,\\hat{k}$ (o $2\\pi r\\,dr\\,\\hat{k}$ al integrar en $\\theta$)',
        '$d\\vec{A} = dr\\,d\\theta\\,\\hat{k}$',
        '$d\\vec{A} = \\pi r^2\\,dr\\,\\hat{k}$',
        '$d\\vec{A} = r^2\\sin\\theta\\,dr\\,d\\theta\\,\\hat{k}$'
      ],
      correctOption: 0,
      explanation: `
        En coordenadas cilíndricas/polares, la transformación desde cartesianas $(x=r\\cos\\theta, y=r\\sin\\theta)$ tiene como determinante del jacobiano $J = r$. Por tanto, el elemento diferencial de área transversal es $dA = r\\,dr\\,d\\theta$. Al no haber dependencia angular en la densidad de corriente, $\\int_0^{2\\pi} d\\theta = 2\\pi$, quedando el conocido anillo circular diferencial $dA = 2\\pi r\\,dr$.
      `
    },
    {
      id: 'm0_ex6',
      title: 'Equivalencia Dimensional de las Constantes de Tiempo',
      level: 'certamen',
      source: 'Pauta C3 2026-1 / Formulario',
      type: 'conceptual',
      statement: `
        Demuestre mediante análisis dimensional riguroso a partir de las leyes fundamentales del formulario (Ley de Ohm $V=IR$, definición de capacitancia $Q=CV$ y fem de autoinductancia $\\varepsilon_L = -L\\frac{di}{dt}$) que tanto $\\tau_C = RC$ como $\\tau_L = \\frac{L}{R}$ tienen unidades de tiempo (segundos).
      `,
      modelAnswer: `
        <strong>1. Demostración para $\\tau_C = RC$:</strong><br>
        • De la Ley de Ohm: $[R] = \\frac{[V]}{[I]} = \\frac{\\text{Volt}}{\\text{Amperio}}$.<br>
        • De la capacitancia $C = Q/V$: $[C] = \\frac{[Q]}{[V]} = \\frac{\\text{Coulomb}}{\\text{Volt}}$.<br>
        • Recordando que corriente es carga por unidad de tiempo: $I = dq/dt \\implies [I] = \\frac{\\text{Coulomb}}{\\text{segundo}}$, es decir, $\\text{Coulomb} = \\text{Amperio}\\cdot\\text{segundo}$.<br>
        • Multiplicando:
        $$[RC] = [R]\\cdot [C] = \\left(\\frac{\\text{V}}{\\text{A}}\\right) \\cdot \\left(\\frac{\\text{A}\\cdot\\text{s}}{\\text{V}}\\right) = \\text{s (segundos)}$$
        <br>
        <strong>2. Demostración para $\\tau_L = L/R$:</strong><br>
        • De la fem inducida $|\\varepsilon_L| = L \\frac{di}{dt}$: $[L] = \\frac{[V]\\cdot [dt]}{[di]} = \\frac{\\text{Volt}\\cdot\\text{segundo}}{\\text{Amperio}}$.<br>
        • Por lo tanto, dividiendo por la resistencia $[R] = \\frac{\\text{Volt}}{\\text{Amperio}}$:
        $$\\left[\\frac{L}{R}\\right] = \\frac{\\frac{\\text{V}\\cdot\\text{s}}{\\text{A}}}{\\frac{\\text{V}}{\\text{A}}} = \\text{s (segundos)}$$
        Ambas constantes de tiempo caracterizan la rapidez de relajación exponencial $e^{-t/\\tau}$ del circuito.
      `,
      rubric: `
        • 5 pts: Deducción correcta y ordenada de las unidades de $[RC] = \\text{s}$.<br>
        • 5 pts: Deducción correcta de $[L/R] = \\text{s}$ mediante la ley de Faraday/autoinductancia.
      `
    },
    {
      id: 'm0_ex7',
      title: 'Circulación Vectorial sobre Trayectoria Circular',
      level: 'certamen',
      source: 'Método Ampère UTFSM',
      type: 'step_by_step',
      statement: `
        Considere un campo vectorial en el plano $xy$ dado en coordenadas cilíndricas por $\\vec{F} = \\frac{K}{r}\\,\\hat{\\theta}$, donde $K$ es una constante. Calcule la integral de línea $\\oint_\\Gamma \\vec{F}\\cdot d\\vec{l}$ a lo largo de una circunferencia de radio $R$ centrada en el origen, recorrida en sentido antihorario.
      `,
      steps: [
        {
          title: 'Paso 1: Parametrización de la trayectoria y diferencial de línea',
          content: `
            La trayectoria $\\Gamma$ es un círculo de radio fijo $r = R$ en el plano $xy$.<br>
            El elemento diferencial de línea en coordenadas cilíndricas con $r$ y $z$ constantes es:
            $$d\\vec{l} = R\\,d\\theta\\,\\hat{\\theta}$$
            El sentido antihorario corresponde a integrar $\\theta$ desde $0$ hasta $2\\pi$.
          `
        },
        {
          title: 'Paso 2: Evaluación del producto punto sobre la trayectoria',
          content: `
            Evaluamos el campo sobre el círculo $r = R$:
            $$\\vec{F}(R, \\theta) = \\frac{K}{R}\\,\\hat{\\theta}$$
            Efectuamos el producto punto con $d\\vec{l}$:
            $$\\vec{F}\\cdot d\\vec{l} = \\left(\\frac{K}{R}\\,\\hat{\\theta}\\right) \\cdot (R\\,d\\theta\\,\\hat{\\theta}) = \\frac{K}{R} R\\,d\\theta (\\hat{\\theta}\\cdot\\hat{\\theta}) = K\\,d\\theta$$
            Observe que la magnitud $R$ se cancela exactamente y el producto punto de versores ortonormales es $\\hat{\\theta}\\cdot\\hat{\\theta} = 1$.
          `
        },
        {
          title: 'Paso 3: Integración y resultado analítico',
          content: `
            Integrando a lo largo del lazo cerrado:
            $$\\oint_\\Gamma \\vec{F}\\cdot d\\vec{l} = \\int_0^{2\\pi} K\\,d\\theta = K [\\theta]_0^{2\\pi} = 2\\pi K$$
            <strong>Chequeo físico:</strong> Este es exactamente el mecanismo por el cual el campo de un cable infinito $\\vec{B} = \\frac{\\mu_0 I}{2\\pi r}\\hat{\\theta}$ cumple la Ley de Ampère:
            $$\\oint \\vec{B}\\cdot d\\vec{l} = \\oint \\left(\\frac{\\mu_0 I}{2\\pi r}\\hat{\\theta}\\right)\\cdot (r\\,d\\theta\\,\\hat{\\theta}) = \\frac{\\mu_0 I}{2\\pi} \\cdot 2\\pi = \\mu_0 I$$
            ¡El radio del lazo no altera el resultado siempre que encierre a la fuente!
          `
        }
      ]
    },
    {
      id: 'm0_ex8',
      title: 'Comportamiento Asintótico de Integrales del Formulario',
      level: 'intermediate',
      source: 'Formulario C3',
      type: 'multiple_choice',
      statement: `
        El formulario oficial incluye la integral $\\int \\frac{1}{(a^2 + x^2)^{3/2}} dx = \\frac{x}{a^2\\sqrt{x^2 + a^2}}$. Al evaluar esta integral para un cable recto muy largo que se extiende desde $x = -L$ hasta $x = +L$ cuando $L \\to \\infty$, ¿cuál es el valor de $\\int_{-\\infty}^{+\\infty} \\frac{1}{(a^2 + x^2)^{3/2}} dx$?
      `,
      options: [
        '$\\frac{2}{a^2}$',
        '$\\frac{1}{a^2}$',
        '$\\frac{\\pi}{a^2}$',
        '$\\infty$'
      ],
      correctOption: 0,
      explanation: `
        Evaluamos los límites:
        $$\\lim_{x\\to +\\infty} \\frac{x}{a^2\\sqrt{x^2 + a^2}} = \\lim_{x\\to +\\infty} \\frac{x}{a^2 x\\sqrt{1 + a^2/x^2}} = \\frac{1}{a^2}$$
        $$\\lim_{x\\to -\\infty} \\frac{x}{a^2\\sqrt{x^2 + a^2}} = -\\frac{1}{a^2}$$
        Restando límite superior menos límite inferior:
        $$\\int_{-\\infty}^{+\\infty} \\frac{1}{(a^2 + x^2)^{3/2}} dx = \\frac{1}{a^2} - \\left(-\\frac{1}{a^2}\\right) = \\frac{2}{a^2}$$
        Este cálculo exacto es el que produce el factor 2 en el campo de un cable infinito por Biot-Savart: $B = \\frac{\\mu_0 I a}{4\\pi} \\left(\\frac{2}{a^2}\\right) = \\frac{\\mu_0 I}{2\\pi a}$.
      `
    }
  ]
};
