from utils.game import Board #importing the Board class from the game.py

"""Python file where we start the program
    :attrib num_of_players number of players in the game
    :attrib player_list list of players in the game
    :Calling function line from class Board  for cleaner code
    :It will print a welcome message for the players
    :attrib startgame will be the name of the method start_game from Board class
    startgame will need two parameters, num_of_players(type int) and player_list(list)
"""
num_of_players = 2
line = Board.lines
line(1)
player_list = ["Player 1", "Player 2"]
print(f"Welcome {player_list}. We will now start!")
line(1)
startgame = Board.start_game(num_of_players, player_list)
