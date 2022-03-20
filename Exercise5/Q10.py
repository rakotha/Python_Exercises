# Write a Python program to print the next 5 days from the date given below.
# given_date = datetime(2020, 10, 17)

from datetime import datetime,timedelta
date = datetime(2020, 10, 17)
for i in range(1,6):
    date += timedelta(days=1)
    print(date)