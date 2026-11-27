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

  function configurarCalendario(campo) {
    const abrir = document.querySelector('#calendario-abrir');
    const dialogo = document.querySelector('#calendario-dialogo');
    if (!campo || !abrir || typeof dialogo?.showModal !== 'function') return null;

    const mesCampo = dialogo.querySelector('#calendario-mes');
    const anoCampo = dialogo.querySelector('#calendario-ano');
    const dias = dialogo.querySelector('[data-cal-dias]');
    const anterior = dialogo.querySelector('[data-cal-anterior]');
    const proximo = dialogo.querySelector('[data-cal-proximo]');
    const [anoMin, mesMin] = campo.min.split('-').map(Number);
    const nomesMes = new Intl.DateTimeFormat('pt-BR', { month: 'long', timeZone: 'UTC' });
    const nomesDia = new Intl.DateTimeFormat('pt-BR', { dateStyle: 'full', timeZone: 'UTC' });
    let periodo;

    anoCampo.min = String(anoMin);
    for (let mes = 0; mes < 12; mes += 1) {
      mesCampo.add(new Option(nomesMes.format(new Date(Date.UTC(anoMin, mes, 1))), String(mes)));
    }

    const atualizaBotao = () => {
      const [ano, mes, dia] = campo.value.split('-');
      abrir.querySelector('span').textContent = ano ? `${dia}/${mes}/${ano}` : 'Escolher data';
      abrir.setAttribute('aria-label', ano ? `Data do evento: ${dia}/${mes}/${ano}` : 'Escolher data do evento');
    };

    const desenhar = () => {
      const ano = periodo.getUTCFullYear();
      const mes = periodo.getUTCMonth();
      anoCampo.value = String(ano);
      mesCampo.value = String(mes);
      for (const opcao of mesCampo.options) {
        opcao.disabled = ano === anoMin && Number(opcao.value) < mesMin - 1;
      }
      anterior.disabled = ano === anoMin && mes === mesMin - 1;
      proximo.disabled = ano === 9999 && mes === 11;
      dias.replaceChildren();

      const total = new Date(Date.UTC(ano, mes + 1, 0)).getUTCDate();
      for (let dia = 1; dia <= total; dia += 1) {
        const data = new Date(Date.UTC(ano, mes, dia));
        const iso = data.toISOString().slice(0, 10);
        const botao = document.createElement('button');
        botao.type = 'button';
        botao.textContent = String(dia);
        botao.dataset.dia = iso;
        botao.setAttribute('aria-label', nomesDia.format(data));
        botao.setAttribute('aria-pressed', String(iso === campo.value));
        if (iso === campo.min) botao.setAttribute('aria-current', 'date');
        botao.disabled = iso < campo.min;
        botao.tabIndex = -1;
        if (dia === 1) botao.style.gridColumnStart = String(periodo.getUTCDay() + 1);
        dias.append(botao);
      }
      const entrada = dias.querySelector('[aria-pressed="true"]:not(:disabled)') || dias.querySelector('button:not(:disabled)');
      if (entrada) entrada.tabIndex = 0;
    };

    const mover = (delta) => {
      periodo = new Date(Date.UTC(periodo.getUTCFullYear(), periodo.getUTCMonth() + delta, 1));
      desenhar();
      if (delta < 0 && anterior.disabled) mesCampo.focus();
      if (delta > 0 && proximo.disabled) mesCampo.focus();
    };
    anterior.addEventListener('click', () => mover(-1));
    proximo.addEventListener('click', () => mover(1));
    const escolherPeriodo = () => {
      let ano = anoCampo.valueAsNumber;
      if (!Number.isInteger(ano) || ano < anoMin || ano > 9999) ano = periodo.getUTCFullYear();
      const mes = Math.max(Number(mesCampo.value), ano === anoMin ? mesMin - 1 : 0);
      periodo = new Date(Date.UTC(ano, mes, 1));
      desenhar();
    };
    mesCampo.addEventListener('change', escolherPeriodo);
    anoCampo.addEventListener('change', escolherPeriodo);
    anoCampo.addEventListener('keydown', (evento) => {
      if (evento.key === 'Enter') {
        evento.preventDefault();
        escolherPeriodo();
        dias.querySelector('[tabindex="0"]')?.focus();
      }
    });

    dias.addEventListener('click', (evento) => {
      const escolha = evento.target.closest('button[data-dia]');
      if (!escolha || escolha.disabled) return;
      campo.value = escolha.dataset.dia;
      campo.dispatchEvent(new Event('change', { bubbles: true }));
      dialogo.close();
    });
    dias.addEventListener('keydown', (evento) => {
      const deslocamentos = { ArrowLeft: -1, ArrowRight: 1, ArrowUp: -7, ArrowDown: 7 };
      const delta = deslocamentos[evento.key];
      if (!delta) return;
      evento.preventDefault();
      const opcoes = [...dias.querySelectorAll('button:not(:disabled)')];
      const atual = opcoes.indexOf(evento.target);
      const proxima = opcoes[atual + delta];
      if (!proxima) return;
      evento.target.tabIndex = -1;
      proxima.tabIndex = 0;
      proxima.focus();
    });

    abrir.addEventListener('click', () => {
      const base = campo.value && campo.value >= campo.min ? campo.value : campo.min;
      const [ano, mes] = base.split('-').map(Number);
      periodo = new Date(Date.UTC(ano, mes - 1, 1));
      desenhar();
      dialogo.showModal();
      dias.querySelector('[tabindex="0"]')?.focus();
    });
    dialogo.querySelector('[data-cal-fechar]').addEventListener('click', () => dialogo.close());
    dialogo.addEventListener('close', () => abrir.focus());
    campo.addEventListener('change', atualizaBotao);
    window.addEventListener('pageshow', atualizaBotao);
    atualizaBotao();
    campo.hidden = true;
    abrir.hidden = false;
    return abrir;
  }

  const formulario = document.querySelector('.formulario[novalidate]');

  // As coleções oferecidas mudam conforme o tipo de evento: quem procura
  // 15 anos não deveria ver pacote de casamento na lista.
  if (formulario) {
    const tipo = formulario.querySelector('#tipo');
    const pacote = formulario.querySelector('#pacote');
    const parametros = new URLSearchParams(window.location.search);
    const tipoPedido = parametros.get('tipo');
    if (tipo && [...tipo.options].some((opcao) => opcao.value === tipoPedido)) {
      tipo.value = tipoPedido;
    }
    let mapa = {};
    try { mapa = JSON.parse(formulario.dataset.pacotes || '{}'); } catch { mapa = {}; }

    const preenchePacotes = (manterEscolha) => {
      if (!tipo || !pacote) return;
      const escolhido = manterEscolha ? (parametros.get('pacote') || pacote.dataset.escolhido || '') : '';
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

    const botaoData = configurarCalendario(dataInput);
    const dataIndefinida = formulario.querySelector('#data-indefinida');
    const atualizaData = () => {
      if (!dataInput || !dataIndefinida) return;
      dataInput.disabled = dataIndefinida.checked;
      if (botaoData) {
        botaoData.disabled = dataIndefinida.checked;
        botaoData.removeAttribute('aria-invalid');
      }
      dataInput.required = !dataIndefinida.checked;
      formulario.querySelector('[data-data-obrigatoria]')?.toggleAttribute('hidden', dataIndefinida.checked);
      dataInput.closest('.campo')?.classList.remove('erro');
      dataInput.removeAttribute('aria-invalid');
      const aviso = dataInput.closest('.campo')?.querySelector('.campo-erro');
      if (aviso) aviso.hidden = true;
    };
    atualizaData();
    dataIndefinida?.addEventListener('change', atualizaData);

    // Site estático: não há servidor para receber o formulário. O envio
    // monta a mensagem no próprio navegador e leva direto para o WhatsApp.
    const formatarData = (valor) => {
      if (!valor) return 'A definir';
      const [ano, mes, dia] = valor.split('-');
      return `${dia}/${mes}/${ano}`;
    };

    formulario.addEventListener('submit', (e) => {
      e.preventDefault();

      let primeiro = null;
      formulario.querySelectorAll('[required]').forEach((campo) => {
        const grupo = campo.closest('.campo');
        const invalido = !campo.value.trim() || !campo.checkValidity();
        grupo?.classList.toggle('erro', invalido);
        const controle = campo === dataInput && botaoData ? botaoData : campo;
        controle.setAttribute('aria-invalid', String(invalido));
        const aviso = grupo?.querySelector('.campo-erro');
        if (aviso) aviso.hidden = !invalido;
        if (invalido && !primeiro) primeiro = controle;
      });
      if (primeiro) {
        primeiro.focus();
        primeiro.scrollIntoView({ block: 'center', behavior: semMovimento ? 'auto' : 'smooth' });
        return;
      }

      // Campo-armadilha: se veio preenchido, foi robô — some sem enviar nada.
      if (formulario.elements.website?.value) return;

      const dados = Object.fromEntries(new FormData(formulario).entries());
      let modelo = '';
      try { modelo = JSON.parse(formulario.dataset.modelo || '""'); } catch { modelo = ''; }

      const conteudo = {
        nome: dados.nome.trim(),
        tipo: dados.tipo,
        data: formatarData(dados.data),
        local: dados.local.trim(),
        pacote: dados.pacote || 'ainda não escolhida',
        mensagem: dados.mensagem?.trim() || 'não informado',
        conheceu: dados.conheceu || 'não informado',
      };
      const texto = modelo.replace(/\{(\w+)\}/g, (campo, chave) => conteudo[chave] ?? campo);

      window.location.href = `https://api.whatsapp.com/send?phone=${formulario.dataset.numero}&text=${encodeURIComponent(texto)}`;
    });

    formulario.querySelectorAll('[required]').forEach((campo) => {
      const limpaErro = () => {
        if (!campo.value.trim() || !campo.checkValidity()) return;
        const grupo = campo.closest('.campo');
        grupo?.classList.remove('erro');
        const controle = campo === dataInput && botaoData ? botaoData : campo;
        controle.removeAttribute('aria-invalid');
        const aviso = grupo?.querySelector('.campo-erro');
        if (aviso) aviso.hidden = true;
      };
      campo.addEventListener('input', limpaErro);
      campo.addEventListener('change', limpaErro);
    });
  }

  /* --------------------------- Página de recebido: abre o WhatsApp */
  const zapAbrir = document.querySelector('[data-abrir-zap]');
  if (zapAbrir) {
    const texto = sessionStorage.getItem('ultimo_contato');
    if (texto) {
      const numero = zapAbrir.dataset.numero;
      zapAbrir.href = `https://api.whatsapp.com/send?phone=${numero}&text=${encodeURIComponent(texto)}`;
      zapAbrir.addEventListener('click', () => sessionStorage.removeItem('ultimo_contato'));
    }
  }
})();
