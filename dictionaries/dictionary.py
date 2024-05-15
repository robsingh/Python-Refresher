# how to turn lists into dictionaries
'''cities = ['Boston', 'New Hampshire', 'Tampa', 'Hillsboro', 'Fremont']
areas = [891.68, 755.3, 310.7, 405.02, 248.31]

city_area_dict = dict(zip(cities, areas))

print(city_area_dict)'''

'''Example: 1
Write a function dict_merge_sum that takes two dictionaries d1 and d2 as parameters. 
The values of both dictionaries are numerical. 
The function should return the merged sum dictionary m of those dictionaries. 
If a key k is both in d1 and d2, the corresponding values will be added and included in the dictionary m,
If k is only contained in one of the dictionaries, the k and the corresponding value will be included in m
'''
'''def dict_merge_sum(d1, d2):
    merged_sum = d1.copy()
    for key,value in d2.items():
        if key in d1:
            d1[key] += value
        else:
            d1[key] = value

    return merged_sum


d1 = dict(a=10, b=5, c=4)
d2 = dict(a=2, b=4, c=6)
print(dict_merge_sum(d1, d2))
'''

'''
Example: 2
Given is the following simplified data of a supermarket:
To be ready for an imminent crisis you decide to buy everything. 
The question is how much will you have to pay?
'''

'''def supermarket_purchase(supermarket):
    total_cost = 0
    for value in supermarket.values():
        quantity = value['quantity']
        price = value['price']
        total_cost += quantity*price
    return total_cost

supermarket = { "milk": {"quantity": 20, "price": 1.19},
               "biscuits":  {"quantity": 32, "price": 1.45},
               "butter":  {"quantity": 20, "price": 2.29},
               "cheese":  {"quantity": 15, "price": 1.90},
               "bread":  {"quantity": 15, "price": 2.59},
               "cookies":  {"quantity": 20, "price": 4.99},
               "yogurt": {"quantity": 18, "price": 3.65},
               "apples":  {"quantity": 35, "price": 3.15},
               "oranges":  {"quantity": 40, "price": 0.99},
               "bananas": {"quantity": 23, "price": 1.29}}

print(supermarket_purchase(supermarket))'''

'''
Example: 3
Create a virtual supermarket. For every article there is a price per article and a quantity, i.e. the stock. 
Create shopping lists for customers. The shopping lists contain articles plus the quantity.
The customers fill their carts, one after the other. Check if enough goods are available! Create a receipt for each customer.
'''
'''supermarket = { "milk": {"quantity": 20, "price": 1.19},
               "biscuits":  {"quantity": 32, "price": 1.45},
               "butter":  {"quantity": 20, "price": 2.29},
               "cheese":  {"quantity": 15, "price": 1.90},
               "bread":  {"quantity": 15, "price": 2.59},
               "cookies":  {"quantity": 20, "price": 4.99},
               "yogurt": {"quantity": 18, "price": 3.65},
               "apples":  {"quantity": 35, "price": 3.15},
               "oranges":  {"quantity": 40, "price": 0.99},
               "bananas": {"quantity": 23, "price": 1.29}}

customers = ["Frank", "Mary", "Paul"]

shopping_lists = { 
   "Frank" : [('milk', 5), ('apples', 5), ('butter', 1), ('cookies', 1)],
   "Mary":  [('apples', 2), ('cheese', 4), ('bread', 2), ('pears', 3), 
             ('bananas', 4), ('oranges', 1), ('cherries', 4)],
   "Paul":  [('biscuits', 2), ('apples', 3), ('yogurt', 2), ('pears', 1), 
             ('butter', 3), ('cheese', 1), ('milk', 1), ('cookies', 4)]}

# filling the carts
carts = {}
for customer in customers:
    carts[customer] = []
    for article, quantity in shopping_lists[customer]:
        if article in supermarket:
            if supermarket[article]['quantity'] < quantity:
                quantity = supermarket[article]['quantity']
            if quantity:
                supermarket[article]['quantity'] -= quantity
                carts[customer].append((article, quantity))

for customer in customers:
    print(carts[customer])

print('checkout')

for customer in customers:
    print("\nCheckout for "+ customer + ":")
    total_sum = 0
    for name, quantity in carts[customer]:
        unit_price = supermarket[name]["price"]
        item_sum = quantity * unit_price
        print(f"{quantity:3d} {name:12s} {unit_price:8.2f} {item_sum:8.2f}")
        total_sum += item_sum
    print(f"\nTotal Sum: {total_sum:11.2f}")
'''

'''
Example: 4
A salesperson takes the following route: 
Port Carol to Rogerburgh to Smithstad to Scottshire to Clarkhaven to Dixonshire to Port Carol. 
How many kilometres did the salesperson drive?
'''
'''
t = "Port Carol to Rogerburgh to Smithstad to Scottshire to Clarkhaven to Dixonshire to Port Carol"
cities = t.split(" to ")
distance_matrix = {
         'Rogerburgh': {'Rogerburgh': 0, 'Smithstad': 5.2, 'Scottshire': 12.3,
                        'Clarkhaven': 14.9, 'Dixonshire': 12.7, 'Port Carol': 3.4},
         'Smithstad': {'Rogerburgh': 5.2, 'Smithstad': 0, 'Scottshire': 8.4, 
                       'Clarkhaven': 13.9, 'Dixonshire': 14.3, 'Port Carol': 8.6},
         'Scottshire': {'Rogerburgh': 12.3, 'Smithstad': 8.4,  'Scottshire': 0,
                        'Clarkhaven': 20.1, 'Dixonshire': 21.6, 'Port Carol': 6.5},
         'Clarkhaven': {'Rogerburgh': 14.9, 'Smithstad': 13.9, 'Scottshire': 20.1,
                        'Clarkhaven': 0, 'Dixonshire': 11.9, 'Port Carol': 18.7},
         'Dixonshire': {'Rogerburgh': 12.7, 'Smithstad': 14.3, 'Scottshire': 21.6,
                        'Clarkhaven': 11.9, 'Dixonshire': 0, 'Port Carol': 15.3},
         'Port Carol': {'Rogerburgh': 3.4, 'Smithstad': 8.6, 'Scottshire': 8.6,
                        'Clarkhaven': 18.7, 'Dixonshire': 15.3, 'Port Carol': 0}}

total_distance = 0
for i in range(len(cities)-1):
    distance = distance_matrix[cities[i]][cities[i+1]]
    txt = f"From {cities[i]} to {cities[i+1]}"
    print(f"{txt:30s}: {distance:5.1f}")
    total_distance += distance

print("="* 37)
print(f'{"The salesperson travelled":30s}: {total_distance:5.1f}')
'''

''''
Example: 5
cities = ['Stuttgart', 'Karlsruhe', 'Mannheim', 'Freiburg', 'Heidelberg', 'Heilbronn']
areas = [207.35, 173.46, 144.96, 153.07, 108.83, 99.88]  # Areas are in square kilometers
populations = [634830, 313092, 309370, 230241, 160355, 125960]
Create a dictionary with the city names as keys and the corresponding areas and population numbers as values.
'''
# def area(cities, areas, populations):
#    for city,area,population in zip(cities, areas, populations):
#       print(f'City: {city}, Area: {area}, Population: {population}')
'''cities = ['Stuttgart', 'Karlsruhe', 'Mannheim', 'Freiburg', 'Heidelberg', 'Heilbronn']
areas = [207.35, 173.46, 144.96, 153.07, 108.83, 99.88]
populations = [634830, 313092, 309370, 230241, 160355, 125960]

city_info_dict = {city:(area,population) for city, area, population in
                  zip(cities, areas, populations)}

print(city_info_dict)'''





