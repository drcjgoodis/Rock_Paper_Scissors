"""
A Rock-Paper-Scissors game that plays one round of human vs. computer

CMS 120
"""

# Imports
from random import randint
import sys

def play_round():


    # Declare constant variables representing the three moves
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


    # Print the welcome message and list the three moves
    print('Welcome to your incredible Rock-Paper-Scissors Game!\n')
    print("Let's play a round!\n")
    print('You will be asked to chose 1 for Rock, 2 for Paper, and 3 for Scissors.\n')

    # Read the user's move
    pick_user = input('Please enter your choice of 1 for Rock, 2 for Paper, and 3 for Scissors.\n')
    try:
        pick_user_int = int(pick_user)
    except:
        print('We are sorry! You did not enter 1, 2, 3. Please start the game again.')
        exit()
    if pick_user_int == ROCK:
        print('You picked: Rock')
    elif pick_user_int == PAPER:   
        print('You picked: Paper')
    else:
        print('You picked: Scissors')



    # If the move is not 1, 2, or 3, exit the program
    if pick_user_int < 1 or pick_user_int > 3:
        print ("You needed to enter 1, 2, 3.")
        return

    # Randomly generate the CPU's move using randint
    pick_CPU = randint(1,3)
    # Print a string representing the CPU's move
    if pick_CPU == ROCK:
        print('We picked: Rock')
    elif pick_CPU == PAPER:
        print('We picked: Paper')
    else:
        print('We picked: Scissors')    
    print(type(pick_user_int))
    print(type(pick_CPU))
    
    
    # Determine the outcome and print a message
    if pick_user_int == ROCK and pick_CPU == ROCK:
        val = "draw" 
    elif pick_user_int == ROCK and pick_CPU == PAPER:
        val = "lose"
    elif pick_user_int == ROCK and pick_CPU == SCISSORS:
        val = "win"
    elif pick_user_int == PAPER and pick_CPU == ROCK:
        val = "win"
    elif pick_user_int == PAPER and pick_CPU == PAPER:
        val = "draw"
    elif pick_user_int == PAPER and pick_CPU == SCISSORS:
        val = "lose"
    elif pick_user_int == SCISSORS and pick_CPU == ROCK:
        val = "lose"
    elif pick_user_int == SCISSORS and pick_CPU == PAPER:
        val = "win"
    else:
        val = "draw"


    # Return a value indicating win, lose or draw.
    return val

    #code which is not inside the function starts here

result = play_round()
print("You: " + result)
