# Without running this code, what will it print? Why?

dict1 = {
    'a': [1, 2, 3],
    'b': (4, 5, 6),
}

dict2 = dict(dict1)
dict1['a'][1] = 42
print(dict2['a'])

# [1, 2, 3]
# WRONG: Nested collections. Shallow copy. 
# Inner lists reference same object.
# "different objects but share value components" 
print(dict2['a'][1] is dict1['a'][1])
