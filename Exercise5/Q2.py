# Print the month and minutes from the datetime object given below.
from datetime import datetime

dob_time = datetime(1995, 6, 14, 10, 37, 50, 0)

print('Month: {}'.format(dob_time.month))
print('Minutes: {}'.format(dob_time.minute))