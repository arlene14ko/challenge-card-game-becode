from player.py import Player, Players
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
        self.players = players # getting the list of players from class Players (player.py)
        self.turn_count = turn_count
        self.active_cards = active_cards
        self.history_cards = history_cards 

    def start_game(self):
        # start the game
        print("Welcome players! We are going to play a card game. You will be given same amount of cards and you need to draw the highest number each turn to have a point. The player who has most points will be the winner!")
        
        #asking input from players from player.py (class Players)
        players.player_list(self) 
        print(f"Welcome {players.playerlist(self)}!. We will now start the game. Good luck!")

        #importing the Deck from card.py (class Deck )
        #fill deck function to fill the deck of 52 cards
        Deck.fill_deck(self)
        #shuffle deck function to shuffle the deck
        Deck.shuffle(self)
        #distribute the deck to the players
        Deck.distribute() 

        #looping the number of times the game will play
        num_of_plays = num_of_players * card_distrib[value]
        for i in number_of_cards:
            for x in num_of_players:
                Player.play(Card) #player should only play 1 card per turn (loop)
                print(f"Player: {Player_name} Turn Count: {turn_count} List of Active Cards: {active_cards} History: {history_cards})

