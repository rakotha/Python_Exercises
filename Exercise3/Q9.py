n = 5623
x = 0
while(n>0):
    y = n%10
    x = x*10 +y
    n = n//10
print(x)