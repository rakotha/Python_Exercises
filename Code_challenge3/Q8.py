# Question 8
for num in range(100, 301):
    evenFlag = True
    ele = num
    while ele > 0:
        chekNum = int(ele % 10)
        if chekNum % 2 != 0:
            evenFlag = False
        ele = int(ele / 10)
    if evenFlag == True:
        print(num,end=', ')