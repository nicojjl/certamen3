/**
 * MÓDULO 1: LEY DE BIOT-SAVART Y CAMPO MAGNÉTICO DE CORRIENTES
 * FIS120 / FIS12125 · UTFSM
 */

window.MODULE_DATA_MOD1 = {
  number: '1',
  title: 'Biot-Savart y Campo Magnético de Cables',
  description: 'Cálculo del campo magnético generado por corrientes estacionarias: cable recto infinito y finito, espiras circulares, arcos y superposición vectorial con regla de la mano derecha.',
  hasInteractive: false,
  theory: `
    <p>
      La Ley de Biot-Savart es el análogo magnético de la Ley de Coulomb: permite calcular el campo magnético $\\vec{B}$ producido en cualquier punto del espacio por una distribución arbitraria de corrientes estacionarias integrando elemento a elemento.
    </p>

    <div class="box-formula">
      <strong>1. Expresión Fundamental de Biot-Savart (Formulario C3):</strong>
      $$d\\vec{B} = \\frac{\\mu_0}{4\\pi} \\frac{I d\\vec{l} \\times \\hat{r}}{r^2} = \\frac{\\mu_0}{4\\pi} \\frac{I d\\vec{l} \\times \\vec{r}}{|\\vec{r}|^3}$$
      <p>
        Donde:
        <br>• $d\\vec{l}$ es el vector tangente al conductor en el sentido de la corriente $I$.
        <br>• $\\vec{r} = \\vec{r}_{obs} - \\vec{r}_{fuente}$ es el vector posición relativo que apunta desde el elemento de corriente hacia el punto donde se mide el campo.
        <br>• $\\mu_0 = 4\\pi \\times 10^{-7}\\ [\\text{H/m}]$ es la permeabilidad magnética del vacío.
      </p>
    </div>

    <div class="figure-container">
      <img src="img/mod1_wire_bfield.svg" alt="Campo Magnético de un Cable Recto">
      <div class="figure-caption">Líneas de campo concéntricas generadas por un cable recto infinito: $\\vec{B}(r) = \\frac{\\mu_0 I}{2\\pi r}\\hat{\\theta}$.</div>
    </div>

    <div class="box-method">
      <strong>2. Geometrías Canónicas Esenciales para Certámenes UTFSM:</strong>
      <p>
        <strong>A. Cable Recto Finito (longitud $2L$, a distancia perpendicular $d$ de su punto medio):</strong>
        $$B = \\frac{\\mu_0 I}{4\\pi d} \\left(\\frac{2L}{\\sqrt{d^2 + L^2}}\\right)$$
        • Si el cable es <em>muy largo o infinito</em> ($L \\gg d$), $\\frac{L}{\\sqrt{d^2 + L^2}} \\to 1$:
        $$B = \\frac{\\mu_0 I}{2\\pi d}$$
        <br>
        <strong>B. Arco de Circunferencia (radio $R$, subtiende ángulo $\\Delta\\theta$ en radianes):</strong>
        Dado que $d\\vec{l} \\perp \\hat{r}$ en todo el arco, $|d\\vec{l} \\times \\hat{r}| = dl = R\\,d\\theta$:
        $$B_{centro} = \\frac{\\mu_0 I}{4\\pi R^2} \\int_0^{\\Delta\\theta} R\\,d\\theta = \\frac{\\mu_0 I \\Delta\\theta}{4\\pi R}$$
        • Para una <strong>espira circular completa</strong> ($\\Delta\\theta = 2\\pi$):
        $$B_{centro} = \\frac{\\mu_0 I}{2R}$$
        • Para media espira ($\\Delta\\theta = \\pi$): $B = \\frac{\\mu_0 I}{4R}$.<br>
        • Para un cuarto de espira ($\\Delta\\theta = \\pi/2$): $B = \\frac{\\mu_0 I}{8R}$.
      </p>
    </div>

    <div class="figure-container">
      <img src="img/mod1_sim2_geometry.svg" alt="Configuración simulacro 2">
      <div class="figure-caption">Problema típico de certamen: superposición de arco circular y segmento rectilíneo finito en el espacio.</div>
    </div>

    <div class="box-warning">
      <strong>Errores Fatales en el Certamen:</strong><br>
      1. <strong>Segmentos alineados con el punto:</strong> Si un cable recto apunta directamente hacia el punto de cálculo (o se aleja radialmente de él), entonces $d\\vec{l} \\parallel \\vec{r}$, lo que implica $d\\vec{l}\\times\\hat{r} = \\vec{0}$. ¡Esos tramos aportan CERO campo magnético!<br>
      2. <strong>Sumar magnitudes en vez de vectores:</strong> Campos que apuntan en distintas direcciones (por ejemplo, uno en $+\\hat{k}$ y otro en $+\\hat{\\jmath}$) NUNCA se suman algebraicamente; deben expresarse en componentes cartesianas: $\\vec{B}_{neto} = \\vec{B}_1 + \\vec{B}_2$.
    </div>
  `,
  exercises: [
    {
      id: 'm1_ex1',
      title: 'Campo en el Centro de una Espira Circular',
      level: 'basic',
      source: 'Formulario C3 (oficial)',
      type: 'multiple_choice',
      statement: `
        Por una espira circular plana de radio $R = 5.0\\text{ cm}$ circula una corriente $I = 2.0\\text{ A}$ en sentido antihorario vista desde arriba (plano $xy$). ¿Cuál es el vector campo magnético $\\vec{B}$ en el centro exacto de la espira?
      `,
      options: [
        '$2.51 \\times 10^{-5}\\,\\hat{k}\\text{ T}$',
        '$-2.51 \\times 10^{-5}\\,\\hat{k}\\text{ T}$',
        '$1.26 \\times 10^{-5}\\,\\hat{k}\\text{ T}$',
        '$5.03 \\times 10^{-5}\\,\\hat{k}\\text{ T}$'
      ],
      correctOption: 0,
      explanation: `
        Usamos la fórmula para el centro de una espira circular:
        $$B = \\frac{\\mu_0 I}{2R} = \\frac{(4\\pi \\times 10^{-7})\\cdot 2.0}{2 \\cdot 0.05} = 2.513 \\times 10^{-5}\\text{ T}$$
        Por regla de la mano derecha, dedos curvados en sentido antihorario en el plano $xy$ implican que el pulgar apunta hacia arriba, en la dirección $+\\hat{k}$.
      `
    },
    {
      id: 'm1_ex2',
      title: 'Campo a Distancia de un Cable Recto Infinito',
      level: 'basic',
      source: 'Ejercicio original (no oficial)',
      type: 'numerical',
      statement: `
        Un cable recto muy largo transporta una corriente de $I = 15.0\\text{ A}$. Calcule la magnitud del campo magnético $B$ a una distancia radial de $r = 6.0\\text{ cm} = 0.060\\text{ m}$ del cable.
      `,
      placeholder: 'Ej: 5.0e-5',
      units: 'T',
      correctValue: 0.00005,
      tolerance: 0.04,
      explanation: `
        Aplicamos la fórmula del cable infinito:
        $$B = \\frac{\\mu_0 I}{2\\pi r} = \\frac{(4\\pi \\times 10^{-7}) \\cdot 15.0}{2\\pi \\cdot 0.060} = \\frac{2 \\times 10^{-7} \\cdot 15.0}{0.060} = 5.0 \\times 10^{-5}\\text{ T} = 50\\,\\mu\\text{T}$$
      `
    },
    {
      id: 'm1_ex3',
      title: 'Contribución de Tramos Radiales',
      level: 'intermediate',
      source: 'Ejercicio original (no oficial)',
      type: 'true_false',
      statement: `
        En un circuito formado por dos arcos concéntricos unidos por dos segmentos rectilíneos radiales dirigidos hacia el centro de curvatura $O$, el campo magnético total en $O$ depende únicamente de los arcos circulares, ya que los segmentos radiales no producen campo en dicho punto.
      `,
      correct: true,
      justification: `
        Verdadero. Para los segmentos rectilíneos que apuntan directamente hacia el centro $O$, el vector desplazamiento relativo $\\vec{r}$ desde cualquier punto del segmento hacia $O$ es colineal con el elemento de corriente $d\\vec{l}$ (ángulo $\\theta = 0^\\circ$ o $180^\\circ$). Por lo tanto, el producto vectorial $d\\vec{l} \\times \\hat{r} = \\vec{0}$, anulando idénticamente la contribución de esos tramos en $O$.
      `
    },
    {
      id: 'm1_ex4',
      title: 'Campo de un Cuarto de Circunferencia',
      level: 'intermediate',
      source: 'Ejercicio original (no oficial)',
      type: 'multiple_choice',
      statement: `
        Un conductor fino transporta una corriente $I$ y forma un arco correspondiente a un cuarto de circunferencia de radio $R$ ubicado en el plano $xy$ con centro en el origen. ¿Cuál es la magnitud del campo magnético producido en el origen $O$?
      `,
      options: [
        '$\\frac{\\mu_0 I}{8R}$',
        '$\\frac{\\mu_0 I}{4R}$',
        '$\\frac{\\mu_0 I}{2R}$',
        '$\\frac{\\mu_0 I}{16R}$'
      ],
      correctOption: 0,
      explanation: `
        Un cuarto de circunferencia subtiende un ángulo de $\\Delta\\theta = \\frac{\\pi}{2}$ radianes.
        $$B = \\frac{\\mu_0 I \\Delta\\theta}{4\\pi R} = \\frac{\\mu_0 I (\\pi/2)}{4\\pi R} = \\frac{\\mu_0 I}{8R}$$
      `
    },
    {
      id: 'm1_ex5',
      title: 'Punto de Campo Neto Nulo entre Dos Cables Paralelos',
      level: 'intermediate',
      source: 'Ejercicio original (no oficial)',
      type: 'numerical',
      statement: `
        Dos cables rectos paralelos e infinitos están separados por una distancia $d = 30.0\\text{ cm}$. El cable 1 transporta una corriente $I_1 = 4.0\\text{ A}$ y el cable 2 transporta $I_2 = 8.0\\text{ A}$, ambas en el mismo sentido hacia $+z$. ¿A qué distancia del cable 1 (a lo largo del segmento que une ambos cables) el campo magnético neto se anula?
      `,
      placeholder: 'Ej: 10.0',
      units: 'cm',
      correctValue: 10.0,
      tolerance: 0.03,
      explanation: `
        Sea $x$ la distancia desde el cable 1 (con $0 < x < d$). Como las corrientes tienen el mismo sentido, por regla de la mano derecha sus campos magnéticos en la región intermedia tienen sentidos opuestos y se restan:
        $$B_1 = \\frac{\\mu_0 I_1}{2\\pi x}, \\quad B_2 = \\frac{\\mu_0 I_2}{2\\pi (d - x)}$$
        Igualando para que el campo neto sea cero:
        $$\\frac{I_1}{x} = \\frac{I_2}{d - x} \\implies I_1(d - x) = I_2 x \\implies x = \\frac{I_1}{I_1 + I_2} d$$
        Sustituyendo los valores:
        $$x = \\frac{4.0}{4.0 + 8.0} \\cdot 30.0\\text{ cm} = \\frac{1}{3} \\cdot 30.0\\text{ cm} = 10.0\\text{ cm}$$
      `
    },
    {
      id: 'm1_ex6',
      title: 'Superposición: Arco Circular y Segmento Finito Paralelo a z',
      level: 'certamen',
      source: 'Ejercicio original (no oficial)',
      type: 'step_by_step',
      figure: 'img/mod1_sim2_geometry.svg',
      figureCaption: 'Configuración: Arco de radio $R$ en 4to cuadrante + segmento recto de longitud $4R$ en $x=2R, y=0$.',
      statement: `
        Considere un arco de circunferencia de radio $R$ con centro en el origen $O$, ubicado en el cuarto cuadrante del plano $xy$ (desde $\\theta = -\\pi/2$ hasta $\\theta = 0$), que transporta una corriente estacionaria $I$ en sentido antihorario. Además, un segmento conductor rectilíneo de longitud $4R$, paralelo al eje $z$, con centro sobre el eje $x$ a una distancia $2R$ del origen (se extiende desde $z = -2R$ hasta $z = 2R$ en la posición fija $x = 2R, y = 0$), transporta una corriente $I$ en dirección $+\\hat{k}$. Determine el vector campo magnético resultante $\\vec{B}_{neto}$ en el origen $O$.
      `,
      steps: [
        {
          title: 'Paso 1: Campo generado por el arco circular en el origen O',
          content: `
            El arco se encuentra en el plano $xy$ y abarca el cuarto cuadrante: $\\Delta\\theta = \\pi/2$.<br>
            La corriente circula en sentido antihorario (de $-\\pi/2$ a $0$). Por regla de la mano derecha, el campo generado en el centro apunta en la dirección perpendicular saliendo del plano: $+\\hat{k}$.
            $$\\vec{B}_{arco} = \\frac{\\mu_0 I (\\pi/2)}{4\\pi R}\\,\\hat{k} = \\frac{\\mu_0 I}{8R}\\,\\hat{k}$$
          `
        },
        {
          title: 'Paso 2: Campo generado por el segmento recto finito de longitud 4R',
          content: `
            El segmento recto tiene longitud $2L = 4R$ (es decir, $L = 2R$) y está ubicado en la recta vertical $(2R, 0, z)$ con $z \\in [-2R, 2R]$.<br>
            La distancia perpendicular más corta desde el origen $O=(0,0,0)$ al conductor es $d = 2R$ (a lo largo del eje $+x$).<br>
            Aplicamos la fórmula del cable finito simétrico:
            $$B_{seg} = \\frac{\\mu_0 I}{4\\pi d} \\left(\\frac{2L}{\\sqrt{d^2 + L^2}}\\right)$$
            Con $d = 2R$ y $L = 2R$:
            $$\\sqrt{d^2 + L^2} = \\sqrt{(2R)^2 + (2R)^2} = \\sqrt{8R^2} = 2\\sqrt{2} R$$
            $$B_{seg} = \\frac{\\mu_0 I}{4\\pi (2R)} \\left(\\frac{4R}{2\\sqrt{2} R}\\right) = \\frac{\\mu_0 I}{8\\pi R} \\cdot \\frac{2}{\\sqrt{2}} = \\frac{\\sqrt{2}\\mu_0 I}{8\\pi R}$$
          `
        },
        {
          title: 'Paso 3: Determinación del versor de dirección por regla de la mano derecha',
          content: `
            El cable transporta corriente en $+\\hat{k}$ (saliendo de la página) y está en $(2R, 0)$.<br>
            El vector relativo desde el cable hacia el origen $O$ apunta en la dirección $-\\hat{\\imath}$.<br>
            Por la Ley de Biot-Savart, la dirección del campo es $d\\vec{l} \\times \\hat{r}_{fuente\\to obs}$:
            $$\\hat{k} \\times (-\\hat{\\imath}) = -(\\hat{k} \\times \\hat{\\imath}) = -\\hat{\\jmath}$$
            Por lo tanto, el vector campo del segmento recto en el origen apunta hacia el eje $-y$:
            $$\\vec{B}_{seg} = -\\frac{\\sqrt{2}\\mu_0 I}{8\\pi R}\\,\\hat{\\jmath}$$
          `
        },
        {
          title: 'Paso 4: Superposición vectorial y resultado final verificado',
          content: `
            Sumando vectorialmente ambas contribuciones ortogonales:
            $$\\vec{B}_{neto}(O) = \\vec{B}_{seg} + \\vec{B}_{arco} = -\\frac{\\sqrt{2}\\mu_0 I}{8\\pi R}\\,\\hat{\\jmath} + \\frac{\\mu_0 I}{8R}\\,\\hat{k}$$
            Factorizando la constante común:
            $$\\vec{B}_{neto}(O) = \\frac{\\mu_0 I}{8R} \\left( -\\frac{\\sqrt{2}}{\\pi}\\,\\hat{\\jmath} + \\hat{k} \\right)$$
            <strong>Chequeo dimensional:</strong> $[\\mu_0 I / R] = \\text{Tesla}$, correcto. Ambos términos son coherentes con las reglas de la mano derecha.
          `
        }
      ]
    },
    {
      id: 'm1_ex7',
      title: 'Biot-Savart vs. Ley de Ampère: Criterio de Selección',
      level: 'certamen',
      source: 'Ejercicio original (no oficial)',
      type: 'conceptual',
      statement: `
        Explique detalladamente bajo qué circunstancias un estudiante está OBLIGADO a utilizar la Ley de Biot-Savart para determinar el campo magnético en lugar de la Ley de Ampère, y por qué la Ley de Ampère no es útil en dichas situaciones a pesar de ser siempre válida formalmente.
      `,
      modelAnswer: `
        La Ley de Ampère $\\oint \\vec{B}\\cdot d\\vec{l} = \\mu_0 I_{enl}$ es una ley fundamental de la naturaleza y es <em>siempre verdadera</em> en magnetostática. Sin embargo, solo es <em>útil para despejar $\\vec{B}$</em> cuando la distribución de corriente posee un <strong>grado de simetría extremadamente alto</strong> (simetría cilíndrica infinita, planar infinita, o solenoide/toroide ideal).
        <br><br>
        En estas configuraciones simétricas, es posible elegir un lazo cerrado $\\Gamma$ sobre el cual la magnitud $|\\vec{B}|$ es estrictamente constante y el campo es colineal con la trayectoria ($\\vec{B}\\cdot d\\vec{l} = B dl$), permitiendo sacar $B$ fuera de la integral: $B \\oint dl = B(2\\pi r) = \\mu_0 I_{enl}$.
        <br><br>
        Un estudiante está <strong>obligado a usar la Ley de Biot-Savart</strong> cuando:
        <br>1. El conductor es de <strong>longitud finita</strong> (por ejemplo, un segmento recto de largo $L$), ya que se rompe la simetría traslacional en $z$ y el campo adquiere componentes complejas dependientes de la posición.
        <br>2. Se tienen <strong>espiras curvas o arcos</strong> y se busca el campo en puntos específicos (como el eje o el centro), donde no existe un lazo amperiano cerrado de campo constante que enlace la corriente sin cruzar líneas asimétricas.
        <br>3. Puntos <strong>fuera del eje de simetría</strong> en sistemas no infinitos.
        <br>En estos casos, no existe ningún lazo amperiano donde $B$ sea constante, por lo que la integral de Ampère se convierte en una identidad irresoluble para $B$, siendo obligatorio integrar $d\\vec{B}$ diferencialmente vía Biot-Savart.
      `,
      rubric: `
        • 5 pts: Distinguir validez universal de la Ley de Ampère vs. utilidad práctica para despejar B.<br>
        • 5 pts: Justificar explícitamente la necesidad de Biot-Savart en conductores finitos, arcos y falta de simetría traslacional/rotacional.
      `
    }
  ]
};
