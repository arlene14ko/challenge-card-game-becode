from random import shuffle


class Symbol:
    """
    Class that shows the symbols of the cards.
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
    """
    Class that inherits from the class Symbol and contains the color, icon and value of the cards
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
    """
    Class that contains all the 52 cards (deck)
    """

    def __init__(self, color, icon, value, card):
        super().__init__(color, icon, value)

    def fill_deck():
        # function that will compile the deck of 52 cards
        cards = []
        cards = Card.cards()
        return cards

    def shuffle(cards):
        # function that will shuffle the list of cards
        shuffle(cards)

    def distribute(num_of_players, player_list, cards):  # number of players
        # function that will distribute cards evenly b/w players
        card_distrib = {}
        card_distrib = {player_list[0]: cards[0:26], player_list[1]: cards[26:52]}
        return card_distrib
