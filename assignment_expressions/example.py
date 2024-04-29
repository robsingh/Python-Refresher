# without walrus operator
data = [1,2,3,4,5]
squared = [x ** 2 for x in data if x > 2]

# with walrus operator
data = [1,2,3,4,5]
squared = [y ** 2 for x in data if (y := x) > 2]

# Without walrus operator
value = 10
if value > 5 and value % 2 == 0:
    print("Value is greater than 5 and even")

# With walrus operator
value = 10
if (value := 10) > 5 and value % 2 == 0:
    print("Value is greater than 5 and even")

# without walrus operator
n = int(input("Please give a number: "))
square = int ** 2
if square > 3:
    print("The number is greater than 3.")

# with walrus operator
n = int(input("Enter a number: "))
if (square := n**2) > 3:
    print("the number is greater than 3.")

# using readline
"""
Most people use a for loop to iterate over a text file line by line. With the walrus operator,
we can also elegantly go through a text using the method readline.
Example:
"""
word_to_find = 'Python'
with open('filename.txt') as file:
    while (line := file.readline()):
        if word_to_find in line:
            print(line)