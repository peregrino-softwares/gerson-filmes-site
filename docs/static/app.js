/* Gerson Filmes — comportamentos da interface */
(() => {
  'use strict';

  const raiz = document.documentElement;
  const semMovimento = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* --------------------------------------------------- Cabeçalho */
  const topo = document.querySelector('[data-topo]');
  const atualizaTopo = () => topo?.classList.toggle('encolhido', window.scrollY > 30);
  atualizaTopo();
  window.addEventListener('scroll', atualizaTopo, { passive: true });

  /* -------------------------------------------------- Menu móvel */
  const menu = document.querySelector('[data-menu-movel]');
  const abrir = document.querySelector('[data-abrir]');
  const fechar = document.querySelector('[data-fechar]');

  const defineMenu = (aberto) => {
    if (!menu || !abrir) return;
    menu.setAttribute('aria-hidden', String(!aberto));
    abrir.setAttribute('aria-expanded', String(aberto));
    document.body.classList.toggle('menu-aberto', aberto);
    if (aberto) menu.querySelector('a')?.focus({ preventScroll: true });
    else abrir.focus({ preventScroll: true });
  };

  abrir?.addEventListener('click', () => defineMenu(true));
  fechar?.addEventListener('click', () => defineMenu(false));
  menu?.querySelectorAll('a').forEach((l) => l.addEventListener('click', () => defineMenu(false)));
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && menu?.getAttribute('aria-hidden') === 'false') defineMenu(false);
  });

  /* ------------------------------------------- Aparecer ao rolar */
  const itens = document.querySelectorAll('.aparece');
  if (!semMovimento && 'IntersectionObserver' in window) {
    const olho = new IntersectionObserver((entradas) => {
      entradas.forEach((entrada) => {
        if (!entrada.isIntersecting) return;
        entrada.target.classList.add('visivel');
        olho.unobserve(entrada.target);
      });
    }, { threshold: 0.1, rootMargin: '0px 0px -6% 0px' });

    itens.forEach((item, i) => {
      item.style.setProperty('--atraso', `${(i % 3) * 90}ms`);
      olho.observe(item);
    });
  } else {
    itens.forEach((item) => item.classList.add('visivel'));
  }

  // Rede de segurança: nada que já esteja na tela pode ficar invisível.
  setTimeout(() => {
    itens.forEach((item) => {
      const caixa = item.getBoundingClientRect();
      if (caixa.top < window.innerHeight && caixa.bottom > 0) item.classList.add('visivel');
    });
  }, 1500);

  /* ---------------------------------------- Luz seguindo o cursor */
  if (!semMovimento && window.matchMedia('(pointer: fine)').matches) {
    let quadro = null;
    window.addEventListener('pointermove', (e) => {
      if (quadro) return;
      quadro = requestAnimationFrame(() => {
        raiz.style.setProperty('--mx', `${e.clientX}px`);
        raiz.style.setProperty('--my', `${e.clientY}px`);
        quadro = null;
      });
    }, { passive: true });
  }

  /* ------------------------------- Abas das coleções por evento */
  const abas = [...document.querySelectorAll('.aba')];
  const paineis = [...document.querySelectorAll('.painel')];

  const secaoColecoes = document.querySelector('.colecoes');
  // Cada aba pode pedir um tema para a seção inteira (os 15 anos pedem rosa).
  const temas = [...new Set(abas.map((a) => a.dataset.tema).filter(Boolean))];

  const mostraAba = (indice, moverFoco = true) => {
    abas.forEach((aba, i) => {
      const ativa = i === indice;
      aba.setAttribute('aria-selected', String(ativa));
      aba.tabIndex = ativa ? 0 : -1;
      paineis[i].hidden = !ativa;
    });

    if (secaoColecoes) {
      const tema = abas[indice].dataset.tema;
      temas.forEach((t) => secaoColecoes.classList.toggle(t, t === tema));
    }

    if (moverFoco) abas[indice].focus();
  };

  abas.forEach((aba, i) => {
    aba.addEventListener('click', () => mostraAba(i, false));
    aba.addEventListener('keydown', (e) => {
      const passo = e.key === 'ArrowRight' ? 1 : e.key === 'ArrowLeft' ? -1 : 0;
      if (!passo) return;
      e.preventDefault();
      mostraAba((i + passo + abas.length) % abas.length);
    });
  });

  /* ------------------------------------ Dúvidas: uma por vez */
  const duvidas = document.querySelectorAll('.duvida');
  duvidas.forEach((item) => {
    item.addEventListener('toggle', () => {
      if (!item.open) return;
      duvidas.forEach((outra) => { if (outra !== item) outra.open = false; });
    });
  });

  /* ------------------------------------------------- Formulário */
  const dataInput = document.querySelector('input[type="date"]');
  if (dataInput && !dataInput.min) {
    const agora = new Date();
    dataInput.min = new Date(agora.getTime() - agora.getTimezoneOffset() * 60000)
      .toISOString().slice(0, 10);
  }

  const zap = document.querySelector('input[name="whatsapp"]');
  zap?.addEventListener('input', () => {
    const n = zap.value.replace(/\D/g, '').slice(0, 11);
    let saida = n;
    if (n.length > 2) saida = `(${n.slice(0, 2)}) ${n.slice(2)}`;
    if (n.length > 7) saida = `(${n.slice(0, 2)}) ${n.slice(2, 7)}-${n.slice(7)}`;
    zap.value = saida;
  });

  const formulario = document.querySelector('.formulario[novalidate]');

  // As coleções oferecidas mudam conforme o tipo de evento: quem procura
  // 15 anos não deveria ver pacote de casamento na lista.
  if (formulario) {
    const tipo = formulario.querySelector('#tipo');
    const pacote = formulario.querySelector('#pacote');
    let mapa = {};
    try { mapa = JSON.parse(formulario.dataset.pacotes || '{}'); } catch { mapa = {}; }

    const preenchePacotes = (manterEscolha) => {
      if (!tipo || !pacote) return;
      const escolhido = manterEscolha ? (pacote.dataset.escolhido || '') : pacote.value;
      const opcoes = mapa[tipo.value] || [];
      pacote.innerHTML = '';

      const vazia = new Option('Ainda não sei', '');
      pacote.add(vazia);
      opcoes.forEach((nome) => pacote.add(new Option(nome, nome)));

      if (escolhido && opcoes.includes(escolhido)) pacote.value = escolhido;
      pacote.disabled = opcoes.length === 0;
    };

    preenchePacotes(true);
    tipo?.addEventListener('change', () => preenchePacotes(false));

    // Site estático: não há servidor para receber o formulário. O envio
    // monta a mensagem no próprio navegador e leva direto para o WhatsApp.
    const formatarData = (valor) => {
      if (!valor) return 'Não informada';
      const [ano, mes, dia] = valor.split('-');
      return `${dia}/${mes}/${ano}`;
    };

    formulario.addEventListener('submit', (e) => {
      e.preventDefault();

      let primeiro = null;
      formulario.querySelectorAll('[required]').forEach((campo) => {
        const grupo = campo.closest('.campo');
        const vazio = !campo.value.trim();
        grupo?.classList.toggle('erro', vazio);
        if (vazio && !primeiro) primeiro = campo;
      });
      if (primeiro) {
        primeiro.focus();
        primeiro.scrollIntoView({ block: 'center', behavior: semMovimento ? 'auto' : 'smooth' });
        return;
      }

      // Campo-armadilha: se veio preenchido, foi robô — some sem enviar nada.
      if (formulario.elements.website?.value) return;

      const rotulo = formulario.querySelector('.enviar span');
      if (rotulo) rotulo.textContent = 'Enviando…';

      const dados = Object.fromEntries(new FormData(formulario).entries());
      let modelo = '';
      try { modelo = JSON.parse(formulario.dataset.modelo || '""'); } catch { modelo = ''; }

      const texto = modelo
        .replace('{nome}', dados.nome || '')
        .replace('{whatsapp}', dados.whatsapp || '')
        .replace('{tipo}', dados.tipo || '')
        .replace('{data}', formatarData(dados.data))
        .replace('{local}', dados.local || '')
        .replace('{pacote}', dados.pacote || 'ainda não escolhida')
        .replace('{mensagem}', dados.mensagem || 'não informado');

      // Pela sessão do navegador, e não pela URL: assim o telefone da
      // pessoa não fica gravado no histórico nem em link compartilhado.
      sessionStorage.setItem('ultimo_contato', texto);
      window.location.href = '/obrigado';
    });

    formulario.querySelectorAll('[required]').forEach((campo) => {
      campo.addEventListener('input', () => {
        if (campo.value.trim()) campo.closest('.campo')?.classList.remove('erro');
      });
    });
  }

  /* --------------------------- Página de recebido: abre o WhatsApp */
  const zapAbrir = document.querySelector('[data-abrir-zap]');
  if (zapAbrir) {
    const texto = sessionStorage.getItem('ultimo_contato');
    if (texto) {
      sessionStorage.removeItem('ultimo_contato');
      const numero = zapAbrir.dataset.numero;
      zapAbrir.href = `https://api.whatsapp.com/send?phone=${numero}&text=${encodeURIComponent(texto)}`;
    }
    setTimeout(() => window.open(zapAbrir.href, '_blank', 'noopener'), 900);
  }
})();
