'''
The data type "set", which is a collection type, has been part of Python since version 2.4.
A set contains an unordered collection of unique and immutable objects.
The set data type is, as the name implies,
 a Python implementation of the sets as they are known from mathematics.
This explains, why sets unlike lists or tuples can't have multiple occurrences of the same element.
'''
#Basically, return a set of non repeted elements of some random list of data.
# is a built-in python function. 
# example
x = set("A python set turorial")
print(x) # return the list of elements not repeated, without order
 #you can pass lists to sets
y = set(['java','python','c++','java'])
print(y)

#Though sets can't contain mutable objects, sets are mutable:
cities = set(["Frankfurt", "Basel","Freiburg"])
cities.add("Strasbourg")
print(cities)

#Frozensets are like sets except that they cannot be changed, i.e. they are immutable:

cities = frozenset(["Frankfurt", "Basel","Freiburg"])
cities.add("Strasbourg")

