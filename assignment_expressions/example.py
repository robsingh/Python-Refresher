# without walrus operator
data = [1,2,3,4,5]
if len(data) > 3:
    print("List is too long")

# with walrus operator
data = [1,2,3,4,5]
if (n:= len(data) > 3):
    print("List is too long")

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
