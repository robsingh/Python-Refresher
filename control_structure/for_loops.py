# Example - 1
# Generate and print the first n numbers in the Fibonacci sequence using a for loop.
'''n = int(input("Enter the number of Fibonacci numbers to generate: "))

if n <= 0:
    print("Please enter a positive integer.")
else:
    fibonacci_sequence = [0,1]
    
    for i in range(2,n):
        next_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_number)

    print("Fibonacci sequence:")
    for number in fibonacci_sequence[:n]:
        print(number, end=" ")
    print()'''

# Create a program that prints a diamond pattern using asterisks (*)
'''height = int(input("Enter height of the diamond: "))

height_is_even = height % 2 == 0
middle = height // 2 if height_is_even else height // 2 + 1

#upper half
spaces = "*"
for counter in range(0, middle):
    print(spaces.center(middle*2+1))
    spaces += "**"

spaces = spaces[:-2]
if height_is_even:
    print(spaces.center(middle*2+1))
while len(spaces) > 1:
    spaces = spaces[:-2]
    print(spaces.center(middle*2+1))'''

# Write a program to find and print all prime numbers between 1 and 50 using a for loop.
'''print("Printing all prime numbers between 1 and 50: ")
start = 1
stop = 51
for num in range(start, stop):
    if num <= 1:
        is_prime = False
    elif num <= 3:
        is_prime = True
    elif num % 2 == 0 or num % 3 == 0:
        is_prime = False
    else:
        is_prime = True
        i = 5
        while i * i <= num:
            if num % i == 0 or num % (i+2) == 0:
                is_prime = False
                break
            i += 6
    if is_prime:
        print(num, end=" ")
        print()'''

# Print numbers from 1 to 42, but for multiples of 3, print "Fizz," and for multiples of 5, print "Buzz." 
# For numbers that are multiples of both 3 and 5, print "FizzBuzz."
'''
start = 1
stop = 43

for num in range(start, stop):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)'''

