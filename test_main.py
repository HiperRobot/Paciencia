import unittest
from unittest.mock import patch
import main

class TestMain(unittest.TestCase):
    @patch('main.criaMenu')
    @patch('main.partida.IniciaJogo')
    def test_main(self, mock_IniciaJogo, mock_criaMenu):
        mock_IniciaJogo.return_value = True
        mock_criaMenu.return_value = False
        main.main()
        mock_IniciaJogo.assert_called_once()
        mock_criaMenu.assert_called_once()

if __name__ == '__main__':
    unittest.main()
