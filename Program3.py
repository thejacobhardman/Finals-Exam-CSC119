# Jacob Hardman
# Professor Marcus Longwell
# Intro to Programming
# 4/24/19
# Python Version 3.7.3

# *DESCRIPTION*
# This program asks the user to name one of the most common letters user in Wheel of Fortune puzzles.
# The program is case-insensitive and will continue to prompt the user to guess until they guess correctly.
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

# Stores the correct values
Correct_Letters = ["R", "S", "T", "L", "N", "E"]

########################################################### PROGRAM LOGIC ################################################################

def Program():

    # Clearing the screen for readability
    cls()

    while User_Confirm == False:

        User_Input = input("Name one of the most common letters in wheel of fortune puzzles: ")

        if User_Input.upper() in Correct_Letters:
            print(User_Input.upper() + " is one of the most common letters!")
            break
        else:
            print("Incorrect!")

    input("Press Enter to Continue")

########################################################### PROGRAM FLOW #################################################################

while Is_Running == True:
    Program()