/**
 * MÓDULO 6: INDUCTANCIA MUTUA Y TRANSFORMADORES
 * FIS120 / FIS12125 · UTFSM
 */

window.MODULE_DATA_MOD6 = {
  number: '6',
  title: 'Inductancia Mutua y Transformadores',
  description: 'Teorema de reciprocidad magnética, acoplamiento de flujo entre circuitos acoplados, bobinas concéntricas, solenoides inclinados y transformadores ideales.',
  hasInteractive: false,
  theory: `
    <p>
      Cuando dos circuitos conductores se encuentran próximos, la corriente variable que circula por el primero genera un campo magnético que atraviesa el área del segundo, induciendo en él una fuerza electromotriz. Este acoplamiento magnético se cuantifica mediante el coeficiente de <strong>inductancia mutua $M$</strong>.
    </p>

    <div class="box-formula">
      <strong>1. Definición y Teorema de Reciprocidad (Formulario C3):</strong>
      $$M = \\frac{N_2 \\phi_{12}}{I_1} = \\frac{N_1 \\phi_{21}}{I_2}$$
      <p>
        Donde:
        <br>• $\\phi_{12}$ es el flujo magnético producido por la corriente $I_1$ que atraviesa <em>una sola vuelta</em> del circuito 2.
        <br>• $N_2$ es el número de vueltas del circuito 2.
        <br>• <strong>Teorema de Reciprocidad:</strong> $M_{12} = M_{21} = M$. ¡Siempre puedes elegir calcular el flujo en la dirección geométrica más simple y el valor de $M$ será idéntico!
        <br>• <strong>fem inducida por inductancia mutua:</strong>
        $$\\varepsilon_2 = -M \\frac{dI_1}{dt} \\quad ; \\quad \\varepsilon_1 = -M \\frac{dI_2}{dt}$$
      </p>
    </div>

    <div class="figure-container">
      <img src="img/mod6_mutual_solenoid_square.svg" alt="Solenoide y bobina cuadrada">
      <div class="figure-caption">Solenoide ideal con bobina cuadrada exterior coaxial de lado $L > 2a$ (Simulacro C3 P3).</div>
    </div>

    <div class="box-method">
      <strong>2. Transformador Ideal:</strong>
      <p>
        Un transformador ideal consta de dos bobinas arrolladas sobre un núcleo ferromagnético de permeabilidad muy alta, de modo que el 100% del flujo magnético $\\phi_B(t)$ generado por el primario es enlazado por el secundario sin pérdidas.
        <br>• <strong>Relación de Transformación de Voltaje:</strong>
        $$V_p = -N_p \\frac{d\\phi_B}{dt}, \\quad V_s = -N_s \\frac{d\\phi_B}{dt} \\implies \\frac{V_s}{V_p} = \\frac{N_s}{N_p}$$
        • <strong>Conservación de Potencia Ideal:</strong>
        $$P_p = P_s \\implies V_p I_p = V_s I_s \\implies \\frac{I_s}{I_p} = \\frac{N_p}{N_s}$$
      </p>
    </div>

    <div class="box-warning">
      <strong>Estrategia de Oro para el Certamen (Uso de Reciprocidad):</strong><br>
      Si te piden calcular la fem en un circuito complejo producida por otro circuito sencillo (por ejemplo, calcular el flujo de una bobina cuadrada sobre un solenoide cilíndrico), NUNCA intentes calcular el campo no uniforme de la bobina cuadrada. <strong>Usa reciprocidad:</strong> calcula el campo uniforme del solenoide, halla $M = N_2 \\phi_{12}/I_1$, y luego aplica $\\varepsilon_1 = -M dI_2/dt$.
    </div>
  `,
  exercises: [
    {
      id: 'm6_ex1',
      title: 'Unidades y Naturaleza de la Inductancia Mutua',
      level: 'basic',
      source: 'Formulario C3',
      type: 'multiple_choice',
      statement: `
        La inductancia mutua $M$ entre dos bobinas mide el grado de acoplamiento geométrico. ¿Cuál de las siguientes unidades del SI es equivalente al Henrio $[\\text{H}]$?
      `,
      options: [
        '$\\text{V}\\cdot\\text{s} / \\text{A} = \\Omega\\cdot\\text{s}$',
        '$\\text{V} / (\\text{A}\\cdot\\text{s})$',
        '$\\text{T} / \\text{m}^2$',
        '$\\text{J} / \\text{C}$'
      ],
      correctOption: 0,
      explanation: `
        A partir de $|\\varepsilon| = M \\frac{dI}{dt}$, despejamos:
        $$[M] = \\frac{[\\varepsilon]}{[dI/dt]} = \\frac{\\text{Volt}}{\\text{Amperio/segundo}} = \\frac{\\text{V}\\cdot\\text{s}}{\\text{A}} = \\Omega\\cdot\\text{s} = \\text{Henrio [H]}$$
      `
    },
    {
      id: 'm6_ex2',
      title: 'fem Inducida por Acoplamiento Mutuo',
      level: 'basic',
      source: 'Cálculo Directo Formulario',
      type: 'numerical',
      statement: `
        Dos bobinas acopladas tienen una inductancia mutua de $M = 0.35\\text{ H}$. Si la corriente en la bobina primaria cambia a una tasa constante de $\\frac{dI_1}{dt} = 60.0\\text{ A/s}$, calcule la magnitud de la fem inducida en la bobina secundaria en voltios.
      `,
      placeholder: 'Ej: 21.0',
      units: 'V',
      correctValue: 21.0,
      tolerance: 0.03,
      explanation: `
        $$|\\varepsilon_2| = M \\left|\\frac{dI_1}{dt}\\right| = 0.35\\text{ H} \\cdot 60.0\\text{ A/s} = 21.0\\text{ V}$$
      `
    },
    {
      id: 'm6_ex3',
      title: 'Universalidad del Teorema de Reciprocidad',
      level: 'intermediate',
      source: 'Teoría Electromagnética UTFSM',
      type: 'true_false',
      statement: `
        El coeficiente de inductancia mutua entre dos conductores cumple siempre $M_{12} = M_{21}$, sin importar que un conductor sea infinitamente largo y el otro sea una diminuta espira cerrada de forma irregular.
      `,
      correct: true,
      justification: `
        Verdadero. La relación de reciprocidad magnética de Neumann demuestra que $M = \\frac{\\mu_0}{4\\pi} \\oint_{\\Gamma_1} \\oint_{\\Gamma_2} \\frac{d\\vec{l}_1 \\cdot d\\vec{l}_2}{|\\vec{r}_1 - \\vec{r}_2|}$, expresión simétrica bajo el intercambio de las etiquetas 1 y 2. Por tanto, $M_{12} = M_{21}$ es una propiedad geométrica exacta universal.
      `
    },
    {
      id: 'm6_ex4',
      title: 'Voltaje en Transformador Reductor',
      level: 'intermediate',
      source: 'Transformadores Ideales',
      type: 'numerical',
      statement: `
        Un transformador ideal reductor tiene un devanado primario de $N_p = 800\\text{ vueltas}$ y un secundario de $N_s = 40\\text{ vueltas}$. Si se alimenta con un voltaje alterno eficaz de $V_p = 220.0\\text{ V}$, calcule el voltaje eficaz en el secundario $V_s$ en voltios.
      `,
      placeholder: 'Ej: 11.0',
      units: 'V',
      correctValue: 11.0,
      tolerance: 0.03,
      explanation: `
        Por la relación del transformador ideal:
        $$V_s = V_p \\left(\\frac{N_s}{N_p}\\right) = 220.0 \\cdot \\left(\\frac{40}{800}\\right) = 220.0 \\cdot \\left(\\frac{1}{20}\\right) = 11.0\\text{ V}$$
      `
    },
    {
      id: 'm6_ex5',
      title: 'Solenoides Concéntricos Muy Largos y Corriente Armónica',
      level: 'certamen',
      source: 'Ayudantía 11 Problema 1',
      type: 'step_by_step',
      statement: `
        Se cuenta con dos solenoides ideales concéntricos muy largos de longitud $l$. El solenoide interno tiene radio $R$ y $N_i$ vueltas, mientras que el externo tiene radio $3R$ y $N_e$ vueltas. Por la espira interna circula una corriente $I(t)$ en sentido antihorario.<br>
        a) Determine el flujo magnético sobre una vuelta del solenoide de radio $3R$.<br>
        b) Encuentre la inductancia mutua $M$ entre ambas bobinas.<br>
        c) Si la corriente interna varía según $I(t) = I_0 \\cos(\\omega t)$ con $I_0, \\omega > 0$, determine la fem inducida en el solenoide exterior en función del tiempo.
      `,
      steps: [
        {
          title: 'Paso 1: Campo magnético del solenoide interno y flujo sobre una vuelta exterior',
          content: `
            El solenoide interno (radio $R$, densidad $n_i = N_i/l$) transporta corriente $I$ y produce un campo magnético confinado a su interior:
            $$\\vec{B}_i = \\mu_0 \\frac{N_i}{l} I\\,\\hat{z} \\quad (r < R), \\qquad \\vec{B}_i = 0 \\quad (r > R)$$
            Para una vuelta del solenoide exterior (radio $3R$), tomamos como normal $\\hat{n} = +\\hat{z}$. El flujo magnético se integra sobre el disco de radio $3R$, pero como el campo es nulo para $r > R$, la integral se reduce estrictamente a la sección del solenoide interno:
            $$\\phi_1 = \\iint_{r \\le 3R} \\vec{B}_i\\cdot d\\vec{A} = \\iint_{r \\le R} \\left(\\mu_0 \\frac{N_i}{l} I\\right) dA + \\iint_{R < r \\le 3R} 0\\,dA = \\mu_0 \\frac{N_i}{l} \\pi R^2 I$$
          `
        },
        {
          title: 'Paso 2: Inductancia mutua entre las bobinas',
          content: `
            El flujo concatenado con las $N_e$ espiras de la bobina externa debido a la corriente interna $I$ es $\\Phi_{total} = N_e \\phi_1$.<br>
            Por definición de inductancia mutua:
            $$M = \\frac{N_e \\phi_1}{I} = \\mu_0 \\frac{N_i N_e \\pi R^2}{l}$$
            Obsérvese que $M$ depende únicamente de la geometría y del radio $R$ de la bobina interna, sin depender del radio $3R$ de la bobina externa.
          `
        },
        {
          title: 'Paso 3: fem inducida con corriente armónica',
          content: `
            Aplicando la Ley de Faraday para la inductancia mutua:
            $$\\varepsilon_e(t) = -M \\frac{dI}{dt} = -M \\frac{d}{dt}(I_0 \\cos(\\omega t)) = -M (-I_0 \\omega \\sin(\\omega t)) = M I_0 \\omega \\sin(\\omega t)$$
            Sustituyendo la inductancia mutua $M$:
            $$\\varepsilon_e(t) = \\mu_0 \\frac{N_i N_e \\pi R^2}{l} I_0 \\omega \\sin(\\omega t)$$
          `
        }
      ]
    },
    {
      id: 'm6_ex6',
      title: 'Alambre Infinito y Rectángulo Conductor',
      level: 'certamen',
      source: 'Ayudantía 11 Problema 2',
      type: 'step_by_step',
      statement: `
        Considere un alambre conductor muy delgado e infinito con corriente variable $I(t) = I_0 e^{-t/\\tau}$ ($t > 0$). Un rectángulo conductor de lados $a$ (en $x$) y $b$ (en $y$) está fijo sobre el plano $xy$ a una distancia $a$ del cable (ubicado entre $x = a$ y $x = 2a$).<br>
        a) Obtenga el flujo magnético a través del rectángulo.<br>
        b) Determine la inductancia mutua $M$ entre el alambre y el rectángulo.<br>
        c) Calcule la fem inducida y fundamente su sentido con Lenz.
      `,
      steps: [
        {
          title: 'Paso 1: Cálculo del flujo magnético en el rectángulo',
          content: `
            El campo del cable infinito a distancia $x$ es $B(x) = \\frac{\\mu_0 I(t)}{2\\pi x}$ entrando al plano ($\\otimes$).<br>
            Tomando $\\hat{n}$ entrando, el elemento diferencial de área es $dA = b\\,dx$:
            $$\\phi_B(t) = \\int_a^{2a} \\left(\\frac{\\mu_0 I(t)}{2\\pi x}\\right) b\\,dx = \\frac{\\mu_0 I(t) b}{2\\pi} \\int_a^{2a} \\frac{dx}{x} = \\frac{\\mu_0 I(t) b}{2\\pi} [\\ln x]_a^{2a} = \\frac{\\mu_0 b \\ln 2}{2\\pi} I(t)$$
          `
        },
        {
          title: 'Paso 2: Determinación de la inductancia mutua M',
          content: `
            Como el rectángulo consta de una sola vuelta ($N = 1$):
            $$M = \\frac{\\phi_B(t)}{I(t)} = \\frac{\\mu_0 b \\ln 2}{2\\pi}$$
            Observe que $M$ depende únicamente de las dimensiones geométricas ($b$ y la razón de distancias $2a/a=2$) y de $\\mu_0$, siendo completamente independiente de la corriente y del tiempo.
          `
        },
        {
          title: 'Paso 3: fem inducida y sentido de Lenz',
          content: `
            Aplicando la relación $\\varepsilon = -M \\frac{dI}{dt}$:
            $$\\varepsilon(t) = -M \\left(-\\frac{I_0}{\\tau} e^{-t/\\tau}\\right) = \\frac{M I_0}{\\tau} e^{-t/\\tau} = \\frac{\\mu_0 b I_0 \\ln 2}{2\\pi \\tau} e^{-t/\\tau}$$
            <strong>Sentido:</strong> Dado que la corriente del cable decrece, el flujo entrante ($\\otimes$) a través del rectángulo disminuye. Por la Ley de Lenz, la corriente inducida genera campo entrante para compensar la pérdida, lo que por regla de la mano derecha corresponde a <strong>sentido horario</strong>.
          `
        }
      ]
    },
    {
      id: 'm6_ex7',
      title: 'Solenoide Coaxial con Bobina Cuadrada Exterior',
      level: 'certamen',
      source: 'Simulacro Certamen 3 Problema 3',
      type: 'step_by_step',
      figure: 'img/mod6_mutual_solenoid_square.svg',
      figureCaption: 'Solenoide de radio $a$ y bobina cuadrada coaxial de $N$ espiras de lado $L > 2a$.',
      statement: `
        Un solenoide ideal muy largo de radio $a$ y $n$ vueltas por metro transporta una corriente $I(t)$ antihoraria vista de frente. Rodeándolo en su zona central hay una bobina de $N$ espiras cuadradas de lado $L > 2a$, coaxial con él.<br>
        a) Determine la inductancia mutua $M$ entre el solenoide y la bobina cuadrada.<br>
        b) Si $I(t) = I_0(1 - e^{-t/\\tau})$, determine la fem inducida en la bobina cuadrada y su sentido por Lenz.<br>
        c) Si ahora el solenoide se abre y por la bobina cuadrada circula $I_2(t) = \\alpha t$, determine la fem en el solenoide sin calcular el campo de la bobina. ¿Depende de $L$?
      `,
      steps: [
        {
          title: 'Paso 1: Inductancia mutua del sistema solenoide-bobina cuadrada',
          content: `
            El solenoide ideal genera un campo magnético estrictamente confinado a su interior ($r < a$):
            $$B = \\mu_0 n I_1$$
            Fuera del solenoide ($r > a$), el campo es nulo: $B = 0$.<br>
            Como la bobina cuadrada tiene lado $L > 2a$, encierra completamente la sección transversal circular del solenoide. Por tanto, el flujo magnético que atraviesa cada una de las espiras cuadradas proviene únicamente del disco de radio $a$:
            $$\\phi_{12} = B \\cdot (\\pi a^2) = (\\mu_0 n I_1) (\\pi a^2) = \\mu_0 n \\pi a^2 I_1$$
            Para las $N$ espiras de la bobina cuadrada:
            $$M = \\frac{N \\phi_{12}}{I_1} = \\mu_0 n N \\pi a^2$$
          `
        },
        {
          title: 'Paso 2: fem inducida con corriente exponencial',
          content: `
            Con $I_1(t) = I_0(1 - e^{-t/\\tau})$:
            $$\\frac{dI_1}{dt} = \\frac{I_0}{\\tau} e^{-t/\\tau}$$
            $$\\varepsilon_2(t) = -M \\frac{dI_1}{dt} = -\\frac{\\mu_0 n N \\pi a^2 I_0}{\\tau} e^{-t/\\tau}$$
            <strong>Sentido según Lenz:</strong> Al inicio la corriente $I_1$ crece desde 0, aumentando el flujo saliente $\\odot$. La bobina cuadrada se opone induciendo campo entrante $\\otimes$, lo que corresponde a corriente en <strong>sentido horario</strong>.
          `
        },
        {
          title: 'Paso 3: Aplicación del teorema de reciprocidad',
          content: `
            Por el Teorema de Reciprocidad, la inductancia mutua es la misma: $M_{21} = M_{12} = M$.<br>
            La fem inducida en el solenoide debido a la corriente en la bobina cuadrada es:
            $$|\\varepsilon_1(t)| = M \\left|\\frac{dI_2}{dt}\\right| = (\\mu_0 n N \\pi a^2) \\frac{d}{dt}(\\alpha t) = \\mu_0 n N \\pi a^2 \\alpha$$
            <strong>¿Depende este resultado de $L$?</strong><br>
            <strong>NO depende de $L$</strong>, siempre y cuando $L > 2a$, porque todo el flujo acoplado está restringido al volumen interior del solenoide (radio $a$). ¡El espacio exterior vacío entre el solenoide y el cuadrado no contiene campo magnético!
          `
        }
      ]
    },
    {
      id: 'm6_ex7b',
      title: 'Bobina Larga con Espira Inclinada en Ángulo α',
      level: 'certamen',
      source: 'Ayudantía 11 Problema 4',
      type: 'step_by_step',
      statement: `
        Considere una bobina muy larga de radio $a$ y $n$ vueltas por unidad de largo. Al interior de la bobina, existe una espira de radio $b < a$ cuyo vector normal forma un ángulo $\\alpha$ con respecto al eje longitudinal de la bobina.<br>
        a) Determine la inductancia mutua $M$ entre la bobina y la espira interior.<br>
        b) Si por la bobina circula una corriente $I(t) = I_0 \\sin(\\omega t)$, determine la fem inducida en la espira en función del tiempo.
      `,
      steps: [
        {
          title: 'Paso 1: Campo en el interior de la bobina y vector normal',
          content: `
            La bobina muy larga (solenoide ideal) de densidad de vueltas $n$ produce en su interior un campo magnético uniforme paralelo a su eje:
            $$\\vec{B}(t) = \\mu_0 n I(t)\\,\\hat{z}$$
            La espira de radio $b$ está inclinada un ángulo $\\alpha$ respecto al eje $\\hat{z}$, por lo que su vector normal unitario satisface $\\hat{n}\\cdot\\hat{z} = \\cos\\alpha$.
          `
        },
        {
          title: 'Paso 2: Flujo magnético e inductancia mutua M',
          content: `
            El flujo magnético a través de la espira circular de área $A = \\pi b^2$ es:
            $$\\phi_B(t) = \\iint_{\\text{espira}} \\vec{B}\\cdot d\\vec{A} = (\\mu_0 n I(t)) (\\pi b^2) \\cos\\alpha = \\mu_0 n \\pi b^2 \\cos\\alpha\\,I(t)$$
            Dado que la espira consta de una sola vuelta ($N_{espira} = 1$), la inductancia mutua es:
            $$M = \\frac{\\phi_B(t)}{I(t)} = \\mu_0 n \\pi b^2 \\cos\\alpha$$
            Note que para $\\alpha = 0^\\circ$ el acoplamiento es máximo ($M = \\mu_0 n \\pi b^2$), mientras que para $\\alpha = 90^\\circ$ la espira es paralela al campo y el acoplamiento es nulo ($M = 0$).
          `
        },
        {
          title: 'Paso 3: fem inducida por Faraday-Lenz',
          content: `
            Con $I(t) = I_0 \\sin(\\omega t)$, derivamos respecto al tiempo:
            $$\\frac{dI}{dt} = I_0 \\omega \\cos(\\omega t)$$
            Por la ley de Faraday:
            $$\\varepsilon_{ind}(t) = -M \\frac{dI}{dt} = -(\\mu_0 n \\pi b^2 \\cos\\alpha) I_0 \\omega \\cos(\\omega t) = -\\mu_0 n \\pi b^2 \\cos\\alpha\\,I_0 \\omega \\cos(\\omega t)$$
            La magnitud de la fem inducida es $|\\varepsilon_{ind}(t)| = \\mu_0 n \\pi b^2 \\cos\\alpha\\,I_0 \\omega |\\cos(\\omega t)|$.
          `
        }
      ]
    },
    {
      id: 'm6_ex7c',
      title: 'Rollo Circular con Espira Central Pequeña y Decaimiento Exponencial',
      level: 'certamen',
      source: 'Pauta Certamen 3 2026-1 Problema 2',
      type: 'step_by_step',
      statement: `
        Con un conductor aislado se fabrica un rollo plano de $N$ vueltas circulares de radio $R$ sobre una mesa. En torno a su centro se ubica una pequeña espira circular de radio $r \\ll R$. Por el rollo circula una corriente $I(t)$ en sentido antihorario.<br>
        a) Encuentre una expresión para la inductancia mutua $M$ del sistema formado por el rollo y la pequeña espira.<br>
        b) Si la corriente varía según $I(t) = I_0$ para $t < 0$ e $I(t) = I_0 e^{-t/\\tau}$ para $t \\ge 0$, encuentre la fem inducida en la pequeña espira en función del tiempo.<br>
        c) Indique el sentido de la fem inducida para $t < 0$ y $t \\ge 0$, fundamentando rigurosamente con la Ley de Lenz.
      `,
      steps: [
        {
          title: 'Paso 1: Campo en el centro e inductancia mutua',
          content: `
            El campo magnético en el centro de un rollo de $N$ espiras de radio $R$ con corriente $I(t)$ antihoraria apunta perpendicular a la mesa ($+\\hat{k}$) y vale:
            $$B(t) = \\frac{N \\mu_0 I(t)}{2R}$$
            Como $r \\ll R$, el campo es prácticamente uniforme sobre toda el área $A = \\pi r^2$ de la pequeña espira central.<br>
            Tomando $\\hat{n} = +\\hat{k}$, el flujo magnético en la pequeña espira ($N_{espira} = 1$) es:
            $$\\phi_B(t) = B(t) \\cdot (\\pi r^2) = \\frac{N \\mu_0 \\pi r^2}{2R} I(t)$$
            Por definición, la inductancia mutua del sistema es:
            $$M = \\frac{\\phi_B(t)}{I(t)} = \\frac{N \\mu_0 \\pi r^2}{2R}$$
          `
        },
        {
          title: 'Paso 2: Cálculo de la fem inducida en ambos intervalos de tiempo',
          content: `
            Aplicando $\\varepsilon_{ind}(t) = -M \\frac{dI}{dt}$:<br>
            • <strong>Para $t < 0$:</strong> La corriente es constante ($I(t) = I_0$), por lo que $\\frac{dI}{dt} = 0$:
            $$\\varepsilon_{ind}(t) = 0$$
            • <strong>Para $t \\ge 0$:</strong> La corriente decae exponencialmente:
            $$\\frac{dI}{dt} = -\\frac{I_0}{\\tau} e^{-t/\\tau} \\implies \\varepsilon_{ind}(t) = -M \\left(-\\frac{I_0}{\\tau} e^{-t/\\tau}\\right) = \\frac{N \\mu_0 \\pi r^2 I_0}{2R\\tau} e^{-t/\\tau}$$
          `
        },
        {
          title: 'Paso 3: Justificación del sentido según la Ley de Lenz',
          content: `
            • <strong>Para $t < 0$:</strong> Como no hay variación de flujo magnético en el tiempo ($d\\phi_B/dt = 0$), no se induce fem ni corriente en la espira central.<br>
            • <strong>Para $t \\ge 0$:</strong> La corriente externa $I(t)$ decrece, provocando una disminución del flujo magnético saliente ($\\odot$). Por la Ley de Lenz, el sistema reacciona induciendo una corriente que genere un campo magnético en el mismo sentido original ($\\odot$) para frenar la pérdida de flujo.<br>
            Por la regla de la mano derecha, un campo saliente exige que la corriente circule en <strong>sentido antihorario</strong>.
          `
        }
      ]
    },
    {
      id: 'm6_ex8',
      title: 'El Transformador Ideal y la Corriente Continua',
      level: 'certamen',
      source: 'Ayudantía 11 Problema Conceptual 1',
      type: 'conceptual',
      statement: `
        Un transformador ideal cuenta con dos bobinas enrolladas en un núcleo ferromagnético (primaria con $N_p$ y secundaria con $N_s$).<br>
        a) ¿Cómo se relaciona el voltaje de la bobina primaria y la secundaria?<br>
        b) ¿Puede funcionar un transformador con corriente continua (CC)? Explique físicamente qué ocurriría si se conecta a una batería de CC.
      `,
      modelAnswer: `
        <strong>a) Relación de voltajes:</strong><br>
        Suponiendo que no hay dispersión de flujo magnético en el núcleo ferromagnético cerrado, cada espira de ambos devanados está atravesada por el mismo flujo magnético instantáneo $\\phi_B(t)$. Por la Ley de Faraday:
        $$V_p(t) = -N_p \\frac{d\\phi_B}{dt}, \\quad V_s(t) = -N_s \\frac{d\\phi_B}{dt}$$
        Dividiendo ambas ecuaciones se obtiene la relación de transformación:
        $$\\frac{V_s(t)}{V_p(t)} = \\frac{N_s}{N_p}$$
        <br>
        <strong>b) Imposibilidad de funcionamiento con Corriente Continua:</strong><br>
        <strong>NO puede funcionar con corriente continua en régimen permanente.</strong><br>
        La inducción electromagnética requiere una <em>variación temporal</em> del flujo magnético ($d\\phi_B/dt \\neq 0$). Con corriente continua pura, la corriente $I_p$ es constante, el campo magnético $\\vec{B}$ es estático y por tanto $\\frac{d\\phi_B}{dt} = 0$, lo que implica que el voltaje inducido en el secundario es exactamente <strong>cero</strong> ($V_s = 0$).<br><br>
        <strong>Peligro físico:</strong> Si se conecta un transformador real a una fuente de CC, al no existir una contra-fem inducida en el primario tras el transitorio inicial, la corriente queda limitada únicamente por la pequeñísima resistencia óhmica del alambre ($I = V/R_{cable}$), lo cual provocará un sobrecalentamiento destructivo por efecto Joule y quemará el bobinado.
      `,
      rubric: `
        • 5 pts: Deducción rigurosa de V_s / V_p = N_s / N_p mediante Faraday.<br>
        • 5 pts: Explicación de dPhi/dt = 0 con CC y análisis del sobrecalentamiento por falta de contra-fem.
      `
    }
  ]
};
