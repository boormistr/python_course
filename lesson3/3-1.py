def division(numerator, denominator):
    try:
        return numerator/denominator
    except ZeroDivisionError:
        print('Division by ZERO!')
