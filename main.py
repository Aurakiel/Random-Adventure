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
            program_intro()
            time.sleep(10)
        # if the user presses anything other than enter, we do that for them
        case _:
            narration = "Narrator: Computers are really good at taking instructions. People, not so much."
            type_narration(narration)
            narration = "Narrator: Here, let me help get you started."
            type_narration(narration)
            startGame = ""
            print(f"...Loading Main Menu...")
            time.sleep(2)
