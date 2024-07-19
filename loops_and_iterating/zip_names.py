forenames = ['Ken', 'Lynn', 'Pat', 'Nancy']
surnames = ['Camp', 'Blake', 'Flannagan', 'Short']

# while loop method
'''
index = 0
while index < len(forenames):
    if index >= len(surnames):
        break

    forename = forenames[index]
    surname = surnames[index]
    print(f'{forename} {surname}')

    index += 1
'''

# zip and for method
zipped_names = zip(forenames, surnames)
for forename, surname in zipped_names:
    print(f'{forename} {surname}')
