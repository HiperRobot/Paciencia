# partida de paciência
import random

# Crie um baralho de cartas
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

deck = [{'rank': rank, 'suit': suit} for suit in suits for rank in ranks]
random.shuffle(deck)

# Inicialize as pilhas
tableau = [[] for _ in range(7)]
foundation = {suit: [] for suit in suits}
waste = []

def display_cards(cards):
    """Exibe as cartas no formato 'Rank de Suit'."""
    return [f"{card['rank']} of {card['suit']}" for card in cards]

def display_tableau():
    """Exibe o tableau do jogo."""
    for i, stack in enumerate(tableau):
        print(f"{i + 1}: {display_cards(stack)}")

def display_foundation():
    """Exibe as fundações do jogo."""
    for suit, cards in foundation.items():
        print(f"{suit} foundation: {display_cards(cards)}")

def main():
    while True:
        print("\nJogo de Paciência")
        print("1. Mostrar Tableau")
        print("2. Mostrar Fundações")
        print("3. Sair")

        choice = input("Escolha uma opção: ")

        if choice == "1":
            display_tableau()
        elif choice == "2":
            display_foundation()
        elif choice == "3":
            break
        else:
            print("Escolha inválida. Tente novamente.")

if __name__ == "__main__":
    main()

