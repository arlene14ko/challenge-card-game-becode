from utils.game import Board    #importing the Board class from utils/game.py
from utils.player import Player #importing the Player class from utils/player.py

''' Start Game using the main.py file
    :attrib line - Calling method lines from class Board  for cleaner code
    :attrib message -  Calling method greetings from class Board for cleaner code 
        - It will print a welcome message for the players and a little message about the mechanics of the game
    :attrib num_of_players - asking input from the user
        - It will contain the number of player
    :attrib player_list will contain the list of players from the method Players in Player class
    Adding an if statement if the num_of_players is not 2, 3, 4 or 5
    :attrib startgame contains the start_game method from the Board class, it needs two parameters namely:
        i. num_of_players - and integer and ii. player_list - a list of players
''' 

line = Board.lines 
message = Board.greetings

line(1)
message(1)
line(2)
message(2)
line(1)

num_of_players = int(input("Please enter number of players:  "))
line(2)

if num_of_players <= 1 or num_of_players > 5:
    num_of_players = int(input("Please enter number more than 1 or less than 6:  "))
else:
    player_list = Player.players(num_of_players)

startgame = Board.start_game(num_of_players, player_list)
        

