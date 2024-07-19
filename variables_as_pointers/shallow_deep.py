
my_list = [[1, 2], 3, 4]
shallow = list(my_list)
print(shallow[0] is my_list[0])

my_dict = {'abc': [1, 2, 3]}
shallow = dict(my_dict)
print(shallow['abc'] is my_dict['abc']) 
