/* Os scripts defer executam em ordem, depois que o contêiner existe.
   Se o serviço estiver indisponível, os links para as opiniões permanecem. */
(() => {
  'use strict';
  if (document.getElementById('wp-widget-reviews') && typeof window.wpShowReviews === 'function') {
    window.wpShowReviews(430900, 'white');
  }
})();
