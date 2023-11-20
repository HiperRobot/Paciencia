import pygame
import sys
import os

def mostra_tabuleiro():
    pygame.init()

    # Configurações da tela
    largura_tela = 800
    altura_tela = 600
    tela = pygame.display.set_mode((largura_tela, altura_tela))

    # Define o título da janela
    pygame.display.set_caption("Tabuleiro Paciência Spider")

    # Carrega e redimensiona a imagem de fundo
    fundo = pygame.image.load(os.path.join('images', 'table_top.png'))
    fundo = pygame.transform.scale(fundo, (largura_tela, altura_tela))


    #slot do baralho
    largura_carta = 70
    altura_carta = 90
    slot_baralho = pygame.Rect(10, 10, largura_carta, altura_carta)

    # Carrega a imagem da carta
    imagem_carta = pygame.image.load(os.path.join('images', 'cards', 'blue_back.png'))

    # Redimensiona a imagem para ter o mesmo tamanho que uma carta
    imagem_carta = pygame.transform.scale(imagem_carta, (largura_carta, altura_carta))

    slots_sequencias_completas = []
    for i in range(8):
        slots_sequencias_completas.append(pygame.Rect(170 + i * (largura_carta + 10), 10, largura_carta, altura_carta))


    # Inicializa a matriz das cartas das pilhas
    matriz_cartas_pilhas = []
    # slots_pilhas = []

    # Para cada coluna
    for i in range(10):
    # Cria uma lista para representar a coluna de cartas
        coluna_cartas = []
        coluna_cartas.append(pygame.Rect(10 + i * (largura_carta + 10), 120, largura_carta, altura_carta))

        # Adiciona cartas à coluna
        for j in range(18):
            # Aqui você pode adicionar a carta à coluna.
            # Por enquanto, vamos usar um retângulo do Pygame para representar uma carta.
            if j == 0:  # Para a primeira carta, use a posição original
                pos_y = 120
            else:  # Para as outras cartas, suba 3/4 da altura da carta
                pos_y = 120 + j * (altura_carta / 4)
            retangulo_carta = pygame.Rect(10 + i * (largura_carta + 10), pos_y, largura_carta, altura_carta)
            coluna_cartas.append(retangulo_carta)


        # Adiciona a coluna de cartas à matriz
        matriz_cartas_pilhas.append(coluna_cartas)


    # Loop do menu
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Desenha a imagem de fundo
        tela.blit(fundo, (0, 0))

        # Desenha o slot do baralho
        # No seu loop de menu, substitua a linha que desenha o retângulo do slot do baralho por esta linha:
        tela.blit(imagem_carta, (10, 10))
        # pygame.draw.rect(tela, (255, 255, 255), slot_baralho)

        # Desenha os slots das sequências
        for i in range(8):
            pygame.draw.rect(tela, (255, 255, 255), slots_sequencias_completas[i])

        # Desenha os slots das pilhas
        for i in range(len(matriz_cartas_pilhas)):
            for j in range(len(matriz_cartas_pilhas[i])):
                # Se estamos nas primeiras 4 colunas e nas primeiras 5 cartas, desenhe a carta
                if i < 4 and j < 5:
                    tela.blit(imagem_carta, matriz_cartas_pilhas[i][j].topleft)
                # Se estamos nas próximas 6 colunas e nas primeiras 3 cartas, desenhe a carta
                elif 4 <= i < 10 and j < 4:
                    tela.blit(imagem_carta, matriz_cartas_pilhas[i][j].topleft)






        # Atualiza a tela
        pygame.display.flip()



def coloca_carta():
    # Coloca cartas no tabuleiro
    # ...
    pass

def clica_carta():
    # Chama a função mover_carta quando o jogador clicar em uma carta para aplicar o movimento de carta
    # ...
    pass

def mostra_qtd_cartas():
    # Printa o número de cartas que podem ser compradas na pilha de compras
    # ...
    pass

def clica_pilha_compras():
    # Chama a função compra_carta() quando o jogador clica na pilha de compras
    # ...
    pass

def coloca_sequencia():
    # Coloca as sequências formadas nos slots de sequências formadas
    # ...
    pass

mostra_tabuleiro()