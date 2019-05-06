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




