#number guessing game
'''
A human player has to guess a number between a range of 1 to n. The player inputs his guess. 
The program informs the player, if this number is larger, smaller or equal to the secret number, 
i.e. the number which the program has randomly created. 
If the player wants to gives up, he or she can input a 0 or a negative number.
'''
import random
upper_bound = 20
lower_bound = 1
to_be_guessed = random.randint(lower_bound, upper_bound)
guess = 0
while guess != to_be_guessed:
    guess = int(input("New number: "))
    if guess == 0:
        print("Sorry that you are giving up!")
        break
    if guess < lower_bound or guess > to_be_guessed:
            print("Guess not within the boundaries!")
    elif guess > to_be_guessed:
        upper_bound = guess - 1
        print("Number too large!")
    elif guess < to_be_guessed:
         lower_bound = guess + 1
         print("Number too small!")
else:
    print("Congratulations! You did it.")