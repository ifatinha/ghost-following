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
import requests

# Função auxiliar para lidar com a paginação da API do GitHub


def get_all_pages(url):
    """
    Coleta todos os resultados de uma URL paginada da API do GitHub.

    A API do GitHub retorna no máximo 100 itens por página.
    Esta função segue os links de paginação (se houver) para obter todos os dados.

    Parâmetros:
        url (str): A URL inicial da requisição (com `?per_page=100` já incluso).

    Retorna:
        list: Lista de dicionários representando os usuários retornados pela API.
    """

    results = []

    while url:
        response = requests.get(url, timeout=30)
        response.raise_for_status()  # Interrompe se a requisição falhar.
        results.extend(response.json())  # Adiciona os dados da página atual
        # Verifica se a uma próxima página na resposta
        url = response.links.get("next", {}).get(url)
    return results

# Extrai apenas os nomes de usuário (login) de cada item retornado pela API


def get_usernames(data):
    """
    Extrai os nomes de usuário (login) de uma lista de dicionários de usuários.

    Parâmetros:
        data (list): Lista de dicionários retornados pela API do GitHub.

    Retorna:
        set: Conjunto com os nomes de usuário (strings) únicos.
    """
    return {user["login"] for user in data}


# Função principal do script
def main():
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
    print("👻 Ghost Following - Descubra quem não te segue de volta no GitHub\n")

    # Solicita o nome de usuário
    username = input("Digite seu nome de usuário do Github: ").strip()

    # Monta as URLs para buscar os dados da API
    following_url = f"https://api.github.com/users/{username}/following?per_page=100"
    followers_url = f"https://api.github.com/users/{username}/followers?per_page=100"

    print("\n🔎 Buscando usuários que você segue...")
    following_data = get_all_pages(following_url)

    print("🔎 Buscando seus seguidores...")
    followers_data = get_all_pages(followers_url)

    # Conjuntos de logins para comparação
    following = get_usernames(following_data)
    followers = get_usernames(followers_data)

    # Diferença entre conjuntos: quem você segue mas não te segue
    not_following_back = following - followers

    print("\n📋 Resultado:")
    if not not_following_back:
        print("🎉 Todos os usuários que você segue também te seguem de volta!")
    else:
        print("👥 Usuários que você segue mas que **não te seguem de volta**:\n")
        for user in sorted(not_following_back):
            print(f" - {user}")


if __name__ == "__main__":
    main()
