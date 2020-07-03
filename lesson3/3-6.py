def int_func(text):
    return text.capitalize()


print(' '.join(list(map(int_func, input().split()))))


def int_func2(text):
    return text.title()


print(int_func2(input()))

# Два варианта - первый интересный, второй правильный
