# Question 10
class InvalidNumError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)

try:
    num = int(input("Enter number of results :"))
    for itr in range(num):
        result = int(input("enter marks{}".format(itr+1)))
        if result <0 or result > 100:
            raise(InvalidNumError("Invalid input error"))
        else:
            print("Results Processing.")

except InvalidNumError as err:
   print('Exception:',err.value)