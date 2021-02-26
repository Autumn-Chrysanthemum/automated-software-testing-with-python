from typing import List, Optional

class Student:
    # def __init__(self, name: str, grades: List[int] = []): #This is bad!!!! because [] mutable and it was created when the function was created
    def __init__(self, name: str, grades: Optional[List[int]] = None): #This is good
        self.name = name
        self.grades = grades or [] # None or [] == []

    def take_exam(self, result):
        self.grades.append(result)

bob = Student("Bob") # not here when it was called
rolf = Student("Rolf") # not here when it was called
bob.take_exam(90)
print(bob.grades)
print(rolf.grades)