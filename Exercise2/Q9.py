myList = ['Red', 'Blue', 'Orange', 'White', 'Black', 'Yellow']
l = []
for i in range(len(myList)):
    if i % 2!= 0:
        l.append(myList[i])
print(l)