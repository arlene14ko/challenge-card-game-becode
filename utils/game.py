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
        cards = deck.fill_deck()  # working

        # shuffle deck function to shuffle the deck
        deck.shuffle(cards)  # working

        # distribute the deck to the players
        distribute = deck.distribute(num_of_players, player_list, cards)  # working

        # looping the number of times the game will play
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
                active_card = Player.play(
                    player_name, cards
                )  # chosen_card should be returned player should only play 1 card per turn (loop)
                if active_card == endgame:
                    print("Game over!\nYou have decided to end the game. Thank you for playing!")
                    break
                else:
                    active_cards.append(active_card)
                    cards.remove(active_card)
                    
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
        print("Game over! Congratulations! Hope you had fun! :) ")
        line(1)

    def points():
        pass
    
    def lines(num):
        if num == 1:
            print("================================================================")
        elif num == 2:
            print("________________________________________________________________")
        elif num == 3:
            print("-----------------------------------------------------------------")
