'''
Check whether the keys 'name' and 'grade' exist in the following dictionary:
'''

student = {
    'id': 123,
    'grade': 'B',
}

print(dict.items(student))

print('name' in student)
print('grade' in student)
