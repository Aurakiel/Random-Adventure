#--------------------------------
# Developer: Ashley Schultz 2025
# -------------------------------
import os
import sys
import time

# List to hold melee Hero Stats
meleeHero = ["Name Me", 25, 5]

# Function to display melee Hero info
# info_melee_hero(meleeHero) - call
def info_melee_hero(meleeHero):
        print(f"Name: {meleeHero[0]}")
        print(f"HP: {meleeHero[1]}")
        print(f"AtK: {meleeHero[2]}")

 # Function to display Main Menu
def program_intro():
    print(f"========================================")
    print(f"     Welcome to Random Adventure")
    print(f"========================================")
    print(f"           Menu Options")
    print(f"Type: start ......to begin your adventure")
    print(f"Type: quit  ......to end the game")
    print(f"Type: lore  ......for the backstory")
    print(f"========================================")
# ----------------------------------------------------
# progam start
# ----------------------------------------------------
print(f"========================================")
print(f"    To begin, please press ENTER")
print(f"========================================")
userInput = input("Press 'ENTER' to continue. ")

while True:
    if userInput == "":
        # displays main menu - gets user selection
        program_intro()
        userInput = input("Please type your selection: ")
        # closes the progam
        if userInput.lower() == 'quit':
            break
        # prompt for valid selection
        else:
            while userInput.lower() != 'start' and userInput.lower() != 'lore':
                print(f"Computers are good at following instructions but not at reading your mind.")
                userInput = input("Please type your selection: ")
        # lore menu
        if userInput.lower() == 'lore':
            # make this pretty - add lore
            print("Lore information to go here...")
            print(f"========================================")
            print(f"      Press 'ENTER' to return")
            print(f"========================================")
            userInput = input(f"'ENTER' will return you to the main menu: ")
            # loops back around to main menu after reading
            while userInput.lower() != '':
                print(f"Computers are good at following instructions but not at reading your mind.")
                userInput = input(f"Press 'ENTER' ")
            else:
                print("Returning to main menu...")
        # main process to drive the game
        elif userInput.lower() == 'start':
            print(f"============================================================")
            print(f"            Your Adventure Begins......")
            print(f"============================================================")
            print(f"Narrator: Every heroic tale, has a main character. In this\n"
                  f"          story, it's you!")
            meleeHero[0] = input("Please, state your name: ")
            print(f"Narrator: {meleeHero[0]}, that's good name. Is that the name\n"
                  f"          you wish the ages to remember you by?")
            print(f"Please type 'yes' to confirm or 'no' to give another name.")
            userInput = input(f"'yes' or 'no': ")
            print(f"Narrator: Let's begin!")
            time.sleep(2)
            while userInput.lower() != 'yes' and userInput.lower() != 'no':
                print(f"You'll need to confirm your name to begin.")
                print(f"Please type 'yes' to confirm or 'no' to give another.")
                userInput = input(f"'yes' or 'no'")
            if userInput.lower() == 'no':
                meleeHero[0] = input(f"What would you like to be called? ")
                print(f"Narrator: {meleeHero[0]}, does have an air of destiny")
                time.sleep(2)
            print("more game here")
    # prompts for enter if user input is invalid
    else:
        print(f"Computers are good at following instructions but not at reading your mind.")
        userInput = input("Please press 'ENTER' to begin. ")
