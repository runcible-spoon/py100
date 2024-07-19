# Write a find_integers function that returns a list of 
# all the integers from my_tuple:

my_tuple = (1, 'a', '1', 3, [7], 3.1415,
            -4, None, {1, 2, 3}, False)

def find_integers(tuple):
    results = []
    for element in tuple:
        if type(element) is int:
            results.append(element)
    return results


# ls solution

def find_integers(things):
    return [ element for element in things if type(element) is int ]


integers = find_integers(my_tuple)
print(integers)                    # [1, 3, -4]
