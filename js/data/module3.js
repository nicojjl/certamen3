/**
 * MÓDULO 3: LEY DE AMPÈRE Y SIMETRÍAS
 * FIS120 / FIS12125 · UTFSM
 */

window.MODULE_DATA_MOD3 = {
  number: '3',
  title: 'Ley de Ampère y Simetrías',
  description: 'Elección rigurosa de lazos amperianos, cálculo del campo en cables coaxiales de múltiples capas, distribuciones volumétricas no homogéneas, solenoides, toroides y superposición vectorial fuera del eje.',
  hasInteractive: true,
  theory: `
    <p>
      La Ley de Ampère relaciona la circulación del campo magnético a lo largo de una curva cerrada imaginaria (lazo amperiano $\\Gamma$) con la corriente neta total que atraviesa cualquier superficie abierta $S$ delimitada por $\\Gamma$.
    </p>

    <div class="box-formula">
      <strong>1. Ley de Ampère Integral (Formulario C3):</strong>
      $$\\Lambda_B = \\oint_\\Gamma \\vec{B} \\cdot d\\vec{l} = \\mu_0 I_{enl} = \\mu_0 \\iint_S \\vec{J} \\cdot d\\vec{A}$$
      <p>
        Para que esta ecuación permita despejar explícitamente $|\\vec{B}|$, se requiere que en el lazo amperiano escogido:
        <br>1. El campo $\\vec{B}$ sea <strong>tangente</strong> a la trayectoria en todo punto (o perpendicular a tramos auxiliares): $\\vec{B}\\cdot d\\vec{l} = B\\,dl$.
        <br>2. La magnitud $B = |\\vec{B}|$ sea <strong>constante</strong> sobre los tramos tangentes.
        <br>Bajo estas condiciones: $\\oint B\\,dl = B \\oint dl = B (2\\pi r) = \\mu_0 I_{enl} \\implies B(r) = \\frac{\\mu_0 I_{enl}(r)}{2\\pi r}$.
      </p>
    </div>

    <div class="figure-container">
      <img src="img/mod3_toroid_simulacro.svg" alt="Toroide rectangular del simulacro">
      <div class="figure-caption">Toroide ideal de sección rectangular (Simulacro C3 P1): vista superior y corte transversal en el plano $rz$.</div>
    </div>

    <div class="box-method">
      <strong>2. Configuraciones Clásicas de Certamen:</strong>
      <p>
        <strong>A. Cable Coaxial Multicapa:</strong>
        <br>• <em>Interior ($r < R_1$):</em> $I_{enl}(r) = \\iint_{0}^r J_1 dA \\implies B(r) = \\frac{\\mu_0 I_{enl}(r)}{2\\pi r}$.
        <br>• <em>Entre conductores ($R_1 < r < R_2$):</em> Encierra toda la corriente interior $I_1 \\implies B(r) = \\frac{\\mu_0 I_1}{2\\pi r}$.
        <br>• <em>Capa exterior ($R_2 < r < R_3$):</em> $I_{enl}(r) = I_1 + \\iint_{R_2}^r J_2 dA$.
        <br>• <em>Exterior total ($r > R_3$):</em> $I_{enl} = I_1 + I_2$. Si $I_2 = -I_1$ (corrientes balanceadas), $I_{enl} = 0 \\implies \\vec{B} = \\vec{0}$ (apantallamiento magnético coaxial).
        <br><br>
        <strong>B. Solenoide Ideal (radio $a$, $n$ vueltas por metro):</strong>
        Lazo rectangular con un lado de longitud $L$ dentro del solenoide y el opuesto afuera donde $B \\approx 0$:
        $$\\oint \\vec{B}\\cdot d\\vec{l} = B L = \\mu_0 (n L I) \\implies B = \\mu_0 n I \\quad (\\text{interior, uniforme})$$
        <br>
        <strong>C. Toroide Ideal ($N$ espiras, radios $a < r < b$):</strong>
        Lazo circular concéntrico de radio $r$:
        $$B(r) = \\begin{cases} 0, & r < a \\\\ \\frac{\\mu_0 N I}{2\\pi r}, & a < r < b \\\\ 0, & r > b \\end{cases}$$
      </p>
    </div>

    <div class="box-warning">
      <strong>Condición de Continuidad en Fronteras:</strong><br>
      En ausencia de corrientes superficiales infinitamente delgadas, el campo magnético $B(r)$ debe ser una función <strong>estrictamente continua</strong> al cruzar cualquier radio frontera ($r = R_1, R_2, R_3$). Evaluar los límites laterales por izquierda y derecha es la mejor forma de verificar en certamen que no te equivocaste en las constantes de integración.
    </div>
  `,
  exercises: [
    {
      id: 'm3_ex1',
      title: 'Campo en el Interior de un Solenoide',
      level: 'basic',
      source: 'Formulario C3',
      type: 'multiple_choice',
      statement: `
        Un solenoide ideal muy largo tiene $n = 800\\text{ vueltas/m}$ y transporta una corriente constante de $I = 2.5\\text{ A}$. ¿Cuál es la magnitud del campo magnético uniforme en su interior?
      `,
      options: [
        '$2.51 \\times 10^{-3}\\text{ T}$',
        '$1.26 \\times 10^{-3}\\text{ T}$',
        '$5.03 \\times 10^{-3}\\text{ T}$',
        '$6.28 \\times 10^{-4}\\text{ T}$'
      ],
      correctOption: 0,
      explanation: `
        Aplicamos la fórmula del solenoide ideal:
        $$B = \\mu_0 n I = (4\\pi \\times 10^{-7}\\text{ H/m}) \\cdot (800\\text{ m}^{-1}) \\cdot (2.5\\text{ A}) = 2.513 \\times 10^{-3}\\text{ T} \\approx 2.51\\text{ mT}$$
      `
    },
    {
      id: 'm3_ex2',
      title: 'Campo en el Interior de Conductor Homogéneo',
      level: 'basic',
      source: 'Ley de Ampère Estándar',
      type: 'numerical',
      statement: `
        Un cable conductor cilíndrico macizo de radio $R = 4.0\\text{ cm} = 0.040\\text{ m}$ transporta una corriente total uniforme de $I = 16.0\\text{ A}$. Calcule la magnitud del campo magnético $B$ a una distancia $r = 2.0\\text{ cm} = 0.020\\text{ m}$ de su eje (en $r = R/2$).
      `,
      placeholder: 'Ej: 4.0e-5',
      units: 'T',
      correctValue: 0.00004,
      tolerance: 0.04,
      explanation: `
        Para un conductor homogéneo en $r \\le R$:
        $$I_{enl}(r) = I \\frac{\\pi r^2}{\\pi R^2} = I \\frac{r^2}{R^2}$$
        Por la Ley de Ampère:
        $$B(r) 2\\pi r = \\mu_0 I \\frac{r^2}{R^2} \\implies B(r) = \\frac{\\mu_0 I r}{2\\pi R^2}$$
        Evaluando en $r = R/2$:
        $$B(R/2) = \\frac{\\mu_0 I}{4\\pi R} = \\frac{(4\\pi \\times 10^{-7}) \\cdot 16.0}{4\\pi \\cdot 0.040} = \\frac{16.0 \\times 10^{-7}}{0.040} = 4.0 \\times 10^{-5}\\text{ T} = 40\\,\\mu\\text{T}$$
      `
    },
    {
      id: 'm3_ex3',
      title: 'Apantallamiento en Cable Coaxial',
      level: 'intermediate',
      source: 'Principios de Coaxial',
      type: 'true_false',
      statement: `
        En un cable coaxial donde el conductor interior transporta una corriente $+I$ y el conductor exterior transporta una corriente de retorno $-I$, el campo magnético en cualquier punto exterior al cable ($r > R_{ext}$) es exactamente nulo.
      `,
      correct: true,
      justification: `
        Verdadero. Al trazar un lazo amperiano circular concéntrico de radio $r > R_{ext}$, la corriente total enlazada es la suma algebraica de ambas corrientes:
        $$I_{enl} = (+I) + (-I) = 0$$
        Por la simetría cilíndrica del sistema, $\\oint \\vec{B}\\cdot d\\vec{l} = B(r) 2\\pi r = \\mu_0 I_{enl} = 0 \\implies B(r) = 0$. Esta es precisamente la razón técnica por la cual los cables coaxiales blindan las señales frente a radiación electromagnética externa.
      `
    },
    {
      id: 'm3_ex4',
      title: 'Campo en Cable Coaxial Asimétrico',
      level: 'intermediate',
      source: 'Ayudantía 9 Problema 1b,c',
      type: 'multiple_choice',
      statement: `
        Un cable coaxial tiene un conductor interior de radio $R$ con densidad $\\vec{J}_1 = J_0\\hat{k}$ y un conductor exterior entre radios $2R$ y $4R$ con $\\vec{J}_2 = 2J_0(-\\hat{k})$. ¿Cuál es la magnitud del campo magnético en el espacio aislante intermedio $r = 1.5R = \\frac{3R}{2}$?
      `,
      options: [
        '$\\frac{\\mu_0 J_0 R}{3}$',
        '$\\frac{\\mu_0 J_0 R}{2}$',
        '$\\frac{2\\mu_0 J_0 R}{3}$',
        '$\\frac{\\mu_0 J_0 R}{6}$'
      ],
      correctOption: 0,
      explanation: `
        Para $R < r < 2R$, el lazo amperiano solo encierra al conductor interior completo:
        $$I_{enl} = J_0 (\\pi R^2) = \\pi J_0 R^2$$
        Por la Ley de Ampère:
        $$B(r) 2\\pi r = \\mu_0 (\\pi J_0 R^2) \\implies B(r) = \\frac{\\mu_0 J_0 R^2}{2r}$$
        Evaluando en $r = \\frac{3R}{2}$:
        $$B\\left(\\frac{3R}{2}\\right) = \\frac{\\mu_0 J_0 R^2}{2 \\cdot (3R/2)} = \\frac{\\mu_0 J_0 R}{3}$$
      `
    },
    {
      id: 'm3_ex5',
      title: 'Cilindro con Densidad Parabólica J(r) = 2J₀(1 - r²/a²)',
      level: 'certamen',
      source: 'Ayudantía 9 Problema 2b,c',
      type: 'step_by_step',
      statement: `
        Considere un cable cilíndrico muy largo alineado con el eje $z$ de radio $a$, que conduce una densidad de corriente variable dada por:
        $$\\vec{J}(r) = 2J_0\\left(1 - \\frac{r^2}{a^2}\\right)\\hat{k}$$
        Determine el vector campo magnético $\\vec{B}(r)$ en todo el espacio: para $r < a$ y para $r > a$.
      `,
      steps: [
        {
          title: 'Paso 1: Elección de lazo amperiano y justificación de simetría',
          content: `
            La distribución tiene simetría cilíndrica infinita y traslacional a lo largo de $z$. Por la regla de la mano derecha con corriente en $+\\hat{k}$, las líneas de campo son circunferencias concéntricas orientadas en $+\\hat{\\theta}$.<br>
            Escogemos un lazo amperiano circular de radio $r$ centrado en el eje $z$, orientado con $d\\vec{l} = r\\,d\\theta\\,\\hat{\\theta}$:
            $$\\oint_\\Gamma \\vec{B}\\cdot d\\vec{l} = \\int_0^{2\\pi} B(r)\\, r\\,d\\theta = B(r) 2\\pi r$$
          `
        },
        {
          title: 'Paso 2: Corriente enlazada y campo en el interior (r < a)',
          content: `
            Para un radio $r < a$, la corriente encerrada es:
            $$I_{enl}(r) = \\int_0^r 2J_0\\left(1 - \\frac{r'^2}{a^2}\\right) 2\\pi r' dr' = 4\\pi J_0 \\left[\\frac{r'^2}{2} - \\frac{r'^4}{4a^2}\\right]_0^r = 4\\pi J_0 r^2 \\left(\\frac{1}{2} - \\frac{r^2}{4a^2}\\right) = 2\\pi J_0 r^2 \\left(1 - \\frac{r^2}{2a^2}\\right)$$
            Aplicando la Ley de Ampère:
            $$B(r) 2\\pi r = \\mu_0 \\cdot 2\\pi J_0 r^2 \\left(1 - \\frac{r^2}{2a^2}\\right)$$
            Despejando y añadiendo el versor de dirección:
            $$\\vec{B}(r) = \\mu_0 J_0 r \\left(1 - \\frac{r^2}{2a^2}\\right) \\hat{\\theta}, \\quad \\text{para } r < a$$
          `
        },
        {
          title: 'Paso 3: Campo en el exterior (r > a) y continuidad',
          content: `
            Para $r > a$, el lazo encierra la corriente total $I_T = \\pi J_0 a^2$ (calculada en el Módulo 2):
            $$B(r) 2\\pi r = \\mu_0 (\\pi J_0 a^2) \\implies \\vec{B}(r) = \\frac{\\mu_0 J_0 a^2}{2r}\\hat{\\theta}, \\quad \\text{para } r > a$$
            <strong>Chequeo de continuidad en $r = a$:</strong>
            $$B(a^-) = \\mu_0 J_0 a \\left(1 - \\frac{a^2}{2a^2}\\right) = \\frac{\\mu_0 J_0 a}{2}$$
            $$B(a^+) = \\frac{\\mu_0 J_0 a^2}{2a} = \\frac{\\mu_0 J_0 a}{2}$$
            ¡Los límites laterales coinciden perfectamente!
          `
        }
      ]
    },
    {
      id: 'm3_ex6',
      title: 'Cable Coaxial Escalonado: Campo en las Tres Regiones',
      level: 'certamen',
      source: 'Pauta Certamen 3 2026-1 Problema 1b,c',
      type: 'step_by_step',
      figure: 'img/mod2_coaxial_stepped.svg',
      figureCaption: 'Sección del cable: Región 1 ($r \\le R/2$), Región 2 ($R/2 < r \\le R$) y Región 3 ($r > R$).',
      statement: `
        Con la densidad escalonada de la Pauta Oficial C3: $J(r) = J_0$ para $0 \\le r \\le R/2$ y $J(r) = 3J_0$ para $R/2 < r \\le R$:<br>
        a) Obtenga el vector campo magnético $\\vec{B}(r)$ en las tres regiones.<br>
        b) En $r = 3R/4$, compare el campo $\\vec{B}_{esc}$ con el campo $\\vec{B}_{unif}$ producido por una densidad uniforme con la misma corriente total $I$.
      `,
      steps: [
        {
          title: 'Paso 1: Campo en Región 1 (r <= R/2) y Región 2 (R/2 < r <= R)',
          content: `
            • <strong>Región 1 ($r \\le R/2$):</strong>
            $$I_{enc} = J_0 \\pi r^2 \\implies B(r) 2\\pi r = \\mu_0 J_0 \\pi r^2 \\implies \\vec{B}(r) = \\frac{\\mu_0 J_0 r}{2}\\,\\hat{\\theta}$$
            • <strong>Región 2 ($R/2 < r \\le R$):</strong>
            La corriente incluye el núcleo interior completo más la corona exterior hasta radio $r$:
            $$I_{enc} = J_0 \\pi \\left(\\frac{R}{2}\\right)^2 + 3J_0 \\pi \\left(r^2 - \\frac{R^2}{4}\\right) = \\pi J_0 \\left(\\frac{R^2}{4} + 3r^2 - \\frac{3R^2}{4}\\right) = \\pi J_0 \\left(3r^2 - \\frac{R^2}{2}\\right)$$
            Por Ampère:
            $$B(r) 2\\pi r = \\mu_0 \\pi J_0 \\left(3r^2 - \\frac{R^2}{2}\\right) \\implies \\vec{B}(r) = \\frac{\\mu_0 J_0}{2r} \\left(3r^2 - \\frac{R^2}{2}\\right)\\,\\hat{\\theta}$$
          `
        },
        {
          title: 'Paso 2: Campo en Región 3 (r > R)',
          content: `
            Para $r > R$, el lazo encierra la corriente total $I = \\frac{5\\pi J_0 R^2}{2}$:
            $$\\vec{B}(r) = \\frac{\\mu_0 I}{2\\pi r}\\,\\hat{\\theta} = \\frac{5\\mu_0 J_0 R^2}{4r}\\,\\hat{\\theta}$$
          `
        },
        {
          title: 'Paso 3: Comparación en r = 3R/4 con la densidad uniforme equivalente',
          content: `
            La densidad uniforme equivalente es $J' = \\frac{I}{\\pi R^2} = \\frac{5 J_0}{2}$.<br>
            El campo uniforme en $r = 3R/4$ es:
            $$B_{unif} = \\frac{\\mu_0 J' r}{2} = \\frac{\\mu_0 (5J_0/2) (3R/4)}{2} = \\frac{15}{16} \\mu_0 J_0 R \\approx 0.938\\,\\mu_0 J_0 R$$
            Evaluando el campo escalonado en $r = 3R/4$:
            $$B_{esc} = \\frac{\\mu_0 J_0}{2(3R/4)} \\left(3\\left(\\frac{3R}{4}\\right)^2 - \\frac{R^2}{2}\\right) = \\frac{2\\mu_0 J_0}{3R} \\left(3\\cdot\\frac{9R^2}{16} - \\frac{8R^2}{16}\\right) = \\frac{2\\mu_0 J_0}{3R} \\left(\\frac{19R^2}{16}\\right) = \\frac{19}{24}\\mu_0 J_0 R \\approx 0.792\\,\\mu_0 J_0 R$$
            <strong>Conclusión de la Pauta Oficial:</strong> Como $0.792 < 0.938$:
            $$B_{esc} < B_{unif}$$
            <strong>Razón física:</strong> Al concentrarse la corriente hacia la corteza externa en la distribución escalonada, a un radio intermedio $r=3R/4$ se ha encerrado <em>menos corriente</em> que si la corriente estuviera uniformemente distribuida por toda la sección.
          `
        }
      ]
    },
    {
      id: 'm3_ex7',
      title: 'Toroide Ideal de Sección Rectangular',
      level: 'certamen',
      source: 'Simulacro Certamen 3 Problema 1a',
      type: 'step_by_step',
      figure: 'img/mod3_toroid_simulacro.svg',
      figureCaption: 'Toroide de radio interno $a$, radio externo $b$ y altura $h$ con $N$ vueltas.',
      statement: `
        Un toroide ideal de sección rectangular, con radio interior $a$, radio exterior $b$ y altura $h$, está formado por $N$ vueltas de alambre por las que circula una corriente $I$. Utilizando la ley de Ampère, determine el vector campo magnético $\\vec{B}$ en todo el espacio ($r < a$, $a < r < b$ y $r > b$). Justifique la elección del lazo amperiano.
      `,
      steps: [
        {
          title: 'Paso 1: Justificación de simetría y lazo amperiano',
          content: `
            El toroide presenta simetría de revolución axial en torno al eje $z$. Las líneas de campo magnético están confinadas en círculos azimutales en la dirección $\\hat{\\phi}$ (o $\\hat{\\theta}$).<br>
            Elegimos un lazo amperiano circular $\\Gamma$ de radio $r$ concéntrico con el eje del toroide y situado en un plano perpendicular al eje $z$.<br>
            A lo largo de este lazo, $\\vec{B} \\cdot d\\vec{l} = B(r) dl$, de modo que:
            $$\\oint_\\Gamma \\vec{B} \\cdot d\\vec{l} = B(r) \\oint dl = B(r) 2\\pi r$$
          `
        },
        {
          title: 'Paso 2: Evaluación de la corriente enlazada en las tres regiones',
          content: `
            • <strong>Región 1 ($r < a$):</strong> El círculo de radio $r$ pasa por el hueco central interior. Ningún cable de las espiras atraviesa el disco definido por $\\Gamma$.
            $$I_{enl} = 0 \\implies \\vec{B} = \\vec{0}$$
            • <strong>Región 2 ($a < r < b$):</strong> El lazo circular pasa por el interior del toroide. Atraviesan la superficie del lazo todas las $N$ vueltas de la cara interna que llevan corriente $I$:
            $$I_{enl} = N I \\implies B(r) 2\\pi r = \\mu_0 N I \\implies \\vec{B}(r) = \\frac{\\mu_0 N I}{2\\pi r}\\,\\hat{\\phi}$$
            • <strong>Región 3 ($r > b$):</strong> El lazo abarca el toroide completo. Cada una de las $N$ espiras atraviesa la superficie dos veces en sentidos contrarios (hacia arriba por el interior y hacia abajo por el exterior):
            $$I_{enl} = N I - N I = 0 \\implies \\vec{B} = \\vec{0}$$
          `
        },
        {
          title: 'Paso 3: Síntesis final de campo en todo el espacio',
          content: `
            $$\\vec{B}(r, \\phi, z) = \\begin{cases} \\vec{0}, & r < a \\\\ \\frac{\\mu_0 N I}{2\\pi r}\\,\\hat{\\phi}, & a < r < b \\\\ \\vec{0}, & r > b \\end{cases}$$
            El campo magnético queda estrictamente confinado al interior del volumen del toroide.
          `
        }
      ]
    },
    {
      id: 'm3_ex8',
      title: 'Superposición Fuera de Eje: Cilindro Macizo y Cable Recto',
      level: 'certamen',
      source: 'Ayudantía 9 Problema 3',
      type: 'step_by_step',
      statement: `
        Un cilindro conductor macizo infinito de radio $R$ transporta $\\vec{J}(r) = \\beta r\\hat{k}$ con $\\beta > 0$. Su eje atraviesa el plano $xy$ en $\\vec{r}_1 = -a\\,\\hat{\\imath}$ (con $a > R$). Además, un cable conductor infinito transporta corriente $I$ y atraviesa el plano $xy$ en $\\vec{r}_2 = a(\\hat{\\imath} - \\hat{\\jmath})$.<br>
        a) Determine el vector campo $\\vec{B}$ en el origen $O$ debido al cilindro.<br>
        b) Determine el vector campo $\\vec{B}$ en el origen $O$ debido al cable.<br>
        c) ¿Qué valor debe tener $\\beta$ para que el campo resultante en el origen solo tenga componente sobre el eje $x$?
      `,
      steps: [
        {
          title: 'Paso 1: Campo del cilindro en el origen O',
          content: `
            El eje del cilindro está en $(-a, 0, 0)$. El origen $O=(0,0,0)$ está a una distancia radial $r = a > R$, por lo que se encuentra en la <em>zona exterior</em> del cilindro.<br>
            La corriente total del cilindro es (del Módulo 2): $I_{cil} = \\frac{2\\pi \\beta R^3}{3}$ en dirección $+\\hat{k}$.<br>
            Como estamos fuera del cilindro, por el teorema de Ampère su campo exterior es idéntico al de un cable equivalente situado en su eje.<br>
            El vector relativo desde el eje del cilindro hacia el origen es $+a\\,\\hat{\\imath}$.<br>
            Por regla de la mano derecha con corriente $+\\hat{k}$:
            $$\\hat{k} \\times \\hat{\\imath} = +\\hat{\\jmath}$$
            $$\\vec{B}_{cil}(O) = \\frac{\\mu_0 I_{cil}}{2\\pi a}\\,\\hat{\\jmath} = \\frac{\\mu_0 \\left(\\frac{2\\pi \\beta R^3}{3}\\right)}{2\\pi a}\\,\\hat{\\jmath} = \\frac{\\mu_0 \\beta R^3}{3a}\\,\\hat{\\jmath}$$
          `
        },
        {
          title: 'Paso 2: Campo del cable en el origen O',
          content: `
            El cable está ubicado en $\\vec{r}_2 = a\\,\\hat{\\imath} - a\\,\\hat{\\jmath}$.<br>
            El vector desde el cable hacia el origen $O$ es:
            $$\\vec{r}' = \\vec{0} - \\vec{r}_2 = -a\\,\\hat{\\imath} + a\\,\\hat{\\jmath}$$
            Su distancia al origen es $d = \\sqrt{(-a)^2 + a^2} = a\\sqrt{2}$.<br>
            El versor que apunta hacia el origen es $\\hat{r}' = \\frac{-\\hat{\\imath} + \\hat{\\jmath}}{\\sqrt{2}}$.<br>
            Suponiendo que el cable lleva corriente hacia $+\\hat{k}$:
            $$\\vec{B}_{cable}(O) = \\frac{\\mu_0 I}{2\\pi d} (\\hat{k} \\times \\hat{r}') = \\frac{\\mu_0 I}{2\\pi a\\sqrt{2}} \\left( \\hat{k} \\times \\frac{-\\hat{\\imath} + \\hat{\\jmath}}{\\sqrt{2}} \\right)$$
            Calculamos el producto cruz: $\\hat{k} \\times (-\\hat{\\imath}) = -\\hat{\\jmath}$, y $\\hat{k} \\times \\hat{\\jmath} = -\\hat{\\imath}$.<br>
            $$\\vec{B}_{cable}(O) = \\frac{\\mu_0 I}{4\\pi a} (-\\hat{\\imath} - \\hat{\\jmath})$$
          `
        },
        {
          title: 'Paso 3: Campo resultante y condición para anular componente y',
          content: `
            Sumamos las componentes en el eje $y$:
            $$B_{y, neto} = \\left( \\frac{\\mu_0 \\beta R^3}{3a} - \\frac{\\mu_0 I}{4\\pi a} \\right) = 0$$
            Igualando a cero para que solo exista componente sobre el eje $x$:
            $$\\frac{\\mu_0 \\beta R^3}{3a} = \\frac{\\mu_0 I}{4\\pi a}$$
            Cancelando $\\mu_0 / a$ y despejando $\\beta$:
            $$\\beta = \\frac{3I}{4\\pi R^3}$$
            Con este valor de $\\beta$, las componentes en $y$ se cancelan exactamente y el campo resultante queda $\\vec{B}_{neto}(O) = -\\frac{\\mu_0 I}{4\\pi a}\\,\\hat{\\imath}$.
          `
        }
      ]
    },
    {
      id: 'm3_ex9',
      title: 'Condiciones de Aplicabilidad de la Ley de Ampère',
      level: 'certamen',
      source: 'Ayudantía 9 Problema Conceptual 1',
      type: 'conceptual',
      statement: `
        ¿Bajo qué condiciones se puede utilizar la ley de Ampère para determinar el campo magnético? ¿Significa que si no se cumplen estas condiciones la ley es falsa?
      `,
      modelAnswer: `
        La Ley de Ampère $\\oint \\vec{B}\\cdot d\\vec{l} = \\mu_0 I_{enl}$ es una ley fundamental de la física y <strong>es siempre verdadera</strong> para corrientes estacionarias en magnetostática.<br><br>
        Sin embargo, <strong>para poder despejar el campo magnético $\\vec{B}$ analíticamente</strong> a partir de ella, se requiere que el sistema posea un <strong>alto grado de simetría geométrica</strong>, de tal modo que se pueda construir un lazo amperiano cerrado $\\Gamma$ donde:
        <br>1. La magnitud $|\\vec{B}|$ sea <strong>estrictamente uniforme y constante</strong> en todo el lazo (o en segmentos determinados del mismo).
        <br>2. La dirección de $\\vec{B}$ sea en cada punto <strong>paralela o perpendicular</strong> al diferencial de línea $d\\vec{l}$.
        <br><br>
        Las únicas simetrías que permiten esto son:
        <br>• <strong>Simetría cilíndrica infinita:</strong> cables rectos infinitos, cilindros macizos o cables coaxiales (lazos circulares concéntricos).
        <br>• <strong>Simetría planar infinita:</strong> láminas infinitas de corriente (lazos rectangulares).
        <br>• <strong>Solenoides y toroides ideales:</strong> donde el campo es uniforme en su interior y nulo fuera.
        <br><br>
        Si la configuración no presenta estas simetrías (por ejemplo, cables finitos, arcos, espiras circulares evaluadas en puntos arbitrarios), la integral sigue valiendo $\\mu_0 I_{enl}$, pero no es posible sacar $B$ fuera de la integral, haciendo imposible su despeje. En esos casos es obligatorio recurrir a la Ley de Biot-Savart.
      `,
      rubric: `
        • 5 pts: Explicar la diferencia entre validez física (siempre cierta) y utilidad de cálculo.<br>
        • 5 pts: Enumerar las simetrías canónicas (cilíndrica infinita, planar, solenoide/toroide) y las condiciones sobre B en el lazo.
      `
    }
  ]
};
