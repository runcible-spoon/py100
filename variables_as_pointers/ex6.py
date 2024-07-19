''' 
The following program is nearly identical to that of the previous exercise. 
However, this time, it should create a shallow copy of dict1. 
Be careful: 
you're not allowed to use the copy module in this exercise.`

In addition, before you run this code, can you predict the output values?
'''

dict1 = {
    'a': [{7, 1}, ['aa', 'aaa']],
    'b': ({3, 2}, ['bb', 'bbb']),
}

dict2 = dict(dict1)

print(dict1         is dict2)
# False
print(dict1['a']    is dict2['a'])
# False #WRONG True. 'a' is not 'a' but the value of 'a', 
# which is a nested list.
print(dict1['a'][0] is dict2['a'][0])
# True 
print(dict1['a'][1] is dict2['a'][1])
# True
print(dict1['b']    is dict2['b'])
# False #WRONG True. 'b' is not 'b' but the value of 'b', 
# which is a nested list.
print(dict1['b'][0] is dict2['b'][0])
# True
print(dict1['b'][1] is dict2['b'][1])
# True
