```

/ **\_| |** **\_ | |** (\_)**_/ _(_) | _** **\_ \_**
 | | _| '_ \ / _ \| '_ \| / **| |_| | |/ _ \/ **|/ _ \
| |_| | | | | (\_) | | | | \__ \ _| | | **/\__ \ (_) |
\_\_**|_| |_|\_**/|_| |_|_|_**/_| |_|\_**||\_**/\_\_\_/

            Ghost followers? A gente mostra.
```

# 👻 ghost-following

Verifique rapidamente quais usuários do GitHub você segue **mas que não te seguem de volta**.

---

## 📌 O que este projeto faz?

Este script usa a [API pública do GitHub](https://docs.github.com/pt/rest) para:

- buscar quem você segue (`following`)
- buscar seus seguidores (`followers`)
- listar quem **não te segue de volta**
- salvar o resultado em um arquivo CSV

---

## ⚙️ Requisitos

- Python 3.10+
- Biblioteca [`python-dotenv`](https://pypi.org/project/python-dotenv/)
- Conexão com a internet
- Token pessoal do GitHub (opcional, mas recomendado)

---

## 🧪 Instalação

    ```bash
    # Clone o repositório

    git clone https://github.com/ifatinha/ghost-following.git
    cd ghost-following

    ```

---

# Crie e ative um ambiente virtual (opcional)

python -m venv venv
venv\Scripts\activate # no Windows

# Instale as dependências

pip install -r requirements.txt

---

## 🔐 Configurando o token (opcional)

Crie um arquivo .env na raiz do projeto com:

```
GITHUB_TOKEN=ghp_seu_token_aqui
```

Você pode criar um token [`neste link`](https://github.com/settings/tokens) com o escopo "public_repo".

Usar o token evita limites baixos de requisições da API.

---

## 🚀 Como usar

```
python ghost_following.py
```

---

## 📄 Licença
Este projeto está licenciado sob os termos da MIT License.

## ✨ Autor
Feito com dedicação por ifatinha 🧠💻
[`ifatinha`](https://github.com/ifatinha)