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
