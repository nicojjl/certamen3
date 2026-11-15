/**
 * MÓDULO 7: AUTOINDUCTANCIA Y ENERGÍA MAGNÉTICA
 * FIS120 / FIS12125 · UTFSM
 */

window.MODULE_DATA_MOD7 = {
  number: '7',
  title: 'Autoinductancia y Energía Magnética',
  description: 'Cálculo de inductancia propia L en solenoides y toroides, fem autoinducida de Faraday, densidad de energía magnética u_B y almacenamiento en inductores.',
  hasInteractive: false,
  theory: `
    <p>
      Todo circuito por el que circula una corriente variable produce un campo magnético que atraviesa su propia área, generando un flujo propio. La variación de este flujo induce una fem en el propio conductor que se opone a cualquier cambio de la corriente que lo alimenta. Este fenómeno se denomina <strong>autoinducción</strong>.
    </p>

    <div class="box-formula">
      <strong>1. Fórmulas Fundamentales (Formulario C3):</strong>
      <p>
        • <strong>Definición de Autoinductancia:</strong>
        $$L = \\frac{N \\phi_B}{I}$$
        • <strong>fem Autoinducida (Ley de Faraday en Inductores):</strong>
        $$\\varepsilon_L = -L \\frac{di}{dt}$$
        • <strong>Autoinductancia de un Solenoide Ideal:</strong>
        $$L = \\mu_0 n^2 l A = \\mu_0 \\frac{N^2}{l} A$$
        donde $n = N/l$ es el número de vueltas por metro, $l$ es la longitud y $A = \\pi R^2$ es el área transversal.
        <br>• <strong>Energía Almacenada en el Inductor:</strong>
        $$U_L = \\frac{1}{2} L I^2$$
      </p>
    </div>

    <div class="box-method">
      <strong>2. Densidad Volumétrica de Energía Magnética:</strong>
      <p>
        La energía magnética no está localizada en el alambre, sino almacenada en el propio <strong>campo magnético</strong> distribuido por el espacio con una densidad volumétrica:
        $$u_B = \\frac{B^2}{2\\mu_0} \\quad \\left[\\frac{\\text{J}}{\\text{m}^3}\\right]$$
        Para un solenoide ideal, donde el campo interior es uniforme ($B = \\mu_0 n I$) y nulo afuera:
        $$U_L = \\iiint u_B\\,dV = u_B \\cdot (A \\cdot l) = \\left( \\frac{(\\mu_0 n I)^2}{2\\mu_0} \\right) (A l) = \\frac{1}{2} (\\mu_0 n^2 l A) I^2 = \\frac{1}{2} L I^2$$
        ¡Ambas descripciones son rigurosamente idénticas!
      </p>
    </div>

    <div class="box-warning">
      <strong>Propiedad Inercial Fundamental del Inductor:</strong><br>
      La corriente $i(t)$ a través de un inductor es una <strong>función continua del tiempo</strong>. No puede cambiar instantáneamente de valor ($i(0^+) = i(0^-)$), ya que un salto discontinuo implicaría $\\frac{di}{dt} \\to \\infty$, lo cual exigiría un voltaje infinito y una potencia infinita, algo físicamente imposible en la naturaleza.
    </div>
  `,
  exercises: [
    {
      id: 'm7_ex1',
      title: 'Autoinductancia de Solenoide Ideal',
      level: 'basic',
      source: 'Formulario C3 (oficial)',
      type: 'multiple_choice',
      statement: `
        Un solenoide ideal de longitud $l = 0.50\\text{ m}$ y radio $r = 0.020\\text{ m}$ tiene $n = 1000\\text{ vueltas/m}$. ¿Cuál es su autoinductancia $L$?
      `,
      options: [
        '$7.90 \\times 10^{-4}\\text{ H} \\approx 0.79\\text{ mH}$',
        '$1.58 \\times 10^{-3}\\text{ H}$',
        '$3.95 \\times 10^{-4}\\text{ H}$',
        '$7.90 \\times 10^{-2}\\text{ H}$'
      ],
      correctOption: 0,
      explanation: `
        El área transversal es $A = \\pi r^2 = \\pi (0.020)^2 = 4\\pi \\times 10^{-4}\\text{ m}^2$.<br>
        Aplicamos la fórmula del formulario oficial:
        $$L = \\mu_0 n^2 l A = (4\\pi \\times 10^{-7}) \\cdot (1000)^2 \\cdot 0.50 \\cdot (4\\pi \\times 10^{-4}) = 8\\pi^2 \\times 10^{-5} \\approx 7.896 \\times 10^{-4}\\text{ H} \\approx 0.79\\text{ mH}$$
      `
    },
    {
      id: 'm7_ex2',
      title: 'Energía Almacenada en Inductor',
      level: 'basic',
      source: 'Formulario C3 (oficial)',
      type: 'numerical',
      statement: `
        Un inductor de $L = 0.80\\text{ H}$ conduce una corriente constante de $I = 3.0\\text{ A}$. Calcule la energía magnética almacenada $U_L$ en Joules.
      `,
      placeholder: 'Ej: 3.6',
      units: 'J',
      correctValue: 3.6,
      tolerance: 0.02,
      explanation: `
        $$U_L = \\frac{1}{2} L I^2 = \\frac{1}{2} (0.80\\text{ H}) (3.0\\text{ A})^2 = 0.40 \\cdot 9.0 = 3.60\\text{ J}$$
      `
    },
    {
      id: 'm7_ex3',
      title: 'Dependencia Cuadrática de Vueltas',
      level: 'intermediate',
      source: 'Ejercicio original (no oficial)',
      type: 'true_false',
      statement: `
        Si duplicamos el número de vueltas por metro $n$ en un solenoide manteniendo fijas su longitud y radio, la autoinductancia $L$ se cuadruplica ($4L$).
      `,
      correct: true,
      justification: `
        Verdadero. Como se observa en la fórmula oficial $L = \\mu_0 n^2 l A$, la inductancia es cuadrática en $n$. Esto se debe a dos efectos acumulativos: duplicar $n$ duplica el campo magnético $B = \\mu_0 n I$ para una corriente dada, y además duplica el número de espiras $N = nl$ que enlazan dicho flujo. $2 \\times 2 = 4$.
      `
    },
    {
      id: 'm7_ex4',
      title: 'fem Inducida en Apertura Brusca de Circuito',
      level: 'intermediate',
      source: 'Ejercicio original (no oficial)',
      type: 'numerical',
      statement: `
        Un inductor de $L = 0.40\\text{ H}$ transporta inicialmente una corriente de $2.0\\text{ A}$. Si al abrir un interruptor la corriente cae linealmente a cero en un intervalo de $\\Delta t = 4.0\\text{ ms} = 0.0040\\text{ s}$, calcule la magnitud de la fem autoinducida $|\\varepsilon_L|$ en voltios.
      `,
      placeholder: 'Ej: 200.0',
      units: 'V',
      correctValue: 200.0,
      tolerance: 0.03,
      explanation: `
        $$|\\varepsilon_L| = L \\left|\\frac{\\Delta i}{\\Delta t}\\right| = 0.40\\text{ H} \\cdot \\frac{2.0\\text{ A}}{0.0040\\text{ s}} = 0.40 \\cdot 500 = 200.0\\text{ V}$$
        Este elevado voltaje (mucho mayor que la fuente que alimentaba el circuito) explica el chispazo característico en los interruptores cuando se desconectan cargas inductivas (motores, bobinas).
      `
    },
    {
      id: 'm7_ex5',
      title: 'Autoinductancia de un Toroide de Sección Rectangular',
      level: 'certamen',
      source: 'Simulacro C3 Problema 1',
      type: 'step_by_step',
      figure: 'img/mod3_toroid_simulacro.svg',
      figureCaption: 'Toroide rectangular: radio interno $a$, externo $b$, altura $h$ y $N$ espiras.',
      statement: `
        Un toroide ideal de sección rectangular tiene radio interno $a$, radio externo $b$ y altura $h$, con $N$ vueltas de alambre distribuidas uniformemente. Determine analíticamente su coeficiente de autoinductancia $L$ a partir del flujo magnético enlazado.
      `,
      steps: [
        {
          title: 'Paso 1: Campo magnético interior por Ley de Ampère',
          content: `
            Del Módulo 3, el campo magnético en el interior del toroide ($a < r < b$) es azimutal:
            $$B(r) = \\frac{\\mu_0 N I}{2\\pi r}$$
          `
        },
        {
          title: 'Paso 2: Flujo magnético a través de una sola espira rectangular',
          content: `
            La sección transversal rectangular tiene ancho $dr$ y altura $h$, con elemento de área $dA = h\\,dr$:
            $$\\phi_1 = \\int_a^b B(r) h\\,dr = \\int_a^b \\left( \\frac{\\mu_0 N I}{2\\pi r} \\right) h\\,dr = \\frac{\\mu_0 N I h}{2\\pi} \\int_a^b \\frac{dr}{r} = \\frac{\\mu_0 N I h}{2\\pi} \\ln\\left(\\frac{b}{a}\\right)$$
          `
        },
        {
          title: 'Paso 3: Autoinductancia total',
          content: `
            El flujo total enlazado por las $N$ vueltas completas es $\\Phi_{total} = N \\phi_1$:
            $$\\Phi_{total} = \\frac{\\mu_0 N^2 I h}{2\\pi} \\ln\\left(\\frac{b}{a}\\right)$$
            Por la definición de autoinductancia $L = \\frac{\\Phi_{total}}{I}$:
            $$L = \\frac{\\mu_0 N^2 h}{2\\pi} \\ln\\left(\\frac{b}{a}\\right)$$
            <strong>Chequeo dimensional:</strong> $[\\mu_0 \\cdot h] = [\\text{H/m}] \\cdot [\\text{m}] = \\text{Henrio [H]}$. La función logaritmo es adimensional.
          `
        }
      ]
    },
    {
      id: 'm7_ex6',
      title: 'Equivalencia de Energía Magnética: Integral de Volumen',
      level: 'certamen',
      source: 'Ejercicio original (no oficial)',
      type: 'step_by_step',
      statement: `
        Demuestre que la energía acumulada en el toroide de sección rectangular obtenida mediante la integral volumétrica de la densidad de energía magnética $U = \\iiint \\frac{B^2}{2\\mu_0} dV$ coincide idénticamente con la fórmula de circuito $U = \\frac{1}{2} L I^2$.
      `,
      steps: [
        {
          title: 'Paso 1: Elemento de volumen en coordenadas cilíndricas',
          content: `
            Para el toroide centrado en el eje $z$, el campo no depende de $\\theta$ ni de $z$, solo del radio $r$.<br>
            El elemento diferencial de volumen de un anillo cilíndrico de radio $r$, espesor $dr$ y altura $h$ es:
            $$dV = (2\\pi r\\,dr) \\cdot h = 2\\pi h r\\,dr$$
          `
        },
        {
          title: 'Paso 2: Evaluación de la integral de densidad de energía',
          content: `
            Sustituimos $B(r) = \\frac{\\mu_0 N I}{2\\pi r}$:
            $$u_B(r) = \\frac{B(r)^2}{2\\mu_0} = \\frac{1}{2\\mu_0} \\left( \\frac{\\mu_0 N I}{2\\pi r} \\right)^2 = \\frac{\\mu_0 N^2 I^2}{8\\pi^2 r^2}$$
            Integramos sobre todo el volumen interior desde $r = a$ hasta $r = b$:
            $$U = \\int_a^b u_B(r) dV = \\int_a^b \\left( \\frac{\\mu_0 N^2 I^2}{8\\pi^2 r^2} \\right) (2\\pi h r\\,dr) = \\frac{\\mu_0 N^2 I^2 h}{4\\pi} \\int_a^b \\frac{dr}{r} = \\frac{\\mu_0 N^2 I^2 h}{4\\pi} \\ln\\left(\\frac{b}{a}\\right)$$
          `
        },
        {
          title: 'Paso 3: Comparación con 1/2 L I²',
          content: `
            Reescribimos la expresión factorizando $\\frac{1}{2} I^2$:
            $$U = \\frac{1}{2} \\left( \\frac{\\mu_0 N^2 h}{2\\pi} \\ln\\left(\\frac{b}{a}\\right) \\right) I^2$$
            Reconociendo el término entre paréntesis como la inductancia propia $L$ del toroide:
            $$U = \\frac{1}{2} L I^2$$
            ¡Queda rigurosamente demostrado que la energía electromagnética está almacenada en el campo magnético del espacio!
          `
        }
      ]
    },
    {
      id: 'm7_ex7',
      title: 'Condición de Continuidad de la Corriente en Inductores',
      level: 'certamen',
      source: 'Ejercicio original (no oficial)',
      type: 'conceptual',
      statement: `
        Explique por qué la corriente que circula por un inductor ideal debe ser continua en el tiempo ($i(0^+) = i(0^-)$) al conmutar un interruptor en un circuito, mientras que el voltaje en los terminales del inductor sí puede experimentar un salto brusco.
      `,
      modelAnswer: `
        La relación constitutiva del inductor ideal es $v_L(t) = L \\frac{di}{dt}$ y su energía almacenada es $U_L = \\frac{1}{2} L i^2$.<br><br>
        1. <strong>Continuidad de la corriente y conservación de energía:</strong><br>
        Si la corriente $i(t)$ sufriera un cambio discontinuo (un salto finito en un tiempo $\\Delta t \\to 0$), la derivada $\\frac{di}{dt}$ tendería a infinito, lo que generaría un voltaje inducido infinito $v_L \\to \\infty$. Además, la potencia instantánea $P(t) = v_L(t) i(t)$ y la tasa de transferencia de energía $\\frac{dU_L}{dt}$ serían infinitas. Dado que ninguna fuente física real puede suministrar potencia infinita, la energía magnética $U_L$ no puede cambiar instantáneamente, exigiendo que la corriente sea estrictamente continua:
        $$i(t^+) = i(t^-)$$
        <br>
        2. <strong>Salto del voltaje:</strong><br>
        Por el contrario, el voltaje $v_L(t) = L \\frac{di}{dt}$ depende de la <em>pendiente</em> de la corriente. La pendiente de una función continua sí puede cambiar abruptamente en un instante dado (por ejemplo, una curva con un vértice o quiebre suave en $t=0$). Por lo tanto, el voltaje del inductor sí puede saltar instantáneamente entre dos valores finitos distintos al conmutar un interruptor.
      `,
      rubric: `
        • 5 pts: Demostrar que un salto en i(t) implicaría di/dt -> infinito y potencia infinita.<br>
        • 5 pts: Explicar por qué el voltaje sí puede ser discontinuo basándose en el cambio de pendiente.
      `
    }
  ]
};
