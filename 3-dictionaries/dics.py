'''
We can use arbitrary types as values in a dictionary, 
but there is a restriction for the keys. 
Only immutable data types can be used as keys, 
i.e. no lists or dictionaries can be used: 
If you use a mutable data type as a key, you get an error message.

we can use tuples as keys in dictinaries
'''
#invalid_dic = {[1,2,3]: "abc"}
valid_dic = {(1, 2, 3): "abc", 3.1415: "abc"} #valid

'''
If you want to loope over a dic, you can use the methods:
 dic.items() - > loop through key-value par of the dic
 dic.values() - > loop through values() of the dic
 dic.keys() - > loop through keys of the dic, but is not necessary.
 if you jus try to loop through a dic without one of these methos, it will be implied that
 you want to loop through the keys
'''
champions_class = {'vayne': 'adcarry', 'leblanc': 'apcarry', 'Amumu': 'jungler', 'Blitz': 'support'}
for champions in champions_class:
    print(champions) #looping through the dictionarie without .keys() method

for champions_pair_values in champions_class.items():
    print(champions_pair_values) #looping through both key and value

for champions_values in champions_class.values():
    print(champions_values) #looping through value

'''
dic.pop() in dictinaries:
 1) You specify the key of the item you want to remove as an argument to the pop() method.
 2) The pop() method then searches for this key in the dictionary.
 3) If the key is found, the corresponding key-value pair is removed from the dictionary,
 and the value associated with the key is returned.
 4) If the key is not found, a KeyError is raised.
'''
capitals = {"Austria":"Vienna", "Germany":"Berlin", "Netherlands":"Amsterdam", "Switzerland":"Bern"}
print(capitals)
capital = capitals.pop("Austria")
print(capital)
print(capitals)