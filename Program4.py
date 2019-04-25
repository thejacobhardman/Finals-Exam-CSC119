# Jacob Hardman
# Professor Marcus Longwell
# Intro to Programming
# 4/24/19
# Python Version 3.7.3

# *DESCRIPTION*
# This program replaces every consonant in the word 'supercalifragilisticexpialidocious' with a - character.
# Both the original word and the adjusted word are displayed on the screen.
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

String = "supercalifragilisticexpialidocious"

Vowels = ["A", "E", "I", "O", "U"]

########################################################### PROGRAM LOGIC ################################################################

def Program():

    # Clearing the screen for readability
    cls()

    result_str = ""

    print(String)

    for char in String:
        if char.upper() in Vowels:
            result_str = result_str + char
        else:
            result_str = result_str + "-"

    print(result_str)

    input("Press Enter to Continue")

########################################################### PROGRAM FLOW #################################################################

while Is_Running == True:
    Program()