"""
Testes para o módulo ghost_following.py
"""
import unittest
import requests
from unittest.mock import patch, Mock
from ghost_following import difference_list
from ghost_following import make_authenticated_request


class TestGhostFollowing(unittest.TestCase):
    """
    Classe de testes automatizados para verificar o comportamento das funções
    principais do módulo ghost_following.

    Utiliza o framework unittest para validar:
        - Comparação de listas de seguidores e seguidos.
        - Requisições autenticadas à API do GitHub.
        - Coleta de dados de seguidores/seguidos.
        - Tratamento de exceções e erros de rede.

    Cada método desta classe testa uma função específica, garantindo que o
    código funcione corretamente e continue robusto a alterações futuras.
    """

    def test_difference_lists(self):
        """
        Testa se a função retorna corretamente os usuários que não seguem de volta.
        """
        followers = ['ana', 'bruno', 'carla']
        following = ['ana', 'bruno', 'carla', 'daniel', 'erica']
        expected = ['daniel', 'erica']
        result = difference_list(following, followers)
        self.assertCountEqual(result, expected)

    def test_diference_lists_empty(self):
        """
        Testa o caso onde ambas as listas estão vazias.
        """
        self.assertCountEqual(difference_list([], []), [])

    def test_diference_lists_inverted(self):
        """
        Testa quando as duas listas têm os mesmos elementos.
        """
        self.assertCountEqual(difference_list(["ana"], ["ana"]), [])

    @patch("ghost_following.requests.get")
    def test_make_authenticated_request_without_token(self, mock_get):
        """
        Testa se a função realiza requisição corretamente sem token.
        """
        # Simulando resposta bem-sucedida
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.raise_for_status = Mock()
        mock_get.return_value = mock_response

        url = "https://api.github.com/users/ifatinha"
        response = make_authenticated_request(url)
        mock_get.assert_called_once_with(url, headers={}, timeout=30)
        self.assertEqual(response.status_code, 200)

    @patch('ghost_following.requests.get')
    def test_make_authenticated_request_with_token(self, mock_get):
        """
        Testa se a função adiciona o cabeçalho Authorization corretamente quando um token é fornecido.
        """

        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.raise_for_status = Mock()
        mock_get.return_value = mock_response

        url = "https://api.github.com/users/ifatinha"
        token = "fake-token"
        response = make_authenticated_request(url, token)

        mock_get.assert_called_once_with(
            url,
            headers={"Authorization": "token fake-token"},
            timeout=30
        )

        self.assertEqual(response.status_code, 200)

    @patch('ghost_following.requests.get')
    def test_make_authenticated_request_raises_http_error(self, mock_get):
        """
        Testa se a função levanta uma exceção HTTPError quando a resposta falha.
        """

        mock_response = Mock()
        mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError("Erro 404")
        mock_get.return_value = mock_response
        url = "https://api.github.com/users/usuario-invalido"

        with self.assertRaises(requests.exceptions.HTTPError):
            make_authenticated_request(url)
