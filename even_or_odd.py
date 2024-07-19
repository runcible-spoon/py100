def even_or_odd():
    num = input('Enter a number: ')
    if int(num) % 2 != 0:
        print(f'{num} is odd')
    else:
        print(f'{num} is even')

even_or_odd()
