# Question 6
from datetime import datetime
from calendar import day_name
given_date = datetime(2010, 6, 12)
try:
    weekday = given_date.weekday()
    weekday = day_name[weekday]
    print(weekday)
except:
    print('Oops! An error occurred.')
