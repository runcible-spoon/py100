numbers = [1, 2, 3]
print(numbers)

numbers2 = numbers

print(id(numbers) == id(numbers2))
print(numbers is numbers2)

print(id(numbers))
print(id(numbers2))



numbers = [1, 2, 3]
numbers2 = [1, 2, 3]

print(numbers)
print(numbers == numbers2)
print(numbers is numbers2)
