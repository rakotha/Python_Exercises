# Question 7 We have a list of lists that contains several numbers. I want you to print the list whose sum of elements is the highest and also the lowest.
# num_list = [[2, 8, 11], [4, 5, 7, 12], [8, 9, 10, 11], [19, 13, 7], [2, 5, 16]]
num_list = [[2, 8, 11], [4, 5, 7, 12], [8, 9, 10, 11], [19, 13, 7], [2, 5, 16]]
maxi = sum(num_list[0])
mini = sum(num_list[0])
maxlist = num_list[0]
minlist = num_list[0]

for lst in num_list:
    if maxi < sum(lst):
        maxi = sum(lst)
        maxlist = lst
    if sum(lst) < mini:
        mini = sum(lst)
        minlist = lst

print("The list with the maximum sum of elements: {}".format(maxlist))
print("The list with the minimum sum of elements: {}".format(minlist))