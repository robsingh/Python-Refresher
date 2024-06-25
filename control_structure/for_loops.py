# Example - 1
# Generate and print the first n numbers in the Fibonacci sequence using a for loop.
n = int(input("Enter the number of Fibonacci numbers to generate: "))

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
    print()
