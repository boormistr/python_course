def my_sum():
    result = 0
    while True:
        val = input()
        try:
            n = val.split().index('q')
            result += sum(list(map(int, val.split()[:n])))
            print(result)
            break
        except ValueError:
            result += sum(list(map(int, val.split())))
            print(result)


my_sum()
