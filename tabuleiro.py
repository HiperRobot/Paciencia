import pygame
import sys
import os
import baralho

def mostra_tabuleiro(bolo_de_cartas):
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
    imagem_carta_fundo = pygame.image.load(os.path.join('images', 'cards', 'blue_back.png'))

    # Redimensiona a imagem para ter o mesmo tamanho que uma carta
    imagem_carta_fundo = pygame.transform.scale(imagem_carta_fundo, (largura_carta, altura_carta))

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
            # Aqui você adiciona a carta à coluna.
            if j == 0:  # Para a primeira carta, use a posição original
                pos_y = 120
            else:  # Para as outras cartas, suba 3/4 da altura da carta
                pos_y = 120 + j * (altura_carta / 4)
            if i < 4 and j < 5 or 4 <= i < 10 and j < 4:  # Se estamos nas primeiras 4 colunas e nas primeiras 5 cartas, ou nas próximas 6 colunas e nas primeiras 3 cartas
                carta = bolo_de_cartas.pop(0)  # Remove a carta do topo do bolo de cartas
                imagem_carta = pygame.image.load(os.path.join('images', 'cards', baralho.cards()[carta[0]+carta[1]]))  # Carrega a imagem da carta
                imagem_carta = pygame.transform.scale(imagem_carta, (largura_carta, altura_carta))  # Redimensiona a imagem para ter o mesmo tamanho que uma carta
                tela.blit(imagem_carta, (10 + i * (largura_carta + 10), pos_y))
            else:
                retangulo_carta = pygame.Rect(10 + i * (largura_carta + 10), pos_y, largura_carta, altura_carta)
                coluna_cartas.append(retangulo_carta)


        # Adiciona a coluna de cartas à matriz
        matriz_cartas_pilhas.append(coluna_cartas)
        #fim do loop for i in range(10):

    # imagens_cartas = {}
    # for carta in bolo_de_cartas:
    #     imagem = pygame.image.load(os.path.join('images', 'cards', baralho.cards()[carta[0]+carta[1]]))
    #     imagem = pygame.transform.scale(imagem, (largura_carta, altura_carta))
    #     imagens_cartas[tuple(carta)] = imagem



    # Loop principal
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Desenha a imagem de fundo
        tela.blit(fundo, (0, 0))

        # Desenha o slot do baralho
        tela.blit(imagem_carta_fundo, (10, 10))

        # Desenha os slots das sequências
        for i in range(8):
            pygame.draw.rect(tela, (255, 255, 255), slots_sequencias_completas[i])

        # # Desenha os slots das pilhas
        # for i in range(len(matriz_cartas_pilhas)):
        #     for j in range(len(matriz_cartas_pilhas[i])):
        #         if i < 4 and j < 5:
        #             if matriz_cartas_pilhas[i][j]:
        #                 if bolo_de_cartas:
        #                     carta = bolo_de_cartas.pop(0)
        #                     print(f"Desenhando carta {carta} na posição ({i}, {j})")
        #                     imagem_carta = imagens_cartas[carta]
        #                     tela.blit(imagem_carta, matriz_cartas_pilhas[i][j].topleft)
        #                     matriz_cartas_pilhas[i][j] = False
        #         elif 4 <= i < 10 and j < 4:
        #             if matriz_cartas_pilhas[i][j]:
        #                 if bolo_de_cartas:
        #                     carta = bolo_de_cartas.pop(0)
        #                     print(f"Desenhando carta {carta} na posição ({i}, {j})")
        #                     imagem_carta = imagens_cartas[carta]
        #                     tela.blit(imagem_carta, matriz_cartas_pilhas[i][j].topleft)
        #                     matriz_cartas_pilhas[i][j] = False


        # Desenha os slots das pilhas
        for i in range(len(matriz_cartas_pilhas)):
            for j in range(len(matriz_cartas_pilhas[i])):
                # Se estamos nas primeiras 4 colunas e nas primeiras 5 cartas, desenhe a carta
                if i < 4 and j < 5:
                    if matriz_cartas_pilhas[i][j]:  # Verifica se a posição da matriz está vazia
                        if bolo_de_cartas:  # Verifica se ainda há cartas no bolo_de_cartas
                            carta = bolo_de_cartas.pop(0)  # Remove a carta do topo do bolo de cartas
                            # print(f"Desenhando carta {carta} na posição ({i}, {j})")
                            imagem_carta = pygame.image.load(os.path.join('images', 'cards', baralho.cards()[carta[0]+carta[1]]))  # Carrega a imagem da carta
                            imagem_carta = pygame.transform.scale(imagem_carta, (largura_carta, altura_carta))  # Redimensiona a imagem para ter o mesmo tamanho que uma carta
                            tela.blit(imagem_carta, matriz_cartas_pilhas[i][j].topleft)
                            # matriz_cartas_pilhas[i][j] = False  # Atualiza a posição da matriz para indicar que não está mais vazia
                # Se estamos nas próximas 6 colunas e nas primeiras 3 cartas, desenhe a carta
                elif 4 <= i < 10 and j < 4:
                    if matriz_cartas_pilhas[i][j]:  # Verifica se a posição da matriz está vazia
                        if bolo_de_cartas:  # Verifica se ainda há cartas no bolo_de_cartas
                            carta = bolo_de_cartas.pop(0)  # Remove a carta do topo do bolo de cartas
                            # print(f"Desenhando carta {carta} na posição ({i}, {j})")
                            imagem_carta = pygame.image.load(os.path.join('images', 'cards', baralho.cards()[carta[0]+carta[1]]))  # Carrega a imagem da carta
                            imagem_carta = pygame.transform.scale(imagem_carta, (largura_carta, altura_carta))  # Redimensiona a imagem para ter o mesmo tamanho que uma carta
                            tela.blit(imagem_carta, matriz_cartas_pilhas[i][j].topleft)
                            # matriz_cartas_pilhas[i][j] = False  # Atualiza a posição da matriz para indicar que não está mais vazia

        # # Desenha os slots das pilhas
        # for i in range(len(matriz_cartas_pilhas)):
        #     for j in range(len(matriz_cartas_pilhas[i])):
        #         # Se estamos nas primeiras 4 colunas e nas primeiras 5 cartas, desenhe a carta
        #         if i < 4 and j < 5:
        #             if not matriz_cartas_pilhas[i][j]:  # Verifica se a posição da matriz está vazia
        #                 if bolo_de_cartas:  # Verifica se ainda há cartas no bolo_de_cartas
        #                     carta = bolo_de_cartas.pop(0)  # Remove a carta do topo do bolo de cartas
        #                     imagem_carta = pygame.image.load(os.path.join('images', 'cards', baralho.cards()[carta[0]+carta[1]]))  # Carrega a imagem da carta
        #                     imagem_carta = pygame.transform.scale(imagem_carta, (largura_carta, altura_carta))  # Redimensiona a imagem para ter o mesmo tamanho que uma carta
        #                     tela.blit(imagem_carta, matriz_cartas_pilhas[i][j].topleft)
        #                     matriz_cartas_pilhas[i][j] = True  # Atualiza a posição da matriz para indicar que está ocupada
        #         # Se estamos nas próximas 6 colunas e nas primeiras 3 cartas, desenhe a carta
        #         elif 4 <= i < 10 and j < 4:
        #             if not matriz_cartas_pilhas[i][j]:  # Verifica se a posição da matriz está vazia
        #                 if bolo_de_cartas:  # Verifica se ainda há cartas no bolo_de_cartas
        #                     carta = bolo_de_cartas.pop(0)  # Remove a carta do topo do bolo de cartas
        #                     imagem_carta = pygame.image.load(os.path.join('images', 'cards', baralho.cards()[carta[0]+carta[1]]))  # Carrega a imagem da carta
        #                     imagem_carta = pygame.transform.scale(imagem_carta, (largura_carta, altura_carta))  # Redimensiona a imagem para ter o mesmo tamanho que uma carta
        #                     tela.blit(imagem_carta, matriz_cartas_pilhas[i][j].topleft)
        #                     matriz_cartas_pilhas[i][j] = True  # Atualiza a posição da matriz para indicar que está ocupada




        # Atualiza a tela
        pygame.display.flip()

# def coloca_carta():
#     # Coloca cartas no tabuleiro
#     # ...
#     pass

# def clica_carta():
#     # Chama a função mover_carta quando o jogador clicar em uma carta para aplicar o movimento de carta
#     # ...
#     pass

# def mostra_qtd_cartas():
#     # Printa o número de cartas que podem ser compradas na pilha de compras
#     # ...
#     pass

# def clica_pilha_compras():
#     # Chama a função compra_carta() quando o jogador clica na pilha de compras
#     # ...
#     pass

# def coloca_sequencia():
#     # Coloca as sequências formadas nos slots de sequências formadas
#     # ...
#     pass

# Cria o bolo de cartas dos 2 baralhos (104 cartas)
baralho1 = baralho.criar_baralho()
baralho2 = baralho.criar_baralho()
bolo_de_cartas = baralho1 + baralho2  # Concatena as duas listas
baralho.embaralha_cartas(bolo_de_cartas)
# print(baralho)

# Coloca as cartas iniciais nos slots do tabuleiro
mostra_tabuleiro(bolo_de_cartas)