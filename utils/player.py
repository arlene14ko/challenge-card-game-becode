from card.py import Card
from random import random

class Player:
    """
    Class containing the Players 
    :attrib cards imported from card.py (Card class)
    :turn_count an int starting at 0
    :number_of_cards an int starting at 0
    :history is a list of (Card class) that will contain all the cards played by the player
    """
    def __init__(self, cards, turn_count, number_of_cards, history = []):
        self.cards = Card
        self.turn_count = turn_count
        self.number_of_cards = number_of_cards
        self.history = history 

    def play(self):
        self.cards.random() = CARD_NUMBER
        self.history.append(CARD_NUMBER)
        print(f"{PLAYER_NAME} - {TURN_COUNT} played {CARD_NUMBER} {CARD_SYMBOL_ICON}.")
        return Card


