# Jacob Hardman
# Professor Marcus Longwell
# Intro to Programming
# 4/24/19
# Python Version 3.7.3

# *DESCRIPTION*
# This program prints a random full name from a nested list containing both first names and last names.
# This can be repeated until the user closes the program.

# Importing pkgs
import os
import random

# Clears the screen
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

########################################################## GLOBAL VARIABLES ##############################################################

# Main Boolean that keeps track of whether the user has closed the program
Is_Running = True

# Stores the list of names
NAMES = [["Luke", "Skywalker"], ["Han", "Solo"], ["Leia", "Organa"], ["Anakin", "Skywalker"], ["Obi-Wan", "Kenobi"], ["Padme", "Amidala"]]

########################################################### PROGRAM LOGIC ################################################################

def Program():

    # Clearing the screen for readability
    cls()

    Index = random.randint(0, len(NAMES) - 1)

    Full_Name = NAMES[Index][0] + " " + NAMES[Index][1]

    print(Full_Name)

    input("Press Enter to Continue")

########################################################### PROGRAM FLOW #################################################################

while Is_Running == True:
    Program()