# Question 1 We have two lists of numbers given below. I want you to create a third list by picking an odd-indexed element from the first list and even-indexed elements from the second list.
# list_1 = [5, 10, 15, 20, 25, 30, 35]
# list_2 = [7, 14, 21, 28, 35, 42, 49]

list_1 = [5, 10, 15, 20, 25, 30, 35]
list_2 = [7, 14, 21, 28, 35, 42, 49]
evenList = list_1[1::2] + list_2[::2]
print(evenList)
