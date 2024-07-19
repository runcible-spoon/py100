# The following code causes an infinite loop 
# (a loop that never stops iterating). Why?

counter = 0

while counter < 5:
    print(counter)

# counter is never incremented
