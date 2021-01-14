from random import choice

class Player:
    """
    Class containing the Players
    :turn_count an int starting at 0
    :number_of_cards an int starting at 0
    :history is a list of (Card class) that will contain all the cards played by the player
    """

    def __init__(self, turn_count, number_of_cards, history, active_card):
        self.turn_count = turn_count
        self.number_of_cards = number_of_cards
        self.history = history
        self.active_card = active_card

    def play(name, cards):
        # function that will allow  make the player to make a turn
        active_card = choice(cards)
        print(
            f"Player: {name} --- Played: {active_card}"
        )
        return active_card
