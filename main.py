# Importing modules
from slowprint import slow_print  # so the printing is slow
from title_screen import *  # title screen
from drawings import *  # Turtle drawings
from grid import *  # grid
import cmd
import os
import random
import textwrap
import sys
import time
from math import *
from turtle import *

# importing the other modules
from mapdict import zonemap
print(zonemap)

t = Turtle()
t.hideturtle()
t.pu()
t.speed(0)
t.pensize(3)


def draw_tick(x, y):
    t.color("green")
    t.seth(315)
    t.setpos(x+65, y+140)
    t.pd()
    t.fd(8)
    t.seth(55)
    t.fd(16)
    t.pu()


def draw_cross(x, y):
    t.color("red")
    t.seth(315)
    t.setpos(x+75-(sqrt(225/2)/2), y+145)
    t.pd()
    t.fd(15)
    t.pu()
    t.seth(225)
    t.setpos(x+75+(sqrt(225/2)/2), y+145)
    t.pd()
    t.fd(15)
    t.pu()

# Shop function


class Shop():  # shop class
    def __init__(self, items=[], itemdesu=[]):
        self.items = items
        self.itemdesu = itemdesu
        self.prompt = "\n\nWelcome to the shop.\n\nWhat would you like to buy?\n(Corresponding number of the item only)"
        self.bprompt = "You have brought: "
        self.bitems = []
# to start the shop

    def start(self):
        if len(self.items) != 0:
            print(self.prompt)
            for x in range(len(self.items)):
                print(str(x + 1) + ". " + self.items[x])
            print("\n")

            if len(
                    self.bitems
            ) != 0:  # if items have been brought then it will print what items have been brought
                print(self.bprompt)
                for x in range(len(self.bitems)):
                    print(str(x + 1) + ". " + self.bitems[x])
                print('\n')

            if len(
                    self.items
            ) != 0:  # if there are still items left it will open the shop and allow for purchase. You can purchase by using the number given or by the item name
                num = []
                for x in range(len(self.items)):
                    num.append(str(x + 1))
                buy = input("> ")
                if buy.lower() in (num):
                    os.system('clear')
                    description = self.itemdesu[int(buy) - 1]
                    self.itemdesu.pop(int(buy) - 1)
                    buy = self.items[int(buy) - 1]
                    self.items.remove(buy)
                    self.bitems.append(buy)
                    myPlayer.inventory.append(buy)
                    print("You have successfully bought " + buy)
                    print(description)
                else:
                    while buy.lower() not in (num):
                        print(
                            "Please select a valid option.(Corresponding number of the item only)"
                        )
                        buy = input("> ")
                    os.system('clear')
                    description = self.itemdesu[int(buy) - 1]
                    self.itemdesu.pop(int(buy) - 1)
                    buy = self.items[int(buy) - 1]
                    self.items.remove(buy)
                    self.bitems.append(buy)
                    myPlayer.inventory.append(buy)
                    print("You have successfully bought " + buy)
                    print(description)

        else:
            print("\n\nYou have brought everything! :)")


# item list
item = [
    "ph scale", "tree seeds", "plant seeds", "rubbish bags", "algae remover",
    "acidic rock", "phone"
]
# item description list
itemdes = [
    "A ph scale is used to measure the ph level. If it is very acidic then it will be on the lower end of the scale (0) and if it is very basic then it will be on the upper end of the scale (14). You will have one.",
    "Tree seeds are used to plant trees around an area instantanously. The trees that will grow are Manuka and Kanuka trees that provide shelter to wildlife and keep the temperature down in the stream. You have an infinite supply of this.",
    "Plant seeds will be used to grow plants around the stream or bush area instantanously. These plants will help flatten down the area where floodplains occur and reduce the impact of floodplains during the winter season. You have an infinite supply of this.",
    "Rubbish bags will allow you to store the rubbish that you have picked up around the stream, city and bush area. It is made from one of the finest recyclable materials made to human existence, it will not break easily or stretch. You will have an infinite supply of this.",
    "Algae remover removes a large buildup of algae that can be seen on rocks and gravel in the stream. It is best to use this when the water is murky and the clarity is very low.",
    "Acidic rocks are used to decrease the pH level in the stream. Eels are more comfortable living in the acidic to netural waters which range around the 3 - 7 on the ph scale.",
    "A phone is used to contact the local automotive business to educate and prevent dumpage of pollutants into the stream."
]
# map This was somewhat taken from Bryan Tong
grid_list = [
    "a1", "a2", "a3", "a4",
    "b1", "b2", "b3", "b4",
    "c1", "c2", "c3", "c4",
    "d1", "d2", "d3"
]
gridx = {'1': -300, '2': -150, '3': 0, '4': 150}
gridy = {'a': 150, 'b': 0, 'c': -150, 'd': -300}


scenarios = {
    'stream': {

        # Flow
        'a3':
        "The stream seems to be flowing faster than usual, it doesn't seem safe for the wildlife in the stream, what should you do?\n(Plant some plants to slow the water down)",
        # Algae
        'b2':
        "The water here seems to be full of this green algae which is reducing the clarity of the water, what should you do?\n(Hmmm, that algae remover...)",
        # Acid rock
        'b3':
        "There doesn't seem to be much wildlife in the stream nowadays, how should you resolve this issue?\n(The pH level of the )",
        # pH
        'c1':
        "There are some eels in the stream although they seem to come up more often than usual, is there something wrong with the water?\n(Maybe try checking the pH level of the water)",
        # Wildlife
        'c2':
        "There seems to only be a few eels in the stream, you should bring more wildlife into the stream, how should you do this?\n(Maybe try to plant some trees as this may attract more wildlife(i.e. bugs))"
    },
    'city': {

        # Phone
        'a1':
        "A business seems to be dumping its oil and pollutants down the drain, how should you prevent this?\n(Maybe try calling the business)",
        # Drain
        'a4':
        "It's been raining quite heavily and the water seems to be flowing very slowly. What should you do?\n(The drain seems to be clogged)",
        # Bottle
        'b4':
        "Oh look, there's a plastic bottle, where should you put it?\n(Maybe that rubbish bag from the shop)",
        # Bottle
        'c4':
        "Oh look, there's a plastic bottle, where should you put it?\n(Hmmm, rubbish bag)",
        # Pollution
        'd1':
        "There seems to be a lot of rubbish and waste that is stuck around the drain area in the city. What should you do?\n(Hmmm, self explainatory)"
    },
    'bush': {

        # Trees
        'a2':
        "There doesn’t seem to be many trees around this area, what should you do?\n(Hmmm...)",
        # Plastic
        'b1':
        "There seems to be quite a lot of plastic here in the surrounding area which is quite bad because as it degrades it will release toxic chemicals into the soil and that will impact the plants that grow within that soil but also reduce the fertility of the soil meaning that it might be harder for plants to grow etc. What should you do about it?\n(Hmmm...)",
        # Floodplain
        'c3':
        "Oh no! There's been heavy rain, it seems like a floodplain will occur. How will you reduce the effect of the floodplain?\n(Maybe try some plants they seem to be able to absorb some of the water)",
        # Plastic
        'd2':
        "There seems to be quite a lot of plastic here in the surrounding area which is quite bad because as it degrades it will release toxic chemicals into the soil and that will impact the plants that grow within that soil but also reduce the fertility of the soil meaning that it might be harder for plants to grow etc. What should you do about it?\n(Hmmm...)",
        # Trees
        'd3':
        "There doesn’t seem to be many trees around this area, what should you do?\n(Hmmm...)",
    }
}

shop = Shop(item, itemdes)

# dictionary setup for scenarios and solutions


# player setup
class player:
    def __init__(self):
        self.name = ''
        self.inventory = []
        self.location = "d4"
        self.game_finished = False


myPlayer = player()

# turtle setup
screen = Screen()
grid(600)

gridposx = {'1': -300, '2': -150, '3': 0, '4': 150}
gridposy = {'a': 150, 'b': 0, 'c': -150, 'd': -300}

p = Turtle()  # make turtle for player position
p.hideturtle()
p.speed(0)


# Draw Player Location (dpl)
def dpl():
    screen.tracer(0)
    global starlocation
    p.clear()
    p.penup()
    p.setpos(gridposx[str(myPlayer.location[1])] + 75,
             (gridposy[str(myPlayer.location[0])] + 100))
    p.pd()
    p.seth(108)
    p.fillcolor("#FFFC35")
    p.begin_fill()
    for x in range(5):
        p.lt(144)
        p.fd(25)
        p.rt(72)
        p.fd(25)
    p.end_fill()
    p.pu()
    starlocation = myPlayer.location
    screen.tracer(1)


screen.setup(600, 600)
drawmap()

# call the draw player location function
dpl()


# game interactivity
def player_move(myAction):
    ask = "Where would you like to move to?\n> "
    dest = input(ask)
    while dest.lower() not in [
            "left", "west", 'right', 'east', 'up', 'north', 'down', 'south'
    ]:
        print("\nThat is not a valid direction.")
        dest = input("\nPlease select a new direction\n> ")

    if myPlayer.location in ["a1", "b1", "c1", "d1"
                             ] and dest.lower() in ["left", "west"]:
        while dest.lower() in ["left", "west"]:
            print("\nYou're on the edge of the board.")
            dest = input("\nPlease select a new direction\n> ")
            if dest.lower() in ['right', 'east']:
                destination = zonemap[myPlayer.location]['RIGHT']
                movement_handler(destination)
            elif dest.lower() in ['up', 'north']:
                destination = zonemap[myPlayer.location]['UP']
                movement_handler(destination)
            elif dest.lower() in ['down', 'south']:
                destination = zonemap[myPlayer.location]['DOWN']
                movement_handler(destination)
            while dest.lower() not in [
                    "left", "west", 'right', 'east', 'up', 'north', 'down',
                    'south'
            ]:
                print("\nThat is not a valid direction.")
                dest = input("\nPlease select a new direction\n> ")

    elif myPlayer.location in ["a4", "b4", "c4", "d4"
                               ] and dest.lower() in ["right", "east"]:
        while dest.lower() in ["right", "east"]:
            print("\nYou're on the edge of the board.")
            dest = input("\nPlease select a new direction\n> ")
            if dest.lower() in ['left', 'west']:
                destination = zonemap[myPlayer.location]['LEFT']
                movement_handler(destination)
            elif dest.lower() in ['up', 'north']:
                destination = zonemap[myPlayer.location]['UP']
                movement_handler(destination)
            elif dest.lower() in ['down', 'south']:
                destination = zonemap[myPlayer.location]['DOWN']
                movement_handler(destination)
            while dest.lower() not in [
                    "left", "west", 'right', 'east', 'up', 'north', 'down',
                    'south'
            ]:
                print("\nThat is not a valid direction.")
                dest = input("\nPlease select a new direction\n> ")

    elif myPlayer.location in ["a1", "a2", "a3", "a4"
                               ] and dest.lower() in ["up", "north"]:
        while dest.lower() in ["up", "north"]:
            print("\nYou're on the edge of the board.")
            dest = input("\nPlease select a new direction\n> ")
            if dest.lower() in ['right', 'east']:
                destination = zonemap[myPlayer.location]['RIGHT']
                movement_handler(destination)
            elif dest.lower() in ['left', 'west']:
                destination = zonemap[myPlayer.location]['LEFT']
                movement_handler(destination)
            elif dest.lower() in ['down', 'south']:
                destination = zonemap[myPlayer.location]['DOWN']
                movement_handler(destination)
            while dest.lower() not in [
                    "left", "west", 'right', 'east', 'up', 'north', 'down',
                    'south'
            ]:
                print("\nThat is not a valid direction.")
                dest = input("\nPlease select a new direction\n> ")

    elif myPlayer.location in ["d1", "d2", "d3", "d4"
                               ] and dest.lower() in ["down", "south"]:
        while dest.lower() in ["down", "south"]:
            print("\nYou're on the edge of the board.")
            dest = input("\nPlease select a new direction\n> ")
            if dest.lower() in ['right', 'east']:
                destination = zonemap[myPlayer.location]['RIGHT']
                movement_handler(destination)
            elif dest.lower() in ['up', 'north']:
                destination = zonemap[myPlayer.location]['UP']
                movement_handler(destination)
            elif dest.lower() in ['left', 'west']:
                destination = zonemap[myPlayer.location]['LEFT']
                movement_handler(destination)
            while dest.lower() not in [
                    "left", "west", 'right', 'east', 'up', 'north', 'down',
                    'south'
            ]:
                print("\nThat is not a valid direction.")
                dest = input("\nPlease select a new direction\n> ")

    else:
        if dest.lower() in ['left', 'west']:
            destination = zonemap[myPlayer.location]['LEFT']
            movement_handler(destination)
        elif dest.lower() in ['right', 'east']:
            destination = zonemap[myPlayer.location]['RIGHT']
            movement_handler(destination)
        elif dest.lower() in ['up', 'north']:
            destination = zonemap[myPlayer.location]['UP']
            movement_handler(destination)
        elif dest.lower() in ['down', 'south']:
            destination = zonemap[myPlayer.location]['DOWN']
            movement_handler(destination)


def movement_handler(destination):
    myPlayer.location = destination
    os.system("clear")
    print_location()


def print_location():

    print("\n" + (
        "################################################################################"
    ))
    if len(zonemap[myPlayer.location]['ZONENAME']) % 2 == 1:
        print("#" + (int((
            (77 - len(zonemap[myPlayer.location]['ZONENAME'])) / 2)) * (" ")) +
            str(zonemap[myPlayer.location]['ZONENAME']) + (int((
                (77 - len(zonemap[myPlayer.location]['ZONENAME'])) / 2)) *
            (" ")) + " #")
    else:
        print("#" + (int((
            (78 - len(zonemap[myPlayer.location]['ZONENAME'])) / 2)) * (" ")) +
            str(zonemap[myPlayer.location]['ZONENAME']) + (int((
                (78 - len(zonemap[myPlayer.location]['ZONENAME'])) / 2)) *
            (" ")) + "#")

    if len(zonemap[myPlayer.location]['DESCRIPTION']) % 2 == 1:
        print("#" + (int((
            (77 - len(zonemap[myPlayer.location]['DESCRIPTION'])) / 2)) *
            (" ")) + str(zonemap[myPlayer.location]['DESCRIPTION']) +
            (int(((77 - len(zonemap[myPlayer.location]['DESCRIPTION'])) / 2)) *
             (" ")) + " #")
    else:
        print("#" + (int((
            (78 - len(zonemap[myPlayer.location]['DESCRIPTION'])) / 2)) *
            (" ")) + str(zonemap[myPlayer.location]['DESCRIPTION']) +
            (int(((78 - len(zonemap[myPlayer.location]['DESCRIPTION'])) / 2)) *
             (" ")) + "#")
    print(
        "################################################################################\n"
    )
    dpl()


def prompt():
    t.clear()
    screen.tracer(0)
    for z in grid_list:
        if zonemap[str(z)]['SOLVED']:
            draw_tick(gridx[z[1]], gridy[z[0]])
        else:
            draw_cross(gridx[z[1]], gridy[z[0]])
    screen.tracer(1)
    print("\n" + "#########################")
    print("What would you like to do?")
    action = input("> ")
    acceptable_actions = [
        'move', 'go', 'travel', 'walk', 'quit', 'examine', 'inspect',
        'interact', 'look', 'help', 'shop', "inventory", "use", "tasks"
    ]
    while action.lower() not in acceptable_actions:
        print('Unknown action, try again.\n')
        action = input('> ')
    if action.lower() == 'quit':
        sys.exit()
    elif action.lower() in ['move', 'go', 'travel', 'walk']:
        player_move(action.lower())
    elif action.lower() in ['examine', 'inspect', 'interact', 'look']:
        player_examine(action.lower())
    elif action.lower() == 'help':
        print("\n\n")
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
    elif action.lower() == 'shop':
        if myPlayer.location == 'd4':
            shop.start()
        else:
            print("This is not the shop! Please go to d4")
    elif action.lower() == "inventory":
        for x in myPlayer.inventory:
            print(x, end=", ")
    elif action.lower() == 'tasks':
        t.clear()
        for z in grid_list:
            if zonemap[z]['SOLVED'] == True:
                print(z + ' solved')
                draw_tick(gridx[z[1]], gridy[z[0]])
            else:
                print(z + ' not solved')
                draw_cross(gridx[z[1]], gridy[z[0]])
        print('')
    elif action.lower() == "use":
        print(
            "What item would you like to use? (make sure you are on the right place and have the item)"
        )
        action = input("> ")
        if action.lower() not in myPlayer.inventory:
            print("You do not own this item or you spelt it wrong!")
        else:
            # stream
            if myPlayer.location == "a3":
                if action.lower() == "plant seeds":
                    print(
                        "You have planted seeds! The water's flowing seems to have slowed down."
                    )
                    zonemap[myPlayer.location]['SOLVED'] = True
                else:
                    print("That item can not be used here.")
            elif myPlayer.location == "b2":
                if action.lower() == "algae remover":
                    print(
                        "You have removed the algae! The water is now cleaner."
                    )
                    zonemap[myPlayer.location]['SOLVED'] = True
                else:
                    print("That item can not be used here.")
            elif myPlayer.location == "b3":

                if action.lower() == "acidic rock":
                    print(
                        "You have placed the acidic rocks! The water's pH level is now lower."
                    )
                    zonemap[myPlayer.location]['SOLVED'] = True
                else:
                    print("That item can not be used here.")
            elif myPlayer.location == "c1":
                if action.lower() == "ph scale":
                    if zonemap['b2']['SOLVED']:
                        print(
                            "You have placed the pH scale! The ph level is now 6."
                        )
                        zonemap[myPlayer.location]['SOLVED'] = True
                    else:
                        print(
                            "You have placed the pH scale! The ph level is 9.")
                else:
                    print("That item can not be used here.")
            elif myPlayer.location == "c2":
                if action.lower() == "tree seeds":
                    print(
                        "Tree appear in front of you! The wildlife has increased substantially!"
                    )
                    zonemap[myPlayer.location]['SOLVED'] = True
                else:
                    print("That item can not be used here.")
# city
            elif myPlayer.location == "a1":
                if action.lower() == "phone":  # phone
                    print(
                        "You have called the local automotive business and educate them about their irresponsible actions that have been killing eels in the stream."
                    )
                    zonemap[myPlayer.location]['SOLVED'] = True
                else:
                    print("That item can not be used here.")
            elif myPlayer.location == "a4":
                if action.lower() == "rubbish bags":  # drain
                    print(
                        "You have picked up the rubbish around the drain and unclogged it."
                    )
                    zonemap[myPlayer.location]['SOLVED'] = True
                else:
                    print("That item can not be used here.")
            elif myPlayer.location == "b4":
                if action.lower() == "rubbish bags":  # bottle
                    print(
                        "You have picked up all the plastic you see around you. Well done!"
                    )
                    zonemap[myPlayer.location]['SOLVED'] = True
                else:
                    print("That item can not be used here.")
            elif myPlayer.location == "c4":
                if action.lower() == "rubbish bags":  # bottle
                    print(
                        "You have picked up all the plastic you see around you. Well done!"
                    )
                    zonemap[myPlayer.location]['SOLVED'] = True
                else:
                    print("That item can not be used here.")
            elif myPlayer.location == "d1":
                if action.lower() == "rubbish bags":  # pollution
                    print(
                        "You have picked up the rubbish around the drain and unclogged it."
                    )
                    zonemap[myPlayer.location]['SOLVED'] = True
                else:
                    print("That item can not be used here.")


# bush
            elif myPlayer.location == "a2":
                if action.lower() == "tree seeds":  # trees
                    print(
                        "Trees appear in front of you! You have increased the oxygen levels in the stream area congratulations!"
                    )
                    zonemap[myPlayer.location]['SOLVED'] = True
                else:
                    print("That item can not be used here.")
            elif myPlayer.location == "b1":
                if action.lower() == "rubbish bags":  # plastic
                    print(
                        "You have increased the fertility of the soil by picking up plastic pollution around the area. Great work!"
                    )
                    zonemap[myPlayer.location]['SOLVED'] = True
                else:
                    print("That item can not be used here.")
            elif myPlayer.location == "c3":
                if action.lower() == "plant seeds":  # floodplain
                    print(
                        "Thanks for planting plants here! You have reduced the effect of floodplains when they occur. Hooray!!"
                    )
                    zonemap[myPlayer.location]['SOLVED'] = True
                else:
                    print("That item can not be used here.")
            elif myPlayer.location == "d2":
                if action.lower() == "rubbish bags":  # plastic
                    print(
                        "You have increased the fertility of the soil by picking up plastic pollution around the area. Great work!"
                    )
                    zonemap[myPlayer.location]['SOLVED'] = True
                else:
                    print("That item can not be used here.")
            elif myPlayer.location == "d3":
                if action.lower() == "tree seeds":  # trees
                    print(
                        "Trees appear in front of you! You have increased the oxygen levels in the stream area congratulations!"
                    )
                    zonemap[myPlayer.location]['SOLVED'] = True
                else:
                    print("That item can not be used here.")


def player_examine(action):
    if zonemap[myPlayer.location]['SOLVED']:
        print("You have already completed this area.")
    else:
        examine_handler()


def examine_handler():
    if zonemap[myPlayer.location]['EXAMINATION'] == "streama3":
        slow_print(scenarios['stream']['a3'], 0.05)
    elif zonemap[myPlayer.location]['EXAMINATION'] == "streamb2":
        slow_print(scenarios['stream']['b2'], 0.05)
    elif zonemap[myPlayer.location]['EXAMINATION'] == "streamb3":
        slow_print(scenarios['stream']['b3'], 0.05)
    elif zonemap[myPlayer.location]['EXAMINATION'] == "streamc1":
        slow_print(scenarios['stream']['c1'], 0.05)
    elif zonemap[myPlayer.location]['EXAMINATION'] == "streamc2":
        slow_print(scenarios['stream']['c2'], 0.05)

    elif zonemap[myPlayer.location]['EXAMINATION'] == "busha2":
        slow_print(scenarios['bush']['a2'], 0.05)
    elif zonemap[myPlayer.location]['EXAMINATION'] == "bushb1":
        slow_print(scenarios['bush']['b1'], 0.05)
    elif zonemap[myPlayer.location]['EXAMINATION'] == "bushc3":
        slow_print(scenarios['bush']['c3'], 0.05)
    elif zonemap[myPlayer.location]['EXAMINATION'] == "bushd2":
        slow_print(scenarios['bush']['d2'], 0.05)
    elif zonemap[myPlayer.location]['EXAMINATION'] == "bushd3":
        slow_print(scenarios['bush']['d3'], 0.05)

    elif zonemap[myPlayer.location]['EXAMINATION'] == "citya1":
        slow_print(scenarios['city']["a1"], 0.05)
    elif zonemap[myPlayer.location]['EXAMINATION'] == "citya4":
        slow_print(scenarios['city']["a4"], 0.05)
    elif zonemap[myPlayer.location]['EXAMINATION'] == "cityb4":
        slow_print(scenarios['city']["b4"], 0.05)
    elif zonemap[myPlayer.location]['EXAMINATION'] == "cityc4":
        slow_print(scenarios['city']["c4"], 0.05)
    elif zonemap[myPlayer.location]['EXAMINATION'] == "cityd1":
        slow_print(scenarios['city']["d1"], 0.05)

    elif zonemap[myPlayer.location]['EXAMINATION'] == "shop":
        print(
            "There seems to be a shop in front of you. Maybe you could try shopping. (Use command 'shop')"
        )


def start_game():
    setup_game()


def main_game_loop():
    while myPlayer.game_finished is False:
        prompt()
        y = 0
        for x in grid_list:
            if zonemap[x]['SOLVED'] == True:
                y = y + 1
            else:
                continue
        if y == 15:
            myPlayer.game_finished = True
    os.system("clear")
    print("Congrats you beat the game!")


def setup_game():
    os.system("clear")

    slow_print("Hello, what's your name?\n")
    player_name = input(">  ")
    myPlayer.name = player_name

    # INTRO
    slow_print("Welcome. " + player_name + "\n")

    slow_print(
        "Welcome to a very educational and informative game about the stream.\n"
    )
    slow_print("The stream as in the Puhinui Stream.\n")
    slow_print(
        "Yeah we have a stream next to our school if you didn't know.\n")
    slow_print("Anyways... lets just begin.\n")
    time.sleep(2)
    os.system("clear")
    main_game_loop()
