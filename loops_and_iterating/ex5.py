# Print all of the even numbers in the following list of nested lists. 
# Don't use any while loops.

my_list = [
    [1, 3, 6, 11],
    [4, 2, 4],
    [9, 17, 16, 0],
]

index = 0
new_list = []

for item in my_list:
    for num in my_list[index]:
        if num % 2 == 0:
            new_list.append(num)
    index += 1

print(new_list)


# solution

for nested_list in my_list:
    for number in nested_list:
        if number % 2 == 0:
            print(number)
