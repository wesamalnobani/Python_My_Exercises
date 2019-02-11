
#unify the list containing lists and tuples

#<pip install more_itertools>

import more_itertools

test = [[-1, -2], [1, 2, 3, [4, (5, [6, 7])]], (30, 40), [25, 35]]
print(list(more_itertools.collapse(test)))
