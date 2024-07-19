# Use the sqrt function from the math library to write some code that outputs the square root of 37. 
# Try to write the code in three different ways.

import math

sqrt37 = math.sqrt(37)
print(sqrt37)

def sqrt37_deux():
    return print(math.sqrt(37))

sqrt37_deux()

def sqrt37_trois():
    num = int(input('Enter the number 37: '))
    if num != 37:
        return print('Not 37.')
    return print (math.sqrt(37))

sqrt37_trois()


# LS solutions 

import math

print(math.sqrt(37))         # 6.082762530298219


import math as m

print(m.sqrt(37))            # 6.082762530298219


from math import sqrt

print(sqrt(37))              # 6.082762530298219
