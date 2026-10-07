// app.js - Interactive application logic for Sistemas Bancarios y Teoría Monetaria

let currentTab = 'tab-matriz';
let isMatrixInverted = false; // false: Economists as rows, Topics as cols. true: Topics as rows, Economists as cols.

document.addEventListener('DOMContentLoaded', () => {
  initApp();
});

function initApp() {
  if (!window.BANKING_DATA) {
    console.error('Data not loaded');
    return;
  }

  // Populate filter dropdowns
  populateMatrixFilters();

  // Render all views
  renderMatrix();
  initFilterTab();
  renderEconomistsList();
  renderTextsList();
  renderDeepDive();

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

          <div class="mt-3 bg-slate-50 p-3.5 rounded-xl border border-slate-200 text-xs text-slate-800 leading-relaxed font-sans">
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

      topicsHtml += `<div class="p-3.5 rounded-xl border ${isExcluded ? 'bg-slate-50 border-slate-200 text-slate-500' : 'bg-indigo-50/40 border-indigo-100 text-slate-800'}">
        <div class="flex items-center justify-between mb-1.5">
          <span class="font-bold text-xs ${isExcluded ? 'text-slate-600' : 'text-indigo-950'} flex items-center gap-1.5">
            <i class="fa-solid ${isExcluded ? 'fa-minus text-slate-400' : 'fa-check text-emerald-600'} text-[10px]"></i>
            ${t.name}
          </span>
          <span class="text-[10px] ${isExcluded ? 'text-slate-400 italic' : 'bg-indigo-100 text-indigo-700 font-semibold px-2 py-0.5 rounded-full'}">
            ${isExcluded ? 'No abordado' : 'Abordado'}
          </span>
        </div>
        <p class="text-xs leading-relaxed ${isExcluded ? 'italic text-slate-500 text-[11px]' : ''}">
          ${stance}
        </p>
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
        <div class="flex items-center gap-2 flex-shrink-0">
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
        matches.push({ type: 'Postura', title: `${e.name} en ${t.name}`, subtitle: stance.substring(0, 110) + '...', tab: 'tab-matriz', econId: e.id, topicId: t.id });
      }
    });
  });

  // Search in texts
  window.BANKING_DATA.texts.forEach(txt => {
    if (txt.title.toLowerCase().includes(q) || txt.author.toLowerCase().includes(q) || txt.summary.toLowerCase().includes(q)) {
      matches.push({ type: 'Texto', title: txt.title, subtitle: `${txt.author} (${txt.year}) - ${txt.category}`, tab: 'tab-textos' });
    }
  });

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
