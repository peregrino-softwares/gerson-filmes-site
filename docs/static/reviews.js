/* Os scripts defer executam em ordem, depois que o contêiner existe.
   Se o serviço estiver indisponível, os links para as opiniões permanecem. */
(() => {
  'use strict';
  const widget = document.getElementById('wp-widget-reviews');
  if (!widget || typeof window.wpShowReviews !== 'function') return;

  // O widget cresce depois que o navegador já posicionou a âncora.
  const orcamento = document.getElementById('orcamento');
  if (location.hash === '#orcamento' && orcamento) {
    const controle = new AbortController();
    const observador = new ResizeObserver(() => {
      orcamento.scrollIntoView({ block: 'start', behavior: 'instant' });
    });
    const parar = () => {
      observador.disconnect();
      controle.abort();
      clearTimeout(limite);
    };
    const limite = setTimeout(parar, 10000);
    for (const evento of ['wheel', 'touchstart', 'pointerdown', 'keydown', 'hashchange']) {
      window.addEventListener(evento, parar, { passive: true, signal: controle.signal });
    }
    observador.observe(widget);
  }

  window.wpShowReviews(430900, 'white');
})();
