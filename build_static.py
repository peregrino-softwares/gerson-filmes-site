# -*- coding: utf-8 -*-
"""Gera a versão estática do site, em `docs/`, para publicar no GitHub Pages.

O site continua sendo editado do jeito de sempre — mexendo no `content.py` e
rodando `python app.py` para conferir. Este script só tira uma "fotografia"
de cada página já pronta, sem Python por trás, para hospedar de graça e
sempre no ar.

Rodar antes de cada publicação:

    python build_static.py
    git add docs
    git commit -m "Atualiza o site publicado"
    git push
"""

import shutil
from pathlib import Path

from app import app, content

BASE_DIR = Path(__file__).resolve().parent
DOCS_DIR = BASE_DIR / "docs"

# Sem domínio próprio (MARCA["site_url"] vazio), o site mora dentro de uma
# pasta: https://peregrino-softwares.github.io/gerson-filmes-site/, e não
# na raiz. Precisa disso para os links entre páginas — Início, Casamentos,
# os vídeos — nascerem já com esse prefixo. Quando o domínio voltar a ser
# preenchido, o prefixo some sozinho e tudo passa a apontar para a raiz.
ENDERECO_PADRAO_PAGES = "https://peregrino-softwares.github.io/gerson-filmes-site"
BASE_URL = content.MARCA.get("site_url") or ENDERECO_PADRAO_PAGES

# Cada página vira uma pasta com um index.html, para o endereço final não
# precisar de extensão (gersonfilmes.com.br/casamentos, não .../casamentos.html).
PAGINAS = {
    "/": "index.html",
    "/casamentos": "casamentos/index.html",
    "/15-anos": "15-anos/index.html",
    "/eventos": "eventos/index.html",
    "/orcamento": "orcamento/index.html",
    "/obrigado": "obrigado/index.html",
}


def congelar():
    if DOCS_DIR.exists():
        shutil.rmtree(DOCS_DIR)
    DOCS_DIR.mkdir()

    with app.test_client() as cliente:
        for rota, destino in PAGINAS.items():
            resposta = cliente.get(rota, base_url=BASE_URL)
            if resposta.status_code != 200:
                raise SystemExit(f"{rota} devolveu {resposta.status_code}, esperado 200")
            caminho = DOCS_DIR / destino
            caminho.parent.mkdir(parents=True, exist_ok=True)
            caminho.write_bytes(resposta.data)

        # A página de erro do GitHub Pages precisa se chamar exatamente
        # 404.html e morar na raiz — é onde o Pages já procura sozinho.
        erro = cliente.get("/uma-pagina-que-nao-existe", base_url=BASE_URL)
        (DOCS_DIR / "404.html").write_bytes(erro.data)

        for rota in ("/robots.txt", "/sitemap.xml"):
            resposta = cliente.get(rota, base_url=BASE_URL)
            (DOCS_DIR / rota.lstrip("/")).write_bytes(resposta.data)

    shutil.copytree(BASE_DIR / "static", DOCS_DIR / "static")

    dominio = content.MARCA.get("site_url", "").split("//")[-1]
    if dominio:
        (DOCS_DIR / "CNAME").write_text(dominio, encoding="utf-8")

    # Sem isso o GitHub trata a pasta como projeto Jekyll e ignora tudo
    # que começa com "_" — não é o caso aqui, mas o arquivo é o padrão.
    (DOCS_DIR / ".nojekyll").touch()

    print(f"Pronto: {len(PAGINAS) + 3} páginas em {DOCS_DIR}")


if __name__ == "__main__":
    congelar()
