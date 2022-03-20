# Question 7 Here we have a list of 3 letters. I want you to concatenate this list with another list of numbers whose range varies from 1 to 3 (3 is included).
# letters_list = ['H', 'R', 'S']
letters_list = ['H', 'R', 'S']
newList = []
for i in range(1,4):
    for j in range(1,4):
        newList.append(letters_list[i-1]+str(j))
print(newList)

