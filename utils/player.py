class Player:
    """
    Class containing the Players
    :turn_count an int starting at 0
    :number_of_cards an int starting at 0
    :history is a list of (Card class) that will contain all the cards played by the player
    """

    def __init__(self, turn_count, history, active_card):
        self.turn_count = turn_count
        self.history = history
        self.active_card = active_card

    def play(player_name, cards):
        # function that will allow  make the player to make a turn
        history = []
        endgame = 'end'
        turn_count = 0
        active_card = input(
            f"Hello {player_name}!\nPlease choose the card you want to play from: \n {cards} \nIf you wish to end game, enter 'end'. \nYour choice here: "
        )
        if active_card not in cards and active_card not in endgame:
            print("\nYou choose something not on the list. Please try again! ")
            active_card = input(
                f"Here are the correct choices: \n {cards} \nYour choice here: "
            )
            if active_card not in cards and active_card == endgame:
                return active_card 
                
        elif active_card not in cards and active_card == endgame:
            return active_card
        turn_count += 1
        history.append(active_card)
        print(f"----------------\n{player_name} \nPlayed: {active_card} \nTurn Count: {turn_count} \nHistory: {history} \n")
        return active_card
