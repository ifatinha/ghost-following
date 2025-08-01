"""
Testes para a função export_to_csv do módulo ghost_following.
"""

import os
import csv
import unittest
from util.ghost_following import export_to_csv


class TestExportCSV(unittest.TestCase):
    """
    Classe de testes para a função export_to_csv, responsável por exportar usuários
    para um arquivo CSV no formato esperado.
    """

    def setUp(self):
        """
        Configuração executada antes de cada teste.
        Define o nome do arquivo temporário para testes.
        """

        self.test_file = "data/test_output.csv"
        # Garante que não exista antes do teste
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def tearDown(self):
        """
        Limpeza após cada teste. Remove o arquivo gerado.
        """
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_export_creates_csv_file(self):
        """
        Testa se o arquivo CSV é criado corretamente com os dados fornecidos.
        """

        usernames = {"Bianca", "Camila", "Eduarda"}
        export_to_csv(usernames, filename=self.test_file)

        # Verifica se o arquivo foi criado
        self.assertTrue(os.path.exists(self.test_file))

        # Lê o conteúdo e verifica se os dados estão corretos
        with open(self.test_file, newline="", encoding="utf-8") as file:
            reader = list(csv.reader(file))
            header = reader[0]
            content = reader[1:]

            self.assertEqual(header, ["Usuarios que você segue, mas que não te seguem de volta"])
            exported_usernames = {row[0] for row in content}
            self.assertEqual(exported_usernames, usernames)
