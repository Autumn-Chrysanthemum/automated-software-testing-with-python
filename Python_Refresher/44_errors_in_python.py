def divide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Divisor cannot be 0.")

    return dividend / divisor

# print(divide(dividend=15, divisor=0))

# grades = [78, 99, 85, 100]
grades = []

print("Welcome to the average grade program")

try:
    average = divide(sum(grades), len(grades))
except ZeroDivisionError as e: # if that error - no ELSE would be run
    # print(e)
    print("There are not grades yet in your list")
else: # will run if NO errors !!!!!
    print(f"The average grade is {average}")
finally: # will be run no matter what
    print("Thank you!")

