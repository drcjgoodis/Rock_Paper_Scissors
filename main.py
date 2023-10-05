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
    
    #print('You will be asked to chose 1 for Rock, 2 for Paper, and 3 for Scissors.\n')

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
    elif pick_user_int == SCISSORS:
        print('You picked: Scissors')       
    else:
        print('Uh-oh...You did not enter 1, 2, or 3...')

    # If the move is not 1, 2, or 3, exit the program
    if pick_user_int < 1 or pick_user_int > 3:
        print ("You need to enter 1, 2, 3.")
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
    #print(type(pick_user_int))
    #print(type(pick_CPU))
    
    
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
    if val == "win":
        return 1
    elif val == "lose":
        return -1
    else:
        return 0
    

    


#code which is not inside the function starts here
print("\n")
print('Welcome to your incredible Rock-Paper-Scissors Game!\n')
print("Let's play a round!\n")
rounds_str = input("How many win total would you like to play to? Maximum is 100 wins.\n")
while True:
    try:
        if rounds_str == "":
            print('You hit return. Please enter a valid number.\n')
            raise Exception("You entered a blank return.")
        rounds_int = int(rounds_str)
        if rounds_int <=0:
            print("You entered a number less than or equal to 0.\n")
            raise Exception("You entered a number less than or equal to 0.")
        if rounds_int > 100:
            print("You entered a number greater than 100.\n")
            raise Exception("You entered a number greater than 100.")
        break
    #except ValueError as e:
    #    print(e)
    #    print('While we love your enthusiasium, we will set you to 100 rounds. Have fun!')
    #    rounds_int = 100
    #    break
    except Exception as e:
        rounds_str = input("Please enter a numerical digit greater than 0, but less than 100 for the number of rounds.\n")
    

wins_int = 0
draws_int = 0
loses_int = 0
i = 0
while wins_int < rounds_int and loses_int < rounds_int:
    result = play_round()
    i_str = str(i + 1)
    print('For round: ' + i_str)
    if result == 1:
        print('Yea! You Won!\n')
        wins_int +=1
    elif result == 0:
        print('You had a draw...\n')
        draws_int +=1
    else:
        print('Awww... you lost. Better luck next time...\n')
        loses_int +=1
        
    print('Wins: ' + str(wins_int))
    print('Loses: ' + str(loses_int))
    print('Draws: ' + str(draws_int))
       
if wins_int > loses_int:
    print("Congradulations! You Won!\n")
if loses_int > wins_int:
    print("You did not win, but...Congradulations to the Computer!\n")
print('Your win total was: ' + str(wins_int))
print("The Computer's win total was:" + str(loses_int))
print('The margin of Victory was: ' + str(abs(wins_int - loses_int)))