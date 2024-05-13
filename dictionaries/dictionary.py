# how to turn lists into dictionaries
'''cities = ['Boston', 'New Hampshire', 'Tampa', 'Hillsboro', 'Fremont']
areas = [891.68, 755.3, 310.7, 405.02, 248.31]

city_area_dict = dict(zip(cities, areas))

print(city_area_dict)'''

'''
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
Given is the following simplified data of a supermarket:

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

To be ready for an imminent crisis you decide to buy everything. 
The question is how much will you have to pay?
'''



