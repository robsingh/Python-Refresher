'''
Lists are related to arrays of C, C++ or Java but in a more powerful and flexible way. 
For example, not all items in a list need to have the same type. Lists can grow in a program run,
while in C the size of an array has to be fixed at the compile time. 

List is a collection of objects, an ordered group of elements to be more precise. These elements do not
have to be the same type. 

Main Properties:
* Ordered.
* Mutable, i.e. the elements of the list can be changed. 
* Elements of the list can be accessed by an index.
* Variable size. 

'''
shopping_list = ['milk', 'yoghurt', 'egg', 'butter', 'bread', 'bananas']
cart = []
while shopping_list != []:
    article = shopping_list.pop()  
    cart.append(article)
    print(article, shopping_list, cart)

print("shopping_list: ", shopping_list)
print("cart: ", cart)

'''
A list can be seen as a Stack. Stack is a data structure which has atleast two operations: 
one which can be used to put or push data on the stack, and another one to take away the 
most upper element of the stack. 

List contains other methods such as append (which appends an element to the end of the list), 
pop (which removes the mentioned element from the list, if it is called with no argument then it removes the last element from the list),
extend (which extends a list by appending all the elements of an iterable).

'''