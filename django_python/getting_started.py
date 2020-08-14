print("Hello World")

# STRING and TUPLES  are immutable data types - mean we can not do item assignment
# whereas LISTS    are mutable datatypes.

#List Comprehesion
#
# matrix = [[1,2,3],[4,5,6],[7,8,9]]
#
# first_col = [row[0] for row in matrix]
#
# print(first_col)

# Dictionaries

my_stuff = {"k1":"v1", "k2":{"v2":[1, "grab Me", 2]}, "k3":"v3"}

print(my_stuff["k2"]["v2"][1])
# print(my_stuff["k2"]["v2"][1].upper())
# print(my_stuff["k2"]["v2"][1].split()) #dict in a dict inside it a list inside it a string ,make it a list :D

# SETS
    # sets are unordered elements and they are unique.

set_1 = set()
set_1.add(3)
set_1.add(2)
set_1.add(3)
set_1.add(9)
set_1.add(5)

print(set_1)

converted = set([1,1,1,3,1,2,2,5,3,5,2])
print(converted)
