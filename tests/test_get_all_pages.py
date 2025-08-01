"""
Módulo de testes para a função get_all_pages do arquivo ghost_following.py.

Este módulo utiliza o framework unittest e a biblioteca unittest.mock para
verificar o comportamento da função get_all_pages, que é responsável por
percorrer todos os resultados paginados de uma API do GitHub.

Testes realizados:
- Simulação de múltiplas páginas de resposta com dados acumulados.
- Verificação da interrupção da coleta ao fim da paginação.
- Uso de autenticação simulada.
"""

import unittest
from unittest.mock import patch, MagicMock
from util.ghost_following import get_all_pages


class TestGetAllPage(unittest.TestCase):
    """
    Testa a função get_all_pages, que coleta resultados paginados da API do GitHub.
    """

    @patch('ghost_following.make_authenticated_request')
    def test_get_all_pages_multiple(self, mock_request):
        """
        Testa se a função retorna corretamente os dados de várias páginas.
        """

        # Simula duas páginas com dados
        response_page_1 = MagicMock()
        response_page_1.json.return_value = [{"user": "john"}, {"user": "jane"}]
        response_page_1.links = {'next': {'url': 'https://api.github.com/page2'}}
        response_page_1.raise_for_status.return_value = None

        response_page_2 = MagicMock()
        response_page_2.json.return_value = [{"user": "sully"}]
        response_page_2.links = {}
        response_page_2.raise_for_status.return_value = None

        # O mock retorna essas duas páginas em sequência
        mock_request.side_effect = [response_page_1, response_page_2]

        url = 'https://api.github.com/fake-endpoint'
        result = get_all_pages(url)

        expected = [{'user': 'john'}, {'user': 'jane'}, {'user': 'sully'}]
        self.assertEqual(result, expected)
