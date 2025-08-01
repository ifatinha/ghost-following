"""
ghost_following.py

Ferramenta de linha de comando que identifica quais usuários do GitHub que você segue
não te seguem de volta. Usa a API pública do GitHub, sem necessidade de autenticação.

Funcionalidades:
- Coleta seguidores e seguidos via API REST.
- Lida automaticamente com paginação de resultados.
- Exibe, no terminal, os usuários que não te seguem de volta.

Limitações:
- Limite de 60 requisições por hora (API sem token).
- Exige conexão com a internet.
"""

# ghost_following.py
import csv
import os
import requests
from dotenv import load_dotenv

# ───────────────────────────────────────────────────────────────
# 👇 1. Carrega variáveis do arquivo .env (como o token do GitHub)
# ───────────────────────────────────────────────────────────────
load_dotenv()

# ───────────────────────────────────────────────────────────────
# 👇 2. Recupera o token do ambiente (ou pede via input, se ausente)
# ───────────────────────────────────────────────────────────────
token = os.getenv("GITHUB_TOKEN")
if not token:
    token = input("🔐 Cole seu token do GitHub [ou pressione Enter para seguir anônimo]: ").strip() or None

# ───────────────────────────────────────────────────────────────
# 👇 3. Função para fazer requisições com ou sem autenticação
# ───────────────────────────────────────────────────────────────


def make_authenticated_request(url, token=None):
    """
    Faz uma requisição GET à API do GitHub com autenticação opcional.

    Parâmetros:
        url (str): URL da API do GitHub.
        token (str): Token pessoal (opcional).

    Retorno:
        requests.Response: Objeto com os dados da resposta.
    """

    # Dicionário para evitar cabeçalhos HTTP
    headers = {}
    if token:
        # Autenticação via token
        headers["Authorization"] = f"token {token}"

    response = requests.get(url, headers=headers, timeout=30)
    response.raise_for_status()
    return response

# ───────────────────────────────────────────────────────────────
# 👇 4. Função para coletar todos os dados paginados da API
# ───────────────────────────────────────────────────────────────


def get_all_pages(url, token=None):
    """
    Percorre todas as páginas de uma API do GitHub que usa paginação.

    Retorna:
        list: Lista com todos os resultados acumulados.
    """

    results = []

    while url:
        response = make_authenticated_request(url, token)
        # Interrompe se a requisição falhar.
        response.raise_for_status()
        # Adiciona os dados da página atual
        results.extend(response.json())
        # Verifica se a uma próxima página na resposta
        url = response.links.get("next", {}).get("url")
    return results


# ───────────────────────────────────────────────────────────────
# 👇 5. Extrai  os nomes de usuário (login) de cada item retornado pela API
# ───────────────────────────────────────────────────────────────


def get_usernames(data):
    """
    Extrai os nomes de usuário (login) de uma lista de dicionários de usuários.

    Parâmetros:
        data (list): Lista de dicionários retornados pela API do GitHub.

    Retorna:
        set: Conjunto com os nomes de usuário (strings) únicos.
    """
    return {user["login"] for user in data}

# ─────────────────────────────────────────────────────────
# 👇 6. Exporta para CSV
# ─────────────────────────────────────────────────────────


def export_to_csv(usernames, filename="data/ghost_following.csv"):
    """
    Exporta uma lista ou conjunto de nomes de usuários para um arquivo CSV.

    Parâmetros:
        usernames (iterável): Conjunto ou lista de logins do GitHub.
        filename (str): Caminho do arquivo CSV a ser criado.
    """

    # Garante que o diretório data existe
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    # Escreve o arquivo CSV
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Usuarios que você segue, mas que não te seguem de volta"])  # Cabeçalho
        for user in usernames:
            writer.writerow([user])

    print(f"\n📁 Resultado exportado para: {filename}")

# ─────────────────────────────────────────────────────────
# 👇 7. Verifica a diferença entre seguidores e seguindo
# ─────────────────────────────────────────────────────────


def difference_list(following, followers):
    """
    Compara duas listas e retorna os elementos que estão em lista1 mas não estão em lista2.

    Útil para identificar, por exemplo, quem você segue no GitHub, mas não te segue de volta.

    Args:
        lista1 (list): Lista base (ex: usuários que você segue).
        lista2 (list): Lista de comparação (ex: usuários que te seguem).

    Returns:
        list: Itens presentes em lista1 que não estão em lista2.
    """

    return list(set(following) - set(followers))

# ───────────────────────────────────────────────────────────────
# 👇 8. Função principal
# ───────────────────────────────────────────────────────────────


def get_ghost_following(username):
    """
    Executa o script principal para analisar seguidores no GitHub.

    Passos:
    1. Solicita ao usuário seu nome de usuário do GitHub.
    2. Busca a lista de usuários que ele segue.
    3. Busca a lista de usuários que o seguem.
    4. Compara as listas e identifica quem não o segue de volta.
    5. Exibe o resultado no terminal.

    Requer conexão com a internet e depende da API pública do GitHub.
    Limite de 60 requisições por hora sem autenticação.
    """
    # print("👻 Ghost Following - Descubra quem não te segue de volta no GitHub\n")

    # Solicita o nome de usuário
    # username = input("👤 Informe seu nome de usuário do GitHub: ").strip()

    # Monta as URLs para buscar os dados da API
    following_url = f"https://api.github.com/users/{username}/following?per_page=100"
    followers_url = f"https://api.github.com/users/{username}/followers?per_page=100"

    print("📥 Buscando seguidores...")
    followers_data = get_all_pages(followers_url, token)
    print(f"✅ {len(followers_data)} seguidores encontrados.")

    print("📤 Buscando usuários que você segue...")
    following_data = get_all_pages(following_url, token)
    print(f"✅ {len(following_data)} usuários sendo seguidos.")

    # Conjuntos de logins para comparação
    following = get_usernames(following_data)
    followers = get_usernames(followers_data)

    # Identifica quem você segue mas não te segue de volta
    not_following_back = following - followers
   
    return not_following_back
