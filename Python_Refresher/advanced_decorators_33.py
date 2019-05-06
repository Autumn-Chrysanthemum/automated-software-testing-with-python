import functools



def decorator_with_arguments(number):
    def my_decorator(func):
        @functools.wraps(func)
        def function_that_runs_func():
            print("in the decorator!")
            if number == 56:
                print("Not running the function!")
            else:
                func()
            print("After the decorator!")
        return function_that_runs_func
    return my_decorator


@decorator_with_arguments(56)
def my_function_too():
    print("Hello")

###### function can taka parameters

def decorator_with_arguments(number):
    def my_decorator(func):
        @functools.wraps(func)
        def function_that_runs_func(*args, **kwargs):
            print("in the decorator!")
            if number == 56:
                print("Not running the function!")
            else:
                func(*args, **kwargs)
            print("After the decorator!")
        return function_that_runs_func
    return my_decorator


@decorator_with_arguments(57)
def my_function_too(x,y):
    print(x+y)
my_function_too(57,67)

# We can pass something as user permissions.
# if user is not matching admin criteria we are not showing him admin page