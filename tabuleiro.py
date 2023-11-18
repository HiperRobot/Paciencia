import pygame
import sys

def mostraTabuleiro():
    # Configurando a janela do jogo
    largura_tela = 800
    altura_tela = 600
    tela = pygame.display.set_mode((largura_tela, altura_tela))

    # Configurando o título da janela
    pygame.display.set_caption('Paciência Spider')

def atualiza():
    # Verificando os eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # # Atualizando a tela
    # pygame.display.flip()
