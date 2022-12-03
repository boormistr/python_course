import math
keys = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

d = {k: [] for k in keys}
d1 = dict.fromkeys(keys, [])

print(d == d1)

print('d до цикла: ', d)
for i in keys:
    d[i].append(i)
print('d после цикла: ', d)

print('d1 до цикла: ', d1)
d1[0].append('c')
for i in keys:
    d1[i].append(i)
print('d1 после цикла: ', d1)
