from itertools import count as cnt, cycle as ccl
from time import time


def first(start, end):
    for n in cnt(start):
        if n > end:
            break
        else:
            yield n


for i in first(5, 150):
    print(i)


def second(lst, duration):
    start = time()
    for i in ccl(lst):
        if time() - start > duration:
            break
        else:
            print(i)


second([1, 2, 3], 3)

