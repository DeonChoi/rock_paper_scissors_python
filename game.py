import random
import sys

name = input("Enter your name: ")
instructions = f"{name}, the rules are simple. Enter the move you wish to play: Rock, Paper, or Scissors."
print(instructions)
print('Type "Quit" to quit game.')
    
opponent_moves = ["Rock", "Paper", "Scissors"]
while True:
    opponent_move = opponent_moves[random.randint(0,2)]
    #print(f"Your opponent has chosen: {opponent_move}")
    move = input("Enter your move: ")
    move = move.title()

    if move == "Quit":
        sys.exit()

    if move not in ["Rock", "Paper", "Scissors", "Bomb"]:
        print("Please enter a valid move: Rock, Paper, or Scissors.")
    
    if move == opponent_move:
        print(f"Tie Game! You both chose {move}")
    
    if move == "Bomb":
        print("You win automatically! Bomb destroys everything!")

    if move == "Rock":
        if opponent_move == "Paper":
            print("You lose! Paper beats Rock!")
        if opponent_move == "Scissors":
            print("You win! Rock beats Scissors!")

    if move == "Paper":
        if opponent_move == "Scissors":
            print("You lose! Scissors beats Paper!")
        if opponent_move == "Rock":
            print("You win! Paper beats Rock!")

    if move == "Scissors":
        if opponent_move == "Rock":
            print("You lose! Rock beats Scissors!")
        if opponent_move == "Paper":
            print("You win! Scissors beats Paper!")