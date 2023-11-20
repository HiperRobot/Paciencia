# import random



# def contar_cartas(baralho):
#     return len(baralho)

# def embaralhar(baralho):
#     random.shuffle(baralho)

# def enviar_cartas(tabuleiro, baralho, quantidade):
#     for _ in range(quantidade):
#         tabuleiro.append(baralho.pop(0))


import random

def criar_baralho():
    naipes = ['♠', '♥', '♦', '♣']
    valores = ['1','2', '3', '4', '5', '6', '7', '8', '9', '10','11','12','13']
    baralho = [[valor, naipe,False] for naipe in naipes for valor in valores]
    random.shuffle(baralho)
    return baralho



def conta_cartas(baralho):
    """Retorna a quantidade de cartas no baralho que ainda não foram jogadas."""
    print(len(baralho)) # nao deveria ser a quantidade de cartas do baralho e sim a qauntidade de cartas com atributo foi jogada = False
    return len(baralho)



def embaralha_cartas(baralho):
    random.shuffle(baralho)
    return True

def compra_carta(tabuleiro, baralho, visivel=True):
    for slot in tabuleiro:
        if not baralho:
            print("O baralho está vazio.")
            return False

        carta = baralho.pop(0)
        slot.append(carta)
        carta[-1] = visivel
    return True