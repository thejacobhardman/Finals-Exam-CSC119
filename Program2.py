# Jacob Hardman
# Professor Marcus Longwell
# Intro to Programming
# 4/24/19
# Python Version 3.7.3

# *DESCRIPTION*
# This program counts backwards from 500 to 0.
# Each step of the count is displayed onto the screen.
# This can be repeated until the user closes the program.

# Importing pkgs
import os

# Clears the screen
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

########################################################## GLOBAL VARIABLES ##############################################################

# Main Boolean that keeps track of whether the user has closed the program
Is_Running = True

########################################################### PROGRAM LOGIC ################################################################

def Program():

    # Clearing the screen for readability
    cls()

    print("Counting backwards from 500 to 0 by 5s:\n", end="")

    for i in range(500, -5, -5):
        if i > 0:
            print(str(i) + ", ", end="")
        elif i == 0:
            print(i)
        
    input("Press Enter to Continue")

########################################################### PROGRAM FLOW #################################################################

while Is_Running == True:
    Program()