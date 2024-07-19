# Write a function called increment_counter that increments a counter variable every time it is called. 

counter = 0

def increment_counter():
    global counter
    counter += 1 # varialbe reassignment in functions needs to reference global, 
                 # otherwise python will throw an error: 

                    # UnboundLocalError: cannot access local variable 'counter' where it 
                    # is not associated with a value

# You can test your code with the following:

print(counter)                # 0

increment_counter()
print(counter)                # 1

increment_counter()
print(counter)                # 2

counter = 100
increment_counter()
print(counter)                # 101
