# student = {'name': 'Jose', 'school': 'Computing', 'grades': (66, 77, 88)}
#
# def average(sequence):
#     return sum(sequence) / len(sequence)
#
# print(average(student["grades"]))
# print(student.average())


class Student:
    def __init__(self, name, grades):
        # self.name = "Natalia"
        self.name = name
        self.grades = grades

    def average(self):
        return sum(self.grades) / len(self.grades)

student = Student("Bob", (100, 100, 93, 78, 90))
student2 = Student("Natalia", (100, 100, 93, 78, 90, 100))
print(student.name)
print(student.grades)
print(Student.average(student))
print(student2.average())
