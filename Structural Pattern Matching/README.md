# Structural Pattern Matching

Structural Pattern Matching is a technique that allows complex data structures to be applied in a concise and readable way in comparisons. With structural pattern matching, a data structure is analyzed and searched for a specific pattern that has been defined. This can often be written in a concise and easy-to-understand way, which increases the readablility of the code. 

It can reduce error-proneness and increase development productivity by shortening syntax and improving readability. 
The match statement works by comparing an evaluated expression with one or more patterns. 
Let's take a look at the below example. We write a function that responds to a chosen language, so 'chosen_language' is the expression to check. 

```
def greeting(language):
    chosen_lang = language.capitalize()
    match chosen_lang:
        case 'English':
            print("hello")
        case 'French':
            print("Bonjour")
        
greeting('english')

```

The underscore character is used as a placeholder to match any value. For the following code, the case with '_' always applies if 'English' or 'French' is not entered:

```
def greeting(language):
    chosen_lang = language.capitalize()
    match chosen_lang:
        case 'English':
            print("hello")
        case 'French':
            print("Bonjour")
        case _:
            print(f"Hello! I don't know {chosen_lang}")
        
greeting('english')
greeting('german')

```

Without match condition, the code will consists of if, elif and else blocks. 

There is an interesting use case in the form of an imaginary adventure game. Gamers could write actions as strings in the various formats, like

* 'help'
* 'show inventory'
* 'go north'
* 'go south'
* 'drop shield'
* 'drop all weapons'

```
commands = ['go north','go west', 'drop potion', 'drop all weapons', 'drop shield']
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

```

Another example, where we can implement functionality of a factorial function using match

```
def factorial(n):
    match n:
        case 0 | 1:
            return 1
        case _:
            return n * factorial(n-1)

for i in range(6):
    print(i, factorial(n))

```
Alert:
'match' is only available from Python 3.10 onward, and hence it is important to check if your code is compatible with it. 