# Print all of the even numbers in the following list of nested lists. 
# This time, don't use any for loops.

my_list = [
  [1, 3, 6, 11],
  [4, 2, 4],
  [9, 17, 16, 0],
]

index_my_list = 0
index_nested_list = 0

result = []

while index_my_list < len(my_list):
    while index_nested_list < len(my_list[index_my_list]):
        if my_list[index_my_list][index_nested_list] % 2 == 0:
            result.append(my_list[index_my_list][index_nested_list])
        index_nested_list += 1
    index_nested_list = 0
    index_my_list += 1
index_my_list = 0

print(result)

# ls solution

outer_index = 0
while outer_index < len(my_list):
    inner_index = 0
    while inner_index < len(my_list[outer_index]):
        number = my_list[outer_index][inner_index]
        if number % 2 == 0:
            print(number)
        inner_index += 1
    outer_index += 1
