# Write Python code to create a new tuple from (1, 2, 3, 4, 5). 
# The new tuple should be in reverse order from the original. 
# It should also exclude the first and last members of the original. 
# The result should be the tuple (4, 3, 2).

t = (1, 2, 3, 4, 5)
rev_t = list(reversed(t))
print(rev_t)
rev_t.remove(1)
rev_t.remove(5)
print(tuple(rev_t))
