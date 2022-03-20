# Print the date, day name, and time in the format given below.
# Day_number-Month_number-Year - Day_name - Hours:Minutes:Seconds
# dob_time = datetime(1995, 6, 14, 10, 37, 50, 0)

from datetime import  datetime
from calendar import day_name
dob_time = datetime(1995, 6, 14, 10, 37, 50, 0)
weekday = dob_time.weekday()
weekday = day_name[weekday]
reqDate = datetime.strftime(dob_time.date(),"%d-%m-%Y")
print("{} - {} - {}".format(reqDate, weekday[:3], dob_time.time()))
