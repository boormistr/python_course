from math import factorial


def fact(n):
    for n in [factorial(x) for x in range(n)]:
        yield n


for i in fact(5):
    print(i)
