from player import Player
from card import Deck

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

    def start_game(self, player_list, card_distrib, num_of_players, current_cards, chosen_card, player_name, active_card):
        # start the game
        print("Welcome players! We are going to play a card game. You will be given same amount of cards and you need to draw the highest number each turn to have a point. The player who has most points will be the winner!")
        
        #asking input from players from player.py (class Player)
        Player.playerlist() 
        print(f"Welcome {player_list}!. We will now start the game. Good luck!")

        #importing the Deck from card.py (class Deck )
        #fill deck function to fill the deck of 52 cards
        Deck.fill_deck()
        #shuffle deck function to shuffle the deck
        Deck.shuffle()
        #distribute the deck to the players
        Deck.distribute() 

        #looping the number of times the game will play
        active_cards = []
        history_cards = []
        while current_cards > 0:
            for num in player_list:
                Player.play() #chosen_card should be returned player should only play 1 card per turn (loop)
                active_cards.append(active_card)
                history_cards.append(active_cards) 
                print(f"Player: {player_name} Turn Count: {turn_count} List of Active Cards: {active_cards} History: {history_cards[:-1]}.")
        print("Game over! Hope you had fun! :) ")

