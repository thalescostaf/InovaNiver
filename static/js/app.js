/* ====================================================
   InovaNiver — App JavaScript
   ==================================================== */

// ─── MODAL ──────────────────────────────────────────

function openModal() {
    document.getElementById('modal-overlay').classList.remove('hidden');
    document.body.style.overflow = 'hidden';
}

function closeModal() {
    document.getElementById('modal-overlay').classList.add('hidden');
    document.body.style.overflow = '';
    document.getElementById('modal-content').innerHTML = '';
}

// Abre modal de adição (clona template do HTML)
function openAddModal() {
    const template = document.getElementById('form-add-template');
    if (!template) return;
    const clone = template.content.cloneNode(true);

    // Sincroniza o mês escondido do form com o mês atual
    const mesAtual = document.getElementById('mes-hidden').value;
    const mesInput = clone.getElementById ? clone.getElementById('form-add-mes') :
                     clone.querySelector('#form-add-mes');
    if (mesInput) mesInput.value = mesAtual;

    const content = document.getElementById('modal-content');
    content.innerHTML = '';
    content.appendChild(clone);

    // Processa os atributos htmx no conteúdo recém-inserido
    if (window.htmx) htmx.process(content);

    openModal();
}

// Fecha modal ao clicar no overlay (fora do box)
document.addEventListener('DOMContentLoaded', () => {
    const overlay = document.getElementById('modal-overlay');
    overlay.addEventListener('click', (e) => {
        if (e.target === overlay) closeModal();
    });

    // Fecha modal com ESC
    document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape') closeModal();
    });
});

// ─── SINCRONIZAÇÃO DO MÊS ───────────────────────────

function updateMes(valor) {
    // Atualiza o campo hidden usado pelos forms e requisições
    const hidden = document.getElementById('mes-hidden');
    if (hidden) hidden.value = valor;
}

// ─── TOAST ──────────────────────────────────────────

function showToast(msg) {
    let toast = document.getElementById('toast');
    if (!toast) {
        toast = document.createElement('div');
        toast.id = 'toast';
        document.body.appendChild(toast);
    }
    toast.textContent = msg;
    toast.classList.add('show');
    setTimeout(() => toast.classList.remove('show'), 2800);
}

// ─── COPIAR MENSAGEM DE PARABÉNS ───────────────────

function copiarParabens(nome) {
    const msg = `🎂 Parabéns, ${nome}! Desejamos a você um feliz aniversário, muita saúde e conquistas! 🎉`;
    navigator.clipboard.writeText(msg).then(() => {
        showToast('Mensagem copiada para a área de transferência!');
    }).catch(() => {
        // fallback para navegadores sem suporte
        const el = document.createElement('textarea');
        el.value = msg;
        el.style.position = 'fixed';
        el.style.opacity = '0';
        document.body.appendChild(el);
        el.select();
        document.execCommand('copy');
        document.body.removeChild(el);
        showToast('Mensagem copiada!');
    });
}

// ─── HTMX: após atualizar tabela, re-processa HTMX ─

document.addEventListener('htmx:afterSwap', (e) => {
    if (e.detail.target.id === 'tabela-container') {
        // sincroniza o select de mês visível com o hidden
        const hidden = document.getElementById('mes-hidden');
        const select = document.getElementById('mes-select');
        if (hidden && select && hidden.value !== select.value) {
            select.value = hidden.value;
        }
    }
});

// ─── SELECT MÊS: passa o valor no parâmetro hx-vals ─
// O select usa hx-include="[name='mes']" para incluir o campo hidden,
// mas também precisamos passar o valor do select como "mes".
// Solução: sobrescrever via hx-vals dinâmico.

document.addEventListener('DOMContentLoaded', () => {
    const select = document.getElementById('mes-select');
    if (!select) return;

    select.addEventListener('change', () => {
        updateMes(select.value);
        // hx-get já é acionado pelo htmx via "change" event, passará o hidden via hx-include
    });
});
