/**
 * MÓDULO 9: CIRCUITOS OSCILANTES LC Y RLC
 * FIS120 / FIS12125 · UTFSM
 */

const MODULE_DATA_MOD9 = {
  number: '9',
  title: 'Circuitos Oscilantes LC y RLC',
  description: 'Oscilaciones libres LC, frecuencia de resonancia natural, amortiguamiento RLC serie, regímenes subamortiguado, crítico y sobreamortiguado según el formulario oficial.',
  hasInteractive: true,
  theory: `
    <p>
      La combinación de un capacitor (que almacena energía eléctrica en su campo $\\vec{E}$) y un inductor (que almacena energía magnética en su campo $\\vec{B}$) constituye el análogo electromagnético del oscilador armónico mecánico (masa-resorte). La adición de una resistencia introduce disipación de energía, equivalente al rozamiento viscoso.
    </p>

    <div class="box-formula">
      <strong>1. Parámetros del Formulario Oficial C3:</strong>
      <p>
        • <strong>Frecuencia Angular Natural (No Amortiguada):</strong>
        $$\\omega_0 = \\frac{1}{\\sqrt{LC}}$$
        • <strong>Factor de Amortiguamiento:</strong>
        $$\\alpha = \\frac{R}{2L}$$
        • <strong>Frecuencia Angular Amortiguada:</strong>
        $$\\omega' = \\sqrt{\\omega_0^2 - \\alpha^2}$$
      </p>
    </div>

    <div class="box-method">
      <strong>2. Clasificación de Regímenes de Amortiguamiento (Formulario C3):</strong>
      <table style="width: 100%; border-collapse: collapse; margin-top: 0.6rem; font-size: 0.95rem;">
        <tr style="border-bottom: 1px solid var(--border-color); background: var(--bg-tertiary);">
          <th style="padding: 0.5rem; text-align: left;">Régimen</th>
          <th style="padding: 0.5rem; text-align: left;">Condición</th>
          <th style="padding: 0.5rem; text-align: left;">Comportamiento Físico</th>
        </tr>
        <tr style="border-bottom: 1px solid var(--border-color);">
          <td style="padding: 0.5rem;"><strong>Subamortiguado</strong></td>
          <td style="padding: 0.5rem;">$\\alpha < \\omega_0 \\iff R < 2\\sqrt{\\frac{L}{C}}$</td>
          <td style="padding: 0.5rem;">La carga oscila a frecuencia $\\omega'$ con envolvente que decae exponencialmente como $e^{-\\alpha t}$.</td>
        </tr>
        <tr style="border-bottom: 1px solid var(--border-color);">
          <td style="padding: 0.5rem;"><strong>Críticamente Amortiguado</strong></td>
          <td style="padding: 0.5rem;">$\\alpha = \\omega_0 \\iff R = 2\\sqrt{\\frac{L}{C}}$</td>
          <td style="padding: 0.5rem;">No hay oscilaciones. Es el retorno <strong>más rápido posible</strong> al estado de equilibrio sin cruzar el eje.</td>
        </tr>
        <tr>
          <td style="padding: 0.5rem;"><strong>Sobreamortiguado</strong></td>
          <td style="padding: 0.5rem;">$\\alpha > \\omega_0 \\iff R > 2\\sqrt{\\frac{L}{C}}$</td>
          <td style="padding: 0.5rem;">Gran resistencia disipa la energía velozmente; decaimiento asintótico lento dominado por exponenciales decrecientes.</td>
        </tr>
      </table>
    </div>

    <div class="box-formula">
      <strong>3. Solución Exacta Subamortiguada (Formulario C3):</strong>
      $$-L\\frac{d^2q}{dt^2} - R\\frac{dq}{dt} - \\frac{q}{C} = 0$$
      $$q(t) = Q_0 \\frac{\\omega_0}{\\omega'} e^{-\\alpha t} \\cos\\left(\\omega' t - \\arctan\\left(\\frac{\\alpha}{\\omega'}\\right)\\right)$$
      <p style="margin-top: 0.5rem;">
        Observe el desfase inicial: en $t = 0$, $\\cos(-\\arctan(\\alpha/\\omega')) = \\frac{\\omega'}{\\sqrt{\\omega'^2 + \\alpha^2}} = \\frac{\\omega'}{\\omega_0}$, lo que garantiza con rigor que $q(0) = Q_0$ e $i(0) = 0$.
      </p>
    </div>

    <div class="box-warning">
      <strong>Errores Fatales en el Certamen:</strong><br>
      1. Confundir la frecuencia natural $\\omega_0 = 1/\\sqrt{LC}$ con la frecuencia amortiguada real $\\omega' = \\sqrt{\\omega_0^2 - \\alpha^2}$. Si hay resistencia $R > 0$, el circuito oscila a frecuencia $\\omega'$, que es <strong>estrictamente menor</strong> que $\\omega_0$.<br>
      2. Olvidar que el factor de amortiguamiento lleva un 2 en el denominador: $\\alpha = \\frac{R}{2L}$ (a diferencia de la constante de tiempo $\\tau_L = L/R$, donde $1/\\tau_L = R/L = 2\\alpha$).
    </div>
  `,
  exercises: [
    {
      id: 'm9_ex1',
      title: 'Frecuencia de Oscilación Natural en Circuito LC',
      level: 'basic',
      source: 'Formulario C3',
      type: 'multiple_choice',
      statement: `
        Un circuito LC ideal contiene un inductor de $L = 2.0\\text{ mH} = 2.0 \\times 10^{-3}\\text{ H}$ y un capacitor de $C = 5.0\\,\\mu\\text{F} = 5.0 \\times 10^{-6}\\text{ F}$. ¿Cuál es la frecuencia angular natural de oscilación $\\omega_0$?
      `,
      options: [
        '$10000\\text{ rad/s} = 1.0 \\times 10^4\\text{ rad/s}$',
        '$1000\\text{ rad/s}$',
        '$5000\\text{ rad/s}$',
        '$100\\text{ rad/s}$'
      ],
      correctOption: 0,
      explanation: `
        $$\\omega_0 = \\frac{1}{\\sqrt{LC}} = \\frac{1}{\\sqrt{(2.0 \\times 10^{-3}\\text{ H}) \\cdot (5.0 \\times 10^{-6}\\text{ F})}} = \\frac{1}{\\sqrt{10^{-8}}} = \\frac{1}{10^{-4}} = 10000\\text{ rad/s}$$
      `
    },
    {
      id: 'm9_ex2',
      title: 'Cálculo de Resistencia Crítica',
      level: 'basic',
      source: 'Condición Crítica Formulario',
      type: 'numerical',
      statement: `
        Para un circuito RLC serie con $L = 0.20\\text{ H}$ y $C = 5.0\\,\\mu\\text{F} = 5.0 \\times 10^{-6}\\text{ F}$, calcule el valor exacto de la resistencia $R_{crit}$ en ohmios para que el circuito esté críticamente amortiguado.
      `,
      placeholder: 'Ej: 400.0',
      units: 'Ω',
      correctValue: 400.0,
      tolerance: 0.02,
      explanation: `
        En el amortiguamiento crítico $\\alpha = \\omega_0$:
        $$\\frac{R}{2L} = \\frac{1}{\\sqrt{LC}} \\implies R_{crit} = 2\\sqrt{\\frac{L}{C}} = 2\\sqrt{\\frac{0.20}{5.0 \\times 10^{-6}}} = 2\\sqrt{40000} = 2 \\cdot 200 = 400.0\\,\\Omega$$
      `
    },
    {
      id: 'm9_ex3',
      title: 'Conservación de Energía en Circuito LC Libre',
      level: 'intermediate',
      source: 'Física Térmica y Electromagnetismo',
      type: 'true_false',
      statement: `
        En un circuito LC ideal libre (sin resistencia $R = 0$), cuando la carga en el capacitor es exactamente la mitad de su valor máximo ($q(t) = Q_0/2$), el $75\\%$ de la energía total del circuito reside en forma de energía magnética en el inductor.
      `,
      correct: true,
      justification: `
        Verdadero. La energía electrostática en el capacitor es cuadrática en la carga:
        $$U_C = \\frac{q^2}{2C} = \\frac{(Q_0/2)^2}{2C} = \\frac{1}{4} \\left(\\frac{Q_0^2}{2C}\\right) = 0.25\\,U_{total}$$
        Por el principio de conservación de energía en un circuito LC ideal ($U_{total} = U_C + U_L = \\text{constante}$):
        $$U_L = U_{total} - U_C = U_{total} - 0.25\\,U_{total} = 0.75\\,U_{total} \\quad (75\\%)$$
      `
    },
    {
      id: 'm9_ex4',
      title: 'Identificación de Régimen RLC',
      level: 'intermediate',
      source: 'Ejercicios de Certamen FIS120',
      type: 'multiple_choice',
      statement: `
        Un circuito RLC serie cuenta con $L = 1.0\\text{ H}$, $C = 1.0\\,\\mu\\text{F}$ y $R = 3000\\,\\Omega$. ¿Bajo qué régimen opera el circuito?
      `,
      options: [
        'Sobreamortiguado ($\\alpha > \\omega_0$)',
        'Subamortiguado ($\\alpha < \\omega_0$)',
        'Críticamente amortiguado ($\\alpha = \\omega_0$)',
        'Oscilador libre no amortiguado'
      ],
      correctOption: 0,
      explanation: `
        Calculamos ambos parámetros:
        $$\\omega_0 = \\frac{1}{\\sqrt{LC}} = \\frac{1}{\\sqrt{1.0 \\cdot 10^{-6}}} = 1000\\text{ rad/s}$$
        $$\\alpha = \\frac{R}{2L} = \\frac{3000}{2 \\cdot 1.0} = 1500\\text{ s}^{-1}$$
        Como $\\alpha = 1500 > \\omega_0 = 1000$, el circuito es <strong>sobreamortiguado</strong>.
      `
    },
    {
      id: 'm9_ex5',
      title: 'Oscilador LC: Corriente y Reparto de Energía al 50%',
      level: 'certamen',
      source: 'Problemas Tipo Control FIS120',
      type: 'step_by_step',
      statement: `
        Un circuito LC ideal tiene capacitancia $C$ e inductancia $L$. En $t = 0$, el capacitor tiene una carga inicial $Q_0$ y la corriente es nula ($i(0) = 0$).<br>
        a) Encuentre la carga $q(t)$ y la corriente $i(t)$.<br>
        b) Determine el primer instante $t_1 > 0$ en el cual la energía eléctrica en el capacitor es exactamente igual a la energía magnética en el inductor ($U_C = U_L$).
      `,
      steps: [
        {
          title: 'Paso 1: Solución de carga y corriente',
          content: `
            La ecuación diferencial del circuito sin resistencia es $-L\\frac{d^2q}{dt^2} - \\frac{q}{C} = 0$.<br>
            Del formulario:
            $$q(t) = Q_0 \\cos(\\omega_0 t)$$
            donde $\\omega_0 = \\frac{1}{\\sqrt{LC}}$.<br>
            La corriente instantánea que sale del capacitor es:
            $$i(t) = -\\frac{dq}{dt} = -Q_0 (-\\omega_0 \\sin(\\omega_0 t)) = \\omega_0 Q_0 \\sin(\\omega_0 t)$$
          `
        },
        {
          title: 'Paso 2: Condición de equipartición de energía',
          content: `
            La energía total inicial es $U_{total} = \\frac{Q_0^2}{2C}$.<br>
            Si en el instante $t_1$ se cumple $U_C = U_L$, como $U_C + U_L = U_{total}$, entonces:
            $$U_C(t_1) = \\frac{1}{2} U_{total} \\implies \\frac{q(t_1)^2}{2C} = \\frac{1}{2} \\left( \\frac{Q_0^2}{2C} \\right)$$
            Simplificando:
            $$q(t_1)^2 = \\frac{Q_0^2}{2} \\implies q(t_1) = \\frac{Q_0}{\\sqrt{2}}$$
          `
        },
        {
          title: 'Paso 3: Cálculo del tiempo t₁',
          content: `
            Igualando a la función temporal:
            $$Q_0 \\cos(\\omega_0 t_1) = \\frac{Q_0}{\\sqrt{2}} \\implies \\cos(\\omega_0 t_1) = \\frac{1}{\\sqrt{2}} = \\frac{\\sqrt{2}}{2}$$
            El ángulo mínimo positivo es:
            $$\\omega_0 t_1 = \\frac{\\pi}{4} \\implies t_1 = \\frac{\\pi}{4\\omega_0} = \\frac{\\pi \\sqrt{LC}}{4}$$
            Dado que el periodo de oscilación completa es $T = \\frac{2\\pi}{\\omega_0}$, este instante corresponde exactamente a un octavo de periodo ($t_1 = T/8$).
          `
        }
      ]
    },
    {
      id: 'm9_ex6',
      title: 'Cálculo Completo de Circuito RLC Subamortiguado',
      level: 'certamen',
      source: 'Pautas de Certamen UTFSM',
      type: 'step_by_step',
      statement: `
        Considere un circuito RLC serie con $L = 0.50\\text{ H}$, $C = 2.0\\,\\mu\\text{F} = 2.0 \\times 10^{-6}\\text{ F}$ y $R = 200\\,\\Omega$. En $t = 0$, el capacitor tiene carga $Q_0 = 40.0\\,\\mu\\text{C}$ y no circula corriente.<br>
        a) Demuestre que el circuito es subamortiguado.<br>
        b) Calcule $\\omega_0, \\alpha$ y la frecuencia angular de oscilación $\\omega'$.<br>
        c) Escriba la ecuación completa de $q(t)$ del formulario oficial evaluando la amplitud y el ángulo de fase.
      `,
      steps: [
        {
          title: 'Paso 1: Cálculo de omega0, alpha y verificación de régimen',
          content: `
            $$\\omega_0 = \\frac{1}{\\sqrt{LC}} = \\frac{1}{\\sqrt{0.50 \\cdot 2.0 \\times 10^{-6}}} = \\frac{1}{\\sqrt{10^{-6}}} = 1000\\text{ rad/s}$$
            $$\\alpha = \\frac{R}{2L} = \\frac{200}{2 \\cdot 0.50} = 200\\text{ s}^{-1}$$
            Como $\\alpha = 200 < \\omega_0 = 1000$, el circuito es estrictamente <strong>subamortiguado</strong>.
          `
        },
        {
          title: 'Paso 2: Cálculo de la frecuencia amortiguada omega\'',
          content: `
            Del formulario oficial:
            $$\\omega' = \\sqrt{\\omega_0^2 - \\alpha^2} = \\sqrt{1000^2 - 200^2} = \\sqrt{1000000 - 40000} = \\sqrt{960000} \\approx 979.8\\text{ rad/s}$$
          `
        },
        {
          title: 'Paso 3: Amplitud efectiva y desfase del formulario',
          content: `
            La fórmula del formulario oficial establece:
            $$q(t) = Q_0 \\frac{\\omega_0}{\\omega'} e^{-\\alpha t} \\cos\\left(\\omega' t - \\arctan\\left(\\frac{\\alpha}{\\omega'}\\right)\\right)$$
            Calculamos el factor de amplitud:
            $$\\frac{\\omega_0}{\\omega'} = \\frac{1000}{979.8} \\approx 1.0206$$
            $$Q_{efectivo} = Q_0 \\cdot 1.0206 = (40.0\\,\\mu\\text{C}) \\cdot 1.0206 = 40.82\\,\\mu\\text{C}$$
            Calculamos el ángulo de fase:
            $$\\phi = \\arctan\\left(\\frac{\\alpha}{\\omega'}\\right) = \\arctan\\left(\\frac{200}{979.8}\\right) = \\arctan(0.2041) \\approx 0.2013\\text{ rad} \\approx 11.54^\\circ$$
            Por lo tanto:
            $$q(t) = 40.82\\, e^{-200 t} \\cos(979.8 t - 0.201)\\ [\\mu\\text{C}]$$
          `
        }
      ]
    },
    {
      id: 'm9_ex7',
      title: 'Importancia del Amortiguamiento Crítico en Ingeniería',
      level: 'certamen',
      source: 'Aplicaciones Conceptuales de Física',
      type: 'conceptual',
      statement: `
        ¿Por qué en el diseño de instrumentos de medición analógicos (como galvanómetros o agujas de velocímetro) y en sistemas de amortiguación de vehículos se busca calibrar el sistema en el régimen <em>críticamente amortiguado</em> en lugar del subamortiguado o sobreamortiguado?
      `,
      modelAnswer: `
        En el régimen <strong>críticamente amortiguado</strong> ($\\alpha = \\omega_0$), el sistema regresa a su posición de equilibrio en el <strong>tiempo mínimo posible sin presentar oscilaciones</strong> ($q(t) = (c_1 + c_2 t)e^{-\\alpha t}$).
        <br><br>
        1. <strong>Frente al régimen subamortiguado ($\\alpha < \\omega_0$):</strong> Si un velocímetro o galvanómetro fuera subamortiguado, ante un cambio de lectura la aguja oscilaría varias veces adelante y atrás alrededor del valor real antes de estabilizarse, haciendo imposible una lectura rápida y precisa. En un automóvil, el coche rebotaría continuamente tras pasar un bache.
        <br><br>
        2. <strong>Frente al régimen sobreamortiguado ($\\alpha > \\omega_0$):</strong> Si el sistema fuera sobreamortiguado, la resistencia excesiva frenaría el movimiento, haciendo que la aguja tarde un tiempo indeseablemente largo en alcanzar la nueva medición (movimiento lento y perezoso).
        <br><br>
        El amortiguamiento crítico proporciona la respuesta óptima: máxima velocidad de respuesta sin sobrepaso ni oscilaciones.
      `,
      rubric: `
        • 5 pts: Describir el defecto del subamortiguado (oscilaciones molestas/rebotar).<br>
        • 5 pts: Describir el defecto del sobreamortiguado (lentitud excesiva) y por qué el crítico es el óptimo en tiempo mínimo sin cruce por cero.
      `
    }
  ]
};
