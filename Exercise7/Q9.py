# Question 9
while True:
    try:
        UserNum = input("Enter a Number: ")
        if UserNum.isdigit() == False:
            raise ValueError
        else:
            UserNum = int(UserNum)
            print(UserNum**2)
            break
    except ValueError:
        print("Enter a valid input.")
