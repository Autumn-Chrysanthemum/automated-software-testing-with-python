my_dict = {"name": "jose", "age": 90, "grade": [56,76,56,99]}
my_dict_num = {1: 15, 2: 90, 3:94} #can be sequence

lottery_player = {
    "name": "Folf",
    'numbers': (24,35,46,57) # can be tuple
}

universities = [
    {
        "name":"Oxford",
        "location": "UK"
    },
    {
        "name": "MIT",
        "location": "US"
    }

]

#WE CAN PUT ANYTHING WE WANT AS A VALUE OF A KEY
# dictionary represent things

dict_in_dict = {
    "key": {
        "name":"Jose"
    }
}

print(sum(lottery_player["numbers"])) #access to this key

lottery_player["name"] = "John"
#lottery_player["numbers"][0] = 50 # can't do because it is a tuple

friend_ages = {"Natalia": 24, "Adam": 30, "Alex": 45}

friend_ages["Bob"] = 50
friend_ages["Bob"] = 70

print(friend_ages["Adam"])
print(friend_ages)

friends = [
    {"name":"Natalia", "age": 33},
    {"name": "Alex", "age": 44},
    {"name": "Matt", "age": 13},
]

print(friends[1]["name"])

students_attendance = {"Natalia": 96, "Adam": 80, "Alex": 100}

for student, attendance in students_attendance.items():
    # print(student)
    # print(f"{student}: {students_attendance[student]}")
    print(f"{student}: {attendance}")

if "Bob" in students_attendance:
    print(f"Bob: {students_attendance['Bob']}")
else:
    print("Bob is not a student in this class")

attendance_values = students_attendance.values()
print(sum(attendance_values)/len(attendance_values))
