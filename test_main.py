import unittest
import main

class TestMain(unittest.TestCase):
    def test_criaMenu(self):
        # Testa se a função criaMenu não retorna nenhum erro
        try:
            main.criaMenu(True)
            main.criaMenu(False)
        except Exception as e:
            self.fail(f"main.criaMenu() raised {type(e).__name__} unexpectedly!")


    def test_main(self):
        # Testa se a função main não retorna nenhum erro
        try:
            main.main()
        except Exception as e:
            self.fail(f"main.main() raised {type(e).__name__} unexpectedly!")

if __name__ == '__main__':
    unittest.main()

