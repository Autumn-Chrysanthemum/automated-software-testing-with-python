def add(x, y=8):
#def add(x = 5, y): #can't do, positinal first
    print(x + y)

add(5)
add(x = 5)
#add(y = 5)# can't do, x is required
add(x = 5, y = 5)
#add(x = 5, 5) # can't do, positinal first

# DO NOT DO:
default_y = 3

def add(x, y=default_y):
    sum = x + y
    print(sum)

add(2)

default_y = 4
add(2) # default_y will remain == 3 since it was define earlier and can't be redefine

