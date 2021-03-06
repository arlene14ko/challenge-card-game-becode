from random import shuffle # Importing Shuffle from random which we will use to shuffle the deck of cards

class Symbol:
    """ Class that shows the symbols of the cards.
        :attrib color is a string
        :attrib icon is a single character out of this list ['♥','♦','♣','♠']
    """

    def __init__(self, color, icon):
        self.color = color
        self.icon = icon

    def symbol():
        icon = ["♥", "♦", "♣", "♠"]
        symbol = []
        color = ["red", "black"]
        for i in range(0, len(icon)):
            if icon[i] == "♥":
                symbol.append({color[0]} + "\u2764\uFE0F")
            elif icon[i] == "♦":
                symbol.append({color[0]} + "\u2666")
            elif icon[i] == "♣":
                symbol.append({color[1]} + "\u2663")
            elif icon[i] == "♠":
                symbol.append({color[1]} + "\u2660")
        return symbol


class Card(Symbol):
    """ Class that inherits from the class Symbol and contains the color, icon and value of the cards
        :attrib value is a string one of this = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'  ])
    """

    def __init__(self, color, icon, value):
        super().__init__(color, icon)
        self.value = value

    def cards():
        card = []
        symbol = ["♥", "♦", "♣", "♠"]
        value = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        for x in range(0, len(symbol)):
            for y in range(0, len(value)):
                card.append(value[y] + symbol[x])
        return card


class Deck(Card):
    """ Class that inherits from the class Card and it will contain the deck of cards
        :attrib cards will contain the cards method from Card class
    """

    def __init__(self, color, icon, value, card):
        super().__init__(color, icon, value)

    def fill_deck():
        """ A method that will fill the deck of cards
            :attrib cards will contain the list of deck cards
            The cards is from the method cards from Card class
        """
        cards = []
        cards = Card.cards()
        return cards

    def shuffle(cards):
        """ A method that will fill shuffle the cards
            :parameter cards  contains the list of deck cards
            :shuffle() - imported from random, will shuffle the cards randomly
        """
        shuffle(cards)

    def distribute(num_of_players, player_list, cards):  
        """ A method that will distribute the cards evenly to all the players
            This method needs 3 parameteres:
                1. num_of_players - contains the number of players from the main.py
                2. player_list - contains the players name in a list from the main.py
                3. cards - contains the shuffled filled cards 
            :attrib card_distrib is a dictionary that will have the player_list and cards
            This method will return the card_distrib dictionary
        """
        card_distrib = {}
        if num_of_players == 2:
            card_distrib = {player_list[0]: cards[0:26], player_list[1]: cards[26:52]}
        elif num_of_players == 3:
            card_distrib = {
                player_list[0]: cards[0:17],
                player_list[1]: cards[17:34],
                player_list[2]: cards[34:51],
            }
        elif num_of_players == 4:
            card_distrib = {
                player_list[0]: cards[0:13],
                player_list[1]: cards[13:26],
                player_list[2]: cards[26:39],
                player_list[3]: cards[39:52],
            }
        elif num_of_players == 5:
            card_distrib = {
                player_list[0]: cards[0:10],
                player_list[1]: cards[10:20],
                player_list[2]: cards[20:30],
                player_list[3]: cards[30:40],
                player_list[4]: cards[40:50],
            }
        return card_distrib
