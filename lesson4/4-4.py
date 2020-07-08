first = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
second = [x for x in first if first.count(x) == 1]
print(second)