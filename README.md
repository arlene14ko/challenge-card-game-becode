# Challenge Card Game (Becode) 

- Developer Name : `Arlene Postrado`
- Level: `Junior Developer`
- Started: `13/01/2020 H:9h00`
- Duration: `2 days`
- Deadline: `15/01/2021 H:16h00`
- Team challenge : `Solo`
- Type of Challenge: `Consolidation`
- Promotion: `AI Theano 2`
- Coding Bootcamp: `Becode  Artificial Intelligence (AI) Bootcamp`

## Goal Objective

To create a card game in Python using Object Oriented Programming (OOP) 

## Learning Objectives
- To familiarize Object Oriented Programming (OOP)
- Learn to structure a project
- Proper importing of files
- Having a clean architecture
- Be able to go deeper in object inheritance
- Improve in using classes

## About the Repository

This is a pretty simple Card game and it has two branches `Main` branch and `Dev` branch.

### `Dev` Branch (Must-Have version)
- This is the base program for any card game. You can clone this repository and make your own card game according to the rules that you want.
- There is no actual game being played. There are no points being counted.
- The base program only has this:
    - deck of cards being created
    - distribute the card between different players
    - it is working until each player doesnt have any cards left

### `Main` Branch (Nice-to-Have version)
- The game is interactive, at first, you will be asked for the number of players and then the player names.
- You will be given the same amount of cards and you have to draw one at every turn.
- At each turn, the player is asked which card he/she wants to play.
- It also has an option if the player wants to end the game during his/her turn

### Code Style
 - Each **class** have a **`__str__()` method**
 - Each **function or class**  is  **typed**
 - Each **function or class** contains a **docstring** 
 - The code is **formatted** with **black**
 - The code has been **commented**.
 - The code is **cleaned of any commented unused code**.

### Repository

**README.md**
  - you are currently reading it right now

**main.py**
  - this is where you start the game
  - everything that you need to start the game is imported here 
  - if you choose the interactive version, you will also be asked here for the number of players and the player names

**utils folder**
  - this has 3 files namely:
      1. **card.py**
          - this is where the 52 Cards for the card game is being made, and created
          - this is also where the Deck of Cards is being filled, shuffled and distribute it among the players
      2. **player.py**
          - this is where the player will chose the card randomly during it's turn 
          - if you choose the interactive version, the player can choose which card to play
      3. **game.py**
          - this is where the actual game codes are
          - you can see a Board class here which indicates the mechanics of the game and how the game works
         
## Clone/Fork Repository
  - If you wish to clone/fork this repository, you can just click on the repository, then click the Clone/fork button and follow the instructions.

## Pending...
  - Still trying to figure out how to add the points system properly. 
  - Will update once that is done
  
### Thank you for reading, you may now proceed. 
