# 1. Identify the data type or class for each of the following values:

# 'True' = bool WRONG str
# False = bool
# (1, 2, 3) = tuple
# 1.5 = float
# [1, 2, 3] = list
# 2 = int
# range(5) = tuple WRONG range
# {1, 2, 3} = set 
# None = None ISH NoneType
# {'foo': 'bar'} = dict

# 2. Create a tuple called names that contains several pet names. 

names = ('Asta', 'Butterscotch', 'Pudding', 'Neptune', 'Darwin')

# 3. Create a dictionary named pets that contains a list of pet names and the type of animal. 

pets = {
    'Asta':             'dog',
    'Butterscotch':     'cat',
    'Pudding':          'cat',
    'Neptune':          'fish',
    'Darwin':           'lizard',
}

# Concatenate two strings, one with your first name and one with 
# your last, to create a new string with your full name as its 
# value. 

# For example, if your name is John Doe, you should 
# combine 'John' and 'Doe' to get 'John Doe'.

first = 'John'
last = 'Doe'

name = first + ' ' + last

print(name)

# Use the REPL and the arithmetic operators to extract the 
# individual digits of 4936:

# As string

x = '4936'

ones_place = x[3]

print(ones_place)

tens_place = x[2]

print(tens_place)

hundreds_place = x[1]

print(hundreds_place)

thousands_place = x[0]

print(thousands_place)

# As int

x = 4936

ones = x % 10

print(ones)

tens = (x - ones) % 10 

print(tens)

hundreds = (x - tens) % 10 

print(hundreds)

thousands = (x - hundreds) % 10

print(thousands)

# LS Solution

number = 4936

ones = number % 10
ones 

number = number // 10 
number 

tens = number % 10
tens

number = number // 10 

hundreds = number % 10
hundreds

thousands = number // 10
thousands 

# What does the following code do? Why?


print('5' + '10')


#Prints the concatenated string 510


# Refactor the code from the previous exercise to use coercion to print 15 instead.



# Will an error occur if you try to access a list element 
# with an index greater than or equal to the list's length? 
# For example:

foo = ['a', 'b', 'c']
print(foo[3])      # will this result in an error?

# Yes, no 4th index position

# To what value does the following expression evaluate?

'foo' == 'Foo'

# False

# What will the following code do? Why?

int('3.1415')

# Convert the string into an int and round to the nearest whole number

# WRONG: Value error; str value '3.1415' does not represent a valid integer

# To what value does the following expression evaluate?

'12' < '9'

# True

# Classify the following potential non-constant variable names as 
# idiomatic, non-idiomatic, or illegal. For the non-idiomatic and 
# illegal names, explain your choice.

index #idiomatic
CatName #non idiomatic
lazy_dog #idiomatic
quick_Fox #non idiomatic
1stCharacter #illegal (number)
operand2 #idiomatic
BIG_NUMBER #non idiomatic (unless constant)
π #non idiomatic (non ascii)


#Classify the following potential constant names as idiomatic,
# non-idiomatic, or illegal. For the non-idiomatic and illegal names,
# explain your choice.

index #non id (lowercase)
CatName #id WRONG no id, no lowercase at all
snake_case #non id
LAZY_DOG3 #id
1ST #illegal
operand2 #non id
BIG_NUMBER #id
Π #non id


# Classify the following potential class names as idiomatic,
#  non-idiomatic, or illegal. For the non-idiomatic and 
# illegal names, explain your choice.

index # id # WRONG non id, no starting w lowercase
CatName # id 
Lazy_Dog # id WRONG no underscores
1ST # illegal 
operand2 # id WRONG non id, no starting w lowercase
BigNumber3 # id 
Πi # non id

#Assume that obj already has a value of 42 when the code below 
# starts running. Which of the subsequent statements reassign 
# the variable? Which statements mutate the value of the 
# object that obj references? Which statements do neither? 
# If necessary, you can read the documentation.

obj = 'ABcd' # reassign
obj.upper() # mutate WRONG neither
obj = obj.lower() #mutate WRONG reassignment
print(len(obj)) #neither 
obj = list(obj) # reassign
obj.pop() # neither WRONG mutation
obj[2] = 'X' # mutate 
obj.sort() # mutate 
set(obj) # neither
obj = tuple(obj) # reassign

def hello():
    print('Hello')
    return True

hello()
print(hello())


#What happens when you run the following program? Why do we get that 
# result?

def set_foo():
    foo = 'bar'

set_foo()
print(foo)

#error: foo not defined in global scope


# What does this program print? Why?
foo = 'bar'

def set_foo():
    foo = 'qux'

set_foo()
print(foo)

#prints bar. 'foo' never passed as argument # WRONG, variable 
# shadowing, foo inside set_foo is local 




# Write a program that uses a multiply function to multiply 
# two numbers and returns the result. Ask the user to enter 
# the two numbers, then output the numbers and result as a 
# simple equation.


def multiply_numbers(num1, num2):
    num1 = input('Enter the first factor: ')
    num2 = input('Enter the second factor: ' )

    product = num1 * num2
    return print(f'The product of {num1} * {num2} is {product}.')

multiply_numbers()


# WRONG: their solution:

def multiply(left, right):
    return left * right

def get_number(prompt):
    entry = input(prompt)
    return float(entry)

first_number = get_number('Enter the first number: ')
second_number = get_number('Enter the second number: ')
product = multiply(first_number, second_number)
print(f'{first_number} * {second_number} = {product}')


# Identify the following items in that code: 

def multiply_numbers(num1, num2, num3):
    result = num1 * num2 * num3
    return result

product = multiply_numbers(2, 3, 4)

# Item
# function name = multiply_numbers
# function arguments = 2, 3, 4
# function definition = 
#                        def multiply_numbers(num1, num2, num3): # WRONG: everything lines 1-3
                       
#function body = 
 #            result = num1 * num2 * num3
  #           return result
#function parameters = num1, num2, num3
#function invocation = multiply_numbers(2, 3, 4)
# function return value = result # WRONG 24
# all identifiers = num1, num2, num3, multiply_numbers, result, product


# What does the following code print?
def scream(words):
    return words + '!!!!'

scream('Yipeee')

# returns yipeeee!!!! but does not print

# What does the following code print?

def scream(words):
    words = words + '!!!!'
    return
    print(words)

scream('Yipeee')

# Prints nothing, print invoked after return


#Without running the following code, what do you think it will do?

def foo(bar, qux):
    print(bar)
    print(qux)

foo('Hello')

#error bc no default param for second position

#Without running the following code, what do you think it will do?


def foo(bar, qux):
    print(bar)
    print(qux)

foo(42, 3.141592, 2.718)

# error, too many args

# Without running the following code, what do you think it will do?

def foo(first, second=3, third=2):
    print(first)
    print(second)
    print(third)

foo(42, 3.141592, 2.718)

# prints the args passed on new lines

# Without running the following code, what do you think it will do?

def foo(first, second=3, third=2):
    print(first)
    print(second)
    print(third)

foo(42, 3.141592)

# prints first two args then 2

# Without running the following code, what do you think it will do?

def foo(first, second=3, third=2):
    print(first)
    print(second)
    print(third)

foo(42)

# 42, 3, 2


# Without running the following code, what do you think it will do?


def foo(first, second=3, third=2):
    print(first)
    print(second)
    print(third)

foo()

# error no default param for first position


# Without running the following code, what do you think it will do?

def foo(first, second=3, third):
    print(first)
    print(second)
    print(third)

foo(42)

# error no default param for third position


# Identify all of the identifiers on each line of the following code.


def multiply(left, right):
    return left * right

def get_num(prompt):
    return float(input(prompt))

first_number = get_num('Enter the first number: ')
second_number = get_num('Enter the second number: ')
product = multiply(first_number, second_number)
print(f'{first_number} * {second_number} = {product}')

# multiply, left, right, get_num, prompt, first_number, second_number, product

# WRONG needs all built in methods (input, product, print)



# Using the code below, classify the identifiers as global, local, or built-in. For our purposes, you may assume this code is the entire program.

def multiply(left, right): # multiply: global left: global right: global
    return left * right # return: builtin left, right: local

def get_num(prompt): # get_num, prompt: global
    return float(input(prompt)) # return, float, input: builtin; prompt: local 

first_number = get_num('Enter the first number: ') #first_number, get_num: global
second_number = get_num('Enter the second number: ') # second_number, get_num: global
product = multiply(first_number, second_number) # product, multiply, first_number, second_number: global
print(f'{first_number} * {second_number} = {product}') #print: builtin; first_number, second_number, product: global

#In the code shown below, identify all of the function names and parameters present in the code. Include the line numbers for each item identified.

def multiply(left, right):
    return left * right

def get_num(prompt):
    return float(input(prompt))

first_number = get_num('Enter the first number: ')
second_number = get_num('Enter the second number: ')
product = multiply(first_number, second_number)
print(f'{first_number} * {second_number} = {product}')

# function names: multiply, return, get_num, print

# WRONG: return not a function. missed float, input

# params: left, right, prompt


#Which of the identifiers in the following program are function names? Which are method names? Which are built-in functions?

def say(message):
    print(f'==> {message}')

string1 = input()
string2 = input()

say(max(string1.upper(), string2.lower()))

# function names: say,
# 
# bultin function names:  print, input,  max
#
# method names: upper(), lower()


# The following function returns a list of the remainders of dividing the numbers in numbers by 3:

def remainders_3(numbers):
    return [number % 3 for number in numbers]

#Use this function to determine which of the following lists contains at least one number that is not evenly divisible by 3 (that is, the remainder is not 0):

numbers_1 = [0, 1, 2, 3, 4, 5, 6]
numbers_2 = [1, 2, 4, 5]
numbers_3 = [0, 3, 6]
numbers_4 = []

print(any(remainders_3(numbers_1))) # true
print(any(remainders_3(numbers_2))) # true
print(any(remainders_3(numbers_3))) # false
print(any(remainders_3(numbers_4))) # false

# The following function returns a list of the remainders of dividing the numbers in numbers by 5:

def remainders_5(numbers):
    return [number % 5 for number in numbers]

# Use this function to determine which of the following lists do not contain any numbers that are divisible by 5:

numbers_1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers_2 = [1, 2, 3, 4, 6, 7, 8, 9]
numbers_3 = [0, 5, 10]
numbers_4 = []


# To what values do the following expressions evaluate?

False or (True and False) # False
True or (1 + 2) # True 
(1 + 2) or True # True WRONG: 3
True and (1 + 2) # True WRONG 3
False and (1 + 2) # False
(1 + 2) and True # True
(32 * 4) >= 129 # False
False != (not True) # False
True == 4 # False
False == (847 == '847') # True

# Write a function, even_or_odd, that determines whether its argument is an even or odd number. If it's even, the function should print 'even'; otherwise, it should print 'odd'. Assume the argument is always an integer.

def even_or_odd():
    num = input('Enter a number: ')
    if int(num) % 2 != 0:
        print(f'{num} is odd')
    else:
        print(f'{num} is even')

even_or_odd()


# Without running the following code, what does it print? Why?

def bar_code_scanner(serial):
    match serial:
        case '123':
            print('Product1')
        case '113':
            print('Product2')
        case '142':
            print('Product3')
        case _:
            print('Product not found!')

bar_code_scanner('113') # Product2
bar_code_scanner(142) # Product Not found!


# Refactor this statement to use a regular if statement instead.

# return ('bar' if foo() else qux())

# if foo():
  #  return 'bar'
# else:
#    return qux()


# What does this code output, and why?

def is_list_empty(my_list):
    if my_list:
        print('Not Empty')
    else:
        print('Empty')

is_list_empty([])

# 'empty'


#Write a function that takes a string as an argument and returns an all-caps version of the string when the string is longer than 10 characters. Otherwise, it should return the original string. Example: change 'hello world' to 'HELLO WORLD', but don't change 'goodbye'.

def all_caps(string):
    if len(string) > 10:
        return print(string.upper())
    else:
        return print(string)

all_caps('hello')
all_caps('hello world')



# Write a function that takes a single integer argument and prints a message that describes whether:
# the value is between 0 and 50 (inclusive)
   # the value is between 51 and 100 (inclusive)
   # the value is greater than 100
   # the value is less than 0


def number_range(num):
    if num < 0:
        return print(f'{num} is less than 0')
    elif num >= 0 and num <= 50:
        return print(f'{num} is betweeen 0 and 50')
    elif num > 50 and num <= 100:
        return print(f'{num} is betweeen 51 and 100')
    else:
        return print(f'{num} is greater than 100')


number_range(0)     # 0 is between 0 and 50
number_range(25)    # 25 is between 0 and 50
number_range(50)    # 50 is between 0 and 50
number_range(75)    # 75 is between 51 and 100
number_range(100)   # 100 is between 51 and 100
number_range(101)   # 101 is greater than 100
number_range(-1)    # -1 is less than 0



# If you have a list named people, how can you determine the number of entries in that list?

people = ['jess', 'steve', 'harry']
print(len(people))


# Can you write some code to change the value 'bye' in the following tuple to 'goodbye'?

stuff = ('hello', 'world', 'bye', 'now')

stuff = list(stuff)
stuff[2] = 'goodbye'
stuff = tuple(stuff)
print(stuff)

# Identify at least 2 differences between lists and tuples. Identify at least 2 ways that lists and tuples are similar.

# tuples are immutable. their literals use parentheses instead of brackets. 
# they are ordered collection (sequences)s. they can contain any element

# Why can we treat strings as sequences?

# they are ordered collections of elements (characters)

# How do the set types differ from the sequence types?

# sets contain unique values only and are unordered

# Assuming you have the following assignment: 
# Write some code that converts the value of pi to a string and assigns it to a variable named str_pi.

pi = 3.141592

str_pi = str(pi)
print(str_pi)

# Without running the following code, identify the numbers that are included in each of the following ranges:

range(7) # [7] # WRONG [0, 1, 2, 3, 4, 5, 6]
range(1, 6) # [1, 2, 3, 4, 5]
range(3, 15, 4) # [3, 7, 11]
range(3, 8, -1) # []
range(8, 3, -1) # [8, 7, 6, 5, 4]


# How would you print all the numbers in the following range?

range(3, 17, 4)

print(list(range(3, 17, 4)))



my_list = [1, 2, 3, [4, 5, 6]]
another_list = list(my_list)

#Given the above code, answer the following questions and explain your answers:

#  Are the lists assigned to my_list and another_list equal?

Yes. Each of their elements has the same value.

# Are the lists assigned to my_list and another_list the same object?

Yes. another_list is a deep copy of my_list # NO: new object created by list() constructor

#Are the nested lists at index 3 of my_list and another_list equal?

Yes. Same elements, same positions.

#Are the nested lists at index 3 of my_list and another_list the same object?

No. Shallow copy # WRONG shallow copy, but this means they are the same object.... Shallow copies don't create new nested lists. Instead, only a reference to the nested list gets copied.and


# Bob expects the following code to print the names in alphabetical order. Without running the code, can you say whether it will? Explain your answer.


names = { 'Chris', 'Clare', 'Karis', 'Karl',
          'Max', 'Nick', 'Victor' }
print(names)

No. The order of sets is inscrutable # "Bob's code may print the names alphabetically on rare occasions, but it would do so only once every 5040 times."

# Consider the data in the following table:



def find_country(index):
    country_names = { 
        'Alice' : 'USA',
        'Francois' : 'Canada',
        'Inti' : 'Peru',
        'Monika' : 'Germany',
        'Sanyu' : 'Uganda',
        'Yoshitaka' : 'Japan',
        }
    print(country_names)
    #print(country_names[index])

find_country(1)


# Using collections

my_dict = {
    'a': 'abc',
    37: 'def',
    (5, 6, 7): 'ghi',
    frozenset([1,2]): 'jkl',
}

my_dict['a'] = 'ABC'
print(my_dict['a'])


seq = [4, 'abcdef', (True, False, None)]
print(4 in seq)
print(4 not in seq)
print('abcdef' in seq)
print('abcdef' not in seq)
print('cde' in seq[1])
print('cde' not in seq[1])
print('acde' in seq[1])
print('acde' not in seq[1])
print((True, False, None) in seq)
print((True, False, None) not in seq)
print(3.14 in seq)
print(3.15 not in seq)


my_set1 = {1, 4, -9, 16, 25, -36, -63, -1}
my_set2 = {'1', '4', '-9', '16', '25', '-36', '-1'}

print(min(my_set1), max(my_set1))
print(min(my_set2), max(my_set2))


numbers = (1, 1, 2, 3, 5, 8, 13, 21, 34)
print(sum(numbers))

names = ['Karl', 'Grace', 'Clare', 'Victor', 'Antonina', 'Allison', 'Trevor']
print(names.index('Clare'))
print(names.index('Trevor'))
print(names.index('Chris'))


iterable1 = [1, 2, 3]
iterable2 = ('Kim', 'Leslie', 'Bertie')
iterable3 = [None, True, False]

zipped_iterables = zip(iterable1, iterable2, iterable3)
print(list(zipped_iterables))


iterable1 = [1, 2]
iterable2 = ('Kim', 'Leslie', 'Bertie')
iterable3 = [None, True, False, 'Another String']


# dict operations

people_phones = {
    'Chris': '111-2222',
    'Pete': '333-4444',
    'Clare': '555-6666',
}

print(people_phones.keys())

pp(people_phones.values())

pp(people_phones.items())


# dictionary view objects

keys = people_phones.keys()
values = people_phones.values()

print(keys)
# dict_keys(['Chris', 'Pete', 'Clare'])

print(values)
# dict_values(['111-2222', '333-4444', '555-6666'])

people_phones['Max'] = '123-4567'
people_phones['Pete'] = '345-6789'
del people_phones['Chris']

print(keys)    # dict_keys(['Pete', 'Clare', 'Max'])
print(values)
# dict_values(['345-6789', '555-6666', '123-4567'])

numbers = [1, 2]

numbers.append(10)      
# Append the number 10
print(numbers)          
# [1, 2, 10]

numbers = [1, 2]

numbers.insert(0, 8)
print(numbers)

numbers = [1, 2]
numbers.extend([7, 8])
print(numbers)

#removing elements

my_list = [2, 4, 6, 8, 10]

my_list.remove(8)
print(my_list)

my_list.remove(8)


my_list = [2, 4, 6, 8, 10]

print(my_list.pop(1))
print(my_list)

my_list = [2, 4, 6, 8, 10]

my_list.clear()
print(my_list)

#sorting

names = ('Grace', 'zoe', 'Zoe', 'Clare', 'Allison', 'Trevor')
print(sorted(names))

print(names)

names = list(names)
print(names)

print(names.sort())
print(names)

#key=func keyword argument

words = ['abc', 'DEF', 'xyz', '123']
print(sorted(words))

print(sorted(words, key=str.lower))

numbers = ['1', '5', '100', '15', '534', '53']
numbers.sort()
print(numbers)

numbers.sort(key=int)
print(numbers)

#reverse

names = ('Grace', 'Clare', 'Allison', 'Trevor')
reversed_names = reversed(names)

print(reversed_names)

print(tuple(reversed(names)))

print(names)

names = list(names)
print(names.reverse())
print(names)

my_dict = {
    'abc':  1,
    'xyz': 23,
    'pqr': 0,
    'jkl': 5
    }
reversed_dict = reversed(my_dict)
print(my_dict)

print(list(reversed_dict))

names = ('Grace', 'Clare', 'Allison', 'Trevor')
for name in reversed(names):
    print(name)

# str operations

print("what's up?".capitalize())
print('456ABC'.capitalize())

print('four SCORE and sEvEn'.title())

print("i can't believe it's already mid-july".title())

import string
print(string.capwords("i can't believe it's already mid-july."))


'Four score and seven'.startswith('Four score')
'Four score and seven'.startswith('For score')
'Four score and seven'.startswith(' score')

'abc def'.startswith('def', 4)
'abc def ghi'.startswith('def', 4, 7)

'Four score and seven'.endswith('and seven')
'Four score and seven'.endswith('ad seven')
'Four score and seven'.endswith('score')

'abc def'.endswith(('abc', 'xyz', 'stu'))
'abc def'.endswith(('abc', 'def'))
'abc def'.endswith('def', 4)
'abc def ghi'.endswith('def', 4, 7)

print("What's up?".swapcase())
print('456ABC'.swapcase())
print('456ABC'.swapcase().swapcase())

'Hello'.isalpha()
'Good-bye'.isalpha()
'Four score'.isalpha()
''.isalpha()

'12340'.isdigit()
'123.4'.isdigit()
'-1234'.isdigit()
''.isdigit()


#stripping 

text = ' \t  abc def    \n\r'
print(repr(text))             # ' \t  abc def    \n\r'
print(repr(text.strip()))     # 'abc def'



text = ' \t  abc def    \n\r'
print(repr(text.strip('abc')))

text = 'aaabaacccabxyzabccba'
print(text.strip('a'))
print(text.strip('ab'))
print(text.strip('ba'))
print(text.strip('abc'))
print(text.strip('bc'))

#splitting
text = '  Four     score and   seven years ago.   '
print(text.split())

print('no-spaces'.split())

text = ',Four,score,and,,,seven,years,ago,'
print(text.split(','))

text = 'Four<>score<:>and<>seven<>years<>ago'
print(text.split('<>'))

text = 'abcde'
print(list(text))
print(tuple(text))

text = 'abcde'
for char in text:
    print(char)

#join
words = ['You', 'were', 'lucky']
print(''.join(words))
print(' '.join(words))
print(','.join(words))
print('\n '.join(words))

#find

school = 'launch school'

print(school.find(' '))
print(school.find('l'))
print(school.find('h'))
print(school.find('hoo'))
print(school.find('x'))
print(school.find('N'))

print(school.rfind(' '))
print(school.rfind('l'))
print(school.rfind('h'))
print(school.rfind('hoo'))
print(school.rfind('oh'))
print(school.rfind('N'))


text = 'abc abc def abc'

print(text.find(' ', 4))
print(text.find(' ', 8))

print(text.find('c', 0, 2))
print(text.rfind('c', 3, 10))

text = 'abc abc def abc'
print(text[3:10].find('c'))
print(text.find('c', 3, 10))


# nested collections

nested_list = [
    {'foo':42, 'bar': [1, 2, 3], 'qux': None},
    {
        'Kim',
        ('Leslie', 'Les'),
        ('Pete', 'Peter')
        ('Jonathan', 'Jon', 'Jack'),
    },
    (4, 5, (1, 2, 3,), 6, 7),
    ['a', 'b', 'cde', -3.141592],
]

my_set = {1, 2, 3, [4, 5]}
my_set = {1, 2, 3, {4, 5}}

my_set = {1, 2, 3, frozenset([4, 5]) }

my_tuple = (1, 2, 3, [4, 5], {6, 7}, {'x': 'a dict'})


deck = [
    {'suit': 'Clubs', 'value': '2'},
    {'suit': 'Clubs', 'value': '3'},
    {'suit': 'Clubs', 'value': '4'},
    # ...
    {'suit': 'Spades', 'value': 'Queen'},
    {'suit': 'Spades', 'value': 'King'},
    {'suit': 'Spades', 'value': 'Ace'},
]

print(f"{deck[49]['value']} of {deck[49]['suit']}")


nested_seq = [
    [1, 2,[3, 4, (5, 6, 7, 8)]],
    [9, [10, (11,)]],
    [12, 13, [14, 15, (16, 17)]],
    [18, [19, 20, (21, 22)]],
]

print(nested_seq[1])
print(nested_seq[3][0])
print(nested_seq[0][2][2])
print(nested_seq[2][2][2][1])


# collection comparisons

print([2, 3] == [2, 3])
print([2, 3] == [3, 2])
print([2, 3] == [2])
print([2, 3] == (2, 3))
print({2, 3} == {3, 2})

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 2, 'a': 1}
dict3 = {'a': 1, 'b': 2, 'c': 3}

print(dict1 == dict2)
print(dict1 == dict3)
