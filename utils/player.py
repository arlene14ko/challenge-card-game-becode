from random import choice

class Player:
    """
    Class containing the Players
    :turn_count an int starting at 0
    :number_of_cards an int starting at 0
    :history is a list of (Card class) that will contain all the cards played by the player
    """

    def __init__(self, turn_count , number_of_cards, history, active_card):
        self.turn_count = turn_count
        self.number_of_cards = number_of_cards
        self.history = history
        self.active_card = active_card

    def play(name, cards):
        ''' Method play will allow the player to make a turn
            :parameter name contains the name of the player
            :parameter cards contains the list of cards the player currently have
            :attrib history will contain the history of cards the player played, starting at empty []
            :attrib active_card will the card the player chose during the turn
            This method will return the active_card
        '''
        turn_count = 0
        history = []
        active_card = choice(cards)
        history.append(active_card)
        turn_count +=1
        print(f"Player: {name} \nTurn Count: {turn_count} \nPlayed: {active_card}\nPlayer History: {history}")
        print("------------------------------------------")
        return active_card
