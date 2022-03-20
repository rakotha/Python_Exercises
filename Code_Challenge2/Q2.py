# Question 2 You have two dictionaries, with each of them containing several letters associated with certain values.
# num_1 = {'a' : 5, 's' : 7, 'x' : 11, 'm' : 12, 'o' : 8}
# num_2 = {'r' : 12, 'x' : 9, 'n' : 8, 'm' : 12, 'q' : 10}
# I want you to perform the below-mentioned operations on these dictionaries:
# 1. Print out the letters which are common to both these dictionaries.
# 2. Print out the (key, value) pair, which is common to both these dictionaries.
# 3. Print out all the letters which have occurred only once in these dictionaries.
# 4. Print out the letters in num_1 that are not present in num_2.
# 5. Print out a new dictionary num_3, which contains unique letters of num_1 from the previous output with their
#    associated values.
num_1 = {'a' : 5, 's' : 7, 'x' : 11, 'm' : 12, 'o' : 8}
num_2 = {'r' : 12, 'x' : 9, 'n' : 8, 'm' : 12, 'q' : 10}
res = {ele for ele in num_1 if ele in list(num_2.keys())}
print(res)
commonPair = dict(set(num_1.items()).intersection(num_2.items()))
print(commonPair)
OnlyOnce = [ele for ele in num_1 if ele not in list(num_2.keys())] + [ele for ele in num_2 if ele not in list(num_1.keys())]
print(set(OnlyOnce))
notInSecond = {ele for ele in num_1 if ele not in list(num_2.keys())}
print(notInSecond)
notInSecondPair = dict([[ele,key] for ele,key in num_1.items() if ele not in list(num_2.keys())] )
print(notInSecondPair)