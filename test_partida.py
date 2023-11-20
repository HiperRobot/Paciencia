import unittest
import partida

class TestPartida(unittest.TestCase):
    def test_inicia_jogo(self):
        # Testa se a função inicia_jogo não retorna nenhum erro
        try:
            partida.inicia_jogo()
        except Exception as e:
            self.fail(f"partida.inicia_jogo() raised {type(e).__name__} unexpectedly!")

    def test_compra_carta(self):
        # Testa se a função compra_carta não retorna nenhum erro
        try:
            partida.compra_carta()
        except Exception as e:
            self.fail(f"partida.compra_carta() raised {type(e).__name__} unexpectedly!")

    def test_mover_carta(self):
        # Testa se a função mover_carta não retorna nenhum erro
        try:
            partida.mover_carta()
        except Exception as e:
            self.fail(f"partida.mover_carta() raised {type(e).__name__} unexpectedly!")

    def test_consulta_regras(self):
        # Testa se a função consulta_regras não retorna nenhum erro
        try:
            partida.consulta_regras()
        except Exception as e:
            self.fail(f"partida.consulta_regras() raised {type(e).__name__} unexpectedly!")

if __name__ == '__main__':
    unittest.main()
