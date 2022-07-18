items = ['Sword of Might', 'Shield of Magic', 'Armor Suit', 'Boots of Silence', 'Cloak of the Eagle',
             'Morph Device', 'Belt of Strength', 'Avocado Stone']
inventory = []
def get_items():
    print("You see the {}.".format(items[0]))
    rooms = True
    while rooms == True:
        action = input("What do you do?: ").lower().strip()
        if action == "get Item":
            print('You picked up the {}'.format(items[0]),
            inventory.append(items[1])
        elif action == "get Item" and items not in inventory:
            print("The door is locked")
        else:
            print("I do not understand")
    else:
        print("Congrats! Time to get the next one!")


get_items()