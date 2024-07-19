# Without running this code, what will it print? Why?

set1 = {42, 'Monty Python', ('a', 'b', 'c')}
set2 = set1
set1.add(range(5, 10))
print(set2)

# output
{42, 'Monty Python', ('a', 'b', 'c'), 5, 6, 7, 8, 9}

# actual output:
{('a', 'b', 'c'), 'Monty Python', 42, range(5, 10)}
