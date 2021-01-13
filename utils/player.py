from card.py import Card, Deck
from random import random

class Players:
    """
    The game first ask the number of players.
    :attrib num_of_players - indicates the number of players
    :attrib player_name - input name by the player
    :attrib num_of_cards - number of cards to be played
    """ 
    def __init__(self, num_of_players, player_list = [], player_name, num_of_cards):
        self.num_of_players = num_of_players
        self.player_name = player_name
        self.num_of_cards = num_of_cards
        self.player_list = player_list
        
    def playerlist(self): 
        """
        Asks input for the playerlist, and also asks the player name
        """
        print("This game requires number of players from 2 to 5 people.")
        num_of_players = int(input("Please enter number of players:  "))
        if num_of_players <= 1 or num_of_players > 5:
            print("Please enter number more than 1 or less than 6")
        else:
            for i in range(num_of_players):
                name = input(f"Please enter name of Player {i+1}: ")
                player_name = f"Player {i+1}: {name}"
                player_list.append(player_name)
            return player_list
    

class Player(Players):
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
        turn_count = 0
        num_of_cards = 0
        history = []
        Deck.distribute(self)
        current_cards = card_distrib[player_list[i]]
        chosen_card = input(f"Choose the card you want to play from: {current_cards}")
        history.append(chosen_card)
        current_cards.remove(chosen_card)
        turn_count += 1
        print(f"Player: {player_name} - Turn Count: {turn_count} Played: {chosen_card}")
        return chosen_card




