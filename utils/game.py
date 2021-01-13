from player.py import Player
from card.py import Deck

class Board:
    """
    Class containing the gameboard 
    :attrib players that is a list of Player (player class)
    :attrib turn_count an int
    :attrib active_cards will contain the last card played by each player
    :attrib history_cards contains all the cards except the 'active_cards'
    """
    def __init__(self, Players, turn_count, active_cards, history_cards = []):
        self.players = Players
        self.turn_count = turn_count
        self.active_cards = active_cards
        self.history_cards = history_cards 

    def start_game(self):
        # start the game
        #fill a Deck - import Deck from card.py
        Deck.fill_deck(self)
        Deck.shuffle()
        Deck.distribute() 
        for i in number_of_cards:
            Player.play(Card) #player should only play 1 card per turn (loop)
            return(f"Player: {Player_name} Turn Count: {turn_count} List of Active Cards: {active_cards} History: {history_cards})

