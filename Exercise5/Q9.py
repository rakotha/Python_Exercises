# Write a Python program to print yesterdays' date.
# Expected Output:

from datetime import date,timedelta
yesterday = date.today() - timedelta(days=1)
print("Yesterday: {}".format(yesterday))
