'''
Text adventure games primarily relies on text-based descriptions and language commands for user input, rather than graphics and sound.
Below are the scenarios within a text adventure game, which includes features of structural pattern matching.
'''

command = input("What are you doing next?")
match command.split():
    case [action]:
        print(f"action without object: {action=}")
    case [action, obj]:
        print(f"{action=}, {obj=}")
'''
# Matching specific patterns

command = input("What are you doing next? ")
match command.split():
    case ["quit"]:
        print("Goodbye!")
        quit_game()
    case ["look"]:
        print("You are in cold and dark room ....")
    case ["get", obj]:
        print(f"You grab the {obj}")
    case ["go", direction]:
        print(f"You will go {direction} if possible")
    case _:
        print("Sorry, I do not understand!")
'''

# Matching multiple values

command = "drop apple armour shield"

match command.split():
    case ["drop", *objects]:
        for obj in objects:
            print(f"You drop a{'n' if obj[0] in 'aeiou' else ''} {obj}")

    
#adding a wild card

commands = ['go north','go west', 'drop potion', 'drop all weapons', 'drop shield', 'fight monster']
weapons = ['axe','sword','dagger']
shield = True
inventory = ['apple','wood','potion'] + weapons + ['shield']
for command in commands: 
    match command.split():
        case ["help"]:
            print("""You can use the following commands:
            """)
        case ["go", direction]: 
            print('going', direction)
        case ["drop", "all", "weapons"]: 
            for weapon in weapons:
                inventory.remove(weapon)
        case ["drop", item]:
            print('dropping', item)
            inventory.remove(item)
        case ["drop shield"]:
            shield = False 
        case _:
            print(f"Sorry, I couldn't understand {command!r}")





