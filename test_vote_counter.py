# test_vote_counter.py

import unittest
from unittest.mock import patch, mock_open
from vote_counter import count_votes  # Se asume que `count_votes` está en `vote_counter.py`

class TestVoteCounter(unittest.TestCase):

    @patch("builtins.print")
    def test_count_votes_valid_file(self, mock_print):
        # Simula un archivo CSV con datos válidos de votos
        mock_csv = """city,candidate,votes
        Springfield,Alice,1200
        Springfield,Bob,750
        Shelbyville,Alice,2000
        Shelbyville,Bob,2500"""
        with patch("builtins.open", mock_open(read_data=mock_csv)):
            count_votes("votes.csv")
        
        # Verificación de la salida esperada después de contar los votos
        mock_print.assert_any_call("Alice: 3200 votos")
        mock_print.assert_any_call("Bob: 3250 votos")
        mock_print.assert_any_call("El ganador es Bob")
        self.assertEqual(mock_print.call_count, 3)

    @patch("builtins.print")
    def test_count_votes_invalid_votes(self, mock_print):
        # Simula un archivo CSV con datos de votos no válidos
        mock_csv = """city,candidate,votes
        Springfield,Bob,750
        Shelbyville,Alice,2000
        Springfield,Alice,invalid
        Shelbyville,Bob,2500"""
        with patch("builtins.open", mock_open(read_data=mock_csv)):
            count_votes("votes.csv")

        # Verificación de la salida cuando hay datos no válidos
        mock_print.assert_any_call("Bob: 3250 votos")
        mock_print.assert_any_call("Alice: 2000 votos")
        mock_print.assert_any_call("El ganador es Bob")
        self.assertEqual(mock_print.call_count, 3)

    @patch("builtins.print")
    def test_count_votes_tie(self, mock_print):
        # Simula un archivo CSV con un empate en los votos
        mock_csv = """city,candidate,votes
        Springfield,Alice,2000
        Springfield,Bob,2000
        Shelbyville,Alice,1500
        Shelbyville,Bob,1500"""
        with patch("builtins.open", mock_open(read_data=mock_csv)):
            count_votes("votes.csv")

        # Verificación de la salida en caso de empate
        mock_print.assert_any_call("Alice: 3500 votos")
        mock_print.assert_any_call("Bob: 3500 votos")
        # Dependiendo de cómo se maneje el empate, podríamos tener cualquier candidato como "ganador"
        # Aquí asumimos que el primer en la lista es el ganador en caso de empate
        mock_print.assert_any_call("El ganador es Alice")
        self.assertEqual(mock_print.call_count, 3)

if __name__ == "__main__":
    unittest.main()
