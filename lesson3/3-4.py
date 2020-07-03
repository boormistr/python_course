def my_func(x, y):
    return x**y


def my_func2(x, y):
    result = 1
    while y != 0:
        result *= x
        y += 1
    return 1/result
