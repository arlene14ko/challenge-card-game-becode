from utils.card import Deck #importing the Deck class from card.py
from utils.player import Player #importing the Player class from player.py


class Board:
    """
    Class containing the gameboard
    :attrib turn_count an int
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
            :deck.fill_deck() - Filling the Deck with 52 cards
            :attrib cards - will be the filled deck with 52 cards
            :deck.shuffle(cards) - will randomly shuffle the cards
            :attrib distribute - will distribute the cards evenly to the players
                - this requires 3 parameters: num_of_players, player_list, and cards
        '''
        deck = Deck 
        deck.fill_deck()
        cards = deck.fill_deck()
        deck.shuffle(cards)
        distribute = deck.distribute(num_of_players, player_list, cards)  # working

        '''Creating a while loop where it will loop the number of times the game will play
            :attrib num_of_plays will contain the number of plays in the game - cards/num_of_players
            :turn_count will contain the number of turns in the game, starting at int 0
            :line - imported from the method lines, to make a cleaner GUI code
            :attrib history_cards - will contain the players history cards, starting at [] list
            :attrib active_cards - will contain the players current played cards
            :attrib endgame - a string containing 'end' which will allow the player to end the game during his/her turn
            :attrib active_card - the card that the player chose during the turn
            :attrib player_name - the name of the player from the player_list
            :attrib cards - containes all the cards the player have
            :attrib history - contains all the history_cards except the last element
            :attrib powerful - contains the most powerful card during the turn
           Adding an if statement where if the active_card contains 'end', it will break the loop and end the game. 
        '''
        num_of_plays = int(len(cards) / num_of_players)
        turn_count = 0
        print(f"\nNumber of plays: {num_of_plays}, Num of Players: {num_of_players} \n")
        line = Board.lines
        line(1)
        history_cards = []
        active_cards = []
        endgame = 'end'
        while turn_count < int(num_of_plays):
            for name, card in distribute.items():
                player_name = name
                cards = card
                line(3)
                active_card = Player.play(player_name, cards) 
                if active_card == endgame:
                    line(1)
                    print(f"\n{player_name} have decided to end the game. \n")
                    break
                else:
                    active_cards.append(active_card)
                    cards.remove(active_card)
                    
            if active_card == endgame:   
                break
            else:
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
        print("\nGame over! \nThank you for playing!\nHope you had fun! :) \n")
        line(1)

    def points():
        '''Still figuring out the points system. 
            Will pass this method as of this moment. 
        '''
        pass

    def lines(num):
        '''Created this method to have a cleaner code
        '''
        if num == 1:
            print("================================================================")
        elif num == 2:
            print("________________________________________________________________")
        elif num == 3:
            print("----------------------------------------------------------------")
