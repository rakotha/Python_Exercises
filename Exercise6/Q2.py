# Question 2
def AdditionSubtraction(num1, num2):
    print("(Addition, Substraction) : ({}, {})".format(num1+num2, num1-num2))

num1, num2 = input("Enter two numbers: ").split()
num1 = int(num1)
num2 = int(num2)
AdditionSubtraction(num1, num2)
