def my_method(arg1,arg2):
    return arg1+arg2

my_method(5,6)

def my_long_method(arg1,arg2,arg3,arg4,arg5):
    return arg1+arg2+arg3+arg4+arg5


def my_list_addition(list_arg):
    return sum(list_arg)

my_long_method(4,5,6,7,8)

my_list_addition([3,4,7,5,4])

def addition_simple(*args):
    return sum(args)

addition_simple(3,5,7,5,6,7,5,4)

def what_are_kwargs(*args,**kwargs):
    print(args)
    print(kwargs)

what_are_kwargs(5,5,6,6,5,2,3,4,2, name ="Jose", location = "UK")