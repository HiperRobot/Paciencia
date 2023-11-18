import tabuleiro


def criar_baralho():
  pass

def mover_carta():
  pass

def conta_carta():
  pass


def embaralha_cartas(baralho):
  pass


def coloca_carta(baralho):
  pass

def compra_carta():
  pass

def pilhas_completas():
  pass

def jogadas_possiveis():
  pass

import pygame
import sys

def inicia_jogo():  #tudo na partida.py
    # Inicializando o Pygame
    pygame.init()

    # Configurando a janela do jogo
    largura_tela = 800
    altura_tela = 600
    tela = pygame.display.set_mode((largura_tela, altura_tela))

    # Configurando o título da janela
    pygame.display.set_caption('Paciência Spider')

    # Criando um novo baralho
    baralho = criar_baralho()
    embaralha_cartas(baralho)
    coloca_carta(baralho)

    print()
    print("Bem-vindo(a) ao Paciência Spider!")
    print("Escolha uma jogada:")
    print("1: Comprar uma carta")
    print("2: Mover uma carta")
    print("3: Sair do jogo")
    print()

    # Loop principal do jogo
    while True:
        # Verificando os eventos
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        try:
            jogada = int(input("Qual jogada vc quer fazer?"))
        except ValueError:
            print("Por favor, insira um número.")
            continue

        print("Sua jogada foi:", jogada)
        if jogada == 1:
            compra_carta()
            print("Você comprou uma carta")
        if jogada == 2:
            mover_carta()
            print("Você moveu uma carta")
        if jogada == 3:
            print("Você escolheu sair do jogo.")
            return False  # Retorna False para indicar que o jogador escolheu sair do jogo
        if conta_carta() == 0 and jogadas_possiveis() == 0: # e não tiverem mais jogadas possiveis (descobrir como implementar isso)
            print("Você perdeu")
            return False  # Retorna False para indicar uma derrota
        if pilhas_completas():
            print("Você ganhou")
            return True  # Retorna True para indicar uma vitória

        # Atualizando a tela
        pygame.display.flip()

inicia_jogo()

# def IniciaJogo(): #apenas logica na partida.py (tela na tabuleiro.py) (nao ta funcionando mt bem)
#     # Inicializando o Pygame
#     pygame.init()

#     tabuleiro.mostraTabuleiro()

#     # Criando um novo baralho
#     baralho = criar_baralho()
#     embaralha_cartas(baralho)
#     coloca_carta(baralho)

#     print()
#     print("Bem-vindo(a) ao Paciência Spider!")
#     print("Escolha uma jogada:")
#     print("1: Comprar uma carta")
#     print("2: Mover uma carta")
#     print("3: Sair do jogo")
#     print()

#     # Loop principal do jogo
#     while True:
#         tabuleiro.atualiza()

#         try:
#             jogada = int(input("Qual jogada vc quer fazer?"))
#         except ValueError:
#             print("Por favor, insira um número.")
#             continue

#         jogada = int(input("Qual jogada vc quer fazer?"))
#         print("Sua jogada foi:", jogada)
#         if jogada == 1:
#             compra_carta()
#             print("Você comprou uma carta")
#         if jogada == 2:
#             mover_carta()
#             print("Você moveu uma carta")
#         if jogada == 3:
#             print("Você escolheu sair do jogo.")
#             return False  # Retorna False para indicar que o jogador escolheu sair do jogo
#         if conta_carta() == 0 and jogadas_possiveis() == 0: # e não tiverem mais jogadas possiveis (descobrir como implementar isso)
#             print("Você perdeu")
#             return False  # Retorna False para indicar uma derrota
#         if pilhas_completas():
#             print("Você ganhou")
#             return True  # Retorna True para indicar uma vitória

#         # Atualizando a tela
#         pygame.display.flip()

# IniciaJogo()

