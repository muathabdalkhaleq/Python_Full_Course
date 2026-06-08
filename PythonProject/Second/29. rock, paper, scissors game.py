import random

options = ("rock","paper","scissors")
is_playing = True

while is_playing:
    player=None
    computer = random.choice(options)
    player = input("Select one (Rock,Paper,Scissors)").lower()
    while player not in options:
        print("Not valid")
        player = input("please Select one (Rock,Paper,Scissors)").lower()
    if  player == computer :
        print(f"YOU: {player} COMPUTER:{computer}")
        print("Fair")

    elif player == "rock" and computer == "scissors":
        print(f"YOU: {player} COMPUTER:{computer}")
        print("You WIN")
        

    elif player == "paper" and computer == "rock":
        print(f"YOU: {player} COMPUTER:{computer}")
        print("You WIN")
        

    elif player == "scissors" and computer == "paper":
        print(f"YOU: {player} COMPUTER:{computer}")
        print("You WIN")
        

    else:
        print(f"YOU: {player} COMPUTER:{computer}")   
        print("YOU LOOSE")
    playing = input("PLAY AGAIN ??(Y , N)").lower()
    if not playing =="y":
        is_playing = False
 
print("Thanks for playing")

