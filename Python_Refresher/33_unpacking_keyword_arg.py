# def named(**kwargs):
#     print(kwargs)
#
# named(name="Natalia", age=25)


def named(name, age):
    print(name, age)

details = {"name": "Natalia", "age": 25}

named(**details)

def print_nicely(**kwargs):
    named(**kwargs)
    for arg, value in kwargs.items():
        print(f"{arg}: {value}")

print_nicely(**details)


def both(*args, **kwargs):
    print(args)
    print(kwargs)

both(1, 3, 5, name="Bob", age=15)

