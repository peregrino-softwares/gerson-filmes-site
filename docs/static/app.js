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

    const personalizado = 'personalizado';
    const servicos = formulario.querySelector('#servicos-personalizados');
    const servicosOpcoes = formulario.querySelector('#servicos-opcoes');
    const servicosErro = formulario.querySelector('#servicos-erro');
    const servicosContagem = formulario.querySelector('#servicos-contagem');
    let catalogo = {};
    try { catalogo = JSON.parse(formulario.dataset.servicos || '{}'); } catch { catalogo = {}; }

    const selecionados = () => [...formulario.querySelectorAll('[name="servicos"]:checked')];
    const atualizaContagem = () => {
      const quantidade = selecionados().length;
      if (servicosContagem) {
        servicosContagem.textContent = quantidade === 1
          ? '1 serviço selecionado'
          : `${quantidade} serviços selecionados`;
      }
      if (quantidade && servicosErro) servicosErro.hidden = true;
    };

    let tipoRenderizado = '';
    const atualizaServicos = () => {
      if (!servicos || !servicosOpcoes || !tipo || !pacote) return;
      const aberto = pacote.value === personalizado;
      servicos.hidden = !aberto;
      servicos.disabled = !aberto;
      if (servicosErro) servicosErro.hidden = true;

      if (tipoRenderizado !== tipo.value) {
        tipoRenderizado = tipo.value;
        servicosOpcoes.replaceChildren();
        for (const [titulo, itens] of catalogo[tipo.value] || []) {
          const grupo = document.createElement('fieldset');
          grupo.className = 'servicos-grupo';
          const legenda = document.createElement('legend');
          legenda.textContent = titulo;
          grupo.append(legenda);
          for (const texto of itens) {
            const rotulo = document.createElement('label');
            const escolha = document.createElement('input');
            escolha.type = 'checkbox';
            escolha.name = 'servicos';
            escolha.value = texto;
            rotulo.append(escolha, document.createTextNode(texto));
            grupo.append(rotulo);
          }
          servicosOpcoes.append(grupo);
        }
      }
      atualizaContagem();
    };

    const preenchePacotes = (manterEscolha) => {
      if (!tipo || !pacote) return;
      const mantenhaPersonalizado = pacote.value === personalizado;
      const escolhido = manterEscolha
        ? (parametros.get('modo') === personalizado
          ? personalizado
          : (parametros.get('pacote') || pacote.dataset.escolhido || ''))
        : (mantenhaPersonalizado ? personalizado : '');
      const opcoes = mapa[tipo.value] || [];
      pacote.innerHTML = '';

      const vazia = new Option('Ainda não sei', '');
      pacote.add(vazia);
      opcoes.forEach((nome) => pacote.add(new Option(nome, nome)));

      if (servicos) pacote.add(new Option('Monte seu orçamento', personalizado));
      if (escolhido && [...pacote.options].some((opcao) => opcao.value === escolhido)) {
        pacote.value = escolhido;
      }
      pacote.disabled = opcoes.length === 0 && !servicos;
      atualizaServicos();
    };

    preenchePacotes(true);
    tipo?.addEventListener('change', () => preenchePacotes(false));
    pacote?.addEventListener('change', atualizaServicos);
    servicosOpcoes?.addEventListener('change', atualizaContagem);

    const dataIndefinida = formulario.querySelector('#data-indefinida');
    const atualizaData = () => {
      if (!dataInput || !dataIndefinida) return;
      dataInput.disabled = dataIndefinida.checked;
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
        campo.setAttribute('aria-invalid', String(invalido));
        const aviso = grupo?.querySelector('.campo-erro');
        if (aviso) aviso.hidden = !invalido;
        if (invalido && !primeiro) primeiro = campo;
      });
      if (primeiro) {
        primeiro.focus();
        primeiro.scrollIntoView({ block: 'center', behavior: semMovimento ? 'auto' : 'smooth' });
        return;
      }

      // Campo-armadilha: se veio preenchido, foi robô — some sem enviar nada.
      if (formulario.elements.website?.value) return;

      const querPersonalizar = pacote?.value === personalizado;
      const escolhas = querPersonalizar ? selecionados() : [];
      if (querPersonalizar && escolhas.length === 0) {
        if (servicosErro) servicosErro.hidden = false;
        servicosOpcoes?.querySelector('input')?.focus();
        return;
      }

      const rotulo = formulario.querySelector('.enviar span');
      if (rotulo) rotulo.textContent = 'Preparando a conversa…';

      const dados = Object.fromEntries(new FormData(formulario).entries());
      let modelo = '';
      try { modelo = JSON.parse(formulario.dataset.modelo || '""'); } catch { modelo = ''; }

      const conteudo = {
        nome: dados.nome.trim(),
        tipo: dados.tipo,
        data: formatarData(dados.data),
        local: dados.local.trim(),
        pacote: querPersonalizar ? 'Personalizado' : (dados.pacote || 'ainda não escolhida'),
        mensagem: dados.mensagem?.trim() || 'não informado',
        conheceu: dados.conheceu || 'não informado',
      };
      let texto = modelo.replace(/\{(\w+)\}/g, (campo, chave) => conteudo[chave] ?? campo);
      if (querPersonalizar) {
        texto += '\n\nServiços desejados:\n' + escolhas.map((escolha) => `• ${escolha.value}`).join('\n');
        texto += `\nTempo de cobertura desejado: ${dados.duracao_cobertura || 'A combinar'}`;
      }

      // A mensagem fica na sessão do navegador até a pessoa abrir o WhatsApp,
      // sem incluir os dados em links internos ou no histórico do site.
      try {
        sessionStorage.setItem('ultimo_contato', texto);
        window.location.href = '/obrigado';
      } catch {
        window.location.href = `https://api.whatsapp.com/send?phone=${formulario.dataset.numero}&text=${encodeURIComponent(texto)}`;
      }
    });

    formulario.querySelectorAll('[required]').forEach((campo) => {
      const limpaErro = () => {
        if (!campo.value.trim() || !campo.checkValidity()) return;
        const grupo = campo.closest('.campo');
        grupo?.classList.remove('erro');
        campo.removeAttribute('aria-invalid');
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
