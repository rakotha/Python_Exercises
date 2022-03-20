import copy
import math
a = 5
b = 2
c = 8
d = 7
l1 = [a, b, c, d]
l2 = []
p = []
d = 1
for i in l1[:-1]:
    l2 = copy.deepcopy(l1)
    l2.remove(i)
    p = l2
    s = 1
    for j in p:
        s = s*(i+j)
    if d == 1:
        d = s
    else:
        d = d/s
print(d*(math.prod(l1)))

