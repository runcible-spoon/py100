# Write Python code to replace all the : characters in the string below with +.

info = 'xyz:*:42:42:Lee Kim:/home/xyz:/bin/zsh'
print('info: ' '\n', info, '\n')

# Try this problem using the methods you've learned about in this chapter. 

split_info = info.split(':')
print('split_info: ', '\n', split_info, '\n')

plusses = []
for element in split_info:
    plusses.append('+')

print('plusses: ', '\n', plusses, '\n')

info_plusses = list(zip(split_info, plusses))

print('info_plusses: ', '\n', info_plusses, '\n')

final_string = ''.join(list(info_plusses[0])) + ''.join(info_plusses[1]) + ''.join(info_plusses[2]) + ''.join(info_plusses[3]) + ''.join(info_plusses[4]) + ''.join(info_plusses[5]) + ''.join(info_plusses[6])
print(final_string.rstrip('+'), '\n')

# Easier solution..... 

split_info = info.split(':')

result = '+'.join(split_info)
print('result: ', result)

# Once you have that working, use the Python documentation for the str type to 
# find an alternative solution.

info = 'xyz:*:42:42:Lee Kim:/home/xyz:/bin/zsh'

info_plusses = info.replace(':', '+')
print(info_plusses)
