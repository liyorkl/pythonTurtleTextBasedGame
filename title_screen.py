import cmd
import os
import random
import textwrap
import sys
import time

from main import start_game
from slowprint import *


def title_screen_selections():
    option = input(">  ")
    if option.lower() == ("start"):
        start_game()
    elif option.lower() == ("help"):
        help_menu()
    elif option.lower() == ("load"):
        sys.exit()
    while option.lower() not in ["start", "help", "load"]:
        print("Please enter a valid command.")
        option = input("> ")
        if option.lower() == ("start"):
            start_game()
        elif option.lower() == ("help"):
            help_menu()
        elif option.lower() == ("load"):
            sys.exit()


def how_to_play():
    print(" - This game is a text RPG -\n - It requires you to type in words(commands) into the console to make things happen. - \n - Commands such as 'help' and 'start' are ones that you could use. - \n - 'help' will open the help menu. - \n - 'start' will start the game - ")
    time.sleep(5)


def title_screen():
    os.system('clear')
    print("#############################")
    print("#  Welcome to the Text Rpg  #")
    print("#############################")
    print("        - S t a r t -        ")
    print("        -  L o a d  -        ")
    print("        -  H e l p  -        ")
    print("     - Copyright 2020 -      ")
    title_screen_selections()


def help_menu():
    os.system('clear')
    print("#############################################")
    print("#                   Help                    #")
    print("#############################################")
    print("")
    print("                 Commands for                ")
    print("        - What would you like to do?         ")
    print("  'move' 'inspect' 'look' 'use' 'inventory'  ")
    print("")
    print("     - Where would you like to move to?      ")
    print("  Use 'up', 'down', 'left', 'right' to move  ")
    print("")
    print('\n\n')
    time.sleep(5)
    title_screen()
    title_screen_selections()


how_to_play()
title_screen()
