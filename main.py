#--------------------------------
# Developer: Ashley Schultz 2025
# -------------------------------
# modules
import os
import sys
import time
import random
# game_functions.py
from game_functions import clear_screen, program_intro, type_narration
from game_functions import press_enter, insert_line
from game_functions import narration_start_game, narration_change_name_no
# hero_class.py
from hero_class import Hero
# default hero settings
hero = Hero("You", 25, 5)
# ----------------------------------------------------
# progam start
# ----------------------------------------------------
press_enter()
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
            menuSelection = userInput.lower()
            match menuSelection:
                # progresses game - needs hella more code
                case "start":
                    clear_screen()
                    narration_start_game()
                    insert_line()
                    # gets name
                    hero.name = input(f"Please type your name: ")
                    insert_line()
                    narration = (f"Narrator: {hero.name}, hero of legend. Is that really the name you "
                                 f"want echoed through the ages?")
                    type_narration(narration)
                    insert_line()
                    # confirm name
                    userInput = input("Type: 'no' .....to give a new name\n"
                                      "Type: 'yes'.....to carry on\n"
                                      "Please make your selection: ")
                    insert_line()
                    # controls naming options
                    changeName = userInput.lower()
                    match changeName:
                        case 'no':
                            # player renames hero
                            clear_screen()
                            narration_change_name_no()
                            insert_line()
                            # prompt for name change
                            hero.name = input("This is it, state your name for the record: ")
                            insert_line()
                            # additional narrator sass
                            narration = (f"Narrator: When given the choice of any name, you choose {hero.name}? "
                                         f"Your choices seem questionable.")
                            type_narration(narration)
                            narration = f"Narrator: At least this will be entertaining...for me."
                            type_narration(narration)
                            narration = f"Narrator: Right, let's progress the story...{hero.name}."
                            type_narration(narration)
                            print("...Loading Next Chapter...")
                            time.sleep(2)
                        case 'yes':
                            # name confirmed - Narrator sass
                            clear_screen()
                            narration = f"Narrator: If you say so...{hero.name}."
                            type_narration(narration)
                            narration = f"Narrator: Right, let's progress the story."
                            type_narration(narration)
                            print("...Loading Next Chapter...")
                            time.sleep(2)
                        case _:
                            # invalid input = Narrator sass - moves along
                            clear_screen()
                            narration = (f"Narrator: When given two options, you decide to go rogue.")
                            type_narration(narration)
                            narration = f"Narrator: Learn, I will do the deciding for you in these instances."
                            type_narration(narration)
                            print("...Loading Next Chapter...")
                            time.sleep(2)
                    # Game continues after naming - needs coding
                    print("Code this outside case")
                    time.sleep(5)
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
            narration = f"Narrator: Our journey has come to an end. Goodbye friend!"
            type_narration(narration)
            print(f"...Closing the Book on Your Adventure...")
            time.sleep(2)
            break
        # if the user presses anything other than enter, we do that for them
        case _:
            clear_screen()
            narration = f"Narrator: Computers are really good at taking instructions. People, not so much."
            type_narration(narration)
            narration = f"Narrator: Here, let me help get you started."
            type_narration(narration)
            print(f"...Loading Main Menu...")
            time.sleep(2)
            clear_screen()
            startGame = ""