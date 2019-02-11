
#Permutations

import itertools

for p in itertools.permutations([1, 2, 3, 4]):
    print(p, "  >  ",''.join(str(x) for x in p))


x = list(itertools.permutations('ab'))
print(x)
