# Use a while loop to print the numbers in my_list, one number per line. 
# Then, do the same with a for loop.

my_list = [6, 3, 0, 11, 20, 4, 17]

index = 0
while index < len(my_list):
    print(f'{my_list[index]} \n')
    index += 1


for num in my_list:
    print(f'{num} \n')
