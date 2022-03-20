# Question 5
roll_numbers = {12, 7, 15, 23, 32, 30}
student_details = {12:'Judy', 30:'Shane', 23:'Aaron'}

print("completed Application: {}".format({ele for ele in student_details.keys()}))
print("Pending Application: {}".format({ele for ele in roll_numbers if ele not in student_details.keys()}))
