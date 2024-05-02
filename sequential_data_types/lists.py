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