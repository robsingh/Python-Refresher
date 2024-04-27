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