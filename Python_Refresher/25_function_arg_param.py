def add(x, y): #parameters
    result = x + y
    print(result)

add(5, 3)  #arguments


def say_hello(name, surname):
    print(f"Hello, {name}")

say_hello("Bob", "Smith") #positionals argument


def say_hello(name, surname):
    print(f"Hello, {name}")

say_hello(surname = "Smith",name = "Bob") #keyword arguments


def divide(dividend, divisor):
    if divisor != 0:
        print(dividend / divisor)
    else:
        print("You fool!")

divide(dividend=15, divisor=0)
#divide(15, divisor=0) #can be combination posional arguments and keywords arguments