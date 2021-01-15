from utils.game import Board

"""Python file where we start the program
    :attrib num_of_players number of players in the game
    :attrib player_list list of player_name in the game
    :attrib player_name is the name of the player
"""
# initializing num_of_players
num_of_players = 2
player_list = ["Arl", "Lene"]
print(f"Welcome {player_list}")
# importing the class Board from utils/game.py
# function Board.start_game() to start running the game
startgame = Board.start_game(num_of_players, player_list)
