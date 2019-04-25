# Jacob Hardman
# Professor Marcus Longwell
# Intro to Programming
# 4/24/19
# Python Version 3.7.3

# *DESCRIPTION*
# This program asks the user to input two numbers.
# These numbers are then added together and the result is printed to the screen.
# The computer then determines which number is larger and displays the inequality to the screen.
# If the two numbers are equal then this is displayed to the screen.
# This can be repeated until the user closes the program.

# Importing pkgs
import os

# Clears the screen
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

########################################################## GLOBAL VARIABLES ##############################################################

# Main Boolean that keeps track of whether the user has closed the program
Is_Running = True

# Stores the user's input
User_Input = ""

# Tracks whether the user has made a decision
User_Confirm = False

# Stores what numbers the user wants to add
Num_1 = 0
Num_2 = 0
Sum = 0

########################################################### PROGRAM LOGIC ################################################################

def Program():

    # Clearing the screen for readability
    cls()

    User_Input = input("Enter number 1: ")

    Num_1 = int(User_Input)

    User_Input = input("Enter number 2: ")

    Num_2 = int(User_Input)

    Sum = Num_1 + Num_2

    if Num_1 > Num_2:
        print("The sum of " + str(Num_1) + " and " + str(Num_2) + " is " + str(Sum) + " and " + str(Num_1) + " > " + str(Num_2) + ".")
    elif Num_1 < Num_2:
        print("The sum of " + str(Num_1) + " and " + str(Num_2) + " is " + str(Sum) + " and " + str(Num_2) + " > " + str(Num_1) + ".")
    else:
        print("The sum of " + str(Num_1) + " and " + str(Num_2) + " is " + str(Sum) + " and " + str(Num_1) + " == " + str(Num_2) + ".")

    input("Press Enter Key to Continue")

########################################################### PROGRAM FLOW #################################################################

while Is_Running == True:
    Program()