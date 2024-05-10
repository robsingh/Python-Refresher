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
def dict_merge_sum(d1, d2):
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