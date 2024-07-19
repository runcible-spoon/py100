# Explain why the code below prints different values on lines 3 and 4.

text = "It's probably pining for the fjords!"

print(text[21:35].rfind('f'))     # 8

# Finds 'f' at index position 8 of string slice "for the fjords!"
# when looking from the right

print(text.rfind('f', 21, 35))    # 29

# same, just counting relative to original string's index numbers.
