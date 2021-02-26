def add(x, y):
    return x + y

print(add(5, 7))


add_lambda = lambda x, y : x + y # first x, y are parameters and x + y what we return
print(add_lambda(5, 7))

# if no name give needed to be used the same line it is defined:
print((lambda x, y : x + y)(5,7))


def double(x):
    return x * 2

sequence = [1, 3, 5, 9]
doubled = [double(x) for x in sequence]
print(doubled)

doubled_lambda_compr = [(lambda x: x * 2)(x) for x in sequence]
print(doubled_lambda_compr)

doubled_with_map = list(map(double, sequence)) # go through each element of iterable (sequence) and apply double on each element
print(doubled_with_map)

doubled_with_lambda = list(map(lambda x: x * 2, sequence))
print(doubled_with_lambda)
