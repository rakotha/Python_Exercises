# Question 9
def StudentDetails(name = "None", **kwSubjects ):
    subjects = []
    for key,value in kwSubjects.items():
        if value > 60:
            subjects.append(key)

    print("Name: {} - Subjects:{}".format(name,set(subjects)))

StudentDetails("Brandon", Mathematics = 80, Physics = 58, Chemistry = 62, English = 72, Biology = 50)
