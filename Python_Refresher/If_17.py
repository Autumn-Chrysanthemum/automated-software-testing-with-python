# should_continue = True
#
# if should_continue == True:
#     print('Hello')
#
# if should_continue:
#     print('Hello')
#
#     people = ["Natalia", "Olga", "Tanya"]
#     person = input("Enter the person you know: ")

# if person in people:
#     print("you know this person")
#
# if person not in people:
#     print("you don't know this person")
#
# if person in people:
#     print("you know {}".format(person))
# else:
#     print("you don't know {}".format(person))

def who_do_you_know():
    people_you_know = input("Enter people you know comma separated: ")
    people_list = people_you_know.split(",")


    people_without_spaces_list = []
    for person in people_list:
        people_without_spaces_list.append(person.strip())
    return people_without_spaces_list

# def who_do_you_know():
# people_without_spaces_        time.sleep(5)list = [person.strip() for person in people_list)]
# people_without_spaces_list = [person.strip() for person in people_you_know.split(",")]
# people_without_spaces_list = [person.strip() for person in input("Enter people you know comma separated: ").split(",")]
# return [person.strip() for person in input("Enter people you know comma separated: ").split(",")] #CORRECT BUT NOT READABLE ANYMORE


def ask_user():
    user_name = input("What is your name?")
    if user_name in who_do_you_know():
        print("We know you {}!".format(user_name))
    else:
        print("Who are you?")


