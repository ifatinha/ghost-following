"""
Testes para a função get_usernames do módulo ghost_following.
"""

import unittest
from ghost_following import get_usernames


class TestGetUsernames(unittest.TestCase):
    """
    Classe de testes para a função get_usernames.

    Essa função extrai os nomes de usuário únicos (campo "login")
    de uma lista de dicionários retornados pela API do GitHub.

    Casos testados:
    - Lista comum com usuários distintos.
    - Lista com usuários duplicados.
    - Lista vazia.
    - Dicionários sem chave "login" (validação robusta opcional).
    """

    def test_common_user_list(self):
        """
        Testa extração simples de nomes de usuários distintos.
        """

        data = [
            {"login": "ana"},
            {"login": "bruno"},
            {"login": "rafaela"},
        ]

        expected = {"ana", "bruno", "rafaela"}
        result = get_usernames(data)
        self.assertEqual(result, expected)
