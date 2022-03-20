# Question 8
def firstTenLetters(str1):
    try:
        strlen = len(str1)
        if strlen <10:
            raise ValueError;
        else:
            print(str1[:10])
    except ValueError:
        print("Oops! Too short string.")

str1= input("enter string: ")
firstTenLetters(str1)