letters = 'abcdefghijklmnopqrstuvwxyz'

# Note that the parentheses surrounding this
# multi-line chain are required.
consonants = (letters.replace('a', '').
              replace('e', '').
              replace('i', '').
              replace('o', '').
              replace('u', ''))
print(consonants)
