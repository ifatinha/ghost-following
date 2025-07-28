   ____ _           _     _     __ _ _                 
  / ___| |__   ___ | |__ (_)___/ _(_) | ___  ___  ___  
 | |  _| '_ \ / _ \| '_ \| / __| |_| | |/ _ \/ __|/ _ \ 
 | |_| | | | | (_) | | | | \__ \  _| | |  __/\__ \ (_) |
  \____|_| |_|\___/|_| |_|_|___/_| |_|\___||___/\___/ 

            Ghost followers? A gente mostra.



# 👻 ghost-following

Verifique quem você segue no GitHub, mas que não te segue de volta — em segundos.

Este script usa a API pública do GitHub para identificar os _"ghost followers"_, ou seja, usuários que você segue, mas que **não te seguem de volta**.

---

## 🔧 Funcionalidades

- Lista todos os usuários que você segue no GitHub
- Lista todos os seus seguidores
- Compara as listas e identifica quem **não te segue de volta**
- Suporte a paginação automática da API do GitHub
- Roda diretamente no terminal, sem necessidade de login (modo público)

---

## ▶️ Como usar

### 1. Instale o Python (caso ainda não tenha)

Acesse [https://www.python.org](https://www.python.org) e instale o Python.  
⚠️ Marque a opção **"Add Python to PATH"** na instalação.

### 2. Instale as dependências

Abra o terminal e rode:

```bash
pip install requests
```

### 3. Execute o script

```bash
python ghost-following.py
```

Digite seu nome de usuário do GitHub quando solicitado e aguarde o resultado.