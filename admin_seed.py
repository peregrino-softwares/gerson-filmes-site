"""Utilitário para cadastrar clientes e arquivos na área reservada.

Exemplos:
  python admin_seed.py criar-cliente --nome "Ana e Lucas" --email casal@email.com --senha "uma-senha-forte"
  python admin_seed.py adicionar-arquivo --email casal@email.com --titulo "Filme principal" --arquivo filme.mp4 --tipo video
"""

import argparse
import shutil
import sqlite3
from pathlib import Path

from werkzeug.security import generate_password_hash

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "private" / "clients.db"
UPLOADS_DIR = BASE_DIR / "uploads"


def connect():
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    UPLOADS_DIR.mkdir(parents=True, exist_ok=True)
    con = sqlite3.connect(DB_PATH)
    con.row_factory = sqlite3.Row
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
    colunas = {c["name"] for c in con.execute("PRAGMA table_info(files)")}
    if "url" not in colunas:
        con.execute("ALTER TABLE files ADD COLUMN url TEXT")

    con.commit()
    return con


def create_client(nome, email, senha):
    email = email.lower().strip()
    with connect() as con:
        try:
            cursor = con.execute(
                "INSERT INTO clients(nome, email, senha_hash) VALUES (?, ?, ?)",
                (nome.strip(), email, generate_password_hash(senha)),
            )
            con.commit()
        except sqlite3.IntegrityError as exc:
            raise SystemExit(f"Já existe um cliente com o e-mail {email}.") from exc

    client_id = cursor.lastrowid
    (UPLOADS_DIR / str(client_id)).mkdir(parents=True, exist_ok=True)
    print(f"Cliente criado com sucesso. ID: {client_id}")


def add_file(email, titulo, source_file, kind):
    source = Path(source_file).expanduser().resolve()
    if not source.is_file():
        raise SystemExit(f"Arquivo não encontrado: {source}")

    with connect() as con:
        client = con.execute(
            "SELECT id, nome FROM clients WHERE lower(email) = ?",
            (email.lower().strip(),),
        ).fetchone()
        if not client:
            raise SystemExit("Cliente não encontrado.")

        destination_dir = UPLOADS_DIR / str(client["id"])
        destination_dir.mkdir(parents=True, exist_ok=True)
        destination = destination_dir / source.name
        shutil.copy2(source, destination)

        con.execute(
            "INSERT INTO files(client_id, titulo, filename, kind) VALUES (?, ?, ?, ?)",
            (client["id"], titulo.strip(), source.name, kind),
        )
        con.commit()

    print(f"Arquivo adicionado para {client['nome']}: {destination}")


def add_link(email, titulo, url, kind):
    """Registra uma entrega que mora fora do servidor (Drive, Vimeo, YouTube).

    Nada é copiado: o site só guarda o endereço e mostra o botão dentro da
    área do cliente. Use isto para filmes grandes, que sairiam caros de
    hospedar aqui.
    """
    url = url.strip()
    if not url.startswith(("http://", "https://")):
        raise SystemExit("O link precisa comecar com http:// ou https://")

    with connect() as con:
        client = con.execute(
            "SELECT id, nome FROM clients WHERE lower(email) = ?",
            (email.lower().strip(),),
        ).fetchone()
        if not client:
            raise SystemExit("Cliente não encontrado.")

        con.execute(
            "INSERT INTO files(client_id, titulo, filename, kind, url) VALUES (?, ?, ?, ?, ?)",
            (client["id"], titulo.strip(), "", kind, url),
        )
        con.commit()

    print(f"Link registrado para {client['nome']}: {titulo}")
    print("Lembre-se de deixar o arquivo compartilhado como 'qualquer pessoa com o link'.")


def list_leads(limite):
    with connect() as con:
        linhas = con.execute(
            "SELECT * FROM leads ORDER BY id DESC LIMIT ?", (limite,)
        ).fetchall()

    if not linhas:
        print("Nenhum pedido de orçamento recebido ainda.")
        return

    print(f"\n{len(linhas)} pedido(s) mais recente(s):\n")
    for linha in linhas:
        print(f"  #{linha['id']}  {linha['criado_em']}")
        print(f"  {linha['nome']}  ·  {linha['whatsapp']}")
        print(f"  {linha['tipo']} em {linha['data_evento']}  ·  {linha['local']}")
        print(f"  Orçamento: {linha['pacote'] or '—'}  ·  Origem: {linha['origem']}")
        if linha["mensagem"]:
            print(f"  \"{linha['mensagem']}\"")
        print("  " + "-" * 60)


def build_parser():
    parser = argparse.ArgumentParser(description="Administração da área do cliente")
    sub = parser.add_subparsers(dest="command", required=True)

    create = sub.add_parser("criar-cliente", help="Cria um novo acesso")
    create.add_argument("--nome", required=True)
    create.add_argument("--email", required=True)
    create.add_argument("--senha", required=True)

    add = sub.add_parser("adicionar-arquivo", help="Copia e registra uma entrega")
    add.add_argument("--email", required=True, help="E-mail do cliente")
    add.add_argument("--titulo", required=True, help="Nome exibido no painel")
    add.add_argument("--arquivo", required=True, help="Caminho do arquivo")
    add.add_argument("--tipo", choices=["video", "file"], default="file")

    link = sub.add_parser("adicionar-link", help="Registra uma entrega hospedada no Drive ou Vimeo")
    link.add_argument("--email", required=True, help="E-mail do cliente")
    link.add_argument("--titulo", required=True, help="Nome exibido no painel")
    link.add_argument("--url", required=True, help="Endereço do Drive, Vimeo ou YouTube")
    link.add_argument("--tipo", choices=["video", "file"], default="video")

    leads = sub.add_parser("ver-pedidos", help="Mostra os orçamentos recebidos pelo site")
    leads.add_argument("--quantidade", type=int, default=20)
    return parser


if __name__ == "__main__":
    args = build_parser().parse_args()
    if args.command == "criar-cliente":
        create_client(args.nome, args.email, args.senha)
    elif args.command == "adicionar-link":
        add_link(args.email, args.titulo, args.url, args.tipo)
    elif args.command == "adicionar-arquivo":
        add_file(args.email, args.titulo, args.arquivo, args.tipo)
    elif args.command == "ver-pedidos":
        list_leads(args.quantidade)
