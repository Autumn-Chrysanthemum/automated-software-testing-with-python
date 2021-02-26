x = (5, 11)
y = 5, 11
z = [(5, 11)]

a, b  = 5, 11

c = 5, 11
d, f = c
print(d, f)


students_attendance = {"Natalia": 96, "Adam": 80, "Alex": 100}

print(list(students_attendance.items()))

for student, attendance in students_attendance.items():
    print(f"{student}: {attendance}")

people = [("Natalia", 45, "Artist"),("Alex", 45, "Dev"),("Matt", 45, "QA")]

for name, age, prof in people:
    print(f"Name: {name}, Age: {age}, profession: {prof}")

for person in people:
    print(f"Name: {person[0]}, Age: {person[1]}, profession: {person[2]}")

person = ("Natalia", 45, "Artist")

name, _, profession = person
print(name, profession)


head, *tail = [1, 2, 3 ,4 ,5]
print(head)
print(tail)

*head, tail = [1, 2, 3 ,4 ,5]
print(head)
print(tail)