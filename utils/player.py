class Player:
    """
    Class containing the Players
    :turn_count an int starting at 0
    :number_of_cards an int starting at 0
    :history is a list of (Card class) that will contain all the cards played by the player
    """

    def __init__(self, turn_count, number_of_cards, history, active_card):
        self.turn_count = turn_count
        self.number_of_cards = number_of_cards
        self.history = history
        self.active_card = active_card

    def play(player_name, current_cards):
        history = []
        # function that will allow  make the player to make a turn
        print("------------------------------------------------------------")
        active_card = input(
            f"Hello {player_name}!\nPlease choose the card you want to play from: \n {current_cards} \nYour choice here: "
        )
        if active_card not in current_cards:
            print("You choose something not on the list. Please try again! ")
            active_card = input(
                f"Hello {player_name}!\nPlease choose the card you want to play from: \n {current_cards} \nYour choice here: "
            )
        history.append(active_card)
        print(
            f"----------------\n{player_name} \nPlayed: {active_card} \nHistory: {history} "
        )
        return active_card
