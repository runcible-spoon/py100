import copy

orig = [[1, 2], 3, 4]
dup = copy.deepcopy(orig)

print('orig is dup): ', orig is dup)
print('orig == dup): ', orig == dup)
orig[2] = 44
print('dup): ', dup)

print('orig[0] is dup[0]: ', orig[0] is dup[0])
orig[0][1] = 22
print('dup[0]): ', (dup[0]))
