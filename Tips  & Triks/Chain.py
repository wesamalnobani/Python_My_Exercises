
#chain

import itertools

a = [1, 2, 3, 4]

for p in itertools.chain(itertools.combinations(a, 2), itertools.combinations(a, 3)) :
    print(p)


a = [[1, 2],[3, 4],[5, 6]]
print(list(itertools.chain.from_iterable(a)))
