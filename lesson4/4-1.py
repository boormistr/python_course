from sys import argv
_, hours, rate, bonus = argv


def salary(h, r, b):
    return h * r + b


print(salary(int(hours), int(rate), int(bonus)))
