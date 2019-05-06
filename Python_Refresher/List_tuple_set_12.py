my_variable = 'hello'

grad_one = 77
grad_two = 98
grad_three = 90
grad_four = 79
grad_five = 89

# LIST
grads_list = [70,88,58,99,78,68,56,98]
grads_list.append(99)
print(sum(grads_list)/len(grads_list))
print(grads_list) # always ordered in order we put elements in
print(grads_list[0])
grads_list[0]=60
print(grads_list)

# TUPLE
grads_tuple = (70,88,58,99,78,68,56,98)
# grads_tuple.append(99) # can not increase size of tuple
print(sum(grads_tuple)/len(grads_tuple))
# we can change tuple whole:
grads_tuple = grads_tuple + (100,)
# comma have to be at the end of 100 because it is a tuple now
# we did't change tuple, we calculated a new tuple
# can't assign == can't change

#SET
grads_set = {70,88,58,99,78,68,56,98,99} #set unordered, unique collection of elements
print(sum(grads_set)/len(grads_set)) # will not count duplicates
print(grads_set) # will not print second 99, only unique
# we should be able to change it, but how to assign if it is not ordered, not indexes
grads_set.add(60)
print(grads_set)
grads_set.add(60) #not going to add the same value because it shoul be unique
print(grads_set)

your_lottery_numbers = {1,2,3,4,5}
winning_numbers = {1,3,5,7,9,11}

print(your_lottery_numbers.intersection(winning_numbers))
print(winning_numbers.intersection(your_lottery_numbers))
print(your_lottery_numbers.union(winning_numbers))
print(winning_numbers.union(your_lottery_numbers))
print(winning_numbers.difference(your_lottery_numbers))


