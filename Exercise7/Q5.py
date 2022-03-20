# Question 5
lst1 = [10,23,45,78]
lst2 = [1,2,3]
def addLists(lst1,lst2):
    try:
        res = []
        for i in range(4):
            res.append(lst1[i] + lst2[i])
    except IndexError:
        print("Invalid index, try again.")
    except TypeError:
        print("Invalid type, try again.")

addLists(lst1,lst2)
