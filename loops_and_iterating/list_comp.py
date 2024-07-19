#transformation 
squares = [ number * number for number in range(5) ]
print(squares)

# as for loop
'''
squares = []
for number in range(5):
    square = number * number
    squares.append(square)

print(squares)
'''

# selection
multiples_of_6 = [ number for number in range(20) if number % 6 == 0 ]
print(multiples_of_6)

# as for loop
"""
multiples_of_6 = []
for number in range(20):
    if number % 6 == 0:
        multiples_of_6.append(number)

print(multiples_of_6)
"""

# selection and transformation
even_squares = [ number * number for number in range(10) if number % 2 == 0 ]
print(even_squares)

# over a dictionary
cats_colors = {
    'Tess':   'brown',
    'Leo':    'orange',
    'Fluffy': 'gray',
    'Ben':    'black',
    'Kat':    'orange',
}

names = [ name.upper() for name in cats_colors ]
print(names)

#selection in a dictionary
cats_colors = { 
    'Tess':     'brown',
    'Leo':      'orange',
    'Fluffy':   'gray',
    'Ben':      'black',
    'Kat':      'orange',
}

names = [ name.upper() 
         for name in cats_colors
         if cats_colors[name] == 'orange'
         if name[0] == 'L' ]
print(names)
