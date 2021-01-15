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
        ''' This method play will allow the player to make a turn
            :parameter player_name contains the name of the player
            :parameter cards contains the list of cards the player currently have
            :attrib history will contain the history of cards the player played, starting at empty []
            :attrib endgame is a string containing the word 'end', it will allow the player to choose to end the game
            :attrib active_card will the card the player chose during the turn
        '''
        
        turn_count = 0
        history = []
        endgame = 'end'
        active_card = input(
            f"Hello {player_name}!\nPlease choose the card you want to play from: \n {cards} \nIf you wish to end game, enter 'end'. \nYour choice here: "
        )
        if active_card not in cards and active_card not in endgame:
            print("\nYou choose something not on the list. Please try again! ")
            active_card = input(
                f"Here are the correct choices: \n {cards} \nIf you wish to end game, enter 'end'. \nYour choice here: "
            )
            if active_card not in cards and active_card == endgame:
                return active_card 
                
        elif active_card not in cards and active_card == endgame:
            return active_card
        
        turn_count += 1
        history.append(active_card)
        print(f"----------------\n{player_name} \nPlayed: {active_card} \nTurn Count: {turn_count} \nHistory: {history} \n")
        return active_card
    
    def players(num_of_players):
        ''' Method that will ask the users to input the players name.
            It needs a parameter: num_of_players - this is also from the user from main.py
            :attrib player_list will contain all the player name in a list, starting at [] empty list
            :name contains the name of the player
            :player name contains the name of the player plus their player number
            This method will return the player_list
        '''
        player_list = []
        for i in range(num_of_players):
            name = input(f"Please enter name of Player {i+1}: ")
            player_name = f"Player {i+1}: {name}"
            player_list.append(player_name)
        print(
        f"\nWelcome {' , '.join(str(e) for e in player_list)}! \nWe will now start the game. \nGood luck! :D "
        )
        return player_list
