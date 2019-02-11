
#Lists

a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print('\n', a[-1], a[-3])

a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print('\n', a[2:8])

a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print('\n', a[-4:-2])

a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print('\n', a[::2])

a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print('\n', a[::-1])
print('\n', a[::-2])

a = [0, 1, 2, 3, 4, 5]
a[2:3] = [0, 0]
print('\n', a)

#Find The Most Frequent Value In A List
test = [1, 2, 3, 4, 2, 2, 3, 1, 4, 4, 4]
print(max(set(test), key = test.count))
