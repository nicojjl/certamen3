/**
 * MÓDULO 5: FEM DE MOVIMIENTO Y DINÁMICA DE CIRCUITOS
 * FIS120 / FIS12125 · UTFSM
 */

window.MODULE_DATA_MOD5 = {
  number: '5',
  title: 'fem de Movimiento y Rieles con Gravedad',
  description: 'Conductores móviles en campos magnéticos, fuerza de frenado de Lorentz, leyes de Newton aplicadas a circuitos, velocidad terminal y balance riguroso de potencia electromecánica.',
  hasInteractive: false,
  theory: `
    <p>
      Cuando un conductor se desplaza a través de un campo magnético, las cargas libres en su interior experimentan la fuerza magnética de Lorentz $\\vec{F} = q(\\vec{v}\\times\\vec{B})$. Esta fuerza separa las cargas creando una diferencia de potencial conocida como <strong>fem de movimiento</strong> (o motriz).
    </p>

    <div class="box-formula">
      <strong>1. Expresiones Fundamentales (Formulario C3):</strong>
      <p>
        • <strong>fem de Movimiento:</strong>
        $$\\varepsilon = \\oint (\\vec{v}\\times\\vec{B})\\cdot d\\vec{l} = B L v \\quad (\\text{cuando } \\vec{v} \\perp \\vec{B} \\perp \\vec{L})$$
        • <strong>Corriente Inducida (Ley de Ohm):</strong>
        $$i(t) = \\frac{\\varepsilon(t)}{R} = \\frac{B L v(t)}{R}$$
        • <strong>Fuerza Magnética sobre el Conductor:</strong>
        $$\\vec{F}_m = i(t) (\\vec{L}\\times\\vec{B}) = \\frac{B^2 L^2 v(t)}{R} \\quad (\\text{siempre opuesta a } \\vec{v})$$
      </p>
    </div>

    <div class="figure-container">
      <img src="img/mod5_motional_emf_rails.svg" alt="Varilla en rieles con gravedad">
      <div class="figure-caption">Varilla en rieles verticales bajo la gravedad $\\vec{g}$ y campo uniforme $\\vec{B} = -B_0\\hat{\\jmath}$ (Ayudantía 10 P3).</div>
    </div>

    <div class="box-method">
      <strong>2. Dinámica de Newton y Velocidad Terminal:</strong>
      <p>
        Para una varilla de masa $m$ que cae verticalmente sobre dos rieles conductores paralelos separados por distancia $L$ en presencia de un campo horizontal $\\vec{B}$:
        $$\\sum F_z = m a = m \\frac{dv}{dt} = mg - F_m = mg - \\frac{B^2 L^2}{R} v$$
        • Conforme la velocidad $v(t)$ aumenta, la fuerza magnética retardadora $F_m$ crece linealmente.
        <br>• Cuando $F_m$ iguala exactamente al peso gravitacional ($a = 0$), la aceleración se anula y la varilla alcanza su <strong>velocidad terminal constante</strong>:
        $$mg - \\frac{B^2 L^2}{R} v_t = 0 \\implies v_t = \\frac{mgR}{B^2 L^2}$$
        <br>
        <strong>Conservación y Balance de Potencia en Régimen Terminal:</strong>
        La potencia suministrada por la gravedad es exactamente igual a la potencia eléctrica disipada por efecto Joule en la resistencia:
        $$P_{mec} = F_{grav} \\cdot v_t = (mg) v_t = \\left(\\frac{B^2 L^2 v_t}{R}\\right) v_t = \\frac{B^2 L^2 v_t^2}{R} = i_t^2 R = P_{Joule}$$
      </p>
    </div>

    <div class="box-warning">
      <strong>Errores Frecuentes en el Certamen:</strong><br>
      1. Asumir que la corriente o la velocidad son constantes desde el inicio: la varilla parte del reposo ($v=0, i=0$) y acelera transitoriamente según $v(t) = v_t(1 - e^{-t/\\tau_m})$ donde $\\tau_m = \\frac{mR}{B^2 L^2}$.<br>
      2. Equivocar la dirección de la fuerza magnética $\\vec{F}_m = i(\\vec{L}\\times\\vec{B})$: por la Ley de Lenz y la conservación de la energía, la fuerza magnética SIEMPRE se opone al movimiento relativo (actúa como fricción electromagnética).
    </div>
  `,
  exercises: [
    {
      id: 'm5_ex1',
      title: 'fem Motriz en Conductor Móvil',
      level: 'basic',
      source: 'Ejercicio original (no oficial)',
      type: 'multiple_choice',
      statement: `
        Una varilla de $L = 0.50\\text{ m}$ de longitud se desplaza con velocidad constante $v = 4.0\\text{ m/s}$ perpendicular a un campo magnético uniforme de $B = 0.60\\text{ T}$. ¿Cuál es la fem inducida entre sus extremos?
      `,
      options: [
        '$1.20\\text{ V}$',
        '$0.60\\text{ V}$',
        '$2.40\\text{ V}$',
        '$0.30\\text{ V}$'
      ],
      correctOption: 0,
      explanation: `
        Al ser los vectores mutuamente ortogonales:
        $$\\varepsilon = B L v = 0.60\\text{ T} \\cdot 0.50\\text{ m} \\cdot 4.0\\text{ m/s} = 1.20\\text{ V}$$
      `
    },
    {
      id: 'm5_ex2',
      title: 'Fuerza Magnética sobre Conductor',
      level: 'basic',
      source: 'Ejercicio original (no oficial)',
      type: 'numerical',
      statement: `
        Por una varilla de longitud $L = 0.40\\text{ m}$ circula una corriente $I = 2.5\\text{ A}$. La varilla se encuentra en un campo magnético uniforme de $B = 0.80\\text{ T}$ perpendicular a ella. Calcule la magnitud de la fuerza magnética en Newtons.
      `,
      placeholder: 'Ej: 0.80',
      units: 'N',
      correctValue: 0.80,
      tolerance: 0.03,
      explanation: `
        $$F_m = I L B = 2.5\\text{ A} \\cdot 0.40\\text{ m} \\cdot 0.80\\text{ T} = 0.80\\text{ N}$$
      `
    },
    {
      id: 'm5_ex3',
      title: 'Efecto de la Resistencia en la Velocidad Terminal',
      level: 'intermediate',
      source: 'Ejercicio original (no oficial)',
      type: 'true_false',
      statement: `
        En el sistema de rieles verticales con gravedad, si se reemplaza la varilla por otra del mismo peso y dimensiones pero con el doble de resistencia eléctrica ($2R$), la velocidad terminal alcanzada será el doble de la original.
      `,
      correct: true,
      justification: `
        Verdadero. La velocidad terminal viene dada por $v_t = \\frac{mgR}{B^2 L^2}$. Dado que $v_t$ es directamente proporcional a la resistencia $R$, si la resistencia se duplica, se requiere el doble de velocidad para que la fem $\\varepsilon = BLv_t$ induzca la misma corriente $i = mg / (BL)$ necesaria para equilibrar el peso.
      `
    },
    {
      id: 'm5_ex4',
      title: 'Cálculo Numérico de Velocidad Terminal',
      level: 'intermediate',
      source: 'Ejercicio original (no oficial)',
      type: 'numerical',
      statement: `
        Una varilla de masa $m = 0.050\\text{ kg}$ y resistencia $R = 2.0\\,\\Omega$ cae por rieles verticales separados $L = 0.25\\text{ m}$ bajo un campo $B = 0.50\\text{ T}$. Usando $g = 9.8\\text{ m/s}^2$, calcule la velocidad terminal $v_t$ en m/s.
      `,
      placeholder: 'Ej: 62.7',
      units: 'm/s',
      correctValue: 62.72,
      tolerance: 0.03,
      explanation: `
        $$v_t = \\frac{mgR}{B^2 L^2} = \\frac{0.050 \\cdot 9.8 \\cdot 2.0}{(0.50)^2 \\cdot (0.25)^2} = \\frac{0.98}{0.25 \\cdot 0.0625} = \\frac{0.98}{0.015625} = 62.72\\text{ m/s}$$
      `
    },
    {
      id: 'm5_ex5',
      title: 'Varilla en Rieles con Gravedad y Campo B₀(-ĵ)',
      level: 'certamen',
      source: 'Ayudantía 10 Problema 3',
      type: 'step_by_step',
      figure: 'img/mod5_motional_emf_rails.svg',
      figureCaption: 'Varilla de masa $m$ y resistencia $R$ deslizándose bajo la gravedad sobre rieles paralelos.',
      statement: `
        Considere una varilla conductora de masa $m$ con resistencia $R$ que se desliza sin fricción por dos raíles paralelos separados por distancia $L$ por acción de la gravedad $\\vec{g} = -g\\hat{k}$. Se presenta un campo magnético uniforme $\\vec{B} = B_0(-\\hat{\\jmath})$. Entre la varilla y los raíles se forma un circuito cerrado.<br>
        a) Calcule el flujo magnético a través de la espira en función de la posición $z(t)$, indicando el vector normal escogido.<br>
        b) Determine la fem inducida en la espira y su signo respecto a la normal.<br>
        c) Determine la corriente inducida y su sentido fundamentado rigurosamente con Lenz.<br>
        d) Determine la fuerza magnética inducida sobre la barra.<br>
        e) A través de la segunda ley de Newton cuando $\\vec{a} = \\vec{0}$, determine la velocidad terminal de la barra.
      `,
      steps: [
        {
          title: 'Paso 1: Elección de normal y flujo magnético a través del circuito',
          content: `
            Orientamos el plano del circuito en el plano $xz$. El área delimitada por los rieles y la varilla en la posición $z(t)$ es un rectángulo de lados $L$ (en $x$) y $z(t)$ (longitud caída en $z$):
            $$A(t) = L \\cdot z(t)$$
            <strong>Elección del vector normal $\\hat{n}$ y convención de circulación:</strong><br>
            Escogemos el vector normal al plano en dirección entrante a la página: $\\hat{n} = -\\hat{\\jmath}$, paralelo al campo magnético $\\vec{B} = -B_0\\hat{\\jmath}$.<br>
            Por la regla de la mano derecha, un vector normal entrante ($-\\hat{\\jmath}$) define como sentido positivo de circulación el <strong>sentido horario</strong>.<br>
            El flujo magnético es:
            $$\\phi_B(t) = \\iint \\vec{B} \\cdot d\\vec{A} = (-B_0\\hat{\\jmath}) \\cdot (L z(t)(-\\hat{\\jmath})) = B_0 L z(t) > 0$$
          `
        },
        {
          title: 'Paso 2: fem inducida y análisis de signo',
          content: `
            Al caer la varilla con velocidad $v(t) = \\frac{dz}{dt} > 0$, el área del circuito se expande y el flujo magnético entrante aumenta en el tiempo:
            $$\\frac{d\\phi_B}{dt} = B_0 L \\frac{dz}{dt} = B_0 L v(t) > 0$$
            Aplicando la Ley de Faraday-Lenz:
            $$\\varepsilon_{ind}(t) = -\\frac{d\\phi_B}{dt} = -B_0 L v(t) < 0$$
            <strong>Interpretación del signo de $\\varepsilon$:** Como $\\varepsilon_{ind}(t) < 0$, la fem actúa en sentido opuesto al sentido positivo asociado a la normal (opuesto al sentido horario), lo que indica formalmente que la circulación inducida es en <strong>sentido antihorario</strong>.
          `
        },
        {
          title: 'Paso 3: Corriente inducida y sentido físico por Ley de Lenz',
          content: `
            Por la Ley de Ohm:
            $$i(t) = \\frac{|\\varepsilon_{ind}|}{R} = \\frac{B_0 L v(t)}{R}$$
            <strong>Sentido físico según Lenz:</strong><br>
            A medida que la varilla cae, el flujo magnético entrante ($\\otimes$) aumenta continuamente. Según la Ley de Lenz, la espira debe oponerse a este incremento induciendo un campo magnético propio dirigido hacia afuera de la página ($\\odot$).<br>
            Por la regla de la mano derecha (pulgar apuntando hacia afuera $\\odot$), los dedos indican que la corriente inducida debe circular en <strong>sentido antihorario</strong>.<br>
            Esto significa que a través de la varilla móvil, la corriente circula de izquierda a derecha en dirección $+\\hat{\\imath}$, sube por el riel derecho, va hacia la izquierda por la conexión superior y baja por el riel izquierdo.
          `
        },
        {
          title: 'Paso 4: Fuerza magnética de frenado sobre la varilla',
          content: `
            La fuerza de Lorentz sobre el elemento conductor móvil de longitud $\\vec{L} = L\\hat{\\imath}$ con corriente $i(t)$ es:
            $$\\vec{F}_m = i (\\vec{L} \\times \\vec{B}) = \\left(\\frac{B_0 L v}{R}\\right) (L\\hat{\\imath} \\times (-B_0\\hat{\\jmath})) = -\\frac{B_0^2 L^2 v}{R}(\\hat{\\imath}\\times\\hat{\\jmath}) = -\\frac{B_0^2 L^2 v}{R}\\hat{k}$$
            Como el eje vertical de caída apunta hacia abajo y la gravedad acelera la barra en dirección de caída, la fuerza magnética apunta verticalmente hacia arriba, actuando como una <strong>fuerza neta de frenado</strong> que se opone a la caída gravitatoria.
          `
        },
        {
          title: 'Paso 5: Segunda Ley de Newton y velocidad terminal',
          content: `
            Escribimos la ecuación de movimiento en el eje vertical de caída:
            $$m \\frac{dv}{dt} = mg - F_m = mg - \\frac{B_0^2 L^2}{R} v$$
            En el régimen estacionario terminal, la aceleración se anula ($a = \\frac{dv}{dt} = 0$):
            $$mg - \\frac{B_0^2 L^2}{R} v_t = 0 \\implies v_t = \\frac{mgR}{B_0^2 L^2}$$
            <strong>Chequeo de unidades:</strong> $[mgR / (B^2 L^2)] = \\frac{\\text{N}\\cdot\\Omega}{\\text{T}^2\\cdot\\text{m}^2} = \\text{m/s}$. Correcto.
          `
        }
      ]
    },
    {
      id: 'm5_ex6',
      title: 'Carrito Conductor Ingresando a Campo Magnético',
      level: 'certamen',
      source: 'Ayudantía 10 Problema 4',
      type: 'step_by_step',
      statement: `
        Un carrito de masa $m$ formado por una espira conductora rectangular de ancho $a$ y resistencia $R$ se desplaza sin fricción con velocidad inicial $\\vec{v} = v_0\\hat{\\imath}$. Este ingresa a una región con campo magnético uniforme $\\vec{B} = B_0\\hat{k}$.<br>
        a) Luego de que el carrito ingresa a la zona con campo, indique el vector normal elegido, el signo de la fem y si se induce en sentido horario o antihorario.<br>
        b) Determine la corriente inducida.<br>
        c) Determine la fuerza inducida sobre la espira y demuestre que siempre actúa como fuerza de frenado.
      `,
      steps: [
        {
          title: 'Paso 1: Elección de normal, variación de flujo y signo de la fem',
          content: `
            Sea $x(t)$ la longitud del carrito que ha penetrado en la zona de campo magnético ($x \\in [0, a]$).<br>
            El área inmersa es $A(t) = a \\cdot x(t)$.<br>
            <strong>Vector normal elegido $\\hat{n}$ y convención:</strong><br>
            Escogemos $\\hat{n} = +\\hat{k}$ (apuntando hacia afuera de la página, en la dirección de $\\vec{B} = B_0\\hat{k}$). Por la regla de la mano derecha, un vector normal saliente define como sentido positivo de circulación el <strong>sentido antihorario</strong>.<br>
            El flujo magnético es:
            $$\\phi_B(t) = \\iint \\vec{B}\\cdot d\\vec{A} = (B_0\\hat{k})\\cdot(a x(t)\\hat{k}) = B_0 a x(t) > 0$$
            Al ingresar, $x(t)$ crece con $\\frac{dx}{dt} = v > 0$, de modo que el flujo saliente aumenta: $\\frac{d\\phi_B}{dt} = B_0 a v > 0$.<br>
            Por la Ley de Faraday-Lenz:
            $$\\varepsilon_{ind}(t) = -\\frac{d\\phi_B}{dt} = -B_0 a v(t) < 0$$
            <strong>Signo y sentido:</strong> Al resultar $\\varepsilon_{ind} < 0$, la corriente circula en sentido opuesto al positivo de la normal (opuesto al antihorario), es decir, en <strong>sentido horario</strong>.<br>
            <strong>Fundamento con Lenz:</strong> El flujo saliente ($\\\\odot$) está aumentando. Para contrarrestar este incremento, la espira induce un campo magnético propio hacia adentro ($\\\\otimes$), lo que exige corriente en <strong>sentido horario</strong>.
          `
        },
        {
          title: 'Paso 2: Corriente inducida en la espira',
          content: `
            Por la Ley de Ohm:
            $$i(t) = \\frac{|\\varepsilon_{ind}|}{R} = \\frac{B_0 a v(t)}{R} \\quad (\\text{en sentido horario})$$
          `
        },
        {
          title: 'Paso 3: Fuerza magnética de frenado (siempre se opone al movimiento)',
          content: `
            Analizamos la fuerza de Lorentz $\\vec{F} = i (\\vec{L} \\times \\vec{B})$ en cada lado de la espira:<br>
            • <strong>Lado frontal (líder):</strong> Está dentro del campo. Al circular en sentido horario, la corriente en este lado viaja hacia abajo ($-\\hat{\\jmath}$):
            $$\\vec{F}_{frontal} = i (-a\\hat{\\jmath}) \\times (B_0\\hat{k}) = -i a B_0 (\\hat{\\jmath}\\times\\hat{k}) = -i a B_0\\,\\hat{\\imath}$$
            • <strong>Lados superior e inferior:</strong> Transportan corrientes en sentidos opuestos ($+\\hat{\\imath}$ y $-\\hat{\\imath}$), por lo que sus fuerzas magnéticas verticales ($\\\\pm \\hat{\\jmath}$) se anulan exactamente por simetría.<br>
            • <strong>Lado posterior:</strong> Aún se encuentra fuera del campo magnético ($\\\\vec{B} = 0$), por lo que no experimenta fuerza.<br><br>
            Sustituyendo la corriente $i(t) = \\frac{B_0 a v(t)}{R}$, la fuerza neta total sobre la espira es:
            $$\\vec{F}_{neto} = -\\frac{B_0^2 a^2 v(t)}{R}\\,\\hat{\\imath}$$
            <strong>Demostración de frenado:</strong> Como $\\vec{v} = v\\hat{\\imath}$ con $v > 0$, la fuerza apunta en $-\\hat{\\imath}$ (opuesta al vector velocidad). Por lo tanto, <strong>la fuerza magnética actúa invariablemente como una fuerza de frenado</strong>, decelerando el carrito según $m \\frac{dv}{dt} = -\\frac{B_0^2 a^2}{R}v$.
          `
        }
      ]
    },
    {
      id: 'm5_ex7',
      title: 'Balance de Potencia en la Velocidad Terminal',
      level: 'certamen',
      source: 'Ejercicio original (no oficial)',
      type: 'conceptual',
      statement: `
        Demuestre analíticamente que cuando la varilla conductora en los rieles alcanza su velocidad terminal $v_t$, la tasa a la cual la gravedad realiza trabajo mecánico sobre la varilla es exactamente igual a la tasa a la cual se disipa energía térmica por efecto Joule en la resistencia $R$.
      `,
      modelAnswer: `
        <strong>1. Potencia mecánica suministrada por la gravedad:</strong><br>
        La fuerza gravitacional constante que tira de la varilla hacia abajo es $F_g = mg$. Cuando la varilla se desplaza a velocidad constante $v_t$, la potencia mecánica entregada al sistema es:
        $$P_{mec} = \\vec{F}_g \\cdot \\vec{v}_t = mg \\cdot v_t$$
        <br>
        <strong>2. Potencia disipada por efecto Joule en la resistencia:</strong><br>
        La corriente eléctrica inducida en régimen terminal es $i_t = \\frac{B L v_t}{R}$. La potencia eléctrica convertida en calor por efecto Joule es:
        $$P_{Joule} = i_t^2 R = \\left(\\frac{B L v_t}{R}\\right)^2 R = \\frac{B^2 L^2 v_t^2}{R}$$
        <br>
        <strong>3. Demostración de igualdad:</strong><br>
        En la velocidad terminal, la fuerza magnética equilibra al peso: $mg = \\frac{B^2 L^2 v_t}{R}$.<br>
        Sustituyendo esta igualdad en la expresión de potencia mecánica:
        $$P_{mec} = (mg) v_t = \\left(\\frac{B^2 L^2 v_t}{R}\\right) v_t = \\frac{B^2 L^2 v_t^2}{R} = P_{Joule}$$
        Por lo tanto:
        $$P_{mec} \\equiv P_{Joule}$$
        Esto demuestra rigurosamente que no hay ganancia de energía cinética ($a=0$), sino una conversión termodinámica perfecta del 100% de la energía potencial gravitatoria en calor disipado en la resistencia.
      `,
      rubric: `
        • 5 pts: Plantear y desarrollar analíticamente las expresiones de P_mec y P_Joule.<br>
        • 5 pts: Usar la condición de equilibrio terminal para demostrar la identidad y explicar su significado físico.
      `
    }
  ]
};
