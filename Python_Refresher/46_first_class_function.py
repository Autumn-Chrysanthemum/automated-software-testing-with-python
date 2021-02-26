def divide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Divisor cannot be 0.")

    return dividend / divisor

def calculate(*values, operator):
    return operator(*values)

result = calculate(20, 4 , operator=divide)
print(result)



from operator import itemgetter

def search(sequence, expected, finder):
    for elem in sequence:
        if finder(elem) == expected:
            return elem
    raise RuntimeError(f"Could not find an element with {expected}")

friends = [
    {"name": "Matt Smith", "age": 15},
    {"name": "Natalia Smith", "age": 18},
    {"name": "Alex Smith", "age": 24},
]

# def get_friend_name(friend):
#     return friend["name"]

# print(search(friends, "Bob Smith", get_friend_name))
# print(search(friends, "Bob Smith", lambda friend: friend["name"]))
print(search(friends, "Matt Smith", itemgetter("name")))