from random import random
from player import Player

class Symbol:
    """
    Class that shows the symbols of the cards.
    :attrib color is a string
    :attrib icon is a single character out of this list ['♥','♦','♣','♠']
    """
    def __init__(self, color, icon):
        self.color = color
        self.icon = icon

    def symbol(self, color, icon):
        icon = ['♥','♦','♣','♠']
        color = ['red', 'black']
        for i in range(0, len(icon)):
            if icon[i] == '♥':
                return(f"{color[0]} \u2764\uFE0F")
            elif icon[i] == '♦':
                return(f"{color[0]} \u2666")
            elif icon[i] == '♣':
                return(f"{color[1]} \u2663")
            elif icon[i] == '♠':
                return(f"{color[1]} \u2660")

class Card(Symbol):
    """
    Class that inherits from the class Symbol and contains the color, icon and value of the cards
    :attrib value is a string one of this = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', ])
    """
    def __init__(self, color, icon, value):
        super().__init__(color, icon)
        self.value = value 
    
    def cards(self, icon, value):
        value = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        for x in range(0, len(icon)):
            for y in range(0, len(value)):
                return icon[x] + value[y]

class Deck(Card):
    """
    Class that contains all the 52 cards (deck)
    """
    def __init__(self, cards = [color, icon, value]):
        super().__init__(cards)
        self.cards = cards
    
    def fill_deck(self, icon, value):
        # function that will fill the deck of 52 cards
        filldeck = [] # list will contain all 52 cards
        for x in range(0, len(icon)):
            for y in range(0, len(value)):
                filldeck.append(Card.cards(self))
        return filldeck

    def shuffle(self):
        # function that will shuffle the list of cards
        return random.shuffle(fill_deck(self))

    def distribute(self, player_list, num_of_players): #number of players
        #function that will distribute cards evenly b/w players
        self.shuffle()
        if num_of_players == 2:
            card_distrib = {
                player_list[0] : fill_deck[0:26],
                player_list[1] : fill_deck[26:52]
            }
        elif num_of_players == 3:
            card_distrib = {
                player_list[0] : fill_deck[0:17],
                player_list[1] : fill_deck[17:34],
                player_list[2] : fill_deck[34:51]
            }
        elif num_of_players == 4:
            card_distrib = {
                player_list[0] : fill_deck[0:13],
                player_list[1] : fill_deck[13:26],
                player_list[2] : fill_deck[26:39],
                player_list[3] : fill_deck[39:52]
            }
        elif num_of_players == 5:
            card_distrib = {
                player_list[0] : fill_deck[0:10],
                player_list[1] : fill_deck[10:20],
                player_list[2] : fill_deck[20:30],
                player_list[3] : fill_deck[30:40],
                player_list[4] : fill_deck[40:50]
            }
        return card_distrib
        






