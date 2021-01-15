from utils.card import Deck
from utils.player import Player


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
        # calling class Deck from card.py
        deck = Deck  # adding a variable deck to call the Deck class

        # filling deck with 52 cards
        deck.fill_deck()
        cards = (
            deck.fill_deck()
        )  # calling the fill_deck function and naming it as cards

        # shuffle deck function to shuffle the deck
        deck.shuffle(cards)

        # distribute the deck to the players
        distribute = deck.distribute(num_of_players, player_list, cards)

        # looping the number of times the game will play
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

