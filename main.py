from utils.game import Board

"""Python file where we start the program
    :attrib num_of_players number of players in the game
    :attrib player_list list of players in the game
"""
# initializing num_of_players
num_of_players = 2
line = Board.lines
line(1)
player_list = ["Player 1", "Player 2"]
print(f"Welcome {player_list}. We will now start!")
line(1)
# importing the class Board from utils/game.py
# function Board.start_game() will start running the game
startgame = Board.start_game(num_of_players, player_list)
