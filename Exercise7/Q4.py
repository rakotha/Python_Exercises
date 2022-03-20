# Question 4
inp = [10,23,45,78]
def printList():
    try:
        res = inp[5]
    except IndexError:
        print("Invalid index, try again.")
printList()