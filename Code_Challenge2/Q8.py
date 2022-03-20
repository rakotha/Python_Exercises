# Question 8 Print all the numbers between 1 and 100 (both being included) that are multiples of 3 and 5 both.
answers = []
for i in range(1,101):
    if (i % 3 == 0 and i % 5 == 0):
        answers.append(i)
print(answers)
