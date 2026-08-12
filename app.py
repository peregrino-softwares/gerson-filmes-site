# -*- coding: utf-8 -*-
"""Gerson Filmes — site institucional e área do cliente.

Para mudar textos, preços e depoimentos, edite `content.py`.
Este arquivo cuida apenas do funcionamento.
"""

from datetime import datetime
from functools import wraps
from pathlib import Path
from urllib.parse import quote
import os
import sqlite3

from flask import (
    Flask, Response, abort, redirect, render_template,
    request, send_from_directory, session, url_for,
)
from werkzeug.security import check_password_hash

import content

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "private" / "clients.db"
UPLOADS_DIR = BASE_DIR / "uploads"
LEADS_DIR = BASE_DIR / "leads"

WHATSAPP = os.getenv("WHATSAPP_NUMBER", content.MARCA["whatsapp"])

# Área do cliente: ligada ou desligada em content.py. Enquanto o servidor não
# tiver disco próprio, ela fica fora do ar de propósito — o banco e os arquivos
# seriam apagados a cada publicação. Desligada, some do site e as páginas
# respondem 404; ligada, tudo volta sem mais nenhuma mudança.
AREA_CLIENTE = getattr(content, "AREA_CLIENTE", True)

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", "troque-esta-chave-em-producao")
app.config.update(
    SESSION_COOKIE_HTTPONLY=True,
    SESSION_COOKIE_SAMESITE="Lax",
    SESSION_COOKIE_SECURE=os.getenv("HTTPS_ONLY", "0") == "1",
    SEND_FILE_MAX_AGE_DEFAULT=60 * 60 * 24 * 7,
)


# ---------------------------------------------------------------- banco
def db_connection():
    con = sqlite3.connect(DB_PATH)
    con.row_factory = sqlite3.Row
    return con


def init_db():
    for folder in (DB_PATH.parent, UPLOADS_DIR, LEADS_DIR):
        folder.mkdir(parents=True, exist_ok=True)

    with db_connection() as con:
        con.execute("""
            CREATE TABLE IF NOT EXISTS clients (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL,
                senha_hash TEXT NOT NULL
            )
        """)
        con.execute("""
            CREATE TABLE IF NOT EXISTS files (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                client_id INTEGER NOT NULL,
                titulo TEXT NOT NULL,
                filename TEXT NOT NULL,
                kind TEXT NOT NULL DEFAULT 'file',
                FOREIGN KEY(client_id) REFERENCES clients(id)
            )
        """)
        con.execute("""
            CREATE TABLE IF NOT EXISTS leads (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                criado_em TEXT NOT NULL,
                nome TEXT NOT NULL,
                whatsapp TEXT NOT NULL,
                data_evento TEXT,
                local TEXT,
                tipo TEXT,
                pacote TEXT,
                origem TEXT,
                mensagem TEXT
            )
        """)

        # Entregas por link (Google Drive, Vimeo, YouTube). Filmes de
        # casamento passam facilmente de 10 GB — hospedar tudo no servidor
        # sairia caro. Com o link, o arquivo mora no Drive e a página
        # continua sendo a sua.
        colunas = {c["name"] for c in con.execute("PRAGMA table_info(files)")}
        if "url" not in colunas:
            con.execute("ALTER TABLE files ADD COLUMN url TEXT")

        con.commit()


init_db()


# ---------------------------------------------------------------- comum
# Os dois ícones ficam aqui para não repetir o desenho em cada template.
ICONE_WHATSAPP = (
    '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2a9.7 9.7 0 0 0-8.4 14.6L2 22'
    'l5.6-1.5A9.8 9.8 0 1 0 12 2Zm0 17.7a7.8 7.8 0 0 1-4-1.1l-.3-.2-3.3.9.9-3.2-.2-.3a7.7 7.7 0 1 1'
    ' 6.9 3.9Zm4.3-5.8c-.2-.1-1.4-.7-1.6-.8-.2-.1-.4-.1-.5.1-.2.2-.6.8-.8.9-.1.2-.3.2-.5.1-1.4-.7'
    '-2.4-1.3-3.3-2.9-.3-.4.3-.4.8-1.3.1-.2 0-.4 0-.5l-.7-1.7c-.2-.4-.4-.4-.6-.4h-.5c-.2 0-.5.1'
    '-.7.3-.2.3-1 1-1 2.4s1 2.8 1.2 3c.1.2 2 3.1 5 4.3 1.9.8 2.7.9 3.7.7.6-.1 1.4-.6 1.6-1.1.2-.5'
    '.2-1 .1-1.1 0-.1-.2-.2-.4-.3Z"/></svg>'
)
ICONE_INSTAGRAM = (
    '<svg viewBox="0 0 24 24" aria-hidden="true">'
    '<path d="M12 2.2c3.2 0 3.6 0 4.9.07 1.17.05 1.8.25 2.23.41.56.22.96.48 1.38.9.42.42.68.82.9 1.38'
    '.16.42.36 1.06.41 2.23.06 1.27.07 1.65.07 4.86s0 3.6-.07 4.86c-.05 1.17-.25 1.8-.41 2.23a3.8 3.8'
    ' 0 0 1-.9 1.38c-.42.42-.82.68-1.38.9-.42.16-1.06.36-2.23.41-1.27.06-1.65.07-4.86.07s-3.6 0-4.86'
    '-.07c-1.17-.05-1.8-.25-2.23-.41a3.8 3.8 0 0 1-1.38-.9 3.8 3.8 0 0 1-.9-1.38c-.16-.42-.36-1.06'
    '-.41-2.23C2.2 15.6 2.2 15.2 2.2 12s0-3.6.07-4.86c.05-1.17.25-1.8.41-2.23.22-.56.48-.96.9-1.38'
    '.42-.42.82-.68 1.38-.9.42-.16 1.06-.36 2.23-.41C8.46 2.2 8.84 2.2 12 2.2Zm0 1.8c-3.15 0-3.5 0'
    '-4.74.07-.9.04-1.38.19-1.7.31-.43.17-.73.37-1.05.69-.32.32-.52.62-.69 1.05-.12.32-.27.8-.31 1.7'
    'C3.44 8.85 3.43 9.2 3.43 12s0 3.15.07 4.38c.04.9.19 1.38.31 1.7.17.43.37.73.69 1.05.32.32.62.52'
    ' 1.05.69.32.12.8.27 1.7.31 1.24.07 1.59.07 4.75.07s3.5 0 4.74-.07c.9-.04 1.38-.19 1.7-.31.43-.17'
    '.73-.37 1.05-.69.32-.32.52-.62.69-1.05.12-.32.27-.8.31-1.7.07-1.23.07-1.58.07-4.38s0-3.15-.07'
    '-4.38c-.04-.9-.19-1.38-.31-1.7a2.8 2.8 0 0 0-.69-1.05 2.8 2.8 0 0 0-1.05-.69c-.32-.12-.8-.27'
    '-1.7-.31C15.5 4 15.15 4 12 4Zm0 3.07a4.93 4.93 0 1 1 0 9.86 4.93 4.93 0 0 1 0-9.86Zm0 1.8a3.13'
    ' 3.13 0 1 0 0 6.26 3.13 3.13 0 0 0 0-6.26Zm5.14-1.9a1.15 1.15 0 1 1-2.3 0 1.15 1.15 0 0 1 2.3 0Z"/>'
    '</svg>'
)


def endereco_base():
    """Endereço público do site, sem a barra final.

    Enquanto não houver domínio em MARCA["site_url"], usa o endereço pelo
    qual a página está sendo acessada. Assim o link de compartilhamento e o
    sitemap continuam válidos mesmo antes de o domínio existir.
    """
    return (content.MARCA.get("site_url") or "").rstrip("/") or request.url_root.rstrip("/")


@app.context_processor
def inject_content():
    """Deixa os textos de content.py disponíveis em todos os templates."""
    return {
        "marca": content.MARCA,
        "base_url": endereco_base(),
        "icone_whatsapp": ICONE_WHATSAPP,
        "icone_instagram": ICONE_INSTAGRAM,
        "ficha": content.FICHA,
        "especialidades": content.ESPECIALIDADES,
        "metodo": content.METODO,
        "processo": content.PROCESSO,
        "colecoes": content.COLECOES,
        "pagamento": content.PAGAMENTO,
        "setores": content.SETORES,
        "ordem_setores": content.ORDEM_SETORES,
        "ordem_colecoes": content.ORDEM_COLECOES,
        "combinado": content.COMBINADO,
        # só entram no site os depoimentos que a pessoa autorizou
        "depoimentos": [d for d in content.DEPOIMENTOS if d.get("aprovado")],
        "quem": content.QUEM,
        # A foto do Gerson é opcional: enquanto o arquivo não existir, a seção
        # mostra só o texto, em vez de abrir um buraco no layout.
        "quem_tem_foto": (BASE_DIR / "static" / content.QUEM["foto"]).is_file(),
        "faq": content.FAQ,
        "tipos_evento": content.TIPOS_EVENTO,
        "pacotes_por_tipo": content.PACOTES_POR_TIPO,
        "como_conheceu": content.COMO_CONHECEU,
        "whatsapp_link": whatsapp_link(content.WHATSAPP_MENSAGEM),
        # No site publicado (estático), o formulário monta a mensagem no
        # próprio navegador — não há servidor para receber o POST.
        "whatsapp_formulario": content.WHATSAPP_FORMULARIO,
        # Desligada, some do menu, do rodapé e da página de obrigado.
        "area_cliente": AREA_CLIENTE,
        "ano": datetime.now().year,
    }


def whatsapp_link(texto):
    return f"https://api.whatsapp.com/send?phone={WHATSAPP}&text={quote(texto)}"


@app.url_defaults
def versionar_estaticos(endpoint, values):
    """Carimba a data do arquivo em toda URL de /static.

    Sem isso, o navegador guardaria o CSS e o vídeo por uma semana e quem já
    visitou o site continuaria vendo a versão antiga depois de uma atualização.
    """
    if endpoint != "static" or "filename" not in values:
        return
    try:
        values["v"] = int((BASE_DIR / "static" / values["filename"]).stat().st_mtime)
    except OSError:
        pass


@app.after_request
def security_headers(response):
    response.headers.setdefault("X-Content-Type-Options", "nosniff")
    response.headers.setdefault("X-Frame-Options", "SAMEORIGIN")
    response.headers.setdefault("Referrer-Policy", "strict-origin-when-cross-origin")
    response.headers.setdefault("Permissions-Policy", "geolocation=(), microphone=(), camera=()")
    return response


# ---------------------------------------------------------------- páginas
@app.get("/")
def home():
    return render_template("index.html")


@app.get("/<any(casamentos, '15-anos', eventos):slug>")
def setor(slug):
    """Uma página por setor: casamentos, 15 anos e eventos.

    Todas usam o mesmo template — o que muda é o bloco em SETORES.
    """
    return render_template("setor.html", setor=content.SETORES[slug], slug=slug)


@app.route("/orcamento", methods=["GET", "POST"])
def orcamento():
    if request.method == "GET":
        return render_template(
            "orcamento.html",
            pacote=request.args.get("pacote", ""),
            tipo=request.args.get("tipo", ""),
        )

    # Campo-armadilha invisível: se veio preenchido, foi robô.
    if request.form.get("website"):
        return redirect(url_for("obrigado"))

    dados = {chave: request.form.get(chave, "").strip() for chave in
             ("nome", "whatsapp", "data", "local", "tipo", "pacote", "mensagem", "conheceu")}
    dados["origem"] = request.form.get("origem", "Site").strip()

    obrigatorios = ("nome", "whatsapp", "data", "local", "tipo")
    if not all(dados[chave] for chave in obrigatorios):
        return render_template(
            "orcamento.html",
            pacote=dados["pacote"],
            tipo=dados["tipo"],
            enviado=dados,
            erro="Faltou preencher um campo obrigatório. Confira os destacados abaixo.",
        ), 400

    registrar_lead(dados)

    texto = content.WHATSAPP_FORMULARIO.format(
        nome=dados["nome"],
        whatsapp=dados["whatsapp"],
        tipo=dados["tipo"],
        data=formatar_data(dados["data"]),
        local=dados["local"],
        pacote=dados["pacote"] or "ainda não escolhida",
        mensagem=dados["mensagem"] or "não informado",
    )
    # A mensagem vai pela sessão, e não pela URL: assim o telefone do cliente
    # não fica gravado no histórico do navegador nem em link compartilhado.
    session["ultimo_contato"] = texto
    return redirect(url_for("obrigado"))


@app.get("/obrigado")
def obrigado():
    # No site publicado, o app.js já troca o link pelo WhatsApp com a
    # mensagem da pessoa, lida do sessionStorage do navegador.
    return render_template("obrigado.html")


def formatar_data(valor):
    try:
        return datetime.strptime(valor, "%Y-%m-%d").strftime("%d/%m/%Y")
    except ValueError:
        return valor or "Não informada"


def registrar_lead(dados):
    """Guarda o contato em dois lugares: banco (consulta) e texto (leitura rápida)."""
    agora = datetime.now()
    try:
        with db_connection() as con:
            con.execute(
                "INSERT INTO leads(criado_em, nome, whatsapp, data_evento, local, tipo,"
                " pacote, origem, mensagem) VALUES (?,?,?,?,?,?,?,?,?)",
                (agora.strftime("%Y-%m-%d %H:%M:%S"), dados["nome"], dados["whatsapp"],
                 dados["data"], dados["local"], dados["tipo"], dados["pacote"],
                 f"{dados['origem']} / {dados['conheceu'] or 'não informado'}", dados["mensagem"]),
            )
            con.commit()
    except sqlite3.Error:
        pass  # nunca deixar o cliente sem resposta por causa do banco

    with (LEADS_DIR / "orcamentos.txt").open("a", encoding="utf-8") as arquivo:
        arquivo.write(
            f"[{agora.strftime('%d/%m/%Y %H:%M')}] "
            f"Nome: {dados['nome']} | WhatsApp: {dados['whatsapp']} | "
            f"Tipo: {dados['tipo']} | Data: {formatar_data(dados['data'])} | "
            f"Local: {dados['local']} | Coleção: {dados['pacote']} | "
            f"Conheceu por: {dados['conheceu']} | Msg: {dados['mensagem']}\n"
        )


# ---------------------------------------------------------------- cliente
def area_ligada(view):
    """Fecha a área do cliente quando AREA_CLIENTE está desligada.

    Esconder o link do menu não bastaria: quem tivesse o endereço salvo
    entraria assim mesmo, criaria acesso e o perderia na publicação
    seguinte. Com o 404, a parte que ainda não se sustenta simplesmente
    não existe para o visitante.
    """
    @wraps(view)
    def wrapped(*args, **kwargs):
        if not AREA_CLIENTE:
            abort(404)
        return view(*args, **kwargs)
    return wrapped


def login_required(view):
    @wraps(view)
    def wrapped(*args, **kwargs):
        if "client_id" not in session:
            return redirect(url_for("cliente"))
        return view(*args, **kwargs)
    return wrapped


@app.route("/cliente", methods=["GET", "POST"])
@area_ligada
def cliente():
    if request.method == "GET":
        if session.get("client_id"):
            return redirect(url_for("cliente_painel"))
        return render_template("cliente_login.html")

    email = request.form.get("email", "").lower().strip()
    senha = request.form.get("senha", "")

    with db_connection() as con:
        cliente_db = con.execute(
            "SELECT * FROM clients WHERE lower(email) = ?", (email,)
        ).fetchone()

    if not cliente_db or not check_password_hash(cliente_db["senha_hash"], senha):
        return render_template("cliente_login.html", erro="E-mail ou senha incorretos."), 401

    session.clear()
    session["client_id"] = cliente_db["id"]
    session["client_name"] = cliente_db["nome"]
    return redirect(url_for("cliente_painel"))


@app.get("/cliente/painel")
@area_ligada
@login_required
def cliente_painel():
    with db_connection() as con:
        arquivos = con.execute(
            "SELECT titulo, filename, kind, url FROM files WHERE client_id = ? ORDER BY id DESC",
            (session["client_id"],),
        ).fetchall()

    def entrega(linha):
        return {
            "titulo": linha["titulo"],
            "arquivo": linha["filename"],
            "url": linha["url"],          # preenchido só quando mora fora daqui
        }

    videos = [entrega(l) for l in arquivos if l["kind"] == "video"]
    downloads = [entrega(l) for l in arquivos if l["kind"] != "video"]
    return render_template(
        "cliente_painel.html",
        nome=session.get("client_name", "Cliente"),
        videos=videos,
        downloads=downloads,
    )


@app.get("/cliente/sair")
def cliente_sair():
    session.clear()
    return redirect(url_for("home"))


def arquivo_autorizado(filename):
    with db_connection() as con:
        linha = con.execute(
            "SELECT filename FROM files WHERE client_id = ? AND filename = ?",
            (session["client_id"], filename),
        ).fetchone()
    return linha is not None


@app.get("/cliente/assistir/<path:filename>")
@area_ligada
@login_required
def cliente_assistir(filename):
    if not arquivo_autorizado(filename):
        abort(404)
    return send_from_directory(UPLOADS_DIR / str(session["client_id"]), filename)


@app.get("/cliente/baixar/<path:filename>")
@area_ligada
@login_required
def cliente_baixar(filename):
    if not arquivo_autorizado(filename):
        abort(404)
    return send_from_directory(
        UPLOADS_DIR / str(session["client_id"]), filename, as_attachment=True
    )


# ---------------------------------------------------------------- buscadores
@app.get("/robots.txt")
def robots():
    corpo = (
        "User-agent: *\n"
        "Allow: /\n"
        "Disallow: /cliente\n"
        f"Sitemap: {endereco_base()}/sitemap.xml\n"
    )
    return Response(corpo, mimetype="text/plain")


@app.get("/sitemap.xml")
def sitemap():
    base = endereco_base()
    hoje = datetime.now().strftime("%Y-%m-%d")
    paginas = [("/", "1.0")]
    paginas += [(f"/{s}", "0.9") for s in content.ORDEM_SETORES]
    paginas += [("/orcamento", "0.8")]
    urls = "".join(
        f"<url><loc>{base}{caminho}</loc><lastmod>{hoje}</lastmod>"
        f"<priority>{peso}</priority></url>"
        for caminho, peso in paginas
    )
    xml = ('<?xml version="1.0" encoding="UTF-8"?>'
           '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
           f'{urls}</urlset>')
    return Response(xml, mimetype="application/xml")


@app.errorhandler(404)
def pagina_nao_encontrada(_erro):
    return render_template("404.html"), 404


if __name__ == "__main__":
    # A porta vem de PORT quando existir, para poder rodar duas versões do
    # site ao mesmo tempo sem uma tomar o lugar da outra.
    app.run(debug=True, port=int(os.getenv("PORT", "5000")))
