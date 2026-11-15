/**
 * FIS120 / FIS12125 · CERTAMEN 3
 * Simuladores y Widgets Interactivos con Canvas HTML5 puro
 */

const InteractiveSimulators = {
  // 1. Perfil B(r) para cable con corriente
  initAmpereProfile(containerId) {
    const container = document.getElementById(containerId);
    if (!container) return;

    container.innerHTML = `
      <div class="interactive-widget">
        <div class="widget-title">Simulador Interactivo: Perfil de Campo Magnético $B(r)$</div>
        <p style="font-size: 0.9rem; color: var(--text-muted);">
          Explora cómo la distribución de corriente $J(r)$ altera el perfil radial del campo magnético $B(r)$ en el interior ($r < R$) y cómo todos convergen a $\\frac{\\mu_0 I}{2\\pi r}$ en el exterior ($r > R$).
        </p>
        <div class="widget-controls">
          <div class="widget-control-item">
            <label><strong>Distribución $J(r)$:</strong></label>
            <select id="ampere-dist-select" class="input-number" style="max-width: 220px; font-size: 0.85rem;">
              <option value="uniform">Uniforme: $J = J_0$</option>
              <option value="parabolic">Parabólica: $2J_0(1 - r^2/R^2)$</option>
              <option value="linear">Lineal: $\\beta r$</option>
              <option value="stepped">Escalonada: $J_0 / 3J_0$ (Efecto pelicular)</option>
            </select>
          </div>
          <div class="widget-control-item">
            <label>Radio $r$: <span id="ampere-r-val" style="font-family: var(--font-mono); font-weight: bold;">0.60</span> R</label>
            <input type="range" id="ampere-r-slider" min="0" max="2" step="0.02" value="0.6" style="width: 140px;">
          </div>
        </div>
        <canvas id="ampere-canvas" class="widget-canvas"></canvas>
        <div id="ampere-readout" style="font-size: 0.9rem; margin-top: 0.5rem; font-family: var(--font-mono); color: var(--accent);"></div>
      </div>
    `;

    const canvas = document.getElementById('ampere-canvas');
    const select = document.getElementById('ampere-dist-select');
    const slider = document.getElementById('ampere-r-slider');
    const rVal = document.getElementById('ampere-r-val');
    const readout = document.getElementById('ampere-readout');

    function draw() {
      if (!canvas) return;
      const ctx = canvas.getContext('2d');
      const w = canvas.width = canvas.offsetWidth;
      const h = canvas.height = canvas.offsetHeight;
      const dist = select.value;
      const rRatio = parseFloat(slider.value);
      rVal.textContent = rRatio.toFixed(2);

      const isDark = document.documentElement.getAttribute('data-theme') === 'dark';
      ctx.fillStyle = isDark ? '#1e293b' : '#f8f9fa';
      ctx.fillRect(0, 0, w, h);

      const padX = 60;
      const padY = 30;
      const graphW = w - padX - 30;
      const graphH = h - padY - 30;

      // Draw axes
      ctx.strokeStyle = isDark ? '#475569' : '#cbd5e1';
      ctx.lineWidth = 1.5;
      ctx.beginPath();
      ctx.moveTo(padX, padY);
      ctx.lineTo(padX, padY + graphH);
      ctx.lineTo(padX + graphW, padY + graphH);
      ctx.stroke();

      // Axis labels
      ctx.fillStyle = isDark ? '#94a3b8' : '#64748b';
      ctx.font = '12px serif';
      ctx.fillText('B(r)', padX - 35, padY + 15);
      ctx.fillText('r / R', padX + graphW - 25, padY + graphH + 20);

      // Vertical line at r = R (boundary)
      const xR = padX + (graphW / 2.0); // let r/R = 1 be at middle
      ctx.setLineDash([4, 4]);
      ctx.strokeStyle = isDark ? '#64748b' : '#94a3b8';
      ctx.beginPath();
      ctx.moveTo(xR, padY);
      ctx.lineTo(xR, padY + graphH);
      ctx.stroke();
      ctx.setLineDash([]);
      ctx.fillText('r = R', xR - 12, padY + graphH + 18);

      // Curve calculation
      function getB(r) {
        if (dist === 'uniform') {
          return r <= 1.0 ? r : 1.0 / r;
        } else if (dist === 'parabolic') {
          // B(r) = 2*r - r^3 for r <= 1, and 1/r for r > 1
          return r <= 1.0 ? (2*r - Math.pow(r, 3)) : 1.0 / r;
        } else if (dist === 'linear') {
          // J = beta r -> I_enc ~ r^3 -> B(r) ~ r^2
          return r <= 1.0 ? Math.pow(r, 2) : 1.0 / r;
        } else if (dist === 'stepped') {
          // Pauta C3 P1: J0 for r <= 0.5, 3J0 for 0.5 < r <= 1
          // I_tot = 10 * pi * J0 * R^2 / 4 = 2.5 * pi * J0 * R^2
          // For r <= 0.5: B ~ 0.4 * r
          // For 0.5 < r <= 1: B ~ (0.4/r) * [0.25 + 3*(r^2 - 0.25)] / 2.5
          if (r <= 0.5) return (r / 0.5) * 0.2;
          if (r <= 1.0) {
            const iEnc = 0.25 + 3 * (r*r - 0.25);
            return (iEnc / 2.5) / r;
          }
          return 1.0 / r;
        }
        return 0;
      }

      // Plot curve
      ctx.strokeStyle = '#2563eb';
      ctx.lineWidth = 2.5;
      ctx.beginPath();
      const maxB = 1.3;
      let curB = 0;

      for (let px = 0; px <= graphW; px++) {
        const r = (px / (graphW / 2.0));
        const b = getB(r);
        const plotX = padX + px;
        const plotY = (padY + graphH) - (b / maxB) * (graphH - 10);
        if (px === 0) ctx.moveTo(plotX, plotY);
        else ctx.lineTo(plotX, plotY);
      }
      ctx.stroke();

      // Current point on curve
      curB = getB(rRatio);
      const curPlotX = padX + (rRatio * (graphW / 2.0));
      const curPlotY = (padY + graphH) - (curB / maxB) * (graphH - 10);

      ctx.fillStyle = '#dc2626';
      ctx.beginPath();
      ctx.arc(curPlotX, curPlotY, 5, 0, Math.PI * 2);
      ctx.fill();

      // Draw dotted projection
      ctx.strokeStyle = '#dc2626';
      ctx.setLineDash([3, 3]);
      ctx.beginPath();
      ctx.moveTo(curPlotX, padY + graphH);
      ctx.lineTo(curPlotX, curPlotY);
      ctx.lineTo(padX, curPlotY);
      ctx.stroke();
      ctx.setLineDash([]);

      readout.textContent = `En r = ${rRatio.toFixed(2)} R → B(r) = ${(curB).toFixed(3)} · (μ₀ I / 2πR). ${rRatio > 1.0 ? 'Zona exterior (dependencia estándar 1/r)' : 'Zona interior (moldeada por J(r))'}`;
    }

    select.addEventListener('change', draw);
    slider.addEventListener('input', draw);
    window.addEventListener('resize', draw);
    setTimeout(draw, 100);
  },

  // 2. Gráfico transitorio RC / RL
  initTransientPlot(containerId) {
    const container = document.getElementById(containerId);
    if (!container) return;

    container.innerHTML = `
      <div class="interactive-widget">
        <div class="widget-title">Simulador Interactivo: Transientes en Circuitos RC y RL</div>
        <p style="font-size: 0.9rem; color: var(--text-muted);">
          Visualiza la evolución temporal de la corriente $i(t)$ y voltaje en procesos de carga y descarga según las soluciones analíticas del formulario oficial.
        </p>
        <div class="widget-controls">
          <div class="widget-control-item">
            <label><strong>Circuito:</strong></label>
            <select id="transient-type" class="input-number" style="max-width: 200px; font-size: 0.85rem;">
              <option value="rc_charge">Carga RC: $q(t) = Q_{\\max}(1 - e^{-t/RC})$</option>
              <option value="rc_discharge">Descarga RC: $q(t) = Q_0 e^{-t/RC}$</option>
              <option value="rl_growth">Conexión RL: $i(t) = I_{\\max}(1 - e^{-(R/L)t})$</option>
              <option value="rl_decay">Desconexión RL: $i(t) = I_0 e^{-(R/L)t}$</option>
            </select>
          </div>
          <div class="widget-control-item">
            <label>Constante $\\tau$: <span id="transient-tau-val" style="font-family: var(--font-mono); font-weight: bold;">1.85</span> ms</label>
            <input type="range" id="transient-tau-slider" min="0.5" max="5.0" step="0.1" value="1.85" style="width: 120px;">
          </div>
        </div>
        <canvas id="transient-canvas" class="widget-canvas"></canvas>
        <div id="transient-readout" style="font-size: 0.9rem; margin-top: 0.5rem; font-family: var(--font-mono); color: var(--accent);"></div>
      </div>
    `;

    const canvas = document.getElementById('transient-canvas');
    const select = document.getElementById('transient-type');
    const slider = document.getElementById('transient-tau-slider');
    const tauVal = document.getElementById('transient-tau-val');
    const readout = document.getElementById('transient-readout');

    function draw() {
      if (!canvas) return;
      const ctx = canvas.getContext('2d');
      const w = canvas.width = canvas.offsetWidth;
      const h = canvas.height = canvas.offsetHeight;
      const mode = select.value;
      const tau = parseFloat(slider.value);
      tauVal.textContent = tau.toFixed(2);

      const isDark = document.documentElement.getAttribute('data-theme') === 'dark';
      ctx.fillStyle = isDark ? '#1e293b' : '#f8f9fa';
      ctx.fillRect(0, 0, w, h);

      const padX = 55;
      const padY = 25;
      const graphW = w - padX - 30;
      const graphH = h - padY - 30;

      // Draw axes
      ctx.strokeStyle = isDark ? '#475569' : '#cbd5e1';
      ctx.lineWidth = 1.5;
      ctx.beginPath();
      ctx.moveTo(padX, padY);
      ctx.lineTo(padX, padY + graphH);
      ctx.lineTo(padX + graphW, padY + graphH);
      ctx.stroke();

      ctx.fillStyle = isDark ? '#94a3b8' : '#64748b';
      ctx.font = '12px serif';
      ctx.fillText(mode.startsWith('rc') ? 'q(t) / Q₀' : 'i(t) / I₀', padX - 45, padY + 15);
      ctx.fillText('t [ms]', padX + graphW - 30, padY + graphH + 20);

      // Plot curve up to 5 tau
      const tMax = 5 * 2.0; // 10 ms scale
      ctx.strokeStyle = '#16a34a';
      ctx.lineWidth = 2.5;
      ctx.beginPath();

      function getY(t) {
        if (mode === 'rc_charge' || mode === 'rl_growth') {
          return 1.0 - Math.exp(-t / tau);
        } else {
          return Math.exp(-t / tau);
        }
      }

      for (let px = 0; px <= graphW; px++) {
        const t = (px / graphW) * tMax;
        const val = getY(t);
        const plotX = padX + px;
        const plotY = (padY + graphH) - val * (graphH - 15);
        if (px === 0) ctx.moveTo(plotX, plotY);
        else ctx.lineTo(plotX, plotY);
      }
      ctx.stroke();

      // Tau marker (t = tau)
      const tauPx = (tau / tMax) * graphW;
      if (tauPx <= graphW) {
        const tauYVal = getY(tau);
        const plotTauX = padX + tauPx;
        const plotTauY = (padY + graphH) - tauYVal * (graphH - 15);

        ctx.setLineDash([4, 4]);
        ctx.strokeStyle = '#dc2626';
        ctx.beginPath();
        ctx.moveTo(plotTauX, padY + graphH);
        ctx.lineTo(plotTauX, plotTauY);
        ctx.stroke();
        ctx.setLineDash([]);

        ctx.fillStyle = '#dc2626';
        ctx.beginPath();
        ctx.arc(plotTauX, plotTauY, 4.5, 0, Math.PI * 2);
        ctx.fill();
        ctx.fillText(`t = τ (${(tauYVal * 100).toFixed(1)}%)`, plotTauX - 25, plotTauY - 10);
      }

      readout.textContent = `Constante de tiempo: τ = ${tau.toFixed(2)} ms. En t = 1τ: ${(getY(tau)*100).toFixed(1)}% del valor final. En t = 5τ: ${(getY(5*tau)*100).toFixed(1)}% (régimen estacionario).`;
    }

    select.addEventListener('change', draw);
    slider.addEventListener('input', draw);
    window.addEventListener('resize', draw);
    setTimeout(draw, 100);
  },

  // 3. Gráfico RLC: Regímenes de Amortiguamiento
  initRLCRegimes(containerId) {
    const container = document.getElementById(containerId);
    if (!container) return;

    container.innerHTML = `
      <div class="interactive-widget">
        <div class="widget-title">Simulador Interactivo: Regímenes del Circuito RLC Serie</div>
        <p style="font-size: 0.9rem; color: var(--text-muted);">
          Compara en tiempo real los 3 regímenes del certamen según la relación entre $\\alpha = \\frac{R}{2L}$ y $\\omega_0 = \\frac{1}{\\sqrt{LC}}$.
        </p>
        <div class="widget-controls">
          <div class="widget-control-item">
            <label><strong>Régimen:</strong></label>
            <select id="rlc-regime-select" class="input-number" style="max-width: 250px; font-size: 0.85rem;">
              <option value="underdamped">Subamortiguado (α < ω₀): Oscilaciones amortiguadas</option>
              <option value="critical">Críticamente amortiguado (α = ω₀): Sin oscilación, retorno más veloz</option>
              <option value="overdamped">Sobreamortiguado (α > ω₀): Decaimiento lento sin oscilación</option>
            </select>
          </div>
          <div class="widget-control-item">
            <label>Amortiguamiento $\\alpha / \\omega_0$: <span id="rlc-alpha-val" style="font-family: var(--font-mono); font-weight: bold;">0.25</span></label>
            <input type="range" id="rlc-alpha-slider" min="0.05" max="2.5" step="0.05" value="0.25" style="width: 130px;">
          </div>
        </div>
        <canvas id="rlc-canvas" class="widget-canvas"></canvas>
        <div id="rlc-readout" style="font-size: 0.9rem; margin-top: 0.5rem; font-family: var(--font-mono); color: var(--accent);"></div>
      </div>
    `;

    const canvas = document.getElementById('rlc-canvas');
    const select = document.getElementById('rlc-regime-select');
    const slider = document.getElementById('rlc-alpha-slider');
    const alphaVal = document.getElementById('rlc-alpha-val');
    const readout = document.getElementById('rlc-readout');

    function draw() {
      if (!canvas) return;
      const ctx = canvas.getContext('2d');
      const w = canvas.width = canvas.offsetWidth;
      const h = canvas.height = canvas.offsetHeight;
      const ratio = parseFloat(slider.value);
      alphaVal.textContent = ratio.toFixed(2);

      const isDark = document.documentElement.getAttribute('data-theme') === 'dark';
      ctx.fillStyle = isDark ? '#1e293b' : '#f8f9fa';
      ctx.fillRect(0, 0, w, h);

      const padX = 55;
      const padY = 25;
      const graphW = w - padX - 30;
      const graphH = h - padY - 30;
      const zeroY = padY + graphH * 0.55;

      // Draw zero axis and time axis
      ctx.strokeStyle = isDark ? '#475569' : '#cbd5e1';
      ctx.lineWidth = 1.5;
      ctx.beginPath();
      ctx.moveTo(padX, padY);
      ctx.lineTo(padX, padY + graphH);
      ctx.moveTo(padX, zeroY);
      ctx.lineTo(padX + graphW, zeroY);
      ctx.stroke();

      ctx.fillStyle = isDark ? '#94a3b8' : '#64748b';
      ctx.font = '12px serif';
      ctx.fillText('q(t) / Q₀', padX - 45, padY + 15);
      ctx.fillText('t [s]', padX + graphW - 20, zeroY + 18);

      const omega0 = 4.0; // reference angular frequency
      const alpha = ratio * omega0;

      ctx.strokeStyle = ratio < 0.98 ? '#2563eb' : (ratio <= 1.05 ? '#16a34a' : '#d97706');
      ctx.lineWidth = 2.5;
      ctx.beginPath();

      const tMax = 6.0;

      function getQ(t) {
        if (ratio < 0.98) {
          // Underdamped formula from official formula sheet:
          // q(t) = Q0 * (omega0 / omega') * exp(-alpha*t) * cos(omega'*t - arctan(alpha/omega'))
          const omegaP = Math.sqrt(omega0*omega0 - alpha*alpha);
          const phi = Math.atan(alpha / omegaP);
          return (omega0 / omegaP) * Math.exp(-alpha * t) * Math.cos(omegaP * t - phi);
        } else if (Math.abs(ratio - 1.0) <= 0.05) {
          // Critically damped: q(t) = Q0 * (1 + alpha*t) * exp(-alpha*t)
          return (1.0 + alpha * t) * Math.exp(-alpha * t);
        } else {
          // Overdamped: sum of two decaying exponentials
          const gamma = Math.sqrt(alpha*alpha - omega0*omega0);
          const r1 = -alpha + gamma;
          const r2 = -alpha - gamma;
          // Initial condition q(0)=1, i(0)=0 -> c1 + c2 = 1, c1*r1 + c2*r2 = 0
          const c1 = -r2 / (r1 - r2);
          const c2 = 1.0 - c1;
          return c1 * Math.exp(r1 * t) + c2 * Math.exp(r2 * t);
        }
      }

      for (let px = 0; px <= graphW; px++) {
        const t = (px / graphW) * tMax;
        const qVal = getQ(t);
        const plotX = padX + px;
        const plotY = zeroY - qVal * (graphH * 0.42);
        if (px === 0) ctx.moveTo(plotX, plotY);
        else ctx.lineTo(plotX, plotY);
      }
      ctx.stroke();

      let regimeLabel = '';
      if (ratio < 0.98) {
        regimeLabel = 'SUBAMORTIGUADO (α < ω₀): la carga oscila con frecuencia ω\' = √(ω₀² - α²) y envolvente exponencial exp(-αt).';
        select.value = 'underdamped';
      } else if (Math.abs(ratio - 1.0) <= 0.05) {
        regimeLabel = 'CRÍTICAMENTE AMORTIGUADO (α = ω₀): no hay oscilación; es el retorno más veloz a cero sin cruzar el eje.';
        select.value = 'critical';
      } else {
        regimeLabel = 'SOBREAMORTIGUADO (α > ω₀): gran resistencia R frena el flujo; decaimiento asintótico sin oscilación.';
        select.value = 'overdamped';
      }

      readout.textContent = `Régimen: ${regimeLabel}`;
    }

    select.addEventListener('change', () => {
      if (select.value === 'underdamped') slider.value = 0.25;
      else if (select.value === 'critical') slider.value = 1.0;
      else if (select.value === 'overdamped') slider.value = 1.8;
      draw();
    });
    slider.addEventListener('input', draw);
    window.addEventListener('resize', draw);
    setTimeout(draw, 100);
  }
};
