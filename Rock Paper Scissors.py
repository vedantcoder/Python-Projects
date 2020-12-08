
# This is a basic Rock Paper Scissors game wherein you enter either Rock, Paper or Scissors and the #
# computer plays its move simultaneously and then you get the result where you win or lose #
# There are some prerequiseites to play this game #
# go to your command promt and type in- pip install random, if random isnt installed then it will be installed #
# if it is already installed then you will get a message saying- requirements already satisfied #
# Once you do this you will be able to play the game...
# ENJOY! #

from random import randint

#create a list of play options
t = ["Rock", "Paper", "Scissors"]

#assign a random play to the computer
computer = t[randint(0,2)]

#set player to False
player = False

while player == False:
#set player to True
    player = input("Rock, Paper, Scissors?")
    if player == computer:
        print("Tie!")
    elif player == "Rock":
        if computer == "Paper":
            print("You lose!", computer, "covers", player)
        else:
            print("You win!", player, "smashes", computer)
    elif player == "Paper":
        if computer == "Scissors":
            print("You lose!", computer, "cut", player)
        else:
            print("You win!", player, "covers", computer)
    elif player == "Scissors":
        if computer == "Rock":
            print("You lose...", computer, "smashes", player)
        else:
            print("You win!", player, "cut", computer)
    else:
        print("That's not a valid play. Check your spelling!")
    #player was set to True, but we want it to be False so the loop continues
    player = False
    computer = t[randint(0,2)]