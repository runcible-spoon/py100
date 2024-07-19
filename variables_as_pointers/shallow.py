import copy

orig = [[1, 2], 3, 4]
dup = copy.copy(orig)

print(orig is dup)
print(orig == dup)
orig[2] = 44
print(dup)

print(orig[0] is dup[0])
orig[0][1] = 22
print(dup[0])
