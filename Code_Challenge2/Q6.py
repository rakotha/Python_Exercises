# Question 6 Print all the prime numbers between the given range.
# start = 20
# end = 60
print("Prime numbers between 20 and 60 are: ", end='')
for i in range(20, 60):
    for j in range(2, int(i / 2) + 1):
        if i % j == 0:
            break
    else:
        print(i)
