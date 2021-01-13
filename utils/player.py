from card import Card, Deck
from random import random

class Player():
    """
    Class containing the Players 
    :attrib cards imported from card.py (Card class)
    :turn_count an int starting at 0
    :number_of_cards an int starting at 0
    :history is a list of (Card class) that will contain all the cards played by the player
    """
    def __init__(self, cards, turn_count, number_of_cards, history, num_of_players, player_list, player_name):
        self.cards = cards
        self.turn_count = turn_count
        self.number_of_cards = number_of_cards
        self.history = history 
        self.num_of_players = num_of_players
        self.player_list = player_list
        self.player_name = player_name

    def playerlist(self):
        """
        Asks input for the number of players, and also asks the player name
        """
        player_list = []
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

    def play(self, card_distrib, num):
        turn_count = 0
        num_of_cards = 0
        history = []
        Deck.distribute()
        
        # will delete this later. only used for debugging
        print(card_distrib)

        current_cards = card_distrib[player_list[num]]
        active_card = input(f"Choose the card you want to play from: {current_cards}")
        history.append(active_card)
        current_cards.remove(active_card)
        turn_count += 1
        print(f"Player: {player_name} - Turn Count: {turn_count} Played: {active_card}")
        return active_card




