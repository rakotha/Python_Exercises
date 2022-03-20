# Question 5 Write a Python program to print the first and the last second of the day.
import datetime
print("First Second : {}".format(datetime.time.min))
print("Last Second  : {}".format(datetime.time.max))
