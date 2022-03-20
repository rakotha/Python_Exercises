# Question 9
passenger_list = {'Ross' : 35,
    'Thomas': 42,
    'Rick' : 55,
    'Ericson' : 51,
    'Josh' : 45,
    'Lara' : 50,
    'Emma' : 38,
    'Lily' : 46,
    'Ron' : 41,
    'Michael' : 47,
    'Joanna' : 56,
    'Arthur' : 42}

Senior_Citizen = [senior for senior,age in passenger_list.items() if age > 45]
print(Senior_Citizen)