// app.js - Interactive application logic for Sistemas Bancarios y Teoría Monetaria

let currentTab = 'tab-economistas';

document.addEventListener('DOMContentLoaded', () => {
  initApp();
});

function initApp() {
  if (!window.BANKING_DATA) {
    console.error('Data not loaded');
    return;
  }

  // Render views
  initFilterTab();
  renderEconomistsList();
  renderTextsList();
  renderDeepDive();
  initExamTab();
  initExamKeysTab();
  initSpeechEngine();

  // Typeset math if MathJax is available
  if (window.MathJax && window.MathJax.typesetPromise) {
    window.MathJax.typesetPromise();
  }
}

// ----------------------------------------------------
// TABS NAVIGATION
// ----------------------------------------------------
function switchTab(tabId) {
  currentTab = tabId;

  // Hide all tab contents
  document.querySelectorAll('.tab-content').forEach(el => el.classList.add('hidden'));

  // Show target tab
  const target = document.getElementById(tabId);
  if (target) target.classList.remove('hidden');

  // Update navigation button active states
  document.querySelectorAll('.nav-btn').forEach(btn => {
    btn.classList.remove('active', 'bg-indigo-800', 'text-amber-300', 'shadow');
    if (!btn.id.includes('render')) {
      btn.classList.add('text-indigo-100');
    }
  });

  const activeBtn = document.getElementById(`nav-${tabId}`);
  if (activeBtn && !tabId.includes('render')) {
    activeBtn.classList.add('active', 'bg-indigo-800', 'text-amber-300', 'shadow');
    activeBtn.classList.remove('text-indigo-100');
  }

  // Re-render math formulas if needed
  if (window.MathJax && window.MathJax.typesetPromise) {
    window.MathJax.typesetPromise();
  }

  window.scrollTo({ top: 0, behavior: 'smooth' });
}

// ----------------------------------------------------
// TAB 1: COMPARATIVE MATRIX RENDERING
// ----------------------------------------------------
function populateMatrixFilters() {
  const topicSelect = document.getElementById('matrixFilterTopic');
  const econSelect = document.getElementById('matrixFilterEconomist');

  if (topicSelect) {
    window.BANKING_DATA.topics.forEach(t => {
      const opt = document.createElement('option');
      opt.value = t.id;
      opt.textContent = t.name;
      topicSelect.appendChild(opt);
    });
  }

  if (econSelect) {
    window.BANKING_DATA.economists.forEach(e => {
      const opt = document.createElement('option');
      opt.value = e.id;
      opt.textContent = e.name;
      econSelect.appendChild(opt);
    });
  }
}

function toggleMatrixView() {
  isMatrixInverted = !isMatrixInverted;
  const btn = document.getElementById('btnToggleAxis');
  if (btn) {
    btn.innerHTML = isMatrixInverted 
      ? '<i class="fa-solid fa-repeat"></i> Vista Normal (Economistas en filas)' 
      : '<i class="fa-solid fa-repeat"></i> Invertir Ejes (Temas en filas)';
  }
  renderMatrix();
}

function renderMatrix() {
  const table = document.getElementById('comparativeTable');
  if (!table) return;

  const filterTopic = document.getElementById('matrixFilterTopic')?.value || 'all';
  const filterEcon = document.getElementById('matrixFilterEconomist')?.value || 'all';

  let visibleTopics = window.BANKING_DATA.topics;
  let visibleEcons = window.BANKING_DATA.economists;

  if (filterTopic !== 'all') {
    visibleTopics = visibleTopics.filter(t => t.id === filterTopic);
  }
  if (filterEcon !== 'all') {
    visibleEcons = visibleEcons.filter(e => e.id === filterEcon);
  }

  table.innerHTML = '';

  if (!isMatrixInverted) {
    // Normal: Rows = Economists, Columns = Topics
    let thead = '<thead><tr>';
    thead += '<th class="w-48 text-left bg-indigo-950 text-amber-300">Economista / Escuela</th>';
    visibleTopics.forEach(t => {
      thead += `<th class="text-left">${t.name}</th>`;
    });
    thead += '</tr></thead>';

    let tbody = '<tbody>';
    visibleEcons.forEach(e => {
      tbody += `<tr>`;
      tbody += `<th>
        <div class="font-bold text-indigo-950 text-xs">${e.name}</div>
        <div class="text-[10px] text-indigo-600 font-semibold">${e.school}</div>
        <div class="text-[10px] text-slate-500 font-medium">${e.epoch}</div>
      </th>`;

      visibleTopics.forEach(t => {
        const stance = e.stances[t.id] || '[No aborda este tema puntualmente en los textos analizados]';
        const isExcluded = stance.includes('[No aborda este tema');
        const cellClass = isExcluded ? 'cell-empty' : 'cell-active';

        const displaySnippet = stance.length > 140 ? stance.substring(0, 140) + '...' : stance;

        tbody += `<td class="matrix-cell ${cellClass}" onclick="openModal('${e.id}', '${t.id}')">
          <div class="line-clamp-4 leading-snug">${displaySnippet}</div>
          <div class="mt-1.5 flex items-center justify-between text-[10px] text-indigo-600 font-semibold">
            <span>${isExcluded ? '<span class="text-slate-400 font-normal">Sin mención</span>' : 'Ver detalle'}</span>
            <i class="fa-solid fa-arrow-up-right-from-square text-[9px]"></i>
          </div>
        </td>`;
      });
      tbody += `</tr>`;
    });
    tbody += '</tbody>';

    table.innerHTML = thead + tbody;
  } else {
    // Inverted: Rows = Topics, Columns = Economists
    let thead = '<thead><tr>';
    thead += '<th class="w-56 text-left bg-indigo-950 text-amber-300">Eje Temático</th>';
    visibleEcons.forEach(e => {
      thead += `<th class="text-left">
        <div>${e.name}</div>
        <div class="text-[9px] font-normal text-indigo-200">${e.epoch}</div>
      </th>`;
    });
    thead += '</tr></thead>';

    let tbody = '<tbody>';
    visibleTopics.forEach(t => {
      tbody += `<tr>`;
      tbody += `<th>
        <div class="font-bold text-indigo-950 text-xs">${t.name}</div>
        <div class="text-[10px] text-slate-500 font-normal mt-0.5">${t.description}</div>
      </th>`;

      visibleEcons.forEach(e => {
        const stance = e.stances[t.id] || '[No aborda este tema puntualmente en los textos analizados]';
        const isExcluded = stance.includes('[No aborda este tema');
        const cellClass = isExcluded ? 'cell-empty' : 'cell-active';
        const displaySnippet = stance.length > 140 ? stance.substring(0, 140) + '...' : stance;

        tbody += `<td class="matrix-cell ${cellClass}" onclick="openModal('${e.id}', '${t.id}')">
          <div class="line-clamp-4 leading-snug">${displaySnippet}</div>
          <div class="mt-1.5 flex items-center justify-between text-[10px] text-indigo-600 font-semibold">
            <span>${isExcluded ? '<span class="text-slate-400 font-normal">Sin mención</span>' : 'Ver detalle'}</span>
            <i class="fa-solid fa-arrow-up-right-from-square text-[9px]"></i>
          </div>
        </td>`;
      });
      tbody += `</tr>`;
    });
    tbody += '</tbody>';

    table.innerHTML = thead + tbody;
  }

  if (window.MathJax && window.MathJax.typesetPromise) {
    window.MathJax.typesetPromise();
  }
}

// ----------------------------------------------------
// TAB NUEVA: FILTRAR POR ECONOMISTA O POR TEMA
// ----------------------------------------------------
let currentFilterMode = 'economist';
let selectedFilterEconId = 'friedman';
let selectedFilterTopicId = 't3_inflacion';

function initFilterTab() {
  renderEconomistChips();
  renderSelectedEconomistDetail();
  renderTopicChips();
  renderSelectedTopicDetail();
}

function setFilterMode(mode) {
  currentFilterMode = mode;
  const btnEcon = document.getElementById('btnFilterModeEcon');
  const btnTopic = document.getElementById('btnFilterModeTopic');
  const secEcon = document.getElementById('filterSectionEconomist');
  const secTopic = document.getElementById('filterSectionTopic');

  if (!btnEcon || !btnTopic || !secEcon || !secTopic) return;

  if (mode === 'economist') {
    btnEcon.className = "px-4 py-2 rounded-lg text-xs font-bold transition-all bg-indigo-900 text-amber-300 shadow flex items-center gap-1.5";
    btnTopic.className = "px-4 py-2 rounded-lg text-xs font-bold transition-all text-slate-700 hover:text-slate-900 flex items-center gap-1.5";
    secEcon.classList.remove('hidden');
    secTopic.classList.add('hidden');
  } else {
    btnTopic.className = "px-4 py-2 rounded-lg text-xs font-bold transition-all bg-indigo-900 text-amber-300 shadow flex items-center gap-1.5";
    btnEcon.className = "px-4 py-2 rounded-lg text-xs font-bold transition-all text-slate-700 hover:text-slate-900 flex items-center gap-1.5";
    secTopic.classList.remove('hidden');
    secEcon.classList.add('hidden');
  }

  if (window.MathJax && window.MathJax.typesetPromise) {
    window.MathJax.typesetPromise();
  }
}

function renderEconomistChips() {
  const container = document.getElementById('econChipsContainer');
  if (!container) return;
  container.innerHTML = '';

  window.BANKING_DATA.economists.forEach(e => {
    const isSelected = e.id === selectedFilterEconId;
    const btn = document.createElement('button');
    btn.type = 'button';
    btn.className = isSelected 
      ? 'px-3 py-1.5 rounded-lg text-xs font-bold bg-indigo-900 text-amber-300 shadow border border-indigo-950 flex items-center gap-1.5 transition transform scale-105'
      : 'px-3 py-1.5 rounded-lg text-xs font-medium bg-white text-slate-700 hover:bg-indigo-50 hover:text-indigo-900 border border-slate-300 flex items-center gap-1.5 transition';
    
    btn.innerHTML = `<i class="fa-solid fa-user-tie text-[10px] ${isSelected ? 'text-amber-400' : 'text-slate-400'}"></i> ${e.name}`;
    btn.onclick = () => selectFilterEconomist(e.id);
    container.appendChild(btn);
  });
}

function selectFilterEconomist(econId) {
  selectedFilterEconId = econId;
  renderEconomistChips();
  renderSelectedEconomistDetail();
}

function renderSelectedEconomistDetail() {
  const container = document.getElementById('selectedEconResult');
  if (!container) return;

  const econ = window.BANKING_DATA.economists.find(e => e.id === selectedFilterEconId);
  if (!econ) return;

  const addressed = [];
  const unaddressed = [];

  window.BANKING_DATA.topics.forEach(t => {
    const stance = econ.stances[t.id] || '[No aborda este tema puntualmente en los textos analizados]';
    if (stance.includes('[No aborda este tema')) {
      unaddressed.push({ topic: t, stance });
    } else {
      addressed.push({ topic: t, stance });
    }
  });

  let primaryTags = '';
  econ.primary_texts.forEach(pt => {
    primaryTags += `<span class="bg-indigo-100 text-indigo-900 font-semibold px-2.5 py-1 rounded text-[11px]">${pt}</span>`;
  });

  let addressedCards = '';
  addressed.forEach(item => {
    addressedCards += `
      <div class="bg-white rounded-xl border border-indigo-100 p-5 shadow-sm hover:shadow-md transition">
        <div class="flex items-center justify-between mb-2">
          <div class="flex items-center gap-2">
            <span class="w-6 h-6 rounded-full bg-emerald-100 text-emerald-800 font-bold text-xs flex items-center justify-center flex-shrink-0">
              <i class="fa-solid fa-check text-[10px]"></i>
            </span>
            <h5 class="text-sm font-bold text-indigo-950">${item.topic.name}</h5>
          </div>
          <span class="text-[10px] bg-emerald-50 text-emerald-700 font-bold px-2 py-0.5 rounded-full border border-emerald-200">
            Aborda este tema
          </span>
        </div>
        <p class="text-xs text-slate-500 mb-3">${item.topic.description}</p>
        <div class="bg-slate-50 p-3.5 rounded-lg border border-slate-200 text-xs text-slate-800 leading-relaxed font-sans">
          ${item.stance}
        </div>
      </div>
    `;
  });

  let unaddressedCards = '';
  if (unaddressed.length > 0) {
    unaddressedCards = '<div class="grid grid-cols-1 sm:grid-cols-2 gap-3 mt-3">';
    unaddressed.forEach(item => {
      unaddressedCards += `
        <div class="bg-slate-100 border border-slate-200 rounded-lg p-3 text-xs text-slate-600 flex items-start gap-2.5">
          <i class="fa-solid fa-ban text-slate-400 mt-0.5"></i>
          <div>
            <div class="font-bold text-slate-700">${item.topic.name}</div>
            <div class="text-[11px] text-slate-500 mt-0.5">${item.stance}</div>
          </div>
        </div>
      `;
    });
    unaddressedCards += '</div>';
  } else {
    unaddressedCards = '<div class="text-xs text-slate-500 italic p-3 bg-slate-50 rounded border border-slate-200">Este autor aborda todos los temas analizados.</div>';
  }

  container.innerHTML = `
    <!-- Economist Header Banner -->
    <div class="bg-gradient-to-r from-indigo-900 via-indigo-950 to-slate-900 text-white rounded-2xl p-6 shadow-md mb-6">
      <div class="flex flex-col md:flex-row md:items-center justify-between gap-4">
        <div>
          <div class="flex flex-wrap items-center gap-2 mb-2">
            <h4 class="text-2xl font-black text-amber-300">${econ.name}</h4>
            <span class="bg-indigo-700 text-indigo-100 text-xs font-bold px-3 py-0.5 rounded-full border border-indigo-500">
              ${econ.school}
            </span>
            <span class="bg-amber-400 text-indigo-950 text-xs font-black px-3 py-0.5 rounded-full">
              <i class="fa-regular fa-clock mr-1"></i> ${econ.epoch}
            </span>
          </div>
          <p class="text-xs text-indigo-200 leading-relaxed max-w-3xl">${econ.context}</p>
        </div>
        <div class="bg-white/10 backdrop-blur rounded-xl p-3 text-center border border-white/20 flex-shrink-0">
          <div class="text-xl font-black text-amber-300">${addressed.length} / ${window.BANKING_DATA.topics.length}</div>
          <div class="text-[10px] text-indigo-200 font-semibold uppercase tracking-wider">Ejes Abordados</div>
        </div>
      </div>

      <div class="mt-4 pt-4 border-t border-indigo-800 flex flex-wrap items-center gap-2">
        <span class="text-xs text-indigo-300 font-semibold">Textos de la Cátedra:</span>
        ${primaryTags}
      </div>
    </div>

    <!-- Section 1: What this economist speaks about -->
    <div class="mb-8">
      <div class="flex items-center gap-2 mb-3">
        <span class="w-2.5 h-2.5 rounded-full bg-emerald-500"></span>
        <h5 class="text-sm font-bold uppercase tracking-wider text-slate-800">
          ¿De qué habla este economista? (${addressed.length} temas desarrollados)
        </h5>
      </div>
      <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
        ${addressedCards}
      </div>
    </div>

    <!-- Section 2: What this economist DOES NOT speak about -->
    <div>
      <div class="flex items-center gap-2 mb-2">
        <span class="w-2.5 h-2.5 rounded-full bg-slate-400"></span>
        <h5 class="text-sm font-bold uppercase tracking-wider text-slate-600">
          Temas que NO aborda puntualmente en los textos (${unaddressed.length} temas)
        </h5>
      </div>
      <p class="text-xs text-slate-500 mb-2">
        El autor no formula una teoría específica sobre estos tópicos en los textos evaluados de la materia:
      </p>
      ${unaddressedCards}
    </div>
  `;

  if (window.MathJax && window.MathJax.typesetPromise) {
    window.MathJax.typesetPromise();
  }
}

function renderTopicChips() {
  const container = document.getElementById('topicChipsContainer');
  if (!container) return;
  container.innerHTML = '';

  const icons = [
    'fa-coins', 'fa-vault', 'fa-arrow-trend-up', 'fa-building-columns',
    'fa-chart-line-down', 'fa-scale-balanced', 'fa-brain', 'fa-globe'
  ];

  window.BANKING_DATA.topics.forEach((t, idx) => {
    const isSelected = t.id === selectedFilterTopicId;
    const card = document.createElement('button');
    card.type = 'button';
    card.className = isSelected
      ? 'p-3 rounded-xl text-left bg-indigo-900 text-white shadow border-2 border-amber-400 transition flex flex-col justify-between transform scale-102'
      : 'p-3 rounded-xl text-left bg-white text-slate-800 hover:bg-indigo-50 border border-slate-200 transition flex flex-col justify-between';

    card.innerHTML = `
      <div class="flex items-center justify-between mb-1.5">
        <i class="fa-solid ${icons[idx % icons.length]} ${isSelected ? 'text-amber-400' : 'text-indigo-600'} text-xs"></i>
        <span class="text-[9px] font-bold ${isSelected ? 'bg-indigo-800 text-amber-300' : 'bg-slate-100 text-slate-600'} px-1.5 py-0.5 rounded">Eje ${idx+1}</span>
      </div>
      <div class="text-xs font-bold ${isSelected ? 'text-white' : 'text-indigo-950'} line-clamp-1">${t.name}</div>
    `;

    card.onclick = () => selectFilterTopic(t.id);
    container.appendChild(card);
  });
}

function selectFilterTopic(topicId) {
  selectedFilterTopicId = topicId;
  renderTopicChips();
  renderSelectedTopicDetail();
}

function renderSelectedTopicDetail() {
  const container = document.getElementById('selectedTopicResult');
  if (!container) return;

  const topic = window.BANKING_DATA.topics.find(t => t.id === selectedFilterTopicId);
  if (!topic) return;

  const speakers = [];
  const nonSpeakers = [];

  window.BANKING_DATA.economists.forEach(e => {
    const stance = e.stances[topic.id] || '[No aborda este tema puntualmente en los textos analizados]';
    if (stance.includes('[No aborda este tema')) {
      nonSpeakers.push({ econ: e, stance });
    } else {
      speakers.push({ econ: e, stance });
    }
  });

  let speakersCards = '';
  speakers.forEach(item => {
    speakersCards += `
      <div class="bg-white rounded-xl border border-slate-200 p-5 shadow-sm hover:shadow-md transition flex flex-col justify-between">
        <div>
          <div class="flex items-start justify-between gap-2 mb-2">
            <div>
              <h5 class="text-sm font-bold text-indigo-950">${item.econ.name}</h5>
              <div class="text-[11px] text-indigo-700 font-semibold">${item.econ.school}</div>
            </div>
            <span class="bg-amber-100 text-amber-900 text-[10px] font-bold px-2.5 py-0.5 rounded-full flex-shrink-0">
              ${item.econ.epoch}
            </span>
          </div>

          <div class="mt-3 bg-slate-50 p-4 rounded-xl border border-slate-200 text-xs text-slate-800 leading-relaxed font-sans whitespace-pre-line">
            ${item.stance}
          </div>
        </div>

        <div class="mt-4 pt-3 border-t border-slate-100 flex items-center justify-between text-[11px]">
          <span class="text-slate-500 font-mono text-[10px]">${item.econ.primary_texts[0] || ''}</span>
          <button onclick="openModal('${item.econ.id}', '${topic.id}')" class="text-indigo-600 font-bold hover:text-indigo-900 flex items-center gap-1">
            Ver Ficha Completa <i class="fa-solid fa-arrow-up-right-from-square text-[9px]"></i>
          </button>
        </div>
      </div>
    `;
  });

  let nonSpeakersBadges = '';
  if (nonSpeakers.length > 0) {
    nonSpeakersBadges = '<div class="flex flex-wrap gap-2 mt-2">';
    nonSpeakers.forEach(item => {
      nonSpeakersBadges += `
        <span class="bg-slate-100 border border-slate-300 text-slate-600 text-xs px-2.5 py-1 rounded-lg font-medium flex items-center gap-1.5" title="${item.stance}">
          <i class="fa-solid fa-minus text-slate-400 text-[10px]"></i>
          ${item.econ.name}
        </span>
      `;
    });
    nonSpeakersBadges += '</div>';
  } else {
    nonSpeakersBadges = '<div class="text-xs text-emerald-700 font-semibold">¡Todos los economistas analizados debaten este tema!</div>';
  }

  container.innerHTML = `
    <!-- Topic Header Banner -->
    <div class="bg-gradient-to-r from-slate-900 via-indigo-950 to-indigo-900 text-white rounded-2xl p-6 shadow-md mb-6">
      <div class="flex flex-col md:flex-row md:items-center justify-between gap-4">
        <div>
          <span class="text-xs font-bold uppercase tracking-wider text-amber-400 bg-amber-400/10 px-2.5 py-0.5 rounded border border-amber-400/30">
            Eje Temático Seleccionado
          </span>
          <h4 class="text-2xl font-black text-white mt-1.5">${topic.name}</h4>
          <p class="text-xs text-indigo-200 mt-1 max-w-3xl leading-relaxed">${topic.description}</p>
        </div>
        <div class="bg-white/10 backdrop-blur rounded-xl p-3 text-center border border-white/20 flex-shrink-0">
          <div class="text-xl font-black text-emerald-400">${speakers.length} / ${window.BANKING_DATA.economists.length}</div>
          <div class="text-[10px] text-indigo-200 font-semibold uppercase tracking-wider">Economistas que debaten</div>
        </div>
      </div>
    </div>

    <!-- Section 1: Who speaks about this topic -->
    <div class="mb-8">
      <div class="flex items-center gap-2 mb-3">
        <span class="w-2.5 h-2.5 rounded-full bg-emerald-500"></span>
        <h5 class="text-sm font-bold uppercase tracking-wider text-slate-800">
          ¿Quiénes hablan de esto? (${speakers.length} economistas confrontados)
        </h5>
      </div>
      <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
        ${speakersCards}
      </div>
    </div>

    <!-- Section 2: Who DOES NOT speak about this topic -->
    <div class="bg-slate-50 border border-slate-200 p-5 rounded-2xl">
      <div class="flex items-center gap-2 mb-1">
        <span class="w-2.5 h-2.5 rounded-full bg-slate-400"></span>
        <h5 class="text-xs font-bold uppercase tracking-wider text-slate-600">
          ¿Quiénes NO abordan este tema puntualmente? (${nonSpeakers.length} economistas)
        </h5>
      </div>
      <p class="text-xs text-slate-500 mb-2">
        Los siguientes autores no tienen un tratamiento específico de este tema en los textos de la materia:
      </p>
      ${nonSpeakersBadges}
    </div>
  `;

  if (window.MathJax && window.MathJax.typesetPromise) {
    window.MathJax.typesetPromise();
  }
}

// ----------------------------------------------------
// MODAL DETAILS (CELL DRILL-DOWN)
// ----------------------------------------------------
function openModal(econId, topicId) {
  const modal = document.getElementById('cellModal');
  const econ = window.BANKING_DATA.economists.find(e => e.id === econId);
  const topic = window.BANKING_DATA.topics.find(t => t.id === topicId);

  if (!modal || !econ || !topic) return;

  document.getElementById('modalEconomist').textContent = econ.name;
  document.getElementById('modalTopic').textContent = `${topic.name} — ${topic.description}`;
  document.getElementById('modalSchoolBadge').textContent = econ.school;
  document.getElementById('modalEpochBadge').textContent = `Época: ${econ.epoch}`;

  const stanceText = econ.stances[topicId] || '[No aborda este tema puntualmente en los textos analizados]';
  const stanceContainer = document.getElementById('modalStance');

  if (stanceText.includes('[No aborda este tema')) {
    stanceContainer.innerHTML = `<div class="bg-amber-50 text-amber-900 border border-amber-200 p-3 rounded-lg flex items-start gap-2">
      <i class="fa-solid fa-circle-info text-amber-600 mt-0.5"></i>
      <div>
        <strong>Sin tratamiento puntual:</strong> ${stanceText}
      </div>
    </div>`;
  } else {
    stanceContainer.textContent = stanceText;
  }

  // Populate sources tags
  const sourcesContainer = document.getElementById('modalSources');
  sourcesContainer.innerHTML = '';
  if (econ.primary_texts && econ.primary_texts.length > 0) {
    econ.primary_texts.forEach(txt => {
      const tag = document.createElement('span');
      tag.className = 'bg-slate-200 text-slate-800 px-2.5 py-1 rounded-md font-medium text-[11px]';
      tag.textContent = txt;
      sourcesContainer.appendChild(tag);
    });
  }

  modal.classList.remove('hidden');

  if (window.MathJax && window.MathJax.typesetPromise) {
    window.MathJax.typesetPromise();
  }
}

function closeModal() {
  const modal = document.getElementById('cellModal');
  if (modal) modal.classList.add('hidden');
}

// Close modal when clicking outside box
document.addEventListener('keydown', (e) => {
  if (e.key === 'Escape') closeModal();
});
document.getElementById('cellModal')?.addEventListener('click', (e) => {
  if (e.target.id === 'cellModal') closeModal();
});

// ----------------------------------------------------
// TAB 2: ECONOMISTS & EPOCHS RENDERING
// ----------------------------------------------------
function renderEconomistsList(filterText = '') {
  const container = document.getElementById('economistsListContainer');
  if (!container) return;

  container.innerHTML = '';
  const search = filterText.toLowerCase().trim();

  const filtered = window.BANKING_DATA.economists.filter(e => {
    if (!search) return true;
    return e.name.toLowerCase().includes(search) || 
           e.school.toLowerCase().includes(search) ||
           e.epoch.toLowerCase().includes(search) ||
           e.context.toLowerCase().includes(search);
  });

  if (filtered.length === 0) {
    container.innerHTML = `<div class="bg-white p-8 rounded-xl text-center text-slate-500 border border-slate-200">
      No se encontraron economistas que coincidan con "${filterText}".
    </div>`;
    return;
  }

  filtered.forEach(e => {
    // Count addressed vs unaddressed
    let addressedCount = 0;
    let unaddressedCount = 0;

    window.BANKING_DATA.topics.forEach(t => {
      const val = e.stances[t.id] || '';
      if (val.includes('[No aborda')) unaddressedCount++;
      else addressedCount++;
    });

    const card = document.createElement('div');
    card.className = 'bg-white rounded-2xl shadow-sm border border-slate-200 overflow-hidden card-hover';

    let topicsHtml = '<div class="grid grid-cols-1 md:grid-cols-2 gap-4 mt-4">';
    window.BANKING_DATA.topics.forEach(t => {
      const stance = e.stances[t.id] || '[No aborda este tema puntualmente en los textos analizados]';
      const isExcluded = stance.includes('[No aborda este tema');

      topicsHtml += `<div class="p-4 rounded-xl border ${isExcluded ? 'bg-slate-50 border-slate-200 text-slate-500' : 'bg-indigo-50/30 border-indigo-100 text-slate-800 shadow-sm'}">
        <div class="flex items-center justify-between mb-2 pb-1.5 border-b ${isExcluded ? 'border-slate-200' : 'border-indigo-100/70'}">
          <span class="font-bold text-xs ${isExcluded ? 'text-slate-600' : 'text-indigo-950'} flex items-center gap-1.5">
            <i class="fa-solid ${isExcluded ? 'fa-minus text-slate-400' : 'fa-graduation-cap text-indigo-600'} text-[11px]"></i>
            ${t.name}
          </span>
          <span class="text-[10px] ${isExcluded ? 'bg-slate-200 text-slate-600 px-2 py-0.5 rounded font-medium' : 'bg-indigo-100 text-indigo-800 font-bold px-2.5 py-0.5 rounded-full'}">
            ${isExcluded ? 'No abordado' : 'Abordado para Examen'}
          </span>
        </div>
        <div class="text-xs leading-relaxed whitespace-pre-line font-sans ${isExcluded ? 'italic text-slate-500 text-[11px]' : 'text-slate-800'}">
          ${stance}
        </div>
      </div>`;
    });
    topicsHtml += '</div>';

    let textsTags = '';
    e.primary_texts.forEach(txt => {
      textsTags += `<span class="bg-indigo-900/10 text-indigo-950 font-semibold px-2.5 py-1 rounded-md text-[11px]">${txt}</span>`;
    });

    card.innerHTML = `
      <div class="p-6 bg-slate-50 border-b border-slate-200 flex flex-col md:flex-row md:items-center justify-between gap-4">
        <div>
          <div class="flex flex-wrap items-center gap-2 mb-1">
            <h4 class="text-lg font-bold text-indigo-950">${e.name}</h4>
            <span class="bg-indigo-100 text-indigo-800 px-2.5 py-0.5 rounded-full text-xs font-semibold">${e.school}</span>
            <span class="bg-amber-100 text-amber-900 px-2.5 py-0.5 rounded-full text-xs font-semibold">
              <i class="fa-regular fa-clock mr-1"></i> ${e.epoch}
            </span>
          </div>
          <p class="text-xs text-slate-600 mt-1 max-w-3xl leading-relaxed">${e.context}</p>
        </div>
        <div class="flex flex-wrap items-center gap-2 flex-shrink-0">
          <button onclick="toggleAudioReader('economist', '${e.id}')" id="btnAudio-economist-${e.id}" class="text-xs bg-amber-400 hover:bg-amber-500 text-slate-950 font-black px-3 py-1.5 rounded-lg shadow transition flex items-center gap-1.5 btn-audio-card" title="Escuchar texto completo con voz femenina">
            <i class="fa-solid fa-microphone-lines text-slate-950"></i> <span class="audio-label">Escuchar</span>
          </button>
          <button onclick="launchExamForEconomist('${e.id}')" class="text-xs bg-indigo-600 hover:bg-indigo-700 text-white font-bold px-3 py-1.5 rounded-lg shadow transition flex items-center gap-1.5">
            <i class="fa-solid fa-graduation-cap text-amber-300"></i> Rendir Examen (20 Preguntas)
          </button>
          <span class="text-xs bg-emerald-100 text-emerald-800 font-bold px-3 py-1 rounded-lg">
            ${addressedCount} temas abordados
          </span>
          <span class="text-xs bg-slate-200 text-slate-700 font-medium px-2.5 py-1 rounded-lg">
            ${unaddressedCount} no abordados
          </span>
        </div>
      </div>

      <div class="p-6">
        <div class="mb-2">
          <span class="text-xs font-bold uppercase tracking-wider text-slate-500">Textos Fuente de la Cátedra:</span>
          <div class="flex flex-wrap gap-2 mt-1.5">
            ${textsTags}
          </div>
        </div>

        <div class="mt-5">
          <h5 class="text-xs font-bold uppercase tracking-wider text-slate-500 mb-2">Desglose de Posturas por Eje Temático:</h5>
          ${topicsHtml}
        </div>
      </div>
    `;

    container.appendChild(card);
  });
}

function filterEconomistsList(val) {
  renderEconomistsList(val);
}

// ----------------------------------------------------
// TAB 3: 13 TEXTS RESUMEN RENDERING
// ----------------------------------------------------
function renderTextsList() {
  const container = document.getElementById('textsListContainer');
  const catFilter = document.getElementById('textCategoryFilter')?.value || 'all';

  if (!container) return;
  container.innerHTML = '';

  const filtered = window.BANKING_DATA.texts.filter(t => {
    if (catFilter === 'all') return true;
    return t.category === catFilter;
  });

  filtered.forEach(t => {
    const card = document.createElement('div');
    card.className = 'bg-white rounded-2xl shadow-sm border border-slate-200 overflow-hidden card-hover flex flex-col justify-between';

    let pointsHtml = '<ul class="mt-3 space-y-1.5 text-xs text-slate-700">';
    t.key_points.forEach(pt => {
      pointsHtml += `<li class="flex items-start gap-2">
        <i class="fa-solid fa-circle-check text-emerald-600 text-[10px] mt-1 flex-shrink-0"></i>
        <span>${pt}</span>
      </li>`;
    });
    pointsHtml += '</ul>';

    let econTags = '';
    t.related_economists.forEach(ec => {
      econTags += `<span class="bg-indigo-50 text-indigo-700 font-semibold px-2 py-0.5 rounded text-[10px]">${ec}</span>`;
    });

    const isLargeDoc = t.pages > 40;

    card.innerHTML = `
      <div class="p-5 flex-1">
        <div class="flex items-start justify-between gap-3 mb-2">
          <span class="bg-indigo-100 text-indigo-900 font-bold text-[11px] px-2.5 py-0.5 rounded-full uppercase tracking-wider">
            ${t.category}
          </span>
          <span class="text-xs font-bold px-2 py-0.5 rounded-md ${isLargeDoc ? 'bg-amber-400 text-indigo-950 font-black' : 'bg-slate-100 text-slate-700'}">
            ${t.pages} págs ${isLargeDoc ? '(&gt;40 pág)' : ''}
          </span>
        </div>

        <h4 class="text-base font-bold text-indigo-950 leading-snug">${t.title}</h4>
        <div class="text-xs text-slate-500 font-medium mt-1 flex items-center gap-2">
          <span><i class="fa-solid fa-pen-nib mr-1 text-slate-400"></i>${t.author} (${t.year})</span>
          <span>&bull;</span>
          <span class="font-mono text-[11px] text-slate-600">${t.file}</span>
        </div>

        <div class="mt-4 text-xs text-slate-700 leading-relaxed whitespace-pre-line bg-slate-50 p-3.5 rounded-xl border border-slate-200">
          ${t.summary}
        </div>

        <div class="mt-4">
          <h5 class="text-[11px] font-bold uppercase tracking-wider text-slate-500">Puntos Clave del Texto:</h5>
          ${pointsHtml}
        </div>
      </div>

      <div class="p-4 bg-slate-50 border-t border-slate-200 flex flex-wrap items-center justify-between gap-2">
        <div class="flex flex-wrap items-center gap-1.5">
          <span class="text-[10px] font-bold text-slate-400 uppercase">Autores/Escuelas:</span>
          ${econTags}
        </div>
        ${isLargeDoc ? `<button onclick="switchTab('tab-largos')" class="text-xs bg-amber-400 hover:bg-amber-500 text-indigo-950 font-bold px-2.5 py-1 rounded transition flex items-center gap-1">
          <i class="fa-solid fa-filter"></i> Ver Filtro
        </button>` : ''}
      </div>
    `;

    container.appendChild(card);
  });
}

function filterTextsList() {
  renderTextsList();
}

// ----------------------------------------------------
// TAB 4: DEEP DIVE (>40 PAGES) RENDERING
// ----------------------------------------------------
function renderDeepDive() {
  const container = document.getElementById('deepDiveContainer');
  if (!container) return;

  const data = window.BANKING_DATA.deep_dive_over_40;
  container.innerHTML = '';

  data.texts.forEach(item => {
    const card = document.createElement('div');
    card.className = 'bg-white rounded-2xl shadow-sm border border-slate-200 overflow-hidden card-hover';

    let comparisonsHtml = '<div class="space-y-3 mt-4">';
    item.cross_comparisons.forEach(c => {
      comparisonsHtml += `
        <div class="p-4 rounded-xl border border-indigo-100 bg-indigo-50/40 text-xs">
          <div class="font-bold text-indigo-950 flex items-center gap-2 mb-1">
            <i class="fa-solid fa-link text-indigo-600"></i>
            Conexión con ${c.linked_text}
          </div>
          <p class="text-slate-700 leading-relaxed">${c.connection}</p>
        </div>
      `;
    });
    comparisonsHtml += '</div>';

    card.innerHTML = `
      <div class="p-6 bg-slate-50 border-b border-slate-200">
        <div class="flex flex-wrap items-center justify-between gap-3 mb-2">
          <span class="bg-amber-400 text-indigo-950 font-black text-xs px-3 py-1 rounded-full uppercase tracking-wider">
            Texto Extenso: ${item.pages} Páginas
          </span>
          <span class="font-mono text-xs text-slate-600 bg-white border border-slate-200 px-2.5 py-1 rounded-md">
            ${item.file}
          </span>
        </div>
        <h4 class="text-xl font-bold text-indigo-950">${item.title}</h4>
        <div class="text-xs text-slate-600 font-semibold mt-1">Autor: ${item.author}</div>
      </div>

      <div class="p-6 space-y-5 text-xs text-slate-700">
        <!-- Tesis Central -->
        <div class="bg-indigo-900 text-white p-4 rounded-xl">
          <div class="font-bold text-amber-300 text-xs uppercase tracking-wider mb-1">
            <i class="fa-solid fa-compass mr-1"></i> Tesis y Aporte Central:
          </div>
          <p class="text-indigo-100 leading-relaxed">${item.core_thesis}</p>
        </div>

        <!-- Filtrado vs Retenido -->
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
          <div class="bg-red-50 border border-red-200 p-4 rounded-xl text-red-900">
            <div class="font-bold text-red-800 flex items-center gap-1.5 mb-1 text-xs uppercase tracking-wider">
              <i class="fa-solid fa-trash-can text-red-600"></i> Contenido No Relacionado (Descartado):
            </div>
            <p class="text-red-950 leading-relaxed">${item.filtered_out}</p>
          </div>

          <div class="bg-emerald-50 border border-emerald-200 p-4 rounded-xl text-emerald-900">
            <div class="font-bold text-emerald-800 flex items-center gap-1.5 mb-1 text-xs uppercase tracking-wider">
              <i class="fa-solid fa-circle-check text-emerald-600"></i> Núcleo Esencial Retenido:
            </div>
            <p class="text-emerald-950 leading-relaxed">${item.retained_core}</p>
          </div>
        </div>

        <!-- Comparaciones Cruzadas con los otros textos -->
        <div>
          <h5 class="text-xs font-bold uppercase tracking-wider text-slate-500 mb-2">
            Comparación Cruzada y Articulación con los Demás Textos de la Cátedra:
          </h5>
          ${comparisonsHtml}
        </div>
      </div>
    `;

    container.appendChild(card);
  });
}

// ----------------------------------------------------
// GLOBAL QUICK SEARCH BAR
// ----------------------------------------------------
function toggleQuickSearch() {
  const banner = document.getElementById('quickSearchBanner');
  const input = document.getElementById('globalSearchInput');
  if (!banner) return;

  if (banner.classList.contains('hidden')) {
    banner.classList.remove('hidden');
    input?.focus();
  } else {
    banner.classList.add('hidden');
  }
}

function handleGlobalSearch(query) {
  const resultsBox = document.getElementById('quickSearchResults');
  if (!resultsBox) return;

  const q = query.toLowerCase().trim();
  if (!q || q.length < 2) {
    resultsBox.classList.add('hidden');
    resultsBox.innerHTML = '';
    return;
  }

  resultsBox.classList.remove('hidden');

  let matches = [];

  // Search in economists
  window.BANKING_DATA.economists.forEach(e => {
    if (e.name.toLowerCase().includes(q) || e.school.toLowerCase().includes(q) || e.context.toLowerCase().includes(q)) {
      matches.push({ type: 'Economista', title: e.name, subtitle: `${e.school} (${e.epoch})`, tab: 'tab-economistas' });
    }
    // Search in stances
    window.BANKING_DATA.topics.forEach(t => {
      const stance = e.stances[t.id] || '';
      if (stance.toLowerCase().includes(q) && !stance.includes('[No aborda')) {
        matches.push({ type: 'Postura', title: `${e.name} en ${t.name}`, subtitle: stance.substring(0, 110) + '...', tab: 'tab-economistas', econId: e.id, topicId: t.id });
      }
    });
  });

  // Search in texts
  window.BANKING_DATA.texts.forEach(txt => {
    if (txt.title.toLowerCase().includes(q) || txt.author.toLowerCase().includes(q) || txt.summary.toLowerCase().includes(q)) {
      matches.push({ type: 'Texto', title: txt.title, subtitle: `${txt.author} (${txt.year}) - ${txt.category}`, tab: 'tab-textos' });
    }
  });

  // Match exam keys
  if (window.BANKING_DATA.exam_keys) {
    window.BANKING_DATA.exam_keys.forEach(k => {
      if (k.title.toLowerCase().includes(q) || k.economist_name.toLowerCase().includes(q) || k.why_is_key.toLowerCase().includes(q) || k.the_key.toLowerCase().includes(q)) {
        matches.push({
          type: 'Clave de Examen',
          title: `#${k.number}: ${k.title}`,
          subtitle: `${k.economist_name} (${k.school})`,
          tab: 'tab-claves'
        });
      }
    });
  }

  if (matches.length === 0) {
    resultsBox.innerHTML = `No se encontraron coincidencias para "${query}".`;
    return;
  }

  let html = `<div class="font-bold text-slate-800 mb-1.5">${matches.length} resultados encontrados:</div><div class="grid grid-cols-1 sm:grid-cols-2 gap-2 max-h-48 overflow-y-auto">`;
  matches.slice(0, 10).forEach(m => {
    html += `
      <div class="bg-white p-2 rounded border border-amber-200 cursor-pointer hover:bg-amber-50" onclick="handleSearchResultClick('${m.tab}', '${m.econId || ''}', '${m.topicId || ''}')">
        <div class="flex items-center gap-1 text-[10px] font-bold text-indigo-700">
          <span class="bg-indigo-50 px-1.5 py-0.5 rounded">${m.type}</span>
          <span>${m.title}</span>
        </div>
        <div class="text-[11px] text-slate-600 line-clamp-1 mt-0.5">${m.subtitle}</div>
      </div>
    `;
  });
  html += '</div>';

  resultsBox.innerHTML = html;
}

function handleSearchResultClick(tab, econId, topicId) {
  switchTab(tab);
  document.getElementById('quickSearchBanner')?.classList.add('hidden');
  if (econId && topicId) {
    setTimeout(() => openModal(econId, topicId), 300);
  }
}

// ====================================================
// CREADOR Y SIMULADOR DE EXÁMENES UNIVERSITARIOS
// ====================================================

let examConfig = {
  economistId: 'all',
  questionCount: 20,
  mode: 'practice' // 'practice' | 'simulacro'
};

let examSession = {
  questions: [],
  currentIndex: 0,
  userAnswers: {}, // index -> { selectedOptionIndex: number, isCorrect: boolean }
  startTime: null,
  timerInterval: null,
  elapsedSeconds: 0,
  isFinished: false,
  mode: 'practice'
};

function initExamTab() {
  const select = document.getElementById('examEconomistSelect');
  if (!select) return;

  // Clear existing options except 'all'
  select.innerHTML = '<option value="all">🌟 Todos los Economistas (Examen Integrador de Cátedra - 260 Preguntas)</option>';

  if (window.BANKING_DATA && window.BANKING_DATA.economists) {
    window.BANKING_DATA.economists.forEach(e => {
      const opt = document.createElement('option');
      opt.value = e.id;
      opt.textContent = `${e.name} (${e.school}) — 20 Preguntas`;
      select.appendChild(opt);
    });
  }

  select.addEventListener('change', (e) => {
    examConfig.economistId = e.target.value;
    updateExamConfigHelperText();
  });

  updateExamConfigHelperText();
}

function updateExamConfigHelperText() {
  const helper = document.getElementById('examAvailableCountText');
  if (!helper) return;

  if (examConfig.economistId === 'all') {
    helper.innerHTML = '<i class="fa-solid fa-layer-group text-indigo-600 mr-1"></i> Banco global: <strong>260 preguntas teóricas</strong> de los 13 autores de la cátedra.';
  } else {
    const econ = window.BANKING_DATA?.economists.find(e => e.id === examConfig.economistId);
    const authorName = econ ? econ.name : 'este autor';
    helper.innerHTML = `<i class="fa-solid fa-user-check text-emerald-600 mr-1"></i> Banco especializado: <strong>20 preguntas de alta rigurosidad</strong> para <strong>${authorName}</strong>.`;
  }
}

function setExamQuestionCount(count) {
  examConfig.questionCount = count;
  document.querySelectorAll('.count-pill').forEach(btn => {
    btn.classList.remove('active', 'border-2', 'border-indigo-600', 'bg-indigo-50', 'text-indigo-900');
    btn.classList.add('border', 'border-slate-200', 'bg-slate-50', 'text-slate-700');
  });

  const activeBtn = document.getElementById(`btnCount-${count}`);
  if (activeBtn) {
    activeBtn.classList.remove('border', 'border-slate-200', 'bg-slate-50', 'text-slate-700');
    activeBtn.classList.add('active', 'border-2', 'border-indigo-600', 'bg-indigo-50', 'text-indigo-900');
  }
}

function setExamMode(mode) {
  examConfig.mode = mode;
  document.querySelectorAll('.mode-pill').forEach(btn => {
    btn.classList.remove('active', 'border-2', 'border-indigo-600', 'bg-indigo-50', 'text-indigo-950');
    btn.classList.add('border', 'border-slate-200', 'bg-slate-50', 'text-slate-700');
  });

  const activeBtn = document.getElementById(`btnMode-${mode}`);
  if (activeBtn) {
    activeBtn.classList.remove('border', 'border-slate-200', 'bg-slate-50', 'text-slate-700');
    activeBtn.classList.add('active', 'border-2', 'border-indigo-600', 'bg-indigo-50', 'text-indigo-950');
  }
}

function launchExamForEconomist(econId) {
  switchTab('tab-examenes');
  const select = document.getElementById('examEconomistSelect');
  if (select) {
    select.value = econId;
    examConfig.economistId = econId;
    updateExamConfigHelperText();
  }
  // Default to 20 questions for that author
  setExamQuestionCount(20);

  // Scroll smoothly to config view
  const configView = document.getElementById('examConfigView');
  if (configView) {
    configView.scrollIntoView({ behavior: 'smooth' });
  }
}

function shuffleArray(arr) {
  const array = [...arr];
  for (let i = array.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [array[i], array[j]] = [array[j], array[i]];
  }
  return array;
}

function startExamSession() {
  if (!window.EXAM_QUESTIONS || !window.EXAM_QUESTIONS.questions_by_economist) {
    alert('El banco de preguntas no se ha cargado correctamente. Por favor recarga la página.');
    return;
  }

  const select = document.getElementById('examEconomistSelect');
  const selectedEconId = select ? select.value : examConfig.economistId;
  examConfig.economistId = selectedEconId;

  let rawQuestions = [];

  if (selectedEconId === 'all') {
    // Collect from all economists
    Object.keys(window.EXAM_QUESTIONS.questions_by_economist).forEach(eid => {
      const econ = window.BANKING_DATA?.economists.find(e => e.id === eid);
      const list = window.EXAM_QUESTIONS.questions_by_economist[eid] || [];
      list.forEach(q => {
        rawQuestions.push({
          ...q,
          econId: eid,
          econName: econ ? econ.name : 'Economista de la Cátedra',
          econSchool: econ ? econ.school : 'Teoría Monetaria'
        });
      });
    });
    // Shuffle all and slice to requested count
    rawQuestions = shuffleArray(rawQuestions).slice(0, examConfig.questionCount);
  } else {
    // Specific economist
    const econ = window.BANKING_DATA?.economists.find(e => e.id === selectedEconId);
    const list = window.EXAM_QUESTIONS.questions_by_economist[selectedEconId] || [];
    list.forEach(q => {
      rawQuestions.push({
        ...q,
        econId: selectedEconId,
        econName: econ ? econ.name : 'Economista de la Cátedra',
        econSchool: econ ? econ.school : 'Teoría Monetaria'
      });
    });
    // Shuffle and pick up to questionCount
    const limit = Math.min(examConfig.questionCount, rawQuestions.length);
    rawQuestions = shuffleArray(rawQuestions).slice(0, limit);
  }

  if (rawQuestions.length === 0) {
    alert('No se encontraron preguntas disponibles para este autor.');
    return;
  }

  // Shuffle options for each question so correct answer isn't always at the same index
  const processedQuestions = rawQuestions.map(q => {
    const optsWithFlags = q.options.map((text, idx) => ({
      text,
      isCorrect: idx === q.correct_index
    }));
    const shuffledOpts = shuffleArray(optsWithFlags);
    const newCorrectIndex = shuffledOpts.findIndex(o => o.isCorrect);

    return {
      ...q,
      options: shuffledOpts.map(o => o.text),
      correct_index: newCorrectIndex
    };
  });

  // Initialize session
  examSession = {
    questions: processedQuestions,
    currentIndex: 0,
    userAnswers: {},
    startTime: Date.now(),
    timerInterval: null,
    elapsedSeconds: 0,
    isFinished: false,
    mode: examConfig.mode
  };

  // Timer handling
  if (examSession.mode === 'simulacro') {
    const timerBox = document.getElementById('examTimerContainer');
    if (timerBox) timerBox.classList.remove('hidden');
    updateTimerDisplay();
    examSession.timerInterval = setInterval(() => {
      examSession.elapsedSeconds++;
      updateTimerDisplay();
    }, 1000);
  } else {
    const timerBox = document.getElementById('examTimerContainer');
    if (timerBox) timerBox.classList.add('hidden');
  }

  // Update header badges
  const badgeAuthor = document.getElementById('examBadgeAuthor');
  if (badgeAuthor) {
    if (selectedEconId === 'all') {
      badgeAuthor.textContent = '🌟 Examen Integrador de Cátedra';
    } else {
      const econ = window.BANKING_DATA?.economists.find(e => e.id === selectedEconId);
      badgeAuthor.textContent = econ ? econ.name : 'Autor Evaluado';
    }
  }

  const badgeMode = document.getElementById('examBadgeMode');
  if (badgeMode) {
    if (examSession.mode === 'practice') {
      badgeMode.className = 'px-2.5 py-1 rounded-full text-xs font-semibold bg-amber-100 text-amber-800 flex items-center gap-1';
      badgeMode.innerHTML = '<i class="fa-solid fa-lightbulb"></i> Práctica Guiada';
    } else {
      badgeMode.className = 'px-2.5 py-1 rounded-full text-xs font-semibold bg-indigo-100 text-indigo-800 flex items-center gap-1';
      badgeMode.innerHTML = '<i class="fa-solid fa-stopwatch"></i> Simulacro Real';
    }
  }

  // Switch Views
  document.getElementById('examConfigView')?.classList.add('hidden');
  document.getElementById('examResultsView')?.classList.add('hidden');
  document.getElementById('examActiveView')?.classList.remove('hidden');

  renderActiveQuestion();

  // Scroll to active container
  document.getElementById('examActiveView')?.scrollIntoView({ behavior: 'smooth' });
}

function updateTimerDisplay() {
  const display = document.getElementById('examTimerDisplay');
  if (!display) return;
  const mins = Math.floor(examSession.elapsedSeconds / 60).toString().padStart(2, '0');
  const secs = (examSession.elapsedSeconds % 60).toString().padStart(2, '0');
  display.textContent = `${mins}:${secs}`;
}

function formatTime(seconds) {
  const mins = Math.floor(seconds / 60).toString().padStart(2, '0');
  const secs = (seconds % 60).toString().padStart(2, '0');
  return `${mins}:${secs}`;
}

function renderActiveQuestion() {
  const total = examSession.questions.length;
  const idx = examSession.currentIndex;
  const q = examSession.questions[idx];

  // Counters & Progress
  document.getElementById('examCurrentNum').textContent = idx + 1;
  document.getElementById('examTotalNum').textContent = total;
  const pct = Math.round(((idx + 1) / total) * 100);
  document.getElementById('examProgressBar').style.width = `${pct}%`;

  // Topic badge & question text
  document.getElementById('examQuestionTopic').innerHTML = `
    <span class="font-bold text-indigo-900">${q.econName}</span>
    <span class="text-slate-400">&bull;</span>
    <span class="text-slate-600">${q.econSchool}</span>
  `;
  document.getElementById('examQuestionText').textContent = q.question;

  // Options rendering
  const optionsContainer = document.getElementById('examOptionsContainer');
  optionsContainer.innerHTML = '';

  const ans = examSession.userAnswers[idx];
  const hasAnswered = ans !== undefined;
  const letters = ['A', 'B', 'C', 'D'];

  q.options.forEach((optText, optIdx) => {
    const btn = document.createElement('button');
    btn.type = 'button';
    btn.className = 'w-full text-left p-4 rounded-xl transition flex items-start gap-3 border text-xs sm:text-sm ';

    const isSelected = hasAnswered && ans.selectedOptionIndex === optIdx;
    const isCorrectOption = optIdx === q.correct_index;

    if (examSession.mode === 'practice') {
      if (hasAnswered) {
        // Practice mode answered state
        btn.disabled = true;
        if (isCorrectOption) {
          btn.className += 'bg-emerald-50 border-2 border-emerald-500 text-emerald-950 font-bold shadow-sm';
        } else if (isSelected && !ans.isCorrect) {
          btn.className += 'bg-rose-50 border-2 border-rose-500 text-rose-950 font-medium line-through';
        } else {
          btn.className += 'bg-slate-50 border-slate-200 text-slate-400 opacity-60';
        }
      } else {
        // Practice mode unanswered state
        btn.className += 'bg-white border-slate-200 hover:border-indigo-400 hover:bg-indigo-50/40 text-slate-800 font-medium cursor-pointer shadow-xs';
        btn.onclick = () => selectExamOption(optIdx);
      }
    } else {
      // Simulacro mode
      if (isSelected) {
        btn.className += 'bg-indigo-50 border-2 border-indigo-600 text-indigo-950 font-bold shadow-sm';
      } else {
        btn.className += 'bg-white border-slate-200 hover:border-indigo-300 hover:bg-slate-50 text-slate-700 cursor-pointer shadow-xs';
      }
      btn.onclick = () => selectExamOption(optIdx);
    }

    // Inner Option HTML
    let iconHtml = '';
    if (examSession.mode === 'practice' && hasAnswered) {
      if (isCorrectOption) {
        iconHtml = '<i class="fa-solid fa-circle-check text-emerald-600 text-base mt-0.5 flex-shrink-0"></i>';
      } else if (isSelected && !ans.isCorrect) {
        iconHtml = '<i class="fa-solid fa-circle-xmark text-rose-600 text-base mt-0.5 flex-shrink-0"></i>';
      } else {
        iconHtml = `<span class="w-6 h-6 rounded-lg bg-slate-200 text-slate-500 font-bold text-xs flex items-center justify-center flex-shrink-0">${letters[optIdx]}</span>`;
      }
    } else {
      const letterBg = isSelected ? 'bg-indigo-600 text-white' : 'bg-slate-100 text-slate-700 border border-slate-200';
      iconHtml = `<span class="w-6 h-6 rounded-lg ${letterBg} font-bold text-xs flex items-center justify-center flex-shrink-0">${letters[optIdx]}</span>`;
    }

    btn.innerHTML = `
      ${iconHtml}
      <div class="flex-1 leading-relaxed">${optText}</div>
    `;

    optionsContainer.appendChild(btn);
  });

  // Feedback Box (Practice Mode Only)
  const feedbackBox = document.getElementById('examFeedbackBox');
  const feedbackTitle = document.getElementById('examFeedbackTitle');
  const feedbackExp = document.getElementById('examFeedbackExplanation');

  if (examSession.mode === 'practice' && hasAnswered) {
    feedbackBox.classList.remove('hidden');
    if (ans.isCorrect) {
      feedbackBox.className = 'mt-6 p-5 rounded-2xl border-2 border-emerald-300 bg-emerald-50/80 text-emerald-950 transition-all shadow-sm';
      feedbackTitle.innerHTML = `
        <span class="w-7 h-7 rounded-full bg-emerald-500 text-white flex items-center justify-center text-sm shadow">
          <i class="fa-solid fa-check"></i>
        </span>
        <span class="text-emerald-900 font-extrabold text-sm sm:text-base">¡Respuesta Correcta! Justificación Teórica Universitaria:</span>
      `;
    } else {
      feedbackBox.className = 'mt-6 p-5 rounded-2xl border-2 border-rose-300 bg-rose-50/80 text-rose-950 transition-all shadow-sm';
      feedbackTitle.innerHTML = `
        <span class="w-7 h-7 rounded-full bg-rose-500 text-white flex items-center justify-center text-sm shadow">
          <i class="fa-solid fa-xmark"></i>
        </span>
        <span class="text-rose-900 font-extrabold text-sm sm:text-base">Respuesta Incorrecta. La opción correcta es la ${letters[q.correct_index]}:</span>
      `;
    }

    feedbackExp.innerHTML = `
      <div class="mt-2 text-xs sm:text-sm text-slate-800 leading-relaxed bg-white/90 p-4 rounded-xl border border-slate-200/60 shadow-xs">
        <p class="font-sans">${q.explanation}</p>
      </div>
    `;
  } else {
    feedbackBox.classList.add('hidden');
  }

  // Navigation Buttons
  const btnPrev = document.getElementById('btnExamPrev');
  const btnNext = document.getElementById('btnExamNext');
  const btnFinish = document.getElementById('btnExamFinish');

  btnPrev.disabled = (idx === 0);

  if (idx === total - 1) {
    btnNext.classList.add('hidden');
    btnFinish.classList.remove('hidden');
  } else {
    btnNext.classList.remove('hidden');
    btnFinish.classList.add('hidden');
  }

  // Paginator Pills
  renderExamPills();

  // MathJax typeset
  if (window.MathJax && window.MathJax.typesetPromise) {
    window.MathJax.typesetPromise();
  }
}

function renderExamPills() {
  const pillsContainer = document.getElementById('examPillsContainer');
  if (!pillsContainer) return;
  pillsContainer.innerHTML = '';

  const total = examSession.questions.length;
  for (let i = 0; i < total; i++) {
    const pill = document.createElement('button');
    pill.type = 'button';
    pill.className = 'w-7 h-7 rounded-lg text-xs font-bold transition flex items-center justify-center flex-shrink-0 ';

    const ans = examSession.userAnswers[i];
    const isCurrent = i === examSession.currentIndex;

    if (isCurrent) {
      pill.className += 'ring-2 ring-indigo-600 ring-offset-1 font-black ';
    }

    if (ans !== undefined) {
      if (examSession.mode === 'practice') {
        pill.className += ans.isCorrect ? 'bg-emerald-500 text-white' : 'bg-rose-500 text-white';
      } else {
        pill.className += 'bg-indigo-600 text-white';
      }
    } else {
      pill.className += 'bg-slate-100 text-slate-600 hover:bg-slate-200';
    }

    pill.textContent = (i + 1);
    pill.onclick = () => jumpToExamQuestion(i);
    pillsContainer.appendChild(pill);
  }
}

function selectExamOption(optIdx) {
  if (examSession.mode === 'practice' && examSession.userAnswers[examSession.currentIndex] !== undefined) {
    return; // Already answered in practice mode
  }

  const q = examSession.questions[examSession.currentIndex];
  examSession.userAnswers[examSession.currentIndex] = {
    selectedOptionIndex: optIdx,
    isCorrect: optIdx === q.correct_index
  };

  renderActiveQuestion();
}

function navigateExam(delta) {
  const newIndex = examSession.currentIndex + delta;
  if (newIndex >= 0 && newIndex < examSession.questions.length) {
    examSession.currentIndex = newIndex;
    renderActiveQuestion();
  }
}

function jumpToExamQuestion(targetIndex) {
  if (targetIndex >= 0 && targetIndex < examSession.questions.length) {
    examSession.currentIndex = targetIndex;
    renderActiveQuestion();
  }
}

function confirmCancelExam() {
  const msg = '¿Estás seguro de que deseas abandonar la sesión de examen actual? Se perderán las respuestas.';
  if (confirm(msg)) {
    if (examSession.timerInterval) clearInterval(examSession.timerInterval);
    document.getElementById('examActiveView')?.classList.add('hidden');
    document.getElementById('examResultsView')?.classList.add('hidden');
    document.getElementById('examConfigView')?.classList.remove('hidden');
    document.getElementById('examConfigView')?.scrollIntoView({ behavior: 'smooth' });
  }
}

function finishExamSession() {
  const total = examSession.questions.length;
  const answeredCount = Object.keys(examSession.userAnswers).length;
  const unansweredCount = total - answeredCount;

  if (unansweredCount > 0) {
    const confirmMsg = `Tienes ${unansweredCount} pregunta(s) sin responder de ${total}. ¿Deseas entregar el examen de todos modos?`;
    if (!confirm(confirmMsg)) return;
  }

  // Stop Timer
  if (examSession.timerInterval) clearInterval(examSession.timerInterval);
  examSession.isFinished = true;

  // Calculate results
  let correctCount = 0;
  for (let i = 0; i < total; i++) {
    const ans = examSession.userAnswers[i];
    if (ans && ans.isCorrect) correctCount++;
  }
  const incorrectCount = total - correctCount;
  const percentage = Math.round((correctCount / total) * 100);
  const grade = Math.round((correctCount / total) * 10 * 10) / 10;

  // Populate Scorecard
  document.getElementById('resStatTotal').textContent = total;
  document.getElementById('resStatCorrect').textContent = correctCount;
  document.getElementById('resStatIncorrect').textContent = incorrectCount;
  document.getElementById('resStatTime').textContent = formatTime(examSession.elapsedSeconds);

  // Diagnostic grading
  const badgeIcon = document.getElementById('examResultBadgeIcon');
  const levelBadge = document.getElementById('examResultLevel');
  const gradeTitle = document.getElementById('examResultGradeTitle');
  const subtext = document.getElementById('examResultSubtext');

  if (grade >= 9) {
    badgeIcon.className = 'w-20 h-20 mx-auto rounded-3xl flex items-center justify-center text-4xl shadow-lg bg-emerald-500 text-white';
    badgeIcon.innerHTML = '<i class="fa-solid fa-trophy"></i>';
    levelBadge.className = 'inline-block px-3 py-1 rounded-full text-xs font-extrabold uppercase tracking-wider mb-2 bg-emerald-100 text-emerald-800 border border-emerald-300';
    levelBadge.textContent = 'Sobresaliente / Nivel Distinguido';
    gradeTitle.textContent = `Calificación: ${grade} / 10 (${percentage}%)`;
    gradeTitle.className = 'text-3xl font-black text-emerald-700';
    subtext.textContent = '¡Rendimiento académico impecable! Demuestras un dominio profundo de los textos, deducciones teóricas y contraposiciones de la cátedra.';
  } else if (grade >= 7) {
    badgeIcon.className = 'w-20 h-20 mx-auto rounded-3xl flex items-center justify-center text-4xl shadow-lg bg-indigo-600 text-white';
    badgeIcon.innerHTML = '<i class="fa-solid fa-medal"></i>';
    levelBadge.className = 'inline-block px-3 py-1 rounded-full text-xs font-extrabold uppercase tracking-wider mb-2 bg-indigo-100 text-indigo-800 border border-indigo-300';
    levelBadge.textContent = 'Distinguido / Muy Buen Nivel';
    gradeTitle.textContent = `Calificación: ${grade} / 10 (${percentage}%)`;
    gradeTitle.className = 'text-3xl font-black text-indigo-800';
    subtext.textContent = 'Sólida preparación teórica. Comprendes con claridad los mecanismos centrales de transmisión y las diferencias doctrinales.';
  } else if (grade >= 6) {
    badgeIcon.className = 'w-20 h-20 mx-auto rounded-3xl flex items-center justify-center text-4xl shadow-lg bg-amber-500 text-white';
    badgeIcon.innerHTML = '<i class="fa-solid fa-check"></i>';
    levelBadge.className = 'inline-block px-3 py-1 rounded-full text-xs font-extrabold uppercase tracking-wider mb-2 bg-amber-100 text-amber-800 border border-amber-300';
    levelBadge.textContent = 'Aprobado (Umbral Universitario)';
    gradeTitle.textContent = `Calificación: ${grade} / 10 (${percentage}%)`;
    gradeTitle.className = 'text-3xl font-black text-amber-700';
    subtext.textContent = 'Has alcanzado los conocimientos indispensables para aprobar la materia, aunque se recomienda repasar los textos y detalles técnicos.';
  } else if (grade >= 4) {
    badgeIcon.className = 'w-20 h-20 mx-auto rounded-3xl flex items-center justify-center text-4xl shadow-lg bg-orange-500 text-white';
    badgeIcon.innerHTML = '<i class="fa-solid fa-triangle-exclamation"></i>';
    levelBadge.className = 'inline-block px-3 py-1 rounded-full text-xs font-extrabold uppercase tracking-wider mb-2 bg-orange-100 text-orange-800 border border-orange-300';
    levelBadge.textContent = 'Insuficiente / Recuperatorio';
    gradeTitle.textContent = `Calificación: ${grade} / 10 (${percentage}%)`;
    gradeTitle.className = 'text-3xl font-black text-orange-700';
    subtext.textContent = 'Se identifican confusiones conceptuales en supuestos analíticos clave. Utiliza la revisión inferior para repasar cada doctrina.';
  } else {
    badgeIcon.className = 'w-20 h-20 mx-auto rounded-3xl flex items-center justify-center text-4xl shadow-lg bg-rose-600 text-white';
    badgeIcon.innerHTML = '<i class="fa-solid fa-xmark"></i>';
    levelBadge.className = 'inline-block px-3 py-1 rounded-full text-xs font-extrabold uppercase tracking-wider mb-2 bg-rose-100 text-rose-800 border border-rose-300';
    levelBadge.textContent = 'Reprobado';
    gradeTitle.textContent = `Calificación: ${grade} / 10 (${percentage}%)`;
    gradeTitle.className = 'text-3xl font-black text-rose-700';
    subtext.textContent = 'No se alcanzan los objetivos teóricos mínimos. Es imprescindible estudiar a fondo las fichas por economista y los textos obligatorios.';
  }

  // Render Detailed Review List
  renderExamDetailedReview();

  // Switch to Results View
  document.getElementById('examActiveView')?.classList.add('hidden');
  document.getElementById('examResultsView')?.classList.remove('hidden');
  document.getElementById('examResultsView')?.scrollIntoView({ behavior: 'smooth' });

  // MathJax typeset
  if (window.MathJax && window.MathJax.typesetPromise) {
    window.MathJax.typesetPromise();
  }
}

function renderExamDetailedReview() {
  const container = document.getElementById('examReviewList');
  if (!container) return;
  container.innerHTML = '';

  const letters = ['A', 'B', 'C', 'D'];

  examSession.questions.forEach((q, idx) => {
    const ans = examSession.userAnswers[idx];
    const isAnswered = ans !== undefined;
    const isCorrect = isAnswered && ans.isCorrect;

    const card = document.createElement('div');
    card.className = `p-6 rounded-2xl border-2 transition ${
      !isAnswered
        ? 'bg-slate-50 border-slate-300'
        : isCorrect
        ? 'bg-emerald-50/40 border-emerald-300'
        : 'bg-rose-50/40 border-rose-300'
    }`;

    let statusBadge = '';
    if (!isAnswered) {
      statusBadge = '<span class="text-xs bg-slate-200 text-slate-700 font-bold px-2.5 py-1 rounded-full"><i class="fa-solid fa-circle-minus mr-1"></i> Sin Responder</span>';
    } else if (isCorrect) {
      statusBadge = '<span class="text-xs bg-emerald-100 text-emerald-800 font-bold px-2.5 py-1 rounded-full border border-emerald-300"><i class="fa-solid fa-check mr-1"></i> Correcta</span>';
    } else {
      statusBadge = '<span class="text-xs bg-rose-100 text-rose-800 font-bold px-2.5 py-1 rounded-full border border-rose-300"><i class="fa-solid fa-xmark mr-1"></i> Incorrecta</span>';
    }

    let optionsHtml = '<div class="space-y-2 mt-4">';
    q.options.forEach((optText, optIdx) => {
      const isSelected = isAnswered && ans.selectedOptionIndex === optIdx;
      const isTheRightOption = optIdx === q.correct_index;

      let rowClass = 'p-3 rounded-xl border text-xs leading-relaxed flex items-start gap-2.5 ';
      let icon = '';

      if (isTheRightOption) {
        rowClass += 'bg-emerald-100/70 border-emerald-400 font-bold text-emerald-950 shadow-xs';
        icon = '<i class="fa-solid fa-circle-check text-emerald-600 text-sm mt-0.5 flex-shrink-0"></i>';
      } else if (isSelected && !isTheRightOption) {
        rowClass += 'bg-rose-100/70 border-rose-400 text-rose-950 line-through';
        icon = '<i class="fa-solid fa-circle-xmark text-rose-600 text-sm mt-0.5 flex-shrink-0"></i>';
      } else {
        rowClass += 'bg-white border-slate-200 text-slate-600';
        icon = `<span class="w-5 h-5 rounded bg-slate-100 text-slate-500 font-bold text-[10px] flex items-center justify-center flex-shrink-0">${letters[optIdx]}</span>`;
      }

      optionsHtml += `
        <div class="${rowClass}">
          ${icon}
          <div>
            <span class="font-bold mr-1">${letters[optIdx]}.</span>
            <span>${optText}</span>
            ${isSelected ? ' <span class="text-[10px] font-black uppercase text-indigo-700 bg-indigo-50 px-1.5 py-0.5 rounded ml-1 border border-indigo-200">(Tu Elección)</span>' : ''}
            ${isTheRightOption ? ' <span class="text-[10px] font-black uppercase text-emerald-800 bg-emerald-200/80 px-1.5 py-0.5 rounded ml-1">(Correcta)</span>' : ''}
          </div>
        </div>
      `;
    });
    optionsHtml += '</div>';

    card.innerHTML = `
      <div class="flex flex-wrap items-center justify-between gap-2 border-b border-slate-200/60 pb-3 mb-3">
        <div class="flex items-center gap-2">
          <span class="w-7 h-7 rounded-lg bg-indigo-900 text-amber-300 font-bold text-xs flex items-center justify-center">
            ${idx + 1}
          </span>
          <span class="text-xs font-bold text-indigo-900">${q.econName}</span>
          <span class="text-slate-400">&bull;</span>
          <span class="text-xs text-slate-600">${q.econSchool}</span>
        </div>
        ${statusBadge}
      </div>

      <h5 class="text-sm font-bold text-slate-900 leading-snug">
        ${q.question}
      </h5>

      ${optionsHtml}

      <!-- Justification Box -->
      <div class="mt-4 p-4 rounded-xl bg-white border border-slate-200 text-xs text-slate-800 shadow-xs">
        <div class="font-bold text-indigo-950 flex items-center gap-1.5 mb-1.5">
          <i class="fa-solid fa-graduation-cap text-indigo-600"></i>
          Justificación Teórica y Referencia Doctrinal:
        </div>
        <p class="leading-relaxed text-slate-700 font-sans">${q.explanation}</p>
      </div>
    `;

    container.appendChild(card);
  });
}

function resetExamToConfig() {
  document.getElementById('examResultsView')?.classList.add('hidden');
  document.getElementById('examActiveView')?.classList.add('hidden');
  document.getElementById('examConfigView')?.classList.remove('hidden');
  document.getElementById('examConfigView')?.scrollIntoView({ behavior: 'smooth' });
}

function restartCurrentExam() {
  // Restart with same questions or reshuffled
  startExamSession();
}

// ====================================================
// TAB: CLAVES PARA EL EXAMEN UNIVERSITARIO
// ====================================================

function initExamKeysTab() {
  if (!window.BANKING_DATA || !window.BANKING_DATA.exam_keys) {
    console.warn('Exam keys data not loaded');
    return;
  }

  const econSelect = document.getElementById('examKeysEconomistFilter');
  if (econSelect) {
    econSelect.innerHTML = '<option value="all">🌟 Todos los Economistas (14 Claves)</option>';
    const seenEcons = new Set();
    window.BANKING_DATA.exam_keys.forEach(k => {
      if (!seenEcons.has(k.economist_id)) {
        seenEcons.add(k.economist_id);
        const opt = document.createElement('option');
        opt.value = k.economist_id;
        opt.textContent = `${k.economist_name} (${k.school})`;
        econSelect.appendChild(opt);
      }
    });
  }

  const topicSelect = document.getElementById('examKeysTopicFilter');
  if (topicSelect && window.BANKING_DATA.topics) {
    topicSelect.innerHTML = '<option value="all">🌟 Todos los Ejes Temáticos</option>';
    window.BANKING_DATA.topics.forEach(t => {
      const opt = document.createElement('option');
      opt.value = t.id;
      opt.textContent = t.name;
      topicSelect.appendChild(opt);
    });
  }

  renderExamKeys();
}

function filterExamKeys() {
  const search = document.getElementById('examKeysSearchInput')?.value.toLowerCase().trim() || '';
  const selectedEcon = document.getElementById('examKeysEconomistFilter')?.value || 'all';
  const selectedTopic = document.getElementById('examKeysTopicFilter')?.value || 'all';

  if (!window.BANKING_DATA || !window.BANKING_DATA.exam_keys) return;

  const filtered = window.BANKING_DATA.exam_keys.filter(k => {
    // Economist filter
    if (selectedEcon !== 'all' && k.economist_id !== selectedEcon) return false;
    // Topic filter
    if (selectedTopic !== 'all' && k.topic_id !== selectedTopic) return false;
    // Search text
    if (search) {
      const match = k.title.toLowerCase().includes(search) ||
                    k.economist_name.toLowerCase().includes(search) ||
                    k.school.toLowerCase().includes(search) ||
                    k.the_key.toLowerCase().includes(search) ||
                    k.why_is_key.toLowerCase().includes(search) ||
                    k.typical_exam_trap.toLowerCase().includes(search) ||
                    k.university_answer.toLowerCase().includes(search) ||
                    k.theoretical_mechanism.toLowerCase().includes(search);
      if (!match) return false;
    }
    return true;
  });

  renderExamKeys(filtered);
}

function resetExamKeysFilters() {
  const searchInput = document.getElementById('examKeysSearchInput');
  const econFilter = document.getElementById('examKeysEconomistFilter');
  const topicFilter = document.getElementById('examKeysTopicFilter');

  if (searchInput) searchInput.value = '';
  if (econFilter) econFilter.value = 'all';
  if (topicFilter) topicFilter.value = 'all';

  renderExamKeys();
}

function renderExamKeys(list = null) {
  const container = document.getElementById('examKeysContainer');
  const counter = document.getElementById('examKeysCounterText');
  if (!container) return;

  const keys = list !== null ? list : (window.BANKING_DATA?.exam_keys || []);
  const total = window.BANKING_DATA?.exam_keys?.length || 14;

  if (counter) {
    counter.textContent = `Mostrando ${keys.length} de ${total} Claves de Examen`;
  }

  if (keys.length === 0) {
    container.innerHTML = `
      <div class="bg-white p-12 rounded-2xl text-center text-slate-500 border border-slate-200">
        <i class="fa-solid fa-magnifying-glass text-3xl text-slate-300 mb-3 block"></i>
        <h4 class="font-bold text-slate-800 text-base">No se encontraron claves con los filtros seleccionados</h4>
        <p class="text-xs text-slate-500 mt-1">Prueba restableciendo los filtros o buscando con términos más amplios.</p>
        <button onclick="resetExamKeysFilters()" class="mt-4 px-4 py-2 bg-indigo-600 text-white rounded-xl text-xs font-bold hover:bg-indigo-700 transition">
          Restablecer Filtros
        </button>
      </div>
    `;
    return;
  }

  let html = '';
  keys.forEach(k => {
    let sourceBadges = '';
    k.source_texts.forEach(txt => {
      sourceBadges += `<span class="bg-slate-100 text-slate-700 font-mono text-[11px] px-2.5 py-0.5 rounded border border-slate-200">${txt}</span>`;
    });

    html += `
      <div class="bg-white rounded-2xl shadow-sm border border-slate-200 overflow-hidden card-hover transition-all">
        <!-- Card Header -->
        <div class="p-6 bg-slate-50 border-b border-slate-200">
          <div class="flex flex-wrap items-center justify-between gap-3 mb-3">
            <div class="flex flex-wrap items-center gap-2">
              <span class="w-8 h-8 rounded-xl bg-amber-400 text-slate-950 font-black text-xs flex items-center justify-center shadow">
                #${k.number}
              </span>
              <span class="bg-indigo-900 text-amber-300 px-3 py-1 rounded-full text-xs font-extrabold flex items-center gap-1.5 shadow-xs">
                <i class="fa-solid fa-user-tie text-[10px]"></i> ${k.economist_name}
              </span>
              <span class="bg-indigo-100 text-indigo-900 px-2.5 py-1 rounded-full text-xs font-semibold">
                ${k.school}
              </span>
              <span class="bg-slate-200 text-slate-800 px-2.5 py-1 rounded-full text-xs font-medium">
                ${k.topic_name}
              </span>
            </div>
            <div class="flex flex-wrap items-center gap-2">
              <button onclick="toggleAudioReader('exam_key', '${k.id}')" id="btnAudio-exam_key-${k.id}" class="text-xs bg-amber-400 hover:bg-amber-500 text-slate-950 font-black px-3 py-1.5 rounded-xl shadow transition flex items-center gap-1.5 btn-audio-card" title="Escuchar clave de examen con voz femenina">
                <i class="fa-solid fa-microphone-lines text-slate-950"></i> <span class="audio-label">Escuchar Clave</span>
              </button>
              <button onclick="launchExamForEconomist('${k.economist_id}')" class="text-xs bg-indigo-600 hover:bg-indigo-700 text-white font-bold px-3 py-1.5 rounded-xl shadow transition flex items-center gap-1.5">
                <i class="fa-solid fa-graduation-cap text-amber-300"></i> Rendir Examen (20 Preguntas)
              </button>
            </div>
          </div>

          <h4 class="text-lg sm:text-xl font-black text-indigo-950 leading-snug">
            ${k.title}
          </h4>

          <div class="mt-3 flex flex-wrap items-center gap-1.5 text-xs text-slate-500">
            <span class="font-bold text-slate-600 uppercase tracking-wider text-[10px]">Fuentes Obligatorias:</span>
            ${sourceBadges}
          </div>
        </div>

        <div class="p-6 space-y-5">
          <!-- 1. Tesis / La Clave Doctrinal -->
          <div class="p-4 rounded-xl bg-indigo-50/50 border border-indigo-100">
            <div class="flex items-center gap-2 text-xs font-black uppercase tracking-wider text-indigo-950 mb-1.5">
              <i class="fa-solid fa-quote-left text-indigo-600"></i>
              La Tesis Central / Postulado Doctrinal:
            </div>
            <p class="text-xs sm:text-sm text-slate-800 font-medium leading-relaxed">
              ${k.the_key}
            </p>
          </div>

          <!-- 2. ¿Por Qué es Clave para el Examen? -->
          <div class="p-5 rounded-xl bg-amber-50/80 border-2 border-amber-300 text-xs sm:text-sm">
            <div class="flex items-center gap-2 font-black text-amber-950 text-sm mb-2">
              <span class="w-6 h-6 rounded-lg bg-amber-500 text-white flex items-center justify-center text-xs shadow-xs">
                <i class="fa-solid fa-bullseye"></i>
              </span>
              <span>¿Por Qué es Clave para el Examen? (Criterio de Evaluación Docente):</span>
            </div>
            <p class="text-slate-800 leading-relaxed font-sans">
              ${k.why_is_key}
            </p>
          </div>

          <!-- Grid: Trampa Habitual vs Respuesta de Nivel 10 -->
          <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
            <!-- Trampa Habitual -->
            <div class="p-5 rounded-xl bg-rose-50/70 border-2 border-rose-300 text-xs">
              <div class="flex items-center gap-2 font-black text-rose-950 text-xs sm:text-sm mb-2">
                <span class="w-6 h-6 rounded-lg bg-rose-500 text-white flex items-center justify-center text-xs shadow-xs">
                  <i class="fa-solid fa-triangle-exclamation"></i>
                </span>
                <span>⚠️ Trampa Habitual (Error Típico del Estudiante):</span>
              </div>
              <p class="text-slate-700 leading-relaxed font-sans">
                ${k.typical_exam_trap}
              </p>
            </div>

            <!-- Respuesta de Nivel 10 -->
            <div class="p-5 rounded-xl bg-emerald-50/70 border-2 border-emerald-300 text-xs">
              <div class="flex items-center gap-2 font-black text-emerald-950 text-xs sm:text-sm mb-2">
                <span class="w-6 h-6 rounded-lg bg-emerald-600 text-white flex items-center justify-center text-xs shadow-xs">
                  <i class="fa-solid fa-award"></i>
                </span>
                <span>🎓 Respuesta de Nivel 10 Universitario:</span>
              </div>
              <p class="text-slate-800 leading-relaxed font-sans font-medium">
                ${k.university_answer}
              </p>
            </div>
          </div>

          <!-- 3. Mecanismo Analítico y Fórmulas -->
          <div class="p-5 rounded-xl bg-slate-900 text-slate-100 text-xs">
            <div class="flex items-center justify-between mb-2">
              <div class="flex items-center gap-2 font-bold text-amber-300 uppercase tracking-wider text-[11px]">
                <i class="fa-solid fa-gears text-amber-400"></i>
                Mecanismo Analítico y Deducción Formal / Fórmula:
              </div>
              <span class="text-[10px] text-slate-400 font-mono">Formalización de Cátedra</span>
            </div>
            <div class="leading-relaxed text-slate-200 font-mono text-xs sm:text-[13px] bg-slate-950/70 p-3.5 rounded-lg border border-slate-800">
              ${k.theoretical_mechanism}
            </div>
          </div>

          <!-- 4. Contraste Doctrinal Obligatorio -->
          <div class="p-4 rounded-xl bg-slate-50 border border-slate-200 text-xs flex items-start gap-3">
            <div class="w-7 h-7 rounded-lg bg-indigo-100 text-indigo-800 font-bold flex items-center justify-center flex-shrink-0 mt-0.5">
              <i class="fa-solid fa-code-compare"></i>
            </div>
            <div>
              <div class="font-bold text-indigo-950 mb-0.5">Contraste Doctrinal Obligatorio:</div>
              <p class="text-slate-600 leading-relaxed">${k.doctrinal_contrast}</p>
            </div>
          </div>
        </div>

        <!-- Card Footer -->
        <div class="p-4 bg-slate-50 border-t border-slate-200 flex flex-wrap items-center justify-between gap-3">
          <div class="text-xs text-slate-500 font-medium">
            <i class="fa-solid fa-circle-info text-indigo-600 mr-1"></i> Prepara esta clave para preguntas a desarrollar y multiple choice.
          </div>
          <div class="flex flex-wrap items-center gap-2">
            <button onclick="toggleAudioReader('exam_key', '${k.id}')" class="px-3.5 py-2 bg-amber-400 hover:bg-amber-500 text-slate-950 rounded-xl text-xs font-black transition flex items-center gap-1.5 shadow-sm" title="Escuchar explicación con voz femenina">
              <i class="fa-solid fa-microphone-lines"></i> Escuchar Explicación
            </button>
            <button onclick="launchExamForEconomist('${k.economist_id}')" class="px-4 py-2 bg-indigo-600 hover:bg-indigo-700 text-white rounded-xl text-xs font-bold transition flex items-center gap-1.5 shadow-sm">
              <i class="fa-solid fa-play"></i> Practicar este Autor en Examen
            </button>
          </div>
        </div>
      </div>
    `;
  });

  container.innerHTML = html;

  if (window.MathJax && window.MathJax.typesetPromise) {
    window.MathJax.typesetPromise();
  }
}

// ====================================================
// MOTOR DE AUDIO TEXT-TO-SPEECH (VOZ FEMENINA & VELOCIDAD)
// ====================================================

let audioPlayerState = {
  activeType: null,      // 'economist' | 'exam_key'
  activeId: null,        // 'friedman' | 'clave_1_friedman_inflacion'
  chunks: [],
  currentChunkIndex: 0,
  isPlaying: false,
  isPaused: false,
  speed: 1.0,
  voice: null,
  title: '',
  typeLabel: ''
};

function initSpeechEngine() {
  if (!('speechSynthesis' in window)) {
    console.warn('Web Speech API no está soportada en este navegador.');
    return;
  }

  const loadVoices = () => {
    audioPlayerState.voice = getFemaleSpanishVoice();
  };

  loadVoices();
  if (window.speechSynthesis.onvoiceschanged !== undefined) {
    window.speechSynthesis.onvoiceschanged = loadVoices;
  }
}

function getFemaleSpanishVoice() {
  const synth = window.speechSynthesis;
  if (!synth) return null;
  const voices = synth.getVoices();
  if (!voices || voices.length === 0) return null;

  // Filter for Spanish voices
  const spanishVoices = voices.filter(v => v.lang && v.lang.toLowerCase().startsWith('es'));
  if (spanishVoices.length === 0) return voices[0];

  const femaleKeywords = [
    'helena', 'sabina', 'laura', 'monica', 'mónica', 'paulina', 
    'francisca', 'penelope', 'penélope', 'elena', 'lucia', 'lucía', 
    'mia', 'mía', 'hilda', 'carmen', 'paloma', 'maria', 'maría', 
    'sofia', 'sofía', 'rosa', 'victoria', 'female', 'mujer', 'zira'
  ];

  for (const v of spanishVoices) {
    const nameLower = v.name.toLowerCase();
    if (femaleKeywords.some(kw => nameLower.includes(kw))) {
      return v;
    }
  }

  // Look for Google español
  const googleVoice = spanishVoices.find(v => v.name.toLowerCase().includes('google'));
  if (googleVoice) return googleVoice;

  // Fallback to first Spanish voice
  return spanishVoices[0];
}

function cleanMathForSpeech(text) {
  if (!text) return '';
  return text
    .replace(/\\\(/g, '')
    .replace(/\\\)/g, '')
    .replace(/\\\[/g, '')
    .replace(/\\\]/g, '')
    .replace(/\\pi\^?\*?/g, ' pi ')
    .replace(/\\alpha/g, ' alfa ')
    .replace(/\\beta/g, ' beta ')
    .replace(/\\omega/g, ' omega ')
    .replace(/\\mu/g, ' mu ')
    .replace(/\\varepsilon/g, ' épsilon ')
    .replace(/\\Delta/g, ' variación de ')
    .replace(/\\dot\{P\}/g, ' tasa de inflación ')
    .replace(/\\dot\{M\}/g, ' crecimiento monetario ')
    .replace(/\\dot\{V\}/g, ' variación de velocidad ')
    .replace(/\\dot\{Y\}/g, ' crecimiento del producto ')
    .replace(/\\approx/g, ' aproximadamente igual a ')
    .replace(/\\neq/g, ' distinto de ')
    .replace(/\\to/g, ' tiende a ')
    .replace(/\\implies/g, ' lo que implica que ')
    .replace(/\\uparrow/g, ' sube ')
    .replace(/\\downarrow/g, ' baja ')
    .replace(/\\partial/g, ' derivada parcial de ')
    .replace(/1\/\\alpha/g, ' uno sobre alfa ')
    .replace(/\\frac\{([^}]+)\}\{([^}]+)\}/g, '$1 sobre $2')
    .replace(/M\/P/g, ' saldos reales M sobre P ')
    .replace(/Y_p/g, ' ingreso permanente ')
    .replace(/M_1/g, ' M uno ')
    .replace(/M_2/g, ' M dos ')
    .replace(/[*_#`]/g, ' ')
    .replace(/\s+/g, ' ')
    .trim();
}

function splitTextIntoSentenceChunks(text) {
  const rawSentences = text
    .replace(/([.?!;])\s+/g, '$1|')
    .replace(/\n+/g, '|')
    .split('|');

  const chunks = [];
  let current = '';

  for (const s of rawSentences) {
    const trimmed = s.trim();
    if (!trimmed) continue;
    if (current.length + trimmed.length < 220) {
      current += (current ? ' ' : '') + trimmed;
    } else {
      if (current) chunks.push(current);
      current = trimmed;
    }
  }
  if (current) chunks.push(current);

  return chunks;
}

function buildEconomistAudioScript(econId) {
  const econ = window.BANKING_DATA?.economists.find(e => e.id === econId);
  if (!econ) return null;

  let text = `Economista: ${econ.name}. `;
  text += `Escuela: ${econ.school}. `;
  text += `Época: ${econ.epoch}. `;
  text += `Contexto: ${cleanMathForSpeech(econ.context)}. `;

  if (econ.primary_texts && econ.primary_texts.length > 0) {
    text += `Textos analizados de la cátedra: ${econ.primary_texts.join(', ')}. `;
  }

  text += `A continuación, las posturas teóricas de ${econ.name} para el examen universitario. `;

  window.BANKING_DATA.topics.forEach(t => {
    const stance = econ.stances[t.id] || '';
    if (!stance.includes('[No aborda')) {
      text += `Sobre ${t.name}: ${cleanMathForSpeech(stance)}. `;
    }
  });

  text += `Fin de la exposición completa de ${econ.name}.`;
  return { title: econ.name, typeLabel: 'Economista', text };
}

function buildExamKeyAudioScript(keyId) {
  const k = window.BANKING_DATA?.exam_keys.find(item => item.id === keyId);
  if (!k) return null;

  let text = `Clave número ${k.number} para el examen universitario. `;
  text += `Título: ${k.title}. `;
  text += `Economista: ${k.economist_name}. Escuela: ${k.school}. `;
  text += `Eje temático: ${k.topic_name}. `;
  text += `Tesis central: ${cleanMathForSpeech(k.the_key)}. `;
  text += `¿Por qué es clave para el examen?: ${cleanMathForSpeech(k.why_is_key)}. `;
  text += `Atención, trampa habitual en los exámenes: ${cleanMathForSpeech(k.typical_exam_trap)}. `;
  text += `Respuesta de nivel diez universitario esperada por la cátedra: ${cleanMathForSpeech(k.university_answer)}. `;
  text += `Mecanismo analítico y deducción formal: ${cleanMathForSpeech(k.theoretical_mechanism)}. `;
  text += `Contraste doctrinal obligatorio: ${cleanMathForSpeech(k.doctrinal_contrast)}. `;
  text += `Fin de la clave número ${k.number}.`;

  return { title: `Clave #${k.number}: ${k.economist_name}`, typeLabel: 'Clave de Examen', text };
}

function toggleAudioReader(type, id) {
  if (!('speechSynthesis' in window)) {
    alert('Tu navegador no soporta síntesis de voz (Text-to-Speech). Se recomienda usar Google Chrome, Microsoft Edge o Safari.');
    return;
  }

  // If already playing this item, stop it
  if (audioPlayerState.isPlaying && audioPlayerState.activeType === type && audioPlayerState.activeId === id) {
    stopAudioReader();
    return;
  }

  // Otherwise, start playing this item
  startAudioReader(type, id);
}

function startAudioReader(type, id) {
  stopAudioReader(); // Cancel any existing speech

  let scriptData = null;
  if (type === 'economist') {
    scriptData = buildEconomistAudioScript(id);
  } else if (type === 'exam_key') {
    scriptData = buildExamKeyAudioScript(id);
  }

  if (!scriptData || !scriptData.text) return;

  const chunks = splitTextIntoSentenceChunks(scriptData.text);
  if (chunks.length === 0) return;

  if (!audioPlayerState.voice) {
    audioPlayerState.voice = getFemaleSpanishVoice();
  }

  audioPlayerState.activeType = type;
  audioPlayerState.activeId = id;
  audioPlayerState.chunks = chunks;
  audioPlayerState.currentChunkIndex = 0;
  audioPlayerState.isPlaying = true;
  audioPlayerState.isPaused = false;
  audioPlayerState.title = scriptData.title;
  audioPlayerState.typeLabel = scriptData.typeLabel;

  // Show floating audio bar
  showAudioPlayerBar(scriptData.title, scriptData.typeLabel);

  // Update card buttons
  updateCardAudioButtons();

  // Start speech
  playCurrentAudioChunk();
}

function playCurrentAudioChunk() {
  const synth = window.speechSynthesis;
  if (!synth) return;

  // Check if finished
  if (audioPlayerState.currentChunkIndex >= audioPlayerState.chunks.length) {
    stopAudioReader();
    return;
  }

  const chunkText = audioPlayerState.chunks[audioPlayerState.currentChunkIndex];
  const utterance = new SpeechSynthesisUtterance(chunkText);

  if (audioPlayerState.voice) {
    utterance.voice = audioPlayerState.voice;
  }
  utterance.lang = 'es-ES';
  utterance.pitch = 1.15; // Feminine pitch
  utterance.rate = audioPlayerState.speed || 1.0;

  utterance.onend = () => {
    if (audioPlayerState.isPlaying && !audioPlayerState.isPaused) {
      audioPlayerState.currentChunkIndex++;
      playCurrentAudioChunk();
    }
  };

  utterance.onerror = (e) => {
    console.warn('Utterance error:', e);
    if (audioPlayerState.isPlaying && !audioPlayerState.isPaused) {
      audioPlayerState.currentChunkIndex++;
      playCurrentAudioChunk();
    }
  };

  synth.speak(utterance);
}

function togglePauseResumeAudio() {
  const synth = window.speechSynthesis;
  if (!synth || !audioPlayerState.isPlaying) return;

  const btn = document.getElementById('btnAudioPauseResume');

  if (audioPlayerState.isPaused) {
    synth.resume();
    audioPlayerState.isPaused = false;
    if (btn) btn.innerHTML = '<i class="fa-solid fa-pause"></i>';
    document.getElementById('audioWaveIcon')?.classList.add('animate-pulse');
  } else {
    synth.pause();
    audioPlayerState.isPaused = true;
    if (btn) btn.innerHTML = '<i class="fa-solid fa-play"></i>';
    document.getElementById('audioWaveIcon')?.classList.remove('animate-pulse');
  }
}

function stopAudioReader() {
  const synth = window.speechSynthesis;
  if (synth) synth.cancel();

  audioPlayerState.isPlaying = false;
  audioPlayerState.isPaused = false;
  audioPlayerState.activeType = null;
  audioPlayerState.activeId = null;
  audioPlayerState.chunks = [];
  audioPlayerState.currentChunkIndex = 0;

  hideAudioPlayerBar();
  updateCardAudioButtons();
}

function setAudioSpeed(newSpeed) {
  audioPlayerState.speed = newSpeed;

  // Update pills styling
  document.querySelectorAll('.speed-pill').forEach(btn => {
    btn.classList.remove('bg-amber-400', 'text-slate-950', 'shadow');
    btn.classList.add('text-slate-300');
  });

  const activeBtn = document.getElementById(`btnSpeed-${newSpeed}`);
  if (activeBtn) {
    activeBtn.classList.remove('text-slate-300');
    activeBtn.classList.add('bg-amber-400', 'text-slate-950', 'shadow');
  }

  // If currently speaking, restart current chunk with new speed seamlessly
  if (audioPlayerState.isPlaying && !audioPlayerState.isPaused) {
    const synth = window.speechSynthesis;
    if (synth) {
      synth.cancel();
      playCurrentAudioChunk();
    }
  }
}

function showAudioPlayerBar(title, typeLabel) {
  const bar = document.getElementById('globalAudioPlayerBar');
  if (!bar) return;

  document.getElementById('audioPlayingTitle').textContent = title;
  document.getElementById('audioPlayingTypeBadge').textContent = typeLabel;
  document.getElementById('btnAudioPauseResume').innerHTML = '<i class="fa-solid fa-pause"></i>';
  document.getElementById('audioWaveIcon')?.classList.add('animate-pulse');

  bar.classList.remove('translate-y-36', 'opacity-0', 'pointer-events-none');
  bar.classList.add('translate-y-0', 'opacity-100', 'pointer-events-auto');
}

function hideAudioPlayerBar() {
  const bar = document.getElementById('globalAudioPlayerBar');
  if (!bar) return;

  bar.classList.add('translate-y-36', 'opacity-0', 'pointer-events-none');
  bar.classList.remove('translate-y-0', 'opacity-100', 'pointer-events-auto');
}

function updateCardAudioButtons() {
  // Reset all audio buttons to default "Escuchar"
  document.querySelectorAll('.btn-audio-card').forEach(btn => {
    btn.classList.remove('bg-rose-600', 'hover:bg-rose-700', 'text-white');
    btn.classList.add('bg-amber-400', 'hover:bg-amber-500', 'text-slate-950');
    const label = btn.querySelector('.audio-label');
    if (label) {
      label.textContent = btn.id.includes('exam_key') ? 'Escuchar Clave' : 'Escuchar';
    }
    const icon = btn.querySelector('i');
    if (icon) {
      icon.className = 'fa-solid fa-microphone-lines text-slate-950';
    }
  });

  // If currently playing, set active button to "Detener"
  if (audioPlayerState.isPlaying && audioPlayerState.activeType && audioPlayerState.activeId) {
    const activeBtnId = `btnAudio-${audioPlayerState.activeType}-${audioPlayerState.activeId}`;
    const activeBtn = document.getElementById(activeBtnId);
    if (activeBtn) {
      activeBtn.classList.remove('bg-amber-400', 'hover:bg-amber-500', 'text-slate-950');
      activeBtn.classList.add('bg-rose-600', 'hover:bg-rose-700', 'text-white');
      const label = activeBtn.querySelector('.audio-label');
      if (label) label.textContent = 'Detener';
      const icon = activeBtn.querySelector('i');
      if (icon) icon.className = 'fa-solid fa-stop text-white';
    }
  }
}
