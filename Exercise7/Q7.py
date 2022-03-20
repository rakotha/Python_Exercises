# Question 7
def checkString(str1):
    try:
        strLen = len(str1)
        if str1.isnumeric():
            raise TypeError
        print(str1[::-1])
    except TypeError:
        print("Check the string.")
    except:
        print("Something went wrong.")
str1 = input("Enter string:")
checkString(str1)