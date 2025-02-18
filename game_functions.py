import os
import time

# Function to clear the screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Function for Narrator text
def type_narration(text, delay=0.05):
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

# Function to prompt for enter
def press_enter():
    print(f"========================================")
    print(f"    To begin, please press ENTER")
    print(f"========================================")

# Function for
def insert_line():
    print(f"-------------------------------------------------------------------------------------")

#-------------------------------------
# Function(s) for Narrator dialogue
#-------------------------------------
def narration_start_game():
    narration = f"Narrator: Every story, has a main character. In this story, it's you."
    type_narration(narration)
    narration = f"Narrator: Brave Adventurer, what is your name?"
    type_narration(narration)

def narration_change_name_no():
    narration = (f"Narrator: We've yet to begin and you're already making changes "
                 f"to the story.  Typical hero nonsense.")
    type_narration(narration)
    narration = (f"Narrator: Have it your way my insecure friend. What name do "
                 f"you wish to be remembered by?")
    type_narration(narration)