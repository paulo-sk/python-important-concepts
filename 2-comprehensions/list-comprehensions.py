# list comprehension
# "list even is equal to x, for x in range (0~49) if x is even"
evens = [x for x in range (50) if x % 2 == 0 ]
print(evens)

# passing lists to dictionaries and using dictionarie comprehension
cities = ['Berlin', 'Hamburg', 'Munich', 'Cologne', 'Frankfurt']
areas = [891.68, 755.3, 310.7, 405.02, 248.31]  # Areas are in square kilometers
populations = [3769495, 1841179, 1471508, 1085664, 753056]
# 3 lists passed to a dic, the frist list is the keys, the other 2 are values passed as tuples.
city_info_dict = {city: (area, population) for city, area, population in zip(cities, areas, populations)}
print(city_info_dict)