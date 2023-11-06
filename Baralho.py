import random

def criar_baralho():
    naipes = ['♠', '♥', '♦', '♣']
    valores = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    baralho = [[valor, naipe,False] for naipe in naipes for valor in valores]
    random.shuffle(baralho)
    return baralho




def conta_cartas(baralho):
  print(len(baralho))



def embaralha_cartas(baralho):
  novobaralho= random.shuffle(baralho)
  return novobaralho

def compra_carta(tabuleiro, baralho):
  for slot in tabuleiro:
      
      if not baralho:
          print("O baralho está vazio.")
          break
      
      carta = baralho.pop(0)
      
      slot.append(carta)
     
      carta[-1] = True



