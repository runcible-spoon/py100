# Which of the following values can't be used as a key in a dict object, and why?

'cat' # Yes
(3, 1, 4, 1, 5, 9, 2) # Yes
['a', 'b'] # No, mutable
{'a': 1, 'b': 2} # No,  mutable
range(5) # Yess
{1, 4, 9, 16, 25} # No, mutable
3 # Yes
0.0 # Yes
frozenset({1, 4, 9, 16, 25}) # Yes
