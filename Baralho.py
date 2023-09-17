import random

# Função para criar e embaralhar um baralho
def criar_baralho():
    naipes = ['♠', '♥', '♦', '♣']
    valores = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    baralho = [{'valor': valor, 'naipe': naipe} for naipe in naipes for valor in valores]
    random.shuffle(baralho)
    return baralho