from copy import deepcopy
#Difference between assigment, copy and deepcopy for objects
'''
In python, everything is a object, some objects are mutable, like lists (list object)
and other objects are immutable like numbers and strings. Every object has a id, that
identifies the object's address in the memory. When you declare a variable, the variable
are only pointing to the id address of object that contains that value.
Inside a list object, each "index" is pointing to another id that cointains a value too, just like
any other variable.
'''
### ASSIGNMENT
a = [1,2,3,4] # a list with immutable values.
# b = a, it means that b is pointing to the same list object that a is pointing to it
# any change in a or b, will affect the same list object.
b = a
b[0] = 'x'
# a = [x,2,3,4], b = [x,2,3,4]
print(a,b)

#COPY/SHALLOW COPU
b = a.copy()
#now, b have created a new list object wich only b is pointing to it
#but since is a "b" copy of "a", the indexes of "b" is pointing to the same id objects that "a" is pointing
b[0] = 'y'
print(a,b)
###DEEP COPY
''' 
deep copy is used when you need to copy is used when you need to copy mutable objects like lists, that contains
another list inside of them. Shallow copy only copy the "first level" list but if some index of the list is pointing
to another list object, both the copy and the original will be pointing again to the same list object, so a change in one
will affect the other. Example
'''
a = [1,2,3,["a","b","c"]]
b = a.copy()
b[3][0] = "x" # it will change this value on "a" too
print(a,b) #a= [1, 2, 3, ['x', 'b', 'c']]   b = [1, 2, 3, ['x', 'b', 'c']]
# now, using deep copy
b = deepcopy(a)
b[3][0] = 'y' #it will only affect "b" list and sublist
print(a,b) #[1, 2, 3, ['x', 'b', 'c']] [1, 2, 3, ['y', 'b', 'c']]
