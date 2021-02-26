def add(x, y):
    return x + y

print(add(5, 8))


def divide(dividend, divisor):
    if divisor != 0:
        return dividend / divisor
    else:
        return "You fool!"

print(divide(dividend=15, divisor=0))