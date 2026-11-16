/**
 * FIS120 / FIS12125 · CERTAMEN 3
 * Controlador principal de la aplicación
 */

const App = {
  currentModuleId: 'mod0',
  modules: [
    { id: 'mod0', title: '0. Repaso Matemático y Conceptual', icon: '0' },
    { id: 'mod1', title: '1. Biot-Savart y Campo de Cables', icon: '1' },
    { id: 'mod2', title: '2. Densidad de Corriente J(r)', icon: '2' },
    { id: 'mod3', title: '3. Ley de Ampère y Simetrías', icon: '3' },
    { id: 'mod4', title: '4. Flujo Magnético y Faraday-Lenz', icon: '4' },
    { id: 'mod5', title: '5. fem de Movimiento y Rieles', icon: '5' },
    { id: 'mod6', title: '6. Inductancia Mutua y Transformadores', icon: '6' },
    { id: 'mod7', title: '7. Autoinductancia y Energía Magnética', icon: '7' },
    { id: 'mod8', title: '8. Circuitos Transientes RC y RL', icon: '8' },
    { id: 'mod9', title: '9. Circuitos Oscilantes LC y RLC', icon: '9' },
    { id: 'mod10', title: '10. Maxwell y Síntesis Conceptual', icon: '10' },
    { id: 'mod11', title: '11. SIMULACRO FINAL CERTAMEN 3', icon: '★' },
  ],

  init() {
    this.initTheme();
    this.renderSidebar();
    this.setupEventListeners();
    this.updateHeaderStats();

    // Render formulas in the formula drawer
    const drawer = document.getElementById('formula-drawer');
    if (drawer) this.renderMathInElement(drawer);

    // Check URL hash or default to mod0
    const hash = window.location.hash.replace('#', '');
    if (hash && this.modules.some(m => m.id === hash)) {
      this.loadModule(hash);
    } else {
      this.loadModule('mod0');
    }
  },

  initTheme() {
    const savedTheme = localStorage.getItem('fis120_theme');
    if (savedTheme) {
      document.documentElement.setAttribute('data-theme', savedTheme);
    } else {
      const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
      document.documentElement.setAttribute('data-theme', prefersDark ? 'dark' : 'light');
    }
    this.updateThemeButton();
  },

  toggleTheme() {
    const current = document.documentElement.getAttribute('data-theme');
    const target = current === 'dark' ? 'light' : 'dark';
    document.documentElement.setAttribute('data-theme', target);
    localStorage.setItem('fis120_theme', target);
    this.updateThemeButton();
    // Redraw any active interactive canvas
    window.dispatchEvent(new Event('resize'));
  },

  updateThemeButton() {
    const current = document.documentElement.getAttribute('data-theme');
    const btn = document.getElementById('theme-toggle-btn');
    if (btn) {
      btn.innerHTML = current === 'dark' ? '☀ Modo Claro' : '☾ Modo Oscuro';
    }
  },

  renderSidebar() {
    const list = document.getElementById('nav-module-list');
    if (!list) return;

    list.innerHTML = this.modules.map(m => {
      const isCompleted = StorageManager.isModuleCompleted(m.id);
      return `
        <li class="nav-module-item ${m.id === this.currentModuleId ? 'active' : ''}" 
            onclick="App.loadModule('${m.id}')" id="nav-item-${m.id}">
          <div>
            <span class="nav-module-num">${m.icon}.</span>
            <span>${m.title.split('. ')[1] || m.title}</span>
          </div>
          <span class="nav-module-status" id="nav-status-${m.id}">${isCompleted ? '✓' : ''}</span>
        </li>
      `;
    }).join('');
  },

  loadModule(modId) {
    this.currentModuleId = modId;
    window.location.hash = modId;
    window.scrollTo({ top: 0, behavior: 'smooth' });

    // Update active in sidebar
    document.querySelectorAll('.nav-module-item').forEach(el => el.classList.remove('active'));
    const activeNav = document.getElementById(`nav-item-${modId}`);
    if (activeNav) activeNav.classList.add('active');

    // Close mobile sidebar if open
    const sidebar = document.getElementById('app-sidebar');
    if (sidebar) sidebar.classList.remove('open');

    // Render module content
    const container = document.getElementById('main-content-area');
    if (!container) return;

    let dataObj = window[`MODULE_DATA_${modId.toUpperCase()}`];
    if (!dataObj) {
      try {
        dataObj = eval(`typeof MODULE_DATA_${modId.toUpperCase()} !== 'undefined' ? MODULE_DATA_${modId.toUpperCase()} : null`);
      } catch (e) {
        dataObj = null;
      }
    }

    if (!dataObj) {
      container.innerHTML = `
        <div class="theory-card">
          <h2>Módulo en preparación</h2>
          <p>El contenido de este módulo se está cargando o estará disponible a la brevedad.</p>
        </div>
      `;
      return;
    }

    const isCompleted = StorageManager.isModuleCompleted(modId);

    let html = `
      <div class="module-header">
        <div class="module-meta">FIS120 / FIS12125 · Certamen 3 · Módulo ${dataObj.number}</div>
        <h1>${dataObj.title}</h1>
        <p class="module-description">${dataObj.description}</p>
      </div>

      <section class="theory-card">
        <h3>1. Resumen Teórico y Ecuaciones Fundamentales</h3>
        <div>${dataObj.theory}</div>
      </section>
    `;

    // Interactive widget container if defined
    if (dataObj.hasInteractive) {
      html += `<div id="interactive-slot-${modId}"></div>`;
    }

    // Exercises section
    html += `
      <section class="exercises-section">
        <h2>2. Ejercicios Prácticos y Nivel Certamen</h2>
        <p style="font-size: 0.95rem; color: var(--text-muted); margin-bottom: 1.5rem;">
          Resuelve los ejercicios en orden progresivo. Tus respuestas e intentos se guardan automáticamente.
        </p>
        ${dataObj.exercises.map((ex, idx) => UIComponents.renderExercise(ex, idx)).join('')}
      </section>

      <div class="module-completion-footer">
        <div class="completion-info">
          <strong>¿Completaste el estudio de este módulo?</strong><br>
          <span style="font-size: 0.85rem; color: var(--text-muted);">
            Marca este módulo para registrar tu progreso hacia el Certamen 3.
          </span>
        </div>
        <button class="btn ${isCompleted ? 'btn-primary' : ''}" id="btn-complete-mod" onclick="App.toggleCompleteCurrentModule()">
          ${isCompleted ? '✓ Módulo Completado' : 'Marcar como Completado'}
        </button>
      </div>
    `;

    container.innerHTML = html;

    // Check debug parameter to reveal all solutions, hints and steps
    if (window.location.href.includes('reveal=all')) {
      this.revealAll(container);
    }

    // Render KaTeX math
    this.renderMathInElement(container);

    // Inline SVGs for seamless dark/light mode CSS styling
    this.inlineSVGs(container);

    // Initialize interactive widget if any
    if (dataObj.hasInteractive) {
      if (modId === 'mod3') {
        InteractiveSimulators.initAmpereProfile(`interactive-slot-${modId}`);
      } else if (modId === 'mod8') {
        InteractiveSimulators.initTransientPlot(`interactive-slot-${modId}`);
      } else if (modId === 'mod9') {
        InteractiveSimulators.initRLCRegimes(`interactive-slot-${modId}`);
      }
      this.renderMathInElement(document.getElementById(`interactive-slot-${modId}`));
    }
  },

  toggleCompleteCurrentModule() {
    const isCompleted = StorageManager.isModuleCompleted(this.currentModuleId);
    StorageManager.setModuleCompleted(this.currentModuleId, !isCompleted);

    const btn = document.getElementById('btn-complete-mod');
    if (btn) {
      if (!isCompleted) {
        btn.classList.add('btn-primary');
        btn.textContent = '✓ Módulo Completado';
      } else {
        btn.classList.remove('btn-primary');
        btn.textContent = 'Marcar como Completado';
      }
    }

    const navStatus = document.getElementById(`nav-status-${this.currentModuleId}`);
    if (navStatus) {
      navStatus.textContent = !isCompleted ? '✓' : '';
    }

    this.updateHeaderStats();
  },

  updateHeaderStats() {
    const stats = StorageManager.getTotalStats();
    const percent = Math.round((stats.completedModules / this.modules.length) * 100);

    const fill = document.getElementById('progress-bar-fill');
    if (fill) fill.style.width = `${percent}%`;

    const label = document.getElementById('stats-indicator');
    if (label) {
      label.textContent = `${stats.solved} ejercicios resueltos · ${stats.completedModules}/${this.modules.length} módulos`;
    }
  },

  revealAll(container) {
    if (!container) container = document.getElementById('main-content-area');
    if (!container) return;

    // 1. Revelar todos los pasos ocultos
    container.querySelectorAll('.step-box').forEach(el => el.classList.add('visible'));

    // 2. Revelar retroalimentacion y explicaciones de alternativas / numericos
    container.querySelectorAll('.feedback-box').forEach(fb => {
      fb.classList.add('visible');
      const raw = fb.getAttribute('data-explanation') || fb.getAttribute('data-justification') || '';
      if (raw && !fb.innerHTML.trim()) {
        try {
          fb.innerHTML = `<strong>Solución / Explicación:</strong> ${decodeURIComponent(raw)}`;
        } catch (e) {
          fb.innerHTML = `<strong>Solución / Explicación:</strong> ${raw}`;
        }
      }
    });

    // 3. Revelar todas las ramas de convenciones alternativas
    container.querySelectorAll('.conv-plano-view, .conv-normal-view').forEach(el => {
      el.style.display = 'block';
    });

    // 4. Actualizar botones de revelar
    container.querySelectorAll('.step-controls button').forEach(btn => {
      btn.textContent = 'Solución Completa Visible';
    });

    // 5. Renderizar fórmulas matemáticas en todos los elementos recién revelados
    this.renderMathInElement(container);
  },

  renderMathInElement(el) {
    if (!el) return;
    const renderFn = window.renderMathInElement || (typeof renderMathInElement === 'function' ? renderMathInElement : null);
    if (!renderFn) {
      setTimeout(() => this.renderMathInElement(el), 200);
      return;
    }
    try {
      renderFn(el, {
        delimiters: [
          { left: '$$', right: '$$', display: true },
          { left: '$', right: '$', display: false },
          { left: '\\[', right: '\\]', display: true },
          { left: '\\(', right: '\\)', display: false }
        ],
        throwOnError: false
      });

      // Renderizar fórmulas con sintaxis o llaves malformadas que auto-render omitió
      if (window.katex) {
        const walker = document.createTreeWalker(el, NodeFilter.SHOW_TEXT);
        const nodesToFix = [];
        while (walker.nextNode()) {
          const node = walker.currentNode;
          if (node.parentElement && node.parentElement.closest('.katex, .katex-error, script, style, svg, math')) continue;
          if (/\$\$[\s\S]+?\$\$/.test(node.nodeValue) || /\$[^$]+?\$/.test(node.nodeValue)) {
            nodesToFix.push(node);
          }
        }
        nodesToFix.forEach(node => {
          const parent = node.parentElement;
          if (!parent) return;
          let html = node.nodeValue.replace(/\$\$([\s\S]+?)\$\$/g, (match, tex) => {
            try {
              return window.katex.renderToString(tex, { throwOnError: false, displayMode: true });
            } catch (err) {
              return `<span class="katex-error" title="${err.message}">${tex}</span>`;
            }
          });
          html = html.replace(/\$([^$]+?)\$/g, (match, tex) => {
            try {
              return window.katex.renderToString(tex, { throwOnError: false, displayMode: false });
            } catch (err) {
              return `<span class="katex-error" title="${err.message}">${tex}</span>`;
            }
          });
          const span = document.createElement('span');
          span.innerHTML = html;
          parent.replaceChild(span, node);
        });
      }
    } catch (e) {
      console.warn('KaTeX rendering error:', e);
    }
  },

  inlineSVGs(container) {
    if (!container) return Promise.resolve();
    const figureBoxes = container.querySelectorAll('.figure-container[data-svg-src], .figure-container');
    const promises = Array.from(figureBoxes).map(box => {
      const img = box.querySelector('img');
      const src = box.getAttribute('data-svg-src') || (img ? img.getAttribute('src') : null);
      if (!src || !src.endsWith('.svg')) return Promise.resolve();

      return fetch(src)
        .then(res => {
          if (!res.ok) throw new Error(`HTTP error ${res.status}`);
          return res.text();
        })
        .then(svgText => {
          const parser = new DOMParser();
          const doc = parser.parseFromString(svgText, 'image/svg+xml');
          const svgEl = doc.querySelector('svg');
          if (svgEl) {
            svgEl.classList.add('inlined-svg');
            svgEl.setAttribute('role', 'img');
            const currentImg = box.querySelector('img');
            if (currentImg) {
              currentImg.replaceWith(svgEl);
            }
            box.setAttribute('data-svg-inlined', 'true');
          }
        })
        .catch(err => {
          console.warn('SVG inlining error:', src, err);
        });
    });
    return Promise.all(promises);
  },

  setupEventListeners() {
    const themeBtn = document.getElementById('theme-toggle-btn');
    if (themeBtn) themeBtn.addEventListener('click', () => this.toggleTheme());

    const formulaBtn = document.getElementById('formula-toggle-btn');
    const drawer = document.getElementById('formula-drawer');
    const overlay = document.getElementById('drawer-overlay');
    const closeBtn = document.getElementById('drawer-close-btn');

    function toggleFormula() {
      drawer.classList.toggle('open');
      overlay.classList.toggle('open');
    }

    if (formulaBtn) formulaBtn.addEventListener('click', toggleFormula);
    if (overlay) overlay.addEventListener('click', toggleFormula);
    if (closeBtn) closeBtn.addEventListener('click', toggleFormula);

    const sidebarToggle = document.getElementById('sidebar-toggle-btn');
    const sidebar = document.getElementById('app-sidebar');
    if (sidebarToggle && sidebar) {
      sidebarToggle.addEventListener('click', () => {
        sidebar.classList.toggle('open');
      });
    }

    // Hash change router support
    window.addEventListener('hashchange', () => {
      const hash = window.location.hash.replace('#', '');
      if (hash && hash !== this.currentModuleId && this.modules.some(m => m.id === hash)) {
        this.loadModule(hash);
      }
    });
  }
};

window.switchAlphaConv = function(conv) {
  const isNormal = conv === 'normal';
  document.querySelectorAll('.conv-normal-view').forEach(el => el.style.display = isNormal ? 'block' : 'none');
  document.querySelectorAll('.conv-plano-view').forEach(el => el.style.display = isNormal ? 'none' : 'block');
  const btnN = document.getElementById('btn-conv-normal');
  const btnP = document.getElementById('btn-conv-plano');
  if (btnN && btnP) {
    if (isNormal) {
      btnN.className = 'btn btn-sm btn-primary';
      btnP.className = 'btn btn-sm';
    } else {
      btnN.className = 'btn btn-sm';
      btnP.className = 'btn btn-sm btn-primary';
    }
  }
};

window.App = App;
document.addEventListener('DOMContentLoaded', () => App.init());
