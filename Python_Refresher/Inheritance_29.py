class Student:
    def __init__(self,name,school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks)/len(self.marks)

    @classmethod
    def friend(cls, origin, friend_name,*args):
        return cls(friend_name, origin.school, *args)

# anna = Student("Anna", "Oxford")
# friend = anna.friend("Greg")
#
# print(friend.name)
# print(friend.school)

class WorkingStudent(Student):

    def __init__(self, name, school, salary, job_titile):
        super().__init__(name,school)
        self.salary = salary

anna = WorkingStudent("Anna", "Oxford", 150000, "Software tester")
friend = WorkingStudent.friend(anna,"Greg", 1000000, "Deleloper")

print(friend.name)
print(friend.school)
print(anna.salary)
print(friend.salary)



