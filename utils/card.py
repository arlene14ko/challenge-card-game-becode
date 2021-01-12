class Symbol:
    """
    Class that shows the symbols of the cards.
    :attrib color is a string
    :attrib icon is a single character out of this list ['♥','♦','♣','♠']
    """
    def __init__(self, color, icon):
        self.color = color
        self.icon = icon 
    def symbol(color, icon):
        icon = ['♥','♦','♣','♠']
        for i in range(0, len(icon)):
            if

class Card(Symbol):
    """
    Class that inherits from the class Symbol and contains the color, icon and value of the cards
    :attrib value is a string one of this = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', ])
    """
    def __init__(self, color, icon, value):
        super().__init__(color, icon)
        self.value = value 


class Deck(Card):
    """
    Class that contains all the 52 cards (deck)
    """
    def __init__(self, cards = [color, icon, value]):
        super().__init__(color,icon,value)
        self.cards = cards
    
    def fill_deck():
        for i in icon:


