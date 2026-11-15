/**
 * MÓDULO 8: CIRCUITOS TRANSIENTES RC Y RL
 * FIS120 / FIS12125 · UTFSM
 */

const MODULE_DATA_MOD8 = {
  number: '8',
  title: 'Circuitos Transientes RC y RL',
  description: 'Constantes de tiempo tau_C y tau_L, ecuaciones diferenciales del formulario, comportamiento en t = 0+ y t -> infinito, y circuitos con interruptores de múltiples posiciones.',
  hasInteractive: true,
  theory: `
    <p>
      Los circuitos con resistencias, capacitores e inductores gobernados por fuentes continuas no alcanzan su estado final instantáneamente. Los capacitores almacenan energía en su campo eléctrico y los inductores en su campo magnético, generando transitorios exponenciales de primer orden.
    </p>

    <div class="box-formula">
      <strong>1. Ecuaciones Diferenciales y Soluciones Exactas (Formulario C3):</strong>
      <table style="width: 100%; border-collapse: collapse; margin-top: 0.6rem; font-size: 0.95rem;">
        <tr style="border-bottom: 1px solid var(--border-color);">
          <th style="padding: 0.4rem; text-align: left;">Proceso</th>
          <th style="padding: 0.4rem; text-align: left;">Ecuación Diferencial</th>
          <th style="padding: 0.4rem; text-align: left;">Solución Analítica</th>
        </tr>
        <tr style="border-bottom: 1px solid var(--border-color);">
          <td style="padding: 0.4rem;"><strong>Carga RC</strong></td>
          <td style="padding: 0.4rem;">$\\mathcal{E} - R\\frac{dq}{dt} - \\frac{q}{C} = 0$</td>
          <td style="padding: 0.4rem;">$q(t) = Q_{\\max}(1 - e^{-t/RC})$</td>
        </tr>
        <tr style="border-bottom: 1px solid var(--border-color);">
          <td style="padding: 0.4rem;"><strong>Descarga RC</strong></td>
          <td style="padding: 0.4rem;">$-R\\frac{dq}{dt} - \\frac{q}{C} = 0$</td>
          <td style="padding: 0.4rem;">$q(t) = Q_0 e^{-t/RC}$</td>
        </tr>
        <tr style="border-bottom: 1px solid var(--border-color);">
          <td style="padding: 0.4rem;"><strong>Crecimiento RL</strong></td>
          <td style="padding: 0.4rem;">$\\mathcal{E} - iR - L\\frac{di}{dt} = 0$</td>
          <td style="padding: 0.4rem;">$i(t) = I_{\\max}(1 - e^{-(R/L)t})$</td>
        </tr>
        <tr>
          <td style="padding: 0.4rem;"><strong>Decaimiento RL</strong></td>
          <td style="padding: 0.4rem;">$-iR - L\\frac{di}{dt} = 0$</td>
          <td style="padding: 0.4rem;">$i(t) = I_0 e^{-(R/L)t}$</td>
        </tr>
      </table>
      <p style="margin-top: 0.8rem;">
        • <strong>Constantes de tiempo:</strong> $\\tau_C = RC$ (segundos), $\\tau_L = \\frac{L}{R}$ (segundos).
        <br>• En $t = 1\\tau$: la variable alcanza el $63.2\\%$ de su valor final en carga/crecimiento, o decae al $36.8\\%$ en descarga.
        <br>• En $t = 5\\tau$: el transitorio se considera prácticamente concluido ($> 99.3\\%$, estado estacionario).
      </p>
    </div>

    <div class="figure-container">
      <img src="img/mod8_switch_circuit.svg" alt="Circuito de interruptor de dos posiciones">
      <div class="figure-caption">Circuito con interruptor de 2 posiciones (Pauta Oficial Certamen 3 2026-1 Problema 3).</div>
    </div>

    <div class="box-method">
      <strong>2. Tabla Maestra de Comportamiento Asintótico (Regla Infalible de Certamen):</strong>
      <table style="width: 100%; border-collapse: collapse; margin-top: 0.6rem; font-size: 0.95rem;">
        <tr style="border-bottom: 1px solid var(--border-color); background: var(--bg-tertiary);">
          <th style="padding: 0.5rem; text-align: left;">Elemento</th>
          <th style="padding: 0.5rem; text-align: left;">Instante Inicial $t = 0^+$</th>
          <th style="padding: 0.5rem; text-align: left;">Estado Estacionario $t \\to \\infty$</th>
        </tr>
        <tr style="border-bottom: 1px solid var(--border-color);">
          <td style="padding: 0.5rem;"><strong>Capacitor ($C$)</strong></td>
          <td style="padding: 0.5rem;">Actúa como <strong>CORTOCIRCUITO</strong> ($V_C = 0$) si estaba descargado.</td>
          <td style="padding: 0.5rem;">Actúa como <strong>CIRCUITO ABIERTO</strong> ($i_C = 0$).</td>
        </tr>
        <tr>
          <td style="padding: 0.5rem;"><strong>Inductor ($L$)</strong></td>
          <td style="padding: 0.5rem;">Actúa como <strong>CIRCUITO ABIERTO</strong> ($i_L = 0$) si partió sin corriente.</td>
          <td style="padding: 0.5rem;">Actúa como <strong>CORTOCIRCUITO</strong> / Conductor ideal ($V_L = 0$).</td>
        </tr>
      </table>
    </div>

    <div class="box-warning">
      <strong>Errores Fatales en el Certamen:</strong><br>
      1. Confundir la resistencia equivalente que "ve" el capacitor o inductor para calcular $\\tau$: la resistencia en $\\tau = RC$ o $\\tau = L/R$ es la <strong>resistencia equivalente de Thévenin</strong> conectada directamente a los terminales del elemento reactivo.<br>
      2. No conservar la corriente en el inductor o la carga en el capacitor durante la conmutación: $i_L(0^+) = i_L(0^-)$ y $q_C(0^+) = q_C(0^-)$.
    </div>
  `,
  exercises: [
    {
      id: 'm8_ex1',
      title: 'Comportamiento Asintótico de Elementos Reactivos',
      level: 'basic',
      source: 'Pauta C3 Problema 3b',
      type: 'multiple_choice',
      statement: `
        Tras mantener conectado un circuito con corriente continua durante un tiempo muy largo ($t \\to \\infty$), ¿cómo se modelan respectivamente un capacitor ideal y un inductor ideal?
      `,
      options: [
        'Capacitor: Circuito abierto ($i_C = 0$); Inductor: Conductor ideal / Cortocircuito ($v_L = 0$)',
        'Capacitor: Cortocircuito ($v_C = 0$); Inductor: Circuito abierto ($i_L = 0$)',
        'Ambos se comportan como circuitos abiertos',
        'Ambos se comportan como resistencias puras de valor $R$'
      ],
      correctOption: 0,
      explanation: `
        En $t \\to \\infty$, el capacitor se ha cargado por completo, cesando el flujo de carga ($i_C = dq/dt = 0$, circuito abierto). El inductor ha alcanzado una corriente continua constante, por lo que su derivada es nula ($v_L = L di/dt = 0$), comportándose como un simple alambre conductor ideal sin caída de potencial.
      `
    },
    {
      id: 'm8_ex2',
      title: 'Cálculo de Constante de Tiempo RC',
      level: 'basic',
      source: 'Pauta C3 Problema 3c',
      type: 'numerical',
      statement: `
        En la rama RC del Problema 3 de la Pauta Oficial C3, se tienen los valores $R = 370\\,\\Omega$ y $C = 5.0\\,\\mu\\text{F} = 5.0 \\times 10^{-6}\\text{ F}$. Calcule la constante de tiempo $\\tau_C$ en milisegundos (ms).
      `,
      placeholder: 'Ej: 1.85',
      units: 'ms',
      correctValue: 1.85,
      tolerance: 0.02,
      explanation: `
        $$\\tau_C = RC = (370\\,\\Omega) \\cdot (5.0 \\times 10^{-6}\\text{ F}) = 1.85 \\times 10^{-3}\\text{ s} = 1.85\\text{ ms}$$
      `
    },
    {
      id: 'm8_ex3',
      title: 'Voltaje en Capacitor en un Tiempo t = tau',
      level: 'intermediate',
      source: 'Propiedades Exponenciales Formulario',
      type: 'true_false',
      statement: `
        Durante el proceso de carga de un capacitor a través de una resistencia desde una fuente de voltaje $\\mathcal{E}$, en el instante $t = \\tau_C = RC$ el voltaje en el capacitor ha alcanzado aproximadamente el $63.2\\%$ del voltaje de la fuente.
      `,
      correct: true,
      justification: `
        Verdadero. La ecuación del formulario es $q(t) = Q_{\\max}(1 - e^{-t/RC})$, por lo que dividiendo por $C$:
        $$V_C(t) = \\mathcal{E}(1 - e^{-t/\\tau})$$
        En $t = \\tau$:
        $$V_C(\\tau) = \\mathcal{E}(1 - e^{-1}) = \\mathcal{E}\\left(1 - \\frac{1}{2.71828}\\right) = \\mathcal{E}(1 - 0.3679) \\approx 0.6321\\,\\mathcal{E} \\ (63.2\\%)$$
      `
    },
    {
      id: 'm8_ex4',
      title: 'Condición de Igualdad de Constantes tau_L = tau_C',
      level: 'certamen',
      source: 'Pauta Certamen 3 2026-1 Problema 3a',
      type: 'step_by_step',
      figure: 'img/mod8_switch_circuit.svg',
      figureCaption: 'Circuito con interruptor en posición 1: capacitor se carga e inductor se energiza.',
      statement: `
        El circuito de la figura cuenta con un capacitor inicialmente descargado y el interruptor toca el terminal 1 (Figura a). Encuentre analítica y numéricamente la inductancia $L$ tal que las constantes de tiempo, $\\tau_L$ y $\\tau_C$, sean iguales. Use: $C = 5\\,\\mu\\text{F}$ y $R = 370\\,\\Omega$.
      `,
      steps: [
        {
          title: 'Paso 1: Planteamiento de las constantes de tiempo',
          content: `
            Del formulario oficial:
            $$\\tau_C = RC \\quad \\text{y} \\quad \\tau_L = \\frac{L}{R}$$
          `
        },
        {
          title: 'Paso 2: Igualación y despeje analítico de L',
          content: `
            Para que ambas constantes sean iguales:
            $$\\tau_L = \\tau_C \\implies \\frac{L}{R} = RC \\implies L = R^2 C$$
          `
        },
        {
          title: 'Paso 3: Evaluación numérica con los datos de la pauta',
          content: `
            Sustituyendo los valores numéricos:
            $$L = (370)^2 \\cdot (5 \\times 10^{-6})\\text{ [H]} = 136900 \\cdot 5 \\times 10^{-6}\\text{ [H]} = 0.6845\\text{ [H]}$$
            $$L \\simeq 0.684\\text{ [H]}$$
            <strong>Chequeo dimensional:</strong> $[\Omega^2 \\cdot F] = [\Omega \\cdot (\Omega \\cdot F)] = [\Omega \\cdot s] = \\text{Henrio [H]}$.
          `
        }
      ]
    },
    {
      id: 'm8_ex5',
      title: 'Corriente Saliendo de la Fuente en Régimen Permanente (t -> inf)',
      level: 'certamen',
      source: 'Pauta Certamen 3 2026-1 Problema 3b',
      type: 'step_by_step',
      statement: `
        Se mantiene la configuración de contacto con el terminal 1 por un tiempo muy largo ($t \\to \\infty$). Encuentre la corriente total que sale de la fuente. Use $\\mathcal{E} = 112\\text{ [V]}$ y $R = 370\\,\\Omega$.
      `,
      steps: [
        {
          title: 'Paso 1: Análisis asintótico de cada rama',
          content: `
            Si el interruptor se mantiene tocando el terminal 1 por un tiempo muy largo ($t \\to \\infty$):
            <br>• El capacitor queda plenamente cargado y se comporta como <strong>circuito abierto</strong>:
            $$I_C(\\infty) = 0$$
            • En el mismo límite, la corriente en el inductor es constante, por lo que su voltaje se anula ($v_L = L di/dt = 0$), comportándose como un <strong>conductor ideal</strong>:
            $$V_L(\\infty) = 0$$
          `
        },
        {
          title: 'Paso 2: Corriente en la rama RL y corriente de la fuente',
          content: `
            Por lo tanto, la rama RL queda determinada únicamente por la resistencia $R$ en serie con la fuente:
            $$I_L(\\infty) = \\frac{\\mathcal{E}}{R}$$
            Como la rama RC no conduce corriente en estado estacionario, la corriente total que sale de la fuente es:
            $$I_{fuente} = I_C(\\infty) + I_L(\\infty) = 0 + \\frac{\\mathcal{E}}{R} = \\frac{\\mathcal{E}}{R}$$
          `
        },
        {
          title: 'Paso 3: Evaluación numérica',
          content: `
            $$I_{fuente} = \\frac{112}{370}\\text{ [A]} \\approx 0.3027\\text{ [A]} \\simeq 0.303\\text{ [A]}$$
          `
        }
      ]
    },
    {
      id: 'm8_ex6',
      title: 'Conmutación a Posición 2: Corrientes Ic(t) e IL(t)',
      level: 'certamen',
      source: 'Pauta Certamen 3 2026-1 Problema 3c',
      type: 'step_by_step',
      figure: 'img/mod8_switch_circuit.svg',
      figureCaption: 'Interruptor en posición 2: rama RC se desconecta de la fuente; rama RL sigue alimentada.',
      statement: `
        Luego de este tiempo muy largo con el interruptor en el terminal 1, se cambia el interruptor al terminal 2 (Figura b). Encuentre $I_C(t)$, la corriente en función del tiempo para la rama RC, e $I_L(t)$, la corriente para la rama RL.
      `,
      steps: [
        {
          title: 'Paso 1: Condiciones iniciales justo antes del cambio',
          content: `
            En el instante del cambio ($t = 0$):
            <br>• El capacitor quedó cargado a la tensión de la fuente: $V_C(0) = \\mathcal{E} = 112\\text{ V}$, con carga $q(0) = C\\mathcal{E}$.
            <br>• La corriente en el inductor era $I_L(0) = \\frac{\\mathcal{E}}{R} = 0.303\\text{ A}$.
          `
        },
        {
          title: 'Paso 2: Evolución de la corriente en la rama RC',
          content: `
            Al pasar al terminal 2, la rama RC queda desconectada de la fuente y forma una malla cerrada donde el capacitor se descarga a través de la resistencia $R$.<br>
            De la ecuación de descarga del formulario:
            $$q(t) = q(0) e^{-t/RC} = C\\mathcal{E} e^{-t/RC}$$
            La corriente de descarga que fluye fuera del capacitor es:
            $$I_C(t) = -\\frac{dq}{dt} = \\frac{\\mathcal{E}}{R} e^{-t/RC}$$
            Con $RC = 1.85 \\times 10^{-3}\\text{ [s]}$ y $\\frac{\\mathcal{E}}{R} = 0.303\\text{ [A]}$:
            $$I_C(t) = 0.303\\, e^{-t / (1.85 \\times 10^{-3})}\\text{ [A]}$$
          `
        },
        {
          title: 'Paso 3: Evolución de la corriente en la rama RL',
          content: `
            Observe el diagrama del circuito (Figura b): la rama RL <strong>permanece conectada directamente a la fuente $\\mathcal{E}$</strong>.<br>
            Como antes del cambio el inductor ya había alcanzado su estado estacionario continuo con corriente $I_L = \\frac{\\mathcal{E}}{R}$, su estado no sufre perturbación alguna.<br>
            Por lo tanto, la corriente en la rama RL permanece constante en el tiempo:
            $$I_L(t) = \\frac{\\mathcal{E}}{R} = 0.303\\text{ [A]}$$
          `
        }
      ]
    },
    {
      id: 'm8_ex7',
      title: 'Continuidad de Corriente vs. Voltaje en Conmutaciones',
      level: 'certamen',
      source: 'Concepto Clave Pauta C3',
      type: 'conceptual',
      statement: `
        En el circuito del problema anterior, ¿cuál es el voltaje en la resistencia $R$ de la rama RC inmediatamente antes ($t=0^-$) e inmediatamente después ($t=0^+$) de cambiar el interruptor a la posición 2? Explique por qué el voltaje sí puede cambiar instantáneamente.
      `,
      modelAnswer: `
        1. <strong>En $t = 0^-$ (justo antes del cambio):</strong><br>
        El capacitor estaba plenamente cargado y en estado estacionario, por lo que la corriente en la rama RC era cero ($i_C(0^-) = 0$). Por Ley de Ohm, el voltaje en la resistencia era nulo:
        $$V_R(0^-) = i_C(0^-) \\cdot R = 0\\text{ V}$$
        <br>
        2. <strong>En $t = 0^+$ (inmediatamente después del cambio):</strong><br>
        Por conservación de la carga en el capacitor, su diferencia de potencial no puede cambiar instantáneamente: $V_C(0^+) = V_C(0^-) = \\mathcal{E} = 112\\text{ V}$. Al cerrarse sobre la resistencia $R$, por Ley de Mallas de Kirchhoff:
        $$V_R(0^+) = V_C(0^+) = \\mathcal{E} = 112\\text{ V}$$
        <br>
        3. <strong>Justificación física:</strong><br>
        El voltaje en una resistencia pura no tiene inercia energética (la resistencia no almacena energía, solo la disipa). Por tanto, su corriente y voltaje pueden saltar instantáneamente de $0\\text{ V}$ a $112\\text{ V}$ para obedecer instantáneamente la Ley de Kirchhoff con el voltaje mantenido por el capacitor.
      `,
      rubric: `
        • 5 pts: Cálculo correcto de V_R(0^-) = 0 y V_R(0^+) = E = 112 V.<br>
        • 5 pts: Explicación de la falta de inercia energética en resistencias puras vs. la continuidad de carga en capacitores.
      `
    }
  ]
};
