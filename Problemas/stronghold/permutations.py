import math
import itertools

n = 5

print(math.factorial(n))
perm = itertools.permutations(list(range(1, n + 1)))

for i, j in enumerate(list(perm)):
    permutation = ''
    for item in j:
        permutation += str(item) + ' '
    print(permutation)