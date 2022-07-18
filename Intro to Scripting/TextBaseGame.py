# Intro to Scripting
# Jonathas Dias
# Project Two
# Super Dad and the Quest for the Avocado Stone

# section with the functions displaying the game of the goal and the commands

# Introduction to game
def show_instructions():
    print("Welcome to Toyland!")
# have user enter their name
    name = input("What is your name, adventurer?\n")
    print("Greetings, " + name + ". Let us go on a quest!")
# print a main menu and the commands
    print("This is text based adventure quest. The goal is to collect the 8 items spread throughout the farm,slay \n"
          "the evil Lord Allosaurus and save the children!")
    print("Move commands: south, north, east, west")
    print("Add to inventory: get 'item name'")


show_instructions()

# A dictionary linking a room to other rooms
# and linking one item for each room except the Start room (Farm Gate) and the room containing the villain

# movement section
# Setup
yes_no = ["yes", "no"]

print("It's time to get the gear and get the evil lord.")
print("Can you find your way through?\n")


rooms = {'Farm Gate': {'name': 'Farm Gate', 'east': 'Chicken Coop',
                       'text': 'You are at the Farm Gate.\n'},
         'Chicken Coop': {'name': 'Chicken Coop', 'east': 'Horse Barn', 'west': 'Farm Gate', 'south': 'Hay Barn',
                          'text': 'You are in the Chicken Coop.', 'inventory': 'Sword of Magic'},
         'Horse Barn': {'name': 'Horse Barn', 'west': ' Chicken Coop',
                        'text': 'You are in the Horse Barn.'},
         'Hay Barn': {'name': 'Hay Barn', 'east': 'Secret Room', 'west': 'Fish Pond', 'north': 'Great Hall',
                      'text': 'You are in the Hay Barn.'},
         'Fish Pond': {'name': 'Fish Pond', 'east': 'Cellar', 'north': 'Great Hall',
                       'text': 'You are at the Fish Pond.'},
         'Tractor Barn': {'name': 'Tractor Barn', 'east': 'Cellar', 'north': 'Great Hall',
                          'text': 'You are in the Bedroom.'},
         'Green Room': {'name': 'Green Room', 'east': 'Cellar', 'north': 'Great Hall',
                        'text': 'You are in the Green Room.'},
         'Solar Batteries Room': {'name': 'the bedroom', 'east': 'Cellar', 'north': 'Great Hall',
                                  'text': 'You are in the Solar Batteries room.'},
         'Secret Room': {'name': 'Secret Room', 'north': 'Farm House'},
         'Farm House': {'name': 'Farm House'}
         }
inventory = {'Sword of Might', 'Shield of Magic', 'Armor Suit', 'Boots of Silence', 'Cloak of the Eagle',
             'Morph Device', 'Belt of Strength', 'Avocado Stone'}
directions = ['north', 'south', 'east', 'west']
current_room = rooms['Farm Gate']

# game loop
command = ""
while True:
    if current_room['name'] == 'Farm House':
        print('Congratulations! You have reached the Farm House and defeated the Lord Allosaurus!')
        break
    # display current location
    print('You are in {}.'.format(current_room['name']))
    # get user input
    command = input('What do you do?\n')
    # movement
    if command in directions:
        if command in current_room:
            current_room = rooms[current_room[command]]

        else:
            # bad movement
            print('You cannot go that way.')
    # quit game
    elif command == 'quit':
        print('Thanks for playing!')
        break
    # bad command
    else:
        print('Invalid input')
