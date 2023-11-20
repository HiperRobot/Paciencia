import partida
import pygame
import sys
import os

def criaMenu(status):
    pygame.init()

    # Configurações da tela
    largura_tela = 800
    altura_tela = 600
    tela = pygame.display.set_mode((largura_tela, altura_tela))

    # Define o título da janela
    pygame.display.set_caption("Menu Paciência Spider")

    # Carrega e redimensiona a imagem de fundo
    fundo = pygame.image.load(os.path.join('images', 'table_top.png'))
    fundo = pygame.transform.scale(fundo, (largura_tela, altura_tela))

    # Configurações da fonte
    fonte_grande = pygame.font.Font(None, 72)
    fonte_pequena = pygame.font.Font(None, 36)

    # Cria os retângulos para os botões
    botao_sim = pygame.Rect(largura_tela / 2 - 100, altura_tela / 2 + 100, 80, 50)
    botao_nao = pygame.Rect(largura_tela / 2 + 20, altura_tela / 2 + 100, 80, 50)

    # Cria o texto para os botões
    texto_sim = fonte_pequena.render("Sim", True, (255, 255, 255))
    texto_nao = fonte_pequena.render("Não", True, (255, 255, 255))

    # Armazena a posição do último clique do mouse
    ultimo_clique = None

    # Loop do menu
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                ultimo_clique = event.pos

        # Verifica se um botão foi clicado
        if ultimo_clique is not None:
            if botao_sim.collidepoint(ultimo_clique):
                return True
            elif botao_nao.collidepoint(ultimo_clique):
                return False

        # Verifica se o jogador quer jogar novamente
        keys = pygame.key.get_pressed()
        if keys[pygame.K_s]:
            return True
        elif keys[pygame.K_n]:
            return False

        # Desenha a imagem de fundo
        tela.blit(fundo, (0, 0))

        # Verifica o status da partida
        if status:
            texto1 = fonte_grande.render("Vitória!", True, (255, 255, 255))
        else:
            texto1 = fonte_grande.render("Derrota!", True, (255, 255, 255))

        texto2 = fonte_pequena.render("Jogar novamente?", True, (255, 255, 255))

        # Desenha o texto na tela
        tela.blit(texto1, (largura_tela / 2 - texto1.get_width() / 2, altura_tela / 2 - texto1.get_height() - 40))
        tela.blit(texto2, (largura_tela / 2 - texto2.get_width() / 2, altura_tela / 2 + 40))

        # Desenha os botões
        pygame.draw.rect(tela, (0, 100, 0), botao_sim)  # Botão Sim em verde escuro
        pygame.draw.rect(tela, (100, 0, 0), botao_nao)  # Botão Não em vermelho escuro

        # Desenha o texto dos botões
        tela.blit(texto_sim, (botao_sim.x + (botao_sim.width - texto_sim.get_width()) // 2, botao_sim.y + (botao_sim.height - texto_sim.get_height()) // 2))
        tela.blit(texto_nao, (botao_nao.x + (botao_nao.width - texto_nao.get_width()) // 2, botao_nao.y + (botao_nao.height - texto_nao.get_height()) // 2))

        # Atualiza a tela
        pygame.display.flip()

        # Limpa a posição do último clique
        ultimo_clique = None

def main():
    while True:
        status = partida.inicia_jogo()
        jogar_de_novo = criaMenu(status)
        if not jogar_de_novo:
            break

if __name__ == "__main__":
    main()



