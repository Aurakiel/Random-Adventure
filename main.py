#--------------------------------
# Developer: Ashley Schultz 2025
# -------------------------------
import os
import sys

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
            print(f"========================================")
            print(f"      Your Adventure Begins......")
            print(f"========================================")
            print(f"Story: Today is the day you've been waiting for. It's"
                  f"your 18th birthday and that means you're finally old"
                  f"enough to begin your adventure.")
                  #pick up here
            userInput = input("Press Enter: ")
    # prompts for enter if user input is invalid
    else:
        print(f"Computers are good at following instructions but not at reading your mind.")
        userInput = input("Please press 'ENTER' to begin. ")
