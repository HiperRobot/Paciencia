# import pygame
# import sys
# #import paciencia
# #import tabuleiro
# #import Baralho

# def main():
#     # Inicializando o Pygame
#     pygame.init()

#     # Configurando a janela do jogo
#     largura_tela = 800
#     altura_tela = 600
#     tela = pygame.display.set_mode((largura_tela, altura_tela))

#     # Configurando o título da janela
#     pygame.display.set_caption('Paciência Spider')

#     # Criando uma nova partida
#     #partida = Partida()

#     # Loop principal do jogo
#     while True:
#         # Verificando os eventos
#         for evento in pygame.event.get():
#             if evento.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()

#         # Atualizando a tela
#         pygame.display.flip()

#         # Verificando o estado da partida
#         #if partida.acabou():
#             # Mostrando o menu de fim de jogo
#             #mostrar_menu_fim_de_jogo()

#             # Começando uma nova partida se o jogador escolher
#             #if jogador_quer_nova_partida():

# if __name__ == "__main__":
#     main()

import partida


def criaMenu(status):  #status pode ser vitoria(True) ou derrota(False)
    # Implemente a lógica para criar o menu aqui
    # Retorne True se o jogador quiser jogar de novo, False caso contrário
    pass

def main():
    while True:
        status = partida.inicia_jogo()
        jogar_de_novo = criaMenu(status)
        if not jogar_de_novo:
            break

if __name__ == "__main__":
    main()



