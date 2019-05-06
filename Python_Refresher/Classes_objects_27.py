lottery_player_dict ={
    'name': "Natalia",
    "numbers": (5,6,12,3,1,21)}

class LotteryPlayer:
    def __init__(self,name):
        self.name = name
        self.numbers = (5,6,12,3,1,21)

    def total(self):
        return sum(self.numbers)




# player_one = LotteryPlayer()
# player_two = LotteryPlayer()
# print(player_one.name)
# print(player_one.numbers)
# print(player_one.total())

# print(player_one == player_two)
# print(player_one.name == player_two.name)

player_one = LotteryPlayer("Natalia")
player_two = LotteryPlayer("Jose")

# print(player_one == player_two)
# print(player_one.name == player_two.name)
player_one.numbers = (1,5,3,5,4)
# print(player_one.numbers == player_two.numbers)

class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks) / len(self.marks)

    @classmethod
    def go_to_school(cls):
        # print("I'm going to {}".format(self.school))
        print("I'm going to school")
        print("I'm a {}".format((cls)))

    # @staticmethod
    # def go_to_school():
    #     print("I'm going to school")

anna = Student("Anna", "MIT")
anna.marks.append(90)
anna.marks.append(100)
print(anna.marks)
print(anna.average())
# print(anna.go_to_school())
print(Student.go_to_school())

