"""
Testes para o módulo ghost_following.py
"""
import unittest
from ghost_following import difference_list


class TestGhostFollowing(unittest.TestCase):
    """
    Classe de testes para o módulo ghost_following.py.

    Testa a função diferenca_listas para garantir que a lógica de comparação de listas
    funcione corretamente, retornando elementos únicos de uma lista em relação à outra.
    """

    def test_difference_lists(self):
        """
        Testa se a função retorna corretamente os usuários que não seguem de volta.
        """
        followers = ['ana', 'bruno', 'carla']
        following = ['ana', 'bruno', 'carla', 'daniel', 'erica']
        expected = ['daniel', 'erica']
        result = difference_list(following, followers)
        self.assertEqual(result, expected)

    def test_diference_lists_empty(self):
        """
        Testa o caso onde ambas as listas estão vazias.
        """
        self.assertEqual(difference_list([], []), [])

    def test_diference_lists_inverted(self):
        """
        Testa quando as duas listas têm os mesmos elementos.
        """
        self.assertEqual(difference_list(["ana"], ["ana"]), [])
