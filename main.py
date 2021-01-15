from utils.game import Board #importing the Board class from game.py

''' Start Game
    :Calling function line from class Board  for cleaner code
    :It will print a welcome message for the players and a little message about the mechanics of the game
''' 
line = Board.lines 
line(1)
print("Welcome players! \nWe are going to play a card game. \nYou will be given same amount of cards and you need to draw the highest number each turn to have a point. \nThe player who has most points will be the winner!")
line(2)

''' Asking input from players
    :attrib player_list will contain the list of players, starting value is an empty list
    :attrib num_of_players will coint the number of players
    :attrib player_name will be the name of the player
'''
player_list = []
print("\nThis game requires number of players from 2 to 5 people.")
line(1)
num_of_players = int(input("Please enter number of players:  "))
line(2)

# An if statement if the num_of_players is not 2, 3, 4 or 5
if num_of_players <= 1 or num_of_players > 5:
    print("Please enter number more than 1 or less than 6")
else:
    # Initiating a for loop to get the players name depending on the number of players entered
    for i in range(num_of_players):
        name = input(f"Please enter name of Player {i+1}: ")
        player_name = f"Player {i+1}: {name}"
        player_list.append(player_name)
    line(1)
    print(
        f"\nWelcome {' , '.join(str(e) for e in player_list)}! \nWe will now start the game. \nGood luck! :D "
    )
    line(2)

''' After getting the num_of_players, player_list and player_name from the user,
    We will now import the Board class from game.py
    :attrib startgame will be the name of the function start_game from Board class
    startgame will need two parameters, num_of_players(type int) and player_list(list)
''' 
startgame = Board.start_game(num_of_players, player_list)
        

