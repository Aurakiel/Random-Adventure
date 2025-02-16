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

