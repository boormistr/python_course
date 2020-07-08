first = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
second = [first[i] for i in range(1, len(first)) if first[i-1] < first[i]]
print(second)
