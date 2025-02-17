#--------------------------------
# Developer: Ashley Schultz 2025
# -------------------------------
import os
import sys
import time

# List to hold melee Hero Stats
meleeHero = ["Name Me", 25, 5]

# Function to clear the screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Function to display melee Hero info
def info_melee_hero(meleeHero):
        print(f"Name: {meleeHero[0]}")
        print(f"HP: {meleeHero[1]}")
        print(f"AtK: {meleeHero[2]}")

# Function for Narrator text
def type_narration(text, delay=0.1):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

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
# controls the outter while loop beginning the program
startGame = userInput

while True:
    match startGame:
        # once enter is pressed, the game starts
        case "":
            clear_screen()
            program_intro()
            userInput = input("Please type your selection: ")
            # controls main menu selection
            menuSelection = userInput
            match menuSelection:
                # progresses game - needs hella more code
                case "start":
                    clear_screen()
                    print(f"Next Step needs coded")
                # opens lore menu - needs coded
                case "lore":
                    clear_screen()
                    print(f"Lore Menu here")
                # kicks out the loop to close the game
                case "quit":
                    startGame = "quit"
                # invalid selections pull back the intro
                case _:
                    clear_screen()
                    startGame = ""
        # ends the program
        case "quit":
            clear_screen()
            narration = "Narrator: Our journey has come to an end. Goodbye friend!"
            type_narration(narration)
            print("...Closing the Book on Your Adventure...")
            time.sleep(2)
            break
        # if the user presses anything other than enter, we do that for them
        case _:
            clear_screen()
            narration = "Narrator: Computers are really good at taking instructions. People, not so much."
            type_narration(narration)
            narration = "Narrator: Here, let me help get you started."
            type_narration(narration)
            print(f"...Loading Main Menu...")
            time.sleep(2)
            clear_screen()
            startGame = ""