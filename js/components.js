/**
 * FIS120 / FIS12125 · CERTAMEN 3
 * Componentes interactivos y renderizadores de ejercicios
 */

const StorageManager = {
  getCompletedModules() {
    try {
      return JSON.parse(localStorage.getItem('fis120_completed_modules') || '[]');
    } catch {
      return [];
    }
  },
  setModuleCompleted(modId, completed) {
    const list = this.getCompletedModules();
    const idx = list.indexOf(modId);
    if (completed && idx === -1) {
      list.push(modId);
    } else if (!completed && idx !== -1) {
      list.splice(idx, 1);
    }
    localStorage.setItem('fis120_completed_modules', JSON.stringify(list));
  },
  isModuleCompleted(modId) {
    return this.getCompletedModules().includes(modId);
  },
  getExerciseState(exId) {
    try {
      const all = JSON.parse(localStorage.getItem('fis120_exercise_state') || '{}');
      return all[exId] || null;
    } catch {
      return null;
    }
  },
  setExerciseState(exId, data) {
    try {
      const all = JSON.parse(localStorage.getItem('fis120_exercise_state') || '{}');
      all[exId] = data;
      localStorage.setItem('fis120_exercise_state', JSON.stringify(all));
    } catch (e) {
      console.error(e);
    }
  },
  getTotalStats() {
    try {
      const all = JSON.parse(localStorage.getItem('fis120_exercise_state') || '{}');
      let solved = 0;
      for (const k in all) {
        if (all[k]?.solved) solved++;
      }
      return { solved, completedModules: this.getCompletedModules().length };
    } catch {
      return { solved: 0, completedModules: 0 };
    }
  }
};

const UIComponents = {
  renderExercise(ex, index) {
    const state = StorageManager.getExerciseState(ex.id) || {};
    let badgeClass = 'badge-basic';
    let levelText = 'Básico';
    if (ex.level === 'intermediate') {
      badgeClass = 'badge-intermediate';
      levelText = 'Intermedio';
    } else if (ex.level === 'certamen') {
      badgeClass = 'badge-certamen';
      levelText = 'Nivel Certamen';
    }

    let innerContent = '';
    if (ex.type === 'multiple_choice') {
      innerContent = this.renderMultipleChoice(ex, state);
    } else if (ex.type === 'numerical') {
      innerContent = this.renderNumerical(ex, state);
    } else if (ex.type === 'true_false') {
      innerContent = this.renderTrueFalse(ex, state);
    } else if (ex.type === 'conceptual') {
      innerContent = this.renderConceptual(ex, state);
    } else if (ex.type === 'step_by_step') {
      innerContent = this.renderStepByStep(ex, state);
    }

    const figureHtml = ex.figure ? `
      <div class="figure-container" data-svg-src="${ex.figure}">
        <img class="svg-figure" src="${ex.figure}" alt="Figura ejercicio ${index + 1}">
        ${ex.figureCaption ? `<div class="figure-caption">${ex.figureCaption}</div>` : ''}
      </div>
    ` : '';

    return `
      <div class="exercise-card" id="card-${ex.id}">
        <div class="exercise-header">
          <div class="exercise-title">
            <span class="level-badge ${badgeClass}">${levelText}</span>
            <span>Ejercicio ${index + 1}: ${ex.title}</span>
          </div>
          ${ex.source ? `<span class="exercise-source">${ex.source}</span>` : ''}
        </div>
        <div class="exercise-statement">${ex.statement}</div>
        ${figureHtml}
        ${innerContent}
      </div>
    `;
  },

  renderMultipleChoice(ex, state) {
    const isSolved = state.solved || false;
    const selectedIdx = state.selectedOption;
    let optionsHtml = '';

    ex.options.forEach((opt, idx) => {
      let extraClass = '';
      if (isSolved) {
        if (idx === ex.correctOption) extraClass = 'correct';
        else if (idx === selectedIdx) extraClass = 'incorrect';
      } else if (selectedIdx === idx) {
        extraClass = 'selected';
      }

      optionsHtml += `
        <div class="option-item ${extraClass}" onclick="UIComponents.handleSelectOption('${ex.id}', ${idx}, ${ex.correctOption})">
          <input type="radio" name="opt-${ex.id}" ${selectedIdx === idx ? 'checked' : ''} ${isSolved ? 'disabled' : ''}>
          <span>${opt}</span>
        </div>
      `;
    });

    const feedbackVisible = isSolved ? 'visible' : '';
    const feedbackType = (selectedIdx === ex.correctOption) ? 'feedback-success' : 'feedback-error';

    return `
      <div class="options-list" id="opts-${ex.id}">
        ${optionsHtml}
      </div>
      <div class="feedback-box solution-box ${feedbackType} ${feedbackVisible}" id="feedback-${ex.id}" data-explanation="${encodeURIComponent(ex.explanation || '')}">
        ${isSolved ? `<strong>${selectedIdx === ex.correctOption ? '¡Correcto!' : 'Incorrecto.'}</strong> ${ex.explanation}` : ''}
      </div>
    `;
  },

  handleSelectOption(exId, chosenIdx, correctIdx) {
    const isCorrect = (chosenIdx === correctIdx);
    StorageManager.setExerciseState(exId, { solved: true, selectedOption: chosenIdx, isCorrect });
    
    const card = document.getElementById(`card-${exId}`);
    if (!card) return;
    const optItems = card.querySelectorAll('.option-item');
    optItems.forEach((item, idx) => {
      item.classList.remove('selected', 'correct', 'incorrect');
      if (idx === correctIdx) item.classList.add('correct');
      else if (idx === chosenIdx) item.classList.add('incorrect');
      const radio = item.querySelector('input');
      if (radio) radio.checked = (idx === chosenIdx);
    });

    const fb = document.getElementById(`feedback-${exId}`);
    if (fb) {
      fb.className = `feedback-box solution-box visible ${isCorrect ? 'feedback-success' : 'feedback-error'}`;
      fb.innerHTML = `<strong>${isCorrect ? '¡Correcto!' : 'Incorrecto.'}</strong> ${fb.getAttribute('data-explanation') || ''}`;
    }
    
    // Trigger global stats and KaTeX rendering
    if (window.App) {
      window.App.updateHeaderStats();
      window.App.renderMathInElement(card);
    }
  },

  renderNumerical(ex, state) {
    const isSolved = state.solved || false;
    const userVal = state.userValue !== undefined ? state.userValue : '';

    return `
      <div class="numerical-input-group">
        <label>Respuesta:</label>
        <input type="text" class="input-number" id="input-${ex.id}" value="${userVal}" placeholder="${ex.placeholder || 'Ej: 0.303'}" ${isSolved ? 'disabled' : ''}>
        <span>${ex.units || ''}</span>
        <button class="btn btn-primary btn-sm" onclick="UIComponents.handleCheckNumerical('${ex.id}', ${ex.correctValue}, ${ex.tolerance || 0.03})">Comprobar</button>
      </div>
      <div class="feedback-box solution-box ${isSolved ? (state.isCorrect ? 'feedback-success visible' : 'feedback-error visible') : ''}" id="feedback-${ex.id}" data-explanation="${encodeURIComponent(ex.explanation || '')}">
        ${isSolved ? `<strong>${state.isCorrect ? '¡Correcto!' : 'Revisa tus cálculos.'}</strong> Valor esperado: ${ex.correctValue} ${ex.units || ''}.<br>${ex.explanation}` : ''}
      </div>
    `;
  },

  handleCheckNumerical(exId, correctVal, tolerance) {
    const input = document.getElementById(`input-${exId}`);
    if (!input) return;
    const rawVal = input.value.replace(',', '.').trim();
    const val = parseFloat(rawVal);
    const fb = document.getElementById(`feedback-${exId}`);

    if (isNaN(val)) {
      if (fb) {
        fb.className = 'feedback-box feedback-error visible';
        fb.innerHTML = 'Por favor ingresa un número válido.';
      }
      return;
    }

    const relError = Math.abs(val - correctVal) / (Math.abs(correctVal) || 1);
    const isCorrect = relError <= tolerance;

    StorageManager.setExerciseState(exId, { solved: true, userValue: val, isCorrect });

    if (fb) {
      fb.className = `feedback-box solution-box visible ${isCorrect ? 'feedback-success' : 'feedback-error'}`;
      fb.innerHTML = `<strong>${isCorrect ? '¡Excelente!' : 'Cálculo inexacto.'}</strong> Valor objetivo: ${correctVal}. Error relativo: ${(relError*100).toFixed(1)}% (tolerancia: ${(tolerance*100).toFixed(0)}%).<br>${fb.getAttribute('data-explanation') || ''}`;
    }

    if (window.App) {
      window.App.updateHeaderStats();
      const card = document.getElementById(`card-${exId}`);
      if (card) window.App.renderMathInElement(card);
    }
  },

  renderTrueFalse(ex, state) {
    const isSolved = state.solved || false;
    const userChoice = state.userChoice;

    return `
      <div class="options-list">
        <div class="option-item ${isSolved && userChoice === true ? (ex.correct === true ? 'correct' : 'incorrect') : ''}" onclick="UIComponents.handleSelectTF('${ex.id}', true, ${ex.correct})">
          <input type="radio" name="tf-${ex.id}" ${userChoice === true ? 'checked' : ''} ${isSolved ? 'disabled' : ''}>
          <span><strong>Verdadero</strong></span>
        </div>
        <div class="option-item ${isSolved && userChoice === false ? (ex.correct === false ? 'correct' : 'incorrect') : ''}" onclick="UIComponents.handleSelectTF('${ex.id}', false, ${ex.correct})">
          <input type="radio" name="tf-${ex.id}" ${userChoice === false ? 'checked' : ''} ${isSolved ? 'disabled' : ''}>
          <span><strong>Falso</strong></span>
        </div>
      </div>
      <div class="feedback-box solution-box ${isSolved ? (state.isCorrect ? 'feedback-success visible' : 'feedback-error visible') : ''}" id="feedback-${ex.id}" data-justification="${encodeURIComponent(ex.justification || '')}">
        ${isSolved ? `<strong>${state.isCorrect ? '¡Correcto!' : 'Incorrecto.'}</strong> ${ex.justification}` : ''}
      </div>
    `;
  },

  handleSelectTF(exId, choice, correct) {
    const isCorrect = (choice === correct);
    StorageManager.setExerciseState(exId, { solved: true, userChoice: choice, isCorrect });
    
    const card = document.getElementById(`card-${exId}`);
    if (card) {
      const items = card.querySelectorAll('.option-item');
      items[0].className = `option-item ${choice === true ? (isCorrect ? 'correct' : 'incorrect') : (correct === true ? 'correct' : '')}`;
      items[1].className = `option-item ${choice === false ? (isCorrect ? 'correct' : 'incorrect') : (correct === false ? 'correct' : '')}`;
      items[0].querySelector('input').checked = (choice === true);
      items[1].querySelector('input').checked = (choice === false);
    }

    const fb = document.getElementById(`feedback-${exId}`);
    if (fb) {
      fb.className = `feedback-box solution-box visible ${isCorrect ? 'feedback-success' : 'feedback-error'}`;
      fb.innerHTML = `<strong>${isCorrect ? '¡Correcto!' : 'Incorrecto.'}</strong> ${fb.getAttribute('data-justification') || ''}`;
    }

    if (window.App) {
      window.App.updateHeaderStats();
      if (card) window.App.renderMathInElement(card);
    }
  },

  renderConceptual(ex, state) {
    const isRevealed = state.revealed || false;

    return `
      <p style="font-size: 0.95rem; color: var(--text-muted); font-style: italic;">
        Intenta responder y formular tus argumentos físicamente antes de revelar la pauta modelo.
      </p>
      <div style="margin: 0.8rem 0;">
        <button class="btn btn-sm" onclick="UIComponents.toggleRevealAnswer('${ex.id}')" id="btn-reveal-${ex.id}">
          ${isRevealed ? 'Ocultar Pauta Modelo' : 'Mostrar Pauta Modelo y Rúbrica'}
        </button>
      </div>
      <div class="step-box pauta-box model-solution ${isRevealed ? 'visible' : ''}" id="box-${ex.id}">
        <div class="step-box-title">Respuesta Modelo y Criterios Oficiales:</div>
        <div>${ex.modelAnswer}</div>
        ${ex.rubric ? `
          <div class="box-note" style="margin-top: 0.8rem;">
            <strong>Criterio de Corrección (10 Puntos):</strong><br>${ex.rubric}
          </div>
        ` : ''}
      </div>
    `;
  },

  toggleRevealAnswer(exId) {
    const box = document.getElementById(`box-${exId}`);
    const btn = document.getElementById(`btn-reveal-${exId}`);
    if (!box || !btn) return;
    const isVis = box.classList.toggle('visible');
    btn.textContent = isVis ? 'Ocultar Pauta Modelo' : 'Mostrar Pauta Modelo y Rúbrica';
    StorageManager.setExerciseState(exId, { solved: true, revealed: isVis });
    if (window.App) {
      window.App.updateHeaderStats();
      window.App.renderMathInElement(box);
    }
  },

  renderStepByStep(ex, state) {
    const currentStep = state.currentStep !== undefined ? state.currentStep : -1;
    let stepsHtml = '';

    ex.steps.forEach((step, idx) => {
      const isVisible = currentStep >= idx;
      const typeClass = (idx === 0) ? 'pista-box' : 'solution-step';
      stepsHtml += `
        <div class="step-box ${typeClass} ${isVisible ? 'visible' : ''}" id="step-${ex.id}-${idx}">
          <div class="step-box-title">${step.title}</div>
          <div>${step.content}</div>
        </div>
      `;
    });

    return `
      <div class="step-reveal-container">
        <div class="step-controls">
          <button class="btn btn-sm" onclick="UIComponents.showNextStep('${ex.id}', ${ex.steps.length})" id="btn-next-${ex.id}">
            ${currentStep === -1 ? 'Mostrar Pista / Paso 1' : (currentStep < ex.steps.length - 1 ? 'Mostrar Siguiente Paso' : 'Solución Completa Visible')}
          </button>
          <button class="btn btn-sm" onclick="UIComponents.showAllSteps('${ex.id}', ${ex.steps.length})">
            Revelar Todo
          </button>
        </div>
        <div style="margin-top: 0.8rem;">
          ${stepsHtml}
        </div>
      </div>
    `;
  },

  showNextStep(exId, totalSteps) {
    const state = StorageManager.getExerciseState(exId) || {};
    let step = state.currentStep !== undefined ? state.currentStep + 1 : 0;
    if (step >= totalSteps) step = totalSteps - 1;

    StorageManager.setExerciseState(exId, { solved: true, currentStep: step });

    for (let i = 0; i <= step; i++) {
      const box = document.getElementById(`step-${exId}-${i}`);
      if (box) box.classList.add('visible');
    }

    const btn = document.getElementById(`btn-next-${exId}`);
    if (btn) {
      btn.textContent = step < totalSteps - 1 ? 'Mostrar Siguiente Paso' : 'Solución Completa Visible';
    }

    if (window.App) {
      window.App.updateHeaderStats();
      const card = document.getElementById(`card-${exId}`);
      if (card) window.App.renderMathInElement(card);
    }
  },

  showAllSteps(exId, totalSteps) {
    StorageManager.setExerciseState(exId, { solved: true, currentStep: totalSteps - 1 });
    for (let i = 0; i < totalSteps; i++) {
      const box = document.getElementById(`step-${exId}-${i}`);
      if (box) box.classList.add('visible');
    }
    const btn = document.getElementById(`btn-next-${exId}`);
    if (btn) btn.textContent = 'Solución Completa Visible';

    if (window.App) {
      window.App.updateHeaderStats();
      const card = document.getElementById(`card-${exId}`);
      if (card) window.App.renderMathInElement(card);
    }
  }
};
