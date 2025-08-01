"""
Testes para o módulo ghost_following.py - Funções de comparação de listas de seguidores.
"""

import unittest
from util.ghost_following import difference_list


class TestDifferenceList(unittest.TestCase):
    """
    Testa a função difference_list, responsável por identificar usuários que você segue
    mas que não te seguem de volta.

    Esta classe contém casos de teste que verificam:
    - Cenário normal com seguidores e seguindo.
    - Listas vazias.
    - Listas idênticas (sem diferenças).
    """

    def test_users_not_following_back(self):
        """
        Testa se a função retorna corretamente os usuários que não seguem de volta.
        """
        followers = ['ana', 'bruno', 'carla']
        following = ['ana', 'bruno', 'carla', 'daniel', 'erica']
        expected = ['daniel', 'erica']
        result = difference_list(following, followers)
        self.assertCountEqual(result, expected)

    def test_empty_lists(self):
        """
        Testa o caso onde ambas as listas estão vazias.
        """
        self.assertCountEqual(difference_list([], []), [])

    def test_identical_lists(self):
        """
        Testa quando as duas listas têm os mesmos elementos (sem diferenças).
        """
        self.assertCountEqual(difference_list(["ana"], ["ana"]), [])
