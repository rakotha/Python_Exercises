# Question 1
def btwNum(num):
    if num > 4 and num < 11:
        print("{} is present between 5-10".format(num))
    else:
        print("{} is not present in between 5-10".format(num))

num = int(input("Enter your number: "))
btwNum(num)