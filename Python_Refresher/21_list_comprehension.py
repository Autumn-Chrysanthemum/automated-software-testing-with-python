my_list = [0,1,2,3,4,5]

equal_list = [x for x in range(5)]

multiply_list = [x*3 for x in range(5)]
print(multiply_list)

print(8%3)
print(9%2)
print(4%2)

even_list = [x for x in range(10) if x%2 == 0]
print(even_list)

people = ['ASDF', 'sdfdsf','Ssdfd', '  dfsfs']
normal_people= [person.strip().capitalize() for person in people]
print(normal_people)

numbers = [1,3,5]
doubled = [num * 2 for num in numbers]

# doubled = []
# for num in numbers:
#     doubled.append(num * 2)

print(doubled)


friends = ["Bob", "Rolf", "Anne", "Natalia", "Sam", "Samanta", "Sarra"]
starts_s = [friend for friend in friends if friend.startswith("S")]
# # starts_s = []
# for friend in friends:
#     if friend.startswith("S"):
#         starts_s.append(friend)

print(starts_s)

friends_s = ["Sam", "Samanta", "Sarra"]
print(friends_s is starts_s)
print(friends_s[0] is starts_s[0])
print("friends_s: ", id(friends_s), "starts_s: ", id(starts_s))




