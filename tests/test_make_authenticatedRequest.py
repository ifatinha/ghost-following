"""
Módulo de testes unitários para o módulo ghost_following.

Este módulo contém a classe TestMakeAuthenticatedRequest, que verifica o
comportamento da função make_authenticated_request responsável por realizar
requisições GET autenticadas (ou não) à API do GitHub.

Os testes utilizam unittest e unittest.mock para simular chamadas HTTP e
assegurar que a função:
 - envia os cabeçalhos corretos conforme o uso do token;
 - retorna o objeto de resposta corretamente;
 - levanta exceções em caso de erros HTTP.

Executar este módulo ajuda a garantir a estabilidade e a correção da lógica
de autenticação e comunicação com a API do GitHub.
"""

import unittest
from unittest.mock import patch, Mock
import requests
from util.ghost_following import make_authenticated_request


class TestMakeAuthenticatedRequest(unittest.TestCase):
    """
    Classe de testes unitários para a função make_authenticated_request.

    Esta classe cobre os seguintes cenários:
    - Requisição bem-sucedida sem uso de token.
    - Requisição bem-sucedida com uso de token.
    - Tratamento de exceção HTTPError em caso de resposta inválida.

    O módulo unittest.mock é utilizado para simular o comportamento de requests.get,
    garantindo que os testes não façam chamadas reais à API do GitHub.
    """

    @patch("ghost_following.requests.get")
    def test_make_authenticated_request_without_token(self, mock_get):
        """
        Testa se a função realiza uma requisição GET corretamente sem token.

        Garante que a função retorna o objeto de resposta simulado e
        que o cabeçalho Authorization não é utilizado.
        """
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
        Testa se a função realiza uma requisição GET corretamente com token.

        Verifica se o cabeçalho Authorization foi corretamente incluído na chamada.
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
        Testa se a função trata corretamente um erro HTTP retornado pela API.

        Simula uma resposta com erro (raise_for_status lança HTTPError)
        e verifica se a exceção é de fato propagada pela função.
        """

        mock_response = Mock()
        mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError("Erro 404")
        mock_get.return_value = mock_response
        url = "https://api.github.com/users/inexistente"

        with self.assertRaises(requests.exceptions.HTTPError):
            make_authenticated_request(url)
