
#Assigning Variables

a, b, c = 1, 2, 3
print('\n', a, b, c)

a, b, c = [1, 2, 3]
print('\n', a, b, c)

a, b, c = [1, (2, 3), 4]
print('\n', a, b, c)

a, (b, c), d = [1, (2, 3), 4]
print('\n', a, b, c, d)

a, b, c = (2 * i for i in range(3))
print('\n', a, b, c)

a, *b, c = [1, 2, 3, 4, 5]
print('\n', a, b, c)

a, b = 1, 2
a, b = b, a
print('\n', a, b)
