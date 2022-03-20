# Write a Python program to add 2 days and 10 hours to a given date.
# given_date = datetime(2016, 2, 27, 11, 30, 0)
from datetime import datetime,timedelta
given_date = datetime(2016, 2, 27, 11, 30, 0)
new_date = given_date + timedelta(days=2, hours=10)
print(new_date)
