# Question 1
list_1 = [12, 25, 31, 20, 18]
list_2 = [11, 9, 43, 22, 55]

for i in range(len(list_1)):
    print(list_1[i], end=' ')
    print(list_2[-(i + 1)])
