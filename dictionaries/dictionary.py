# how to turn lists into dictionaries
cities = ['Boston', 'New Hampshire', 'Tampa', 'Hillsboro', 'Fremont']
areas = [891.68, 755.3, 310.7, 405.02, 248.31]

city_area_dict = dict(zip(cities, areas))

print(city_area_dict)