my_variable = 'hello'
print(my_variable[0])

my_string = "Natalia"

for char in my_string: #iterables are LISTS, SETS, TUPLES, AND MORE

    print(char)

my_list = [1,2,5,7,9]

for num in my_list:
    print(num**2)

user_num  = True

# while user_num == True:
#     # user_num == False
#     user_input = input("Should we print again? (y/n)")
#     print(10)
#
#     if user_input == "n":
#         user_num = False



number = 7


while True:
    user_input = input("Would you like to play? (Y/n) ")

    if user_input == "n":
        break

    user_number = int(input("Guess our number: "))
    if user_number == number:
        print("You guessed correctly!")
    # elif number - user_number in (1, -1):
    elif abs(number - user_number) == 1:
        print("You were off by one.")
    else:
        print("Sorry, it's wrong!")

    print("Done playing!")


friends = ["Bob", "Rolf", "Anne"]

for friend in friends:
    print(f"{friend} is my friend")

for friend in range(4):
    print(f"{friend} is my friend")

grades = [53, 67, 98, 100, 100]
total = 0
total = sum(grades)
amount = len(grades)

# for grade in grades:
#     total += grade

print(total/amount)