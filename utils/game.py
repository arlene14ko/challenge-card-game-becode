from utils.card import Deck #importing the Deck class from utils/card.py
from utils.player import Player #importing the Player class from utils/player.py


class Board:
    """
    Class containing the gameboard
    :attrib turn_count an int starting at 0
    :attrib active_cards will contain the last card played by each player
    :attrib history_cards contains all the cards except the 'active_cards'
    """

    def __init__(self, turn_count, active_cards, history_cards):
        self.turn_count = turn_count
        self.active_cards = active_cards
        self.history_cards = history_cards

    def start_game(num_of_players, player_list):
        ''' The method start_game will start the game. 
            It will have 2 parameters that it will get from main.py
                1. num_of_players - int - this has the total number of players
                2. player_list - list - this has the list of the player names
            Calling the Deck class from card.py
            :attrib deck will be the Deck class
            :deck.fill_deck() - calling the method fill_deck in Deck class Filling the Deck with 52 cards
            :attrib cards - will be the filled deck with 52 cards
            :deck.shuffle(cards) - calling the method shuffle that will randomly shuffle the cards
            :attrib distribute - calling the method distribute from Deck class that will distribute the cards evenly to the players
                - this requires 3 parameters: num_of_players, player_list, and cards
        '''
        deck = Deck  
        deck.fill_deck()
        cards = (deck.fill_deck())  
        deck.shuffle(cards)
        distribute = deck.distribute(num_of_players, player_list, cards)

        
        '''Creating a while loop where it will loop the number of times the game will play
            :attrib num_of_plays will contain the number of plays in the game - cards/num_of_players
            :line - imported from the function lines, to make a cleaner code
            :attrib active_card - the card that the player chose during the turn
            :attrib name - the name of the player from the player_list
            :attrib cards - containes all the cards the player have
            :attrib history - contains all the history_cards except the last element
            :attrib powerful - contains the most powerful card during the turn
        '''
        num_of_plays = int(len(cards) / num_of_players)
        
        line = Board.lines
        line(2)
        print(f"Number of Plays: {num_of_plays} == Number of Players: {num_of_players}")
        line(2)
        turn_count = 0
        
        active_cards = []
        history_cards = []
        history = []
        #while loop to loop the number of times the game will play, when the turn count is equal to the num of plays, the loop will stop
        while turn_count < int(num_of_plays):
            for name, card in distribute.items():
                name = name
                cards = card
                active_card = Player.play(
                    name, cards
                )  # chosen_card should be returned player should only play 1 card per turn (loop)
                cards.remove(active_card)
                active_cards.append(active_card)
            history_cards.append(active_cards)
            history = history_cards[:-1]
            turn_count += 1
            powerful = max(active_cards)
            line(2)
            print(
                f"Players Turn Count: {turn_count} \nList of Active Cards: {active_cards} \nWinning Card: {powerful} \nHistory: {history}."
            )
            line(2)
            active_cards = []
        line(1)
        print("Game over!")
        line(1)
        

    def lines(num):
        if num == 1:
            print("================================================================")
        elif num == 2:
            print("________________________________________________________________")
        elif num == 3:
            print("-----------------------------------------------------------------")
        elif num == 4:
            print("-----------------------------")

