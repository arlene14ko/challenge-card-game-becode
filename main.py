from utils.game import Board

#Start Game
print("=================================================================")
print("\nWelcome players! \nWe are going to play a card game. \nYou will be given same amount of cards and you need to draw the highest number each turn to have a point. \nThe player who has most points will be the winner!\n")

#asking input from players 
player_list = []
print("=================================================================")
print("This game requires number of players from 2 to 5 people.")
print("=================================================================")
num_of_players = int(input("Please enter number of players:  "))
print("_________________________________________________________________")
if num_of_players <= 1 or num_of_players > 5:
    print("Please enter number more than 1 or less than 6")
else:
    for i in range(num_of_players):
        name = input(f"Please enter name of Player {i+1}: ")
        player_name = f"Player {i+1}: {name}"
        player_list.append(player_name)
    print("_________________________________________________________________")
    print(f"Welcome {' , '.join(str(e) for e in player_list)}! \nWe will now start the game. \nGood luck! :D ")
    print("_________________________________________________________________")

#importing the Deck from card.py (class Deck )
#fill deck function to fill the deck of 52 cards

startgame = Board.start_game(num_of_players,player_list)




