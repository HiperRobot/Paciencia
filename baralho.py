import random

def criar_baralho():
    naipes = ['S', 'H', 'D', 'C']
    valores = ['A','2', '3', '4', '5', '6', '7', '8', '9', '10','J','Q','K']
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

# def compra_carta(tabuleiro, baralho, visivel=True):
#     for slot in tabuleiro:
#         if not baralho:
#             print("O baralho está vazio.")
#             return False

#         carta = baralho.pop(0)
#         slot.append(carta)
#         carta[-1] = visivel
#     return True

def compra_carta(tabuleiro, baralho, visivel=True):
    for slot in tabuleiro:
        if not baralho:
            print("O baralho está vazio.")
            return False

        carta = baralho.pop(0)
        while carta[-1]:  # Verifica se a carta já foi jogada
            baralho.append(carta)  # Adiciona a carta de volta ao baralho
            carta = baralho.pop(0)  # Pega uma nova carta

        slot.append(carta)
        carta[-1] = visivel

    return True


# def enviar_cartas(tabuleiro, baralho, quantidade):
#     for _ in range(quantidade):
#         tabuleiro.append(baralho.pop(0))

def cards():
  return {'JH': 'JH.png',
          'QD': 'QD.png',
          '3C': '3C.png',
          '6C': '6C.png',
          '9H': '9H.png',
          '7H': '7H.png',
          '8H': '8H.png',
          '3D': '3D.png',
          '5C': '5C.png',
          '8D': '8D.png',
          'AD': 'AD.png',
          'AC': 'AC.png',
          '5D': '5D.png',
          '10H': '10H.png',
          '3H': '3H.png',
          '9C': '9C.png',
          '9S': '9S.png',
          '4H': '4H.png',
          '9D': '9D.png',
          'JS': 'JS.png',
          '4D': '4D.png',
          '7S': '7S.png',
          '8C': '8C.png',
          '10D': '10D.png',
          '4S': '4S.png',
          '10C': '10C.png',
          'AH': 'AH.png',
          '2H': '2H.png',
          '10S': '10S.png',
          '3S': '3S.png',
          '5H': '5H.png',
          'JD': 'JD.png',
          '6D': '6D.png',
          'KH': 'KH.png',
          '7D': '7D.png',
          '6H': '6H.png',
          'JC': 'JC.png',
          '2C': '2C.png',
          '8S': '8S.png',
          'AS': 'AS.png',
          'KD': 'KD.png',
          '5S': '5S.png',
          'QC': 'QC.png',
          '6S': '6S.png',
          'KC': 'KC.png',
          '4C': '4C.png',
          'KS': 'KS.png',
          'QS': 'QS.png',
          '7C': '7C.png',
          '2S': '2S.png',
          'QH': 'QH.png',
          '2D': '2D.png',
          'blue_back': 'blue_back.png',
          }
